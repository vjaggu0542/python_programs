import re
str1 ="this is string \ this/ string. belongs, to"
print(re.split('\ / . ,',str1))