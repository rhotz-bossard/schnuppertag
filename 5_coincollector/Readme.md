# Coin Collector
Nun wollen wir unser erstes "richtiges" Spiel programmieren.
Mit unserer Spielfigur wollen wir Münzen einsammeln.

## Münzen hinzufügen
Zuerst wollen wir Münzen hinzufügen.
Editiere dafür `main.py` und füge bei TODO folgendes hinzu:
``` python
        # TODO: Münzen hinzufügen
        self.coins = [
            coin.Coin(self, 10, 150),
            coin.Coin(self, 250, 50),
            coin.Coin(self, 450, 350)
        ]
```

Starte nun das Programm. Die Münzen sind da, aber du kannst nichts mit ihnen machen.
Wir brauchen also noch die Möglichkeit, die Münzen einzusammeln.

## Kollisionsabfrage
Das machen wir über eine Kollisionsabfrage: Sobald die Spielfigur über eine Münze fährt, wird sie entfernt.

Ergänze hierfür in der Datei `coin.py` beim TODO:
``` python
        # TODO: Kollisionsabfrage
        if self.rect.colliderect(self.game.player.rect):
            self.is_destroyed = True
```

Jetzt wird die Münze entfernt, wenn du darüber fährst.

## Score anzeigen
Nun wollen wir anzeigen, wie viele Münzen du bereits eingesammelt hast.
Hierbei ergänzen wir in `main.py` die folgende Abfrage mit dem Erhöhen des Scores (`self.score += 1`):
``` python
                # TODO: Score Erhöhen
                if coin.is_destroyed:
                    self.coins.remove(coin)
                    self.score += 1
```

* Erstelle mehr Münzen.
* Versuche den Score grösser anzuzeigen, oder an einer anderen Position

