class SavingsAccount:
    def __init__(self,saving_balance):
        self.saving_balance=saving_balance
    def modifyInterestRate(annual_inter_rate):
        return annual_inter_rate
    def calculateMonthlyInterest(self):
        return(self.saving_balance*change.modifyInterestRate(5)/12)
change=SavingsAccount
change.modifyInterestRate=staticmethod(change.modifyInterestRate)
saver1= SavingsAccount(2000.00)
saver2=SavingsAccount(3000.00)
print(saver1.calculateMonthlyInterest() + saver1.saving_balance)
print(saver2.calculateMonthlyInterest() + saver2.saving_balance)
