x=int(input('Enter the number: '))
# % isused to calculate remainder
if x%2==0: #check divisibility with 2
    if x%3==0: # if x%2=0, then check this line
        print("Number is divisible by 2 and 3")
    else:
        print("Number is divisible by 2 only")
        print("x%3= ", x%3)
elif x%3==0: #check thisif x%2 is not zero
    print("Number is divisible by 3 only")
else:
    print("Number is not divisible by 2and 3")
    print("x%2= ", x%2)
    print("x%3= ", x%3)
print("Thank you")


# x = float(input("Enter a number: "))
# if (x%2 ==0):
#     print(f"{x} is even.")
# else:
#     print(f"{x} is not even.")
# print('Bye Bye')


# x=int(input('Enter the number:\t'))
# # % isused to calculate remainder
# if x%2==0:
#  print ("Number is even")
# if x%2!=0:
#  print ("Number is odd")

