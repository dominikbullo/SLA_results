import requests

from datetime import datetime
from bs4 import BeautifulSoup
from Competition import Competition
from Racer import Racer


class ResultsFinder:
    def __init__(self, competitions_links_list, racer_list):
        self.competitions_links_list = competitions_links_list
        self.racer_list = racer_list
        self.competition_list = []

    def create_competitions_list_with_results(self):
        for competition_link in self.competitions_links_list:
            # for every competition create class Competition
            soup = BeautifulSoup(requests.get(competition_link).content, "lxml")
            competition_class = Competition(link=competition_link)

            for link in soup.findAll('a', href=True, title='Výsledky'):
                # for every class Competition add class Result
                # autofill every detail about competition and result
                result = competition_class.ResultsList(
                    link='http://www.slovak-ski.sk/zjazdove-lyzovanie/podujatia/' + link['href'])

                # TODO: fill results for my child immediately when searching for every result
                competition_class.results_list.append(result)
                competition_class.date = result.date
                competition_class.place = result.place
                result.create_racer_list_with_results(self.racer_list)

            self.competition_list.append(competition_class)

    def print_results_list(self):
        for competition in self.competition_list:
            print('\n-----------\nZoznam výsledkov podujatia v {}\n-----------\n'.format(competition.place))
            for result_list in competition.results_list:
                my_results = [x for x in result_list.racer_list if x.my_racer]
                if len(my_results) > 0:
                    print('Pre kategóriu {} pohlavie {}'.format(result_list.category, result_list.gender),
                          *my_results, sep='\n- ')

    def write_results_into_excel(self):
        from ExcelWritter import ExcelWritter
        writter = ExcelWritter(self.competition_list)
        # writter.write_into_excel()


def create_racers_list(racers_list_to_create):
    # TODO: better method
    def create_and_add_categories():
        global MP, SP, MZ, SZ, racer
        # TODO: ask for correction date
        MP = datetime.now().year - 8
        SP = MP - 3
        MZ = SP - 2
        SZ = MZ - 2
        for i, racer in enumerate(racers_list_to_create):
            if datetime.strptime(racers_list_to_create[i][1], '%Y').year <= datetime(SZ, 1, 1).year:
                racer.append("Staršie žiactvo")
                # print("SZ")
            elif datetime.strptime(racers_list_to_create[i][1], '%Y').year <= datetime(MZ, 1, 1).year:
                racer.append("Mladšie žiactvo")
                # print("MZ")
            elif datetime.strptime(racers_list_to_create[i][1], '%Y').year <= datetime(SP, 1, 1).year:
                racer.append("Staršie predžiactvo")
                # print("SP")
            elif datetime.strptime(racers_list_to_create[i][1], '%Y').year <= datetime(MP, 1, 1).year:
                racer.append("Mladšie predžiactvo")
                # print("MP")
            elif datetime.strptime(racers_list_to_create[i][1], '%Y').year >= datetime(MP, 1, 1).year:
                racer.append("Superbejby")
                # print("SB")
            else:
                print("Neviem rozpoznať dátum")

    create_and_add_categories()
    my_racers_list = []
    for racer in racers_list_to_create:
        my_racers_list.append(Racer(full_name=racer[0],
                                    year_of_birth=racer[1],
                                    country="SVK",
                                    category=racer[3],
                                    gender=racer[2]))

    print('Zoznam pretekárov v objektochg:', *[[x.full_name, x.category] for x in my_racers_list], sep='\n- ')

    return my_racers_list


def find_competitions_links(start_number, number_of_rounds):
    competitions_links_list = []
    link = "http://www.slovak-ski.sk/zjazdove-lyzovanie/podujatia/detail$"
    for x in range(start_number, start_number + number_of_rounds):
        competitions_links_list.append(link + str(x) + ".html")
    return competitions_links_list


def find_club_name_in_database(ski_club_name):
    # TODO: database of clubs_list into text file, to check if club is good or wrong spelled
    return True


