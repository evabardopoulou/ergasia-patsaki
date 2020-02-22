file = open('book4.txt', 'w')
file.write("When it first appeared in 1964, \n The Sufis was welcomed as the decisive work on the subject: rich in scope, \n clearly explaining the traditions")
file.write(" and philosophy of the Sufis to a Western audience for the first time. ")
file.close()
file=open('book4.txt','r')
w=file.read()
file.close()

list1 = w.split()#δημιουργειται λιστα
i=len(list1)#μεγεθος της λιστας 
print ("Το περιεχόμενο του αρχείου πριν την μετατροπή:",list1)

print ("Το περιεχόμενο του αρχείου μετά την μετατροπή:")
for x in list1:
   if (len(x) > 3):
       x1 = list(x)#δημιουργω λιστα με τα γραμματα της λεξης
       y=x1.pop(0)
       x1.append(y)
       x1.append("ay")
       listToString =''.join(map(str,x1))
       print (listToString)
       
