from datetime import datetime


class ExcelWriter:
    def __init__(self, competitions_list):
        self.competitions_list = competitions_list
        pass

    def write_into_excel(self, racer_list):
        import xlsxwriter
        start_row = 3  # must be >= 3
        file = "Výsledky AC_UNIZA %s-%s -- test.xlsx" % (datetime.now().year - 1, datetime.now().year)
        #
        my_worksheets = {}
        workbook = xlsxwriter.Workbook(file)
        #
        format1 = workbook.add_format({'bg_color': '#FFC7CE',
                                       'font_color': '#9C0006'})
        format2 = workbook.add_format({'bg_color': '#C6EFCE',
                                       'font_color': '#006100'})
        merge_format = workbook.add_format({
            'bold': 1,
            'border': 1,
            'align': 'center',
            'valign': 'vcenter',
            'fg_color': '#00b0f0'})

        for index, racer in enumerate(racer_list):
            name_formated = racer.surname.upper() + " " + racer.name.title()

            existing_ws = workbook.get_worksheet_by_name(name_formated)

            if existing_ws:
                worksheet = existing_ws
                my_worksheets[worksheet.get_name()][1] += 1
            else:
                worksheet = workbook.add_worksheet(name_formated)
                my_worksheets[worksheet.get_name()] = [worksheet.get_name(), 1]

            column = my_worksheets[worksheet.get_name()][1]

            if column == 1:
                worksheet.conditional_format(start_row + 7, 1, start_row + 7, 17, {'type': 'cell',
                                                                                   'criteria': '>',
                                                                                   'value': "10%",
                                                                                   'format': format1})
                worksheet.conditional_format(start_row + 7, 1, start_row + 7, 17, {'type': 'cell',
                                                                                   'criteria': '>',
                                                                                   'value': 0,
                                                                                   'format': format2})

                fmt = workbook.add_format(
                    {'num_format': '0.00%', 'text_wrap': True, 'align': 'center', 'valign': 'vcenter'})
                worksheet.set_row(start_row + 7, cell_format=fmt)

                cell_format_wrap = workbook.add_format({'text_wrap': True, 'align': 'center', 'valign': 'vcenter'})
                worksheet.set_column("B:Z", width=13.43, cell_format=cell_format_wrap)

                cell_format_header = workbook.add_format({'bold': True, 'font_size': 12})
                worksheet.set_column("A:A", width=30, cell_format=cell_format_header)
                column_headers = 0
                worksheet.write(start_row - 3, column_headers, str(name_formated))

                worksheet.write(start_row - 1, column_headers, "Sezóna " +
                                str(datetime.now().year - 1) + "!" +
                                str(datetime.now().year))
                worksheet.write(start_row - 1, column_headers + 1, str(racer.category),
                                cell_format_header)
                worksheet.write(start_row, column_headers, "Miesto konania: ")
                worksheet.write(start_row + 1, column_headers, "Dátum konania: ")
                worksheet.write(start_row + 3, column_headers, "Meno najlepšieho: ")
                worksheet.write(start_row + 4, column_headers, "Najlepší čas: ")
                worksheet.write(start_row + 5, column_headers, "Čas porov. pretekára: ")
                worksheet.write(start_row + 6, column_headers, "Časová strata ")
                worksheet.write(start_row + 7, column_headers, "% strata ", cell_format_header)
                worksheet.write(start_row + 8, column_headers, "Umiestnenie ")
                worksheet.write(start_row + 9, column_headers, "Celkový počet pretekárov ")

        workbook.close();

    # aaa = [x for x in racers_list if name_formated.lower() in x]
    # try:
    #     worksheet.write(start_row - 3, column_headers + 1, str(aaa[0][1]), cell_format_header)
    #     kategoria = 2015
    #     if aaa[0][3] == "Staršie žiactvo":
    #         kategoria = SZ
    #     if aaa[0][3] == "Mladšie žiactvo":
    #         kategoria = MZ
    #     if aaa[0][3] == "Staršie predžiactvo":
    #         kategoria = SP
    #     if aaa[0][3] == "Mladšie predžiactvo":
    #         kategoria = MP

    #     pocet_rokov_v_kat = kategoria - datetime.strptime(aaa[0][1], '%d.%m.%Y').year + 1
    #     worksheet.merge_range(start_row - 3, column_headers + 2, start_row - 3, column_headers + 3,
    #                           str(pocet_rokov_v_kat) + ". rok v kategorií", merge_format)
    # except Exception as e:
    # print(e)
    # pass

    # worksheet.write(start_row - 1, column_headers, "Sezóna " + str(MP + 7) + "/" + str(MP + 8))
    # worksheet.write(start_row - 1, column_headers + 1, str(racers_list_with_results[index][0][5]),
    #                 cell_format_header)
    # worksheet.write(start_row, column_headers, "Miesto konania: ")
    # worksheet.write(start_row + 1, column_headers, "Dátum konania: ")
    # worksheet.write(start_row + 3, column_headers, "Meno najlepšieho: ")
    # worksheet.write(start_row + 4, column_headers, "Najlepší čas: ")
    # worksheet.write(start_row + 5, column_headers, "Čas porov. pretekára: ")
    # worksheet.write(start_row + 6, column_headers, "Časová strata ")
    # worksheet.write(start_row + 7, column_headers, "% strata ", cell_format_header)
    # worksheet.write(start_row + 8, column_headers, "umiestnenie ")
    #     worksheet.write(start_row + 9, column_headers, "celkový počet pretekárov ")
    # write_headers_to_EXCEL(workbook.add_format({'bold': 1}),
    #                        cell_format_header, index, name_formated, racers_list_with_results, start_row,
    #                                    worksheet)
    #
    #         if column % 2 == 0 and column > 1:
    #             worksheet.merge_range(start_row, column - 1, start_row, column, str(racers_list_with_results[index][0][0]),
    #                                   merge_format)
    #             worksheet.merge_range(start_row + 1, column - 1, start_row + 1, column,
    #                                   str(racers_list_with_results[index][0][6]), merge_format)
    #
    #         if racers_list_with_results[index][1]:
    #             if len(racers_list_with_results[index]) > 4:
    #                 myformat = workbook.add_format({'bold': True, 'font_size': 12, 'fg_color': '#00b0f0', 'border': True})
    #                 worksheet.write(start_row + 2, column, "Celkovo(SVK)",
    #                                 myformat) if column % 2 == 1 else worksheet.write(start_row + 2, column, "Ročník(SVK)",
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
    #
    # def write_headers_to_EXCEL(merge_format, cell_format_header, index, name_formated, racers_list_with_results, start_row,
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
    #     worksheet.write(start_row - 1, column_headers + 1, str(racers_list_with_results[index][0][5]), cell_format_header)
    #     worksheet.write(start_row, column_headers, "Miesto konania: ")
    #     worksheet.write(start_row + 1, column_headers, "Dátum konania: ")
    #     worksheet.write(start_row + 3, column_headers, "Meno najlepšieho: ")
    #     worksheet.write(start_row + 4, column_headers, "Najlepší čas: ")
    #     worksheet.write(start_row + 5, column_headers, "Čas porov. pretekára: ")
    #     worksheet.write(start_row + 6, column_headers, "Časová strata ")
    #     worksheet.write(start_row + 7, column_headers, "% strata ", cell_format_header)
    #     worksheet.write(start_row + 8, column_headers, "umiestnenie ")
    #     worksheet.write(start_row + 9, column_headers, "celkový počet pretekárov ")
