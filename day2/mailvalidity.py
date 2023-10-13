import re
n=str(input("Enter the email address:"))
pattern=re.compile("[a-z][a-z0-9]*@(?!hotmail|yahoo)[a-z]+\.(?:com|org|in)")
r=re.match(pattern,n)
if r:
    print("Valid email")
else:
    print("Invalid email")