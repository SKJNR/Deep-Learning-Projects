import spacy
from newspaper import Article
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests
from selenium.common.exceptions import StaleElementReferenceException
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

sections=['india-news', 'world-news', 'business-news', 'bollywood', 'latest-news', 'education', 'cricket', 
          'opinion', 'entertainment']

links=[]
for section in sections:
    for page in range(1,12):
        current_page_url = driver.get('https://www.hindustantimes.com/{}/page/?pageno={}'.format(section,page))
        values= driver.find_elements_by_xpath("//div[@class='media-heading headingfour']//a")
        for value in values:
            link=value.get_attribute('href')
            links.append(link)
            
print(len(links))
links=set(links)
print(len(links))


for link in links:           
            article=Article(link)
            article.download()
            article.parse()
            article.nlp()
            text=article.text
            final=''
            for i in text.split('\n')[4:]:
                if i.startswith('Click here') or i.startswith('Also read') or i.startswith('Follow'):
                    continue
                final+=i
            final=final+'\n'
            with open('train_news.txt', 'a') as f:
                f.writelines(final)
