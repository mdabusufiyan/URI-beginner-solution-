import math
x1, y1 = list(map(float, input().split()))
x2, y2 = list(map(float, input().split()))
x2x1 = (x2-x1)*(x2-x1)
y2y1 = (y2-y1)*(y2-y1)
res = math.sqrt(x2x1+y2y1)
print(format(res, "0.4f"))
