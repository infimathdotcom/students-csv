import csv
import random

# Generate random student names and ages
student_names = ['John', 'Jane', 'Michael', 'Emily', 'William', 'Sophia', 'Jacob', 'Olivia', 'Matthew', 'Ava']
ages = [random.randint(18, 25) for _ in range(10)]

# Write data to CSV file
with open('students.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['StudentName', 'Age'])
    for i in range(10):
        writer.writerow([random.choice(student_names), ages[i]])

print("CSV file 'students.csv' has been generated.")
