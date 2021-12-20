from bs4 import BeautifulSoup


def find_abstract(html):
    soup = BeautifulSoup(html, "html.parser")
    abstract = soup.find("h2") or soup.find("h3")
    if abstract:
        return abstract.text
    return None


def find_body(html):
    soup = BeautifulSoup(html, features="html.parser")
    body = soup.find_all("div") or soup.find_all("p")
    if body:
        return body
    return None


def find_summary(html):
    soup = BeautifulSoup(html, features="html.parser")
    body = soup.find_all("div") or soup.find_all("p")
    if body:
        return body[-1].get_text()
    return None