from random import randint
import bisect 
import os

lngs = {
	'de' : True,
	'en' : True,
	'es' : True,
	'fr': True,
	'ca' : True
}


def createFile(lng, content):

	count = len(content)
	newContent = []
	for _ in range(1000):
		word_index = randint(0, count-1)
		word = content[word_index]
		bisect.insort(newContent, word) 

	print(len(newContent))
	file = open(f'{lng}.txt', "w+")
	for word in newContent:
		file.write(word)
	file.close()

path = os.path.dirname(__file__)

for lng, count in lngs.items():
	file = open(f'{path}/{lng}.txt')
	content = file.readlines()
	file.close()
	createFile(lng, content)




