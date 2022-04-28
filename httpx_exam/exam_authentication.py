import httpx


httpx.get("https://example.com", auth=("my_user", "password123"))

auth = httpx.DigestAuth("my_user", "password123")
httpx.get("https://example.com", auth=auth)