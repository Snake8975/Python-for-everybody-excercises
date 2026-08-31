# process of asking Hours worked and Hourly rate
varPromptHours = "Enter Hours: \n"
varHours = float(input(varPromptHours))
varPromptRate = "Enter Rate: \n"
varRate = float(input(varPromptRate))

# showing the value of the Pay and the parameters
print("Enter Hours: ", varHours)
print("Enter Rate: ", varRate)
print("Pay: ", (varHours * varRate) )

# letting the user reads what he typed
import time
time.sleep(2.5)