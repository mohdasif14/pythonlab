
# Create a dictionary with keys: 'name', 'age', and 'major'

student_info = {
    'name': 'Asif',
    'age': 20,
    'major': 'Electrical Engineering'
}

print("Name:", student_info['name'])
print("Age:", student_info['age'])

student_info['email'] = 'Asif@example.com'
print("Email added:", student_info['email'])

student_info['age'] = 21
print("Updated Age:", student_info['age'])

del student_info['major']
print("Updated Student Information:", student_info)