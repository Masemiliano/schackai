import random

print("LET'S PLAY SCHACK!")

rutnat = ["A1", "B1", "C1", "D1", "E1", "F1", "G1", "H1", "A2", "B2", "C2", "D2", "E2", "F2", "G2", "H2", "A3",
          "B3", "C3", "D3", "E3", "F3", "G3", "H3", "A4", "B4", "C4", "D4", "E4", "F4", "G4", "H4", "A5", "B5",
          "C5", "D5", "E5", "F5", "G5", "H5", "A6", "B6", "C6", "D6", "E6", "F6", "G6", "H6", "A7", "B7", "C7",
          "D7", "E7", "F7", "G7", "H7", "A8", "B8", "C8", "D8", "E8", "F8", "G8", "H8"]

kollaiborjan = False
bonder = True
visanastbast = False

farg = input("Är jag vit eller svart? ").lower().strip()
while farg != "vit" and farg != "svart":
    farg = input("Error. Är jag vit eller svart? ").lower().strip()

ordning = ["t", "h", "l", "d", "k", "l", "h", "t"]

bokstaver = "ABCDEFGHI"  # i måste vara med för annars kan det gå runt baklänges

hall = [-9, -8, -7, -1, 1, 7, 8, 9]

# vilka pjäser som är viktigast
varden = ["b", "l", "h", "t", "d"]
namn = ["bonden", "löparen", "hästen", "tornet", "damen"]

# för att veta om den får göra rokad
gkungv, gkungs = False, False
ga1, gh1, ga8, gh8 = False, False, False, False

# för att veta om den får göra en passant
enpassant = None

prio_ett_drag = []

if farg == "vit":
    e, a = "v", "s"
    prio_ett_drag.append("E2 E3")
    prio_ett_drag.append("F2 F3")
    # prio_ett_drag.append("E2 E4")
else:
    e, a = "s", "v"
    prio_ett_drag.append("E7 E6")
    prio_ett_drag.append("F7 F6")
    # prio_ett_drag.append("E7 E5")

rutor = []

for v in ordning:
    rutor.append(v + "v")
for _ in range(0, 8):
    if bonder:
        rutor.append("bv")
    else:
        rutor.append("inget")

for _ in range(0, 32):
    rutor.append("inget")

for _ in range(0, 8):
    if bonder:
        rutor.append("bs")
    else:
        rutor.append("inget")
for v in ordning:
    rutor.append(v + "s")

# rutor[rutnat.index("F3")] = "dv"


while True:
    if not kollaiborjan:
        break
    test = input("Skriv in en ruta, så skriver jag vad som står på den: ").upper().strip()
    if test == "E":
        exit()
    if test == "B":
        break
    try:
        print(rutor[rutnat.index(test)])
    except IndexError:
        print("Error.")


def vem_star_pa(ruta="A1", scenario=None):
    if scenario is None:
        scenario = rutor
    return scenario[rutnat.index(ruta.upper())]


def gar_ut(ruta1, ruta2):
    plats1 = rutnat.index(ruta1)
    plats2 = rutnat.index(ruta2)
    nubok1 = rutnat[plats1][0]
    nubok2 = rutnat[plats2][0]
    if bokstaver.index(nubok1) + 1 == bokstaver.index(nubok2) or bokstaver.index(nubok1) - 1 == bokstaver.index(
            nubok2) or bokstaver.index(nubok1) == bokstaver.index(nubok2):
        return False
    else:
        return True


