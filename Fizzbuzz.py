

currentNumber = int(input("input a number"))
print (currentNumber)
my_file.open("fizzbuzz.txt", w+)
for loopCounter in range(0, currentNumber):
    if loopCounter %3 == (0):
        print("FIZZ" , currentNumber)
    my_file.write(str() +  "\n")





