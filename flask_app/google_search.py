#!/usr/bin/python3

import requests
import urllib
from requests_html import HTMLSession
from bs4 import BeautifulSoup
import time

def get_source(url):
    """Return the source code for the provided URL. 

    Args: 
        url (string): URL of the page to scrape.

    Returns:
        response (object): HTTP response object from requests_html. 
    """

    try:
        session = HTMLSession()
        response = session.get(url)
        time.sleep(2)

        return response

    except requests.exceptions.RequestException as e:
        print(e)

def get_results(query):
    query = urllib.parse.quote_plus(query)
    response = get_source("https://www.google.com/search?q=" + query)
    return response

def scrape_google_wiki(response):

    links = list(response.html.absolute_links)
    wiki_domains = (
                      'https://en.wikipedia.org/wiki'
                      )
    links_wiki = []
    for url in links[:]:
        if url.startswith(wiki_domains):
            if "#" not in url: # select only main pages
                links_wiki.append(url)
    return links_wiki
    # return min(links_wiki, key=len)

def wiki_main_content(url):
    
    results = requests.get(url)
    html=results.text
    soup=BeautifulSoup(html,'html.parser')
        
    get_text = soup.find(class_ = 'mw-parser-output')
    get_text_list = []

    if get_text is not None:
        
        if len(get_text.select('p')) >= 4:
            for i in range(0,2):
                body_text = get_text.select('p')[i]
                get_text_list.append(body_text.getText().strip())

        if len(get_text.select('p')) < 4:
            length = len(get_text.select('p'))
            
            for i in range(0,length):
                body_text = get_text.select('p')[i]
                get_text_list.append(body_text.getText().strip())
    else:
        None
    return ' '.join(get_text_list)

def get_all_wiki(url_list):
    
    output = []
    output_id = []

    if len(url_list) != 0:
        for i in range(0, len(url_list)):
            id = ["wiki_"+str(i)]
            item = {
                "text": wiki_main_content(url_list[i])
            }            
            output_id.append(id)
            output.append(item)

    else:
        wiki_dict = {
            'wiki_0' : { "text" : "None" }
            }
    
    wiki_dict = {key: value for keys, value in zip(output_id, output) for key in keys}
    return wiki_dict

def parse_results(response):
    
    css_identifier_result = ".tF2Cxc"
    css_identifier_title = "h3"
    css_identifier_link = ".yuRUbf a"
    css_identifier_text = ".IsZvec"
    
    results = response.html.find(css_identifier_result)
    
    output = []
    output_id = []
    
    for i in range(0, 3):

        if results[0].find(css_identifier_text, first=True) is not None:

            id = ["output_"+str(i)]
            item = {
                "title": results[i].find(css_identifier_title, first=True).text,
            "link": results[i].find(css_identifier_link, first=True).attrs['href'],
            "text": results[i].find(css_identifier_text, first=True).text.encode("utf-8").decode("ascii", errors="ignore").replace('\n', ' ')
            }
            
        else: 
            id = ["None"]
            item = {
            "title": "None",
            "link": "None",
            "text": "None"
            }
        output_id.append(id)
        output.append(item)

    output_dict = {key: value for keys, value in zip(output_id, output) for key in keys}
    return output_dict

def get_query(query):
    
    if query is not None:
        item = {
                "query": str(query)
            }            
    else:
        item = {
            'query' : "None"
            }
    
    return item

def google_search(query):
    response = get_results(query)
    googl_search_results = parse_results(response)
    url_list = scrape_google_wiki(response)
    wiki_results = get_all_wiki(url_list)
    output = {**googl_search_results, **wiki_results}
    time.sleep(2)

    return output


# def google_search(query):
#     result = []
#     for i in query:
#         response = get_results(i)
#         queries = get_query(i)
#         googl_search_results = parse_results(response)
#         url_list = scrape_google_wiki(response)
#         wiki_results = get_all_wiki(url_list)
#         output = {**queries, **googl_search_results, **wiki_results}
#         result.append(output)
#         time.sleep(2)

#     return result
# if __name__ == "__main__":


#     query = "Steve Israel"
#     print(google_search(query))

    # url_list = scrape_google_wiki(query)
    # print(get_all_wiki(url_list))


#    print(scrape_google_wiki("Tim Johnson"))
#   print(wiki_main_content("https://en.wikipedia.org/wiki/Tim_Johnson_(South_Dakota_politician)"))


 #   print(google_search("Roy Cooper"))


