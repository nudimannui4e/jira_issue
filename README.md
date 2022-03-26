# Python Jira
Скрипт, для работы с jira, использующий одноименную библиотеку 

https://pypi.org/project/jira/

## Content
* [Python Jira](#python-jira)
  * [Content](#content)
  * [Setup and Run](#setup-and-run)
  * [Authenticate](#authenticate)
    * [От себя:](#от-себя:)
    
## Setup and Run
Clone repository:
```
git clone https://github.com/nudimannui4e/python_jira.git
cd python_jira
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
### От себя:
Тут идет запрос через **JiraQueryLanguage**, как пример, можно взять запрос с самой Jira
![alt text](https://i.imgur.com/aeSDAlc.png)

Креды запихнул в .env, для этого ставится дополнительно **python-dotenv**,
благодаря чему логин выглядит секьюрнее:
```
jira = JIRA(os.getenv('JIRA_URL'),
            basic_auth=(os.getenv('JIRA_USER'), os.getenv('JIRA_PASS')),
```
