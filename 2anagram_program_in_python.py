str1 = "dcab"
str2 = "adcb"

if (len(str1) == len(str2)):
    if(sorted(str1) == sorted(str2)):
        print("given strings are  anagram")
    else:
        print("given strings are not a anagram")
else:
    print("given strings are not a anagram")