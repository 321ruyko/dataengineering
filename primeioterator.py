class Prime:
    def __init__(self,f,l):
        self.start=f
        self.end=l
    def __iter__(self):
        self.n=-1
        return self
    def __next__(self):
        if (self.n <= self.end):
            c=self.primeno()
            self.n += 1
            return c[self.n]
        else:
            raise StopIteration
    def primeno(self):
        primes = []
        for num in range(self.start, self.end + 1):
            if num > 1:
                for i in range(2, int(num ** 0.5) + 1):
                    if (num % i) == 0:
                        break
                else:
                    primes.append(num)
        return primes




prime=Prime(11,23)
i=iter(prime)
print(next(i))
print(next(i))
print(next(i))
print(next(i))






