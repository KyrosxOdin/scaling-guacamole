from pyannote.audio import Pipeline
import torch
import os
from resemblyzer import VoiceEncoder


def diarize_video(video_path: str, output_rttm: str="diarization.rttm"):
    """Use pretrained pyannote.audio speaker diarization pipeline."""
    pipeline = Pipeline.from_pretrained("pyannote/speaker-diarization")
    diarization = pipeline(video_path)
    diarization.write_rttm(output_rttm)
    print(f"Diarization RTTM saved to {output_rttm}.")


class SpeakerLabeler:
    def __init__(self, embed_dir="embeddings"):
        self.encoder = VoiceEncoder()
        self.embeds = {
            name: torch.load(os.path.join(embed_dir, f))
            for f in os.listdir(embed_dir) if f.endswith('.pt')
            for name in [os.path.splitext(f)[0]]
        }

    def label(self, wav_segment):
        emb = self.encoder.embed_utterance(wav_segment)
        sims = {name: torch.cosine_similarity(emb, target, dim=0).item()
                for name, target in self.embeds.items()}
        return max(sims, key=sims.get)
