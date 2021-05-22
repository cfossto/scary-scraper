# Scary Scraper!


## Background
This tool was developed for a specific task of gathering information to a school project about consumer rights.
Since we couldn't find a public API for open and public data, we needed to scrape this from the website in question.
However, the data was available through a public search tool. We needed to automate the search tool
to deliver a great amount of documents to be analysed in a later stage.
This is what this tool is doing.

## The process
The program does not do anything malicous. It just automates what a normal user would have done.
The program simulates a webpage (in our case: Firefox (<3)) and puts in a search query into
a POST-request. This POST-request then delivers search results containing a description of the documents
and links to their respective detailed documents.

When the request is done, the program then sorts out the relevant web-objects, which in our case are links.
The program opens these links, prints the contents of the popups (saving them as PDFs),
closes the popup window and continues until there are no more documents left. Then it quits.

## Tools used:

* Python
* Selenium
* PyCharm


# DISCLAIMER

This program (also known as "Scary Scraper") can only be used for educational purposes. No other usage or development of the program is intended.

This program is not intended to be used to break any copyright and/or discretionary laws.

This program cannot be used for breaking any laws and/or disrupting operations of any entity subjected to the tool.

All usage of this program is at own risk and peril. I will not take responsibilty for any damage or disruptions made by anyone who has used or will use this program.

This program is open source under a GNU-license, which means it can be modified and redistributed freely.

By using this program, you acknowledge and accept the terms above. By using this program, you - and solely you - take responsibility for the effects of using this program.
