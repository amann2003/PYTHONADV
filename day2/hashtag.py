import re
n=input("Enter the sequence:")
pattern=re.compile("\#\w*")
r=pattern.findall(n)
if r:
    print("Hashtag is extracted" ,r)
else:
    print("No hashtags are present")