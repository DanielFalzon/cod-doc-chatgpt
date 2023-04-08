from classes.crawler_class import Crawler
from classes.file_creator import create_file

domain = "https://vuejs.org/guide/"

crawler = Crawler(domain)

links = crawler.get_initial_links()
print(links)

for url in links:
   link_crawler = Crawler(domain + url)
   create_file(link_crawler.get_page_content(), url)

