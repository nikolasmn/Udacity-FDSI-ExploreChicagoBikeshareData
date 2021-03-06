
# coding: utf-8

# Here goes the imports
import csv
import matplotlib.pyplot as plt

# Let's read the data as a list
print("Reading the document...")
with open("chicago.csv", "r") as file_read:
    reader = csv.reader(file_read)
    data_list = list(reader)
print("Ok!")

# Let's check how many rows do we have
print("Number of rows:")
print(len(data_list))

# Printing the first row of data_list to check if it worked.
print("Row 0: ")
print(data_list[0])
# It's the data header, so we can identify the columns.

# Printing the second row of data_list, it should contain some data
print("Row 1: ")
print(data_list[1])

input("Press Enter to continue...")

# TASK 1
# TODO: Print the first 20 rows using a loop to identify the data.
print("\n\nTASK 1: Printing the first 20 samples")

for item in range(21):
    print(str(item))
    print(data_list[item])
  
# Let's change the data_list to remove the header from it.
data_list = data_list[1:]

# We can access the features through index
# E.g. sample[6] to print gender or sample[-2]

input("Press Enter to continue...")

# TASK 2
# TODO: Print the `gender` of the first 20 rows

print("\nTASK 2: Printing the genders of the first 20 samples")

for item in range(20):
    print(str(item + 1))
    print(data_list[item][6])

# Cool! We can get the rows(samples) iterating with a for and the columns(features) by index.
# But it's still hard to get a column in a list. Example: List with all genders

input("Press Enter to continue...")

# TASK 3
# TODO: Create a function to add the columns(features) of a list in another list in the same order
def column_to_list(data, index):
    """ Get a column from a list and create new list with this values
      Args:
          param1: The list with all the data.
          param2: The index of the list that we want do copy.
      Returns:
          List of the values of a column the original 
    """ 
    column_list = []
    # Tip: You can use a for to iterate over the samples, get the feature by index and append into a list
    for item in range(len(data)):
        column_list.append(data[item][index])
    return column_list

# Let's check with the genders if it's working (only the first 20)
print("\nTASK 3: Printing the list of genders of the first 20 samples")
print(column_to_list(data_list, -2)[:20])

# ------------ DO NOT CHANGE ANY CODE HERE ------------
assert type(column_to_list(data_list, -2)) is list, "TASK 3: Wrong type returned. It should return a list."
assert len(column_to_list(data_list, -2)) == 1551505, "TASK 3: Wrong lenght returned."
assert column_to_list(data_list, -2)[0] == "" and column_to_list(data_list, -2)[1] == "Male", "TASK 3: The list doesn't match."
# -----------------------------------------------------

input("Press Enter to continue...")
# Now we know how to access the features, let's count how many Males and Females the dataset have
# TASK 4
# TODO: Count each gender. You should not use a function to do that.
male = 0
female = 0

for item in range(len(data_list)):
    if data_list[item][-2]=="Male":
        male += 1
    elif data_list[item][-2]=="Female":
        female += 1

# Checking the result
print("\nTASK 4: Printing how many males and females we found")
print("Male: ", male, "\nFemale: ", female)

# ------------ DO NOT CHANGE ANY CODE HERE ------------
assert male == 935854 and female == 298784, "TASK 4: Count doesn't match."
# -----------------------------------------------------

input("Press Enter to continue...")

# Why don't we creeate a function to do that?
# TASK 5
# TODO: Create a function to count the genders. Return a list
# Should return a list with [count_male, counf_female] (e.g., [10, 15] means 10 Males, 15 Females)
def count_gender(data_list):
    """ Counts the gender of a given list
        Args:
            param1: List with the values 
        Returns:
          List with the male and female countings
    """
    male = 0
    female = 0
    
    for item in range(len(data_list)):
        if data_list[item][-2]=="Male":
            male += 1
        elif data_list[item][-2]=="Female":
            female += 1

    return [male, female]

print("\nTASK 5: Printing result of count_gender")
print(count_gender(data_list))

