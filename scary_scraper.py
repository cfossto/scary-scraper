
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import keyboard
import time

# Main query string
query_string = "konsument"

# Main URL
URL = "https://rattsinfosok.domstol.se/lagrummet/SokAvgorande.jsp?tmpMenyVal=enkel&tmpFelFocus=false&tmpBesokStatistikSparad=true&tmpDisabledReferat=&oldSokDomstol=&oldSokSortering=&oldSokSenaste=&slctDomstol=ALLAMYND&txtAvgDatumFran=&txtAvgDatumTill=&txtRubrikText={}".format(query_string)


# Setup "browser"

driver = webdriver.Firefox()
driver.get(URL)
original_window = driver.current_window_handle
elem = driver.find_elements_by_tag_name("a")



# Fetch a list of articles
list_of_articles = []
try:
    for li in elem:
    
        # Fetching relevant documents
        if not li.text.isnumeric() and not li.text.isspace():
            list_of_articles.append(li)
except:
    driver.quit()


print(driver.current_window_handle)

try:
    # Takes the list of links and clicks on them
    #for link_position in range(6,len(list_of_articles)):
    for link_position in range(6, 7):
        list_of_articles[link_position].click()
        windows = driver.window_handles
        print(windows)
        print(windows[1])
        driver.switch_to.window(window_name=windows[1])
        print(driver.current_window_handle)
        time.sleep(1)
        driver.execute_script("window.print=function(){};")
        time.sleep(1)
        for i in range(1,6):
            keyboard.send("tab")
            print(i)
        keyboard.press_and_release("enter")
        print("Finished")

except:
    #driver.quit()
    pass

# Quits browser
#driver.quit()