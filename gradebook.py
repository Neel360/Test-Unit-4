grades = {
    "Sam": 83,
    "Bob": 96,
    "Alice": 91,
    "Charlie": 76,
    "Alex": 80,
    "Joe": 79
}

total = 0

for name, grade in grades.items():
    total += grade

average = total / len(grades)

print(f"\n\nThe class average was {average}.")

highest = max(grades.values())
lowest = min(grades.values())

for name, grade in grades.items():
    if grade == highest:
        print(f"\n{name} got the highest. They got {grade}.")

    if grade == lowest:
        print(f"\n{name} got the lowest. They got {grade}.")

student = input("\nEnter the name of the student who you would like to check the grades of: ")
grade = grades.get(student)

if grade is not None:
    print(f"{student} got {grade}!")
else:
    print("Sorry! We could not find that name in our database!")
          
