# Geometrische Formen zeichnen

Mit PyGame lassen sich sehr einfach geometrische Formen zeichnen.

## Das Koordinatensystem
Das Koordinatensystem beginnt beim PyGame oben links in der Ecke. D.h. Oben Links ist x=0 und y=0, das ist zu Beginn etwas verwirrend.

## Das Rechteck
Du findest bereits eine Datei `main.py`, welche du erweitern kannst. Öffne die Datei im Editor.

Kopiere den folgenden Code in den TODO bereich. Dies zeichnet ein Rechteck von der Grösse 100*200 an der Position x=32, y=32.

``` python
    # TODO: zeichne ein Rechteck
    pygame.draw.rect(window, "red", (32, 32, 100, 200))
```
> TIPP: Achte auf die Klammern beim Koordinatensystem: (x, y, breite, höhe)

## Ein Kreis
Man kann natürlich auch einen Kreis zeichnen:
```python
pygame.draw.circle(window, "blue", (200, 200), 100)
```
> TIPP: Achte auf die Klammern beim Koordinatensystem: (x, y), radius)

Wie kannst du den Kreis genau in die Mitte des Fensters zeichnen?

## Eine Linie
Du kannst auch eine Linie zeichnen:
``` python
pygame.draw.line(window, "white", (0, 0), (window_width, window_height), 10)
```
> TIPP: Achte auf die Klammern beim Koordinatensystem: (x-startpunkt, y-startpunkt), (x-endpunkt, y-endpunkt, liniendicke))

Spiele nun mit den Zeichnungsfunktionen und erstelle für dich ein geometrisches Muster.
