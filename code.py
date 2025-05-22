import tkinter as tk
from tkinter import ttk
import requests
import pyperclip
import PIL
from PIL import Image, ImageTk

# Die URL des Bildes
image_url = "https://static.wikia.nocookie.net/minecraft_de_gamepedia/images/c/cc/Schleim.png/revision/latest/scale-to-width-down/150?cb=20200403150614.png"

# Speichere das Bild lokal
response = requests.get(image_url)
with open("schleim.png", "wb") as f:
    f.write(response.content)
from PIL import Image

# Lade das Bild mit Pillow
image = Image.open("schleim.png")




# Wörterbuch für Buchstabenübersetzungen in der ersten Sprache
buchstaben_uebersetzungen_ardenvell = {
    "a": "l",
    "b": "i",
    "c": "s",
    "d": "r",
    "e": "k",
    "f": "d",
    "g": "v",
    "h": "w",
    "i": "g",
    "j": "n",
    "k": "z",
    "l": "n",
    "m": "n",
    "n": "x",
    "o": "y",
    "p": "p",
    "q": "",
    "r": "q",
    "s": "b",
    "t": "d",
    "u": "e",
    "v": "t",
    "w": "a",
    "x": "c",
    "y": "c",
    "z": "u",
    # ... (Ihre Übersetzungen für die Ardenvellische Sprache hier)
}



buchstaben_uebersetzungen_sued = {
    'a': 'u',
    'b': 'g',
    'c': 'z',
    'd': 'p',
    'e': 'o',
    'f': 'm',
    'g': 'b',
    'h': 'h',
    'i': 'i',
    'j': 's',
    'k': 'x',
    'l': 'n',
    'm': 'c',
    'n': 'r',
    'o': 'e',
    'p': 'd',
    'q': 'q',
    'r': 'f',
    's': 'm',
    't': 'd',
    'u': 'a',
    'v': 'v',
    'w': 'v',
    'x': 'p',
    'y': 'i',
    'z': 'c',
    'ä': 'ue',
    'ö': 'oe',
    'ü': 'ae',
    'ß': 'ss',
    # ... (Ihre Übersetzungen für die erste Sprache hier)
}

# Wörterbuch für Buchstabenübersetzungen in der zweiten Sprache
buchstaben_uebersetzungen_ost = {
    "a": "i",
    "b": "p",
    "c": "k",
    "d": "t",
    "e": "ä",
    "f": "v",
    "g": "q",
    "h": "h",
    "i": "y",
    "j": "i",
    "k": "c",
    "l": "w",
    "m": "n",
    "n": "m",
    "o": "u",
    "p": "b",
    "q": "g",
    "r": "x",
    "s": "ß",
    "t": "d",
    "u": "o",
    "v": "f",
    "w": "v",
    "x": "ks",
    "y": "ü",
    "z": "ts",
    "ä": "e",
    "ö": "ü",
    "ü": "ö",
    "ß": "skh",
    # ... (Ihre Übersetzungen für die zweite Sprache hier)
}

def uebersetze_buchstabe(buchstabe, sprache):
    if sprache == "Südsleimisch" or sprache == "S":
        uebersetzungen = buchstaben_uebersetzungen_sued
    elif sprache == "Ostsleimisch" or sprache == "O":
        uebersetzungen = buchstaben_uebersetzungen_ost
    elif sprache == "Ardenvellisch" or sprache == "A":
        uebersetzungen = buchstaben_uebersetzungen_ardenvell
    else:
        # Wenn die ausgewählte Sprache nicht erkannt wird, verwende die erste Sprache als Standard
        uebersetzungen = buchstaben_uebersetzungen_sued
    
    return uebersetzungen.get(buchstabe, buchstabe)

