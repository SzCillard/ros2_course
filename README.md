### Turtlesim Controller – Dokumentáció
Cél
Ez a Python program a ROS 2 (Robot Operating System) környezetében futó turtlesim szimulátor irányítására szolgál. A cél, hogy egy teknőcöt adott koordinátákra mozgassunk, "Sz" betűt fogja kirajzolni.

### Felépítés:

TurtlesimController osztály

Feladata: A teknős aktuális pozíciójának lekérdezése, és vezérlési parancsok küldése (/turtle1/cmd_vel topic).

Feliratkozik a /turtle1/pose topicra, hogy mindig friss információja legyen a teknős helyzetéről.

main() függvény

Példányosítja a vezérlő objektumot

Meghívja a draw_sz() függvényt, ami a go_to() függvényeket, amelyekkel egy-egy betű kirajzolása történik

### Működés:

A teknős mozgatása az go_to(speed, omega, x, y) függvény segítségével történik, amely egy célkoordinátához irányítja a teknőst:

speed: lineáris sebesség (mennyire gyorsan halad előre)

omega: szögsebesség arány (mennyire gyorsan fordul a cél irányába)

A függvény a következő lépéseket végzi:

Megvárja, hogy megérkezzen az első pozíció (Pose) üzenet

Kiszámolja a céltávolságot és a kívánt szöget

Arányos vezérléssel (proportional control) beállítja:

lineáris sebességet (csökken, ha közel van)

szögsebességet (omega * szögeltérés)

Publikálja a vezérlési parancsokat (Twist)

Leállítja a teknőst, ha elég közel ért a célponthoz

Használati példa – Betűk rajzolása

tc.go_to(1.0, 2.0, 5, 6)  # Elindul az (5,6) pontba
tc.go_to(1.0, 2.0, 5, 5)  # stb...

Ezeket a pontokat úgy kell összeállítani, hogy a teknős betűket rajzoljon a képernyőre.

Paraméterek hatása
Nagyobb omega: lassabb fordulás → egyenesebb mozgás

Kisebb omega: gyorsabb fordulás → íves, görbe mozgás

Nagyobb speed: gyorsabb haladás → néha pontatlanabb, ha túl gyors

Futás és használat
Indítsd el a turtlesim szimulátort:

ros2 launch ros2_course turtlesim_controller_launch.py

Fontos fájlok:
turtlesim_controller.py – fő vezérlő program

setup.py – telepítési konfiguráció, itt van bejegyezve az entry_point
