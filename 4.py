from urllib.request import urlopen
from urllib.error import HTTPError, URLError
import io, json
# could have used built-in python HTMLParser 
# but I choose BeautifulSoup in order to provide a more succint code
from bs4 import BeautifulSoup

def parse_page(html_source):

    # create BeautifulSoup object
    soup = BeautifulSoup(html_source, 'html.parser')

    # get Appellant name, Appellee name, CAV record number, and date received

    # CAV record number
    cav_record_num = soup.find('input', id='caseNumber')['value']
    # date received - assuming CAV date received and not RECORD date received
    cav_date_received = soup.find('input', id='noticeOfAplDt')['value']

    # get Appelant and Appelle Sections
    for section in soup.find_all(colspan='5'):
        # Appelant Parties Section
        if section.find('legend', class_='text').text == 'Appellant Parties':
            # Appellant name
            appellant_name = section.find(class_='gridText').text.strip()
        # Appellee Parties Section
        if section.find('legend', class_='text').text == 'Appellee Parties':
            # Appelle name
            appellee_name = section.find(class_='gridText').text.strip()
   
    data = {}
    data['Appellant name'] = appellant_name
    data['Appellee name'] = appellee_name
    data['CAV record number'] = cav_record_num
    data['CAV date received'] = cav_date_received

    return data

def output_to_json(data):

    # if JSON file already exists append result
    try:
        json_data = json.load(open('q4.json'))
        # convert data to list if not
        if type(json_data) is dict:
            json_data = [json_data]

        # append new item to json data list
        json_data.append(data)
    except IOError:
        json_data = data
        pass
        
    # write list to file
    with io.open('q4.json', 'w', encoding='utf8') as outfile:
        json.dump(json_data, outfile)


def main():

    # Scan through caseids 23800 to 23850 
    # ('downloads 50 cases sequentially' - deducing that case 23850 is not part of the sequence)
    for case_id in range(23800, 23850):
        # get each URL
        url = 'https://eapps.courts.state.va.us/cav-public/caseInquiry/showCasePublicInquiry?caseId=' + str(case_id)

        # Open page with urllib urlopen and fetch page source
        try:
            html_source = urlopen(url).read().decode('utf-8')
        except (HTTPError, URLError):
            print("not connected")

        # Call parsing function with html source string
        data = parse_page(html_source)

        # output results data to JSON file
        # append each result at a time, avoiding losing all data if scraper crashes
        output_to_json(data)


if __name__ == '__main__':
    main()
