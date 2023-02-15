from sys import stdin
import random

lunch_list = list(map(str, stdin.readline().rstrip().split()))

today_lunch = random.sample(lunch_list, 1)

print(today_lunch)