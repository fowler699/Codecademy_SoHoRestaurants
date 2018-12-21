# Codecademy_SoHoRestaurants
Final project of Codeacademy Data structures course

## Project instructions
1. Clone this repository by "git clone https://github.com/fowler699/Codecademy_SoHoRestaurants.git" command
2. Execute the application by "python3 script.py"
3. Read the instructions provided by the application

## Implementation details
### Part 1 - Search for a food type
For this part, Hash Map of Linked Lists has been selected. Number of Hash Map entries (number of keys) has been selected based on number of possible first characters of the food types.
Searching in Hash Map datastructure has runtime O(1). Because Hash Map of Linked Lists has been used and the Linken List runtime is O(N), the final worst runtime is O(N). 

A better option would be used a data structure with the worst complexity O(logN) like a Height Balanced Tree.

### Part 2 - Printing the list of restaurants
For this part, Hash Map of Linken Lists has been selected as well. Number of Hash Map entries (number of keys) has been selected based on number of possible food types.
Searching in Hash Map datastructure has the worst runtime O(1). Because Hash Map of Linked Lists has been used and the Linken List runtime is O(N), the final worst runtime is O(N). 
