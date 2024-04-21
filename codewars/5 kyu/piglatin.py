def pig_it(text):
	text = text + " "
	words = []
	words_final = []
	a = 0
	b = 1
	for x in text:
		if(x == " "):
			words.append(str(text[a:b-1]))
			a = b
		b = b + 1
	for x in words:
		if(x != '!' and x != '?'):
			words_final.append(x[1:(len(x))] + x[0] + "ay")
		else:
			words_final.append(x)
	return(" ".join(words_final))