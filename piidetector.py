import re 

# SSN regex grabbed from: 
# https://www.geeksforgeeks.org/how-to-validate-ssn-social-security-number-using-regular-expression/
# 

	# Adapted from https://github.com/m4ll0k/SecretFinder/blob/master/BurpSuite-SecretFinder/SecretFinder.py
regexes = {
	'google_api' : 'AIza[0-9A-Za-z-_]{35}',
	'bitcoin_address' : '([13][a-km-zA-HJ-NP-Z0-9]{26,33})',
	'slack_api_key' : 'xox.-[0-9]{12}-[0-9]{12}-[0-9a-zA-Z]{24}',
	'google_cloud_platform_auth' : '[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}',
	'google_cloud_platform_api' : '[A-Za-z0-9_]{21}--[A-Za-z0-9_]{8}',
	'gmail_auth_token' : '[0-9(+-[0-9A-Za-z_]{32}.apps.qooqleusercontent.com',
	'github_auth_token' : '[0-9a-fA-F]{40}',
	'Instagram_token' : '[0-9a-fA-F]{7}.[0-9a-fA-F]{32}',
	'google_captcha' : '6L[0-9A-Za-z-_]{38}|^6[0-9a-zA-Z_-]{39}$',
	'google_oauth' : 'ya29\.[0-9A-Za-z\-_]+',
	'amazon_aws_access_key_id' : 'A[SK]IA[0-9A-Z]{16}',
	'amazon_mws_auth_toke' : 'amzn\\.mws\\.[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}',
	'amazon_aws_url' : 's3\.amazonaws.com[/]+|[a-zA-Z0-9_-]*\.s3\.amazonaws.com',
	'facebook_access_token' : 'EAACEdEose0cBA[0-9A-Za-z]+',
	'authorization_basic' : 'basic\s*[a-zA-Z0-9=:_\+\/-]+',
	'authorization_bearer' : 'bearer\s*[a-zA-Z0-9_\-\.=:_\+\/]+',
	'authorization_api' : 'api[key|\s*]+[a-zA-Z0-9_\-]+',
	'mailgun_api_key' : 'key-[0-9a-zA-Z]{32}',
	'paypal_braintree_access_token' : 'access_token\$production\$[0-9a-z]{16}\$[0-9a-f]{32}',
	'square_oauth_secret' : 'sq0csp-[ 0-9A-Za-z\-_]{43}|sq0[a-z]{3}-[0-9A-Za-z\-_]{22,43}',
	'square_access_token' : 'sqOatp-[0-9A-Za-z\-_]{22}|EAAA[a-zA-Z0-9]{60}',
	'stripe_standard_api' : 'sk_live_[0-9a-zA-Z]{24}',
	'stripe_restricted_api' : 'rk_live_[0-9a-zA-Z]{24}',
	'github_access_token' : '[a-zA-Z0-9_-]*:[a-zA-Z0-9_\-]+@github\.com*',
	'rsa_private_key' : '-----BEGIN RSA PRIVATE KEY-----',
	'ssh_dsa_private_key' : '-----BEGIN DSA PRIVATE KEY-----',
	'ssh_dc_private_key' : '-----BEGIN EC PRIVATE KEY-----',
	'pgp_private_block' : '-----BEGIN PGP PRIVATE KEY BLOCK-----',
	'json_web_token' : 'ey[A-Za-z0-9_-]*\.[A-Za-z0-9._-]*|ey[A-Za-z0-9_\/+-]*\.[A-Za-z0-9._\/+-]*',
	'social_security_number': '(?!666|000|9\\d{2})\\d{3}-(?!00)\\d{2}-(?!0{4})\\d{4}$' 
    }
	
class PIIDetector: 
	# Pre compile regexes. 
	def __init__(self):
		self.regexListCompiled = []
		for regex in regexes.values():
			regexCompiled = re.compile(regex, re.I) 
			self.regexListCompiled.append(regexCompiled)
			
	# Returns first match or ("", 0), one line may contain more than one match though, so the script needs to run until all PII has been handled. 
	def getPII(self, inputText:str):# -> (context:str, pos:int): 
		for reg in self.regexListCompiled: 
			match = re.search(reg, inputText) 
			if match is None: 
				continue 
			else: 
				return (match.group(), match.start())
		return ("", 0)
		
	def formattedOutput(self, matchList:list): 
		pass 
		
def main(): 
	f = open("test.txt", "r") 
	content = f.readlines()
	piiDetector = PIIDetector() 
	# Check every line with every regex. 
	piiR = [(index, line) for index, line in enumerate(content) if piiDetector.getPII(line)[1] != 0]
	print(piiR) 
	#piiDetector.formattedOutput(piiR) 
	
if __name__ == "__main__": 
	main() 