class BookStore:
	noOfBook=0

def __init__(self,title,author):
	self.title=title
	self.author=author
	BookStore.noOfBook+=1
	
def  bookInfo(self):
	print("book title",self.title)
	print("book author",self.author)

	b1=BookStore("wings of fire","apj abdul")
	b2=BookStore("Middlemarch", "George Eliot")

b1.bookInfo()
b2.bookInfo()

print("no of books",BookStore.noOfBook)