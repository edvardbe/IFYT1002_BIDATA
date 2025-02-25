import requests

# Nettadressen til PNG-filen du vil laste ned
#url = "https://www.nuclear-power.com/wp-content/uploads/2021/11/atomic-number-density-atomic-mass-Silver.png"
#url = "https://www.nuclear-power.com/wp-content/uploads/2021/11/atomic-number-density-atomic-mass-Gold.png"
url = "https://www.nuclear-power.com/wp-content/uploads/2021/11/atomic-number-density-atomic-mass-Copper.png"
# Send en GET-forespørsel
response = requests.get(url)

# Sjekk om forespørselen var vellykket (HTTP-statuskode 200)
if response.status_code == 200:
    # Åpne (eller opprett) en fil i binær skrive-modus
    #with open("gold.png", "wb") as f:
    with open("copper.png", "wb") as f:
        f.write(response.content)
    print("Bilde lastet ned!")
else:
    print("Noe gikk galt. HTTP-statuskode:", response.status_code)
