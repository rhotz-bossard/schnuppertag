# PyGame - Programmieren mit Python

In dieser einfachen Übungen lernen wir die Programmiersprache Python mit PyGame kennen.
Mit PyGame lassen sich ganze Spiele programmieren. Dies können wir aus Zeitgründen leider nicht machen, aber wir können ein paar Basics lernen.

## Ein grauer Bildschirm
Erstelle eine neue Text-Datei `main.py` und öffne sie im Visual Studio Code.

Die Grundstruktur sieht wie folgt aus. Kopiere das Beispiel in die `main.py` und speichere die Datei.
Lass dich von der kryptischen Schreibweise nicht verunsichern. Es ist nicht so kompliziert wie es aussieht. :)

``` python
import pygame

pygame.init()

window_width = 800
window_height = 600
background_color = (25, 25, 25)
window = pygame.display.set_mode((window_width, window_height))

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    window.fill(background_color)
    pygame.display.update()

pygame.quit()
```

In diesem Programm erstellen wir ein Fenster von der Grösse 800x600 Pixel und lassen es mit einer Hintergrundfarbe ausmalen.
Starte das Programm über das kleine Play-Symbol oben Recht im Editor.

Versuche nun, die Hintergrundfarbe zu ändern. Finest du heraus, wo du im Programm die Farbe ändern kannst?

> TIPP: Hier findest du einen Farbmischer für RGB: https://informatik.schule.de/rgb/RGB_farbmischer.html
