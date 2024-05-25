# PS: Build a system for the smart home 
# Date: 1/24/2024
'''
Parameters for the eveluation:
time of the day:
----------------
rule: if 6:00 am to 5:00 pm : 1 (to make switch ON)
      else: 0 (to make switch OFF)

Presence of the human:
---------------------
rule: If present (= 1)then, switch ON (Only in case of night)
      daytime: no need to check human presence

      rows: time
      col: presence

      __0______1
     0 |0      0
     1 |0      1

     

# Extract the hour from the current time
time_hour = current_time.hour

# Update time_crisp based on the correct time comparison
time_crisp = 1 if 6 <= time_hour < 17 else 0
      
'''
import datetime
# Rule base for the PS
rule_base = [[0,0],[0,1]]

# Take the inputs
human_presence = int(input("If person is present enter 1: Else 0\n"))
current_time = datetime.datetime.now().time()


# Extract the hour hand to know the night or daytime
time_hour = current_time[0:2]

# Convert to integer for easy comparison
time_int = int(time_hour)

# To match the content in the knowledge base 
time_crisp = 0 if time_int >= 6 and time_int <= 17 else 1

# Extract the answer from the knowledge base
ans = rule_base[time_crisp][human_presence]

# Give the answer 
if ans:
    print("Light is switched ON")
else:
    print("Light is OFF")





# Design a rule base ac system in python:
'''
rules: User prefers 23 degrees C 
       user location: 
       if outside tempeartor is 40 or more then  lower the temp to 30
       if outside temp is 10 or lower increase to 22
       if it is day keep average temp of 30 and at night kep av of 25
'''

