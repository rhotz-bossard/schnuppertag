# Events

Einfach ein Programm zu starten ist langweilig. Wir wollen nun damit etwas machen.
Über Events können Tastatureingaben verarbeitet werden.

## Ein grauer Bildschirm
Erstelle eine neue Text-Datei `main.py` und öffne sie im Visual Studio Code.

Du findest bereits eine Datei `main.py`, welche du erweitern kannst. Öffne die Datei im Editor.

Das Programm läuft im Dauerloop und wartet auf unsere Eingaben.
Im vorherigen Beispiel konnte das Programm durch Klicken auf das X rechts oben beendet werden.

Nun wollen wir das Programm auch beenden, wenn wir Escape (ESC) drücken.
Wir müssen also auf das Event `Drücke ESC` reagieren.

Das können wir machen, indem wir unterhalb von `# TODO` folgendes einfügen:
``` python
        # TODO: hier auf ESCAPE reagieren
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False
```
Anschliessend kann das Programm mit dem Play-Symbol wieder gestartet werden.
Kannst du das Fenster nun mit Escape auch schliessen?

Versuche eine zusätzliche Taste zum schliessen zu verwenden, z.B. die Q-Taste.


> TIPP: Achte auf das korrekte Einrücken.

> TIPP: Hier findest du die Dokumentation der Tastatur-Events: https://www.pygame.org/docs/ref/key.html

