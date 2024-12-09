import scrapy
from scrapy.crawler import CrawlerProcess


class BonanzaSatrangiSpider(scrapy.Spider):
    name = "bonanzasatrangi_spider"
    # custom_settings = {
    #     "DOWNLOAD_DELAY": 0.1,
    #     "DOWNLOAD_TIMEOUT": 90,
    #     "RETRY_ENABLED": True,
    #     "HTTPPROXY_ENABLED": True,
    #     "ROBOTSTXT_OBEY": False,
    #     "RETRY_TIMES": 12,
    #     "ROTATING_PROXY_LIST": [
    #         f"http://{os.getenv('PROXY_USERNAME')}:{os.getenv('PROXY_PASSWORD')}@{os.getenv('PROXY_HOST')}:{os.getenv('PROXY_PORT')}"
    #     ],
    #     "DOWNLOADER_MIDDLEWARES": {
    #         "rotating_proxies.middlewares.RotatingProxyMiddleware": 610,
    #         "rotating_proxies.middlewares.BanDetectionMiddleware": 620,
    #     },
    # }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def start_requests(self):
        pass

    def closed(self, reason):
        pass


if __name__ == "__main__":
    process = CrawlerProcess()
    process.crawl(BonanzaSatrangiSpider)
    process.start()
