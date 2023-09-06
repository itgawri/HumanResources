assessment_score = 85
location = "Poland"
location2 = "Canada"
location3 = "US"

if location3 == "US" or location2 == "Canada" and assessment_score >= 75:
  print(f"Your assessment score is {assessment_score}/100! You're hired!")
elif location == "US" and location != "Canada" and assessment_score >= 75:
  print(f"Apologies, you are based in {location} but this role requires you to be based in the US/Canada. Would you be interested in another role?")
elif location == "Poland" and assessment_score >= 75:
  print("Jest dobrze")
else:
  print(f"Thank you for your interest, we regret to inform you that we will not be moving forward with your application.")

# PL------------------------------------------------------------------------------------

wynik_oceny = 85
miejsce = "Polska"
miejsce2 = "Kanada"
miejsce3 = "USA"

if miejsce3 == "USA" or miejsce2 == "Kanada" and wynik_oceny >= 75:
  print(f"Twój wynik oceny to {wynik_oceny}/100! Zostałeś przyjęty!")
elif miejsce == "USA" and miejsce != "Kanada" and wynik_oceny >= 75:
  print(f"Przepraszamy, jesteś zarejestrowany w {miejsce}, ale to stanowisko wymaga bycia zarejestrowanym w USA/Kanadzie. Czy jesteś zainteresowany inną rolą?")
elif miejsce == "Polska" and wynik_oceny >= 75:
  print("Jest dobrze")
else:
  print(f"Dziękujemy za zainteresowanie, niestety informujemy, że nie będziemy kontynuować Twojej aplikacji.")
