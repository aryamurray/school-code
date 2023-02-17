def factorial(n):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)

def helloworld(n):
    for i in range(n):
        print("Hello, World!")


def countVowels(word):
    numVowels = 0
    for letter in word:
        if letter.lower() in "aeiou":
            numVowels +=1
    return numVowels



print(countVowels("arya"))
# print(factorial(7))