def find_racers_by_club(ski_club):
    # "žiaci":"http://www.slovak-ski.sk/zjazdove-lyzovanie/pohare/jednotlivci$18.html"
    # "predžiaci": "http://www.slovak-ski.sk/zjazdove-lyzovanie/pohare/jednotlivci$17.html"
    # "zapocitane", http://www.slovak-ski.sk/zjazdove-lyzovanie/pohare/zapoctene$17.html
    # TODO: find racers_with_club_and_points_list by given urls
    racers_list = []
    racers_with_club_and_points_list = [
        "http://www.slovak-ski.sk/zjazdove-lyzovanie/pohare/jednotlivci$17:MP:M.html",
        "http://www.slovak-ski.sk/zjazdove-lyzovanie/pohare/jednotlivci$17:MP:L.html",
        "http://www.slovak-ski.sk/zjazdove-lyzovanie/pohare/jednotlivci$17:SP:M.html",
        "http://www.slovak-ski.sk/zjazdove-lyzovanie/pohare/jednotlivci$17:SP:L.html"]
    for link in racers_with_club_and_points_list:
        gender = str(str(link).rsplit(":", 1)[1]).split(".", 1)[0].upper()
        soup = BeautifulSoup(requests.get(link).content, "lxml")
        content = soup.find("table", {"class": "list"})
        for row in content.findChildren('tr'):
            # DANGEROUS but fast
            try:
                test = row.findChildren('td')
                for cell in test[4]:
                    if str(cell.string).capitalize() == ski_club.capitalize():
                        racers_list.append([test[2].text, test[3].text, gender])
            except IndexError:
                pass
                continue

    print('Zoznam nájdených pretekárov podľa klubu (ak majú body):', *racers_list, sep='\n- ')
    return racers_list


def find_results(racers_list):
    # TODO: remove duplicates from racers_list
    clean_list = []
    for x, element in enumerate(racers_list):
        racers_list[x][0] = element[0].title()
    [clean_list.append(x) for x in racers_list if x not in clean_list]

    categories = {
        "Predžiaci": find_competitions_links(651, 8),
        # "Žiaci": find_competitions_links(645, 6)
    }

    for competition_links in categories.values():
        print('Zoznam podujatí:', *competition_links, sep='\n- ')
        finder = ResultsFinder(competition_links, create_racers_list(racers_list))
        finder.create_competitions_list_with_results()
        finder.print_results_list()
        finder.write_results_into_excel()


if __name__ == "__main__":
    import argparse

    # TODO: create some database about racer and his page, club and so on for better speed

    parser = argparse.ArgumentParser(description='App for searching results from slovak-ski.sk')
    parser.add_argument('-sc', '--ski_club_name', type=str,
                        help='Argument for full ski club name, for searching result for racers from this club',
                        default=None)
    parser.add_argument('-cb', '--combine_search', action='store_true', default=True,
                        help='If you want to find racers by club, and add some racers from file use this')
    parser.add_argument('-rl', '--by_racers_list', action='store_true', default=False,
                        help='If you want to specify list of racers, e.g. from multiple clubs_list')
    args = parser.parse_args()

    racers = []

    if args.by_racers_list or args.combine_search:
        try:
            with open('racers_to_find_list.txt', 'r', encoding='utf-8-sig')as f:
                for line in f:
                    inner_list = [elt.strip() for elt in line.split(',')]
                    racers.append(inner_list)
        except IOError:
            print('fCannot read {f.name}')

    if not args.by_racers_list and args.ski_club_name is not None:
        clubs_list = args.ski_club_name.split(",")

        for club in clubs_list:
            if not find_club_name_in_database(ski_club_name=club):
                club = input("Insert the proper name of ski club for which you want to find results")

            # correct append racers in list
            [racers.append(x) for x in find_racers_by_club(club)]
            print(f'Start finding results for club {club}')

            find_results(racers)
    else:
        find_results(racers)
