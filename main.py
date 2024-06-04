from pydub import AudioSegment

originBgm = AudioSegment.from_mp3("input/bgm.mp3")
bgm = originBgm.apply_gain(-30.0 - originBgm.dBFS)
voice = AudioSegment.from_mp3("input/voice.mp3")

output = bgm.overlay(voice, position=2000)
output.export("output/result.mp3", format="mp3")