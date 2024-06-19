def celcius_to_fareignheight(cel):
    faren = (cel/5)*9 + 32
    return faren

temp = int(input("Enter temperature in celcius : "))
print(celcius_to_fareignheight(temp))