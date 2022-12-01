def Bubble_Sort():
  user_input = input("Enter items (seperate using spaces): ")
  list = user_input.split(" ")
  list_length = len(list)
  swap_made = True
  while swap_made and list_length > 0:
    swap_made = False
    list_length -= 1
    for i in range(0, list_length):
      if list[i] > list[i + 1]:
        temp = list[i]
        list[i] = list[i + 1]
        list[i + 1] = temp
        swap_made = True
  print(list)  

#Main Program
Bubble_Sort()
