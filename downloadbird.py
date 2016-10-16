import requests
from bs4 import BeautifulSoup
from urlparse import urljoin

r = requests.get('http://www.ejcr.org/teaching-sets/teachingsets.html')
soup = BeautifulSoup(r.content, 'html.parser')

page_list = []
metadata = []
for link in soup.find_all('a'):
    if link.select("img"):
        if "org" in link.get("href"):
            page_list.append(link.get("href"))
            continue
        page_list.append("http://www.ejcr.org/teaching-sets/" + link.get("href"))

print len(page_list)
# print page_list
for i in page_list:
    print i
    metadata.append(i)
    count = 1
    r = requests.get(i)
    soup = BeautifulSoup(r.content, 'html.parser')
    name = str(soup.title).split(" -- ")[1].replace("</title>", "")
    for link in soup.find_all("a"):
        link_string = str(link.get("href")).upper()
        if ("REVIEW" in link_string or "REVISION" in link_string) and "PDF" in link_string and "../" not in link_string:
            metadata.append(link_string)
            o = urljoin (r.url, link.get("href"))
            r = requests.get(o, stream=True)

            output_name = name + ' - '+ str(count)
            # print output_name
            count += 1
            with open(output_name + '.pdf', 'wb') as f:
                for chunk in r.iter_content(chunk_size=2000):
                    f.write(chunk)
with open('metadata.txt', 'w') as f:
    for i in metadata:
        f.write("%s\n" % i)
# url = 'http://www.hrecos.org//images/Data/forweb/HRTVBSH.Metadata.pdf'
# r = requests.get(url, stream=True)
#
# with open('/tmp/metadata.pdf', 'wb') as fd:
# for chunk in r.iter_content(chunk_size):
#     fd.write(chunk)