# ------------ DO NOT CHANGE ANY CODE HERE ------------
assert type(count_gender(data_list)) is list, "TASK 5: Wrong type returned. It should return a list."
assert len(count_gender(data_list)) == 2, "TASK 5: Wrong lenght returned."
assert count_gender(data_list)[0] == 935854 and count_gender(data_list)[1] == 298784, "TASK 5: Returning wrong result!"
# -----------------------------------------------------

input("Press Enter to continue...")

# Now we can count the users, which gender use it the most?
# TASK 6
# TODO: Create a function to get the most popular gender and print the gender as string.
# We expect to see "Male", "Female" or "Equal" as answer.
def most_popular_gender(data_list):
    """ Identifies the most popular gender of a given list
      Args:
          param1: List with the values 
      Returns:
          String with the most popular gender
    """
    answer = ""
    amount = count_gender(data_list)
    if amount[0] > amount[1]:
        answer = "Male"
    elif amount[0] < amount[1]:
        answer = "Female"
    else:
        answer = "Equal"
    return answer

print("\nTASK 6: Which one is the most popular gender?")
print("Most popular gender is: ", most_popular_gender(data_list))

# ------------ DO NOT CHANGE ANY CODE HERE ------------
assert type(most_popular_gender(data_list)) is str, "TASK 6: Wrong type returned. It should return a string."
assert most_popular_gender(data_list) == "Male", "TASK 6: Returning wrong result!"
# -----------------------------------------------------

# If it's everything running as expected, check this graph!
gender_list = column_to_list(data_list, -2)
types = ["Male", "Female"]
quantity = count_gender(data_list)
y_pos = list(range(len(types)))
plt.bar(y_pos, quantity)
plt.ylabel('Quantity')
plt.xlabel('Gender')
plt.xticks(y_pos, types)
plt.title('Quantity by Gender')
plt.show(block=True)

input("Press Enter to continue...")
# TASK 7
# TODO: Plot a similar graph for user_types. Make sure the legend is correct.
print("\nTASK 7: Check the chart!")

def count_user_types(data_list):
    """ Counts the user_types of a given list
        Args:
            param1: List with the values 
        Returns:
          List with the user_types countings
    """
    customer = 0
    subscriber = 0
    dependent = 0
    
    for item in range(len(data_list)):
        if data_list[item] == "Customer":
            customer += 1
        elif data_list[item] == "Subscriber":
            subscriber += 1
        elif data_list[item] == "Dependent":
            dependent += 1 
    
    return [customer, subscriber, dependent]
  
user_type_list = column_to_list(data_list, -3)
types = ["Subscriber", "Customer", "Dependent"]
quantity = count_user_types(user_type_list)
y_pos = list(range(len(types)))
plt.bar(y_pos, quantity)
plt.ylabel('Quantity')
plt.xlabel('User Types')
plt.xticks(y_pos, types)
plt.title('Quantity by User Types')
plt.show(block=True)

input("Press Enter to continue...")

# TASK 8
# TODO: Answer the following question
male, female = count_gender(data_list)
print("\nTASK 8: Why the following condition is False?")
print("male + female == len(data_list):", male + female == len(data_list))
answer = "Because there are some missing values of the feature gender, so the sum don't considerate this values."
print("Answer:", answer)

# ------------ DO NOT CHANGE ANY CODE HERE ------------
assert answer != "Type your answer here.", "TASK 8: Write your own answer!"
# -----------------------------------------------------

input("Press Enter to continue...")
# Let's work with the trip_duration now. We cant get some values from it.
# TASK 9
# TODO: Find the Minimum, Maximum, Mean and Median trip duration.
# You should not use ready functions to do that, like max() or min().
trip_duration_list = column_to_list(data_list, 2)
min_trip = 0.
max_trip = 0.
mean_trip = 0.
median_trip = 0.

sum_trip = 0.

