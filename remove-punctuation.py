punctuation="''''!@#$%^&*(),."
mystr=(input("please enter string :"))

my_str=""
for c in mystr:
    if c not in punctuation:
        my_str+=c
print(my_str)
