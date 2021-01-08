import scrapy


class Seoscore(scrapy.Spider):

    name = 'Seo'
    def start_requests(self):
        urls = [
            'https://www.woorank.com/en/www/amazon.com',
            'https://www.woorank.com/en/www/cnn.com',
            'https://www.woorank.com/en/www/nytimes.com',
            'https://www.woorank.com/en/www/gglink.com',
            'https://www.woorank.com/en/www/ebay.com'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        website = response.url
        score = response.css('#dashboard-web > div.review-score.use-svg::attr(data-score)').extract()
        #creating files with website names first letters
        try:
            with open('scores.txt', 'a') as f:
                for s in score:
                  f.write(website+" \t"+ s +"\n" )

        except:
            print("Cannot open the files")
