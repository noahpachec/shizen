# works with video files too

from faster_whisper import WhisperModel

model = WhisperModel(
    "small",
    device="cpu",
    compute_type="int8")

segments, info = model.transcribe(
    "audio.mov",
    language="ja"
)


for segment in segments:
    print(segment.text)