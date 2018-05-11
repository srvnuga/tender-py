from source import HtmlParser
from MongoConnect import MongoConnect


class Controller:
    _htmlparser = None
    _mongo_conn = None

    def __init__(self):
        self._htmlparser = HtmlParser()
        self._mongo_conn = MongoConnect()

    def process(self):
        result_list = self._htmlparser.get_tenders()
        self._mongo_conn.remove_all_coll()
        self._mongo_conn.insert_tenders(result_list)
        # self._mongo_conn.insert_My_tenders(33061357)
