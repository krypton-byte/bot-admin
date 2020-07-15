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
        "Cookie":"js_enabled=true; user_token=D8Na31vvquwtCT7Jy6Bju7KAIJ5iHuUB8KXJnfJo; _ga=GA1.3.1849872659.1594728174; _gid=GA1.3.1043323936.1594728174; js_enabled=true; __auc=181590701734d34e2d50a8defd8; _gid=GA1.2.1043323936.1594728174; __asc=5bf85d1c1734d8e752eb01c23b7; upgraded_laravel_session=eyJpdiI6ImVDZWhTK0Q2SW5mQjZzTlJpXC9HQ0hnPT0iLCJ2YWx1ZSI6InJWOHFaWjZrZHpHMnBwZ1RObVl1NTNzb2t5dDVTZ0JQTVgzTWdtRkNiZ2REOEFMdUJDTm1qNUxoaHBrcERvWFVLUkg5b0duRXN6MnFrUCtaVEN5TjRRPT0iLCJtYWMiOiIyNWJlOTVkM2ZjNGEzODEzNmQyMzgwNmM4M2NiNjdmNWI3Zjg4OWM3NDliMDJkNmM3NzA5MGJjNWIwMzNiMmIyIn0%3D; _ga_KRW7RGZYS5=GS1.1.1594734047.2.1.1594734122.0; _ga=GA1.2.1849872659.1594728174; _dc_gtm_UA-38846936-1=1; _gat_UA-38846936-1=1",
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
        "_token":"D8Na31vvquwtCT7Jy6Bju7KAIJ5iHuUB8KXJnfJo",
        "back-to":"",
        "full_name":"Krypton",
        "email":"apikrypton@gmail.com",
        "phone":"%s"%nomor
    }
    resp=requests.post('https://www.klikdokter.com/users/check',data=data, headers=headers).text
    if 'lewat SMS ke nomor ponsel yang Anda daftarkan' in resp:
        return True
    else:
        return False