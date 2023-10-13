import re
n=input("Enter the IP address:")
pattern=re.compile(r"(?:\b[01][0-9]?[0-9]?\b|\b[2][0-5][0-5]\b).(?:\b[01][0-9]?[0-9]?\b|\b[2][0-5][0-5]\b).(?:\b[01][0-9]?[0-9]?\b|\b[2][0-5][0-5]\b).(?:\b[01][0-9]?[0-9]?\b|\b[2][0-5][0-5]\b)")
r=pattern.findall(n)
if r:
    print("Valid IP address" ,r)
else:
    print("Invalid IP address")