class Game:
    def initialize(self):
        pass

    def start_play(self):
        pass

    def end_play(self):
        pass

    def play(self):
        self.initialize()
        self.start_play()
        self.end_play()

class Cricket(Game)        :
    def end_play(self):
        print('cricket game finished')

    def initialize(self):
        print('cricket game initialized start playing')

    def start_play(self):
        print('cricket gama started, enjoy the game')

class  FootBall(Game):
    def end_play(self):
        print('football game finished')

    def initialize(self):
        print('football game initialized start playing')

    def start_play(self):
        print('football game started, enjoy the game')

game = Cricket()
game.play()
print()
game = FootBall()
game.play()
