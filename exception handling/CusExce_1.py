class InvalidLevelException(Exception):
	def __init__(self,message):
		self.message=message

level=-1

try:
	if level<1:
		raise InvalidLevelException("this is a invalid level: {}".format(level))

except InvalidLevelException as e:
	print(e.message)