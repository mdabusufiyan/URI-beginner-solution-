#URI-1020

import math
x = int(input())
y = 365
z = 30
year, extra = divmod(x,y)
print (%year,"ano (s)")
month, day = divmod(extra,z)
print (%month,"mes (es)")
print (%day,"dia (s)")

#Solved by https://github.com/sufiyanism
