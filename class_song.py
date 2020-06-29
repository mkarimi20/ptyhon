class songs:
    def __init__(self, lyrics):
        self.lyrics = lyrics
    
    def sing_me_a_song(self):
        for sing_me_a_song in self.lyrics:
            print(sing_me_a_song)
    
Song = songs(["May god bless you, ", "Have a sunshine on you,","Happy Birthday to you !"])
print(Song.sing_me_a_song())