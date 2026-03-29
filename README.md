# 🩺 My AI Doctor – Multimodal Healthcare Assistant

My AI Doctor is a multimodal AI-powered healthcare assistant that simulates a preliminary doctor–patient interaction using voice input, image analysis, and large language model reasoning. The system captures patient symptoms through speech, analyzes visual cues from images, processes the information using an AI model, and generates natural voice responses.

This project demonstrates end-to-end integration of AI APIs, speech processing, and backend orchestration to create an interactive healthcare support system.

## 🚀 Features
- 🎤 **Speech-to-Text Input** - Captures patient symptoms using microphone input with SpeechRecognition and PyAudio.
- 🧠 **AI Medical Reasoning** - Uses Groq LLM API to analyze symptoms and visual inputs and generate preliminary insights.
- 🖼 **Image-Based Health Analysis** - Processes facial images to detect potential visible conditions.
- 🔊 **Text-to-Speech Response** - Converts AI-generated responses into natural voice using gTTS or ElevenLabs.
- ⚡ **End-to-End Pipeline** - Voice → AI Analysis → Voice Response interaction pipeline.
  ## Images
**Patient Audio Recording** 

![Alt img](https://github.com/shivam15102005/My-AI-Doctor/blob/main/Patient%20Audio.png)


 # 🏗 System Architecture
 ```
 Patient Voice Input + Image Upload
            │
            ▼
Speech Recognition (SpeechRecognition + PyAudio)
            │
            ▼
Image Encoding & Processing (Base64 / Vision Input)
            │
            ▼
AI Reasoning Engine (Groq Vision LLM)
            │
            ▼
Response Generation
            │
            ▼
Text-to-Speech (gTTS / ElevenLabs)
            │
            ▼
Audio Response to User
```
## 🛠 Tech Stack

**Languages**
- Python
  
**Libraries & Tools**
- SpeechRecognition
- PyAudio
- gTTS
- ElevenLabs API
- Groq API
- Pydub
- FFmpeg
  
**Concepts Used**
- Multimodal AI systems
- Speech processing
- API integration
- Backend orchestration
- Conversational AI pipelines
  
## 📂 Project Structure
```
AI_Doctor
│
├── voice_of_patient.py        # Records patient voice input
├── brain_of_the_doctor.py     # AI reasoning using Groq LLM
├── voice_of_doctor.py         # Converts AI response to speech
│
├── audio/                     # Generated audio responses
├── images/                    # Sample medical images
│
├── requirements.txt
└── README.md
```
## ⚙️ Installation
**1️⃣ Clone the repository**
```
git clone https://github.com/shivam15102005/My-AI-Doctor.git
cd My Doctor AI
```
## 2️⃣ Install dependencies
```
pip install -r requirements.txt
```
## 3️⃣ Install system dependencies
- Install FFmpeg for audio processing.
- For Windows:
  ```
  winget install ffmpeg
  ```
## 🔑 Environment Variables
- Create a .env file in the root directory.
```
GROQ_API_KEY=your_groq_api_key
ELEVENLABS_API_KEY=your_elevenlabs_api_key
```
## ▶️ Running the Project
- Run the voice interaction pipeline:
```
python voice_of_patient.py
```
- or run individual modules:
```
python brain_of_the_doctor.py
python voice_of_doctor.py
```
## 💡 Real-World Applications
This system demonstrates how multimodal AI assistants can support healthcare by:
- providing preliminary symptom analysis
- enabling voice-based medical interaction
- assisting in remote health guidance
- supporting telemedicine and accessibility

## 📜 License
This project is developed for educational and research purposes only and should not be used for real medical diagnosis.

