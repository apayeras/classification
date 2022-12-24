from random import randint
import bisect 

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
	file = open(f'{lng}2.txt', "w+")
	for word in newContent:
		file.write(word)
	file.close()


for lng, count in lngs.items():
	file = open(f'/workspaces/AprAut/Practica1/data2/{lng}.txt')
	content = file.readlines()
	file.close()
	createFile(lng, content)




