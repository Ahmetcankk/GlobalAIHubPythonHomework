i=0
myList=[]
while i<5:
   val1=input("Enter a value : " )
   myList.insert(i,val1)
   i+=1
myList
j=0
while j<5:
    print(f"value {j+1}= ",myList[j],"\tType: {} ".format(type(myList[j])))
    j+=1
   #Also the type function is not necessary here because of the input method stores String type whatever you enter.  
              
   
   
   
   
    
   
