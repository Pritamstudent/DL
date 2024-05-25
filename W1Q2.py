import datetime

user_p = int(input("Enter user preference temperature (in degrees Celsius): "))
o_temp = float(input("Enter outside temperature (in degrees Celsius): "))

current_time = datetime.datetime.now().time()
hour = current_time.hour

if o_temp >= 40:
    d_temp = 30
elif o_temp <= 10:
    d_temp = 22
elif 6 <= hour < 12:  
    d_temp = 28
elif 12 <= hour < 18:   
    d_temp = 30
else:
    d_temp = 25

d_temp = max(user_p, d_temp)

print(f"Temperature: {d_temp} degrees C")
