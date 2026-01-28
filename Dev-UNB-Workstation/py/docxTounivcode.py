from docx import Document
import pyperclip

def extract_text_from_docx(file_path):
    """Extracts text from a .docx file."""
    try:
        doc = Document(file_path)
        text = ""
        for paragraph in doc.paragraphs:
            text += paragraph.text + "\n"
        return text.strip()
    except Exception as e:
        return f"Error: {e}"

def convert_to_inpage_format(unicode_text):
    """Converts Unicode text to Inpage-compatible format."""
    try:
        # Placeholder conversion function
        # Replace this with actual Unicode to Inpage conversion logic
        inpage_text = unicode_text.encode('windows-1256', errors='replace').decode('windows-1256')
        return inpage_text
    except Exception as e:
        return f"Error in conversion: {e}"

def copy_to_clipboard(text):
    """Copies the given text to the clipboard."""
    try:
        pyperclip.copy(text)
        print("Text copied to clipboard successfully!")
    except Exception as e:
        print(f"Error copying to clipboard: {e}")

def main():
    file_path = input("Enter the path to your .docx file: ").strip()
    if file_path.startswith('"') and file_path.endswith('"'):
        file_path = file_path[1:-1]  # Remove quotes
    text = extract_text_from_docx(file_path)
    
    if "Error" not in text:
        print("Extracted text:")
        print(text)
        # Convert to Inpage-compatible format
        inpage_text = convert_to_inpage_format(text)
        print("Converted to Inpage-compatible format:")
        print(inpage_text)
        # Copy converted text to clipboard
        copy_to_clipboard(inpage_text)
        print("Now you can paste it in Inpage!")
    else:
        print(text)

if __name__ == "__main__":
    main()
