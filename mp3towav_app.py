import streamlit as st
from pydub import AudioSegment
import io

def convert_to_wav(audio_file):
    sound = AudioSegment.from_mp3(audio_file)
    buffer = io.BytesIO()
    sound.export(buffer, format="wav")
    return buffer

def main():
    st.title('MP3 to WAV Converter')
    audio_file = st.file_uploader("Upload MP3 file", type=['mp3'])

    if audio_file is not None:
        st.audio(audio_file, format='audio/mp3', start_time=0)
        if st.button('Convert to WAV'):
            buffer = convert_to_wav(audio_file)
            buffer.seek(0)
            st.download_button(label="Download WAV",
                               data=buffer,
                               file_name="converted.wav",
                               mime="audio/wav")

if __name__ == "__main__":
    main()
