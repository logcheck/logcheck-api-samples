from jsonapi_client import Session, Filter, ResourceTuple, Modifier, Inclusion

import requests
from requests.auth import HTTPBasicAuth
import os

TOKEN_ID = os.getenv('TOKEN_ID')
SECRET_KEY = os.getenv('SECRET_KEY')
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
            request_kwargs=dict(auth=HTTPBasicAuth(TOKEN_ID, SECRET_KEY))) as s:

  logbook_id = '2aafb79e4f364feebe6e92393a5aee3d'
  published_since = '2019-10-31T00:00:00Z'
  document = get_logbook_records(s, logbook_id, published_since)

  for record in document.resources:
    print(record)
    print(record.id)
    if 'value' in record._attributes:
      print(record.value)
    if 'deleted' in record._attributes:
      print('(DELETED)')
    print(record.user)
    print(record.user.name)
    print(record.log.title)
