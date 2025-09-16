class BankExample:
    def __init__(self,name,min_bal,ac_number,p_number):
        self.name=name
        self.min_bal=min_bal
        self._ac_number=ac_number
        self.__p_number=p_number
    def show_details(self):
        print(f"{self.name} with min balance{self.min_bal}")
    def depost_amount(self,d_ac_num,d_amount):
        self.d_ac_num=d_ac_num
        self.d_amount=d_amount
        if self.min_bal>0:
            self.min_bal+=self.d_amount
            print(f"total amount:---{self.min_bal} after deposting {self.d_amount}")
        else:
            print("incorrect account number",d_ac_num)
    def with_draw_amount(self,p_num,w_amount):
        self.p_num=p_num
        self.w_amount=w_amount
        if w_amount<=self.min_bal:
            self.min_bal-=w_amount
            print(f"{w_amount} drawn successfully and your account balance is {self.min_bal}")
        else:
            print("insufficient balance {self.min_bal}")
    def check_bal(self,pin):
        if self.__p_number==pin:
            print(f"{self.min_bal} is main balance")
        else:
            print("incorrect pin",pin)
abc=BankExample("Devi",10000,"123123123123",1234)
abc.show_details()
depo_amount=int(input("enter amount to deposit:--"))
ac_number=input("enter account number to deposit amount:----")
abc.depost_amount(ac_number,depo_amount)
with_amount=int(input("enter amount to withdraw:---"))
pin_numberforwithdraw=int(input("enter pin to withdraw amount:-----"))
abc.with_draw_amount(with_amount,pin_numberforwithdraw)
pin_numberforbalcheck=int(input("enter pin to check bal amount:-----"))
abc.check_bal(pin_numberforbalcheck)