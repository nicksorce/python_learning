def askAge():
    while True:
        try:
            age = int(input("How old are you?: "))
            if age > 1 and age < 115:
                break
            elif age < 1 or age > 115:
                print("Invalid choise, please enter your age")
                age = askAge()
                break
            else:
                print("")
                print("Invalid choise, please enter your age")
                age = askAge()
                break
        except ValueError:
                print("")
                print("Invalid choise, please enter your age")
                age = askAge()
                break           
    exit
    return age
def askWeight():
    while True:
        try:
            weight = float(input("How much do you weigh?(in pounds): "))
            if weight > 1 and weight < 1235:
                break
            elif weight < 1 or weight > 1235:
                print("Invalid choise, please enter your weight")
                weight = askWeight()
                break
            else:
                print("")
                print("Invalid choise, please enter your weight")
                weight = askWeight()
                break
        except ValueError:
                print("")
                print("Invalid choise, please enter your weight")
                weight = askWeight()
                break
    exit
    return weight
def askHeight():
    while True:
        try:
            height = int(input("How tall are you in inches?: "))
            if height > 20 and height < 110:
                break
            elif height < 20 or height > 110:
                print("Invalid choice, please enter your height in inches")
                print("") 
                height = askHeight()
                break
            else:
                print("Invalid choice, please enter your height in inches")
                print("") 
                height = askHeight()
                break  
        except ValueError:
                print("")
                print("Invalid choise, please enter your height in inches")
                height = askHeight()
                break
    exit
    return height
def bmi():
    kilo = weight * .45
    meter = height * .025
    squareMeter = meter * meter
    bmi = kilo/squareMeter
    print("Based on your height and weight, you have a body mass index (BMI) of: ","%.2f"%bmi)
    print("")
    if bmi < 18.5:
        print("This is considered underweight")
    elif bmi >= 18.5 and bmi <= 25:
        print("This is considered normal weight")    
    elif bmi >=25 and bmi <= 30:
        print("This is considered overweight")
    elif bmi >= 30:
        print("This is considered heavily overweight")        
def askSex():
    sex = 0
    sexs = []
    sexs.append("Male")
    sexs.append("Female")
    while True:
        try:
            print("1.",sexs[0])
            print("2.",sexs[1])
            selection = int(input("Are you a male or female?: "))
            print("")
            if selection == 1:
                sex = ("male")
                break
            elif selection  == 2:
                sex = ("female") 
                break  
            else:
                print("Invalid choise, please choose 1 for male or 2 for female")
                print("")
                sex = askSex()
                break
        except ValueError:
            print("Invalid choise, please choose 1 for male or 2 for female")
            print("")
            sex = askSex()
            break        
    exit
    return sex

# main routine         
print("Hello, Welcome to Nick's Workout and Nutrition Creator")
print(" ")
print("Please answer the following questions")
print(" ")
age = askAge()
weight = askWeight()
height = askHeight()
bmi()
sex = askSex()
print(sex)
print(age)
