import sounddevice as sd
import numpy as np
import torch
from coqui_tts import TTS
from resemblyzer import VoiceEncoder


class RealTimeConverter:
    """Capture microphone and convert voice in real-time."""
    def __init__(self, target_embed_path: str, chunk_size=2048, samplerate=16000):
        self.sr = samplerate
        self.chunk = chunk_size
        self.encoder = VoiceEncoder()
        self.target_emb = torch.load(target_embed_path)
        self.tts = TTS("tts_models/multilingual/multi-dataset_zh-tacotron2-DDC",
                      progress_bar=False, gpu=False)

    def callback(self, indata, frames, time, status):
        audio = indata[:, 0]
        converted = self.tts.tts_with_vc(audio, self.target_emb)
        sd.play(converted, self.sr)

    def start(self):
        with sd.InputStream(channels=1, callback=self.callback,
                            samplerate=self.sr, blocksize=self.chunk):
            print("Real-time conversion running. Press Ctrl+C to stop.")
            sd.sleep(int(1e8))
