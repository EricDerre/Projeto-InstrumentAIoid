# Roda todos os benchmarks num cenario. Uso: .\rodar_tudo.ps1 com_jogo
param([string]$Cenario = "sem_jogo", [string]$Modelos = "qwen3:1.7b,llama3.2:3b,qwen3:4b-instruct")
$B = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $B
$env:PYTHONIOENCODING = 'utf-8'
# o Kokoro quebra no DirectML; forca CPU para ele (o YOLO escolhe o provedor sozinho)
$env:ONNX_PROVIDER = 'CPUExecutionProvider'
New-Item -ItemType Directory -Force resultados | Out-Null
# amostra GPU (uso, VRAM, temperatura) a cada 2 s enquanto os testes rodam
$amostrador = Start-Process nvidia-smi -ArgumentList "--query-gpu=timestamp,utilization.gpu,memory.used,temperature.gpu,power.draw,clocks.gr","--format=csv","-l","2","-f","$B\resultados\gpu_$Cenario.csv" -WindowStyle Hidden -PassThru
cmd /c ".venv\Scripts\python.exe bench_llm.py $Cenario $Modelos 2>&1" | Select-String '^\{'
cmd /c ".venv\Scripts\python.exe bench_voz.py $Cenario 2>&1" | Select-String '^\{'
cmd /c "applio\.venv\Scripts\python.exe bench_rvc.py gpu $Cenario 2>&1" | Select-String '^\{'
cmd /c "applio\.venv\Scripts\python.exe bench_rvc.py cpu $Cenario 2>&1" | Select-String '^\{'
cmd /c ".venv\Scripts\python.exe bench_visao.py $Cenario 2>&1" | Select-String '^\{'
Stop-Process -Id $amostrador.Id -Force
"FIM $Cenario"
