import re
n=input("Enter the phone number")
pattern=re.compile(r"\b\d{8,12}\b|\b\+?\d{1,3}\s\d{10}\b")
r=re.findall(pattern,n)
if r:
    print("Valid number")
else:
    print("Invalid number")