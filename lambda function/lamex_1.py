def greetings():
	start_word="hello "

	greet=lambda x,y: start_word+'mr. '+str(x) if y=='M' else start_word+'miss '+str(x)
	return greet

result=greetings()

print(result)
print(result("durgesh","M"))