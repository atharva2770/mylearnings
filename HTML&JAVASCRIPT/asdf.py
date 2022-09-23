class Country:
    cname="India" #class variable
	def __init__(self,state,capital):
		self.state=state
		self.capital=capital
	def dispS(self):#method atharva atharva atharva atharva
		print("Name of the Country is:",Country.cname,"\nThe name of the the state is:",self.state,"\nand it's captial is:",self.capital)
	ob=Country("Maharashta","Mumbai")
	ob.dispS()