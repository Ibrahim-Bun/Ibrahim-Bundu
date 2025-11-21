employees = []
employee_commision =[]
total_properties = 0

#number of employees
while True:
    try:
        num_employee = int(input("Enter number of employees to add to logbook (From 2 to 5): "))
        if 2 <= num_employee <=5:
            break
        else:
             print("Please enter amount from 2 to 5: ")
    except ValueError:
        print("Invalid input please enter a number: ")

#employee details added to list
for i in range(num_employee):
    employee_name = str(input(f"Please enter employee {i+1}'s name: "))
    employee_ID = int(input(f"Please enter employee {i+1}'s 4 digit ID number: "))
    employee_properties = int(input(f"Please enter number of proprties sold: "))

    #sorting details
    employees.append({
        'Name': employee_name,
        'ID':employee_ID,
        'Properties Sold': employee_properties
    })


total_properties =sum(i['Properties Sold'] for i in employees)

top_employee = max(employees, key=lambda i:i['Properties Sold'])

#commision
commision_rate = 500
top_commision = top_employee['Properties Sold'] * commision_rate

#each employee commision appended to list
for i in employees:
    commision = i['Properties Sold'] * commision_rate
    employee_commision.append(commision)
    
#calculating bonus
bonus_percentage = 0.15
bonus_amount = top_commision * bonus_percentage
total_commision= top_commision + bonus_amount
        

employees.sort(key=lambda employee: employee['Properties Sold'], reverse=True)

print("\n-- Employee List sorted by sales --")
print(employees)

print("\n--Commision List--")
for i in range(len(employees)):
    print(f"{employees[i]['Name']} earned £{employee_commision[i]}")


print("Employee with most sales:", top_employee['Name'])
print("Amount sold by them:", top_employee['Properties Sold'])
print("Bonus amount (15%): £",bonus_amount)
print("Total commision cost: £",total_commision)

print("\nTotal number of properties sold:",total_properties)
