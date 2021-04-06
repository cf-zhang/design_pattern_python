class MediaPlayer:
    def play(self, audio_type: 'str', file_name: 'str'):
        pass


class AdvancedMediaPlayer:
    def play_vlc(self, file_name: 'str'):
        pass

    def play_mp4(self, file_name: 'str'):
        pass


class VlcPlayer(AdvancedMediaPlayer):
    def play_vlc(self, file_name: 'str'):
        print("play vlc file, name: " + file_name)

    def play_mp4(self, file_name: 'str'):
        pass


class Mp4Player(AdvancedMediaPlayer):
    def play_vlc(self, file_name: 'str'):
        pass

    def play_mp4(self, file_name: 'str'):
        print("play mp4 file, name: " + file_name)


class MediaAdapter(MediaPlayer):
    def __init__(self, audio_type: 'str'):
        if audio_type == 'vlc':
            self.advanced_player = VlcPlayer()
        elif audio_type == 'mp4':
            self.advanced_player = Mp4Player()

    def play(self, audio_type: 'str', file_name: 'str'):
        if audio_type == 'vlc':
            self.advanced_player.play_vlc(file_name)
        elif audio_type == 'mp4':
            self.advanced_player.play_mp4(file_name)


class AudioPlayer(MediaPlayer):
    def play(self, audio_type: 'str', file_name: 'str'):
        if audio_type == 'mp3':
            print("play mp3 file, name "+ file_name)
        elif audio_type == 'mp4' or audio_type == 'vlc':
            media_adapter = MediaAdapter(audio_type)
            media_adapter.play(audio_type, file_name)
        else:
            print("not support.")


audio_player = AudioPlayer()
audio_player.play('mp3', 'aaaaaa')
audio_player.play('vlc', 'bbbbbb')
audio_player.play('mp4', 'cccccc')


