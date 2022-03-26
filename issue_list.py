# from .env
from dotenv import load_dotenv
import os

from jira import JIRA, Project
from jira.client import ResultList
from jira.resources import Issue
import urllib3

# disable ssl_error
urllib3.disable_warnings()

# creds from .env file
dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)


jira = JIRA(os.getenv('JIRA_URL'),
            basic_auth=(os.getenv('JIRA_USER'), os.getenv('JIRA_PASS')),
            options=dict(verify=False))


# search issues by JiraQueryLang
oh_shit = jira.search_issues(jql_str='project = DUTYADMIN AND status in (Open, "On Approval", Research) AND resolution = Unresolved AND updated >= -100d AND assignee in (currentUser(), duty-admin) ORDER BY priority DESC, updated DESC')


for issue in oh_shit:
    print('{}: {}'.format(os.getenv('JIRA_URL') + '/browse/' + issue.key, issue.fields.summary))
