# Hold all our lists at the top for usage later

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

#Init our final cost list which is printed at the end as well as the cost
#variable that is used to add prices during the custom PC build(is added to the list at the end)
totalcost = []
cost = 0

#Function to choose the cpu
def pickcpu():
    while True:
        print("First, let's pick a CPU.")
        print("1 : %s, $%.2f" % (CPU[0][1],CPU[0][2]))
        print("2 : %s, $%.2f" % (CPU[1][1],CPU[1][2])) 
        choice = input("Choose the number that corresponds with the part you want:")
        global cost 
        global cpu
        if choice == "1": 
            cost = (CPU[0][2])
            cpu = 1
            break
        elif choice == "2":
            cost = (CPU[1][2])
            cpu = 2
            break
        else:
            continue
    
#Function that chooses the motherboard based on a compatable CPU chosen beforehand
def pickmotherboard(cpu):
    print("Next, let's pick a compatible motherboard")
    global cost 
    if cpu == 1:
        while True:
            print("2 : %s, $%.2f" % (MOTHERBOARD[1][1],CPU[1][2]))
            choice = input("Choose the number that corresponds with the part you want:")
            if choice == "2":
                cost += (MOTHERBOARD[1][2])
                break
            else:
                continue
    elif cpu == 2:
        while True:
            print("1 : %s, $%.2f" % (MOTHERBOARD[0][1],CPU[0][2]))
            choice = input("Choose the number that corresponds with the part you want:")
            if choice == "1":
                cost += (MOTHERBOARD[0][2])
                break
            else:
                continue
    
#Choose between two capacities of ram
def pickram():
    while True:
        print("Next, Let's pick your RAM.")
        print("1 : %s, $%.2f" % (RAM[0][1],RAM[0][2]))
        print("2 : %s, $%.2f" % (RAM[1][1],RAM[1][2])) 
        choice = input("Choose the number that corresponds with the part you want:")
        global cost
        if choice == "1":
            cost += (RAM[0][2])
            break
        elif choice == "2":
            cost += (RAM[1][2])
            break
        else:
            continue
    
#Don't really have an option here, you're just getting the only PSU
def pickpsu():
    while True:
        print("Next, Let's pick your PSU.")
        print("1 : %s, $%.2f" % (PSU[0][1],PSU[0][2]))
        choice = input("Choose the number that corresponds with the part you want:")
        global cost
        if choice == "1":
            cost += (PSU[0][2])
            break
        else:
            continue
    
#picking your case
def pickcase():
    while True:
        print("Next, Let's pick your case.")
        print("1 : %s, $%.2f" % (CASE[0][1],CASE[0][2]))
        print("2 : %s, $%.2f" % (CASE[1][1],CASE[1][2])) 
        choice = input("Choose the number that corresponds with the part you want:")
        global cost
        if choice == "1":
            cost += (CASE[0][2])
            break
        elif choice == "2":
            cost += (CASE[1][2])
            break
        else:
            continue
#Picking your ssd (if any)
def pickssd():
    while True:
        print("Next, Let's pick an SSD (Optional, but you must have at least one SSD or HDD).")
        print("1 : %s, $%.2f" % (SSD[0][1],SSD[0][2]))
        print("2 : %s, $%.2f" % (SSD[1][1],SSD[1][2])) 
        print("3 : %s, $%.2f" % (SSD[2][1],SSD[2][2])) 
        choice = input("Choose the number that corresponds with the part you want (or X to not get an SSD):")
        global cost
        global bought_ssd
        bought_ssd = True
        if choice == "1":
            cost += (SSD[0][2])
            break
        elif choice == "2":
            cost += (SSD[1][2])
            break
        elif choice == "3":
            cost += (SSD[2][2])
            break
        elif choice == "X" or "x":
            bought_ssd = False
            break
        else:
            continue
    
#Picking your hdd (must buy one if no ssd was bought)
def pickhdd(bought_ssd):
    while True:
        print("Next, Let's pick an HDD (Optional, but you must have at least one SSD or HDD).")
        print("1 : %s, $%.2f" % (HDD[0][1],HDD[0][2]))
        print("2 : %s, $%.2f" % (HDD[1][1],HDD[1][2]))
        global cost
        if bought_ssd == True:
            choice = input("Choose the number that corresponds with the part you want (or X to not get an HDD):")
            if choice == "1":
                cost += (HDD[0][2])
                break
            elif choice == "2":
                cost += (HDD[1][2])
                break
            elif choice == "x" or "X":
                break
            else:
                continue
        elif bought_ssd == False:
            choice = input("Choose the number that corresponds with the part you want (since you did not get an SSD, you must get an HDD):")
            if choice == "1":
                cost += (HDD[0][2])
                break
            elif choice == "2":
                cost += (HDD[1][2])
                break
            else:
                continue
    
#Can choose to buy gfx card if you want
def pickgfx():
    while True:
        print("Next, Let's pick your graphics card (or X to not get a graphics card).")
        print("1 : %s, $%.2f" % (GRAPHICS_CARD[0][1],GRAPHICS_CARD[0][2]))
        choice = input("Choose the number that corresponds with the part you want:")
        global cost
        if choice == "1":
            cost += (GRAPHICS_CARD[0][2])
            break
        elif choice == "x" or "X":
                break
        else:
            continue
#Final build message once all parts are chosen
def build_message():
    global cost
    global totalcost
    print("You have selected all of the required parts! Your total for this PC is %.2f" % (cost))
    cost = round(cost, 2)
    totalcost.append(cost)

#Choosing prebuilt PC function. Essnetially the same as before except it's immediately adding the cost 
#to the list from the prebuilt choices
def pickprebuilt():
    while True:
        print("Great, let's pick a pre-built PC!")
        print("Which prebuilt would you like to order?")
        print("1 : %s, $%.2f" % (PREBUILTS[0][1],PREBUILTS[0][2]))
        print("2 : %s, $%.2f" % (PREBUILTS[1][1],PREBUILTS[1][2])) 
        print("3 : %s, $%.2f" % (PREBUILTS[2][1],PREBUILTS[2][2])) 
        choice = int(input("Choose the number that corresponds with the part you want:"))
        if choice == 1:
            totalcost.append(PREBUILTS[0][2])
            print("Your total cost for this prebuilt is $%.2f" % (PREBUILTS[0][2]))
            break
        elif choice == 2:
            totalcost.append(PREBUILTS[1][2])
            print("Your total cost for this prebuilt is $%.2f" % (PREBUILTS[1][2]))
            break
        elif choice == 3:
            totalcost.append(PREBUILTS[2][2])
            print("Your total cost for this prebuilt is $%.2f" % (PREBUILTS[2][2]))
            break
        else:
            continue
#Kind of a redundant function but it was required in the outline.
def pickitems():
    print(totalcost)

def main():
    while True:
        choice = input("Would you like to build a custom PC? (1), purchase a prebuilt PC (2), or would you like to checkout? (3)")     
        if choice == "1":
            print("Great! Let's start building your PC!")
            pickcpu()
            pickmotherboard(cpu)
            pickram()
            pickpsu()
            pickcase()
            pickssd()
            pickhdd(bought_ssd)
            pickgfx()
            build_message()
        elif choice == "2":
            pickprebuilt()
        elif choice == "3":
            pickitems()
        elif choice == "q" or "exit":
            exit()
        else:
            continue
        
#This is where all the magic actually happens
print("Welcome to my PC Shop!!")
main()