# Konzepte & Fachbegriffe

## Konzepte

### Klassen
Klassen in Python sind Baupläne für Objekte, die dazu verwendet werden, benutzerdefinierte Datentypen zu erstellen. Eine Klasse definiert eine Struktur, die sowohl Daten (Attribute) als auch Funktionen (Methoden) enthalten kann.

### Variable
Variablen in Python sind benannte Speicherorte, die verwendet werden, um Datenwerte zu speichern und zu manipulieren. Sie dienen als Referenzen auf die gespeicherten Daten, sodass diese im Laufe eines Programms leicht verwendet und geändert werden können.

### Konditionen
Konditionen in Python beschreiben Bedingungen oder Aufforderungen, damit etwas als "Wahr" gilt. Das heißt, in einem Code muss z.B. eine gewisse Zahl gegeben sein, damit der Code ausgeführt werden kann. Wenn dies nicht gegeben ist kann der Code logischerweise nicht ausgeführt werden. Bei Konditionen kann man dann sagen "If". Wenn dieses "If" erfüllt ist, ist das Ergebnis Wahr.

### Schleife
Schleifen, auch Loops genannt auf Englisch sind in Python etwas, was sich wiederholt, bis es z.B. eine gewisse Zahl erreicht hat. Das heißt, wenn man eine Loop in einen Code einbaut, wiederholt z.B. der Code sich ein paar Mal bis es die gewollte Zahl erreicht hat. Nachdem es dies geschafft hat, hört das Programm auf sich zu wiederholen. Ein Beispiel für ein Loop wäre die "For loop", welche über Objekte iteriert, also durch geht, bis es das gefunden hat, was es sucht.

### Funktion
Funktionen ermöglichen es, den Code innerhalb dem Programm besser zu strukturieren. So können einzelne Funktionalitäten des Programms in jeweils unterschiedliche Funktionen geteilt werden. Einee Funktion kann man sich als eine Art Unterprogramm vorstellen, welches man über den entsprechenden Funktionsnamen aufrufen kann. Wenn das erfolgt, werden alle Anweisungen der Funktion der Reihe nach ausgeführt. Anschließend wird der Programmverlauf ganz normal fortgesetzt.


## Fachbegriffe


### Scripting
Scripting bezieht sich auf das Schreiben von Skripten oder kleinen Programme, die häufig für automatisierte Aufgaben oder spezifische Anwendungen verwendet werden. Im Gegensatz zu umfangreichen Anwendungsprogrammen, die oft in kompilierten Sprachen wie C++ oder Java geschrieben werden, werden Skripte normalerweise in interpretierten Sprachen wie Python, JavaScript oder Bash geschrieben.


### Hacking
Hacking bezieht sich auf den unerlaubten Zugriff auf Computersysteme, Netzwerke oder Daten, oft für kriminelle Zwecke wie Daten Diebstahl oder finanziellen Betrug. Es kann jedoch auch ethisch sein, wenn autorisierte Sicherheitsanalysten Schwachstellen aufdecken, um Sicherheit zu verbessern. Hacktivismus nutzt Hacking-Techniken für politische oder soziale Zwecke.

### Coding
Coding ist im Wesentlichen die Erstellung von Anweisungen für Computer, um sie ausführen zu lassen. Es ist eine Möglichkeit, Computerprogramme zu schreiben, indem man eine spezielle Sprache verwendet, die von Menschen und Maschinen verstanden werden kann. Diese Sprache besteht aus einer Reihe von Anweisungen, die zusammenarbeiten, um bestimmte Aufgaben zu erledigen. 

### Programmierung
Programmierung ist der Prozess des Entwerfens und Schreibens von Computerprogrammen, um spezifische Aufgaben oder Problemlösungen zu automatisieren. Es umfasst eine Reihe von Techniken und Prinzipien, die es Entwicklern ermöglichen, Anweisungen in einer Weise zu formulieren, die Computer verstehen und ausführen können.

### Script
Ein Script (oder Skript) ist ein Programm oder eine Datei mit einer Reihe von Anweisungen, die ohne Kompilierung direkt interpretiert und ausgeführt werden können. Scripts werden oft in sogenannten Skriptsprachen geschrieben, die leicht verständlich und für die schnelle Entwicklung und Ausführung von Programmen optimiert sind. Beispiele für Skriptsprachen sind Python, JavaScript, Bash, Perl und Ruby.

### Algorithmus
Ein Algorithmus in Python ist eine präzise und eindeutige Schritt-für-Schritt-Anleitung zur Lösung eines bestimmten Problems oder zur Durchführung einer Aufgabe. Algorithmen sind zentral in der Programmierung und können in verschiedenen Programmiersprachen implementiert werden, einschließlich Python.

### Compiler
Ein Compiler ist ein Computerprogramm, das Quellcode in eine ausführbare Form übersetzt, die von einem Computer oder einem anderen Zielsystem direkt ausgeführt werden kann. Im Gegensatz zu Interpretern, die Anweisungen zeilenweise ausführen, übersetzt ein Compiler den gesamten Quellcode in eine Zwischenform, oft als Maschinencode oder Bytecode bezeichnet, bevor er ausgeführt wird.

### Compiler
Ein Interpreter ist ein Computerprogramm, das Quellcode Zeile für Zeile liest, interpretiert und direkt ausführt, ohne den gesamten Code im Voraus in eine ausführbare Form zu übersetzen. Im Gegensatz zu Compilern, die den gesamten Code auf einmal analysieren und übersetzen, führt ein Interpreter den Code schrittweise aus und gibt die Ergebnisse unmittelbar aus.



# Flussdiagramme

Flussdiagramme sind grafische Darstellungen von Prozessen oder Algorithmen. Jede Komponente, wie Start/Ende, Entscheidungen und Aktionen, wird visuell dargestellt, um den Ablauf eines Programms oder Prozesses zu veranschaulichen.


Start/Ende: Markiert den Anfang oder das Ende des Flussdiagramms und signalisiert den Start oder das Ende des Prozesses oder Algorithmus.

Aktionen: Führen spezifische Aufgaben aus, wie Berechnungen, Ausgaben oder andere Operationen im Programmablauf.

Entscheidungen: Basierend auf Bedingungen bestimmen Entscheidungen den Fluss des Programms, leiten verschiedene Pfade abhängig von wahren oder falschen Bedingungen.

Verzweigungen: Ähnlich wie Entscheidungen, jedoch mit mehreren Bedingungen, die verschiedene Pfade im Flussdiagramm beeinflussen können.

Schleifen: Wiederholen bestimmte Aktionen oder Prozesse, bis eine bestimmte Bedingung erfüllt ist, um Iterationen im Programmablauf zu ermöglichen.


# Programmieren in Python

## 11.2
## 14

### a.
WAHR
set = {0, 1, 2}
print(set[1])

## b.
FALSCH
Set = {"Hallo", "Welt"}
print(len(Set))

## c.
WAHR
Liste = [0, 1, 2]
Liste[1] += 1
print(Liste)

## d.
FALSCH
Liste = [0, 1, 2]
Liste[2] += 1
print(Liste)

## e.
WAHR
Liste = [0, 1, 2]
Liste[2] = Liste[0+1] + Liste[1-0]
print(Liste)

## f.
WAHR
Dictionary = {2: "Hallo"}
Dictionary[2+1] = "Hallo"
print(Dictionary)

## g.
WAHR
Dictionary = {3: "Welt"}
Dictionary[3] = Dictionary[3] + "weit"
print(Dictionary[3])

## h.
WAHR
Dictionary = {"Key": 42}
print(Dictionary["Key"])