# if you dont use pipenv uncomment the following:
# from dotenv import load_dotenv
# load_dotenv()

#Step1a: Setup Text to Speech–TTS–model with gTTS

import os
from gtts import gTTS

def text_to_speech_with_gtts_old(input_text, output_filepath):
    language="en"

    audioobj= gTTS(
        text=input_text,
        lang=language,
        slow=False
    )
    audioobj.save(output_filepath)


input_text="Hi this is Shivam Kumar Gupta!"
#text_to_speech_with_gtts_old(input_text=input_text, output_filepath="gtts_testing.mp3")

#Step1b: Setup Text to Speech–TTS–model with ElevenLabs
# import os
# from elevenlabs.client import ElevenLabs


# def text_to_audio_elevenlabs_sdk(
#     text: str,
#     voice_id: str = "JBFqnCBsd6RMkjVDRZzb",
#     model_id: str = "eleven_multilingual_v2",
#     output_format: str = "mp3_44100_128",
#     output_dir: str = "audio",
#     api_key: str = None
# ) -> str:
#     """
#     Converts text to speech using ElevenLabs SDK and saves it to audio/ directory.

#     Returns:
#         str: Path to the saved audio file.
#     """
#     try:
#         api_key = api_key or os.getenv("ELEVENLABS_API_KEY")
#         if not api_key:
#             raise ValueError("ElevenLabs API key is required.")

#         # Initialize client
#         client = ElevenLabs(api_key=api_key)

#         # Get audio stream
#         audio_stream = client.text_to_speech.convert(
#             text=text,
#             voice_id=voice_id,
#             model_id=model_id,
#             output_format=output_format
#         )

#         # Create audio directory if it doesn't exist
#         os.makedirs(output_dir, exist_ok=True)

#         # Output file path
#         output_filepath = os.path.join(output_dir, "doctor_voice.mp3")

#         # Save audio stream to file
#         with open(output_filepath, "wb") as f:
#             for chunk in audio_stream:
#                 f.write(chunk)

#         print(f"Audio saved to: {output_filepath}")

#         return output_filepath

#     except Exception as e:
#         print(f"Error generating audio: {e}")
#         return None


# # Example usage
# if __name__ == "__main__":
#     text = "Hello Shivam, I am your AI doctor. How can I help you today?"

#     text_to_audio_elevenlabs_sdk(text)

# from gtts import gTTS

# tts = gTTS("Hello Shivam, your AI doctor is ready.")
# tts.save("doctor_voice.mp3")

#Step2: Use Model for Text output to Voice

import subprocess
import platform

def text_to_speech_with_gtts(input_text, output_filepath):
    language="en"

    audioobj= gTTS(
        text=input_text,
        lang=language,
        slow=False
    )
    audioobj.save(output_filepath)
    os_name = platform.system()
    try:
        if os_name == "Darwin":  # macOS
            subprocess.run(['afplay', output_filepath])
        elif os_name == "Windows": #Windows
            subprocess.run(["start", output_filepath], shell=True)
        elif os_name == "Linux":  # Linux
            subprocess.run(['aplay', output_filepath])  # Alternative: use 'mpg123' or 'ffplay'
        else:
            raise OSError("Unsupported operating system")
    except Exception as e:
        print(f"An error occurred while trying to play the audio: {e}")


input_text="Hi this is Shivam, autoplay testing!"
text_to_speech_with_gtts(input_text=input_text, output_filepath="gtts_testing_autoplay.mp3")
