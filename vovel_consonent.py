# to check for the vovels and consonents
import re
charac = input("Enter any alphabet ")

if re.search("[a-z]", charac):
    if charac == 'a' or charac == 'e' or charac == 'i' or charac == 'o' or charac == 'u':
        print("vowel")
    else:
        print("consonent")
