s1 ="ipad"
s2="iphone"
model=14
s3 = s1 + " " + s2 + str(model)     #concat

dash="-"
line = dash * 50  # line = dash +dash+dash ..... 50 times

print(s3)
print(line)
print(len(s3)+ 8)

#############################################
nine= "9"
seven= "7"
pi="3.14"
mult= int(nine) * int(seven) * float(pi) # "9" * "7"
print(mult)
print(line)

####################################

fname="Johnnyaskldfjasd^"
lname="Doe"
init = fname[0] +"."+ lname[0]
print(init)
print(fname[2])

#i want to print the last letter in fname?
lastIndex = len(fname) - 1
print(fname[lastIndex])
print(line)
##############################
#methods
lname="John DoE "
# print(lname.lower())
# print(lname.upper())

anotherName = lname.replace("DoE", "Smith")
print(anotherName)
print(lname)
print(line)

####################################
#escape seq
print("*\n*\n\n$") #\n means a new line
print("@\t@") # \t means a big space "tab"
print("c\\c")
print(line)
####################################
# mname = input()
# tname = input()
# print("Hello "+mname + " " + tname)
# print(line)

####################################
# #write a prog to get two numbers from the user and just print the addition
# a= int(input("please enter the first num:"))
# b= int(input("please enter the second num:"))
# print("The result is:",a+b)
####################################


# print("a"+9)
# print("a"+"9")
# print("a",9,7,"8",9,lname)
print(line)