from pymongo import MongoClient
from tender import Tender


class MongoConnect:
    _conn = None  # conn = connection
    _db = None
    _coll = None  # coll = collection
    _my_coll = None

    def __init__(self):
        self._conn = MongoClient('localhost', 27017)
        print(self._conn)
        self._db = self._conn["TenderDB"]  # создали базу
        self.create_collections()

    def create_collections(self):
        self._coll = self._db["Tender"]  # создали коллекцию
        #self._coll.save({"ID": None, "name": None})
        self._my_coll = self._db["MyTender"]

    def insert_tenders(self, tenders):
        if not isinstance(tenders, list) and len(tenders) is not 0 and isinstance(tenders[0], Tender):
            raise TypeError("input tenders is not list or is not %s type" % (Tender.__name__,))
        for tender_item in tenders:
            number = tender_item.get_number()
            name = tender_item.get_name()
            industry = tender_item.get_industry()
            price = tender_item.get_start_max_price()
            start_date = tender_item.get_start_auction_date()
            finish_date = tender_item.get_doc_deadline_date()
            place_tender = tender_item.get_place_tender()
            customer = tender_item.get_customer()
            winner = tender_item.get_winner_of_auction()
            self._coll.save({"number": number,
                             "name": name,
                             "industry": industry,
                             "price": price,
                             "start_auction_date": start_date,
                             "doc_deadline_date": finish_date,
                             "place_of_tender": place_tender,
                             "customer": customer,
                             "winner": winner})
        for i in self._coll.find():  # вывести все docs in коллекции
            print(i)

    def remove_all_coll(self):
            self._coll.remove({})

    def insert_to_my_tenders(self, num_tender):
        if not isinstance(num_tender, int):
            raise TypeError("input num_tender is not int")
        tender = self._coll.find_one({"number": num_tender})
        if tender is None:
            raise ValueError("not found tender num = " + str(num_tender))
        my_tender = self._my_coll.find_one({"number": num_tender})
        if my_tender is None:
            self._my_coll.save(tender)
        else:
            print("WARN: my tender " + str(num_tender) + " already exists")

    def find_changed_tenders(self):
        chanded_tenders = []
        tenders = self._coll.find()
        my_tenders = self._my_coll.find()
        return chanded_tenders