def legit_rutor(ruta, scenario=None, kollakung=False):
    if scenario is None:
        scenario = rutor.copy()
    ruta = ruta.upper()
    plats = rutnat.index(ruta)

    lr = ""
    vem = vem_star_pa(ruta, scenario)
    eh = vem[1]

    def uppochnert(ganger=1):
        nonlocal lr
        for numh in range(1, 8):
            plus = 8 * numh * ganger
            if plats + plus < 0:
                break
            if plats + plus > 63:
                break
            if scenario[plats + plus][1] == "n" or scenario[plats + plus][1] != eh:
                lr += rutnat[plats + plus] + ","
                if scenario[plats + plus][0] != "i":
                    break
            else:
                break

    def hogerochvanstert(ganger=1):
        nonlocal lr
        forra = ruta
        for plus in range(1, 8):
            plus *= ganger
            if plats + plus < 0:
                break
            if plats + plus > 63:
                break
            if gar_ut(forra, rutnat[plats + plus]):
                break
            forra = rutnat[plats + plus]
            if scenario[plats + plus][1] == "n" or scenario[plats + plus][1] != eh:
                lr += rutnat[plats + plus] + ","
                if scenario[plats + plus][0] != "i":
                    break
            else:
                break

    def uppochnerl(ganger=1):
        nonlocal lr
        forra = ruta
        for numh in range(1, 8):
            plus = 7 * numh * ganger
            if plats + plus < 0:
                break
            if plats + plus > 63:
                break
            if gar_ut(forra, rutnat[plats + plus]):
                break
            forra = rutnat[plats + plus]
            if scenario[plats + plus][1] == "n" or scenario[plats + plus][1] != eh:
                lr += rutnat[plats + plus] + ","
                if scenario[plats + plus][0] != "i":
                    break
            else:
                break

    def hogerochvansterl(ganger=1):
        nonlocal lr
        forra = ruta
        for numh in range(1, 8):
            plus = 9 * numh * ganger
            if plats + plus < 0:
                break
            if plats + plus > 63:
                break
            if gar_ut(forra, rutnat[plats + plus]):
                break
            forra = rutnat[plats + plus]
            if scenario[plats + plus][1] == "n" or scenario[plats + plus][1] != eh:
                lr += rutnat[plats + plus] + ","
                if scenario[plats + plus][0] != "i":
                    break
            else:
                break

    if vem[0] == "t":
        uppochnert(1)
        uppochnert(-1)

        hogerochvanstert(1)
        hogerochvanstert(-1)

    if vem[0] == "l":
        uppochnerl(1)
        uppochnerl(-1)

        hogerochvansterl(1)
        hogerochvansterl(-1)

    if vem[0] == "h":
        alternativ = [17, 15, 10, 6, -6, -10, -15, -17]
        utforning = [(+8, +9), (+8, +7), (+1, +9), (-1, +7), (+1, -7), (-1, -9), (-8, -7), (-8, -9)]

        fel = []
        for vh in alternativ:
            if plats + vh < 0 or plats + vh > 63:
                fel.append(vh)
            elif scenario[plats + vh][1] == eh:
                fel.append(vh)

        for vh in fel:
            utforning.pop(alternativ.index(vh))
            alternativ.pop(alternativ.index(vh))

        fel = []
        num = 0
        for vh in utforning:
            nu = plats
            for v2h in vh:
                try:
                    if gar_ut(rutnat[nu], rutnat[nu + v2h]):
                        fel.append(alternativ[num])
                except IndexError:
                    fel.append(alternativ[num])
                nu += v2h
            num += 1
        for vh in fel:
            utforning.pop(alternativ.index(vh))
            alternativ.pop(alternativ.index(vh))

        for vh in alternativ:
            lr += rutnat[plats + vh] + ","

    if vem[0] == "d":
        uppochnert(1)
        uppochnert(-1)

        hogerochvanstert(1)
        hogerochvanstert(-1)

        uppochnerl(1)
        uppochnerl(-1)

        hogerochvansterl(1)
        hogerochvansterl(-1)

    if vem[0] == "b":
        if eh == "v":
            gangerh = 1
            ah, forstrut = "s", "2"
        else:
            gangerh = -1
            ah, forstrut = "v", "7"
        if len(scenario) > plats + 8 * gangerh > -1:
            if scenario[plats + 8 * gangerh] == "inget":
                lr += rutnat[plats + 8 * gangerh] + ","
                if ruta[1] == forstrut and scenario[plats + 16 * gangerh] == "inget":
                    lr += rutnat[plats + 16 * gangerh] + ","
        if len(scenario) > plats + 7 * gangerh > -1:
            if (scenario[plats + 7 * gangerh][1] == ah or rutnat[plats + 7 * gangerh] == enpassant) \
                    and not gar_ut(rutnat[plats], rutnat[plats + 7 * gangerh]):
                lr += rutnat[plats + 7 * gangerh] + ","

        if len(scenario) > plats + 9 * gangerh > -1:
            if (scenario[plats + 9 * gangerh][1] == ah or rutnat[plats + 9 * gangerh] == enpassant) \
                    and not gar_ut(rutnat[plats], rutnat[plats + 9 * gangerh]):
                lr += rutnat[plats + 9 * gangerh] + ","

    if kollakung:
        if vem[0] == "k":
            alternativ = [-9, -8, -7, -1, 1, 7, 8, 9]

            fel = []
            for vh in alternativ:
                if plats + vh < 0 or plats + vh > 63:
                    fel.append(vh)
            for vh in fel:
                alternativ.pop(alternativ.index(vh))

            fel = []
            for vh in alternativ:
                if gar_ut(rutnat[plats], rutnat[plats + vh]):
                    fel.append(vh)
            for vh in fel:
                alternativ.pop(alternativ.index(vh))

            fel = []
            for vh in alternativ:
                if scenario[plats + vh][1] == eh:
                    fel.append(vh)
            for vh in fel:
                alternativ.pop(alternativ.index(vh))

            fel = []
            for vh in alternativ:
                for v2h in range(0, 64):
                    if vem_star_pa(rutnat[v2h])[1] != "n" and vem_star_pa(rutnat[v2h])[1] != eh:
                        copylist = scenario.copy()
                        copylist[plats], copylist[plats + vh] = "inget", "k" + eh
                        if legit_rutor(rutnat[v2h], copylist).split(",").__contains__(rutnat[plats + vh]):
                            fel.append(vh)
                            break

            for vh in fel:
                alternativ.pop(alternativ.index(vh))

            if eh == "v":
                frad = 1
            else:
                frad = 8
            if not i_schack(scenario, eh)[0]:
                if not globals()["gkung" + eh] and not globals()["ga" + str(frad)]:
                    if vem_star_pa("B" + str(frad)) == "inget" and vem_star_pa("C" + str(frad)) == "inget" and \
                            vem_star_pa("D" + str(frad)) == "inget":
                        lr += "C" + str(frad) + ","
                if not globals()["gkung" + eh] and not globals()["gh" + str(frad)]:
                    if vem_star_pa("F" + str(frad)) == "inget" and vem_star_pa("G" + str(frad)) == "inget":
                        lr += "G" + str(frad) + ","

            for vh in alternativ:
                lr += rutnat[plats + vh] + ","

    lr = lr[:-1]
    return lr


