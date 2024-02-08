# Steuerung

Wir hatten bereits etwas das Event-System kennengelernt (zum Schliessen des Programms).
Nun wollen wir unsere Spielfigur umherfahren lassen.

## Pfeiltasten
Mit den Pfeiltasten können wir unser Rechteck umherfahren lassen.
Lade `main.py` und ergänze beim TODO:
``` python
    # TODO: Pfeiltaste nach Rechts
    if keys[pygame.K_RIGHT]:
        player_x += speed
```

Ergänze den Code mit den übrigen Pfeiltasten (links, hoch, runter). Welche Variable muss jeweils angepasst werden, damit die Spielfigur korrekt reagiert?

## Zusatzaufgaben

### Geschwindigkeit ändern
Ändere die Variable `speed` um die Geschwindigkeit des Umhersausens zu erhöhen oder zu verringern.

### Spielfigur begrenzen
Wie kann verhindert werden, dass die Spielfigur aus dem Fenster herausfährt.

### Zwei Spielfiguren
Erstelle eine zweite Spielfigur mit einer anderen Farbe und steuere sie mit W, A, S, D.
