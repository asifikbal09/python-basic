year = int(input("Enter the year: "))
if year%4==0 and year%400==0:
    print("Leap year")
else:
    print("Not Leap year")