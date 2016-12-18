
class SearchResults:

    def __init__(self, query):
        self._index = 0
        self._query = query

    def __len__(self):
        return self.__dict__.__len__()

    def append(self, item):
        self.__dict__[self._index] = item
        self._index += 1

    def get(self, index):
        return self.__dict__[index]


class SearchItem:

    def __init__(self, title, href):
        self._title = title
        self._href = href

    def get_title(self):
        return self._title

    def get_url(self):
        return self._href

