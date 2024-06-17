from collections import *
# coursed=namedtuple('course','name,tech')
# clist=coursed('datascience','python')
# print(clist)
# c=['web','cloud']
# print(getattr(clist,"tech"))
# print(coursed._make(c))
# print(coursed._asdict(clist))
#************* "namedtuple over***************"
# team_list=['Rohit',"Virat","Hardik","Rahul"]
# tqueue=deque(team_list)
# tqueue[1]='harsha'
# print(tqueue)
#*********deque over**************

# c={1:'one'}
# d={2:'two'}
# e=ChainMap(c,d)
# print(set(e.keys()))
# ********chainMap over*********

# Rohit_Scores=[70,89,170,270,70,89,32,32,32,32,]
# score_count=Counter(Rohit_Scores)
# c=max(list(score_count.values()))
# for i in score_count:
#     if(score_count[i]==c):
#         print(i)
# print("total count",c)
# *******counter is over*********
# tempod=OrderedDict()
# c=int(input("enter the size"))
# for i in range(c):
#     tempod[i]=input("enter")
# print(tempod)
# ********ordered dictionary over********
# *********Iterators*********
# prime_numbers=[1,3,5,7,13,11]
# it=iter(prime_numbers)
# print(next(it))
# class powten:
#     def __init__(self,max=0):
#         self._max=max
#     def __iter__(self):
#         self.n=0
#         return self
#     def __next__(self):
#        if self.n<=self._max:
#            result=3**self.n
#            self.n+=1
#            return result
#        else:
#            raise StopIteration
# numbers=powten(4)
# i=iter(numbers)
# print(next(i))
# print(next(i))
# print(next(i))
# "******iterator is over******"
# def custom_generator(n):
#     value=0
#     while value<n:
#         yield value
#         value+=1
# for value in custom_generator(10):
#     print(value)
# cubes_generator=(i*i*i for i in range(5))
# for j in cubes_generator:
#     print(j)
class PowerThree:
    def __init__(self,max=0):
        self.n=0
        self._max=max
    def __iter__(self,max=0):
        return self
    def __next__(self):
        if self.n>self.max:
            raise StopIteration
        result=3**self.n
        self.n+=1
        return result
    def cetpowerthree(max):
        value=0
        while value < max:
            yield value
            value+=1

