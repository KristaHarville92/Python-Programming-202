""" One cause of speeding is the desire to shorten the time spent traveling. Create a program that calculates the amount of time saved if you are traveling with an average speed that is above the speed limit as compared to traveling with an average speed exactly at the speed-limit. Ask the user for the average speed, speed limit and distance traveled. EDIT THE TIME SAVED SHOULD BE REPORTED IN MINUTES"""

distance = float (input ("Enter the distance in miles "))
speedlimit = float (input("Enter miles/hours speed limit "))
speed = float (input("Enter your average speed in miles/hours "))

time = distance / speedlimit
speedtime = distance / speed

print (time, speedtime)

Minutes_in_hour = 60

speedtimein = speedtime*Minutes_in_hour
timein = time*Minutes_in_hour

if speed > speedlimit:
    savedtime = timein - speedtimein

else:
    print("safe driver but no time saved")


print(f'time taken at speed limit {timein: .2f} minutes')
print(f'time taken at your speed {speedtimein: .2f} minutes')
print(f'time saved in min {savedtime: .2f}')
