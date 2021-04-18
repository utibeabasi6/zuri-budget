class Budget(object):
	"""docstring for Budget"""
	def __init__(self, category, amount):
		super(Budget, self).__init__()
		self.category = category
		self.amount = amount
		
	def transfer(self, budget2, transfer_amount):
		if transfer_amount > self.amount:
			return "Cannot make this transaction"
		self.amount -= transfer_amount
		budget2.amount += transfer_amount
		return "transfer succesful"
	
	def deposit(self, amount):
		self.amount += amount
	
	def withdraw(self, amount):
		self.amount -= amount
	
	def getBalance(self):
		return self.amount
	
	


clothes_budget = Budget('clothes', 500)
food_budget = Budget('food', 200)
print(clothes_budget.amount)
clothes_budget.transfer(food_budget, 200)
print(clothes_budget.amount)
print(food_budget.amount)
