import streamlit as st
from pydub import AudioSegment
import io

def convert_to_wav(audio_file):
    try:
        sound = AudioSegment.from_mp3(audio_file)
        buffer = io.BytesIO()
        sound.export(buffer, format="wav")
        buffer.seek(0)
        return buffer
    except Exception as e:
        st.error(f"An error occurred: {str(e)}. This format may require external dependencies not available in this environment.")

def main():
    st.title('Audio Converter')
    audio_file = st.file_uploader("Upload MP3 file", type=['mp3'])

    if audio_file is not None:
        wav_buffer = convert_to_wav(audio_file)
        if wav_buffer is not None:
            st.audio(wav_buffer, format='audio/wav')

if __name__ == "__main__":
    main()
