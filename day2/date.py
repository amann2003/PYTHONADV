import re

def dat(d):
    pattern=re.compile("\d{1,12}\/(?:[0-2][0-9]|[3][0-1])\/[0-9][0-9][0-9][1-9]")
    n=pattern.findall(d)
    if n:
        print("MM/DD/YYYY :",n)
    else:
        print("Not in the valid format")

def main():
    x=input("Enter the date:")
    dat(x)
    
main()