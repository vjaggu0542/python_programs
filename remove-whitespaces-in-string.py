import re
string="this   is  python"
print("original string :", string)
print("new string :", re.sub(r'\s+','',string))