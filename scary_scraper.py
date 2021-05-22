
from selenium import webdriver


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



try:
    # Takes the list of links and clicks on them
    #for link_position in range(6,len(list_of_articles)):
    for link_position in range(6, 7):
        list_of_articles[link_position].click()
        windows = driver.window_handles
        print(windows)
        print(windows[1])
        driver.switch_to.window(windows[0])
        divs = driver.find_elements_by_tag_name("div")

except:
    driver.quit()

# Quits browser
driver.quit()