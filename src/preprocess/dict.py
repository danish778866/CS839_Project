# n v a s r
from nltk.corpus import wordnet as wn
def tag_word(w):
	pos_l = set()
	tags = [0,0,0,0,0]
	for tmp in wn.synsets(w):
		if tmp.name().split('.')[0] == w:
			pos_l.add(tmp.pos())
	for val in pos_l:
		if val  == 'n':
			tags[0]=1;
		elif val  == 'v':
			tags[1]=1;
		elif val ==  'a':
			tags[2]=1;
		elif val  ==  's':
			tags[3]=1;
		elif val == 'r':
			tags[4]=1;
		else:
			print(w, val)
	return tags;
