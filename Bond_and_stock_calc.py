# Project 1
# Bond and Stock Calculator
# Author: Nate Maassen

# q is the variable I used to create an endless while loop until the user inputs 'quit'
q = 0
while q == 0:
    user_inp = input('What would you like to calculate? (Bond, Coupon Bond, or Stock) Enter quit to exit program. ')
    user_inp = user_inp.lower()
    
    
    # here I use the present value formula to determine the price of user's bond
    if user_inp == 'bond':
        FV = float(input('What is the face value of the bond? '))
        i = float(input('What is the yield to maturity on the bond? (in decimal) '))
        n = float(input('How many years between the settlement and maturity date? '))
        print('#' * 100)
        solution = round(((FV) / (1 + i) ** n), 2)
        print(f'Your bond is worth {solution} dollars')
        print('#' * 100)
    # here I use a coupon bond and present value formula
    elif user_inp == 'coupon bond':
        FV = float(input('What is the face value of the bond? '))
        i = float(input('What is the yield to maturity on the bond? (in decimal) '))
        CR = float(input('What is the coupon rate of the bond? (in decimal) '))
        n = float(input('How many years between the settlement and maturity date? '))
        CP = FV * CR
        print('#' * 100)
        solution = round(((CP) / (1 + i) ** n) + ((FV) / (1 + i) ** n), 2)
        print(f'Your bond is worth {solution} dollars')
        print('#' * 100)
    # here I use the Gordon Growth Model to calculate the price of a stock
    elif user_inp == 'stock':
        Do = float(input('How much was the most recent dividend? '))
        g = float(input('What is the expected growth rate in the dividend? (in decimal) '))
        Ke = float(input('What is your required rate of return? (in decimal) '))
        print('#' * 100)
        solution = round((Do * (1 + g)) / (Ke - g), 2)
        
        print(f'Your stock is worth {solution} dollars')
        print('NOTE: this stock was calculated using the Gordon Growth Model. Rates are assumed to be constantly growing.')
        print('#' * 100)
        
    elif user_inp == 'quit':
        exit()
    else:
        print('You did not input an allowed security.')
        


