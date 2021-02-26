class Singleton(object):
	__instance = None
	
	def __init__(self):
		if not Singleton.__instance:
			print("__init__ method called...")
		else:
			print("Instance already created: {}".format( self.getInstance()))
	@classmethod
	def getInstance(cls):
		if not cls.__instance:
			cls.__instance = Singleton()
		return cls.__instance


class Singleton_Twin(object):
	def __new__(cls):
		if not hasattr(cls,'instance'):
			cls.instance = super(Singleton_Twin, cls).__new__(cls)
		return cls.instance

sl = Singleton()
sl2 = Singleton()
print('Singleton Instances: ')
print(sl.getInstance(),sl2.getInstance())

print('Twin Singleton Instances: ')
ss = Singleton_Twin()
ss2 = Singleton_Twin()
print(ss,ss2)
