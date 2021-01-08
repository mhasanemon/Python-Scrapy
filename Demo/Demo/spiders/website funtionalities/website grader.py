import scrapy


class Seoscore(scrapy.Spider):

    name = 'Grader'
    def start_requests(self):
        urls = [
            'https://website.grader.com/results/cnn.com'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        website = response.url
        score = response.css('div.radial-inner-container').extract()

        try:
            with open('grades.txt', 'a') as f:
                for s in score:
                  f.write(website+" \t"+ s +"\n" )

        except:
            print("Cannot open the files")
