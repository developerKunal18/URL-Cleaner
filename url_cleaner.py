from urllib.parse import urlparse, parse_qs, urlencode, urlunparse

url = input("Enter URL: ")

parsed_url = urlparse(url)
query_params = parse_qs(parsed_url.query)

clean_params = {}

for key, value in query_params.items():
    if not key.startswith("utm_"):
        clean_params[key] = value

clean_query = urlencode(clean_params, doseq=True)

clean_url = urlunparse((
    parsed_url.scheme,
    parsed_url.netloc,
    parsed_url.path,
    parsed_url.params,
    clean_query,
    parsed_url.fragment
))

print("\nClean URL:")
print(clean_url)
