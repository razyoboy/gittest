class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def singmeasong(self):
        for line in self.lyrics:
            print(line)

summertime = Song(["Kimi no toriko ni natte shimaeba kitto", "Kono natsu wa jyujitsu suru no motto", "Mou modorenakutatte wasurenaide"])

summertime.singmeasong()