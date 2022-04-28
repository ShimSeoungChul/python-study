import httpx


response = httpx.get('https://httpbin.org/get')
print(response.headers)

print(response.headers['Content-Type'])
print(response.headers['content-type'])
print(response.headers.get('Content-Type'))
print(response.headers.get('content-type'))
