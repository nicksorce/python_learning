def unknownList ():
    print("What is the unknown?")
    print("")
    print("1.Initial Pressure")
    print("2.Final Pressure")
    print("3.Initial Temperature")
    print("4.Final Temperature")
    print("5.Internal Energy")
    print("6.Work done by/to the system")
    print("7.Number of moles in the system")
    print("8.Heat Transfered to the system")
    print("")
    unknown = int(input("Choose (1), (2), (3), (4), (5), (6), (7), or (8) : "))
    
    return unknown


# main routine 
     
print("Which type of system?")
print("1.Isovolumetric")
print("2.Isobaric")
print("3.Isothermal")
print("4.Adiabetic")
system = int(input("Enter (1), (2), (3), or (4) : "))
print("")
if system == 1:
    unknownV = unknownList()
    if unknownV == 1:
        print("")
        print("These are the equations for initial pressure")
        print("P1 = (P2 * T1)/T2")
        print("P1 = (nRT1)/V1)")
        print("")
    elif unknownV == 2:
        print("")
        print("These are the equations for final pressure")
        print("P2 = (P1 * T2)/T1")
        print("P2 = (nRT2)/V2)")
        print("")
    elif unknownV == 3:
        print("")
        print("These are the equations for initial temperature")
        print("T1 = (T2 * P1)/P2")
        print("T1 = T2 -(U/(n * Cv)")
        print("")    
    elif unknownV == 4:
        print("")
        print("These are the equations for final temperature")
        print("T2 = (T1 * P2)/T2")
        print("T2 = T1 + (U/(n * Cv)")
        print("")
    elif unknownV == 5:
        print("")
        print("These are the equations for internal energy")
        print("U = Qv")
        print("U = n * Cv * (T2-T1)")
        print("")
    elif unknownV == 6:
        print("")
        print("Work for a isovolumetric system is always zero")
        print("")
    elif unknownV == 7:
        print("")
        print("These are the equations for number of moles")
        print("n = (P * V)/(R * T)")
        print("n = (U2 - U1)/(Cv * (T2 - T1))")
        print("")
    elif unknownV == 8:
        print("")
        print("These are the equations for heat transfer")
        print("**NOTE**")
        print("If final temperature is larger than initial temperature, heat transfer will be positive")
        print("If initial temperature is larger than final temperature, heat transfer will be negative")
        print("Qv = U")
        print("Q = n * Cv (T2-T1)")
        print("")
elif system == 2:
    unknownB = unknownList()
    if unknownB == 1:
        print("")
        print("Pressure is constant in this system, initial pressure = final pressure")
        print("")
    elif unknownB == 2:
        print("")
        print("Pressure is constant in this system, initial pressure = final pressure")
        print("")




     


