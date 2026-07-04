"""
End-to-end local Urdu TTS with voice cloning (ElevenLabs-style, but local).

Pipeline:
    1. MMS-TTS-urd turns your Urdu text into correctly-pronounced speech
       (using a generic base voice).
    2. OpenVoice's tone-color converter reshapes that audio to match a
       reference voice clip you provide (zero-shot, no training).

Usage:
    python generate.py "آپ کیسے ہیں؟" --voice my_voice_sample.wav --out final.wav

Requirements:
    - A reference voice clip: 6-20 seconds, one speaker, minimal background
      noise/music, ideally recorded in the same language family (Urdu/Hindi)
      but any clear speech sample will work reasonably.
"""

import argparse
import os
import sys
import tempfile

from tts_urdu import synthesize
from clone_voice import clone_voice


def generate(text: str, reference_wav: str, output_wav: str, device: str = "cpu") -> str:
    # Step 1: correct Urdu pronunciation, generic voice
    with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as tmp:
        base_wav = tmp.name
    synthesize(text, base_wav, device=device)

    # Step 2: clone the timbre onto the reference voice
    clone_voice(base_wav, reference_wav, output_wav, device=device)

    os.remove(base_wav)
    return output_wav


def main():
    parser = argparse.ArgumentParser(description="Local Urdu TTS with voice cloning")
    parser.add_argument("text", nargs="?", help="Urdu text to synthesize")
    parser.add_argument("--file", help="Path to a .txt file with Urdu text instead of inline text")
    parser.add_argument("--voice", required=True, help="Path to a reference voice sample (.wav/.mp3)")
    parser.add_argument("--out", default="output.wav", help="Output path (default: output.wav)")
    parser.add_argument("--device", default="cpu", help="'cpu' or 'cuda:0'")
    args = parser.parse_args()

    if args.file:
        with open(args.file, "r", encoding="utf-8") as f:
            text = f.read().strip()
    elif args.text:
        text = args.text
    else:
        print("Error: provide text as an argument or use --file", file=sys.stderr)
        sys.exit(1)

    path = generate(text, args.voice, args.out, device=args.device)
    print(f"Saved cloned-voice audio to: {path}")


if __name__ == "__main__":
    main()
