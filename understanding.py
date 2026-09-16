count = 1
while count <=5:
    print(count)
    count += 1

# 1. Standardize dictionary keys by making them all lowercase
student_name = {"alice": 85, "bob": 90, "charlie": 78}

while True:
    # 2. Get input and convert it to lowercase right away
    name_input = input("Enter student name (or 'exit' to quit): ").strip()
    name_lower = name_input.lower()
    
    # 3. Check for exit condition
    if name_lower == 'exit':
        print("Exiting program. Goodbye!")
        break
        
    # 4. Check if the lowercase name exists in the dictionary
    elif name_lower in student_name:
        # .capitalize() makes the name look nice in the final print statement
        print(f"{name_lower.capitalize()} scored {student_name[name_lower]} marks.")
        
    # 5. Handle missing records
    else:
        print(f"'{name_input}' is not in the records.")
