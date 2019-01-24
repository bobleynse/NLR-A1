# Maandag 21 Januari

### Iedereen | 6 uur
- Voortgangspresentatie
- Meeting met Caitlin
- Meeting met het NLR


### Bob | 5 uur
- 4 bands NIR trainen

### Rutger
- Multi road classification

### Alex 
- Huidige training/ classificatie verbeteren, IR, andere hidden layers
- rectsize = 7, trainingsteps=1000, lineslimit=400000,2 test 8 train images, trainen op fotos met veel stedelijke gebieden:
0.66 accuracy maar slecht resultaat.

### Midas | 3 uur
- Post-processing, line-detection

# Dinsdag 22 Januari
### Alex & Midas | 3 uur
- accuracyberekening roadmap vs validation

### Bob | 4 uur
- 4 bands Tif classificeren ipv JPG

### Rutger | 7 uur
- Multiclassify afgemaakt
- Multiclassify getest
- Supercomputer aan de praat krijgen en testen

# 3 Woensdag
### Rutger | 3 uur
- Met de supercomputer onderzoeken welke rectsize het best werkt
### Bob | 3 uur
- Onderzoekt of er een formule is voor een goede grote voor het hidden network
- Onderzoekt hoe we een treshhold in het netwerk kunnen implementeren

### Alex | 
- Kijkt of landelijke gebieden of stedelijke gebieden beter classificeren
- rectsize=5, trainingsteps=100, lineslimit=200000, 6 training en 2 tests img. Trainingstijd:


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
- Eerst weg segmenteren en daaroverheen de rest of alles tegelijk segmenteren?
- Kunnen we classifien met betrekking tot de classifications van de omliggende punten
- Begeleiding bij de supercomputer