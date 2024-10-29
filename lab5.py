import data
from data import Time,Point
# Write your functions for each part in the space below.

# Part 1
   # The function for Part 1 should be within the class in data.py.


# Part 2
   # The function for Part 2 should be within the class in data.py.


# Part 3
#adds two objects of the class time, making note to add the seconds as a time below 60s. Takes two time objects. Returns a time object.
#INPUT: Time 1
#INPUT: Time 2 (to add)
#OUTPUT: Combined Time

def time_add(time1: Time, time2:Time) -> Time:
    combined_hours = time1.hour + time2.hour
    combined_minutes = time1.minute + time2.minute +(time1.second + time2.second)//60
    if combined_minutes>60:
        combined_hours += combined_minutes%60
        combined_minutes = combined_minutes//60
    combined_seconds = (time1.second + time2.second)%60
    total_time = Time(combined_hours,combined_minutes,combined_seconds)
    return total_time
# Part 4
#takes a list of floats, tells if it is in descending order
#INPUT List[float]
#OUTPUT Bool that indicates descending order or not
def is_descending(list1:list[float]) -> bool:
    for idx in range (len(list1)-1):
        if list1[idx]<list1[idx+1] and list1[idx] != list1[idx+1] :
            return False
    return True
# Part 5
#takes a list of floats, a starting index as an integer, and an ending index as an integer.
#The function should find the largest value in the list between the two indexes and return its index.
# if the method receives an out-of-bounds index, it should still return the integer assuming that the
# list is infinitely long and containing elements with a value equaling 0

#INPUT list[int]
#INPUT int representing the starting index
#INPUT int representing the ending index
#OUTPUT integer representing the index of the highest value or None if idx 2 is greater than index 1
def largest_between(list1: list[int], idx1: int, idx2: int) -> int or None:
    if idx2<idx1:
        return None
    if idx1<0:
        idx1 = 0
    if idx2>len(list1):
        idx2 = len(list1)
    largest = list1[idx1]
    for x in range(idx1,idx2):
        if list1[x] > list1[largest]:
            largest = x
    return largest

# Part 6
#the function takes a list of points, it should return the index of the point with the largest distance from the origin
# input list
# output the integer representing the index of the point farthest from the origin
def furthest_from_origin(list1:list[Point]) -> int:
    largest_distance_index = 0
    for idx in range(len(list1)):
        distance = ((list1[idx].x)**2+(list1[idx].y)**2)**(1/2)
        if distance > largest_distance_index:
            largest_distance_index = idx
    return largest_distance_index
