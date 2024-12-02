# Část 1
import json
import requests

ico = input("Zadej IČO subjektu: ")
response = requests.get(f"https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/{ico}")
response_json = response.json()
with open("ico.json", "w", encoding="utf-8") as file:
    json.dump(response_json, file, indent=4)

print(response_json["obchodniJmeno"])
print(response_json["sidlo"]["textovaAdresa"])


# Část 2
import json
import requests

nazev = input("Zadej název subjektu: ").strip()

headers = {
    "accept": "application/json",
    "Content-Type": "application/json",
}

data = json.dumps({"obchodniJmeno": nazev})

response = requests.post("https://ares.gov.cz/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/vyhledat", headers=headers, data=data)

response_json = response.json()
with open("nazev.json", "w", encoding="utf-8") as file:
    json.dump(response_json, file, indent=4)

print(f"Nalezeno subjektů: {response_json["pocetCelkem"]}")
for item in response_json["ekonomickeSubjekty"]:
    print(f"{item["obchodniJmeno"]}, {item["ico"]}")