from jsonapi_client import Session, Filter, ResourceTuple, Modifier, Inclusion

import requests
from requests.auth import HTTPBasicAuth
import os

USER_NAME = os.getenv('USER_NAME')
PASSWORD = os.getenv('PASSWORD')
LOGCHECK_API_ENDPOINT = os.getenv('LOGCHECK_API_ENDPOINT') or 'https://www.logcheckapp.com/api/v1'

def get_logbook_records(session, logbook_id, published_since):

    path = f'logbooks/{logbook_id}/records'

    # This would be better, but we can get by with Modifier until
    # we redefine how our endpoints handle filter parameters
    # filter = Filter(published_since=published_since)
    modifier = Modifier(f'published_since={published_since}')

    include = Inclusion('user', 'log')

    return session.get(path, modifier + include)

with Session(LOGCHECK_API_ENDPOINT,
            request_kwargs=dict(auth=HTTPBasicAuth(USER_NAME, PASSWORD))) as s:

  logbook_id = '2aafb79e4f364feebe6e92393a5aee3d'
  published_since = '2019-05-02T00:00:00Z'

  document = get_logbook_records(s, logbook_id, published_since)

  for record in document.resources:
    print(record)
    print(record.id)
    print(record.note)
    print(record.user)
    print(record.user.name)
    print(record.log.title)
