#!/usr/bin/env python3

import google_search.crawler as crawler


if __name__ == '__main__':
    search_query = "united kingdom"
    result = crawler.search(search_query)
    print(result)

