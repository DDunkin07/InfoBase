###git c Fachbegriffe

## High Level Programming Language
Beispiele: Java, Python

Sie sind darauf ausgelegt, leichter bedienbar und lesbar zu sein für Programmierer, im Gegensatz zu Low-Level-Sprachen, die schwerer zu lesen und benutzen sind, da sie näher zu der Maschinensprache ist als zu anderen Programmiersprachen.

 ## Assembly Language
Beispiele: MIPS, ARM

D Assembly Language ist Teil der Low-Level Programmiersprachen und sind eng mit der Maschinensprache des Computers verbunden. Assembly Code wird bei ausführung direkt in Maschinencode übersetzt.

## Machine Language
Beispiele: MIPS, PowerPC

Die Maschinensprache ist die grundlegenste Art von Computerprogrammiersprachen, die auch von dem CPU selbst verwendet wird. Die Maschinensprache besteht aus Binärzahlen die jeweils eine bestimmte Maschinenanweisung darstellen. Jedoch ist bei der Maschinensprache der Fakt zu beachten, das sie sich ändert je nach Prozessorarchitektur, da sie direkt von dem Prozessor verstanden und benutzt wird.



### Konzepte

Von-Numann: 
Die von-Neumann-Architektur ist das grundlegende Konzept hinter modernen Computern und besteht aus vier Hauptteilen:
+ Das Steuerwerk (Control Unit)
+ Die Arithmetisch/Logische Einheit (Arithmetic/Logic Unit, ALU)
+ Die Speichereinheit (Memory Unit)
+ Register (Kleiner Speicherbereich)

Das Steuerwerk (Control Unit) kontrolliert den Ablauf von Befehlen, holt die nächsten Befehle aus dem Serkläre ALUeicher und entschlüsselt Befehle und erkennt welche Operation ausgeführt werden soll im Computer.

Die Arithmetisch/Logische Einheit (Arithmetic/Logic Unit,  ALU) führt mathematische Berechnungen wie z.B. Addition, Subtraltion, Multiplikation etc. durch und führt auch logische Operationen wie AND, OR, NOt, XOR etc. durch

Die Speichereinheit (Memory Unit) speichert Daten sowie Programme ab und ist ein zentraler Bestandteil der Von-Neumann-Architektur, die von den meisten modernen Computern verwendet wird.

Register sind kleine und sehr schnelle Speicherbereiche, die sich direkt in der CPU befinden. Im Gegensatz zum RAM kann die CPU auf Register deutlich schneller zugreifen.



### Assemblersprache

## Instruction
Eine Anweisung für den Computer.

## Mnemonic
Ein verkürzter und vereinfachter Befehl, der für eine Person lesbarer ist

## Instruction Encoding
Die Darstellung einer Anweisung in Bits, die der Computer lesen kann.

## Instruction Format
Definiert den Aufbau eines Befehls, der von der CPU verstanden und ausgeführt werden kann.

## OPCode
Ein Teil der Instruktionscodierung, der die Art der auszuführenden Operation angibt. 

## Register
Eine kleine Speichereinheit im Prozessor, die zur temporären Speicherung von z.B. Daten verwendet wird.

## Memory Address
Eine Speicheradresse ist eine eindeutige Kennung für einen bestimmten Speicherplatz im Arbeitsspeicher (RAM) eines Computers.


### Instruktionskategorien

## Arithmetic
Führen grundlegende arithmetische Operationen wie Subtraktion, Addition oder Multiplikation durch.

## Move
Diese Instruktionen kopieren Daten zwischen Registern, Speicherorten oder anderen Speicherbereichen.

## Shift
Diese Instruktionen verschieben Bits innerhalb eines Operanden um eine bestimmte Anzahl von Positionen

## Load
Diese Instruktionen laden Daten aus verschiedenen Quellen in Register.

## Control
Diese Instruktionen ändern den Programmablauf, indem sie Sprünge, Schleifen oder Unterprogramme steuern.

## Memory
Diese Instruktionen führen Operationen auf Speicheradressen oder Speicherinhalten aus.



### 32-Bit Befehlssatz in Hexadezimal

Wenn man z.B einen 32-Bit Befehlssatz wie AND $1 $1 $1 hat, sucht man in einem MIPS Reference Skript erst einmal nach dem Befehlssatz den man hat, in diesem Fall AND. Man kopiert sich die Binärzahl des ersten Bytes heraus und schaut auch wie viele Bits die anderen Bytes dann haben und schreibt die Werte die man in den Registern z.B. 1 und 2 hat so auf, das man auf die benötigten Byten kommt.

Wenn man die Binärzahlen dann aufgeschrieben hat, teilt man die Bits in 4er Blöcke auf und schreibt zu jedem 4er Block dazu, welche Hexadezimalzahl diese Block hat. So hätte man dann einen 32-Bit Befehlssatz in Hexadezimal konvertiert.


### Bitreihe zu dazugehörigen MIPS Instruktion ordnen.

Um dies zu machen, braucht man wieder ein MIPS Reference Skript, wo man die ersten sechs Bit kopiert und im Skript nachschaut, zu welcher MIPS Instruktion diese gehören. So kann man dann auch die restlichen Byte umkonvertieren, falls nötig, da bei der MIPS Instruktion der ganze Aufbau des Befehlssatzes zu sehen ist.