class Song(object):

	def __init__(self, lyrics):
		self.lyrics = lyrics

	def sing_me_a_song(self):
		for line in self.lyrics:
			print line
	def prompt_a_song(self):
		print self.lyrics[0]

happy_bday = Song(["Happy Birthday to you.",
	"I don't want to get sued.",
	"So I'll stop right there."])

bulls_on_parade = Song(["They rally around the family",
	"With pockets full of shells"])

i_will_be_back = Song(["I'll be back I swear",
	"I believe I can",
	"Oh darling Don't scare I'll be back"])
print 
print "--># Print the happy_bday:"
happy_bday.sing_me_a_song()
print 
print "--># Print the bulls_on_parade:"
bulls_on_parade.sing_me_a_song()
print 
print "--># Print the whole song:"
i_will_be_back.sing_me_a_song()
print 
print "--># Print only the 1st line of a song:"
i_will_be_back.prompt_a_song()
print 