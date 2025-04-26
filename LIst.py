import random

# Creating a list named backpack with 15 items, including some duplicates
backpack = [
    "notebook", "pen", "pencil", "eraser", "ruler", 
    "laptop", "charger", "water bottle", "snacks", "headphones", 
    "pen", "notebook", "marker", "sticky notes", "pencil"
]
# learning how to use list comprehension to remove duplicates from the backpack list
# The list comprehension iterates over each item in the backpack and checks if the count of that item is less than 2
backpack[:] = [i for i in backpack if backpack.count(i) < 2]
# Printing the modified backpack list to see the result
#print(backpack)
# code to reverse a list
# Creating a list named data that contains 6 numerals
data = [10, 20, 30, 40, 50, 60]
data.reverse()  # Reversing the order of elements in the data list
#swapping elements in a list
# Swapping the first and last elements of the data list
#print(data)  # Output: [60, 50, 40, 30, 20, 10]
#data[0], data[-1] = data[-1], data[0]  # Swapping the first and last elements
#using temp variable to swap elements
temp = data[1]  # Storing the first element in a temporary variable
data[1] = data[-2]  # Assigning the last element to the first position
data[-2] = temp  # Assigning the value stored in temp to the last position
# Printing the modified data list to see the result after the swap
print(data)  # Output: [60, 20, 30, 40, 50, 10]
#using a for loop to swap out each itment in the list
for i in range(len(data) // 2):  # Looping through half the length of the list
    data[i], data[-i - 1] = data[-i - 1], data[i]  # Swapping elements at positions i and -(i + 1)

#using reversed iterator to swap elements in a list
data_reversed = []
for i in reversed(data):  # Looping through the data list in reverse order
    data_reversed.append(i)  # Printing each element in reverse order

print(data_reversed)  # Output: [10, 50, 40, 30, 20, 60]

### HOW TO SORT A LIST ###

# Creating a list of workdays named workdays
workdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

# Sorting the workdays list in alphabetical order
workdays.sort()

# Printing the sorted workdays list
print(workdays)  # Output: ['Friday', 'Monday', 'Thursday', 'Tuesday', 'Wednesday']

# Creating a list named num filled with random positive and negative numbers
num = [random.randint(-100, 100) for _ in range(20)]

# Sorting the num list in ascending order
num.sort(reverse=True)  # Setting reverse=True to sort in descending order
# Printing the sorted num list        
print(num)  # Output: Sorted list in descending order              
  # Output: Sorted list in descending order