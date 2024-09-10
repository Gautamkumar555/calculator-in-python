a=input("enter operation name \n add \n sub \n mul \n div \n")
b=input("enter 1st no.")
c=input("enter 2nd no.")
b=int(b)
c=int(c)

	
if a==("add"):
    print("addition of a your no.s is" ,b+c)
elif a==("sub"):
      print("subtraction of your no.s is" ,b-c)
 
elif a==("mul"):
        print("multiplicaton of your no.s is" , b*c)
 
elif a==("div"):
 	print("division of your no.s is" , b/c)
 
else:
	 print("enter valid operators only")