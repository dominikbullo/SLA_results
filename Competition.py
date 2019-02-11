import requests
from bs4 import BeautifulSoup

from Racer import Racer
from local_settings import *


class Competition:
    def __init__(self, link):
        self.competition_link = link
        self.results_list = []
        self.date = None
        self.place = None

    def __str__(self):
        return "- " + str(self.place) + " " + str(self.date)

    class Result:
        def __init__(self, link):
            self.result_link = link

            self.date = None
            self.place = None
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
            self.place = header_list[0]
            self.date = header_list[6]
            self.category = header_list[5]
            self.gender = header_list[3]
            self.discipline = header_list[4]

            self.data = soup.find("table", {"class": "list"})

        def create_racer_list_with_results(self, racer_list):
            # TODO: Total number of racers and another statistics
            value = ""

            for row in self.data.findChildren('tr'):
                racer = []
                without_time = row.find('td', {"class": "bold", "colspan": "11"})
                if without_time:
                    value = without_time.string
                    continue

                for cell in row.findChildren('td'):
                    # TODO: DNS,_DNF,DSQ
                    racer.append(cell.string)

                if racer:
                    racer_class = Racer(full_name=racer[3],
                                        year_of_birth=racer[4],
                                        country=racer[5],
                                        category=self.category,
                                        gender=self.gender
                                        )
                    racer_class.position = str(racer[0]).replace(".", "")
                    racer_class.start_number = racer[1]
                    racer_class.code = racer[2]

                    # if race is without time
                    if len(racer) > 8:
                        racer_class.times = {"1. round": racer[7],
                                             "2. round": racer[8],
                                             "Together:": racer[9]}
                        # TODO: ignore string
                        racer_class.points_earned = racer[10]
                    else:
                        racer_class.without_time = True
                        racer_class.additional_info = value

                    if racer_class.full_name in [racer.full_name for racer in racer_list]:
                        racer_class.my_racer = True
                        print(
                            f'Printing result for race on {self.date} in {self.place} for category {self.category}')
                        print(racer_class)

                    self.racer_list.append(racer_class)
