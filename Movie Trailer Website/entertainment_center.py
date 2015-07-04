#Import libraries
import fresh_tomatoes
import media

#Toy Story Movie
toy_story = media.Movie("Toy Story","A strory of a boy and his toys that come to life",
	"http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
	"https://www.youtube.com/watch?v=W_PUOogoFsk")
#print (toy_story.storyline)

#Avatar Movie
avatar = media.Movie("Avatar",
	"A marine on an alien planet",
	"http://www.mubis.es/media/covers/1090/1124/avatar-edicion-extendida-coleccionistas-portada-original.jpg",
	"https://www.youtube.com/watch?v=cRdxXPV9GNQ")
#print avatar.storyline
#avatar.show_trailer()
movies = [toy_story, avatar]

#Open Movies
print fresh_tomatoes.open_movies_page(movies)