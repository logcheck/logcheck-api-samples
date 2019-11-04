from jsonapi_client import Session, Filter, ResourceTuple

import requests
from requests.auth import HTTPBasicAuth
import os

USER_NAME = os.getenv('USER_NAME')
PASSWORD = os.getenv('PASSWORD')
LOGCHECK_API_ENDPOINT = os.getenv('LOGCHECK_API_ENDPOINT')

with Session(LOGCHECK_API_ENDPOINT,
            request_kwargs=dict(auth=HTTPBasicAuth(USER_NAME, PASSWORD))) as s:

  logbook_id = '2aafb79e4f364feebe6e92393a5aee3d'
  published_since = '2019-05-02T00:00:00Z'

  filter = Filter(published_since='2019-05-02T00:00:00Z')

  documents = s.get(f'logbooks/{logbook_id}/records?published_since={published_since}')

  print(documents)

  r1 = documents.resource

  print(r1)
