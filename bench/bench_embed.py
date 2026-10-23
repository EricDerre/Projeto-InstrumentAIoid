"""Embeddings para a memoria da persona (RAG): RAM, latencia na CPU e acerto simples em portugues.
Uso: python bench_embed.py modelo1,modelo2
"""
import json, sys, time, pathlib, statistics as st
import numpy as np, psutil, requests
B = pathlib.Path(__file__).resolve().parent; URL = "http://127.0.0.1:11434"
MEMORIAS = ["O Eric toca guitarra e gosta de rock dos anos 80.", "O jogo favorito do Eric e Warcraft III.",
            "O Eric estuda e escreveu um TCC sobre agentes de teste com IA local.", "A Astolfo nao gosta de perder no Mario Kart.",
            "O Eric prefere respostas curtas e em portugues.", "O notebook do Eric tem uma GTX 1650 de 4 GB.",
            "O Eric quer que a Astolfo cante musicas com voz propria feita no RVC.", "O aniversario do Eric e em marco.",
            "O Eric usa o REAPER e o Cubase para gravar.", "O gato do Eric se chama Pixel."]
PERGUNTAS = [("que instrumento eu toco?", 0), ("qual jogo eu mais curto?", 1), ("sobre o que foi meu trabalho de conclusao?", 2),
             ("como e minha placa de video?", 5), ("qual o nome do meu bichinho?", 9), ("onde eu gravo minhas musicas?", 8)]
def emb(m, textos):
    return np.array(requests.post(f"{URL}/api/embed", json={"model": m, "input": textos, "keep_alive": "5m",
                                                           "options": {"num_gpu": 0}}, timeout=300).json()["embeddings"])
for m in sys.argv[1].split(","):
    requests.post(f"{URL}/api/generate", json={"model": m, "keep_alive": 0}); time.sleep(2)
    emb(m, ["aquecimento"])
    t = time.time(); D = emb(m, MEMORIAS); t_doc = (time.time() - t) / len(MEMORIAS)
    tt, acertos = [], 0
    for q, alvo in PERGUNTAS:
        t = time.time(); v = emb(m, [q])[0]; tt.append(time.time() - t)
        sims = D @ v / (np.linalg.norm(D, axis=1) * np.linalg.norm(v)); acertos += int(np.argmax(sims) == alvo)
    p = max((x for x in psutil.process_iter(["name"]) if (x.info["name"] or "").lower() == "llama-server.exe"), key=lambda x: x.memory_info().rss)
    i = p.memory_full_info()
    reg = {"peca": f"embed {m}", "dim": int(D.shape[1]), "ms_por_memoria": round(t_doc * 1000, 1), "ms_por_consulta": round(st.median(tt) * 1000, 1),
           "acerto_top1": f"{acertos}/{len(PERGUNTAS)}", "privada_mb": round(i.private / 2**20), "working_set_mb": round(i.rss / 2**20)}
    print(json.dumps(reg, ensure_ascii=False))
    with open(B / "resultados" / "ram.jsonl", "a", encoding="utf-8") as f: f.write(json.dumps(reg, ensure_ascii=False) + "\n")
    requests.post(f"{URL}/api/generate", json={"model": m, "keep_alive": 0})
