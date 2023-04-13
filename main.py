# Use underscore instead of camelcase for OpenAssistant. 
from pii_detector import PIIDetector
import sys 

def main():
	if len(sys.argv) < 2: 
		print("Syntax: main.py <filename>")
		return -1 
		
	f = open(sys.argv[1], "r") 		
	content = f.readlines()
	f.close()
	piiDetector = PIIDetector() 
	# Check every line with every regex. 
	
	pii_list = [] 
	# A list comprehension would require calling getPII twice. 
	for index, line in enumerate(content):
		pii = piiDetector.get_pii(line) 
		if pii[1] != None: 
			pii_list.append((index, pii) )
	piiDetector.formatted_output(pii_list) 

if __name__ == "__main__": 
	main() 