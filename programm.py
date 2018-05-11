'''from pymongo import MongoClient



mymodel = Model()

mytender = Tender(1, "tender 1")
mytender2 = Tender(2, "tender 2")

mymodel.add_tender(mytender)
mymodel.add_tender(mytender2)

mymodel.print_tenders()'''

'''
myparser = HtmlParser()

mymongo = MongoClient()

mycontrol = Controller()

mycontrol.get_tenders(myparser)

mycontrol.insert_tenders(mymongo)
     # for link in soup.findAll('a', {'target': '_blank'}):
            #     title = link.get('title')
            #     if title is None:
            #         continue
            #     ten = Tender(str(title))
            #     ten.set_number(link.get('number'))
            #     list_tend.append(ten)
'''
from controller import Controller
from source import HtmlParser

cont = Controller()
cont.process()










