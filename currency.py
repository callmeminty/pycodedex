co = float(input("Whaty do you have left in pesos? "))
pe = float(input("Whaty do you have left in soles? "))
br= float(input("Whaty do you have left in reais? "))

usd = (co * 0.058 + pe * 0.27 + br * 0.20)

print(usd)
