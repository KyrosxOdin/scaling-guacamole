import os
from resemblyzer import VoiceEncoder, preprocess_wav
import torch

class VoiceEnrollment:
    """Enroll voices by extracting embeddings."""
    def __init__(self, save_dir="embeddings"):
        os.makedirs(save_dir, exist_ok=True)
        self.encoder = VoiceEncoder()
        self.save_dir = save_dir

    def enroll(self, audio_path: str, name: str):
        wav = preprocess_wav(audio_path)
        embed = self.encoder.embed_utterance(wav)
        torch.save(embed, os.path.join(self.save_dir, f"{name}.pt"))
        print(f"Saved embedding for {name}.")
