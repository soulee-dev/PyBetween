import requests


class APIUrl:
    BASE = 'https://api-between.vcnc.co.kr/'
    AUTH = BASE + 'authentication/getAccessTokenV2'
    THREADS = 'threads'
    MESSAGES = 'messages/v4'
    SENDMESSAGE = 'messages'

    def get_url(self, endpoint, param):
        print()
        return f'{self.BASE + param}/{endpoint}'


def APIHandler(method, url, payload=None, headers=None):
    response = requests.request(method=method, url=url, data=payload, headers=headers)

    if response.ok:
        return response.json()
    raise AuthenticationError


class AuthenticationError(Exception):
    def __init__(self):
        super().__init__('Authentication failed')
