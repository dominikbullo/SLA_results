import requests
from bs4 import BeautifulSoup

from Racer import Racer


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
            self.result_link = link

            self.date = None
            self.category = None
            self.gender = None
            self.discipline = None
            self.data = None
            self.racer_list = []

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

            # Indexes from page -> same on every site
            self.date = header_list[6]
            self.category = header_list[5]
            self.gender = header_list[3]
            self.discipline = header_list[4]

            self.data = soup.find("table", {"class": "list"})

        def create_racer_list(self):
            # TODO: get data
            # TODO: Total number of racers and another statistics
            value = ""

            for row in self.data.findChildren('tr'):
                racer = []
                special_DNF_DNS = row.find('td', {"class": "bold", "colspan": "11"})
                if special_DNF_DNS:
                    # print("hura")
                    print(special_DNF_DNS.string)
                    value = special_DNF_DNS.string
                    continue

                for cell in row.findChildren('td'):
                    # TODO: DNS,DNF,DSQ
                    racer.append(cell.string)

                if racer:
                    if len(racer) > 8:
                        racer_class = Racer(position=racer[0],
                                            start_number=racer[1],
                                            code=racer[2],
                                            full_name=racer[3],
                                            year_of_birth=racer[4],
                                            country=racer[5],
                                            times={"1. round": racer[8],
                                                   "2. round": racer[9],
                                                   "Spolu:": racer[10]},
                                            points=racer[10],
                                            category=self.category,
                                            gender=self.gender
                                            )
                    else:
                        # TODO: DNF,DNS cases
                        racer_class = Racer(position=racer[0],
                                            start_number=racer[1],
                                            code=racer[2],
                                            full_name=racer[3],
                                            year_of_birth=racer[4],
                                            country=racer[5],
                                            times=None,
                                            points="",
                                            category=self.category,
                                            gender=self.gender
                                            )
                    print(racer_class.__dict__)
                    self.racer_list.append(racer_class)

                # print(racer)
                # racer = Racer()