def i_schack(scenario=None, lag=e):
    if scenario is None:
        scenario = rutor.copy()
    kungruta = rutnat[scenario.index("k" + lag)]

    schackh = False
    vem_schackar = []
    num = 0
    for vh in scenario:
        if vh[1] != "n" and vh[1] != lag and vh[0] != "k":
            lr = legit_rutor(rutnat[num], scenario)
            if lr.split(",").__contains__(kungruta):
                schackh = True
                vem_schackar.append(rutnat[num])
        num += 1
    return schackh, kungruta, vem_schackar


def kan_bli_tagen(ruta, scenario):
    f = scenario[rutnat.index(ruta)][1]
    numh = 0
    ja, vem = False, None
    for vh in scenario:
        if vh[1] != f and vh[1] != "n":
            g = legit_rutor(rutnat[numh], scenario)
            if g.split(",").__contains__(ruta):
                ja = True
                vem = rutnat[numh]
                break
        numh += 1
    return ja, vem


def basta_draget():
    global rutor, schack
    schackad = i_schack()
    if schackad[0]:
        print("\nOjojoj jag är schackad.\n")
        kan_ta = []
        if len(schackad[2]) == 1:
            num = 0
            for vh in rutor:
                if vh[1] == e and vh[0] != "k":
                    if legit_rutor(rutnat[num]).split(",").__contains__(schackad[2][0]):
                        kan_ta.append(rutnat[num])
                num += 1
            if kan_ta:
                allaplaneradedrag.append((random.choice(kan_ta) + " " + schackad[2][0], 10))
        alternativ = legit_rutor(schackad[1], kollakung=True).split(",")
        if alternativ == [""]:
            alternativ = []
        if not alternativ and not kan_ta:
            noddrag = ""
            numh = 0
            for vh in rutor:
                if vh[1] == e:
                    for v2h in legit_rutor(rutnat[numh]).split(","):
                        if v2h:
                            kanskeejschacklista = rutor.copy()
                            kanskeejschacklista[rutnat.index(v2h)] = rutor[numh]
                            kanskeejschacklista[numh] = "inget"
                            if not i_schack(kanskeejschacklista)[0]:
                                noddrag = rutnat[numh] + " " + v2h
                                break
                numh += 1
            if not noddrag:
                input("OJOJOJOJ NEEEEJ! Du vann. Det är schack matt.")
                exit()
            allaplaneradedrag.append((noddrag, 11))
        if alternativ:
            allaplaneradedrag.append((schackad[1] + " " + random.choice(alternativ), 9))

    else:
        pjaser = []
        num = 0
        for vh in rutor:
            if vh[1] == e:
                pjaser.append(rutnat[num])
            num += 1

        num = 0
        fel = []
        for vh in pjaser:
            if not legit_rutor(vh):
                fel.append(num)
            num += 1
        fel = sorted(fel, reverse=True)
        for num in fel:
            pjaser.pop(num)

        # här väljer den en random pjäs och en random gång, ifall programmet senare inte hittar nåt vettigt att göra
        pjas = random.choice(pjaser)
        alternativ = legit_rutor(pjas).split(",")
        val = random.choice(alternativ)

        # här kollar den så att den inte går i en position där den kan tas, men bara 1000 gånger, sen ger den upp
        copy = rutor.copy()
        copy[rutnat.index(val)] = rutor[rutnat.index(pjas)]
        copy[rutnat.index(pjas)] = "inget"
        numh = 0
        while kan_bli_tagen(val, copy)[0]:
            pjas = random.choice(pjaser)
            alternativ = legit_rutor(pjas).split(",")
            val = random.choice(alternativ)
            copy = rutor.copy()
            copy[rutnat.index(val)] = rutor[rutnat.index(pjas)]
            copy[rutnat.index(pjas)] = "inget"
            numh += 1
            if numh > 1000:
                break

        allaplaneradedrag.append((pjas + " " + val, 0))

        # här kollar den om någon av dess pjäser är hotade
        undvikmojligheter = []
        for p in pjaser:
            if kan_bli_tagen(p, rutor)[0]:
                print(random.choice(["Jaså", "Jaha", "Mhm"]) + ", " + namn[varden.index(vem_star_pa(p)[0])] +
                      " som står på " + p + " är lite hotad!")
                pjas = p
                alternativ = legit_rutor(pjas).split(",")
                val = random.choice(alternativ)

                # här kollar den så att den inte går i en position där den kan tas, men bara 1000 gånger, sen ger den upp
                copy = rutor.copy()
                copy[rutnat.index(val)] = rutor[rutnat.index(pjas)]
                copy[rutnat.index(pjas)] = "inget"
                numh = 0
                fail = False
                while kan_bli_tagen(val, copy)[0]:
                    alternativ = legit_rutor(pjas).split(",")
                    val = random.choice(alternativ)
                    copy = rutor.copy()
                    copy[rutnat.index(val)] = rutor[rutnat.index(pjas)]
                    copy[rutnat.index(pjas)] = "inget"
                    numh += 1
                    if numh > 1000:
                        fail = True
                        break

                if not fail:
                    undvikmojligheter.append((p, val, varden.index(vem_star_pa(p)[0])))

        basta = -1
        bd = ""
        for vh in undvikmojligheter:
            if vh[2] > basta:
                basta = vh[2]
                bd = vh[0] + " " + vh[1]

        if bd:
            allaplaneradedrag.append((bd, 3 + basta))

        # här kollar den om den kan ta någon av de andra pjäserna
        tamojligheter = []
        for vh in pjaser:
            for v2h in legit_rutor(vh, kollakung=True).split(","):
                if vem_star_pa(v2h)[1] == a:
                    copy = rutor.copy()
                    copy[rutnat.index(v2h)] = rutor[rutnat.index(vh)]
                    copy[rutnat.index(vh)] = "inget"
                    y = kan_bli_tagen(v2h, copy)
                    if not y[0] or varden.index(vem_star_pa(vh)[0]) <= varden.index(vem_star_pa(v2h)[0]):
                        tamojligheter.append((vh + " " + v2h, vem_star_pa(v2h)))
        basta = ""
        bd = ""
        for vh in tamojligheter:
            if not basta:
                basta = vh[1][0]
                bd = vh[0]
            elif varden.index(vh[1][0]) > varden.index(basta):
                basta = vh[1][0]
                bd = vh[0]
        if basta:
            allaplaneradedrag.append((bd, 4 + varden.index(basta)))

        # här kollar den om den kan schacka den andra
        num, motkungruta = 0, ""
        for vh in rutor:
            if vh[0] == "k" and vh[1] != e:
                motkungruta = rutnat[num]
            num += 1

        schackmojligheter = []
        for vh in pjaser:
            for testh in legit_rutor(vh, kollakung=True).split(","):
                kopy = rutor.copy()
                kopy[rutnat.index(testh)] = rutor[rutnat.index(vh)]
                kopy[rutnat.index(vh)] = "inget"
                lr = legit_rutor(testh, kopy)
                if lr.__contains__(motkungruta):
                    y = kan_bli_tagen(testh, kopy)
                    if not y[0]:
                        schackmojligheter.append(vh + " " + testh)

        if schackmojligheter:
            sm = random.choice(schackmojligheter)
            schack = (True, sm)
            allaplaneradedrag.append((sm, 5))


