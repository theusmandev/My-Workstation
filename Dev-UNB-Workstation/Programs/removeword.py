import os

def remove_word_from_file(file_path, output_file, word_to_remove):
    try:
        # Normalize the file path to avoid literal issues
        file_path = file_path.strip('"').strip("'")

        # Check if the file exists
        if not os.path.exists(file_path):
            print(f"The file '{file_path}' does not exist.")
            return

        # Read the file content
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()

        # Replace the word with an empty string
        updated_content = content.replace(word_to_remove, "")

        # Write the updated content to a new file
        with open(output_file, "w", encoding="utf-8") as file:
            file.write(updated_content)

        print(f"The word '{word_to_remove}' has been removed, and the updated file is saved as '{output_file}'.")
    except Exception as e:
        print(f"An error occurred: {e}")


# Inputs
file_path = input("Enter the full path of the file: ").strip()
output_file = input("Enter the name for the new output file: ").strip()
word_to_remove = input("Enter the word you want to remove: ").strip()

# Call the function
remove_word_from_file(file_path, output_file, word_to_remove)
