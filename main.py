#from concurrent.futures import ThreadPoolExecutor
import concurrent.futures
import time
import os

for x in range(0,20000):
   f = open("out/test"+str(x), 'w')
   f.write(str(x) + "\n" + str(20-x))
   f.close()
URLS = os.listdir('out/')
# Retrieve a single page and report the URL and contents
def load_url(x, timeout):
    f = open("out/"+str(x), 'w')
    time.sleep(10)
    return "Good morning!"
# We can use a with statement to ensure threads are cleaned up promptly
# for i in range (0,5):
with concurrent.futures.ThreadPoolExecutor(max_workers=2000) as executor:
    # Start the load operations and mark each future with its URL
    future_to_url = {executor.submit(load_url, url, 60): url for url in URLS}
    for future in concurrent.futures.as_completed(future_to_url):
        url = future_to_url[future]
        try:
            data = future.result()
        except Exception as exc:
            print('%r generated an exception: %s' % (url, exc))
        else:
            print('%r page is %d bytes' % (url, len(data)))