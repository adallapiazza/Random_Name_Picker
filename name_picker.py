'''
Random Name Picker
Picks draft order for fantasy football draft
19 Aug 2019
'''

# import libs
import random
import time

# fantasy football team owners
names = ['Alex','Tyler','Steve','Ryan','Shaun','Joe', 'Lee', 'Dave', 'Courtney', 'Ashley', 'Jen', 'Steph']

# used names
used_names = []

# Print out random draft order
for i in names:

    # list to store potential names
    remaining_names = []
    
    # Remove already printed names
    remaining_names = list(set(names) - set(used_names))
            
    # Select a random name from remaining names
    r = random.randint(0, (len(remaining_names))-1)
    random_name = remaining_names[r]
    
    # Move name into used_names so they arent duplicated in draft order
    used_names.append(random_name)

    print (random_name)
    
    # pause for a 2.5 seconds to add dramatic effect
    time.sleep(2.5)
    print
    
