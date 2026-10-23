# Prepara o ambiente do benchmark do InstrumentAIoid (gerado pelo Claude, 23/10/2026).
# Tudo fica dentro desta pasta bench\ : Python do uv, cache, venvs, Applio e modelos.
$ErrorActionPreference = 'Continue'
$B = Split-Path -Parent $MyInvocation.MyCommand.Path
$env:UV_PYTHON_INSTALL_DIR = "$B\python"
$env:UV_CACHE_DIR = "$B\uv-cache"
Set-Location $B
$log = "$B\setup.log"
$py = "$B\.venv\Scripts\python.exe"

"== venv principal ==" | Out-File $log
cmd /c "py -m uv venv --python 3.11 .venv 2>&1" | Out-File -Append $log
cmd /c "py -m uv pip install --python $py torch --index-url https://download.pytorch.org/whl/cu126 2>&1" | Select-Object -Last 3 | Out-File -Append $log
cmd /c "py -m uv pip install --python $py ultralytics onnx onnxruntime-directml faster-whisper kokoro-onnx piper-tts dxcam pynvml psutil requests gdown soundfile numpy 2>&1" | Select-Object -Last 5 | Out-File -Append $log
"== venv principal FIM ==" | Out-File -Append $log

"== applio ==" | Out-File -Append $log
if (-not (Test-Path applio)) { cmd /c "git clone --depth 1 https://github.com/IAHispano/Applio applio 2>&1" | Out-File -Append $log }
Set-Location applio
cmd /c "py -m uv venv --python 3.11 .venv 2>&1" | Out-File -Append $log
$apy = "$B\applio\.venv\Scripts\python.exe"
(Get-Content requirements-engine.txt) | Where-Object { $_ -notmatch '^(torch|torchaudio)==' } | Set-Content req-sem-torch.txt
cmd /c "py -m uv pip install --python $apy torch==2.11.0 torchaudio==2.11.0 --index-url https://download.pytorch.org/whl/cu126 2>&1" | Select-Object -Last 3 | Out-File -Append $log
cmd /c "py -m uv pip install --python $apy -r req-sem-torch.txt gdown 2>&1" | Select-Object -Last 3 | Out-File -Append $log
cmd /c "$apy core.py prerequisites --models --no-exe 2>&1" | Select-Object -Last 5 | Out-File -Append $log
"== modelo astolfoV3 ==" | Out-File -Append $log
New-Item -ItemType Directory -Force "$B\modelos\rvc" | Out-Null
cmd /c "$apy -m gdown 1xhAcacM2h5HZ1YBJ3Rmku8APaLlkfrph -O $B\modelos\rvc\astolfoV3_300e_7800s.pth 2>&1" | Select-Object -Last 2 | Out-File -Append $log
cmd /c "$apy -m gdown 1m71m91Yoj0l4vCfQ26Xv3WU4_kbpLT8X -O $B\modelos\rvc\astolfoV3.index 2>&1" | Select-Object -Last 2 | Out-File -Append $log
"== FIM ==" | Out-File -Append $log
