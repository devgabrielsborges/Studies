from httpx import get
import fire


def get_dolar():
    response = get('https://economia.awesomeapi.com.br/all').json()
    return response


def get_euro():
    response = get('https://economia.awesomeapi.com.br/all/EUR-BRL').json()
    return response['EUR']['high']


def get_bitcoin():
    response = get('https://economia.awesomeapi.com.br/all/BTC-BRL').json()
    return response['BTC']['high']


fire.Fire()
