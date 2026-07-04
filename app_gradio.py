"""
Local web UI for Urdu Text-to-Speech with voice cloning.

Run:
    python app_gradio.py

Then open the printed local URL (e.g. http://127.0.0.1:7860) in your browser.
Upload a short (6-20s) clean voice sample, type Urdu text, and generate
speech in that cloned voice -- fully offline after models are cached.
"""

import tempfile

import gradio as gr

from generate import generate


def tts(text, voice_sample):
    if not text or not text.strip():
        return None
    if voice_sample is None:
        return None
    out_tmp = tempfile.NamedTemporaryFile(suffix=".wav", delete=False)
    generate(text, voice_sample, out_tmp.name)
    return out_tmp.name


with gr.Blocks(title="Local Urdu Voice Cloning TTS") as demo:
    gr.Markdown("# Local Urdu Text-to-Speech (Voice Cloning)")
    gr.Markdown(
        "Upload a clean 6-20 second voice sample, type Urdu text, and generate "
        "speech in that voice. Runs fully offline after the first model download.\n\n"
        "*Note: voice cloning here uses OpenVoice, which is licensed for "
        "personal/research use only (non-commercial).*"
    )

    with gr.Row():
        with gr.Column():
            voice_sample = gr.Audio(
                label="Reference voice sample (6-20s, clean speech)",
                type="filepath",
            )
            text = gr.Textbox(
                label="اردو متن (Urdu text)",
                placeholder="یہاں اردو میں کچھ لکھیں...",
                lines=4,
                rtl=True,
            )
            btn = gr.Button("Generate", variant="primary")
        with gr.Column():
            output = gr.Audio(label="نتیجہ (Cloned voice output)")

    btn.click(fn=tts, inputs=[text, voice_sample], outputs=output)

if __name__ == "__main__":
    demo.launch()
