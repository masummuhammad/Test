
from itertools import cycle

# List of proxies
proxies = [
    'http://residential.dinamikproxy.com:11250:C05ax7:Rkutyc1_country-tr'
]
proxy_pool = cycle(proxies)

# Create a cycle iterator for the proxies
def retriveProxy():
    proxy=next(proxy_pool)
    return {"http":proxy,"https":proxy}

