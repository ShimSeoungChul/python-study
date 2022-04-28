import httpx


response = httpx.get('https://httpbin.org/cookies/set?chocolate=chip')
print(response.cookies['chocolate'])

cookies = {"ted": "robin"}
response = httpx.get('https://httpbin.org/cookies', cookies=cookies)
print(response.json())

cookies = httpx.Cookies()
cookies.set('cookie_on_domain', 'hello, there!', domain='httpbin.org')
cookies.set('cookie_off_domain', 'nope', domain='example.org')
response = httpx.get('http://httpbin.org/cookies', cookies=cookies)
print(response.json())