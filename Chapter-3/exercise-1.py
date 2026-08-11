# Retrieving user inputs, hours and rate, for calculating pay, fixed with overtime pay if applicable.
varHours = float(input("Enter hours worked: ")) # Retrieve hours worked from user
varRate = float(input("Enter hourly rate: ")) # Retrieve hourly rate from user

if varHours >= 0: # Check if hours worked is a positive number or zero
    if varRate >= 0: # Check if hourly rate is a positive number or zero
        if varHours > 40: # Check if hours worked is greater than 40 to calculate overtime pay
           varOvertimeHours = varHours - 40 
           varPay = (40 * varRate) + ((varOvertimeHours * varRate) * 1.5)  # Calculate pay with overtime pay if applicable
        else:   
            varPay = varHours * varRate # Calculate pay without overtime pay if applicable
        print("Pay:", varPay) # Print the calculated pay
    else:
        print("Invalid rate entered. Enter a positive number or zero.")  
else:
    print("Invalid hours entered. Enter a positive number or zero.")