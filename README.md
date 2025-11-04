# 1️⃣ Create a virtual environment
python -m venv .venv
.\.venv\Scripts\activate    # (Windows)
# or
source .venv/bin/activate   # (Linux/Mac)

# 2️⃣ Upgrade pip
python -m pip install --upgrade pip

# 3️⃣ Install all requirements
pip install -r requirements.txt

# 4️⃣ Install ffmpeg (required for Whisper audio processing)
# Windows (choco)
choco install ffmpeg
# Linux
sudo apt install ffmpeg

only versions >=3.10,<3.14 are supported

Must Download https://ollama.com/download
