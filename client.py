from jsonapi_client import Session, Filter, ResourceTuple, Modifier

import requests
from requests.auth import HTTPBasicAuth
import os

USER_NAME = os.getenv('USER_NAME')
PASSWORD = os.getenv('PASSWORD')
LOGCHECK_API_ENDPOINT = os.getenv('LOGCHECK_API_ENDPOINT')

def get_logbook_records(logbook_id, published_since):
  with Session(LOGCHECK_API_ENDPOINT,
              request_kwargs=dict(auth=HTTPBasicAuth(USER_NAME, PASSWORD))) as s:

    path = f'logbooks/{logbook_id}/records'

    # This would be better, but we can get by with Modifier until
    # we redefine how our endpoints handle filter parameters
    # filter = Filter(published_since=published_since)
    modifier = Modifier(f'published_since={published_since}')

    return s.get(path, modifier)

logbook_id = '2aafb79e4f364feebe6e92393a5aee3d'
published_since = '2019-05-02T00:00:00Z'

document = get_logbook_records(logbook_id, published_since)

for record in document.resources:
  print(record)
  print(record.id)
  print(record.note)
