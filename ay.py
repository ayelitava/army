#list - списки - [1,2,3, 'srtr', True] # изменяемые 
#tuple - кортежи - (1,2,3, 'srtr', True) # НЕ изменяемые 
#dict - словари - {1:2, 3:'srtr', 'hel': True}# изменяемые 
#set - множество - {3,4,5,4,3,5} #он хранит только уник. знач #изменяемые 


#student = {1: 'Aziret' , 'age' :55}
#stud2 = dict( name= "Aziret" , age= 56)
#student [1] = 'Radik' 
#print(student)


#student = dict (name= 'Ivan', age= 12)
#print(student ['name'])
 






# Fruits = ['Яблоко', 'Банан', 'Киви', 'Арбуз', 'Манго', 'Груша', 'Помидор', 'Дыня']
# last_name = len(Fruits)
# for i in range(last_name):
#     print(str(i+1)+'.'+ '{}'.format(Fruits[i]))



# lst1 = [1, 3, 5, 7, 9]
# lst2 = [3, 8, 6, 5]
# for item in lst1: 
#     if item in lst2: 
#         lst1.remove(item)
#         print(lst1)
#         print(lst2) 



lst = [1, 4, 3, 42, 48, 34, 4, 5, 10, 7, 8, 9]
new_lst = []

for i in lst: 
    if i % 2 == 0: 
        new_lst.append(i/4)
    else: 
        new_lst.append(i*2)
print(new_lst)