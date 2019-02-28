#determine whether the string contains apostrophe at any position (not end)
def has_apos(w):
	result = w.find("'")
	if result != -1:
		return 1
	else:
		return 0

