# bill_thickness = 0.11
# tower_height = 442
# no_of_bills = 1
# days = 1
#
# while(no_of_bills*bill_thickness<tower_height):
#     days+=1
#     no_of_bills*=2
# print("no of days: ",days)
# print("no of bills: ",no_of_bills)
# print("Final height of bills: ",no_of_bills * bill_thickness)
#leap year question
# year=int(input("enter the year"))
# if(year%400==0 or(year%4==0 and year%100!=0)):
#     print(year,"is leap year")
# else:
#     print(year, "is not leap year")
#interest
# principal= 500000.00
# rate=0.05
# payment=2684.11
# total_paid=0.0
# while principal>0:
#     principal=principal*(1+rate/12)-payment
#     total_paid+=payment
# print("total paid amount",total_paid)
# print("total paid amount",round(total_paid,2))

# message='Learning python for Data Engineering'
# vowels=0
# consonents=0
# words=len(message.split(' '))
# space=0
# for i in message:
#     if(i==' '):
#         space+=1
#     elif(i in 'aeiouAEIOU'):
#         vowels+=1
#     elif(i not in 'aeiouAEIOU'):
#         consonents+=1
# print('vowels',vowels)
# print('consonents',consonents)
# print("space",space)
# print("Words",words)
#tuple
#
stock={'pen':10,'pencil':5,'book':25,'eraser':4}
for i in stock:
    print(stock[i])