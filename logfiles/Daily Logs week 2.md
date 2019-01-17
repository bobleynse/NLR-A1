# Maandag 14 januari

### Iedereen | 2 uur
- Presentatie en bespreking met Caitlin

### Rutger & Bob | 2 uur
- Kijken of we het Airs project werkend kunnen krijgen

# Dinsdag 15 janiari
### Rutger & Bob | 3 uur
- We lopen er tegenaan dat we lege CSV's krijgen bij het runnen van ConvertToFeatureFiles
- Contact opgenomen met de maker van Airs om dit se fixen

### ALex & Midas | 3 uur
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
- Voorbereidingen gemaakt 

### Bob | 2 uur
- Github ordennen
- Oberbodige bestanden wissen
- Mail naar NLR over onze voortgang en een afspraak gemaakt

# Donderdag 17 januari

### Alex & Midas | 3
- Onze eigen data opgeknipt in stukken van 2500x2500 pixels voor de satellietfoto's en bijbehorende roadmap

### Bob | 3 uur
- Github ordennen
- De train.py, classify.py, convertToFeatureFiles gecomment
- Extra functie toegevoegd om meerdere models te trainen en te gebruiken
- Readme gemaakt zo dat iedereen een netwerk kan trainen
- Logboek en plan updaten

### Rutger | 3
- Huidige voortgang beschreven in het technisch rapport


# Toekomstplannen
- Het "weg, geen weg" trainen met onze eigen data
- Een gescheiden, "meerdere wegen" classificatie schrijven
- Programma schrijven die wegen op een satellietfoto plot
