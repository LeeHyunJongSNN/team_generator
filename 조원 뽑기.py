import random
import csv
import math

teams = []
all_teams = []

total = int(input("학생 수 입력: "))
team = int(input("조원 수 입력: "))

students = [input("학생 이름 입력: ") for _ in range(total)]

for i in range(int(math.ceil(total / team))):
    if(len(students) < team):
        teams = [f"{i+1} 조"] + students
    else:
        teams = [f"{i+1} 조"] + random.sample(students, team)

    print(teams)
    students = [x for x in students if x not in teams]
    all_teams.append(teams)

f = open ("조원 목록.csv", 'w')
writer = csv.writer(f)
writer.writerows(all_teams)
f.close()
