import os
import json
from groq import Groq

client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

prompt = """
Agisci come un super assistente di intelligenza artificiale per il calcio. Genera un elenco JSON valido (e RESTITUISCI SOLO un array JSON puro, senza alcun blocco di codice markdown come ```json o testo introduttivo) delle principali partite di calcio in programma oggi o per il prossimo turno ufficiale, includendo stime di xG, statistiche chiave e un'analisi approfondita con "fattore umano".

L'array JSON deve avere esattamente questa struttura:
[
  {
    "partita": "Nome Squadra A vs Nome Squadra B",
    "analisi": "Qui scrivi l'analisi dettagliata della partita, le statistiche recenti, gli xG stimati, le quote o lo stato di forma e le considerazioni sul fattore umano."
  }
]
"""

response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
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

data = json.loads(content)
with open("dati.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)
