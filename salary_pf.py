import sys
import datetime
sys.stdin = open("input.txt")
bonus = False
day, month, year = map(int, raw_input().split('/'))
if month == 4:
    bonus = True
current_date = datetime.date(year, month, day)
current_salary = int(raw_input())
no_of_years = int(raw_input())
salary = current_salary
for year in xrange(1, no_of_years+1):
    salary = salary
