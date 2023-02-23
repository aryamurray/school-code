SSD = [['1', '250 GB', 69.99], ['2', '500 GB', 93.99], ['3', '4 TB', 219.99]]
HDD = [['1', '500 GB', 106.33], ['2', '1 TB', 134.33]]
CPU = [['1', 'Intel Core i7-11700K', 499.99], ['2', 'AMD Ryzen 7 5800X', 312.99]]
MOTHERBOARD = [['1', 'MSI B550-A PRO', 197.46], ['2', 'MSI Z490-A PRO', 262.30]]
RAM = [['1', '16 GB', 82.99], ['2', '32 GB', 174.99]]
GRAPHICS_CARD = [['1', 'MSI GeForce RTX 3060 12GB', 539.99]]
PSU = [['1', 'Corsair RM750', 164.99]]
CASE = [['1', 'Full Tower (black)', 149.99], ['2', 'Full Tower (red)', 149.99]]

PREBUILTS = [['1', 'Legion Tower Gen 7 with RTX 3080 Ti', 3699.99], ['2',
'SkyTech Prism II Gaming PC', 2839.99], ['3', 'ASUS ROG Strix G10CE Gaming PC',
1099.99]]

totalcost = []
cost = 0



def pickcpu():
    while True:
        print("First, let's pick a CPU.")
        print("1 : %s, $%.2f" % (CPU[0][1],CPU[0][2]))
        print("2 : %s, $%.2f" % (CPU[1][1],CPU[1][2])) 
        choice = int(input("Choose the number that corresponds with the part you want:"))
        global cost 
        if choice == 1: 
            cost = (CPU[0][2])
            pickmotherboard(1)
            break
        elif choice ==2:
            cost = (CPU[1][2])
            pickmotherboard(2)
            break
        else:
            continue
def pickmotherboard(x):
    while True:
        print("Next, let's pick a compatible motherboard")
        global cost 
        if x == 1:
            while True:
                print("1 : %s, $%.2f" % (MOTHERBOARD[1][1],CPU[1][2]))
                choice = int(input("Choose the number that corresponds with the part you want:"))
                if choice == 1:
                    cost += (MOTHERBOARD[1][2])
                    break
                else:
                    continue
        elif x == 2:
            while True:
                print("1 : %s, $%.2f" % (MOTHERBOARD[0][1],CPU[0][2]))
                choice = int(input("Choose the number that corresponds with the part you want:"))
                if choice == 1:
                    cost += (MOTHERBOARD[0][2])
                    break
                else:
                    continue
        pickram()
def pickram():
    while True:
        print("Next, Let's pick your RAM.")
        print("1 : %s, $%.2f" % (RAM[0][1],RAM[0][2]))
        print("2 : %s, $%.2f" % (RAM[1][1],RAM[1][2])) 
        choice = int(input("Choose the number that corresponds with the part you want:"))
        global cost
        if choice == 1:
            cost += (RAM[0][2])
            break
        elif choice == 2:
            cost += (RAM[1][2])
            break
        else:
            continue
    pickpsu()

def pickpsu():
    while True:
        print("Next, Let's pick your PSU.")
        print("1 : %s, $%.2f" % (PSU[0][1],PSU[0][2]))
        choice = int(input("Choose the number that corresponds with the part you want:"))
        global cost
        if choice == 1:
            cost += (PSU[0][2])
            break
        else:
            continue
    pickcase()

def pickcase():
    while True:
        print("Next, Let's pick your case.")
        print("1 : %s, $%.2f" % (CASE[0][1],CASE[0][2]))
        print("2 : %s, $%.2f" % (CASE[1][1],CASE[1][2])) 
        choice = int(input("Choose the number that corresponds with the part you want:"))
        global cost
        if choice == 1:
            cost += (CASE[0][2])
            break
        elif choice == 2:
            cost += (CASE[1][2])
            break
        else:
            continue
    pickssd()

def pickssd():
    while True:
        print("Next, Let's pick an SSD (Optional, but you must have at least one SSD or HDD).")
        print("1 : %s, $%.2f" % (SSD[0][1],SSD[0][2]))
        print("2 : %s, $%.2f" % (SSD[1][1],SSD[1][2])) 
        print("3 : %s, $%.2f" % (SSD[2][1],SSD[2][2])) 
        choice = input("Choose the number that corresponds with the part you want (or X to not get an SSD):")
        global cost
        if choice == 1:
            cost += (SSD[0][2])
            break
        elif choice == 2:
            cost += (SSD[1][2])
            break
        elif choice == 3:
            cost += (SSD[2][2])
            break
        elif choice.lower == "x":
            pickhdd(False)
            break
        else:
            continue
    pickhdd(True)



def pickhdd(x):
    while True:
        print("Next, Let's pick an HDD (Optional, but you must have at least one SSD or HDD).")
        print("1 : %s, $%.2f" % (HDD[0][1],HDD[0][2]))
        print("2 : %s, $%.2f" % (HDD[1][1],HDD[1][2]))
        global cost
        if x == True:
            choice = input("Choose the number that corresponds with the part you want (or X to not get an HDD):")
            if choice == 1:
                cost += (HDD[0][2])
                break
            elif choice == 2:
                cost += (HDD[1][2])
                break
            elif choice.lower == "x":
                break
            else:
                continue
        elif x == False:
            choice = input("Choose the number that corresponds with the part you want (since you did not get an SSD, you must get an HDD):")
            if choice == 1:
                cost += (HDD[0][2])
                break
            elif choice == 2:
                cost += (HDD[1][2])
                break
            else:
                continue
def pickprebuilt():
    while True:
        print("Great, let's pick a pre-built PC!\n")
        print("Which prebuilt would you like to order?")
        print("1 : %s, $%.2f" % (PREBUILTS[0][1],PREBUILTS[0][2]))
        print("2 : %s, $%.2f" % (PREBUILTS[1][1],PREBUILTS[1][2])) 
        print("2 : %s, $%.2f" % (PREBUILTS[2][1],PREBUILTS[2][2])) 
        choice = int(input("Choose the number that corresponds with the part you want:"))
        if choice == 1:
            break
        elif choice == 2:
            break
        elif choice == 3:
            break
        else:
            continue

def checkout():
    return 0

def pickitems():
    return 0

def main():
    while True:
        print("Welcome to my PC Shop!!")
        choice = int(input("Would you like to build a custom PC? (1), purchase a prebuilt PC (2), or would you like to checkout? (3)"))     
        if choice == 1:
            print("Great! Let's start building your PC!")
            pickcpu()
        elif choice == 2:
            print("Great! Let's pick a pre-built PC!")
            pickprebuilt()
        elif choice == 3:
            checkout()
        else:
            False


main()