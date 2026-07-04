"""
Voice cloning layer for Urdu TTS, using OpenVoice's zero-shot tone-color
conversion (no training needed — just a short reference clip).

This takes audio that already has correct Urdu pronunciation (produced by
tts_urdu.py / MMS-TTS) and reshapes its timbre to match a reference voice
sample you provide.

Note: the underlying OpenVoice model is for personal/research use only
(non-commercial license), and MyShell (its creator) can detect audio it
generated even without an audible watermark.
"""

from openvoice_cli.__main__ import tune_one


def clone_voice(input_wav: str, reference_wav: str, output_wav: str, device: str = "cpu") -> str:
    """
    Reshape the voice in `input_wav` to match the voice in `reference_wav`.

    Args:
        input_wav: path to the base TTS-generated audio (correct pronunciation)
        reference_wav: path to a clean ~6-20 second sample of the target voice
        output_wav: where to save the final cloned-voice audio
        device: 'cpu' or 'cuda:0'

    Returns:
        The output path.
    """
    tune_one(
        input_file=input_wav,
        ref_file=reference_wav,
        output_file=output_wav,
        device=device,
    )
    return output_wav
