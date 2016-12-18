#!/usr/bin/env python3

import google_search.crawler as crawler


if __name__ == '__main__':
    search_query = "united kingdom"
    result = crawler.search_web(search_query)
    # result = crawler.search_news(search_query)
    print(result)
    for item in result:
        print(item)

