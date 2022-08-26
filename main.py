import regeng

if __name__ == "__main__" :
	
	pattern = input("Enter with the regex pattern: ")
	rgx = regeng.Regex(pattern)
	while True  :
		test=input("Enter with the expression to be evaluated: ")
		print(rgx.match(test))
		if rgx.match(test) :
			break
		else :
			answer=input("I want to keep trying :(y/n)")
			if answer=="y" :
				continue
			else :
		 		break	
		