def fixa_den_andras_drag(d):
    global gh1, gh8, ga1, ga8, enpassant
    if d.lower().__contains__("lika"):
        print("Nej.")
        while d.lower().__contains__("lika"):
            d = input("Skriv in mostståndarens drag: ")
    while True:
        try:
            dragdata = d.split(" ")
            fran, till = dragdata[0], dragdata[1]
            try:
                special = dragdata[2]
            except IndexError:
                special = None
            fran, till = fran.upper(), till.upper()
            if rutnat.__contains__(fran) and rutnat.__contains__(till):
                if legit_rutor(fran, kollakung=True).split(",").__contains__(till):
                    break
                else:
                    d = input("Dit får den inte gå. Skriv in mostståndarens drag: ")
                    if d.lower().__contains__("jo"):
                        break
            else:
                d = input("De rutorna finns inte. Skriv in mostståndarens drag: ")
        except (ValueError, IndexError):
            d = input("Error. Skriv in mostståndarens drag: ")
    rutor[rutnat.index(till)] = rutor[rutnat.index(fran)]
    rutor[rutnat.index(fran)] = "inget"

    if vem_star_pa(till)[0] == "b":
        if vem_star_pa(till)[1] == "v":
            plus = -8
        else:
            plus = 8
        if till == enpassant:
            rutor[rutnat.index(enpassant) + plus] = "inget"
    enpassant = None
    if vem_star_pa(till)[0] == "b":
        if vem_star_pa(till)[1] == "v":
            plus = -1
        else:
            plus = 1
        if abs(int(fran[1]) - int(till[1])) == 2:
            enpassant = till[0] + str(int(till[1]) + plus)

    if vem_star_pa(till)[0] == "k":
        globals()["gkung" + vem_star_pa(till)[1]] = True
        if bokstaver.index(fran[0]) - bokstaver.index(till[0]) == 2:
            if vem_star_pa(till)[1] == "v":
                frad = 1
            else:
                frad = 8
            if till == "C" + str(frad):
                rutor[rutnat.index("D" + str(frad))] = vem_star_pa("A" + str(frad))
                rutor[rutnat.index("A" + str(frad))] = "inget"
        if bokstaver.index(fran[0]) - bokstaver.index(till[0]) == -2:
            if vem_star_pa(till)[1] == "v":
                frad = 1
            else:
                frad = 8
            if till == "G" + str(frad):
                rutor[rutnat.index("F" + str(frad))] = vem_star_pa("H" + str(frad))
                rutor[rutnat.index("H" + str(frad))] = "inget"

    if till == "h8" and vem_star_pa(till)[0] == "t":
        gh8 = True
    if till == "h1" and vem_star_pa(till)[0] == "t":
        gh1 = True
    if till == "a8" and vem_star_pa(till)[0] == "t":
        ga8 = True
    if till == "a1" and vem_star_pa(till)[0] == "t":
        ga1 = True

    if special is not None and rutor[rutnat.index(till)][0] == "b":
        rutor[rutnat.index(till)] = special.lower()[0] + rutor[rutnat.index(till)][1]
    if rutor[rutnat.index("H8")] != "ts":
        gh8 = True
    if rutor[rutnat.index("H1")] != "ts":
        gh1 = True
    if rutor[rutnat.index("A8")] != "tv":
        ga8 = True
    if rutor[rutnat.index("A1")] != "tv":
        ga1 = True


