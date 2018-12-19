
n = int(input("fibbonacci number = " ))
n = n - 1
i = 0
new = 1
old = 0
new_num = 1
for i in range(n):
    new_num = old + new
    old = new
    new = new_num
if n <= 0:
    print ("Enter a positive value")
elif n >= 0:
    print ("Your Fibbonacci number is:  " , (new_num))