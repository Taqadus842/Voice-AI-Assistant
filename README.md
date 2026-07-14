# Voice AI Assistant

A Python-based Voice AI Assistant that converts text into natural-sounding speech using AI-powered Text-to-Speech (TTS) models. The project provides an interactive Gradio web interface for generating speech and includes voice cloning capabilities for creating personalized AI voices.

## Features

* AI-powered Text-to-Speech (TTS)
* Voice cloning support
* Interactive Gradio web interface
* Generate high-quality speech from text
* Modular project structure
* Easy to customize and extend
* Python-based implementation

## Project Structure

```
Voice-AI-Assistant/
│
├── app_gradio.py        # Gradio web interface
├── clone_voice.py       # Voice cloning functionality
├── generate.py          # Speech generation logic
├── tts_ursu.py          # Text-to-Speech implementation
├── requirements.py      # Project dependencies
└── README.md
```

## Technologies Used

* Python
* Gradio
* AI Text-to-Speech (TTS)
* Voice Cloning
* Deep Learning

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/Taqadus842/Voice-AI-Assistant.git
cd Voice-AI-Assistant
```

### 2. Create a virtual environment (Recommended)

Windows

```bash
python -m venv venv
venv\Scripts\activate
```

Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

If your dependency file is named `requirements.py`, rename it to `requirements.txt` for standard Python package management.

```bash
pip install -r requirements.txt
```

## Running the Application

Start the Gradio application:

```bash
python app_gradio.py
```

After launching, Gradio will provide a local URL similar to:

```
http://127.0.0.1:7860
```

Open the URL in your browser to interact with the Voice AI Assistant.

## How It Works

1. Enter the text you want to convert into speech.
2. Select or clone a voice.
3. Generate natural-sounding audio.
4. Listen to or save the generated speech.

## Project Modules

### app_gradio.py

Provides the interactive Gradio user interface.

### clone_voice.py

Implements voice cloning functionality.

### generate.py

Handles speech generation and inference.

### tts_ursu.py

Contains the Text-to-Speech pipeline and model integration.

## Future Improvements

* Multiple language support
* Emotion-aware speech synthesis
* Speaker management
* Audio download functionality
* Streaming audio generation
* REST API integration
* Docker support
* GPU optimization

## Author

Ume Taqadus

GitHub: https://github.com/Taqadus842

LinkedIn: https://www.linkedin.com/in/umetaqadus/

## License

This project is intended for educational and research purposes.
