# Course Code: ICS3U
# Author: jn_xyp
# Version: 2017-11-02
# Problem Set 5 - Question 4

lockers = [False] * 1000
for student in range(1,1001):
    locker_number = 1
    while locker_number <= len(lockers):
        if locker_number % student == 0:
            lockers[locker_number - 1] = not lockers[locker_number - 1]
        locker_number = locker_number + 1

opened_lockers = 'Opened Lockers:'
locker_number = 1
while locker_number <= len(lockers):
    if lockers[locker_number - 1]:
        opened_lockers = opened_lockers + str(locker_number) + ' '
    locker_number = locker_number + 1

print(opened_lockers)