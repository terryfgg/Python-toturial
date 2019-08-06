list_grade = [100, 30, 50, 70] #要用append
tuple_grade = (199, 77, 100)#無法更改
set_grade = {99, 55, 5} #要用add


list_grade.append(100)
print(list_grade)

tuple_grades = tuple_grade + (100,)#need to add comma, it's a tuple type
print(tuple_grades)

list_grade[0] = 50
print(list_grade[0])

set_grade.add(45)
print(set_grade)

lottery_num ={1, 3, 10, 18 ,55}
win_num = {1, 10 ,15, 18, 20 }
print(lottery_num.intersection(win_num))  #交集
print(lottery_num.union(win_num))  #連集
print(lottery_num.difference(win_num))