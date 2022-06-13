weight = int(input("Enter the weight in pounds or Kg "))
unit = input("(L)bs or (k)g")
if unit.upper() == "L":
    conv = weight*0.45
    print(conv)
else:
    print(weight/0.45)




