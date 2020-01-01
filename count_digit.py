# count the digits of the letter and also letter

str = input("Enter the strings to count")
l=0
d=0
for c in str:
    if c.isalpha():
        l=l+1
    if c.isnumeric():
        d=d+1

print("letters",l)
print("Digits",d)
