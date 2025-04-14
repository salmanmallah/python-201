"""
3rd lecturer.



write a program that will ask user about his or her age and calculate his 
father age who is 25 years older than his and print 
and print("your father is x years old)
"""
# user_age = input("Enter your age")
# father_age = 25 + user_age
# exit()
# print(f"Your father is {25+user_age} years old")
# print("your father age is ", 25+user_age, "years old")

# age = int(input('enter your age: '))
# if age >= 18:
#     print("you age eligible to vote.")
    

# x = 'salman'
# if x < 10:
#     print(x)
# elif x >= 10:
#     print(x)
# else:
#     print('something else')



# age = input('enter you age: ')
# try:
#     age_i = int(age)
# except:
#     age_i = -1


'''
    exercise: rewrite your pay computation to give the employee 1.5
    times the hourly rate for hours worked above 40 hours
'''

# worked_hours = int(input("Enter hours you worked: "))
# rate = 10
# if worked_hours <= 40:
#     print(f"total salary: {worked_hours*rate}")
# elif worked_hours > 40:
#     extra_work = rate * 1.5
#     print(f"total salary with extra hours: {worked_hours*extra_work}")
'''
homeWork: what if user inputed string as inputs: 
'''

while True:
    try:
        worked_hours = int(input("\nEnter hours you worked: "))
        rate = int(input('Enter your rate:'))
        break
    except:
        print('please enter numbers only:')

if worked_hours>40:
    extrawork = worked_hours - 40
    salary = 40 * rate + (extrawork * (1.5*rate))
    print("your salary is: ", salary)
else:
    salary = worked_hours * rate
    print("your salary is: ", salary)