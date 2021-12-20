#Initialize list and dictionary
employeeData = []

dict1 = {'Employee ID':'', 'Employee Name':'', 'Employee Email Address':'', 'Employee Address':'', 'Employee Salary':''}

#repeat used for the overall while loop to stop entering employees
repeat = 'y'

#Initialize different character sets for what is allowed and not allowed
IDCharacter = '0123456789' 

nameCharacter = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ '-"

emailIllegalCharacter = """!"'#$%^&*()=+,<>/?;:[]{ }\)"""

addressIllegalCharacter = """!"'@$%^&*_=+<>?;:[]}{()"""

salaryCharacter = '.0123456789'

#Define the function that will find errors in IDs
def ID(tag): 
    #Initialize values for tests
    recall = False
    test = False
    i = 0

    #Test length of ID
    if len(tag) > 7:
        print('ERROR: ID must be 7 digits or less')
        recall = True
    
    #Test that ID is only numbers
    for i in range(len(tag)):
        
        if tag[i] not in IDCharacter:  
            test = True
            break
    
    if test == True:
        print('ERROR: ID must be a number')
        recall = True       
    
    #Used so that recursion only happens once
    if recall == True:
        tag = input('Enter the employee ID (number 7 digits or less):')
        tag = ID(tag)

    #Return the ID to be put into the dictionary
    return tag

#Define the function that will find errors in names
def employeeName(name):
    #Initialize values for tests
    test = False
    i = 0
    
    #Test if name has invalid characters
    for i in range(len(name)):
        
        if name[i] not in nameCharacter:  
            test = True
            break
    
    #Jump out to reset 'for' loop and begin recursion
    if test == True:
        print('ERROR: name can not include', name[i])
        name = input('Enter the employee name:')
        name = employeeName(name)
    
    #Return the name to be put into the dictionary
    return name

#Define the function that will find errors in emails
def employeeEmail(email):
    #Initialize values for tests
    test = False
    i = 0

    #Test if email has invalid characters
    for i in range(len(email)):
        
        if email[i] in emailIllegalCharacter:  
            test = True
            break
    
    #Jump out to reset 'for' loop and begin recursion
    if test == True:
        print('ERROR: email can not include', email[i])
        email = input('Enter the employee email:')
        email = employeeEmail(email)
    
    #Return the name to be put into the dictionary
    return email

#Define the function that will find errors in address'
def employeeAddress(address):
    #Initialize values for tests
    test = False
    i = 0

    #Test if address has invalid characters
    for i in range(len(address)):
        
        if address[i] in addressIllegalCharacter:  
            test = True
            break
    
    #Jump out to reset 'for' loop and begin recursion
    if test == True:
        print('ERROR: address can not include', address[i])
        address = input('Enter the employee address:')
        address = employeeAddress(address)
    
    #Return the address to be put into the dictionary
    return address

#Define the function that will find errors in salaries
def employeeSalary(salary):
    #Initialize values for tests
    count = 0
    test = False
    recall = False

    #Test salary has invalid characters
    for i in range(len(salary)):
        if salary[i] not in salaryCharacter:  
            test = True
            break
        
        #Count decimal places so there is only one
        if salary[i] == '.':
            count = count + 1

    #Catch decimal error
    if count > 1:
        print('ERROR: only enter 1 decimal or less')
        recall = True

    #Catch invalid characters
    if test == True:
        print('ERROR: salary can not include', salary[i])
        recall = True  

    #Determine if input number is in the right range
    if recall == False:
        if(round(float(salary), 2) < 18 or round(float(salary), 2) > 27):
            print('ERROR: enter number between 18 and 27')
            recall = True

    #Begin recursion if errors arise
    if recall == True:
        salary = input('Enter the employee salary (18 - 27):')
        salary = employeeSalary(salary)
    
    #Float to two decimal places and return the salary to be put into the dictionary
    salary = str(round(float(salary), 2))
    return salary


#Loop to allow user to exit when they want
while (repeat != 'n'):

    #Use all functions to put into dictionary
    dict1['Employee ID'] = ID(input('Enter the employee ID (number 7 digits or less):'))
    dict1['Employee Name'] = employeeName(input('Enter the employee name:'))
    dict1['Employee Email Address'] = employeeEmail(input('Enter the employee email:'))
    dict1['Employee Address'] = employeeAddress(input('Enter the employee address:'))
    dict1['Employee Salary'] = employeeSalary(input('Enter the employee salary (18 - 27):'))

    #Make a copy of the dictionary so it doesn't repeat the same dictionary in the list
    dict1_copy = dict1.copy()
    #Append the dictionary to the list
    employeeData.append(dict1_copy)

    #Allow user to repeat
    repeat = input('\nWould you like to enter another employee? (y/n):')

#Update strings and values for specified modifications
for i in range(len(employeeData)):
    employeeData[i]['Employee Name'] = employeeData[i]['Employee Name'] + " IT Department"

    employeeData[i]['Employee Salary'] = str(round(float(employeeData[i]['Employee Salary']) * 1.3, 2))

#Finally print out updated list of dictionaries
print()
print("Updated Employee Data: ", employeeData)