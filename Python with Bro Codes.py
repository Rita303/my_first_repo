#A SIMPLE MAD LIBS GAME
#noun_1= input("Enter a noun(person, place, things): ")
#verb_1= input("Enter a verb ending with 'ing': ") 
#adjective_1= input("Enter an adjective: ")
#adjective_2= input("Enter another adjective: ")
#adverb_1= input("Enter an adverb: ")
#print(f"Today I went to the {adjective_1} zoo. I saw a {noun_1} {verb_1} {adverb_1} in a tree. \nIt was so {adjective_2}! \nThat was the best part of my day.")

#BUILD A CALCULATOR
while True :
 OPERATORS= input(f" Please choose an operator: '+', '-', '*', '/' ")
 num1= float(input("Enter first number: "))
 num2= float(input("Enter another number: "))
#result = round()
 if OPERATORS== '+':
    result = round(num1 + num2, 2)
    print(f"{num1} + {num2} = {result}")
    
 elif OPERATORS == '-':
    result = round(num1 - num2, 2)
    print(f" This {result} is the difference of {num1} - {num2}")
 elif OPERATORS== '*':
    result = round(num1 * num2, 2)
    print(f"This {result} is the product of {num1} * {num2}")
 elif OPERATORS == '/':
    try:
        result = round(num1 / num2, 2)
        print(f"This {result} is the quotient of {num1} / {num2}")
    except ZeroDivisionError:
        print(f"Error! {num1} can not be divided by 0")
    else:
        print("Invalid operator. Please try again.")
    
 cont = input("Do you want to calculate something else? (yes to continue, no to exit): ").lower()
 if cont != 'yes':
        print("Calculator exited. Bye!")
        break


# ...existing code...
