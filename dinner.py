# Developed by Arya C. Murray
# Date: January 25th, 2022
# Desc: A Program in order to recommend food for multiple dinner guests based on dietary preferences.
# DISCLAIMER: Program assumes that user knows the program syntax.

#Establishing number of dinner invitees and assigning to variable
#valid input is assumed for these integer values

print("Please enter the number of invitees:")
invitees = int(input())

#these variables need to be initialized here . Just adding the initial amounts for each 'food' item to count as we add them

pizza_counter = 0
pasta_counter = 0
steak_counter = 0
falafel_counter = 0
beverage_counter = 0
cost = 0 #initialize the cost variable 

#loop over the number of invitees to attain their preferences
for i in range(invitees):
    print("Please enter the order details for invitee Number %d/%d" % (i+1,invitees))

#store preferenes in boolean variables named after preference types within loop

    print("Do you want a keto friendly meal?")
    if input() == "y":
        keto = True
    else:
        keto = False
    print("Do you want a vegan meal?")
    if input() == "y":
        vegan = True
    else:
        vegan = False
    print("Do you want a Gluten-free meal?")
    if input() == "y":
        gf = True
    else:
        gf = False

    # Creating Space for Aesthetic
    print("_______________________________________________________________\n")

    #Make reccomendations for food based on preferences !
    
    if keto == False and vegan == False and gf == False:
        cost = cost + 5.99
        beverage_counter +=1
    elif keto == False and vegan == False and gf == True:   
        cost = cost + 5.99
        beverage_counter +=1
    elif keto == False and vegan == True and gf == False:
        cost = cost + 48.99
        pasta_counter +=1
    elif keto == True and vegan == False and gf == False:  
        cost = cost + 5.99
        beverage_counter +=1
    elif keto == True and vegan == True and gf == False:
        cost = cost + 44.50
        pizza_counter +=1
    elif keto == False and vegan == True and gf == True:
        cost = cost + 5.99
        beverage_counter +=1
    elif keto == True and vegan == False and gf == True:
        cost = cost + 49.60
        steak_counter +=1
    elif keto == True and vegan == True and gf == True:
        cost = cost + 52.99
        falafel_counter +=1

 # Creating Space for Aesthetic
    print("_______________________________________________________________\n")

    
#Attain how much the user would like to tip, also init the tax stuff.
tax = 1.13
tip = ((int(input("How much do you want to tip your server (% percent)?")) /100) + 1)
after_tax_cost = (cost*1.13)
post_tip_cost = (tip*after_tax_cost)

# Report to the user the orders that they have chosen
print("You have %d invitees with the following orders:" % (invitees))
print(pizza_counter, 'invitees ordered Pizza. The cost is:$%.2f ' % (pizza_counter* 44.50 * tax ))
print(pasta_counter, 'invitees ordered Pasta. The cost is:$%.2f ' % (pasta_counter* 48.99 * tax ))
print(falafel_counter, 'invitees ordered Falafel. The cost is:$%.2f' % (falafel_counter* 52.99 * tax))
print(steak_counter, 'invitees ordered Steak. The cost is:$%.2f ' % (steak_counter* 49.60 * tax))
print(beverage_counter, 'invitees ordered only beverage. The cost is: $%.2f' % (beverage_counter* 5.99 * tax) )

# Creating Space for Aesthetic
print("\n _______________________________________________________________\n")

#Finding and printing the toal cost based on food choices and added tax.
final_cost = (post_tip_cost* 1.13)

print("The total cost before tax is:$%.2f" % (cost))
print("The total cost after tax is %.2f" % (cost*tax))
print("The total cost after a %i%% tip is $%i" % ((tip-1)*100,final_cost))
