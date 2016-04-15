#!/usr/bin/env python
from xmlrpclib import ServerProxy

SERVER = 'http://localhost:1200'
DATABASE = 'tph_etl'
USERNAME = 'admin'
PASSWORD = 'admin'

server = ServerProxy('http://localhost:1200/xmlrpc/common')
user_id = server.login(DATABASE, USERNAME, PASSWORD)

server = ServerProxy('http://localhost:1200/xmlrpc/object')
user_ids = server.execute(
    DATABASE, user_id, PASSWORD,
    'res.users', 'search', []
)

users = server.execute(
    DATABASE, user_id, PASSWORD,
    'res.users', 'read', user_ids, []
)

for user in users:
    print(user['id'], user['name'])
