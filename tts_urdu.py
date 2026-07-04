"""
Urdu Text-to-Speech (offline, local) using Meta's MMS-TTS model.

Usage:
    python tts_urdu.py "آپ کیسے ہیں؟" output.wav
    python tts_urdu.py --file input.txt output.wav

First run will download the model (~150MB) from Hugging Face and cache it
locally (~/.cache/huggingface). After that, everything runs fully offline.
"""

import argparse
import sys

import torch
import scipy.io.wavfile
from transformers import VitsModel, AutoTokenizer

MODEL_NAME = "facebook/mms-tts-urd-script_arabic"

_model = None
_tokenizer = None


def load_model(device: str = "cpu"):
    """Load and cache the model + tokenizer (only happens once per process)."""
    global _model, _tokenizer
    if _model is None:
        print(f"Loading model '{MODEL_NAME}' (first time may take a while)...")
        _tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
        _model = VitsModel.from_pretrained(MODEL_NAME).to(device)
        _model.eval()
    return _model, _tokenizer


def synthesize(text: str, output_path: str, device: str = "cpu") -> str:
    """Convert Urdu text to a .wav file. Returns the output path."""
    model, tokenizer = load_model(device)

    inputs = tokenizer(text, return_tensors="pt").to(device)

    with torch.no_grad():
        output = model(**inputs).waveform

    waveform = output.squeeze().cpu().numpy()
    sample_rate = model.config.sampling_rate

    scipy.io.wavfile.write(output_path, rate=sample_rate, data=waveform)
    return output_path


def main():
    parser = argparse.ArgumentParser(description="Local Urdu Text-to-Speech")
    parser.add_argument("text", nargs="?", help="Urdu text to synthesize")
    parser.add_argument("--file", help="Path to a .txt file containing Urdu text")
    parser.add_argument("output", help="Path to save the output .wav file")
    parser.add_argument(
        "--device",
        default="cuda" if torch.cuda.is_available() else "cpu",
        help="Device to run on: 'cpu' or 'cuda' (default: auto-detect)",
    )
    args = parser.parse_args()

    if args.file:
        with open(args.file, "r", encoding="utf-8") as f:
            text = f.read().strip()
    elif args.text:
        text = args.text
    else:
        print("Error: provide text as an argument or use --file", file=sys.stderr)
        sys.exit(1)

    path = synthesize(text, args.output, device=args.device)
    print(f"Saved audio to: {path}")


if __name__ == "__main__":
    main()
