import scrapy

class platform_checker(scrapy.Spider):
    name = 'platform'
    def start_requests(self):
        urls = [
            'https://builtwith.com/bbc.co.uk',
            'https://builtwith.com/cnn.com',
            'https://builtwith.com/nytimes.com',
            'https://builtwith.com/gglink.uk',
            'https://builtwith.com/ebay.com'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        website = response.url
        techs = response.css('h2 a.text-dark::text').extract()
        #creating files with website names first letters
        try:
            with open('platform.txt', 'a') as f:
                f.write('\n\n'+website+'\n\n')
                for u in techs:
                    f.write(u+', ')

        except:
            print("Cannot open the files")
