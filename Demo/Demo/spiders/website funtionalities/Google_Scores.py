import scrapy
import time


##########THIS SOLUTION IS NOT WORKING

#
# I Later tried to Use Splash_Scrapy to download the dynamic content but wasn't sucessful



base_URL = 'https://developers.google.com/speed/pagespeed/insights/?url='
class Google_insight(scrapy.Spider):

    name = 'insightScore'

    def start_requests(self):
        urls = [
            'https://developers.google.com/speed/pagespeed/insights/?url=bbc.co.uk',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        time.sleep(10)
        website = response.url
        score = response.css('#page-speed-insights > div.pagespeed-results > div:nth-child(2) > div.result-container > div:nth-child(1) > div.psi-category-wrapper > div > div.lh-score__gauge > a > div.lh-gauge__percentage::text').extract()

        try:
            with open('Insight_scores.txt', 'a') as f:
                f.write('\n\n'+score+'\n\n')
                for u in score:
                    f.write(u+', ')

        except:
            print("Cannot open the files")