def uebersetze_wort(wort, sprache):
    wort = wort.lower()  # Konvertiere das Wort in Kleinbuchstaben, um Groß- und Kleinschreibung zu behandeln
    modifizierte_buchstaben = []
    
    in_klammern = False  # Eine Variable, um zu verfolgen, ob wir uns innerhalb von Klammern befinden
    inhalt_klammern = []  # Eine Liste, um den Inhalt der Klammern zu speichern
    
    for buchstabe in wort:
        if buchstabe == '(':
            in_klammern = True
        elif buchstabe == ')':
            in_klammern = False
            # Füge den Inhalt der Klammern zur Ausgabe hinzu
            modifizierte_buchstaben.extend(inhalt_klammern)
            # Lösche den Inhalt der Klammern
            inhalt_klammern = []
        elif in_klammern:
            inhalt_klammern.append(buchstabe)  # Füge den Buchstaben zum Inhalt der Klammern hinzu
        else:
            modifizierte_buchstaben.append(uebersetze_buchstabe(buchstabe, sprache))
    
    return ''.join(modifizierte_buchstaben)

def ardenvell():
    global sprache
    sprache = "Ardenvellisch"
    label.config(text="Ardenvellisch ist ausgewählt.")

   

    



  
    
def syso():
    global sprache
    sprache = "Südsleimisch"
    label.config(text="Südsleimisch ist ausgewählt.")

def o():
    global sprache
    sprache = "Ostsleimisch"
    label.config(text="Ostsleimisch ist ausgewählt.")


def uebersetzen():
    
    eingabe = eingabe_entry.get()
    uebersetzte_text = uebersetze_wort(eingabe, sprache)
    ausgabe_entry.delete(0, "end")  # Löschen Sie den aktuellen Text im Entry
    ausgabe_entry.insert(0, uebersetzte_text)  # Fügen Sie den übersetzten Text ein



def beenden():
    start.destroy()

start = tk.Tk()
# Bildgröße auf Icon-Standard anpassen (z. B. 32x32)
img = image.resize((32, 32), Image.LANCZOS)

# In Tkinter-kompatibles Objekt konvertieren
tk_icon = ImageTk.PhotoImage(img)
start.title("Sleim 11")
start.geometry("1300x800")
start.iconphoto(True, tk_icon)



label = tk.Label(start, text="Dies ist ein Übersetzungsprogramm. Klammern in Ihrer Eingabe bleiben unverändert, und der Inhalt von Klammern wird nicht übersetzt.", bg="green")
label.pack()

sued = ttk.Button(start, text="Südsleimisch", padding="20", command=syso)
sued.pack(fill="x")

ost = ttk.Button(start, text="Ostsleimisch", padding="20", command=o)
ost.pack(fill="x")

ard = ttk.Button(start, text="Gainaxische Kodierung", padding="20", command=ardenvell)
ard.pack(fill="x")





eingabe_entry = tk.Entry(start, width=50, text="Übersetzung")
eingabe_entry.pack()
eingabe_entry.insert(0, "Gib hier das zu übersetzene ein:")

uebersetzen_button = ttk.Button(start, text="Übersetzen", command=uebersetzen)
uebersetzen_button.pack()


ausgabe_entry = tk.Entry(start, width=50)
ausgabe_entry.pack()

beenden_button = ttk.Button(start, text="Beenden", padding="10", command=beenden)
beenden_button.pack()




