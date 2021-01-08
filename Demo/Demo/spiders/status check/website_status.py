import urllib.request as urltoopen;

def check_status(param):
    status =  urltoopen.urlopen(param);
    return status.getcode()


#This checks if the website is up or down

urls = [
        'https://bbc.co.uk ',
        'https://cnn.com ',
        'https://nytimes.com ',
        'https://gglink.uk',
        'https://ebay.com'
        ]

try:

    with open('status.text','w') as status:
        for u in urls:
            if(check_status(u)==200):
                status.write(u+ "Website is up \n\n" )

            else :
                status.write(u+"Website is down \n\n")
except:
    print("Cannot finish the operation")
