# def get_grade(marks):
#     if marks >= 90:
#         return 'A'
#     elif marks >= 80:
#         return 'B'
#     elif marks >= 70:
#         return 'C'
#     elif marks >= 60:
#         return 'D'
#     else:
#         return 'F'

# # Get input safely
# user_input = input("Enter your marks: ")

# # Check if input is not empty and is a number
# if user_input.strip().isdigit():
#     marks = int(user_input)
#     print("Your grade is:", get_grade(marks))
# else:
#     print("❌ Please enter a valid number.")







def get_grade(marks):
    if marks >= 90:
        return 'A'
    elif marks >= 80:
        return 'B'
    elif marks >= 70:
        return 'C'
    elif marks >= 60:
        return 'D'
    else:
        return 'F'

marks = int(input("Enter your marks: "))  # Convert to integer
print("Your grade is:", get_grade(marks))
