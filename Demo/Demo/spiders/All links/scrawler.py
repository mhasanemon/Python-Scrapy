import scrapy
import urllib.request as urltoopen;

def check_status(param):
    status =  urltoopen.urlopen(param);
    return status.getcode()
###This is for crawling all the links of given websites
class linkSpider(scrapy.Spider):

    name = 'links'
    def start_requests(self):
        urls = [
        'https://bbc.co.uk',
        'https://cnn.com',
        'https://nytimes.com ',
        'https://gglink.uk',
        'https://ebay.com'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        website = response.url
        urls = response.css('a::attr(href)').extract()
        #creating files with website names first letters
        try:
            with open(website[8:15]+'urls.txt', 'w') as f:
                for u in urls:
                    if(u.find('http')!=-1):
                        #this checks is the link is dead or not
                        if(check_status(u)==200):
                            f.write(u + "\t\t Website is up\n\n")
                        else:
                            f.write(u+"\t\tWebsite is down\n\n")

        except:
            print("Cannot open the files")
