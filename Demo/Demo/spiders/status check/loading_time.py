import urllib.request as urltoopen;
from time import time




urls = [
        'https://bbc.co.uk ',
        'https://cnn.com ',
        'https://nytimes.com ',
        'https://gglink.uk',
        'https://ebay.com'
        ]

try:

    with open('loading_time.text','w') as status:
        for u in urls:
            stream = urltoopen.urlopen(u)
            start_time = time()
            #this calculates how much time taken to read the stream of bytes of the website in seconds
            output = stream.read()
            end_time = time()
            stream.close()
            status.write(u+ "\t\t"+str(end_time-start_time) +'\n\n')

except Exception as e:
    print(e)
