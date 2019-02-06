#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime

import requests
from bs4 import BeautifulSoup

from local_settings import *


def add_dates_to_categories(MP_date_from=datetime.now().year):
    global MP, SP, MZ, SZ
    MP = MP_date_from - 8
    SP = MP - 3
    MZ = SP - 2
    SZ = MZ - 2


def find_competitions_links(start_number, number_of_rounds):
    competitions_links_list = []
    link = "http://www.slovak-ski.sk/zjazdove-lyzovanie/podujatia/detail$"
    for x in range(start_number, start_number + number_of_rounds):
        competitions_links_list.append(link + str(x) + ".html")
    return competitions_links_list


def add_category_to_racers():
    help = 0
    for x in racers_list:
        if datetime.strptime(racers_list[help][1], '%d.%m.%Y').year <= datetime(SZ, 1, 1).year:
            x.append("Staršie žiactvo")
            # print "SZ"
        elif datetime.strptime(racers_list[help][1], '%d.%m.%Y').year <= datetime(MZ, 1, 1).year:
            x.append("Mladšie žiactvo")
            # print "MZ"
        elif datetime.strptime(racers_list[help][1], '%d.%m.%Y').year <= datetime(SP, 1, 1).year:
            x.append("Staršie predžiactvo")
            # print "SP"
        elif datetime.strptime(racers_list[help][1], '%d.%m.%Y').year <= datetime(MP, 1, 1).year:
            x.append("Mladšie predžiactvo")
            # print "MP"
        elif datetime.strptime(racers_list[help][1], '%d.%m.%Y').year >= datetime(MP, 1, 1).year:
            x.append("Superbejby")
            # print "SB"
        else:
            print("Neviem rozpoznať dátum")
        help = help + 1


