productCode, quantity = map(int,input().split())

if productCode == 1:
    print(f"Total: R$ {quantity*4.00:.2f}")
if productCode == 2:
    print(f"Total: R$ {quantity*4.50:.2f}")
if productCode == 3:
    print(f"Total: R$ {quantity*5.00:.2f}")
if productCode == 4:
    print(f"Total: R$ {quantity*2.00:.2f}")
if productCode == 5:
    print(f"Total: R$ {quantity*1.50:.2f}")
