import photos
import random

# get one foto from iphone/ipad/icloud
def get_foto():
	all_foto = photos.get_assets()		# get all foto type(list)
	one_random_foto = random.choice(all_foto)	# choice one random foto from list
	return one_random_foto.get_image()	# return foto as 'image' (import image)
