wochentag = input("Wochentag : ")
kalenderwoche = int(input("Kalenderwoche : "))
if wochentag == "Montag":
    # True
    print("Müllabfuhr der schwarzen Tonne")
    if kalenderwoche % 2:
        # True
        print("und Müllabfuhr der gelben Tonne")
else:
    # False
    if wochentag == "Mittwoch":
        # True
        print("Müllabfuhr der blauen Tonne")
    else:
        print("Keine Müllabfuhr")