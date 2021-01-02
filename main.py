txtFilePath = input("Give full path of text file: ")
searchWord = input("word you want to search in uploaded text file: ")
file = open(txtFilePath, "r")
fileText = file.read()
result = fileText.count(searchWord)

print('Word \"{}\" has occurred {} times in selected text file.'.format(searchWord, result))