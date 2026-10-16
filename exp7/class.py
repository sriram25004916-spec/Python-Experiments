class charge:
    name=input("enter your good name")
    phone=int(input("enter mobile number darling"))

    def chooseplan(self):
        print("choose a plan according to your needs")
        print("1.$99 1 gb per day (unlimited call)\n2. $299 (1 month free unlimited sms)\n3. $499 (unlimited data)")
        choice=int(input("enter your choice"))

        if(choice==1):
            print("$99 Chosen. Gareeb Insaan")
        elif(choice==2):
            print("$299 Chosen. Dengue Class")
        elif(choice==3):
            print("$499 Chosen. Ameer Insaan")
        else:
            print("Wrong Input. Gawar Insaan")
    def shreesha(self):
        print("Majestic Shreesha")
            
gooseberry= charge()


class recharge:
    def ch(self):
        print("Dengue Dengue")


class chargere(charge,recharge):
    def chr(self):
        print("Sooraj bhai mast nahi hain")
        
virus=chargere()
virus.chooseplan()
virus.ch()
virus.shreesha()
virus.chr()


    
    
