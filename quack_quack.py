import datetime
import time
from utils import http_make_request

max_type_egg = 7 # số cấp tối thiếu mà trứng sẽ ấp. 

def api_collect_item(token, nest_id):
    url = "https://api.quackquack.games/nest/collect"

    payload = f'nest_id={nest_id}'
    headers = {
    'accept': '*/*',
    'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
    'authorization': f'Bearer {token}',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://dd42189ft3pck.cloudfront.net',
    'priority': 'u=1, i',
    'referer': 'https://dd42189ft3pck.cloudfront.net/',
    'sec-ch-ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
    }
    return http_make_request(payloads=payload, header=headers, url=url)
   
def api_get_list_item(token):
    url = "https://api.quackquack.games/nest/list-reload"

    payload = {}
    headers = {
        'accept': '*/*',
        'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
        'authorization': f'Bearer {token}',
        'if-none-match': 'W/"caf-xIhdrSheghbmsRPpMnv0w+LFtOg"',
        'origin': 'https://dd42189ft3pck.cloudfront.net',
        'priority': 'u=1, i',
        'referer': 'https://dd42189ft3pck.cloudfront.net/',
        'sec-ch-ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
    }
    
    response = http_make_request(payloads=payload, header=headers, url=url, method="GET")
    if response:
        nests = response.get("data", {}).get("nest")
        ducks = response.get("data", {}).get("duck")
        return nests, ducks
    return None , None

def api_collect_duck_high_level(token, nest_id):
    url = "https://api.quackquack.games/nest/collect-duck"

    payload = f'nest_id={nest_id}'
    headers = {
    'accept': '*/*',
    'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
    'authorization': f'Bearer {token}',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://dd42189ft3pck.cloudfront.net',
    'priority': 'u=1, i',
    'referer': 'https://dd42189ft3pck.cloudfront.net/',
    'sec-ch-ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
    }
    print("@#@#@#@#@#@#@")
    http_make_request(payloads=payload, header=headers, url=url)
    
def api_hatch_nest_high_level(token, nest_id):
    url = "https://api.quackquack.games/nest/hatch"
    payload = f'nest_id={nest_id}'
    headers = {
    'accept': '*/*',
    'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
    'authorization': f'Bearer {token}',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://dd42189ft3pck.cloudfront.net',
    'priority': 'u=1, i',
    'referer': 'https://dd42189ft3pck.cloudfront.net/',
    'sec-ch-ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
    }
    response_hatch = http_make_request(payloads=payload, header=headers, url=url)
    if not response_hatch:
        return
    
    sleep_time = response_hatch.get("data", {}).get("time_remain") or '1'
    try:
        time.sleep(int(sleep_time) + 2)
    except Exception as e:
        print(e)
    api_collect_duck_high_level(token, nest_id)

def collect_nest(name, token, nets_data, hatch, current_total_dusk, max_ducks, data : dict = {}):
    for nest in nets_data:
        nest_id = nest.get("id")
        if nest.get("status") == 1:
            print(f"{name} {datetime.datetime.now()} trứng chưa nở chưa thể thu hoạch {nest.get("id")}")
            continue

        if hatch and (nest.get("type_egg") or 1) >= max_type_egg:
            
            if current_total_dusk < max_ducks:
                current_total_dusk += 1
                api_hatch_nest_high_level(token=token, nest_id=nest_id)
                print(f"{name} {datetime.datetime.now()} ấp trứng thành công trứng cấp {nest.get("type_egg")}")
                continue
            elif current_total_dusk > max_ducks:
                print(f"[WARNING] : {name} {datetime.datetime.now()} trứng có level cao cần xoá dusk để thu thập {nest.get("type_egg")}")
                continue
                
        
        response_collect_item = api_collect_item(token ,nest_id)
        if response_collect_item and not response_collect_item.get("error_code"):
            print(f"{name} {datetime.datetime.now()} thu thập trứng thành công trứng cấp {nest.get("type_egg")}")
        else:
            print(f"{name} {datetime.datetime.now()} thu thập KHÔNG thành công trứng cấp {nest.get("type_egg")} {response_collect_item.get("error_code")}")
        time.sleep(1)

def check_dusk(dusk_data):
    max_min_total_race = [0, 0]
    min_total_rate = None
    max_total_rate = None
    for dusk in dusk_data:
        if not min_total_rate and not max_total_rate:
            max_total_rate = dusk.get("total_rare")
            min_total_rate = dusk.get("total_rare")
            max_min_total_race[1] = dusk.get("id")
            max_min_total_race[0] = dusk.get("id")
            continue
        
        if dusk.get("total_rare") > max_total_rate:
            max_total_rate = dusk.get("total_rare")
            max_min_total_race[0] = dusk.get("id")
            continue
        
        if dusk.get("total_rare") < min_total_rate:
            min_total_rate = dusk.get("total_rare")
            max_min_total_race[1] = dusk.get("id")
            continue
        
    return max_min_total_race, max_total_rate, min_total_rate
        
def check_gold_duck(name, token):
    url = "https://api.quackquack.games/golden-duck/reward"

    payload = {}
    headers = {
    'accept': '*/*',
    'accept-language': 'vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7',
    'authorization': f'Bearer {token}',
    'if-none-match': 'W/"36-E2ieVRpjms0b+2/eLyvulqTkTwI"',
    'origin': 'https://dd42189ft3pck.cloudfront.net',
    'priority': 'u=1, i',
    'referer': 'https://dd42189ft3pck.cloudfront.net/',
    'sec-ch-ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
    }
    response_check_dusk = http_make_request(payloads=payload, header=headers, url=url, method="GET")
    
    if response_check_dusk and response_check_dusk.get("error_code"):
        pass
    else:
        print(f"[{datetime.datetime.now()}] - [{name}] - response check gold duck {response_check_dusk}")



#### main process
def main_process(name, token, max_ducks):
    try:
        pass
        # await check_gold_duck(name, token)
    except Exception as e:
        print(e)
    hatch = False
    data = {}
    nests, ducks = api_get_list_item(token)
    if not nests:
        print(f"{datetime.datetime.now()} không có trứng nào để thu hoạch")
        time.sleep(3)
        return
    
    if not ducks:
        print(f"{datetime.datetime.now()} không có vịt nào để so sánh")
        time.sleep(1)
        return
    
    if len(ducks) < max_ducks:
        hatch = True
    elif len(ducks) == max_ducks:
        hatch = True
        id_max_min, max_total, min_total = check_dusk(ducks)
        data = {
            "id_max_min" : id_max_min,
            "max_total" : max_total,
            "min_total" : min_total
        }
    collect_nest(name, token, nests, hatch, len(ducks), max_ducks, data)
    time.sleep(10)
    print(f"------- end user {name} ------")
    
if __name__ == '__main__':
    
    list_token = {
        "account1" : {
            "token" : "",# token của tài khoảng
            "max_dusk" : 20# số còn vịt max của tài khoản 1
            },
        "account2" : {
            "token" : ""
            ,"max_dusk" : 10 
            },
        "feehily" : {
            "token" : "",
            "max_dusk" : 15
            }
    }
    while True:
        for item in list_token:
            name = item
            token = list_token.get(item).get("token")
            max_dusk = list_token.get(item).get("max_dusk")
            print("@#$@#")
            main_process(name, token, max_dusk)
