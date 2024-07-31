10.1 Tastaturkürzel

# Tastaturkürzel

Sonic Pi ist zu gleichen Teilen Musikinstrument und Programmierumgebung. Mit Tastaturkürzeln kannst Du Sonic Pi viel *effizienter und natürlicher* spielen - insbesondere, wenn Du live vor Publikum spielst.

Sehr vieles in Sonic Pi kann mit der Tastatur gesteuert werden. Je vertrauter Du mit Sonic Pi wirst, umso mehr wirst Du diese Tastaturkürzel verwenden. *Ich selbst tippe, ohne die Tastatur anzusehen* (und kann Dir nur empfehlen, das Zehnfingersystem auch zu lernen). Und ich bin jedes Mal frustriert, wenn ich zur Maus greifen muss, denn das macht mich langsam. Deshalb benutze ich ständig Tastaturkürzel!

Wer die Tastaturkürzel beherrscht, kann auch seine Tastatur viel effektiver benutzen und in kürzester Zeit wirst Du programmieren wie ein Profi.

*Versuche aber nicht, alle auf einmal zu lernen*, merke dir erst einmal die, welche du am häufigsten brauchst und füge später weitere deinem Repertoire hinzu.

## Konsistenz auf verschiedenen Plattformen

Stell Dir vor, Du lernst Klarinette. Du kannst davon ausgehen, dass alle Klarinetten aller Marken gleiche Mechaniken und Fingersätze haben. Hätten sie das nicht, könntest Du nicht ohne weiteres zwischen verschiedenen Klarinetten hin- und her wechseln. Sondern müsstest immer bei einer Marke bleiben.

Unglücklicherweise haben die drei wesentlichen Betriebssysteme (Linux, Mac OS X und Windows) alle ihre eigenen typischen Tastaturkürzel für Aktionen wie z.B. Kopieren, Ausschneiden und Einfügen. Sonic Pi nutzt diese Standards wo immer möglich. Jedoch *liegt die Priorität auf plattformübergreifender Konsistenz* innerhalb von Sonic Pi, nicht auf dem Versuch, die Standards der jeweiligen Plattform vollumfänglich zu erfüllen. Das bedeutet, dass die in Sonic Pi auf dem Raspberry Pi gelernten Tastaturkürzel ebenso auf einem Mac oder PC mit Sonic Pi funktionieren.

## Control und Meta

Für diese Konsistenz müssen wir auch die Namen der Tastaturkürzel entsprechend auswählen. In Sonic Pi verwenden wir die Namen *Control* und *Meta* für die beiden wichtigsten Kombinationstasten. *Control* (*Ctrl* - oder *Strg* für "Steuerung" auf deutschen Tastaturen) ist auf allen Plattformen gleich. Auf Linux und Windows ist *Meta* die *Alt*-Taste, während *Meta* auf dem Mac die *Command*-Taste ist. Um konsistent zu bleiben, nutzen wir den Begriff *Meta* - diesem musst Du mental die passende Taste Deines Betriebssystems zuordnen.

## Abkürzungen

Um die Dinge einfach und lesbar zu halten, werden wir die Abkürzungen *C-* für *Control* und eine weitere Taste sowie *M-* für *Meta* und eine weitere Taste verwenden. Wenn ein Tastaturkürzel beispielsweise erfordert, dass Du *Meta* und *r* gleichzeitig drückst, werden wir die Abkürzung `M-r` verwenden. Der Bindestrich in der Mitte (*-*) bedeutet nur "zur gleichen Zeit."

Hier sind ein paar der Tastaturkürzel, die ich am nützlichsten finde.

## Starten und Stoppen

Du musst nicht immer zur Maus greifen, um Deinen Code auszuführen. Drücke stattdessen einfach `M-r` zum Abspielen. Mit `M-s` stoppst Du die Musik.

## Navigation

Ohne die Tastenkürzel zur Navigation bin ich verloren. Deshalb empfehle ich Dir dringend, diese Kürzel zu lernen. Sie funktionieren besonders gut, wenn Du das Zehnfingersystem schon halbwegs beherrschst, da sie normale Buchstaben verwenden - so musst Du Deine Hand nicht zur Maus oder zu den Pfeiltasten bewegen.

Mit `C-a` springst Du an den Anfang, mit `C-e` ans Ende einer Zeile. Eine Zeile nach oben geht es mit `C-p`, eine nach unten mit `C-n`, ein Zeichen vorwärts mit `C-f` und eines nach hinten mit `C-b`. Du kannst auch alle Zeichen von der aktuellen Cursorposition bis zum Ende der Zeile mit `C-k` löschen.

## Code aufräumen

Um Deinen Code sauber einzurücken, drücke `M-m`.

## Hilfesystem

Zum Hilfesystem kommst Du mit `M-i`. Noch hilfreicher ist allerdings `C-i`, damit wird Dir für das Wort, auf dem der Cursor gerade steht, sofort die passende Stelle in der Dokumentation gezeigt. Sofortige Hilfe!

Eine Liste aller Tastaturkürzel ist in Kapitel 10.2 "Cheatsheet für Tastenkürzel" enthalten.
