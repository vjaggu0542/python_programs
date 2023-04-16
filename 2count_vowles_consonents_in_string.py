a= "adalkjioerjflkbnaioqvcmniuryuwejkhcna"
che="aeiou"
vow = ""
con =""

for i in a:
    if i in che:
        vow = vow + i
    else:
        con = con + i
print ("total vowles count is : ", len(vow))
print ("total consonents count is : ", len(con))
