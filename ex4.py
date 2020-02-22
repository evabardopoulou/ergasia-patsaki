def ConvertASCIInPrime():
    x=input ("give your input:")
    while x=="":
        x=input ("Please give a valid input:")
        
    Inascii=''.join(str(ord(k)) for k in x)
    #print (Inascii)
    number =int (Inascii)
    if number > 1: 
       
       for i in range(2, number): 
           
           if (number % i) == 0: 
               print(number, "is not a prime number") 
               break
       else: 
           print(number, "is a prime number") 
  
    else: 
       print(number, "is not a prime number")
ConvertASCIInPrime()
