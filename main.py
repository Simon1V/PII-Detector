from piidetector import PIIDetector
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
	
	piiList = [] 
	# A list comprehension would require calling getPII twice. 
	for index, line in enumerate(content):
		pii = piiDetector.getPII(line) 
		if pii[1] != 0: 
			piiList.append((index, pii) )
	piiDetector.formattedOutput(piiList) 

if __name__ == "__main__": 
	main() 