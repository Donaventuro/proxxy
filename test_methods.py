import requests


def test():
    print("Проверка метода get " + str(requests.get('https://httpbin.org/')))
    print("Проверка метода post " + str(requests.post('https://httpbin.org/post', data={'key': 'value'})))
    print("Проверка метода put " + str(requests.put('https://httpbin.org/put', data={'key': 'value'})))
    print("Проверка метода delete " + str(requests.delete('https://httpbin.org/delete')))
    print("Проверка метода head " + str(requests.head('https://httpbin.org/get')))
    print("Проверка метода patch " + str(requests.patch('https://httpbin.org/patch', data={'key': 'value'})))
    print("Проверка метода options " + str(requests.options('https://httpbin.org/get')))


if __name__ == '__main__':
    test()
