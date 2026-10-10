# works with video files too

from faster_whisper import WhisperModel

def transcribe_media(file):


    model = WhisperModel(
        "small",
        device="cpu",
        compute_type="int8")

    segments, info = model.transcribe(
        file,
        language="ja"
    )


    full_text = ""
    for segment in segments:
        full_text += segment.text

    return full_text

