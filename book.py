#######################
#   Recommend Books   #
#     For IRC BOT     #
#                     #
#    By: Evan Seils   #
#######################
import random

books = ["To Kill a Mockingbird by Harper Lee","1984 by George Orwell","The Catcher in the Rye by J. D. Salinger"]

def newBook():
	length = len(books)
	number = random.randrange(0,length)
	return books[number]