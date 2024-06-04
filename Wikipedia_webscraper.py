import requests
from bs4 import BeautifulSoup

url = 'https://www.wikipedia.org/'

try:
    response = requests.get(url)
    response.raise_for_status()  

    if response.text.strip() == '':
        print("The response is empty.")
    
    else:
        print("Successfully fetched the webpage content.")

    soup = BeautifulSoup(response.text, 'html.parser')
    
    print("Content fetched from the webpage:")

    with open('Web_output.txt', 'w', encoding='utf-8') as file:
        file.write(soup.prettify()) 
        print("Output has been written to 'Web_output.txt' file.")

except requests.exceptions.RequestException as e:
    print(f"Error fetching the webpage: {e}")

except Exception as e:
    print(f"An error occurred: {e}")