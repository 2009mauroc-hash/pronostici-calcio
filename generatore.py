import os
import json
import urllib.request
from groq import Groq

# 1. Inizializza l'IA con la chiave gratuita
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

# 2. Struttura dati base (puoi automatizzare lo scraping o aggiornare le partite)
partite = [
    {
        "partita": "Inter vs Milan",
        "stats": "Inter 1° in classifica, Milan 4°. Inter con 2.1 xG medi, Milan 1.5 xG.",
        "fattore_umano": "Derby di altissima tensione. Il Milan viene da una sconfitta pesante e l'allenatore rischia l'esonero, mentre la tifoseria dell'Inter è in contestazione per i prezzi dei biglietti."
    }
]

risultati_pronostici = []

for item in partite:
    prompt = f"""
    Sei un analista calcistico cinico, esperto ed emotivo.
    Analizza questo match: {item['partita']}.
    Dati Statistici: {item['stats']}
    Fattore Umano e Notizie dell'Ultimo Minuto: {item['fattore_umano']}

    Crea una scheda pronostico super dettagliata in formato JSON o testo chiaro con:
    1. Analisi Tattica
    2. Impatto del Fattore Umano/Psicologico (perché la palla è rotonda)
    3. Il Verdetto / Pronostico
    """

    response = client.chat.completions.create(
        model="llama3-8b-8192",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )
    
    testo_generato = response.choices[0].message.content
    risultati_pronostici.append({
        "partita": item['partita'],
        "analisi": testo_generato
    })

# 3. Salva i risultati nel file dati.json che il sito mostrerà agli utenti
with open("dati.json", "w", encoding="utf-8") as f:
    json.dump(risultati_pronostici, f, ensure_ascii=False, indent=2)

print("Pronostici generati con successo!")
