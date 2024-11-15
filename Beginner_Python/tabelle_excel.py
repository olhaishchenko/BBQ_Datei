# dict_tab_big= {}
# dict_tab = {}
# # for j in range(12):
# for i in range(ord('A'), ord('C') + 1):
#     for j in range(1,3):
#         dict_tab[j]= chr(i)+str(j)
#     dict_tab_big.update({chr(i): dict_tab})
# print(dict_tab_big)

import tabelle
import csv


def erstelle_excel_tabelle(m_spalten, n_zeilen=None, value=None):
    ex_tab = dict()
    for sp in range(1, m_spalten + 1):
        spalten_name = chr(ord('A') + sp - 1)
        spalte = erstelle_spallte(spalten_name, n_zeilen, value)
        # ex_tabelle_füge_spalte_hinzu(ex_tab, spalten_name, spalte)
        ex_tab.update({spalten_name: spalte})
    return ex_tab


def erstelle_spallte(spalten_name, n_zeilen=0, value=None):
    spalte = dict()
    if n_zeilen:
        for z in range(1, n_zeilen + 1):
            zelle = erstelle_zellen_inhalt(spalten_name, z, value)
            spalte[z] = zelle
    else:
        for z in spalten_name:
            spalte.update({z: ''})
    return spalte


def erstelle_zellen_inhalt(spalten_name, zeilen_nr, value=None):
    if not value:
        return spalten_name + str(zeilen_nr)
    else:
        return value
    

def ex_tabelle_füge_spalte_hinzu(ex_tab, spalten_name, spalte):
    ex_tab.update({spalten_name: spalte})


def ex_tabelle_zellenwert(ex_tab, spalte, zeile):
    return ex_tab[spalte][zeile]


def ex_tabelle_setze_zellenwert(ex_tab, spalte, zeile, neuer_wert):
    alter_wert = ex_tabelle_zellenwert(ex_tab, spalte, zeile)
    ex_tab[spalte][zeile] = neuer_wert
    return alter_wert


# A2=17
def ex_tabelle_setze_wertformel(ex_tab, wert_formel):
    zs = wert_formel.split("=") # 0=>['A2', '17']
    adr = zs[0]
    wert = zs[1]
    spalte = adr[0]
    zeile = int(adr[1:])
    return ex_tabelle_setze_zellenwert(ex_tab, spalte, zeile,wert)


#A2=B1
def ex_tabelle_copyzeile(ex_tab, wert_formel):
    zs = wert_formel.split("=") # 0=>['A2', 'B1']
    adr1 = zs[0]
    adr2 = zs[1]
    spalte1 = adr1[0]
    zeile1 = int(adr1[1:])
    spalte2 = adr2[0]
    zeile2 = int(adr2[1:])
    nw = ex_tabelle_zellenwert(ex_tab, spalte2, zeile2)
    return ex_tabelle_setze_zellenwert(ex_tab, spalte1, zeile1, nw)    

def ex_tabelle_zu_CSV(ex_tab):
    spalten_namen = list(ex_tab.keys())
    zeilen_anzahl = len(ex_tab[spalten_namen[0]])
    rows = [spalten_namen]
    for i in range(1, zeilen_anzahl + 1):
        row = [ex_tab[spalte][i] for spalte in spalten_namen]
        rows.append([str(i)] + row)
    return rows


# def ex_tabelle_zu_CSV(ex_tab):
#     list_key = []
#     for key in ex_tab.keys():
#         list_key += key
#     list_key += '\n'

#     list_value = []
#     for value in ex_tab.values():
#         raus = False
        
#         for key in value.keys():
#             if len(list_value) == len(value):
#                 raus = True
#                 break
#             if key not in list_value:
#                 list_value += value
#         if raus:
#             break

