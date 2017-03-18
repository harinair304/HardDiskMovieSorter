import os
import json
import requests
from guessit import guessit

class Movie:

	def __init__(self,name,genre,imdbRating,plot):
		self.name = name
		self.genre = genre
		self.imdbRating = imdbRating
		self.plot = plot

url = "http://www.omdbapi.com/?t="

# loc = raw_input('Please enter the location where your movies are stored = > ')
# loc = '/media/hari/My Passport/movies'
# loc ="/media/hari/Expansion Drive/Movies/English/Movies/Movies/Horror"
# loc = '/media/hari/Expansion Drive/Movies/English/Movies/Horror'
loc='/media/hari/Expansion Drive/Movies/English/Movies/Horror'

movies =  os.listdir(loc)



# print len(movies)

# print movies[112]

# normalized_movie =  guessit('2012(1080p)')

# print normalized_movie

# response = requests.get(url)
# python_dictionary_values = json.loads(response.text)
# print response.text

# for i in movies:
	
# 	normalized_movie = guessit(i)
# 	with open('MovieInfo','w') as fp:
		# try:
		# 	fp.write(normalized_movie['title'])
		# except:
		# 	print normalized_movie

MovieList = []

# with open('MovieInfo','w') as fp:

for i in movies:

	try:
		normalized_movie = guessit(i)
		response = requests.get(url+normalized_movie['title'])
		movieInfo = json.loads(response.text)
		movieInstance = Movie(normalized_movie['title'],movieInfo['Genre'],movieInfo['imdbRating'],movieInfo['Plot'])
		MovieList.append(movieInstance)

		
			# fp.write(normalized_movie['title']+'\n')
	except:
		try:

			movieInstance = Movie(normalized_movie['title'],'N/A','N/A','N/A')
			MovieList.append(movieInstance)
		except: 
			print 'Sorry, Could not figure out that movie name. Moving on.'


genreSet = set()

for i in MovieList:

	genreList = i.genre.split(', ')
	genreSet |= set(genreList)


with open('MovieInfo','w') as fp :
	fp.write('###########  Welcome to your MovieInfo Doc #############\n\n\n\n')
	fp.write('Location: '+loc+' \n\n\n')
	fp.write('The genres in your movie set are\n\n')

	for i in genreSet:
		fp.write(i+'\n')


with open('MovieInfo','a') as fp :

	for i in genreSet :
		# print 'Sorry'
		fp.write('\n\n\n\n*****************'+i+'****************\n\n\n\n')

		for j in MovieList :

			if i in j.genre :
				fp.write(j.name+'   IMDB RATING:'+j.imdbRating.encode('utf-8')+'   Plot:'+j.plot.encode('utf-8')+'\n\n')