tippsuedueberschrift = tk.Label(start, text="Dies gilt für das Südsleimische:")
tippsuedueberschrift.pack()
tippsuedverb = tk.Label(start, text="Verben:", bg="red")
tippsuedverb.pack()
tippsuedpraesens = tk.Label(start, text="Endungen des Präsens: 1.Sg: uha  2.Sg: usa  3.Sg: uta   1.Pl: umusa  2.Pl: utis  3.Pl: unta")
tippsuedpraesens.pack(fill="x")
tippsuedpraeteritum = tk.Label(start, text="Endungen des Präteritums: 1.Sg: iuha  2.Sg: iusa  3.Sg: iuta   1.Pl: iumusa  2.Pl: iutisa  3.Pl: iunta")
tippsuedpraeteritum.pack(fill="x")
tippsuedperfekt = tk.Label(start, text="Endungen des Perfekts: 1.Sg: auha  2.Sg: ausa  3.Sg: auta   1.Pl: aumusa  2.Pl: autisa  3.Pl: aunta")
tippsuedperfekt.pack(fill="x")
tippsuedfutur1 = tk.Label(start, text="Endungen vom ersten Futur: 1.Sg: euha  2.Sg: eusa  3.Sg: euta   1.Pl: eumusa  2.Pl: eutis  3.Pl: eunta")
tippsuedfutur1.pack(fill="x")
tippsuedfutur2 = tk.Label(start, text="Futur zwei: Hier musst du an das Verb im Futur 1 nur das Wort cada ranhängen")
tippsuedfutur2.pack(fill="x")
tippsuedplusquamperfekt = tk.Label(start, text="Endungen für das Plusquamperfekt: 1.Sg: ohuha  2.Sg: ohusa  3.Sg: ohuta   1.Pl: ohumusa  2.Pl: ohutis  3.Pl: ohunta")
tippsuedplusquamperfekt.pack(fill="x")
tippsuedimp = tk.Label(start, text="Endungen für den Imperativ: Sg: a Pl: teha")
tippsuedimp.pack(fill="x")
tippsuedsubstantiv = tk.Label(start, text="Substantive:", bg="blue")
tippsuedsubstantiv.pack()
tippsuedsubstantivsingular = tk.Label(start, text="Sg: Nom: o Gen: io Dat: o Akk: umo Abl: o Vok: eo")
tippsuedsubstantivsingular.pack()
tippsuedsubstantivplural = tk.Label(start, text="Pl: Nom: io Gen: orumo Dat: iso Akk: oso Abl: iso Vok: io")
tippsuedsubstantivplural.pack()
tippsuedadjektivueberschrift = tk.Label(start, text="Adjektive, Personalpronomen, Adverben, Konjunktionen und Possesivpronomen:", bg="green")
tippsuedadjektivueberschrift.pack()
adjektiv = tk.Label(start, text="Adjektiv: Hänge hierzu die Endung des beschriebenem Substantives an das Adjektiv und hänge daran ein i")
adjektiv.pack()
adjst = tk.Label(start, text="Normal: i, Vergleich: ui, Am Meisten: ahui")
adjst.pack()
possesiv = tk.Label(start, text="Adverben, Konjunktionen und Possesivpronomen: Hänge hier ein i dran")
possesiv.pack()
personal = tk.Label(start, text="Personalpronomen haben die Endung des Wortes auf das sie siech beziehen")
personal.pack()





tippleere = tk.Label(start, text=" ")
tippleere.pack()

tippoueberschrift = tk.Label(start, text="Dies gilt nur für das Ostsleimische:")
tippoueberschrift.pack()

tippo = tk.Label(start, text="Hier musst du nichts machen!")
tippo.pack()


tippkl = tk.Label(start, text="!!!Alle Endungen und Namen müssen in Klammern geschrieben werden!!!",bg="red")
tippkl.pack()

addueberschrift = tk.Label(start, text="anzeige:")
addueberschrift.pack()

add =tk.Label(start, text="SPIELEN SIE THEO TOWN JETZT KOSTENLOS AUF DEM HANDY", bg="red")
add.pack()



sprache = "Südsleimisch"  # Starten Sie mit Südsleimisch als Standard




start.mainloop()



#To-Do-Liste:
#Übersetzung Markierbar machen für Copy-Paste Funktion
#Paralele Website laufen lassen???
#Schrift
#Ardenvellisch
#Pogramm schöner machen

#Diese liste muss abgearbeitet werden!!!!!!!!!!!!!!!!!!!!!!
