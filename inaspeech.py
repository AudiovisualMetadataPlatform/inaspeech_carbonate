#!/usr/bin/env python3
#
# This is a one-file-only version of the ina_speech_segmenter.py that
# is installed in the container.  It requires both input and output
# filenames to make it easier to plug into different runtimes.
#
import argparse
from inaSpeechSegmenter import Segmenter

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-g", "--detect_gender", type=bool, default=False, help="Enable gender detection")
    parser.add_argument("-d", "--vad_engine", choices=['sm', 'smn'], default='smn', help="Voice activity detection:  smn (default) or sm")
    parser.add_argument("-b", "--ffmpeg_binary", default='ffmpeg', help="FFMPEG binary")
    parser.add_argument("input", help="Input file")
    parser.add_argument("output", help="Output file")
    args = parser.parse_args()

    seg = Segmenter(vad_engine=args.vad_engine, detect_gender=args.detect_gender, ffmpeg=args.ffmpeg_binary)
    seg.batch_process([args.input], [args.output], verbose=True)


if __name__ == "__main__":
    main()