def Moneybucket(): #Moneybucket interest code begins
    user_salary = int(input("What's Your salary?"))

   #calculating the amount of
    Blow = user_salary * 60/100

    Daily_expense = 60/100 * Blow
    splurge = 10/100 * Blow
    fire_extinguisher =  20/100 * Blow

    # Blow calculation
    grow = 20/100 * Blow

    #Mojo calculation
    Mojo = 20/100 * Blow

    # blow print
    print(f'blow= {Blow}')

    # daily expense print
    print(f'Daily_expense = {Daily_expense}')

    # Splurge print
    print(f'splurge = {splurge}')

    # Grow print
    print(f'grow = {grow}')

    # Mojo print
    print(f'Mojo = {Mojo}')





    return # MoneyBucket code ends
def Compound_Interest(): # compund interest code begins
    Age_started_investing = int(input('Enter your age when you started investing: '))  # Obtaining when the user started investiing
    Annual_Interest = int(input('Enter the annual interest return (in decimal): '))  # Asking user for the interest return
    amount_invested_each_year = int(input('Enter the amount that you will invest: '))  # Getting the amount they will invest each year
    total = 0 # Starting the total set price

    # Heading
    print('Age == Investment == Total')
    for year in range(Age_started_investing, 61):  # Allows only under 61

        total = amount_invested_each_year + total  # Calculation of the total by adding Amount with total

        total = (total * Annual_Interest/100) + total  # Multiplying the interest with the total and adding the total after


        total = int(round(total, 0)) #Rounds the amount
        print(f'{year} == ${amount_invested_each_year} == ${total}')  # Calculations for the table



    return #Compund interest code ends



#welcomes user
print('Welcome to BetterMoney')
#tells user to choose option
print('choose your option for BetterMoney')
#gets users chpice
User_choice = int(input('Enter "1" for money bucket and "2" for Compound interest:'))
#money bucket choice
if User_choice  == 1:
    Moneybucket()
#Compound Interest choice
elif User_choice == 2:
    Compound_Interest()
else:
    print('invalid choice X') #cant,  choose other



