import requests
from bs4 import BeautifulSoup

def get_company_info(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text,'html.parser')

    # Get page title
    title = soup.title.string if soup.title else "No Title Found"

    #grabing all text from <p> tag
    paragraphs = soup.find_all('p')
    text = ' '.join([para.get_text() for para in paragraphs])


    return title,text.strip()[:2000]



