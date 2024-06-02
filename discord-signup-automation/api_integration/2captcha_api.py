import requests

class TwoCaptchaAPI:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = 'https://2captcha.com/in.php'
        self.result_url = 'https://2captcha.com/res.php'
    
    def solve_captcha(self, site_key, page_url):
        data = {
            'key': self.api_key,
            'method': 'userrecaptcha',
            'googlekey': site_key,
            'pageurl': page_url,
            'json': 1
        }
        response = requests.post(self.base_url, data=data).json()
        
        if response['status'] == 1:
            captcha_id = response['request']
            while True:
                result = requests.get(f'{self.result_url}?key={self.api_key}&action=get&id={captcha_id}&json=1').json()
                if result['status'] == 1:
                    return result['request']
                elif result['request'] == 'CAPCHA_NOT_READY':
                    continue
                else:
                    return None
        else:
            return None