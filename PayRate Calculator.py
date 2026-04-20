while True:
    msg = ("Do you want to calculate \n1. Yearly Salary\n2. Hourly Calculate. \nType 1 or 2 \n" )
    user_in = int(input(msg))
    if user_in == 1:
        hourly = input("Enter the hourly rate: \n")
        yearly = int(hourly) * 40 * 4 *12
        take_home = yearly * 0.75
        print("Your pay before taxes is: $" + str(yearly))
        print("Your take home pay is: $" + str(take_home))
        print("\n______________")
    else:
        year_salary = input("Enter the year salary: \n")
        hour_rate = ((int(year_salary) / 12) / 4) / 40
        print("Your hourly rate is: $" + str(hour_rate))
    



