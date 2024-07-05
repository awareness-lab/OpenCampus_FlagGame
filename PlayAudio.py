import wave
import pyaudio

def play_wav(filename):
    wav_file = wave.open(filename, 'rb')
    p = pyaudio.PyAudio()
    stream = p.open(format=p.get_format_from_width(wav_file.getsampwidth()),
                    channels=wav_file.getnchannels(),
                    rate=wav_file.getframerate(),
                    output=True)

    data = wav_file.readframes(512)
    while data:
        stream.write(data)
        data = wav_file.readframes(512)

    stream.stop_stream()
    stream.close()
    p.terminate()

play_wav('DontDownRed.wav')
play_wav('DontDownWhite.wav')