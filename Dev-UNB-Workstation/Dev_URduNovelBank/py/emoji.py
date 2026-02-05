# import os

# def add_pointing_hand_right(file_path, output_file):
#     try:
#         # Normalize the file path
#         file_path = file_path.strip('"').strip("'")
        
#         # Check if the file exists
#         if not os.path.exists(file_path):
#             print(f"The file '{file_path}' does not exist.")
#             return

#         # Read the file content
#         with open(file_path, "r", encoding="utf-8") as file:
#             lines = file.readlines()

#         # Add pointing hand to the end of each line
#         updated_lines = [f"{line.strip()} 👈\n" for line in lines]

#         # Write the updated content to a new file
#         with open(output_file, "w", encoding="utf-8") as file:
#             file.writelines(updated_lines)

#         print(f"A pointing hand has been added to the end of each line, and the updated file is saved as '{output_file}'.")
#     except Exception as e:
#         print(f"An error occurred: {e}")


# # Inputs
# file_path = input("Enter the full path of the file: ").strip()
# output_file = input("Enter the name for the new output file: ").strip()

# # Call the function
# add_pointing_hand_right(file_path, output_file)


import os

def add_pointing_hand_right(file_path, output_file):
    try:
        # Normalize the file path
        file_path = file_path.strip('"').strip("'")
        
        # Check if the file exists
        if not os.path.exists(file_path):
            print(f"The file '{file_path}' does not exist.")
            return

        # Read the file content
        with open(file_path, "r", encoding="utf-8") as file:
            lines = file.readlines()

        # Add pointing hand to the end of each line
        updated_lines = [f"{line.strip()} 👈\n" for line in lines]

        # Write the updated content to a new file
        with open(output_file, "w", encoding="utf-8") as file:
            file.writelines(updated_lines)

        print(f"A pointing hand has been added to the end of each line, and the updated file is saved as '{output_file}'.")
    except Exception as e:
        print(f"An error occurred: {e}")


# Inputs
file_path = input("Enter the full path of the file: ").strip()
output_file = input("Enter the name for the new output file: ").strip()

# Call the function
add_pointing_hand_right(file_path, output_file)
