def add_word(tree, word):
	## Rekursionsanfang
	if word=="":
		return (True, tree[1])
	## Rekursionsschritt
	## Fall 1: Zeichen kommt schon in der Adjazenzliste vor
	for i in range(len(tree[1])):
		char, subtree = tree[1][i]
		if char == word[0]:
			tree[1][i] = (char, add_word(subtree, word[1:]))
			return tree
	## Fall 2: Zeichen kommt noch nicht in der Adjazenzliste vor
	pre = []
	for child in tree[1]:
		if child[0] < word[0]:
			pre.append(child)
	post = []
	for child in tree[1]:
		if child[0] > word[0]:
			pre.append(child)
	new = (word[0], add_word((False, []), word[1:]))
	return tree[0], pre+[new]+post