class Customers:
	def __init__(self,name,balance):
		self.name = name
		self.balance = balance

	def deposit(self,ammount):
		self.balance += ammount
		return self.balance

	def withdraw(self,ammount):
		self.balance -= ammount
		return self.balance

	def getbalance(self):
		return self.balance

if __name__ =="__main__":

	customer1 = (Customers("ali",5000))

	while True:
		option = int(input("Enter your choise\n1-press 1 deposit\n2-press 2 withdraw\n3-press 3 to get balance\n4- press 0 to exit:  "))
		if option == 1 :
			deposit_ammount = float(input("Enter The deposit ammount: "))
			current_balance = customer1.deposit(deposit_ammount)
			print(current_balance)
			print("----")
		elif option == 2 :
			withdraw_ammount = float(input("Enter The withdraw ammount: "))
			current_balance = customer1.getbalance()
			#withdraw_ammount >=0 and no - numbers
			if withdraw_ammount >=0 and current_balance >= withdraw_ammount:
				new_abalance = customer1.withdraw(withdraw_ammount)
				print("your new_abalance balance",new_abalance)
			else:
				print("The balance Not enaph")

		elif option == 3 :
			current_balance = customer1.getbalance()
			print("Your balance Is: ",current_balance)
			print("----")

		elif option == 0:
			break

		else:
			print("Enter Correct choise")
			

