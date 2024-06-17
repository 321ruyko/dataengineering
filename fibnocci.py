def fn(nums):
    x,y=0,1
    for _ in range(nums):
        x,y=y,x+y
        yield x
def prime(val):
    for num in val:
        if num > 1:
            for i in range(2, int(num ** 0.5) + 1):
                if (num % i) == 0:
                    break
            else:
                yield num
print('fibnocci')
for j in fn(6):
    print(j)
print('Prime Numbers')
for i in prime(fn(6)):
    print(i)