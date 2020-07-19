class Account:

  def __init__(self, account_holder, quantity = 0.00):
    self.account_holder = account_holder
    self._quantity = quantity
    self._txt = "{:.2f}"

  def deposit(self, ammount):
    if ammount > 0:      
      self._quantity += ammount
    quantity_txt= self._txt.format(self._quantity)
    print(f'deposit of {self.account_holder} : {ammount} new quantity: {quantity_txt}')
  
  def withdraw(self,ammount):
    if ammount > self._quantity:
      self._quantity = 0
    else:
      self._quantity -= ammount
    quantity_txt= self._txt.format(self._quantity)
    print(f'withdraw of {self.account_holder} : {ammount} new quantity: {quantity_txt}')

  def toString(self):
    quantity_txt= self._txt.format(self._quantity)
    print(f'The account of {self.account_holder} has {quantity_txt}')

class Executable(Account):
  
  def __init__(self,account_holder,quantity = 0.00):
    super().__init__(account_holder,quantity)

  def make_movement(self,movement_type,ammount):
    if movement_type == 'deposit':
      self.deposit(ammount)
    elif movement_type == 'withdraw':
      self.withdraw(ammount)
    else:
      print(f'movement type {self._movement_type} is invalid must be deposit or withdraw')



if __name__ == '__main__':
  account = Account('Carlos 33')
  account.toString()
  account.deposit(1000.00)
  account.withdraw(600.00)
  account.withdraw(800.00)
  account.deposit(-500.00)
  print('-'*20)
  account1 = Account('Maria 55', 2000.00)
  account1.toString()
  account1.deposit(-700.00)
  account1.deposit(700.00)
  account1.withdraw(600.00)
  account1.withdraw(800.00)
  account1.withdraw(2000.00)
  account1.deposit(-500.00)
  print('-'*20)
  account2 = Executable('Maria 55', 2000.00)
  account2.toString()
  account2.make_movement('deposit',-700.00)
  account2.make_movement('deposit',700.00)
  account2.make_movement('withdraw',600.00)
  account2.make_movement('withdraw',800.00)
  account2.make_movement('withdraw',2000.00)
  account2.make_movement('deposit',-500.00)