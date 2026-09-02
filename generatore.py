<!DOCTYPE html>
<html lang="it">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Pronostici Calcio IA + Fattore Umano</title>
    <style>
        body { font-family: Arial, sans-serif; background-color: #121212; color: #fff; padding: 20px; max-width: 800px; margin: auto; }
        .card { background-color: #1e1e1e; border-radius: 8px; padding: 20px; margin-bottom: 20px; border-left: 4px solid #00ff88; box-shadow: 0 4px 6px rgba(0,0,0,0.3); }
        h1 { color: #00ff88; text-align: center; margin-bottom: 30px; }
        h2 { margin-top: 0; color: #ffffff; border-bottom: 1px solid #333; padding-bottom: 10px; }
        p { white-space: pre-line; line-height: 1.6; color: #d1d5db; }
        .loading { text-align: center; color: #888; font-style: italic; }
    </style>
</head>
<body>
    <h1>⚽ Pronostici & Pagelle IA (Fattore Umano Included)</h1>
    <div id="contenuto" class="loading">Caricamento ultimi aggiornamenti dal web...</div>

    <script>
        fetch('dati.json?t=' + new Date().getTime())
            .then(res => res.json())
            .then(data => {
                let html = '';
                data.forEach(item => {
                    html += `<div class="card">
                        <h2>${item.partita}</h2>
                        <p>${item.analisi}</p>
                    </div>`;
                });
                document.getElementById('contenuto').innerHTML = html;
            })
            .catch(err => {
                document.getElementById('contenuto').innerHTML = "<p>Nessun pronostico disponibile al momento. L'IA sta elaborando i dati live.</p>";
            });
    </script>
</body>
</html>
