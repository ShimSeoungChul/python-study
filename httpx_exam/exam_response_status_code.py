import httpx


response = httpx.get('https://httpbin.org/get')
print(response.status_code)

print(response.status_code == httpx.codes.OK)

not_found = httpx.get('https://httpbin.org/status/404')
print(not_found.status_code)
not_found.raise_for_status()