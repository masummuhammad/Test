
from itertools import cycle

# List of proxies
proxies = [
    'http://proxy1.example.com:8080',
    'http://proxy2.example.com:8080',
    # Add more proxies as needed
]
proxy_pool = cycle(proxies)

# Create a cycle iterator for the proxies
def retriveProxy():
    proxy=next(proxy_pool)
    return {"http":proxy,"https":proxy}

