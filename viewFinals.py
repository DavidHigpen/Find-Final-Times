import time
import re

examTimes = {
    'MW 5:45pm - 7:00pm' : 'Thursday 7:30 - 9:30 a.m.',
    'MW 7:30pm - 8:45pm' : 'Thursday 7:30 - 9:30 a.m.',
    'MWF 8:00am - 8:50am' : 'Thursday 10:00 a.m. - 12:00 p.m.',
    'MWF 8:35am - 9:25am' : 'Thursday 10:00 a.m. - 12:00 p.m.',
    'TTh 9:35am - 10:50am' : 'Thursday 12:30 - 2:30 p.m.',
    'TTh 10:20am - 11:35 a.m' : 'Thursday 12:30 - 2:30 p.m.',
    'TTh 11:10am - 12:25pm' : 'Thursday 3:00 - 5:00 p.m.',
    'TTh 11:55am - 1:10pm' : 'Thursday 3:00 - 5:00 p.m.',

    'MWF 9:10am - 10:00am' : 'Friday 8:00 - 10:00 a.m.',
    'MWF 9:45am - 10:35am' : 'Friday 8:00 - 10:00 a.m.',
    'MWF 12:40pm - 1:30pm' : 'Friday 10:30 a.m. - 12:30 p.m.',
    'MWF 1:15pm - 2:05pm' : 'Friday 10:30 a.m. - 12:30 p.m.',
    'TTh 8:00am - 9:15am' : 'Friday 1:00 - 3:00 p.m.',
    'TTh 8:45am - 10:00am' : 'Friday 1:00 - 3:00 p.m.',
    'MW 4:10pm - 5:25pm' : 'Friday 3:30 - 5:30 p.m.',
    'MW 5:55pm - 7:20pm' : 'Friday 3:30 - 5:30 p.m.',
    'MW 7:20pm - 8:35pm' : 'Friday 6:00 - 8:00 p.m.',
    'MW 9:05pm - 10:20pm' : 'Friday 6:00 - 8:00 p.m.',
    
    'MWF 10:20am - 11:10am' : 'Monday 8:00 - 10:00 a.m.',
    'MWF 10:55am - 11:45am' : 'Monday 8:00 - 10:00 a.m.',
    'MWF 3:00pm - 3:50pm' : 'Monday 10:30 a.m. - 12:30 p.m.',
    'MW 4:20pm - 5:35pm' : 'Monday 10:30 a.m. - 12:30 p.m.',
    'TTh 3:55pm - 5:10pm' : 'Monday 1:00 - 3:00 p.m.',
    'TTh 4:40pm - 5:55pm' : 'Monday 1:00 - 3:00 p.m.',
    'MWF 1:50pm - 2:40pm' : 'Monday 3:30 - 5:30 p.m.',
    'MW 2:25pm - 3:40pm' : 'Monday 3:30 - 5:30 p.m.',
    'TTh 7:05pm - 8:20pm' : 'Monday 6:00 - 8:00 p.m.',
    'TTh 7:50pm - 9:05pm' : 'Monday 6:00 - 8:00 p.m.',

    'TTh 12:45pm - 2:00pm' : 'Tuesday 8:00 - 10:00 a.m.',
    'TTh 1:30pm - 2:45pm' : 'Tuesday 8:00 - 10:00 a.m.',
    'MWF 11:30am - 12:20pm' : 'Tuesday 10:30 a.m. - 12:30 p.m. - 12:20 p.m.',
    'MWF 12:05pm - 12:55pm' : 'Tuesday 10:30 a.m. - 12:30 p.m. - 12:20 p.m.',
    'TTh 2:20pm - 3:35pm' : 'Tuesday 1:00 - 3:00 p.m.',
    'TTh 3:05pm - 4:20pm' : 'Tuesday 1:00 - 3:00 p.m.',
    'TTh 5:30pm - 6:45pm' : 'Tuesday 3:30 - 5:30 p.m.',
    'TTh 6:15pm - 7:30pm' : 'Tuesday 3:30 - 5:30 p.m.'
}

schedule = []
classes = []
start = False
days = ['M', 'T', 'W', 'F']
classRegEx = r'[A-Z]{4}\t[0-9]{3}' #finds classes from a line input using regex

print('Enter your schedule:')
while time.perf_counter() - start < 0.2 or time.perf_counter() - start > 10: #reads multiple line input from keyboard
    line = input()
    classListing = re.findall(classRegEx, line)
    if classListing: #if it is a class listing, add it to the class listing and creates a new array for multiple times per class
        classes.append(classListing)
        schedule.append([])
    if line and line[0] in days and schedule: #if it is a class time, add it to the last list of class times
        schedule[-1].append(line[:line.find(' 08')])
    if not start: #starts a timer to end the loop after the clipboard input
        start = time.perf_counter()

print("\nFinals are:")
for classTime in examTimes: #iterates in this order so that it prints in final time order
    for i, realClassTime in enumerate(schedule):
        # print(classTime)
        # print(realClassTime[0])
        # print()
        if classTime in realClassTime[0]:
            print(classes[i][0][:4] + " " + classes[i][0][5:], ":", examTimes[classTime])
