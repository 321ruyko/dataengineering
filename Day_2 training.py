# import csv
# with open('data.csv') as data:
#     csv_reader=csv.reader(data,delimiter=",")
#     line_count=0
#     for row in csv_reader:
#         if line_count==0:
#             print(f'ColumnNames are {",".join(row)}')
#             line_count+=1
#         else:
#             print(f'\t{row[0]} has {row[1]} no of shares at price  {row[2]}')
#             line_count+=1

# try:
#     c=0/4
# except Exception:
#     print(Exception)
# import csv
# with open('eggs.csv', 'w', newline='') as csvfile:
#     spamwriter = csv.writer(csvfile, delimiter=' ',
#                             quotechar='|', quoting=csv.QUOTE_MINIMAL)
#     spamwriter.writerow(['Spam'] * 5 + ['Baked Beans'])
#     spamwriter.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])
# itemname = input("Enter the item").capitalize()
# print(itemname)
import datetime
today=datetime.date.today()
year=today.year
class company:
    def __init__(self):
        self.name='hello'
    def test(self):
        print("hi from Parent class")
class Employee(company):
    def __init__(self,fname,lname,yob):
        self._fname=fname
        self.lname=lname
        self._age=year-yob
    def getEmpDetails(self):
        print('FullName',self._fname)
        print(year-self._age)
e=Employee("ME","M",2000)
e.getEmpDetails()
e.test()