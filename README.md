# 🩺 My AI Doctor – Multimodal Healthcare Assistant

My AI Doctor is a multimodal AI-powered healthcare assistant that simulates a preliminary doctor–patient interaction using voice input, image analysis, and large language model reasoning. The system captures patient symptoms through speech, analyzes visual cues from images, processes the information using an AI model, and generates natural voice responses.

This project demonstrates end-to-end integration of AI APIs, speech processing, and backend orchestration to create an interactive healthcare support system.

## 🚀 Features
- 🎤 **Speech-to-Text Input** - Captures patient symptoms using microphone input with SpeechRecognition and PyAudio.
- 🧠 **AI Medical Reasoning** - Uses Groq LLM API to analyze symptoms and visual inputs and generate preliminary insights.
- 🖼 **Image-Based Health Analysis** - Processes facial images to detect potential visible conditions.
- 🔊 Text-to-Speech Response
Converts AI-generated responses into natural voice using gTTS or ElevenLabs.
- ⚡ End-to-End Pipeline
Voice → AI Analysis → Voice Response interaction pipeline.
