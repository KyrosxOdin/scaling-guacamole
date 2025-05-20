import argparse
from consent import ConsentManager
from training import VoiceEnrollment
from diarization import diarize_video
from realtime import RealTimeConverter


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Voice App CLI")
    sub = parser.add_subparsers(dest='cmd')

    sub_enroll = sub.add_parser('enroll')
    sub_enroll.add_argument('audio', help='Path to WAV for enrollment')
    sub_enroll.add_argument('name', help='Speaker name')

    sub_diarize = sub.add_parser('diarize')
    sub_diarize.add_argument('video', help='Path to video file')

    sub_realtime = sub.add_parser('realtime')
    sub_realtime.add_argument('name', help='Enrolled speaker name')

    args = parser.parse_args()
    cm = ConsentManager()

    if args.cmd == 'enroll':
        cm.request_consent(args.name)
        ve = VoiceEnrollment()
        ve.enroll(args.audio, args.name)

    elif args.cmd == 'diarize':
        diarize_video(args.video)

    elif args.cmd == 'realtime':
        target_path = f'embeddings/{args.name}.pt'
        cm.request_consent(args.name)
        rtc = RealTimeConverter(target_path)
        rtc.start()
