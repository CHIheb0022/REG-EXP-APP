from multiprocessing.resource_sharer import stop
from pickle import TRUE
import regeng

if __name__ == "__main__" :
	
	pattern = input("Enter with the regex pattern: ")
	rgx = regeng.Regex(pattern)
	regeng.tostring_tr(rgx)
	regeng.tostring_ep_tr(rgx)
	while TRUE :
		try :
			str=input("Enter with the expression to be evaluated: ")
			if str=="stop" :
				break	
		except EOFError:
			break
	
