from transformers import AutoModelForCausalLM, AutoTokenizer, TextStreamer
import torch

# Caminho para seu modelo treinado
MODEL_PATH = "./modelo_sena"  # ajuste o path se necessário

tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH)
model = AutoModelForCausalLM.from_pretrained(
    MODEL_PATH,
    torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32,
    device_map="auto"  # usa GPU se disponível
)

def gerar_resposta(prompt):
    inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
    with torch.no_grad():
        outputs = model.generate(**inputs, max_new_tokens=128, streamer=TextStreamer(tokenizer))
    resposta = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return resposta[len(prompt):].strip()

if __name__ == "__main__":
    while True:
        prompt = input("Você: ")
        if prompt.lower() in ['sair', 'exit', 'quit']:
            break
        resposta = gerar_resposta(prompt)
        print("Sena:", resposta)