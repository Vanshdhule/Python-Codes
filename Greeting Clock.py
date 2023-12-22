import time

timestamp  = time.strftime('%H:%M:%S')
print(timestamp)

timestamp = int(time.strftime('%H'))

if (timestamp >=0 and timestamp < 12):
    print("Good morning")

elif (timestamp == 12):
    print("Good noon")

elif (timestamp >= 12 and timestamp < 17):
    print("Good afternoon")

else:
    print("Good night")

