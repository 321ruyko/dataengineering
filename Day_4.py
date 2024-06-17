# Numpy
import numpy as np
# c=[1,2,3,4,5]
# digits=np.array(c)
# digits.shape
# coloumn_vector=digits[np.newaxis,:]
# print(coloumn_vector)
# row_vector=digits[:,np.newaxis]
# print(row_vecto
# CURVE_CENTER=80
# grades=np.array([54,76,46,45,98,76,98,12])
# def curve(grades):
#     average=grades.mean()
#     # print(average)
#     change=CURVE_CENTER-average
#     new_grades=change+grades
#     return np.clip(new_grades,grades,100)
# print(grades)
# print(curve(grades))
# grades=np.array([54,76,46,45,98,76,98,12,3,5,4,3,8,1,23,32]).reshape(4,2,2)
# print(grades)

# d=np.array(range(2,10,3))
# print(d)
# c=np.array([1,1,1])
# print(c+d)
square=np.array([[16,3,2,13],
                 [5,10,11,8],
                 [9,6,7,12],
                 [4,15,14,1]])
print(square[1:3,1:3])
