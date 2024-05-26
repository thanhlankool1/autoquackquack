# -*- coding: utf-8 -*-
import httpx
import ujson
 
def http_make_request(
        payloads,
        header,
        url,
        method='POST',
        params=None,
        basic_auth={},
        file=None,
):  # json dump
    auth_request = None
    proxies = {
        "http://": None,
        "https://": None,
    }
    if basic_auth:
        auth_request = httpx.BasicAuth(username=basic_auth.get("user"), password=basic_auth.get("pass"))

    with httpx.Client(auth=auth_request, proxies=proxies, timeout=5) as client:
        try:
            request = client.build_request(method=method.upper(), url=url, data=payloads,
                                           files=file, headers=header, params=params)
            response = client.send(request)
            if response.status_code == 200 and response.text:
                return response.json()
            elif response.status_code == 400:
                print("response.json()", response.json())
                return response.json()
            else:
                print("error", response.text)
                return {}
        except Exception as e:
            print(f'[request call] {url} get exception {e}')
            return {}