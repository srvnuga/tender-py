class Tender:
    _id = None  #_приватные
    _number = None
    _name = None
    _industry = None
    _start_auction_date = None
    _start_max_price = None
    _place_tender = None
    _doc_deadline_date = None    #for sending document
    _customer = None
    _winner_of_auction = None
    _url = None

    def __init__(self): #конструктор класса с двумя параметрами
        pass

    def set_id(self, new_id):
        if not isinstance(new_id, int):
            raise TypeError("input id is not int")
        self._id = new_id

    def set_number(self, new_number):
        if not isinstance(new_number, int):
            raise TypeError("input new_number is not int")
        self._number = new_number

    def set_name(self, new_name):
        if not isinstance(new_name, str):
            raise TypeError("input name is not str")
        self._name = new_name

    def set_industry (self, new_industry):
        if not isinstance(new_industry, str):
            raise TypeError("input name is not str")
        self._industry = new_industry

    def set_start_auction_date(self, new_start_date):
        if not isinstance(new_start_date, str):
            raise TypeError("input new_start_date is not str")
        self._start_auction_date = new_start_date

    def set_start_max_price(self, new_start_max_price):
        if not isinstance(new_start_max_price, str):
            raise TypeError("input new_start_max_price is not str")
        self._start_max_price = new_start_max_price

    def set_place_tender(self, new_place_tender):
        if not isinstance(new_place_tender, str):
            raise TypeError("input new_place_tender is not str")
        self._place_tender = new_place_tender

    def set_doc_deadline_date(self, new_finish_date):
        if not isinstance(new_finish_date, str):
            raise TypeError("input new_finish_date is not str")
        self._doc_deadline_date = new_finish_date

    def set_customer(self, new_customer):
        if not isinstance(new_customer, str):
            raise TypeError("input new_download_doc is not str")
        self._customer = new_customer

    def set_winner_of_auction(self, new_download_doc):
        if not isinstance(new_download_doc, str):
            raise TypeError("input new_download_doc is not str")
        self._winner_of_auction = new_download_doc

    def set_url(self, url):
        if not isinstance(url, str):
            raise TypeError("input url is not str")
        self._url = url

    def get_id(self):  # геттер получить id
        return self._id

    def get_number(self):  # геттер получить number
        return self._number

    def get_name(self):  # геттер получить name
        return self._name

    def get_industry(self):  # геттер получить name
        return self._industry

    def get_start_auction_date(self):
        return self._start_auction_date

    def get_start_max_price(self):
        return self._start_max_price

    def get_place_tender(self):
        return self._place_tender

    def get_doc_deadline_date(self):
        return self._doc_deadline_date

    def get_customer(self):
        return self._customer

    def get_winner_of_auction(self):
        return self._winner_of_auction

    def get_url(self):
        return self._url

    def print_info(self):  # вывести в консоль инфо
        print("tender: id = %s" % str(self._id) + ", name = %s" % self._name)
