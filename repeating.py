import random 
count = 0
for x in range(10001):
    num1 = random.randint(1,9)
    num2 = random.randint(1,9)
    num3 = random.randint(1,9)
    if num1 == num2:
        if num2 == num3:
            print("three repeating")
            print(num1,num2,num3)
            count += 1
    elif num1 != num2:
        print("not equal")
        print(num1,num2,num3)
     
print(count)
percentage = float(count/10000*100)
print(percentage,"Percent of repeating numbers")
