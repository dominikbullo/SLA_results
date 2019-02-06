import requests
from bs4 import BeautifulSoup


class Competition:
    def __init__(self, link):
        self.competition_link = link
        self.results_list = []
        self.date = None
        self.place = None

    def set_date(self, date):
        self.date = date

    class Result:
        def __init__(self, link):
            # TODO: if date is None -> check if every date is equal
            self.result_link = link

            self.date = None
            self.category = None
            self.gender = None
            self.discipline = None
            self.data = None

            self.get_additional_info_about_race()

        def get_additional_info_about_race(self):
            soup = BeautifulSoup(requests.get(self.result_link).content, "lxml")
            # print(soup.prettify())
            header = soup.find("table", {"class": "card"})

            header_list = []
            header_rows = header.findChildren('tr')
            for row in header_rows:
                cells = row.findChildren('td')
                for cell in cells:
                    value = cell.string
                    header_list.append(value)

            # Indexex from page -> same on every site
            self.date = header_list[6]
            self.category = header_list[5]
            self.gender = header_list[3]
            self.discipline = header_list[4]

            self.data = soup.find("table", {"class": "list"})
