# Steuerung

Wir hatten bereits etwas das Event-System kennengelernt (zum Schliessen des Programms).
Nun wollen wir unsere Spielfigur umherfahren lassen.

## Pfeiltasten
Mit den Pfeiltasten können wir unser Rechteck umherfahren lassen.
Lade `main.py` und ergänze beim TODO:
```
    # TODO: Pfeiltaste nach Rechts
    if keys[pygame.K_RIGHT]:
        player_x += speed * delta_time
```

Ergänze den Code mit den übrigen Pfeiltasten (links, hoch, runter). Welche Variable muss jeweils angepasst werden, damit die Spielfigur korrekt reagiert?

Ändere die Variable `speed` um die Geschwindigkeit des Umhersausens zu erhöhen oder zu verringern.