def fixa_eget_drag(d):
    global draget, schackmatt, gh1, gh8, ga1, ga8, enpassant
    fran, till = d.split(" ")
    rutor[rutnat.index(till)] = rutor[rutnat.index(fran)]
    rutor[rutnat.index(fran)] = "inget"

    if vem_star_pa(till)[0] == "b":
        if vem_star_pa(till)[1] == "v":
            plus = -8
        else:
            plus = 8
        if till == enpassant:
            rutor[rutnat.index(enpassant) + plus] = "inget"
    enpassant = None
    if vem_star_pa(till)[0] == "b":
        if vem_star_pa(till)[1] == "v":
            plus = -1
        else:
            plus = 1
        if abs(int(fran[1]) - int(till[1])) == 2:
            enpassant = till[0] + str(int(till[1]) + plus)

    if vem_star_pa(till)[0] == "k":
        globals()["gkung" + vem_star_pa(till)[1]] = True
        if bokstaver.index(fran[0]) - bokstaver.index(till[0]) == 2:
            if vem_star_pa(till)[1] == "v":
                frad = 1
            else:
                frad = 8
            if till == "C" + str(frad):
                rutor[rutnat.index("D" + str(frad))] = vem_star_pa("A" + str(frad))
                rutor[rutnat.index("A" + str(frad))] = "inget"
        if bokstaver.index(fran[0]) - bokstaver.index(till[0]) == -2:
            if vem_star_pa(till)[1] == "v":
                frad = 1
            else:
                frad = 8
            if till == "G" + str(frad):
                rutor[rutnat.index("F" + str(frad))] = vem_star_pa("H" + str(frad))
                rutor[rutnat.index("H" + str(frad))] = "inget"
    if till == "h8" and vem_star_pa(till)[0] == "t":
        gh8 = True
    if till == "h1" and vem_star_pa(till)[0] == "t":
        gh1 = True
    if till == "a8" and vem_star_pa(till)[0] == "t":
        ga8 = True
    if till == "a1" and vem_star_pa(till)[0] == "t":
        ga1 = True

    if e == "v":
        rad = 8
    else:
        rad = 1
    if rutor[rutnat.index(till)][0] == "b" and int(till[1]) == rad:
        rutor[rutnat.index(till)] = "d" + e
        draget += " dam"

    if i_schack(lag=a)[0]:
        schackmatt = True
        numh = 0
        for vh in rutor:
            if vh[1] != "n" and vh[1] != e:
                for testh in legit_rutor(rutnat[numh], kollakung=True).split(","):
                    if testh:
                        scen = rutor.copy()
                        scen[rutnat.index(testh)] = vh
                        scen[numh] = "inget"
                        if not i_schack(scen, a)[0]:
                            schackmatt = False
                            break
            numh += 1
    if rutor[rutnat.index("H8")] != "ts":
        gh8 = True
    if rutor[rutnat.index("H1")] != "ts":
        gh1 = True
    if rutor[rutnat.index("A8")] != "tv":
        ga8 = True
    if rutor[rutnat.index("A1")] != "tv":
        ga1 = True


