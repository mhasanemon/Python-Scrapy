import scrapy


class Seoscore(scrapy.Spider):

    name = 'Meta'
    def start_requests(self):
        urls = [
            'https://bbc.co.uk ',
            'https://cnn.com',
            'https://nytimes.com',
            'https://gglink.uk',
            'https://ebay.com'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        website = response.url
        metaTags = response.css("meta::attr(name)").extract()

        try:
            with open('meta.txt', 'a') as f:
                f.write('\n'+website+'\n')
                for s in metaTags:
                  f.write( s +'\t' )
                print('\n')

        except:
            print("Cannot open the files")
