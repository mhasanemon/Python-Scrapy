import scrapy
import re

###This is for crawling all the links of given websites
class Social_media_check(scrapy.Spider):

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

        socials = [
            'facebook',
            'twitter',
            'instagram',
            'youtube'
            'linkedIn'
        ]

        #Using Regex to find any of the social media keywords exist in all the links
        #if exists then it is added as social media link

        try:
            with open('social-media.txt', 'w') as f:
                f.write('\n'+website+'\n\n')
                for u in urls:
                    if any(re.findall('|'.join(socials),u)):
                        f.write(u+'\n')

        except:
            print("Cannot open the files")
