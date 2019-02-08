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
    print(" ")
    print("Based on your height and weight, you have a body mass index (BMI) of: ","%.2f"%bmi)
    if bmi < 18.5:
        print("This is considered underweight")
        print(" ")
    elif bmi >= 18.5 and bmi <= 25:
        print("This is considered normal weight")
        print(" ")    
    elif bmi >=25 and bmi <= 30:
        print("This is considered overweight")
        print(" ")
    elif bmi >= 30:
        print("This is considered heavily overweight")
        print(" ")        
def askSex():
    sex = 0
    sexs = []
    sexs.append("Male")
    sexs.append("Female")
    while True:
        try:
            print("Are you Male or Female?")
            print("1.",sexs[0])
            print("2.",sexs[1])
            selection = int(input("Please choose (1) for Male and (2) for Female: "))
            print("")
            if selection == 1:
                sex = ("Male")
                break
            elif selection  == 2:
                sex = ("Female") 
                break  
            else:
                print("Invalid choise, please choose (1) for male or 2 for female")
                print("")
                sex = askSex()
                break
        except ValueError:
            print("Invalid choise, please choose (1) for male or (2) for female")
            print("")
            sex = askSex()
            break        
    exit
    return sex
def activityLevel():
    actLevel = 0
    levels = []
    levels.append("Sedentary")
    levels.append("Lightly Active")
    levels.append("Active")
    levels.append("Highly Active")
    while True:
        try:
            print("HOW ACTIVE ARE YOU?")
            print("____________________________________________________________________________________________________________________________________")
            print("1.",levels[0],"     You do less than 30 minutes of intentional exercise per day") 
            print("2.",levels[1],"You perform daily exercise that is equal to 30 minutes of brisk walking (100-160 calories burned)")
            print("3.",levels[2],"        You perform daily exercise that is equal to 1 hour and 45 minutes of brisk walking (450-550 calories burned)")
            print("4.",levels[3]," You perform daily exercise that is equal to 4 hours and 15 minutes of brisk walking(1,000-1,500 calories burned)")
            print("____________________________________________________________________________________________________________________________________")
            print("")
            print("***NOTE*** if you fall inbetween one of these, choose the lower of the two")
            print("")
            level = int(input("Please choose (1) for Sedentary, (2) for Lightly Active, (3) for Active, and (4) for Highly Active: "))
            print("")
            if level == 1:
                actLevel = ("Sedentary")
                break
            elif level == 2:
                actLevel = ("Lightly Active")
                break    
            elif level == 3:
                actLevel = ("Active")
                break
            elif level == 4:
                actLevel = ("Highly Active")
                break
            else: 
                print("Invalid choice, please choose (1) for Sedentary, (2) for Lightly Active, (3) for Active, and (4) for Highly Active")   
                print("")
                actLevel = activityLevel()
                break
        except ValueError:  
            print("Invalid choice, please choose (1) for Sedentary, (2) for Lightly Active, (3) for Active, and (4) for Highly Active")    
            print("")
            actLevel = activityLevel()
            break
    exit
    return actLevel
def metobolicRate():
    multiplier = 0
    if actLevel == ("Sedentary"):
        multiplier = 1.2
    elif actLevel == ("Lightly Active"):
        multiplier = 1.375
    elif actLevel == ("Active"):
        multiplier = 1.55
    elif actLevel == ("Highly Active"):
        multiplier = 1.725     

    if sex == ("Female"):
        bmr = ((weight * 4.35) + (height * 4.7) - (age * 4.7) + (655)) * multiplier

    elif sex == ("Male"):
        bmr = ((weight * 6.23) + (height * 12.7) - (age * 6.8) + (66)) * multiplier

    return bmr
def goals():
    goal = 0
    hopes = []
    hopes.append("Burn fat and stay same weight")
    hopes.append("Burn fat and loose weight")
    hopes.append("Build muscle and stay same weight")
    hopes.append("Build muscle and gain weight")
    hopes.append("Build muscle and burn fat")
    while True:
        try:
            print("WHAT GOALS DO YOU WISH TO MEET?")
            print("________________________________")
            print("1.", hopes[0])
            print("2.", hopes[1])
            print("3.", hopes[2])
            print("4.", hopes[3])
            print("5.", hopes[4])
            print("________________________________")
            number = int(input("Please choose one of the goals above [(1), (2), (3), (4) or (5)]: "))
            if number == 1:
                goal = ("Burn fat and stay same weight")
                break
            elif number == 2:
                goal = ("Burn fat and loose weight")
                break
            elif number == 3:
                goal = ("Build muscle and stay same weight")
                break
            elif number == 4:
                goal = ("Build muscle and gain weight")  
                break
            elif number == 5:
                goal = ("Build muscle and burn fat")  
                break
            else: 
                print("Invalid choise, please choose (1), (2), (3), (4), or (5)")
                print("")
                goal = goals()
                break
        except ValueError:
            print("Invalid choise, please choose (1), (2), (3), (4), or (5)")
            print("")
            goal = goals()
            break  
    exit 
    return goal        



        

 



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
actLevel = activityLevel()
bmr = metobolicRate()
goal = goals()
print(goal)