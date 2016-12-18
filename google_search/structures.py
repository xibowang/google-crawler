
class SearchResults:

    def __init__(self, query):
        self._index = 0
        self._query = query
        self._results = {}

    def __len__(self):
        return self._results.__len__()

    def __iter__(self):
        return self

    def __next__(self):
        if self._index < self._results.__len__():
            res = self._results[self._index]
            self._index += 1
        else:
            self._index = 0
            raise StopIteration
        return res

    def append(self, item):
        self._results[self._results.__len__()] = item

    def get(self, index):
        return self._results[index]



class SearchItem:

    def __init__(self, title, href):
        self._title = title
        self._href = href

    def get_title(self):
        return self._title

    def get_url(self):
        return self._href

    def __str__(self):
        return "title: {} : href: {}".format(self._title, self._href)