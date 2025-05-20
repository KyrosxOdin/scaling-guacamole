# scaling-guacamole

This repository contains a sample voice application demonstrating consent handling, voice enrollment, speaker diarization, and real-time voice conversion. The project files live in the `voice_app/` directory.

## Directory Structure

```
voice_app/
├── consent.py       - Handles user consent, privacy, and logging.
├── training.py      - Voice enrollment & cloning training pipeline.
├── diarization.py   - Speaker separation & labeling of pre-recorded video.
├── realtime.py      - Real-time microphone capture & voice conversion.
├── utils.py         - Common helper functions (audio I/O, logging, config).
├── main.py          - CLI entry point to select mode: enroll, diarize, realtime.
└── requirements.txt - Python dependencies
```

Install dependencies from `requirements.txt` and run `python main.py --help` inside `voice_app/` to see available commands.
