# making conversion calculator
# By: Jin Starks

# user input in length
UserInput = float(input("What number to convert? "))
print(UserInput)
# choose starting unit
InputUnit = input("In what Units? ")
print(InputUnit)
# choose ending unit
# OutputUnit = input("Convert to what Units? ")
# print(OutputUnit)
# conversion calculation in to mm -> in * 25.4 and mm to in -> mm / 25.4
# convert in to mm
if(InputUnit == 'in'):
    Output = UserInput * 25.4
    OutputUnit = "in"
elif(InputUnit == 'mm'):
    Output = UserInput / 25.4
    OutputUnit = "mm"
else:
    print("Not a valid Unit!")
# display results
print(Output, OutputUnit)