file=open ("book3.txt","r")
w=file.read()
file.close()
lista1=w.split()
x=max(lista1, key=len)#biggest element 
lista1.remove(x)
x1=max(lista1, key=len)#second biggest element
lista1.remove(x1)
x2=max(lista1, key=len)#third biggest element
lista1.remove(x2)
x3=max(lista1, key=len)#fourth biggest element 
lista1.remove(x3)
x4=max(lista1, key=len) #fifth biggest element 
lista1.remove(x4)
lista2=[x, x1, x2 ,x3 ,x4]


def removeVowels(strg):

    vowels=['a', 'e', 'i', 'o', 'u','y','A' ,'E','I','O','U','Y']
    for k in strg:    
        if k in vowels:
           strg=strg.replace(k,'')
            
    print(strg[::-1])

for h in lista2:
    removeVowels(h)


