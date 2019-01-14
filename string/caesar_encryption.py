def caesar_encryption(str,step):
	outtext=[]
	crypttext=[]

	uppercase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

	lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

	for text in str:
		if text in uppercase:
			index=uppercase.index(text)
			crypting=(index+step)%26
			crypttext.append(crypting)
			newLetter=uppercase[crypting]
			outtext.append(newLetter)
	
		elif text in lowercase:
			index=lowercase.index(text)
			crypting=(index+step)%26
			crypttext.append(crypting)
			newLetter=lowercase[crypting]
			outtext.append(newLetter)

	return outtext

code=caesar_encryption('pyThon',2)

print(code)