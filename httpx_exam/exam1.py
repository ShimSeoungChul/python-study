import httpx
r = httpx.get('https://www.example.org/')
print('r:',r)
print('r.status_code:', r.status_code)
print('r.headers[\'content-type\']:', r.headers['content-type'])
print('r.text:', r.text)