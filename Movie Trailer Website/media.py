#Import library
import webbrowser

#Class Movies
class  Movie():
	valied_ratings = ["G","PG","PG-13","R"]
	"""docstring for  Movie"""
	def __init__(self, movie_title,movie_storyline,poster_image, trailer_youtube):
		self.title = movie_title
		self.storyline = movie_storyline
		self.poster_image_url = poster_image
		self.trailer_youtube_url = trailer_youtube
	#Function show the trailer movies
	def show_trailer(self):
		webbrowser.open(self.trailer_youtube_url)
