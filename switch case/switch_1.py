class PythonSwitch:
	def switch(self,dayOfWeek):
		default="incorrect day"
		return getattr(self,'case_'+str(dayOfWeek),lambda :default)()

	def case_1(self):
		return "monday"
	def case_2(self):
		return "tuesday"

s=PythonSwitch()
print(s.switch(0))
print(s.switch(1))