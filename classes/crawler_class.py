from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import re

class Crawler(object):
        def __init__(self, base_url) -> None:
            
            chrome_options = Options()
            chrome_options.add_argument("--headless")
            chrome_options.add_argument("--disable-gpu")
            chrome_options.add_argument("--no-sandbox")

            # Create a ChromeDriver instance
            self.driver = webdriver.Chrome(options=chrome_options)
            self.base_url = base_url
            self.driver.get(base_url)
            self.driver.implicitly_wait(5)

        def get_initial_links(self):
            nav = self.driver.find_element("tag name", "aside").find_element("tag name", "nav")
            a_elements = nav.find_elements("tag name", "a")
            links = []
            for a_element in a_elements:
                link = a_element.get_attribute("href")
                links.append(link.replace(self.base_url, ''))
            return links

        def get_page_content(self):
            main = self.driver.find_element("tag name", "main")
            content = main.get_attribute("innerHTML")

            pattern = re.compile(r'<.*?>')
            clean_content = re.sub(pattern, '', content)

            return clean_content