def Binary_Search():
  list = ['a','b','c','d','e','f','g','h','i','j']
  item = input("What do you want to find: ")
  listlength = len(list)
  LowerBound = 0
  UpperBound = listlength - 1
  Found = False
  
  while Found == False and LowerBound <= UpperBound:
    MidPoint = round(LowerBound + (UpperBound - LowerBound)/2)
    if list[MidPoint] == item:
      Found = True
    elif list[MidPoint] < item:
      LowerBound = MidPoint + 1
    else:
      UpperBound = MidPoint - 1
  
  if Found == True:
    print(f"Item found at {MidPoint}")
  elif Found == False:
    print("Item not found in list")


def Linear_Search():
  list = ['a','b','c','d','e','f','g','h','i','j']
  listlength = len(list)
  item = input("What item do you want: ")
  Found = False
  Position = 0
  
  while Found == False and Position <= listlength - 1:
    if item in list[Position]:
      Found = True
    else:
      Position+=1
  
  if Found == True:
    print(f"Item found at {Position}")
  else:
    print("Item not found in list")

#Main Program
user_input = input("Do you want Linear Search or Binary Search: (L/B)")
if user_input == "L":
  Linear_Search()
elif user_input == "B":
  Binary_Search()
else:
  input("Invalid input, either put 'L' or 'B'")
