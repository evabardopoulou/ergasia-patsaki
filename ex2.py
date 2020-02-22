file=open('book3.txt','r')
w=file.read()
file.close()

lista1=w.split()
a = [0,1,2,3,4,5,6,7,8,9]
for word in lista1:
    for letter in lista1:
        if (int(letter) in a):
            lista1.pop(letter)
print (lista1)
def findCon(strg):
    count=0
    countf=0
    countc=0
    countk=0
    countr=0
    vowels=['a', 'e', 'i', 'o', 'u']
    for k in strg.lower():
        #print(strg)
        if k not in vowels:
            if k!='f':
                if k!='c':
                    if k!='k':
                        if k!='r':
                            count+=1
        if k=='f':
            countf+=1
        if k=='c':
            countc+=1
        if k=='k':
            countk+=1
        if k=='r':
            countr+=1
    countCon=countf+countc+countk+countr
    if count==0 and countCon==0:
            print('The word:',strg,'is good')
            print ("Number of good consonants:",count ,"Number of bad consonants:",countCon)
    elif count<=(countCon)  :
            print('The word:',strg,'is bad ')
            print("Number of good consonants:",count ,"Number of bad consonants:",countCon)
    elif count>countCon:
            print('The word:',strg,'is good')
            print("Number of good consonants:",count ,"Number of bad consonants:",countCon)
for h in lista1:
    findCon(h)
    
