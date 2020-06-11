# proxxy
Python proxxy-server

myserver.py - поднимает асинхронный веб-сервер на localhost:9000 проксирующий http - запросы к определенному серверу, передаваемому с именованным аргументом --host

Пример запуска:
python -m myserver --host http://httpbin.org

test_client.py - имитирует подключение нескольких клиентов 

test_method.py - проверяет работоспособность всех http-методов