while True:
    if not kollaiborjan:
        break
    test = input("Skriv in en ruta, så skriver jag vart pjäsen på den kan flytta: ").upper().strip()
    if test == "E":
        exit()
    if test == "B":
        break
    print(legit_rutor(test, kollakung=True))

if farg == "svart":
    drag = input("Skriv in motståndarens drag: ")
    fixa_den_andras_drag(drag)

while True:
    schackmatt = False
    schack = (False, None)
    allaplaneradedrag = []
    print("")
    if prio_ett_drag:
        allaplaneradedrag.append((prio_ett_drag.pop(0), 6))
        if not legit_rutor(allaplaneradedrag[0][0].split(" ")[0]).__contains__(allaplaneradedrag[0][0].split(" ")[1]):
            allaplaneradedrag = []
    basta_draget()
    kopia = rutor.copy()
    draget = ""
    hogst = -1000
    nastbast = ""
    for v in allaplaneradedrag:
        if v[1] > hogst:
            nastbast = draget
            draget = v[0]
            hogst = v[1]
    fixa_eget_drag(draget)
    pattrak = 0
    while i_schack()[0]:
        schackmatt = False
        schack = (False, None)
        allaplaneradedrag = []
        rutor = kopia.copy()
        basta_draget()
        draget = ""
        hogst = -1000
        for v in allaplaneradedrag:
            if v[1] > hogst:
                draget = v[0]
                hogst = v[1]
        fixa_eget_drag(draget)
        pattrak += 1
        if pattrak > 5000:
            input("Jag är inte i schack, och jag hittar ingenstans att flytta. Det är patt.")
            exit()
    print(draget)
    if schack[0] and schack[1] == draget:
        print("Schack.")
    if schackmatt:
        input("Jag vann! Det är schack matt! MOHAHAHAHAHA!")
        exit()
    print("")
    if visanastbast and nastbast:
        print("Om jag inte kommit på mitt briljanta drag, så hade jag gjort " + nastbast + ".")
    else:
        fixa_den_andras_drag(input("Skriv in motståndarens drag: "))
