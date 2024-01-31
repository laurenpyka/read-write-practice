import csv

employees = open('employee_data.csv', 'r')

#name, salary, bonus, and total pay
csv_file = csv.reader(employees)

next(csv_file)

print("Employee name, salary, bonus, total pay")
for line in csv_file:
    name = line[1]
    salary = int(line[3])
    hours_worked = int(line[4])
    bonus = float(line[7])
    total_bonus = (salary * bonus)
    total_pay = (salary + total_bonus)

    print(f'Name: {name}')
    print(f'Salary: $ {salary:.2f}')
    print(f'Bonus: ${total_bonus:.2f}')
    print(f'Pay: ${total_pay:.2f}')
    
    #print(f'{name}, {salary}, ')
    input()
