
from selenium import webdriver


# Main query string
query_string = "konsument"

# Main URL
URL = "https://rattsinfosok.domstol.se/lagrummet/SokAvgorande.jsp?tmpMenyVal=enkel&tmpFelFocus=false&tmpBesokStatistikSparad=true&tmpDisabledReferat=&oldSokDomstol=&oldSokSortering=&oldSokSenaste=&slctDomstol=ALLAMYND&txtAvgDatumFran=&txtAvgDatumTill=&txtRubrikText={}".format(query_string)

## Single docs

'''
for lopnummer in range(1,10):

    lopnummer = "3"
    single_doc_url = "https://rattsinfosok.domstol.se//lagrummet/Hamta_Detalj.jsp?traffLopNr={}".format(lopnummer)
'''

# Setup "browser"

driver = webdriver.Firefox()
driver.get(URL)
original_window = driver.current_window_handle
elem = driver.find_elements_by_tag_name("a")


#Fetch a list of articles
list_of_articles = []

try:
    for li in elem:
    
        # Links sorted
        if not li.text.isnumeric() and not li.text.isspace():
            list_of_articles.append(li)
            driver.
            '''
            for handle in driver.window_handles:
                if handle != original_window:
                    pop_up = handle
                    driver.switch_to_window(pop_up)
                    test_things = driver.find_elements_by_tag_name("h1")
                    print(test_things)
                    driver.close()
                    driver.switch_to.window(original_window)
                    '''


except:
    driver.quit()
    pass


# Just a list of links
for link_position in range(6,len(list_of_articles)):
    print(list_of_articles[link_position-2]) #Minus 2, last two links irrelevant


driver.quit() #Quits browser