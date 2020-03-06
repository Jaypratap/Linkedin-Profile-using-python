import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import pdfkit
import time
from pdfrw import PdfWriter
import logging

driver=webdriver.Chrome(executable_path='D:/Python_module/chromedriver_win32/chromedriver.exe')
driver.get('https://www.linkedin.com/login?trk=guest_homepage-basic_nav-header-signin')
time.sleep(5)
user=driver.find_element_by_css_selector('#username')
user.send_keys('Email')
password=driver.find_element_by_css_selector('#password')
password.send_keys('password')
login=driver.find_element_by_css_selector('.login__form_action_container ')
login.click()
time.sleep(1)
# search = driver.find_element_by_css_selector("#nav-search-artdeco-typeahead")
# search.send_keys("Python Developer")

driver.execute_script("document.getElementsByClassName('search-result__actions--primary button-secondary-medium m5')[1].click();")

# url = "https://www.linkedin.com/jobs/view/1235309881/"
# response = requests.get(url)

# div_class_name_ = "mt6 ml5 flex-grow-1"
# h1_class_name = "jobs-top-card__job-title t-24"

# soup =  BeautifulSoup(response.content, 'lxml')

# # print(soup)

# print(soup)
# name = soup.find("title")
# print(name)

# soup= BeautifulSoup(driver.page_source, 'lxml')
# f=open('htmlfile.html', 'w')
# head=open('htmlfile1.html', 'w')

# data=[]
# mobile="Not Available"
# mail="Not Available"




# elem=driver.find_element_by_css_selector(".contact-see-more-less.link-without-visited-state")
# elem.click()

# time.sleep(5)

# soup= BeautifulSoup(driver.page_source, 'lxml')



# for item in soup.select('.pv-top-card-section__body'):
#     name=item.text.strip()
#     for div in soup.find_all("div", {'class': 'pv-top-card-section__distance-badge'}):
#         div.decompose()
#     for div in soup.find_all("div", {'class': 'pv-top-card-section__actions pv-top-card-section__actions--at-bottom mt4'}):
#         div.decompose()
#     for span_tag in soup.find_all("span", {'class': 'svg-icon-wrap'}):
#         span_tag.replace_with('')
#     for h_tag in soup.find_all("h3", {'class': 'pv-top-card-section__connections pv-top-card-section__connections--with-separator Sans-17px-black-70% mb1 inline-block'}):
#         h_tag.replace_with('\n')
#     for h_tag in soup.find_all("h3", {'class': 'pv-entity__summary-title Sans-17px-black-85%-semibold'}):
#         h_tag.replace_with('\n')
#     for div in soup.find_all("div", {'class': 'pv-top-card-section__summary mt4 ph2 ember-view'}):
#         div.decompose()
#     for p_tag in soup.find_all("p", {'class': 'Sans-15px-black-55%'}):
#         p_tag.replace_with('')
# #    for span_tag in soup.find_all("span", {'class': 'truncate-multiline--last-line'}):
# #        span_tag.replace_with('')
#     for span_tag in soup.find_all("span", {'class': 'visually-hidden'}):
#         span_tag.replace_with('')
#     f.write("%s" % item)


# '''
# for div in soup.select('.pv-contact-info__ci-container'):
#     for link in soup.find_all('a', {'class': 'pv-contact-info__contact-item pv-contact-info__contact-link Sans-15px-black-55%'}): 
#         lk=link.get('href')
#         data.append(lk)
#         print(data)
# '''




# for div in soup.select('.pv-contact-info__ci-container'):
#     for link in soup.find_all('a', {'class': 'pv-contact-info__contact-link Sans-15px-black-55%'}):
#         old=link.get('href')
#         mobile=old.replace("tel:", " ")
    
# print(mobile)


# for div in soup.select('.pv-contact-info__ci-container'):
#     for link in soup.find_all('a', {'class': 'pv-contact-info__contact-item pv-contact-info__contact-link Sans-15px-black-55%'}):
#         old=link.get('href')
#         data.append(old)
#         mail=old.replace("mailto:", " ")
# linkedin=data[0]

# if mail==linkedin:
#     mail="Not Available"
# if mobile==linkedin:
#     mobile="Not Available"



    
# print(mail)
# f.write("<h4>Mobile No: %s" % mobile)
# f.write("<h4>Email: %s" %mail)
# f.write("<h4>Linkedin: %s" %linkedin)    
# f.write("<hr><h2>Experience:</h2><hr>")


# '''

# for div in soup.select('.pv-contact-info__ci-container'):
#     for link in soup.find_all('a', href=True): 
#         href=link.get('href')
#         print(href)

#     for span_tag in soup.find_all("span", {'class': 'visually-hidden'}):
#         span_tag.replace_with('')
#     print(name)
#     for span_tag in soup.find_all("span", {'class': 'a11y-text'}):
#         span_tag.replace_with('')
#     for span_tag in soup.find_all("span", {'class': 'pv-s-profile-actions__label'}):
#         span_tag.replace_with('')
    
#     '''
    

# with open('htmlfile1.html') as head:
#     pdfkit.from_file(head, 'headname.pdf')

# for item in soup.select('.pv-entity__summary-info'):
#     name=item.text.strip()        
#     f.write("%s" % item)


    
# options = {
#     'page-size': 'Letter',
#     'margin-top': '0.75in',
#     'margin-right': '0.75in',
#     'margin-bottom': '0.75in',
#     'margin-left': '0.75in',
#     'encoding': "UTF-8",
#     'custom-header' : [
#         ('Accept-Encoding', 'gzip')
#     ]

# }

# with open('htmlfile.html') as f:
#     pdfkit.from_file(f, 'out.pdf')

driver.quit()
