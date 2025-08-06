from flask import Flask, request, jsonify
import os
import tempfile
import whisper

app = Flask(__name__)
model = whisper.load_model("base")

@app.route("/transcribe", methods=["POST"])
def transcribe_audio():
    if "file" not in request.files:
        return jsonify({"error": "No file provided"}), 400

    file = request.files["file"]

    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as temp_audio:
        file.save(temp_audio.name)
        temp_audio_path = temp_audio.name

    try:
        result = model.transcribe(temp_audio_path)
        transcript = result["text"]
    except Exception as e:
        transcript = f"Error during transcription: {str(e)}"
    finally:
        # Elimina el archivo temporal
        os.remove(temp_audio_path)

    return jsonify({"transcript": transcript})
