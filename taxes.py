def main():
    assessed_value = 0
    property_tax = 0
    
    value = float(input("Enter the actual value: ")) 
    while value <= 0:
        print("Actual value must be >=0")
        value = float(input("Enter the actual value: ")) 
    
    assessed_value = (value * 0.60)
    property_tax = (assessed_value * .0072)


    show_property_tax(assessed_value,property_tax)
    

def show_property_tax(assessed_value, property_tax):
    print("Assessed value:" ,'${:,.2f}'.format(assessed_value))
    print("Property Tax" ,'${:,.2f}'.format(property_tax))

main()