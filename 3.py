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
    with io.open('q3.json', 'w', encoding='utf8') as outfile:
        json.dump(data, outfile)


def main():

    url = 'https://eapps.courts.state.va.us/cav-public/caseInquiry/showCasePublicInquiry?caseId=23811'

    # Open page with urllib urlopen and fetch page source
    try:
        html_source = urlopen(url).read().decode('utf-8')
    except (HTTPError, URLError):
        print("not connected")

    # Call parsing function with html source string
    data = parse_page(html_source)

    # output results data to JSON file
    output_to_json(data)


if __name__ == '__main__':
    main()
