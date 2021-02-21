num = int(input("Enter a two-digit number: "))
ones = num % 10
tens = num//10
sum = ones + tens
print("The sum is: " + str(sum))
print("The reversal is: " + str(ones) + str(tens) )
