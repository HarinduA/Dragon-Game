import random
import time
fo=0
userinput=0


fo=open("D &D demo1.txt", "w")
fo.write("you are un the kingdom of dragons \nIn fornt of you, see two caves \none cave , the dragon is freindly and will \nshare his tressure with you \nThe other dragon is hungry and will eat you on sight!\n   \nyou approach....")
("A large dragon jumps out in front of you \nHe opens his jaws and \nGreets you with his tressure")
print("you are in the kingdom of dragons")
print("In front of you, see two caves")
print("In one cave , the dragon is freindly and will \nshare his tressure with you.")
print("The other dragon is hungry and will eat you on sight!")
fo.close()

#variables
cave1=0
cave2=0

hungrydragon=0
count = 0
retry = "y"


#main program
while retry == "y" :
    count = 0
    while count <1 :
        
        print("                ")
        userinput=int(input("select cave 1,2,3,4 or 5 :   "))

        if userinput >5 :
            print ("Invalid number")
            count = 0
            
        else :
            count =2


    hungrydragon= random.randint(1,5)

    
    if hungrydragon== userinput:
       print("you approach.... ",userinput,"\n")
       time.sleep(1)
       print("A large dragon jumps out in front of you!")
       time.sleep(1)
       print("He opens his jaws and....")
       print("   ")
       time.sleep(1)
       print("Gobbles you down ! ")
       #fo.close() 
    else:
        time.sleep(1)           
        print("you approach the cave ....",userinput)
        time.sleep(1)
        print("A large dragon jumps out in front of you !")
        time.sleep(1)
        print("He opens his jaws and ...")
        time.sleep(1)
        print("Greets you before share his tressure")
      
    print("")
    retry = input("Do you want to retry (y/n):")



