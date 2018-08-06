from urllib.request import urlopen
from urllib.error import HTTPError, URLError
import io, json
# could have used built-in python HTMLParser 
# but I choose BeautifulSoup in order to provide a more succint code
from bs4 import BeautifulSoup
import os
import re


def parse_pages(filename):

    # create BeautifulSoup object
    soup = BeautifulSoup(open(filename), 'html.parser')

    # regex date pattern
    pattern = re.compile(r'[0-9]{2}/[0-9]{2}/[0-9]{4}')

    # get records table headings 
    headings = []
    headings_elms = soup.find_all(class_='nounderline')
    for heading_elm in headings_elms[:5]:
        headings.append(heading_elm.text.strip())
    # add headings for html links
    headings.extend(('Link','Img Src'))

    records = []
    # find all 'tr' tags
    elements = soup.find_all('tr')
    for el in elements:
        # get all children tags w/ date
        children = el.findChildren(text=pattern)

        if children != []:
            # create result elms list, remove '\n' chars
            result = [x.strip() for x in el.td.text.splitlines()]

            try:
                # target result has 5 elems in total, contains a date elem
                if re.match(pattern, result[1]) and len(result) == 5:
                    # if elem has link and image add to dict
                    if el.td.a is not None:
                        result.append(el.td.a['href'])
                        result.append(el.td.a.img['src'])
                    else:
                        # all final result dicts will have 7 elems
                        result.extend(('',''))
                    

                    # create record dict
                    record = {}
                    for i in range(len(headings)):
                        record[headings[i]] = result[i]

                    records.append(record)

            # result list does not have -at least- 2 items
            except IndexError:
                pass
                         
    return records
        

def output_to_json(data, filename):


    json_filename = filename.split('.')[0] + '.json'
        
    # write list to file
    with io.open(json_filename, 'w', encoding='utf8') as outfile:
        json.dump(data, outfile)


def main():
  
    filenames = [f for f in os.listdir(".") if f.startswith('q6') and f.endswith('html')]
    for filename in filenames:
        data = parse_pages(filename)
        output_to_json(data, filename)


if __name__ == '__main__':
    main()
