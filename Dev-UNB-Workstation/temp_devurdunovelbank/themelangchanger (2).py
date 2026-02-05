# from googletrans import Translator

# def translate_file(file_path, output_path, source_lang='id', target_lang='en'):
#     translator = Translator()

#     try:
#         with open(file_path, 'r', encoding='utf-8') as file:
#             content = file.read()

#         print("Translating content...")  # Debugging line
#         translated = translator.translate(content, src=source_lang, dest=target_lang)

#         if translated and translated.text:  # Ensure the response is not None
#             translated_content = translated.text

#             with open(output_path, 'w', encoding='utf-8') as output_file:
#                 output_file.write(translated_content)

#             print(f"Translation complete! Translated file saved as: {output_path}")
#         else:
#             print("Translation failed. No response from translator.")

#     except Exception as e:
#         print(f"Error occurred: {e}")

# # Specify input and output file paths
# input_file = r"C:\Users\Latitude\Downloads\ok.txt" # Replace with your actual input file path
# output_file = 'translated_theme.txt'  # Replace with desired output file path

# # Run the translation function
# translate_file(input_file, output_file)




# from deep_translator import GoogleTranslator

# def translate_file(file_path, output_path, source_lang='id', target_lang='en'):
#     try:
#         # Read the file content
#         with open(file_path, 'r', encoding='utf-8') as file:
#             content = file.read()

#         print("Translating content...")
#         # Translate the content
#         translated_content = GoogleTranslator(source=source_lang, target=target_lang).translate(content)

#         # Save the translated content
#         with open(output_path, 'w', encoding='utf-8') as output_file:
#             output_file.write(translated_content)

#         print(f"Translation complete! Translated file saved as: {output_path}")

#     except Exception as e:
#         print(f"Error occurred: {e}")

# # Specify paths
# input_file = r"C:\Users\Latitude\Downloads\ok.txt" # Replace with your input file path
# output_file = 'translated_theme.txt'  # Replace with your desired output file path

# # Run the function
# translate_file(input_file, output_file)







# from deep_translator import GoogleTranslator

# def translate_in_chunks(text, source_lang='id', target_lang='en', chunk_size=5000):
#     """
#     Translate a large text in chunks of specified size.
#     """
#     translator = GoogleTranslator(source=source_lang, target=target_lang)
#     translated_text = ""
#     for i in range(0, len(text), chunk_size):
#         chunk = text[i:i + chunk_size]
#         try:
#             translated_chunk = translator.translate(chunk)
#             translated_text += translated_chunk
#         except Exception as e:
#             print(f"Error translating chunk: {e}")
#     return translated_text

# def translate_file(file_path, output_path, source_lang='id', target_lang='en', chunk_size=5000):
#     """
#     Translate a file's content and save the result to an output file.
#     """
#     try:
#         # Read the input file
#         with open(file_path, 'r', encoding='utf-8') as file:
#             content = file.read()

#         print("Translating content in chunks...")
#         # Translate the content
#         translated_content = translate_in_chunks(content, source_lang, target_lang, chunk_size)

#         # Write the translated content to the output file
#         with open(output_path, 'w', encoding='utf-8') as output_file:
#             output_file.write(translated_content)

#         print(f"Translation complete! Translated file saved as: {output_path}")

#     except Exception as e:
#         print(f"Error occurred: {e}")

# # Specify file paths
# input_file = r"C:\Users\Latitude\Downloads\ok.txt" # Replace with your actual input file path
# output_file = 'translated_theme.txt'  # Replace with your desired output file path

# # Translate the file
# translate_file(input_file, output_file)






from deep_translator import GoogleTranslator
import os

def translate_in_chunks(text, source_lang='id', target_lang='en', chunk_size=5000):
    """
    Translate a large text in chunks and handle large files sequentially.
    """
    translator = GoogleTranslator(source=source_lang, target=target_lang)
    translated_chunks = []
    for i in range(0, len(text), chunk_size):
        chunk = text[i:i + chunk_size]
        try:
            translated_chunk = translator.translate(chunk)
            translated_chunks.append(translated_chunk)
            print(f"Translated chunk {i // chunk_size + 1}")
        except Exception as e:
            print(f"Error translating chunk {i // chunk_size + 1}: {e}")
    return translated_chunks

def translate_file(file_path, output_path, source_lang='id', target_lang='en', chunk_size=5000):
    """
    Translate the content of a file and save the result in chunks sequentially.
    """
    try:
        # Read the input file
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()

        print("Starting translation...")
        # Translate the content
        translated_chunks = translate_in_chunks(content, source_lang, target_lang, chunk_size)

        # Write the translated content to the output file
        with open(output_path, 'w', encoding='utf-8') as output_file:
            for chunk in translated_chunks:
                output_file.write(chunk)
                output_file.write("\n")  # Separate chunks with a newline

        print(f"Translation complete! Translated file saved as: {output_path}")

    except Exception as e:
        print(f"Error occurred: {e}")

# File paths
input_file = r"C:\Users\Latitude\Downloads\ok.txt" # Replace with your input file path
output_file = 'translated_theme_complete.txt'  # Replace with your output file path

# Run the translation
translate_file(input_file, output_file)
