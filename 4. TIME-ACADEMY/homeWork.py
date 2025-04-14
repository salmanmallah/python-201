'''
Code by: Salman Mallah

homeWork: what if user inputed string as inputs: solve this issue using python's exceptions;
'''

while True:
    try:
        worked_hours = int(input("\nEnter hours you worked: "))
        rate = int(input('Enter your rate:'))
        break
    except:
        print('\nplease enter numbers only:')
if worked_hours>40:
    extrawork = worked_hours - 40
    salary = 40 * rate + (extrawork * (1.5*rate))
    print("your salary is: ", salary)
else:
    salary = worked_hours * rate
    print("your salary is: ", salary)
