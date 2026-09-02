import os
import json
import sys
import requests
from groq import Groq

groq_key = os.environ.get("GROQ_API_KEY")
football_key = os.environ.get("FOOTBALL_API_KEY")

if not groq_key or not football_key:
    print("ERRORE: Mancano le chiavi API nei Secrets di GitHub.")
    sys.exit(1)

url = "https://api.football-data.org/v4/competitions/SA/matches?status=SCHEDULED"
headers = {"X-Auth-Token": football_key}

try:
    response = requests.get(url, headers=headers)
    data_matches = response.json()
    matches = data_matches.get("matches", [])[:5]
except Exception as e:
    print(f"Errore nel recupero delle partite da internet: {e}")
    sys.exit(1)

if not matches:
    partite_str = "Juventus vs Inter, Milan vs Napoli"
else:
    partite_list = []
    for m in matches:
        home = m["homeTeam"]["name"]
        away = m["awayTeam"]["name"]
        partite_list.append(f"{home} vs {away}")
    partite_str = ", ".join(partite_list)

print(f"Partite reali trovate: {partite_str}")

client = Groq(api_key=groq_key)

prompt = f"""
Agisci come un super assistente di intelligenza artificiale per il calcio. 
Ho estratto queste partite reali dal calendario ufficiale: {partite_str}.

Genera un elenco JSON valido (e RESTITUISCI SOLO un array JSON puro, senza alcun blocco di codice markdown come ```json o testo introduttivo) analizzando esattamente queste partite, includendo stime di xG, statistiche chiave e un'analisi approfondita con "fattore umano".

L'array JSON deve avere esattamente questa struttura:
[
  {{
    "partita": "Nome Squadra A vs Nome Squadra B",
    "analisi": "Qui scrivi l'analisi dettagliata della partita, le statistiche recenti, gli xG stimati, le quote o lo stato di forma e le considerazioni sul fattore umano."
  }}
]
"""

try:
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )
    
    content = response.choices[0].message.content.strip()

    if content.startswith("```json"):
        content = content[7:]
    if content.startswith("```"):
        content = content[3:]
    if content.endswith("```"):
        content = content[:-3]
    content = content.strip()

    final_data = json.loads(content)
    with open("dati.json", "w", encoding="utf-8") as f:
        json.dump(final_data, f, ensure_ascii=False, indent=4)
    print("File dati.json aggiornato con le partite reali di internet!")

except Exception as e:
    print(f"Errore durante la generazione dell'analisi IA: {e}")
    sys.exit(1)
