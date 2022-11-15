#Detected bigger and smallest number by user input
num1= int(input('Enter your number: '))
num2= int(input('Enter your second compare number: '))
num3= int(input('Enter your third compare number: '))

if num1 > num2 and num1 > num3:
    print(num1)
elif num2>num1 and num2>num3:
    print(num2)
else:
    print(num3)


#Vowel detected
vowel= input("Enter your article: ")
if vowel=="a" or vowel=="e" or vowel=="i" or vowel=="o" or vowel=="u":
    print("This is a vowel")
else:
    print("This is a consonant")
