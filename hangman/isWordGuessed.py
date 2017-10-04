def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    word_list=[]
    for i in secretWord:
        word_list.append(i) 
    for letter in word_list[:]:
        if letter in lettersGuessed:
            word_list.remove(letter)
    if len(word_list)==0:
        return True
    elif len(word_list)>0:
        return False
        
 '''
 or
 '''
 
for x in secretWord:
        if x not in lettersGuessed:
            return False
    return True        
