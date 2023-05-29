import os
import shutil
import time

import requests

site_url = 'https://q.midpass.ru/'

# captcha


captcha_url = site_url + '/ru/Account/CaptchaImage?' + int(time.time()).__str__()

print(captcha_url)

resp = requests.get(captcha_url, stream=True)
if resp.status_code == 200:
    with open('test.jpeg', 'wb') as f:
        resp.raw.decode_content = True
        shutil.copyfileobj(resp.raw, f)
        f.flush()
        os.fsync(f.fileno())
# sol
login_url = 'https://q.midpass.ru/ru/Account/DoPrivatePersonLogOn'

payload = {
    'NeedShowBlockWithServiceProviderAndCountry': True,
    'CountryId': "64798480-0aa4-8eec-f455-61d7179a5b17",
    "ServiceProviderId": "396eed8d-b062-d776-093a-0e330e74f1c0",
    'Email': "fastrapier1@yandex.ru",
    'g-recaptcha-response': "",
    'Captcha': input('Введите капчу'),
    'Password': "Wp2x9PMj"
}

headers = {
    'content-type': "application/x-www-form-urlencoded"
}

resp = requests.post(site_url, data=payload, headers=headers)

print(resp.status_code)
print(resp.headers)
print(resp.text)
