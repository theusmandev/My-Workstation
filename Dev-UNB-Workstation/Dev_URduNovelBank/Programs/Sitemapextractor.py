import requests
import xml.etree.ElementTree as ET
import pandas as pd

# Function to extract the sitemap and save it as an Excel file
def extract_sitemap_to_excel(url):
    try:
        # Send a request to fetch the sitemap XML
        response = requests.get(url)
         
         
        # Check if the request was successful
        if response.status_code == 200:
            # Parse the XML content
            root = ET.fromstring(response.content)
            
            # List to store sitemap URLs
            sitemap_urls = []

            # Loop through each <url> entry in the sitemap
            for url_entry in root.findall("{http://www.sitemaps.org/schemas/sitemap/0.9}url"):
                loc = url_entry.find("{http://www.sitemaps.org/schemas/sitemap/0.9}loc").text
                sitemap_urls.append(loc)
            
            # Convert the sitemap URLs to a pandas DataFrame
            df = pd.DataFrame(sitemap_urls, columns=["URL"])
            
            # Save the DataFrame to an Excel file
            output_file = "sitemap_urls.xlsx"
            df.to_excel(output_file, index=False)
            print(f"Sitemap has been extracted and saved to {output_file}")
        else:
            print(f"Failed to retrieve sitemap. Status code: {response.status_code}")
    
    except Exception as e:
        print(f"An error occurred: {e}")

# Input the URL of the sitemap
sitemap_url = input("Enter the sitemap URL: ")

# Extract the sitemap and save it to an Excel file
extract_sitemap_to_excel(sitemap_url)
