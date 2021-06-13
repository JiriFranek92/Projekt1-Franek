import string as st

import texts as txt


# nastavení vstupních údajů uživatelů
users = {"bob": "123",
         "ann": "pass123",
         "mike": "password123",
         "liz": "pass123"}

DELIM = 20 * "-"

# zeptej se na vstupní údaje
usr = input("username: ")
pwd = input("password: ")
print(DELIM)

# pokud uživatel zadá špatné jméno, nebo heslo skonči a vypiš chybu
if usr not in users or users[usr] != pwd:
    exit("Incorrect username or password!")

# pozdrav uživatele a vypiš počet textů k analýze
print(f"Welcome to the app, {usr}")
print(f"We have {len(txt.TEXTS)} texts to be analyzed.")
print(DELIM)

# zeptej se uživatele, který text si vybral
selection = input(f"Enter a number btw. 1 and {len(txt.TEXTS)} to select: ")
print(DELIM)

# zkontroluj správnost vstupu
# pokud vstup není celé číslo skonči
if not selection.isnumeric():
    exit("Error! Selection must be a (whole) number.")

# ... jinak převeď vstup na integer
selection = int(selection)

# pokud vstup je menší než jedna nebo větší než délka listu s texty skonči
if selection < 1 or selection > len(txt.TEXTS):
    exit(f"Error! Number must be between 1 and {len(txt.TEXTS)}.")

# ... jinak odečti 1 aby jsi získal index
selection -= 1

# vytvoř list slov očištěných od interpunkce a bílých znaků
# rozdělením zvoleného textu podle mezer
word_list = [word.strip(st.whitespace + st.punctuation)
             for word in txt.TEXTS[selection].split()]

# vytvoř prázdný slovník pro uložení výsledků analýzy
text_stats = {"words": 0,          # počet slov
              "titlecase": 0,      # počet slov s prvním velkým písmenem (Slov)
              "uppercase": 0,      # počet slov psaných velkými (SLOV)
              "lowercase": 0,      # počet slov psaných malými (slov)
              "numbers": 0,        # počet čísel
              "number_sum": 0,    # suma čísel
              "word_lengths": {}}  # slovník s četnostmi délek slov

# pro každé slovo v listu ho připočti do statistik pokud splňuje rel. podmínku
for word in word_list:
    text_stats["words"] += 1
    if word.isupper():
        text_stats["uppercase"] += 1
    elif word.istitle():
        text_stats["titlecase"] += 1
    elif word.islower():
        text_stats["lowercase"] += 1
    elif word.isnumeric():
        text_stats["numbers"] += 1
        text_stats["number_sum"] += int(word)
    # ... a připočti délku slova do slovníku "word_lengths"
    text_stats["word_lengths"][len(word)] = \
        text_stats["word_lengths"].get(len(word), 0) + 1

# vypiš statistiky
if text_stats['words'] == 1:
    print(f"There is {text_stats['words']} word in the selected text.")
else:
    print(f"There are {text_stats['words']} words in the selected text.")

for case in ["titlecase", "uppercase", "lowercase"]:
    if text_stats[case] == 1:
        print(f"There is {text_stats[case]} {case} word.")
    else:
        print(f"There are {text_stats[case]} {case} words.")

if text_stats['numbers'] == 1:
    print(f"There is {text_stats['numbers']} numeric string.")
else:
    print(f"There are {text_stats['numbers']} numeric strings.")

if text_stats['number_sum'] > 0:
    print(f"The sum of all the numbers is {text_stats['number_sum']}.")
print(DELIM)

# ------------------------- Tisk grafu ---------------------------------------

# definuj texty v záhlaví
heading_labels = 'LEN'
heading_values = 'OCCURENCES'

# ----- pomocné proměnné pro správné formátování -----
# šířka sloupce popisků
# (co je delší: délka nejdelšího popisku, nebo délka textu záhlaví)
label_col_width = \
    max(max([len(str(key)) for key in text_stats["word_lengths"].keys()]),
        len(heading_labels))
# šířka sloupce hodnot
# (co je delší: délka sloupce + délka textu popisku + mezera
# NEBO délka textu záhlaví)
values_col_width = max(max(text_stats["word_lengths"].values()) +
                       len(str(max(text_stats["word_lengths"].values()))) + 1,
                       len(heading_values))

# tiskni záhlaví
# (margin_label)POPISEK|(margin_value)HODNOTA
margin_label = (label_col_width - len(heading_labels)) * " "
margin_value = ((values_col_width - len(heading_values)) // 2) * " "
print(margin_label + heading_labels + "|" + margin_value + heading_values)

print("-" * (label_col_width + values_col_width + 2))
# tiskni jednotlivé údaje do grafu
# (margin_label)popisek|****** (číslo)
for label, value in sorted(text_stats["word_lengths"].items()):
    margin_label = (label_col_width - len(str(label))) * " "
    print(margin_label + str(label) + "|" + value * "*" + " " + str(value))
