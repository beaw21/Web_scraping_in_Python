import requests
import requests_cache

# Enable caching for all requests
requests_cache.install_cache('my_cache', expire_after=3600)  # cache for 1 hour

# Define the list of URLs to request
urls = ['https://example.com/resource1', 'https://example.com/resource2', 'https://example.com/resource3']

# Loop through the URLs and make GET requests
for url in urls:
    # Check if the response is already cached
    if requests_cache.get_cache().has_url(url):
        response = requests_cache.get_cache().get_response(url)
        print('Response retrieved from cache')
    else:
        # Send a new GET request and cache the response
        response = requests.get(url)
        requests_cache.get_cache().add_response(url, response)
        print('New response cached')

    print(response.content)
