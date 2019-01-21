# Maandag 14 januari

### Iedereen | 2 uur
- Presentatie en bespreking met Caitlin

### Rutger & Bob | 2 uur
- Kijken of we het Airs project werkend kunnen krijgen

# Dinsdag 15 janiari
### Rutger & Bob | 3 uur
- We lopen er tegenaan dat we lege CSV's krijgen bij het runnen van ConvertToFeatureFiles
- Contact opgenomen met de maker van Airs om dit se fixen

### Alex & Midas | 3 uur
- De tiff-files van het NLR voorbereiden zodat we een testrun in het Airs project
- In qgis rgb banden samenvoegen.
- Max gb bereikt, big tif om het op telossen
- Banden individueel opgeslagen, merge rgb bands
### Rutger & Bob | 4 uur
- Een mini-test ontworpen van 400 bij 400 pixels
- Contact opgenomen met de maker van Airs voor informatie over de segmentation sizes
- 
- nog niet werkend gekregen
### Alex | 3 uur
- Alex maakt de corresponderende roadmap 400x400 (weg of geen weg) in de vorm van airs. (zwart of weg)
- Converteer grote tif naar naar kleinere tifs
- Converteer kleinere tiffs naar csv
- Converteer csv's naar correcte vorm van airs
- Converteer correcte csv's naar tiffs  
# Woensdag 16 januari

### Rutger & Bob | 7 uur
- Verschillende versies van Tensorflow geprobeerd om train.py werkend te krijgen
- De code aangepast van sklearn naar numpy en tensorflow arrays
- Na het verwijderen van oude models hebben we eindelijk een network kunnen trainen met de airs data

### Alex & Midas | 7 uur
- Data klaarmaken en namen overeen laten komen van input en output data

### Bob | 2 uur
- Github ordenen
- Oberbodige bestanden wissen
- Mail naar NLR over onze voortgang en een afspraak gemaakt

# Donderdag 17 januari

### Alex & Midas | 5
- Onze eigen data opgeknipt in stukken van 2500x2500 pixels voor de satellietfoto's en bijbehorende roadmap

### Bob | 3 uur
- Github ordenen
- De train.py, classify.py, convertToFeatureFiles gecomment
- Extra functie toegevoegd om meerdere models te trainen en te gebruiken
- Readme gemaakt zo dat iedereen een netwerk kan trainen
- Logboek en plan updaten

### Rutger | 3 uur
- Huidige voortgang beschreven in het technisch rapport

### Rutger & Bob | 

# Vrijdag 18 januari en het weekend

### Rutger | 8 uur
- Start met het maken van een Multi-road classifier
- in convertToFeatFiles.py het aantal classes aanpassen
- in train.py
- in classify.py

### Midas | 7 uur
- Tif to jpg converter gemaakt
- IR voorbereiden
- Start met het schrijven van een layerfunctie schrijven

### Alex | 9 uur
- Onderzoek hoe je je GPU inschakelt
- Huidige training/ classificatie verbeteren, IR, andere hidden layers
- VERGEET NIET DE TIJDEN TE METEN
- Grafiek aanpassing rectSize in convertToFeatFiles.py
- Grafiek aanpassing trainingSteps in train.py 
- Grafiek aanpassingen lineslimit in convertToFeatFiles.py
TODO: trainingsteps 100 - 500- 1000
    rectsize 1 - 3 - 5
    lineslimit 200000 - 400000 - 1000000
-accuracy noteren!!!
- 5 training img, 2 test img, rectsize = 5, trainingsteps: 100, lineslimit: 200000, kost 11 minuten en 8 seconden om te trainen met een accuracy van 0.6665867. Als een jpeg wordt gebruikt om te testen is het resultaat erg hoog.
- 10 training, 2 test img, rectsize = 7, trainingsteps: 500, lineslimit: 400000. Trainingtijd niet gemeten, ongeveer 30 minuten. Accuracy van  0.66623914. Classify krijgt een value error: "Cannot create a tensor proto whose content is larger than 2GB."
- 10 training, 2 test img, rectsize=7, trainingsteps=250, lineslimit=300000. trainingtijd 20 minuten en 10 sec, accuracy: 0.66662335. Opnieuw error :(
- 10 training, 2 test img, rectsize=7, trainingsteps=250, lineslimit=200000, trainingtijd 21 min en 3 sec, tantoe error.
- 10 training, 2 test img, rectsize=5, trainingsteps=100, lineslimit=200000, trainingtijd 21 min en 3 sec, tantoe error.
### Bob | 8 uur
- Presentatie maken
- Logboek maken
- Plan week 3 maken
- Iedereen proberen te helpen

## Toekomstplannen
- Infrarood toevoegen
- Het "weg, geen weg" trainen met onze eigen data
- Tijdsberekening 
- Een gescheiden, "meerdere wegen" classificatie schrijven
- Met grafieken onderbouwen waarom we een specifieke hoeveelheid 
- Een postprocessing algoritme schrijven. Bijv. losse pixels wegfilteren die overblijven.
- Programma schrijven die wegen op een satellietfoto plot
- Runnen op en externe GPU

## Vragen
- Hoe wil het NLR de output zien?
  - train
  - test
  - validation
- Kloppen de kleuren van onze Tiff? Daken worden blauw namelijk
- Eerst weg segmenteren en daaroverheen de rest of alles tegelijk segmenteren?
- Kunnen we classifien met betrekking tot de classifications van de omliggende punten
- Begeleiding bij de supercomputer

# Maandag 21 Januari

Tif classificeren