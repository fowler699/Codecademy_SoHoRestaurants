from data import *
from welcome import *
from hashmap import HashMap
from linkedlist import LinkedList
from node import Node

#Printing the Welcome Message
print_welcome()

#Write code to insert food types into a data structure here. The data is in data.py

#Prepare set of first characters
first_chars = []
for type in types:
  first_chars.append(type[0]) 
first_chars = set(first_chars)

#Prepare hashmap for types of food
hash_map_types = HashMap(len(first_chars))
for i in first_chars:
  linked_list = LinkedList()
  hash_map_types.assign(i, linked_list)
  
for type in types:
  list = hash_map_types.retrieve(type[0])
  list.insert_beginning(type)

#Prepare hashmap for list of restaurants
hash_map_rests = HashMap(len(types))
for i in types:
  linked_list = LinkedList()
  hash_map_rests.assign(i, linked_list)

for restaurant in restaurant_data:
  list = hash_map_rests.retrieve(restaurant[0])
  list.insert_beginning(restaurant)
  
#Write code for user interaction here
while True:
  user_input = str(input("\nWhat type of food would you like to eat?. \nType 'exit' to stop the searching.\n")).lower()
  #Search for user_input in food types data structure here
  if user_input == "exit":
    print("\nHave a nice day!")
    exit()
  if len(user_input) > 0:
    list = hash_map_types.retrieve(user_input[0])
    node = list.get_head_node()
    types_found = []
    while node.get_value() is not None:
      types_found.append(node.get_value())
      node = node.get_next_node()
    types_found_final = []
    for s in types_found:
      if user_input == s[0:len(user_input)]:
        types_found_final.append(s)
    if len(types_found_final) > 1:
      print(types_found_final)
    else:
      #After finding food type write code for retrieving restaurant data here
      user_input = str(input("\nThe only option with those beginning letters is " + types_found_final[0] + ". Do you want to look at " + types_found_final[0] + " restaruants? enter 'y' for yes and 'n' (default) for no\n"))
      if user_input == "y":
        print("The " + types_found_final[0] + " restaurants in SoHo are...")
        list = hash_map_rests.retrieve(types_found_final[0])
        node = list.get_head_node()
        while node.get_value() is not None:
          rest_info = node.get_value()
          print("\n---------------------------\n")
          print("Name: " + rest_info[1])
          print("Price: " + rest_info[2] + "/5")
          print("Rating: " + rest_info[3] + "/5")
          print("Address: " + rest_info[4])      
          node = node.get_next_node()
        user_input = str(input("\nDo you want to find other restaruants? enter 'y' (default) for yes and 'n' for no.\n"))
        if user_input == "n":
          print("\nHave a nice day!")
          exit()
  

