# Python Jira
Скрипт, для работы с jira, использующий одноименную библиотеку 

https://pypi.org/project/jira/

https://jira.readthedocs.io/examples.html?highlight=jira.search_issues#searching

```
~/_git/python_jira (master) » python issue_list.py                                                                           
https://jira.XXX.local/browse/XXX-221: livegamews-grpc: скорректировать hp
https://jira.XXX.local/browse/XXX-222: Прошу предоставить доступ по ssh на все хосты linux
https://jira.XXX.local/browse/XXX-223: RabbitMQ Shovel - допилить скрипт починки shovel, для массовой обработки
```

## Content
* [Python Jira](#python-jira)
  * [Content](#content)
  * [Setup and Run](#setup-and-run)
  * [Authenticate](#authenticate)
  * [Other:](#Other)

## Setup and Run
Clone repository:
```
git clone https://github.com/nudimannui4e/python_jira.git
cd python_jira
```
VirtualEnv install:
```
pip install virtualenv
virtualenv venv
source venv/bin/activate
```
Установка зависимостей:
```
pip3 install -r requirements.txt
```
## Authenticate
Создать **.env** файл, в котором будут храниться креды
```
JIRA_URL=https://xxx
JIRA_USER=login
JIRA_PASS=password
```
## Other
Тут идет запрос через **JiraQueryLanguage**, как пример, можно взять запрос с самой Jira
![alt text](https://i.imgur.com/aeSDAlc.png)

Креды запихнул в .env, для этого ставится дополнительно **python-dotenv**,
благодаря чему логин выглядит секьюрнее:
```
jira = JIRA(os.getenv('JIRA_URL'),
            basic_auth=(os.getenv('JIRA_USER'), os.getenv('JIRA_PASS')),
```
