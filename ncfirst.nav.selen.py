from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests
import time
from   selenium.common.exceptions import TimeoutException
import sys, getopt

file_name = "dummy"

subListOfUrls = []

def fetch_url(url):

    response = requests.get(url)
    assert response.status_code == 200
    if response.status_code != 200:
        print "INVALID LINK"
    else:
        print url


def dumpResults(data):
    print "dumpResults"
    outF = open("myOutFile.txt", "w")
    for line in data:
         print >>outF, line
    outF.close()
   

def main(argv):
    global subListOfUrls
    driver = webdriver.Firefox()
    driver.get('http://nc-first.renci.org')
    #print "Links in NCFirst Page:"
    print "username = ", sys.argv[1]
    print "password = ", sys.argv[2]
    
    
    username = driver.find_element_by_name("email")
    password = driver.find_element_by_name("password")
    
    username.send_keys(sys.argv[1])
    password.send_keys(sys.argv[2])

    #driver.find_element_by_type("submit").click()
    login_attempt = driver.find_element_by_xpath("//*[@type='submit']")
    login_attempt.submit()
    
    #time.sleep(15)
    wait = WebDriverWait(driver, 10)
    wait.until(EC.title_is("NC First Main Page"))
    print "NC First Main Page is loaded"
    
    time.sleep(1)
    #lists = driver.find_elements_by_xpath("//div[contains(@class, 'menuTab')]")
    
    lists= driver.find_elements_by_class_name('menuTab')
    print ("Found " + str(len(lists)) + " menu tabs")
    for listitem in lists:
        click = listitem.get_attribute("onclick")
        print "    ",  (click)
        
    #elems = driver.find_elements_by_xpath("//a[@href]")
    #for elem in elems:
        #url = elem.get_attribute("href")
        #if url == "javascript:void(0)":
            #print "INVALID LINK URL: ", url
            #continue

        #subListOfUrls.append(url)
        #fetch_url(url)

    #dumpResults(subListOfUrls)

if __name__== "__main__":
    main(sys.argv[1:])
