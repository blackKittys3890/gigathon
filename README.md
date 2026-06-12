# Gigathon - Pokemon Spiel

Ein textbasiertes Pokemon-Adventure in Python, bei dem du als Trainer durch eine Welt reist, Pokemon fängst, Arenen besiegst und dich durch die Top 4 kämpfst.

## Spielstart
Du wirst nach folgenden Startparametern gefragt:
- Dein Trainername
- Deine Startposition (x, y) zwischen -100 und 100
- Schwiriegkeitsgrad (1 = leicht, 2 = mittel, 3 = schwer)
- Name deines Rivalen
- Dein Startgeld

## Spielwelt
- Weltgrenzen: **-100 bis 100** in x- uznd y.Richtung
- Deine Position wird nach jedem Schritt aktualisiert
- Bei jedem Schritt passiert ein Zuffallsereigniss

## Kampfsystem
- Du kmäpfst mit deinem ersten Pokemon im Team
- Optionen: Angreifen, Heilen (mit ITems, Fliehen)
- Der Schaden des Gegners skaliert mit dem Schwierigkeitsgrad:
    - Leicht: 0.75-facher Schaden
    - Normal: 1,0-facher Schaden
    - Schwer: 1,5-facher Schaden

## Arenen
Es gibt **8 Arenaleiter**:
1. Rocko
2. Misty
3. Major Bob
4. Erika
5. Koga
6. Sabrina
7. Pyro
8. Giovanni

Nach jedem Arena-Sieg kannst du:
- Pokemon heilen
- Neue Pokemon fangen
- Zur nächsten Arena weitergehen

## Top 4
Nach allen 8 Arenen kämpfst du gegen die Top 4:
1. Lorelei
2. Bruno
3. Agathe
4. Siegfried
5. Dein Rival

## Zufallsereignisse
Dein Kumpel (abhängig von deiner Startposition) beeinflusst die Event-Wahrscheinlichkeiten:

    Trainer:    Bevorzugte Events:
    Rocko       Gefährliche Felder
    Ash         Pokémon fangen
    Misty       Items finden

### Mögliche Events:
- Pokemon finden - Ein wildes Pokemon fangen
- Legendäres Pokemon - Seltenes, starkes Pokemon
- Item finden - Potions für Heilung
- Gefährliches Feld - Alle Pokemon verlieren 10KP

## Geld
- Startgeld wird am Anfang festgelegt
- Geld ändert sich nur durch Ereignisse (nicht durch Bewegung)
- Wenn dein Geld auf 0 fällt, endet das Spiel

## Spielende
Das Spiel endet wenn:
- Du eine Arena oder Top 4 verlierst
- Dir das Geld ausgeht
- Du alle Top 4 (inklusive Rivalen) besiegst -> Champion!

Danach wird ein ausführlicher Abschlussbericht angezeigt mit:
- Endposition
- Verbleibendes Geld
- Zurückgelgte Schritte
- Arenasiege
- Top 4 Siege
- Dein Pokemon-Team
- Gesammeltes Items
- Ereignis-Log

## Neustart
Nach Spielende kannst du mit j (ja) oder n (nein) entscheiden, ob du nochmal spielen möchtest

## Autor
Entwickelt von black_Kittys (Eliah Weichert) im Rahmen der Gigathon-Aufgabe
