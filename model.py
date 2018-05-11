from tender import Tender


class Model:

    _tenders = None  # список тендеров исходный


    #def __init__(self):

    def add_tender(self, tender):
        if not isinstance(tender, Tender):
            raise TypeError("input tender is not %s type" % (Tender.__name__,))
        if self._tenders is None:
            self._tenders = []  # пустой список если список был None
        self._tenders.append(tender)

    def create_tender(self, param1, param2, param3):
        # validation of types
        tender = Tender(param1, param2,...)
        self.add_tender(tender)



''' def print_tenders(self):
        if self._tenders is None:
            print("Empty Tenders =(")
        else:
            for tender in self._tenders:
                tender.print_info()
    def create_tender
'''