class ResultsFinder:
    def __init__(self, competitions_links_list):
        # self.data = []
        # self.data_sorted_by_date_of_birth = []
        # self.header_list = []
        # self.competition_list = []
        # self.results_of_racers = []
        self.events_list = []
        self.competitions_links_list = competitions_links_list

        self.words_to_sort = [x.lower() for x in ["Nedokočili", "Neštartovali", "Diskvalifikovaní"]]

        for item in racers_list:
            item[0] = item[0].lower()

        add_dates_to_categories()

    def create_competitions_list(self):
        # TODO: create list of all comptetiions as object Competition - add category,date and so on
        for x in self.competitions_links_list:
            soup = BeautifulSoup(requests.get(x).content, "lxml")

            for link in soup.findAll('a', href=True, title='Výsledky'):
                self.events_list.append('http://www.slovak-ski.sk/zjazdove-lyzovanie/podujatia/' + link['href'])

    # def search_on_web(self):
    #     for competition in competition_list:
    #         zapisuj = ""
    #         del data[:]
    #         del data_sorted_by_date_of_birth[:]
    #         del header_list[:]
    #         data.append("")
    #         data_sorted_by_date_of_birth.append("")
    #         selected_page = competition
    #         print(colored('<=================>', "blue"))
    #
    #         try:
    #             page = urllib.request.urlopen(selected_page)
    #             soup = BeautifulSoup(page, 'html.parser')
    #         except Exception as e:
    #             try:
    #                 soup = BeautifulSoup(page, 'html.parser')
    #             except Exception as e:
    #                 print(e)
    #                 break
    #
    #         # táto časť potrebuje ošetrenie - nemuselo by sa podariť načítať tabuľky
    #         try:
    #             tables = soup.findChildren('table')
    #             header_table = tables[0]
    #         except Exception as e:
    #             print(e)
    #             try:
    #                 time.sleep(3)
    #                 print("Sleeping for 3 seconds")
    #                 tables = soup.findChildren('table')
    #                 header_table = tables[0]
    #             except Exception as e:
    #                 print(e)
    #                 exit(0)
    #
    #         my_table = tables[1]
    #         rows = my_table.findChildren(['tr'])
    #         header_rows = header_table.findChildren(['tr'])
    #
    #         # vypisovanie hlavičiek stránky
    #         for row in header_rows:
    #             cells = row.findChildren('td')
    #             for cell in cells:
    #                 value = cell.string
    #                 header_list.append(value)
    #
    #         print(header_list[0])
    #         print(header_list[2])
    #         print(header_list[3])
    #         print(header_list[4])
    #         print(header_list[5])
    #         print(header_list[6])
    #         print(colored('<=================>', "blue"))
    #
    #         # print map(lambda x: x.lower(), words_to_sort)
    #
    #         # If you want to do this using regex, you could simply use a non-capturing group,
    #         # to get the word "world" and then grab everything after, like so
    #         # (?:world)
    #
    #         # získanie dát z jedlotlivých súťaží, ako umiestnenie a pod
    #         for row in rows:
    #             data_list = []
    #             cells = row.findChildren('td')
    #             for cell in cells:
    #                 value = str(cell.string).lower()
    #                 data_list.append(value)
    #                 # print "The value in this cell is %s" % value
    #
    #             if 0 < len(data_list) <= 1:
    #                 for x in words_to_sort:
    #                     if data_list[0].find(x) != -1:
    #                         # print data_list[0]
    #                         zapisuj = data_list[0]
    #                         # write to next data this value for better sorting later
    #             else:
    #                 if zapisuj != "":
    #                     data_list[0] = zapisuj
    #                 # filtrujem slovákov
    #                 if len(data_list) >= 5:
    #                     if data_list[5].lower() == "svk" and len(data_list) >= 5:
    #                         data.append(data_list)
    #             # print str(data)
    #
    #         for racer in racers_list:
    #             search(racer)
    #
    # def search(self, racer):
    #     nasiel_som_pretekara_ale_DNS_DNF = False
    #     najdene = False
    #     hladam = False
    #     prvy_v_rocniku = ""
    #     if racer[2] == 'z':
    #         racer[2] = "ženy"
    #     if racer[2] == 'm':
    #         racer[2] = "muži"
    #     name_to_find = racer[0]
    #     if header_list[5] == racer[3] and header_list[3] == racer[2]:
    #         hladam = True
    #         print(colored("Hľadám meno " + racer[0], "yellow"))
    #         del data_sorted_by_date_of_birth[:]
    #         data_sorted_by_date_of_birth.append("")
    #         # search for all racer in year of founded race from my team and create list of them
    #
    #         # celkovo
    #         for x in data:
    #             if name_to_find.lower() in x:
    #                 najdene = True
    #                 print(colored("Našiel som meno: " + name_to_find, "green"))
    #                 nasiel_som_pretekara_ale_DNS_DNF = find_rank_and_loss(1, data.index(x), data)
    #                 break
    #
    #         if nasiel_som_pretekara_ale_DNS_DNF:
    #             # v ročníku
    #             date_position = 4
    #             for x in data:
    #                 if len(x) >= date_position:
    #                     target = x[date_position]
    #                     if int(target) >= int(datetime.strptime(racer[1], '%d.%m.%Y').year):
    #                         data_sorted_by_date_of_birth.append(x)
    #
    #             if data_sorted_by_date_of_birth:
    #                 for x in data_sorted_by_date_of_birth:
    #                     if name_to_find.lower() in x:
    #                         najdene = True
    #                         print(colored("Našiel som meno v zozname ročníkov: " + name_to_find, "green"))
    #                         if prvy_v_rocniku == "":
    #                             find_rank_and_loss(1, data_sorted_by_date_of_birth.index(x),
    #                                                data_sorted_by_date_of_birth)
    #                         break
    #
    #     else:
    #         if not najdene and not hladam:
    #             print(colored("Nehľadal meno(nespĺňa kategóriu): " + name_to_find, "cyan"))
    #
    #     if not najdene and hladam:
    #         print(colored("Nenašiel som meno: " + name_to_find + ". Takže sa  asi nezúčastnil/a týchto pretekov ",
    #                       "red"))
    #         create_results_of_racers_list(data, 0, 0, 1, False, name_to_find, 0)
    #
    # def find_rank_and_loss(self, first, index, data_from):
    #     # tu niekde je chyba ktorá vkladá do poľa aj pretekárky ktoré tam nemajú byť, matea valča 45-46 v array
    #
    #     # riešenie textu, pokiaľ ej sortovanie v ročníku, pridanie strinug
    #
    #     text = ""
    #     if data_from == data_sorted_by_date_of_birth:
    #         text = " v ročníku"
    #
    #     DNS_DNF = data_from[index][0].split(" ")
    #
    #     if DNS_DNF[0] not in words_to_sort:
    #
    #         best_racer = data_from[1][9]
    #         compare_racer = data_from[index][9]
    #
    #         if len(best_racer) > 5:
    #             best_racer = datetime.strptime(best_racer, '%M:%S.%f')
    #         else:
    #             best_racer = datetime.strptime(best_racer, '%S.%f')
    #
    #         if len(compare_racer) > 5:
    #             compare_racer = datetime.strptime(compare_racer, '%M:%S.%f')
    #         else:
    #             compare_racer = datetime.strptime(compare_racer, '%S.%f')
    #
    #         # print ("%s minutes, %s seconds, %s millisecond " % (best_racer.minute, best_racer.second, best_racer.microsecond))
    #         microsecond_formated_a = round(float(best_racer.microsecond / 10000) / 100, 2)
    #         microsecond_formated_b = round(float(compare_racer.microsecond / 10000) / 100, 2)
    #
    #         time_best = float(best_racer.minute * 60 + best_racer.second + microsecond_formated_a)
    #         time_compare = float(compare_racer.minute * 60 + compare_racer.second + microsecond_formated_b)
    #
    #         differece = float(time_compare - time_best)
    #         difference_in_percent = float((time_compare / time_best) * 100 - 100)
    #
    #         print(str(1) + " . pretekár/ka" + text)
    #         print(data_from[1][3], time_best)
    #
    #         print(str(index) + " pretekár/ka" + text)
    #         print(data_from[index][3], "strata:" + text, "+" + str(differece), str(
    #             difference_in_percent) + "%")
    #
    #         create_results_of_racers_list(data_from, index, difference_in_percent, first, True, data_from[index][3],
    #                                       strata=differece)
    #         return True
    #     else:
    #         create_results_of_racers_list(data, index, 0, 1, True, data_from[index][3], -1)
    #         return False
    #
    # def create_results_of_racers_list(self, data_from, index, percentualna_strata, prva, zucastnil, meno, strata):
    #     local_column = []
    #     for element in header_list:
    #         local_column.append(header_list[header_list.index(element)].strip(","))
    #
    #     if zucastnil:
    #         try:
    #             results_of_racers.append([local_column,
    #                                       zucastnil,
    #                                       data_from[index][3],
    #                                       data_from[index][9],
    #                                       data_from[prva][3],
    #                                       data_from[prva][9],
    #                                       strata,
    #                                       percentualna_strata,
    #                                       data_from[index][0],
    #                                       index,
    #                                       len(data_from)
    #                                       ])
    #         except Exception as e:
    #             print(e)
    #             try:
    #                 results_of_racers.append([local_column, zucastnil, meno, data_from[index][0]])
    #             except Exception as e:
    #                 print(e)
    #
    #     else:
    #         results_of_racers.append([local_column, zucastnil, meno, -1])
    #
    # def zapis_do_excelu(self, racers_list_with_results):
    #     results_of_racers_test = racers_list_with_results
    #     import xlsxwriter
    #     start_row = 3  # must be >= 3
    #     file = "Výsledky AC_UNIZA %s-%s.xlsx" % (datetime.now().year - 1, datetime.now().year)
    #
    #     my_worksheets = {}
    #     workbook = xlsxwriter.Workbook(file)
    #
    #     format1 = workbook.add_format({'bg_color': '#FFC7CE',
    #                                    'font_color': '#9C0006'})
    #     format2 = workbook.add_format({'bg_color': '#C6EFCE',
    #                                    'font_color': '#006100'})
    #     merge_format = workbook.add_format({
    #         'bold': 1,
    #         'border': 1,
    #         'align': 'center',
    #         'valign': 'vcenter',
    #         'fg_color': '#00b0f0'})
    #
    #     for x in racers_list_with_results:
    #         index = racers_list_with_results.index(x)
    #         test = str(racers_list_with_results[index][2]).split(" ")
    #         name_formated = test[0].upper() + " " + test[1].title()
    #
    #         if len(test) > 2:
    #             name_formated = test[0].upper() + " " + test[1].title() + test[2].title()
    #
    #         existing_ws = workbook.get_worksheet_by_name(name_formated)
    #
    #         if existing_ws:
    #             worksheet = existing_ws
    #             my_worksheets[worksheet.get_name()][1] += 1
    #         else:
    #             worksheet = workbook.add_worksheet(name_formated)
    #             my_worksheets[worksheet.get_name()] = [worksheet.get_name(), 1]
    #
    #         column = my_worksheets[worksheet.get_name()][1]
    #
    #         if column == 1:
    #             worksheet.conditional_format(start_row + 7, 1, start_row + 7, 17, {'type': 'cell',
    #                                                                                'criteria': '>',
    #                                                                                'value': "10%",
    #                                                                                'format': format1})
    #             worksheet.conditional_format(start_row + 7, 1, start_row + 7, 17, {'type': 'cell',
    #                                                                                'criteria': '>',
    #                                                                                'value': 0,
    #                                                                                'format': format2})
    #
    #             fmt = workbook.add_format(
    #                 {'num_format': '0.00%', 'text_wrap': True, 'align': 'center', 'valign': 'vcenter'})
    #             worksheet.set_row(start_row + 7, cell_format=fmt)
    #
    #             cell_format_wrap = workbook.add_format({'text_wrap': True, 'align': 'center', 'valign': 'vcenter'})
    #             worksheet.set_column("B:Z", width=13.43, cell_format=cell_format_wrap)
    #
    #             cell_format_header = workbook.add_format({'bold': True, 'font_size': 12})
    #             worksheet.set_column("A:A", width=30, cell_format=cell_format_header)
    #
    #             write_headers_to_EXCEL(workbook.add_format({'bold': 1}),
    #                                    cell_format_header, index, name_formated, racers_list_with_results, start_row,
    #                                    worksheet)
    #
    #         if column % 2 == 0 and column > 1:
    #             worksheet.merge_range(start_row, column - 1, start_row, column,
    #                                   str(racers_list_with_results[index][0][0]),
    #                                   merge_format)
    #             worksheet.merge_range(start_row + 1, column - 1, start_row + 1, column,
    #                                   str(racers_list_with_results[index][0][6]), merge_format)
    #
    #         if racers_list_with_results[index][1]:
    #             if len(racers_list_with_results[index]) > 4:
    #                 myformat = workbook.add_format(
    #                     {'bold': True, 'font_size': 12, 'fg_color': '#00b0f0', 'border': True})
    #                 worksheet.write(start_row + 2, column, "Celkovo(SVK)",
    #                                 myformat) if column % 2 == 1 else worksheet.write(start_row + 2, column,
    #                                                                                   "Ročník(SVK)",
    #                                                                                   myformat)
    #
    #                 worksheet.write(start_row + 3, column, racers_list_with_results[index][4].title())
    #                 worksheet.write(start_row + 4, column, racers_list_with_results[index][5])
    #                 worksheet.write(start_row + 5, column, racers_list_with_results[index][3])
    #                 worksheet.write(start_row + 6, column, racers_list_with_results[index][6])
    #                 worksheet.write(start_row + 7, column, racers_list_with_results[index][7] / 100)
    #                 worksheet.write(start_row + 8, column, racers_list_with_results[index][9])
    #                 worksheet.write(start_row + 9, column, racers_list_with_results[index][10])
    #             else:
    #                 my_worksheets[worksheet.get_name()][1] = my_worksheets[worksheet.get_name()][1] + 1
    #
    #                 column = my_worksheets[worksheet.get_name()][1]
    #                 worksheet.merge_range(start_row, column - 1, start_row, column,
    #                                       str(racers_list_with_results[index][0][0]), merge_format)
    #                 worksheet.merge_range(start_row + 1, column - 1, start_row + 1, column,
    #                                       str(racers_list_with_results[index][0][6]), merge_format)
    #
    #                 worksheet.merge_range(start_row + 2, column - 1, start_row + 9, column,
    #                                       racers_list_with_results[index][3],
    #                                       workbook.add_format({
    #                                           'bold': 1,
    #                                           'border': 1,
    #                                           'align': 'center',
    #                                           'valign': 'vcenter',
    #                                           'fg_color': 'yellow'}))
    #         else:
    #             # pre celkovo
    #             # worksheet.write(start_row + 2, column, "nezúčastnil/a sa")
    #
    #             # pre ročník
    #             my_worksheets[worksheet.get_name()][1] = my_worksheets[worksheet.get_name()][1] + 1
    #
    #             column = my_worksheets[worksheet.get_name()][1]
    #             if column % 2 == 0 and column > 1:
    #                 worksheet.merge_range(start_row, column - 1, start_row, column,
    #                                       str(racers_list_with_results[index][0][0]), merge_format)
    #                 worksheet.merge_range(start_row + 1, column - 1, start_row + 1, column,
    #                                       str(racers_list_with_results[index][0][6]),
    #                                       merge_format)
    #
    #                 worksheet.merge_range(start_row + 2, column - 1, start_row + 2, column, "nezúčastnil/a sa",
    #                                       workbook.add_format({
    #                                           'bold': 1,
    #                                           'border': 1,
    #                                           'align': 'center',
    #                                           'valign': 'vcenter',
    #                                           'fg_color': 'red'}))
    #
    #     for sheet in my_worksheets:
    #         worksheet = workbook.get_worksheet_by_name(sheet)
    #         worksheet.merge_range(0, 4, 0, 5, 'Najmenšia strata celkovo(%):')
    #         worksheet.write_formula('G1', '=OFFSET(INDEX($11:$11,MATCH(MIN($11:$11),$11:$11,0)),0,0)', fmt)
    #         worksheet.write_formula('H1',
    #                                 '=IF(MOD(MATCH(MIN($11:$11),$11:$11,0),2)=0,OFFSET(INDEX($11:$11,MATCH(MIN($11:$11),$11:$11,0)),-7,0),OFFSET(INDEX($11:$11,MATCH(MIN($11:$11),$11:$11,0)),-7,-1))')  # OK
    #
    #         worksheet.merge_range(1, 4, 1, 5, 'Najlepšie umiestnenie celkovo:')
    #         worksheet.write_formula('G2', '=OFFSET(INDEX($12:$12,MATCH(MIN($12:$12),$12:$12,0)),0,0)')
    #         worksheet.write_formula('H2',
    #                                 '=IF(MOD(MATCH(MIN($12:$12),$12:$12,0),2)=0,OFFSET(INDEX($12:$12,MATCH(MIN($12:$12),$12:$12,0)),-8,0),OFFSET(INDEX($12:$12,MATCH(MIN($12:$12),$12:$12,0)),-8,-1))')  # OK
    #
    #         worksheet.merge_range(0, 9, 0, 10, 'Najmenšia strata ročník(%):')
    #         worksheet.write_formula('L1', '=OFFSET(INDEX($11:$11,MATCH(MIN($11:$11),$11:$11,0)),0,0)', fmt)
    #         worksheet.write_formula('M1',
    #                                 '=IF(MOD(MATCH(MIN($11:$11),$11:$11,0),2)=0,OFFSET(INDEX($11:$11,MATCH(MIN($11:$11),$11:$11,0)),-7,0),OFFSET(INDEX($11:$11,MATCH(MIN($11:$11),$11:$11,0)),-7,-1))')  # OK
    #
    #         worksheet.merge_range(1, 9, 1, 10, 'Najlepšie umiestnenie ročník:')
    #         worksheet.write_formula('L2', '=OFFSET(INDEX($12:$12,MATCH(MIN($12:$12),$12:$12,0)),0,0)')
    #         worksheet.write_formula('M2',
    #                                 '=IF(MOD(MATCH(MIN($12:$12),$12:$12,0),2)=0,OFFSET(INDEX($12:$12,MATCH(MIN($12:$12),$12:$12,0)),-8,0),OFFSET(INDEX($12:$12,MATCH(MIN($12:$12),$12:$12,0)),-8,-1))')  # OK
    #
    #         # =OFFSET(INDEX($11:$11,MATCH(MIN($11:$11),$11:$11,0)),0,0)
    #         # =OFFSET(INDEX($11:$11,MATCH(MIN($11:$11),$11:$11,0)),-7,-1)
    #
    #     try:
    #         workbook.close()
    #         print(colored("Všetko prebehlo v poriadku", "green"))
    #     except IOError as e:
    #         print(colored("Nepodarilo sa uložiť, dokument sa používa", "red"), e)
    #
    # def write_headers_to_EXCEL(self, merge_format, cell_format_header, index, name_formated, racers_list_with_results,
    #                            start_row,
    #                            worksheet):
    #     column_headers = 0
    #     worksheet.write(start_row - 3, column_headers, str(name_formated))
    #
    #     aaa = [x for x in racers_list if name_formated.lower() in x]
    #     try:
    #         worksheet.write(start_row - 3, column_headers + 1, str(aaa[0][1]), cell_format_header)
    #         kategoria = 2015
    #         if aaa[0][3] == "Staršie žiactvo":
    #             kategoria = SZ
    #         if aaa[0][3] == "Mladšie žiactvo":
    #             kategoria = MZ
    #         if aaa[0][3] == "Staršie predžiactvo":
    #             kategoria = SP
    #         if aaa[0][3] == "Mladšie predžiactvo":
    #             kategoria = MP
    #
    #         pocet_rokov_v_kat = kategoria - datetime.strptime(aaa[0][1], '%d.%m.%Y').year + 1
    #         worksheet.merge_range(start_row - 3, column_headers + 2, start_row - 3, column_headers + 3,
    #                               str(pocet_rokov_v_kat) + ". rok v kategorií", merge_format)
    #     except Exception as e:
    #         print(e)
    #         pass
    #
    #     worksheet.write(start_row - 1, column_headers, "Sezóna " + str(MP + 7) + "/" + str(MP + 8))
    #     worksheet.write(start_row - 1, column_headers + 1, str(racers_list_with_results[index][0][5]),
    #                     cell_format_header)
    #     worksheet.write(start_row, column_headers, "Miesto konania: ")
    #     worksheet.write(start_row + 1, column_headers, "Dátum konania: ")
    #     worksheet.write(start_row + 3, column_headers, "Meno najlepšieho: ")
    #     worksheet.write(start_row + 4, column_headers, "Najlepší čas: ")
    #     worksheet.write(start_row + 5, column_headers, "Čas porov. pretekára: ")
    #     worksheet.write(start_row + 6, column_headers, "Časová strata ")
    #     worksheet.write(start_row + 7, column_headers, "% strata ", cell_format_header)
    #     worksheet.write(start_row + 8, column_headers, "umiestnenie ")
    #     worksheet.write(start_row + 9, column_headers, "celkový počet pretekárov ")


if __name__ == "__main__":
    # http://www.slovak-ski.sk/zjazdove-lyzovanie/podujatia/detail$651.html
    # to
    # 650+8
    # http://www.slovak-ski.sk/zjazdove-lyzovanie/podujatia/detail$658.html

    # competitions "žiaci" starts from
    # http://www.slovak-ski.sk/zjazdove-lyzovanie/podujatia/detail$645.html
    # to
    # 644 + 6
    # http://www.slovak-ski.sk/zjazdove-lyzovanie/podujatia/detail$650.html
    # TODO: create 2 list of comptetiions

    categories = {
        "Predžiaci": find_competitions_links(651, 8),
        "Žiaci": find_competitions_links(645, 6)
    }

    for competition_links in categories.values():
        print('Zoznam podujatí:', *competition_links, sep='\n- ')
        ResultsFinder(competition_links).create_competitions_list()

    # test = ResultsFinder(categories)
    # print('Predžiaci:', *test, sep='\n- ')

    # add_category_to_racers()
    # zapis_do_excelu(results_of_racers_test)
