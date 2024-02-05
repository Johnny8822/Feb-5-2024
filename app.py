# //////??CODE 1
# creating an empty list
resistance_vals = []
 
# number of elements as input
r = int(input("Enter the number of resistors in parallel: "))
 
# iterating till the range
for i in range(0, r):
    resistor_value = float(input())
    # adding the resistor value to the list
    resistance_vals.append(resistor_value)  
 
print(resistance_vals)

def parallel(*resist):
 inv_resist = [1 / j for j in resistance_vals] 
 total_inv_resist = sum(inv_resist)
 resistance_eff =   1/total_inv_resist
 return(resistance_eff)

result = parallel(*resistance_vals)
print(f"The effective reisitance through the circuit is {result} Ohms")   


# ///////// CODE 2 

v = int(input("Enter the value of the voltage source: "))

resistance_vals = []

# number of elements as input
r = int(input("Enter the number of resistors in series: "))

# iterating till the range
for i in range(0, r):
    resistor_value = float(input())
    # adding the resistor value to the list
    resistance_vals.append(resistor_value)

# print(resistance_vals)

def potential_divider(voltage, resistor_values):
    total_resistance = sum(resistor_values)
    voltage_values = [(voltage * val) / total_resistance for val in resistor_values]
    return voltage_values

voltage = v
result = potential_divider(voltage, resistance_vals)
print(f"Voltage drop accross the resistors: {resistance_vals} in ohms and in the order they were entered: {result} volts") 


# //////////CODE 3  

Temp =int(input("Enter the value of the patients temperature: "))
print('Enter "C" for Celsius OR "F" for Farenheit') 

Unit_Temp = input()

def temperature_check(temp_patient, unit_F_C):
    

    if unit_F_C == 'F':
        
        temp_patient = (temp_patient + 32) * 9/5  # Convert Celsius to Farenheit

    if temp_patient < 100.4:
        return "the patient is hypothermic"
    
    elif 95.9 <= temp_patient <= 99.5:
        return "The patient has a normal body temperature."
    
    else:
        return "the patient is hypothermic."


body_temp = Temp
temperature_unit = Unit_Temp  
result = temperature_check(body_temp, temperature_unit)
print(result)
