word=input('enter a word')
char=input('enter a character to check') 
i=0
count=0
while (i<len(word)):
    if word[i]==char:
        count+=1
    i+=1
print("the letter",char,"occurs",count,"times in the word",word)
        