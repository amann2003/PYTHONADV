vowel=0
cons=0
def check(a):
    n=len(a)
    global vowel
    global cons
    for char in a:
        char=char.lower()
        if char in 'aeiou':
            vowel+=1
            print(f"Letter {char} is vowel")
        elif char >= 'a' and char<= 'z'  :
            cons+=1
            print(f"Letter {char} is consonant")

def main():
    str1=input("Enter the string:")
    str1.lower()
    check(str1)
    print(f"Vowels:{vowel}  \nConsonants{cons}")
main()