#     list_lvalue = []
#     list_lvalue.append(list_key)
#     for i in range(1, len(list_value)+1):
#         lv = []
#         lv.append(str(i))
#         for j in range(len(list_key)-1):
#             inhalt = erstelle_zellen_inhalt(list_key[j], i)
#             lv.append(inhalt)
#         lv.append('\n')      
#         list_lvalue.append(lv)

#     csv_str = ","
#     for l in list_lvalue:
#         x = ','.join(l)
#         csv_str += x

#     return csv_str


def ex_tabelle_speichern_als_CSV(ex_tab, dateiname="mycsvfile.csv"):
    rows = ex_tabelle_zu_CSV(ex_tab)
    with open(dateiname, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(rows)


# def ex_tabelle_speichern_als_CSV(ex_tab):
#     with open("mycsvfile.csv", "w", newline="") as f:
#         f.write(ex_tabelle_zu_CSV(ex_tab))
#     return f


# def ex_tabelle_von_CSV_laden(dateiname):
 
#     with open(dateiname, "r") as csv_file:
#         data = csv_file.readlines()

#     list_aus_data = []
#     for row in data:
#         x = row.strip().split(',')
#         list_aus_data.append(x)

#     spalte_namen = list_aus_data[0][1:len(list_aus_data[0])-1]
#     ex_tab_dict2 = erstelle_spallte(spalte_namen)
#     print("2dict: ", ex_tab_dict2)


#     n_zeilen =  list_aus_data[1:]
#     zeilen_numer = []
#     value = []
#     for el in n_zeilen:
#         zeilen_numer.append(el[0])
#         el.pop(0)
#         el.pop()
#         value.append(el)

#     zu_dict = {}
#     for el in zeilen_numer:
#         zu_dict[el]=''
#     ex_tab_dict = {}
#     for sp_n in spalte_namen:
#         ex_tab_dict[sp_n] = zu_dict.copy() # WICHTIG

#     for i, row in enumerate(value):
#         for j, item in enumerate(row):
#             letter = spalte_namen[j]  # 'A', 'B', 'C', ...
#             number = zeilen_numer[i]  # '1', '2', '3', ...
#             ex_tab_dict[letter][number] = item

#     return ex_tab_dict


def ex_tabelle_von_CSV_laden(dateiname):
    with open(dateiname, newline="") as csv_file:
        reader = csv.reader(csv_file)
        data = list(reader)

    spalte_namen = data[0][1:-1]
    ex_tab = {spalte: {} for spalte in spalte_namen}
    
    for row in data[1:]:
        zeilen_nr = int(row[0])
        for j, item in enumerate(row[1:-1]):
            ex_tab[spalte_namen[j]][zeilen_nr] = item
    
    return ex_tab


    
if __name__ == "__main__":

    super_tabelle = erstelle_excel_tabelle(7, 10)
    tabelle.tabelle_ausgeben(super_tabelle)
    # sp = input("Geben Sie die Spalte an: ")
    # ze = int(input("Geen Sie Die Zeile an: "))
    
    #zellenwert = ex_tabelle_zellenwert(super_tabelle, sp, ze)
    # nw = input("Geben Sie den neuen Wert ein: ")
    # alter_zellenwert = ex_tabelle_setze_wertformel(super_tabelle, sp, ze,nw)

    # formel = input("Geben Sie die Formel an: ")
    # alter_zellenwert = ex_tabelle_setze_wertformel(super_tabelle, formel)

    # formel = input("Geben Sie die Formel an: ")
    # alter_zellenwert = ex_tabelle_copyzeile(super_tabelle, formel)

    # ex_tabelle_zu_CSV(super_tabelle)
    # print(ex_tabelle_zu_CSV(super_tabelle))
    r = ex_tabelle_speichern_als_CSV(super_tabelle)
    new_tabelle =  ex_tabelle_von_CSV_laden('mycsvfile.csv')
    tabelle.tabelle_ausgeben(new_tabelle)
    # tabelle.tabelle_ausgeben(super_tabelle)
    # print("Zellen: ", alter_zellenwert)

    
