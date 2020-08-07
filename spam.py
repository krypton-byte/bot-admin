import requests
def klikdokter(nomor):
    headers={
        "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Accept-Encoding":"gzip, deflate, br",
        "Accept-Language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
        "Cache-Control":"max-age=0",
        "Connection":"keep-alive",
        "Content-Length":"121",
        "Content-Type":"application/x-www-form-urlencoded",
        "Cookie":"js_enabled=true; _ga=GA1.3.1849872659.1594728174; __auc=181590701734d34e2d50a8defd8; user_token=DGmXuY2eMr3fqVVaPoQkPXvTDgRENSNtvm5nwkW1; _gid=GA1.3.1987657010.1595677399; js_enabled=true; __asc=7c76538017385c8df22f5a0eca7; _gid=GA1.2.1987657010.1595677399; _ga_KRW7RGZYS5=GS1.1.1595677398.4.1.1595677487.0; upgraded_laravel_session=eyJpdiI6Inp0VndTeXdrdGVVaXk3S0Zqa0hVWkE9PSIsInZhbHVlIjoiTDNDK2k3ZTJyVFBSYWNqK1FGRzl3UUt6Z0JiMEVkaE1NOG5ZVVRjUVlSd1RkM3ZsWjVFd3paZVNqTW1jZEFxd1IwNWN1REx6T1RRd0REejJtM2NQdnc9PSIsIm1hYyI6ImE4YTBjMzg5OTIzMDM0NmUwYzZhNWFiNDU0NGFmNjdmNjg0MTIyYTEyYTkzNDA3MDVhZGQ2M2IzZTA4MzI2YWYifQ%3D%3D; _ga=GA1.2.1849872659.1594728174",
        "DNT":"1",
        "Host":"www.klikdokter.com",
        "Origin":"https://www.klikdokter.com",
        "Referer":"https://www.klikdokter.com/users/create",
        "Sec-Fetch-Dest":"document",
        "Sec-Fetch-Mode":"navigate",
        "Sec-Fetch-Site":"same-origin",
        "Sec-Fetch-User":"?1",
        "Upgrade-Insecure-Requests":"1",
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"
    }
    data={
        "_token":"DGmXuY2eMr3fqVVaPoQkPXvTDgRENSNtvm5nwkW1",
        "back-to":"https://www.klikdokter.com/login?back-to=https%3A%2F%2Fwww.klikdokter.com%2F",
        "full_name":"krypton",
        "email":"apikrypton@gmail.com",
        "phone":"%s"%nomor
    }
    resp=requests.post('https://www.klikdokter.com/users/check',data=data, headers=headers).text
    if 'lewat SMS ke nomor ponsel yang Anda daftarkan' in resp:
        return True
    else:
        return False