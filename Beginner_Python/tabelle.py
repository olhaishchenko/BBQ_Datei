# ASCII-Tablle von Code 32 bis 255 in 7 Spalten
spalte1 = {a: chr(a) for a in range(32, 64)}
spalte2 = {a: chr(a) for a in range(64, 96)}
spalte3 = {a: chr(a) for a in range(96, 128)}
spalte4 = {a: chr(a) for a in range(128, 160)}
spalte5 = {a: chr(a) for a in range(160, 192)}
spalte6 = {a: chr(a) for a in range(192, 224)}
spalte7 = {a: chr(a) for a in range(224, 256)}

# Zeilen (255-32+1)/7
ascii_tabelle = {
    1: spalte1,
    2: spalte2,
    3: spalte3,
    4: spalte4,
    5: spalte5,
    6: spalte6,
    7: spalte7,
}


def erzeuge_ascii_tabelle():
    s = 0
    spalte = None
    ascii_t = dict()
    for i in range(32, 256):
        if (i - 32) % 32 == 0:
            s += 1
            spalte = dict()
            ascii_t[s] = spalte
        spalte[i] = chr(i)
    return ascii_t

ascii_tabelle = erzeuge_ascii_tabelle()


def tabelle_ausgeben(tabellen_dict):
    tabellen_kopf_ausgeben(tabellen_dict)
    n_zeilen = anzahl_zeilen(tabellen_dict)
    n_spalten = len(tabellen_dict.items())
    for zi in range(1, n_zeilen + 1):
        dz = daten_zeile(tabellen_dict, zi)
        tabellen_zeile_ausgeben(dz, zi)
    print("   "+("+---" * n_spalten) + "+")

def tabellen_kopf_ausgeben(tabellen_dict):
    dz = []
    for sp_name in tabellen_dict.keys():
        dz.append(sp_name)
    tabellen_zeile_ausgeben(dz, None)

def anzahl_zeilen(tb_d):
    # alle Spalten gleich lang
    sp_vs = tb_d.values()
    for sp_d in sp_vs:
        return len(sp_d)


def daten_zeile(tb_d, zeilen_nr):
    dz = []
    for sp_i, sp_d in tb_d.items():
        zi = 1
        for k, v in sp_d.items():
            if zi == zeilen_nr:
                # dz.append(k)
                dz.append(v)
            zi += 1
    return dz


def tabellen_zeile_ausgeben(dz, zeilen_nr):
    if zeilen_nr:
        print("   "+("+---" * len(dz)) + "+")
        print(f'{zeilen_nr:>3}', end="")
    else: 
        print(f'   ', end="")
    for d in dz:
        p = f"{d:>3}"
        if isinstance(d, str):
            p = "   "
            if len(d)==1:
                d = bytes([ord(d)]).decode("cp437")
                if d.isprintable():
                    p = f"{d:^3}"
            else:
                p = f"{d:>3}"
        if zeilen_nr:
            print("|"+f"{p}",end="")
        else:
            print(" "+f"{p}", end="")
        # print(f"|{p}", end="")
    print("|"*int(bool(zeilen_nr)))


# tabelle_ausgeben(ascii_tabelle)
