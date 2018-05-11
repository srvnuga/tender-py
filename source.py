import requests
from bs4 import BeautifulSoup
import re
from tender import Tender
from DateUtils import DateUtils
import random

CUSTOMERS = ['ООО Никель Никель',
             'ООО Формат',
             'ЗАО Дружба',
             'ООО ПитерФМ',
             'ООО ГазРаз',
             'ОАО МясоСуп',
             'ООО КартаКарыча',
             'ООО Стройград']
WINNERS_OF_AUCTION = ['OOO Электросчастье',
                      'ИП Иванисова С.К',
                      'ЗАО Ваш Застройщик',
                      'ООО Каркарыч',
                      'ИП Алексанян Г.Р']
RANDOM_START_DATE = "1/1/2012 1:30 PM"
RANDOM_END_DATE = "1/1/2019 4:50 AM"


class HtmlParser:
    TENDER_HOST = "http://rostender.info/region/saratovskaya-oblast/saratov"

    def __init__(self):
        pass

    def get_tenders(self):
        page = 1
        list_tend = []
        soup = HtmlParser.get_soup_by_url(HtmlParser.TENDER_HOST + "?pg=1&branch1=1&b=1&active_filter=YES")
        max_pages = int(re.sub("\D", "", soup.find_all("div", {"class": "b-paging"})[0].getText().split('[')[0]))
        while page <= max_pages:
            print('[INFO] process ' + str(page) + ' of ' + str(max_pages))
            soup = HtmlParser.get_soup_by_url(HtmlParser.TENDER_HOST + "?pg=" + str(
                page) + "&branch1=1&b=1&active_filter=YES")
            for tender_column in soup.findAll("div", {"class": "tender-columns"})[1:]:
                new_tender = Tender()

                number_element = tender_column.findAll("div", {"class": "column description-column"})[0].findAll("div",
                                                                                                                 {
                                                                                                                     "class": "description-content"})[
                    0].findAll("div", {"class": "description-header"})[0].findAll("div", {
                    "class": "description-header-item description-header-tender-number"})[0]
                number = int(re.sub("\D", "", number_element.getText()))  # избавиться от № привести к типу Инт
                new_tender.set_number(number)

                name_element = tender_column.findAll('a', {'target': '_blank'})[0]
                title = name_element.get('title')
                new_tender.set_name(title)
                tender_link = HtmlParser.TENDER_HOST + name_element.get('href')
                new_tender.set_url(tender_link)

                industry_element = \
                    tender_column.findAll("div", {"class": "column branch-column column-clickwork"})[0].findAll("div", {
                        "class": "branch-column-wrapper"})[0].findAll("ul")
                industry_title = ''
                for ul in industry_element:
                    for li in ul.findAll('li'):
                        industry_title = li.text
                new_tender.set_industry(industry_title)

                price_element = tender_column.findAll("div", {"class": "column price-column"})[0]
                price = re.sub("\D", "", price_element.getText())
                new_tender.set_start_max_price(price)

                place_element = tender_column.findAll("div", {"class": "column place-column column-clickwork-simple"})[
                    0]
                place_tender = re.sub("\r\n", "", place_element.getText())
                new_tender.set_place_tender(place_tender)

                list_tend.append(HtmlParser.add_additional_info_to_tender(new_tender))
            page += 1
        return list_tend

    @staticmethod
    def get_soup_by_url(url):
        source_code = requests.get(url)
        plain_text = source_code.text
        return BeautifulSoup(plain_text, "html.parser")

    @staticmethod
    def add_additional_info_to_tender(tender):
        start_auction_date = DateUtils.generate_random_date(RANDOM_START_DATE, RANDOM_END_DATE)
        tender.set_start_auction_date(start_auction_date)
        customer = random.choice(CUSTOMERS)
        tender.set_customer(customer)
        if DateUtils.is_target_before_now(start_auction_date):
            winner = random.choice(WINNERS_OF_AUCTION)
            if customer == CUSTOMERS[0]:
                winner = WINNERS_OF_AUCTION[0]
            tender.set_winner_of_auction(winner)
        doc_deadline_date = DateUtils.generate_random_date(RANDOM_START_DATE, start_auction_date)
        tender.set_doc_deadline_date(doc_deadline_date)
        return tender
