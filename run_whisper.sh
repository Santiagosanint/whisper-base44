#!/bin/bash
# Activar entorno virtual si lo usas (opcional)
# source venv/bin/activate

# Inicia whisper.cpp (asume que el binario está en ./main)
./main -m models/ggml-base.en.bin -f audio/audio.wav -otxt &

# Inicia el servidor Flask
python3 server.py
