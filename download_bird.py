import requests
from bs4 import BeautifulSoup
from urlparse import urljoin
import re


def generate_url_list(input_url):
    r = requests.get(input_url)
    soup = BeautifulSoup(r.content, 'html.parser')

    page_list = []
    for link in soup.select('a > img'):
        if "org" in link.parent.get("href"):
            page_list.append(link.parent.get("href"))
            continue
        page_list.append("http://www.ejcr.org/teaching-sets/" + link.parent.get("href"))

    print len(page_list)
    return page_list


def generate_pdf_url(page_url):
    for i in page_url:
        # print i
        metadata = []
        metadata.append(i)
        count = 1
        r = requests.get(i)
        soup = BeautifulSoup(r.content, 'html.parser')
        name = str(soup.title).split(" -- ")[1].replace("</title>", "")
        print name
        for link in soup.find_all(href=review_revision_pdf_href):
            download_pdf(urljoin(r.url, link.get("href")), name + ' - ' + str(count))
            count += 1
            metadata.append(link.get("href"))
        write_metadata(metadata)



def review_revision_pdf_href(href):
    return href and re.compile(r"^(?!../).*(review|revision).*\.pdf$", re.IGNORECASE).search(href)

    # return href and ((((re.compile("review", re.IGNORECASE).search(href) or \
    #        re.compile("revision", re.IGNORECASE).search(href)) and\
    #        re.compile("pdf", re.IGNORECASE).search(href)) and not re.compile("../", re.IGNORECASE).search(href)))


def download_pdf(pdf_url, name):
    r = requests.get(pdf_url, stream=True)
    with open(name + '.pdf', 'wb') as f:
        for chunk in r.iter_content(chunk_size=2000):
            f.write(chunk)


def write_metadata(datas, path="metadata.txt"):
    with open(path, 'a') as f:
        for i in datas:
            f.write("%s\n" % i)

if __name__ == "__main__":
    url_list = generate_url_list("http://www.ejcr.org/teaching-sets/teachingsets.html")
    generate_pdf_url(url_list)
