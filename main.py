from urllib.request import urlopen as urlopen
from bs4 import BeautifulSoup as soup
import re

# 1st Professor
# Open and read the html
url_to_scrape = 'https://cs.txstate.edu/accounts/profiles/js236/'

# Open up connection, grabbing the page, closet he page
request_page = urlopen(url_to_scrape)
page_html = request_page.read()
request_page.close()

# html parsing
page_soup = soup(page_html, "html.parser")

# grab each product
containers = page_soup.findAll('div', class_="page-wrapper")

filename = "Jill Seaman.txt"
f = open(filename, "w")

headers = 'Name:'
headers1 = 'Title:'
headers2 = 'Research interest:'
headers3 = 'Education:'
headers4 = 'Office:'

for container in containers:
    name_containers = container.findAll('div', class_="row page-row")
    name = name_containers[0].div.figure.img["alt"]

    title = container.find('h2', class_="has-divider title").text

    education = container.p.text

    office_containers = container.findAll('div', class_="panel-body")
    office = office_containers[1].p.text

    f.write(headers + name + '\n')
    f.write(headers1 + title + '\n')
    f.write(headers2 + "NA" + '\n')
    f.write(headers3 + education + '\n')
    f.write(headers4 + office + '\n')
f.close()

# 2nd Professor
# Open and read the html
url_to_scrape2 = 'https://cs.txstate.edu/accounts/profiles/jg66/'

# Open up connection, grabbing the page, closet he page
request_page2 = urlopen(url_to_scrape2)
page_html2 = request_page2.read()
request_page2.close()

# html parsing
page_soup2 = soup(page_html2, "html.parser")

# grab each product
containers2 = page_soup2.findAll('div', class_="page-wrapper")

filename2 = "Bryon Gao.txt"
f2 = open(filename2, "w")

headers_2 = 'Name:'
headers1_2 = 'Title:'
headers2_2 = 'Research interest:'
headers3_2 = 'Education:'
headers4_2 = 'Office:'

for container2 in containers2:
    name_containers2 = container2.findAll('div', class_="row page-row")
    name2 = name_containers2[1].figure.img["alt"]

    title2 = container2.find('h2', class_="has-divider title").text

    research_interest = container2.p.text

    education_container2 = container2.findAll('div', class_="panel-body")
    education2 = education_container2[1].p.text

    office_containers2 = container2.findAll('div', class_="panel-body")
    office2 = office_containers2[2].p.text


    f2.write(headers_2 + name2 + '\n')
    f2.write(headers1_2 + title2 + '\n')
    f2.write(headers2_2 + research_interest + '\n')
    f2.write(headers3_2 + education2 + '\n')
    f2.write(headers4_2 + office2 + '\n')
f2.close()

# 3rd Professor
# Open and read the html
url_to_scrape3 = 'https://cs.txstate.edu/accounts/profiles/v_m137/'

# Open up connection, grabbing the page, closet he page
request_page3 = urlopen(url_to_scrape3)
page_html3 = request_page3.read()
request_page3.close()

# html parsing
page_soup3 = soup(page_html3, "html.parser")

# grab each product
containers3 = page_soup3.findAll('div', class_="page-wrapper")

filename3 = "Vangelis Metsis.txt"
f3 = open(filename3, "w")

headers_3 = 'Name:'
headers1_3 = 'Title:'
headers2_3 = 'Research interest:'
headers3_3 = 'Education:'
headers4_3 = 'Office:'

for container3 in containers3:
    name_containers3 = container3.findAll('div', class_="row page-row")
    name3 = name_containers3[1].figure.img["alt"]

    title3 = container3.find('h2', class_="has-divider title").text

    research_interest3 = container3.p.text

    education_container3 = container3.findAll('div', class_="panel-body")
    education3 = education_container3[1].p.text

    office_containers3 = container3.findAll('div', class_="panel-body")
    office3 = office_containers3[2].p.text


    f3.write(headers_3 + name3 + '\n')
    f3.write(headers1_3 + title3 + '\n')
    f3.write(headers2_3 + research_interest3 + '\n')
    f3.write(headers3_3 + education3 + '\n')
    f3.write(headers4_3 + office3 + '\n')
f3.close()

