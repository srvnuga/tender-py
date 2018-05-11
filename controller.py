from source import HtmlParser
from MongoConnect import MongoConnect
from notification import Notificator


class Controller:
    _htmlparser = None
    _mongo_conn = None
    _notificator = None

    def __init__(self):
        self._htmlparser = HtmlParser()
        self._mongo_conn = MongoConnect()
        self._notificator = Notificator()

    def process(self):
        result_list = self._htmlparser.get_tenders()
        self._mongo_conn.remove_all_coll()
        self._mongo_conn.insert_tenders(result_list)
        self._mongo_conn.insert_to_my_tenders(result_list[0].get_number())
        self._notificator.notify_about_tenders(self._mongo_conn.find_changed_tenders())
