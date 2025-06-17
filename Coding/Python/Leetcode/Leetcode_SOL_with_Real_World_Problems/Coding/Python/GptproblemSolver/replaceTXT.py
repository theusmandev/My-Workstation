# File ka path den
file_path = r"D:\Python\GptproblemSolver\pythonfile.txt"

# File read karen aur content ko update karen
with open(file_path, 'r') as file:
    content = file.read()

# Replace 'S' with 'T'
updated_content = content.replace('S', 'T')

# Wapis file ko likh dein
with open(file_path, 'w') as file:
    file.write(updated_content)

print("File mein S ko T se replace kar diya gaya hai.")
