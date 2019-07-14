#raises numbers to powers
print(2**3)

base_num = float(input("Pic a number to raise: "))
power_num = float(input("Pic your power number: "))

def raise_to_power (base_num, power_num): #function takes 2 arguments
    result = 1 # variable where we store the loop result
    for index in range(power_num): # loop which allows of an unknown power
        result = result * base_num # loop executing the power calculation
    return result #returning the unknow power to be used





