class AtmMachine:
    def __init__(self,cardholder,amount,pin):
        self.cardholder=cardholder
        self.__MainBal=amount
        self.__pin=1234
    def __verifypin(self,incomingpin):
        return  self.__pin==incomingpin
    def __updating_main_balbydeposit(self,incomingdepositamount):
        self.__MainBal+=incomingdepositamount
    def __checkAtmamount(self,ea,type):
        if "withdraw"==type:
            return False
        else:
            return True
    def __updating_main_balBywith(self,incomingwithdrawAmount):
        if  self.__MainBal>=incomingwithdrawAmount:
            self.__MainBal-=incomingwithdrawAmount
            print(f"{incomingwithdrawAmount} is debited to your account and your main balance after withdrawal is {self.__MainBal}")
        else:
            print("your account has insufficient funds")
    def deposit(self, ea, ep):
        if self.__pin == ep:   
            self.__MainBal += ea   
            print(f"{ea} is credited to your account.")
            print(f"After depositing, your total balance is {self.__MainBal}")
        else:
            print("You entered wrong PIN")
    def withdraw(self, ea, ep):
        if self.__verifypin(ep):
            if self.__MainBal >= ea:
                self.__MainBal -= ea
                print(f"{ea} is debited from your account.")
                print(f"Remaining balance: {self.__MainBal}")
            else:
                print("Your account has insufficient funds.")
        else:
            print("You entered wrong PIN")
atm=AtmMachine("devi",10000)
enterpin=int(input("enter your Pin here:"))
enterdeposit=int(input("enter your deposit amount here:"))
enterwithdraw=int(input("enter your withdraw amount here:"))
atm.deposit(enterdeposit,enterpin)
atm.withdraw(enterwithdraw,enterpin)

