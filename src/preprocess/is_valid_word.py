from nltk.corpus import wordnet
def word(w):
	if not wordnet.synsets(w):
		return 0
	else:
		return 1