def min_max_sum_calculate(value_list):
    """ Identifies the max and min value a given list. Also calculates the sum of the values.
        Args:
            param1: List with the values 
        Returns:
          Float the min value
          Float the max value
          Float the sum of the values
    """   
    sum_value = 0.
    max_value = 0.
    min_value = float(value_list[0])
    len_list = len(value_list)
        
    for item in range(len_list):
        #finding the min value
        if float(value_list[item]) < min_value:
            min_value = float(value_list[item] )
        
        #finding the max value 
        if float(value_list[item]) > max_value:
            max_value = float(value_list[item])

        #calculating the amount
        sum_value += float(value_list[item])
    
    return min_value, max_value, sum_value

def median_calculate(value_list):
    """ Counts the user_types of a given list
        Args:
            param1: List with the values 
        Returns:
          List with the user_types countings
    """
    
    #ordering the values
    ordered_list = value_list
    ordered_list.sort(key=int)
    len_list = len(ordered_list)

    if len_list % 2:
        median = float(ordered_list[round(len_list / 2)])   
    else:
        median = float((ordered_list[round(len_list / 2)] + ordered_list[round(len_list / 2) - 1]) / 2.0)
    
    return median

#finding the min, max and the sum of the values
min_trip, max_trip, sum_trip = min_max_sum_calculate(trip_duration_list)

#finding the median   
median_trip = median_calculate(trip_duration_list)

#finding the mean    
mean_trip = sum_trip/len(trip_duration_list)

print("\nTASK 9: Printing the min, max, mean and median")
print("Min: ", min_trip, "Max: ", max_trip, "Mean: ", mean_trip, "Median: ", median_trip)

# ------------ DO NOT CHANGE ANY CODE HERE ------------
assert round(min_trip) == 60, "TASK 9: min_trip with wrong result!"
assert round(max_trip) == 86338, "TASK 9: max_trip with wrong result!"
assert round(mean_trip) == 940, "TASK 9: mean_trip with wrong result!"
assert round(median_trip) == 670, "TASK 9: median_trip with wrong result!"
# -----------------------------------------------------

input("Press Enter to continue...")

# TASK 10
# Gender is easy because usually only have a few options. How about start_stations? How many options does it have?
# TODO: Check types how many start_stations do we have using set()
user_types = set()

for item in column_to_list(data_list,3):
    if item not in user_types:
        user_types.add(item)

print("\nTASK 10: Printing start stations:")
print(len(user_types))
print(user_types)

# ------------ DO NOT CHANGE ANY CODE HERE ------------
assert len(user_types) == 582, "TASK 10: Wrong len of start stations."
# -----------------------------------------------------

input("Press Enter to continue...")

# TASK 11
# Go back and make sure you documented your functions. Explain the input, output and what it do. Example:
# def new_function(param1: int, param2: str) -> list:
"""
      Example function with annotations.
      Args:
          param1: The first parameter.
          param2: The second parameter.
      Returns:
          List of X values

"""

input("Press Enter to continue...")
# TASK 12 - Challenge! (Optional)
# TODO: Create a function to count user types without hardcoding the types
# so we can use this function with a different kind of data.
print("Will you face it?")
answer = "yes"

def count_items(column_list):
    """ Creates a new list with the unique values of a given list and the amount per value
      Args:
          param1: List with the values 
      Returns:
          List with the unique values
          The amount per value
    """

    item_types = []
    count_items = []
   
   #Identifies the unique values
    for item in range(len(column_list)):
        if column_list[item] not in item_types:
            item_types.append(column_list[item]) 
    
    #Identifies the amount per values
    for item_type in range(len(item_types)):
        count = 0
        for item_count in range(len(column_list)):
            if item_types[item_type] == column_list[item_count]:
                count += 1                            
        count_items.append(count) 

    return item_types, count_items

if answer == "yes":
    # ------------ DO NOT CHANGE ANY CODE HERE ------------
    column_list = column_to_list(data_list, -2)
    types, counts = count_items(column_list)
    print("\nTASK 11: Printing results for count_items()")
    print("Types:", types, "Counts:", counts)
    assert len(types) == 3, "TASK 11: There are 3 types of gender!"
    assert sum(counts) == 1551505, "TASK 11: Returning wrong result!"
    # -----------------------------------------------------


    