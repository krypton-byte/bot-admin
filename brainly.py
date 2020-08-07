import bs4, requests, urllib,re
from urllib.parse import quote
heder = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0',
}

def gsearch(query):
    src = requests.get("https://www.google.com/search?q="+quote(query)).text
    return re.findall('<a href="/url\?q\=(.*?)\&amp;',src)

class brainlyparse:
    def __init__(self,url):
        self.result = []
        source = requests.get(url, headers = heder).text
        parse = bs4.BeautifulSoup(source,"html.parser")
        self.soal = parse.find("span", class_="sg-text sg-text--large sg-text--bold sg-text--break-words brn-qpage-next-question-box-content__primary").text
        self.mapel,self.sekolah = [i.text for i in parse.findAll("span",itemprop="name",class_="sg-text sg-text--xsmall sg-text--gray-secondary sg-text--link")]
        self.p = [i.text.replace("\n","",1)[::-1].replace("\n","")[::-1] for i in parse.findAll("span",role="link",class_="sg-text sg-text--bold sg-text--small sg-text--gray sg-text--gray sg-text--link")]
        self.ans = [i.text.replace("\n","",1)[::-1].replace("\n","")[::-1] for i in parse.findAll("div",class_="sg-text js-answer-content brn-rich-content")]
        self.answ = [i.findAll("p") for i in parse.findAll("div",class_="sg-text js-answer-content brn-rich-content")]
        self.lk = [i.text for i in parse.findAll("span",class_="js-thanks-button-counter")]
        self.result.append([self.p[0],self.ans[0],self.lk[0]])
        self.result.append([self.p[1],self.ans[1],self.lk[1]]) if len(self.p) == 2 else None



user = []
reply = """
-  Detail Soal
   Pertanyaan : {}
   Mata Pelajaran : {}
   Tingkat Soal : {}
   Original Url : {}
=========================
-  Jawaban 1
{}
Penjawab : {}
Terima Kasih : {}
"""
j2 = """
- Jawaban 2
{}
Penjawab : {}
Terima Kasih : {}
"""