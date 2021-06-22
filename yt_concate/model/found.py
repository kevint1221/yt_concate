

class Found:
    def __init__(self, youtubechannel, caption, time):
        self.youtubechannel = youtubechannel
        self.caption = caption
        self.time = time

    def __str__(self):
        return '<found>'

    def __repr__(self):
        return 'yt = ' + str(self.youtubechannel) + ' : ' + 'caption = ' + str(self.caption) + ' : ' + 'time = ' + str(self.time)
