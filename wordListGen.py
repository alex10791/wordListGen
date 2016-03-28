def allNumCases(word):
	wordlist = []
	changePos = []
	numOfWords = []
	wordCounter = []

	j = 0

	[retWordList, changePos] = changeNums(name, 0)
	wordlist.append(retWordList)
	numOfWords.append(retWordList.count)
	wordCounter.append(0)

	while 1:	
		if (len(wordlist[j]) > 1):
			[retWordList, retChangePos] = changeNums(wordlist[j-numOfWords[j], wordCounter[j] ], changePos[j-numOfWords[j],wordCounter[j]] )
			wordlist.append(retWordList)
			wordlist.append(retChangePos)
			numOfWords = retWordList.count
			j = j + 1
		else:
			j = j + 1
			if (wordCounter[j] == numOfWords):
				

	return wordlist

def changeNums(word, pos):
	#changes = ['a', 'b', 'e', 'i', 'o', 'q', 
	localWords = []
	changePos = []
	newWord = ""
	newWord = list(word)
	for i in range(pos, len(word)):
		newWord[i] = changeChar(word[i])
		if (''.join(newWord) != word):
			localWords.append(''.join(newWord))
			changePos.append(i)
		newWord = list(word)
		#print ''.join(newWord)
	return [localWords, changePos]

		
def changeChar(ch):
	if (ch == 'a') or (ch == 'A'):
		return '4'
	elif (ch == 'b') or (ch == 'B'):
		return '6'
	elif (ch == 'e') or (ch == 'E'):
		return '3'
	elif (ch == 'i') or (ch == 'I'):
		return '1'
	elif (ch == 'o') or (ch == 'O'):
		return '0'
	elif (ch == 'q') or (ch == 'Q'):
		return '9'
	else: 
		return ch

	






name = "alexandros"
surname = "andreou"
dobD = "10"
dobM = "7"
dobY = "1991"
givenwordlist = ["alex", "kanenas", "psilos", "kokos"]

wordlist = allNumCases(name)


print wordlist


print "\nkokos"





