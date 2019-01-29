# Maandag 21 januari

### Iedereen | 6 uur
- Voortgangspresentatie
- Meeting met Caitlin
- Meeting met het NLR


### Bob | 5 uur
- 4 bands NIR trainen

# Dinsdag 22 januari

### Alex | 4 uur
- Huidige training/ classificatie verbeteren, IR, andere hidden layers
- rectsize = 7, trainingsteps=1000, lineslimit=400000,2 test 8 train images, trainen op fotos met veel stedelijke gebieden:
0.66 accuracy maar slecht resultaat.

### Midas | 7 uur
- Post-processing, line-detection

### Alex & Midas | 3 uur
- accuracyberekening roadmap vs validation

### Bob | 4 uur
- 4 bands Tif classificeren ipv JPG

### Rutger | 7 uur
- Multiclassify afgemaakt
- Multiclassify getest
- Supercomputer aan de praat krijgen en testen

# Woensdag 23 januari
### Rutger | 7 uur
- Met de supercomputer onderzoeken welke rectsize het best werkt
- Met de supercomputer onderzoeken of andere hidden layers invloed hebben

### Bob | 8 uur
- Onderzoekt of er een formule is voor een goede grote voor het hidden network
- Onderzoekt hoe we een treshhold in het netwerk kunnen implementeren
- Een verdunner gemaakt voor de roadmap zodat er minder scheiding tussen weg en gebouw wordt geclassificeerd

### Alex | 6 uur
- Kijkt of landelijke gebieden of stedelijke gebieden beter classificeren
- rectsize=5, trainingsteps=100, lineslimit=200000, 6 training en 2 tests img. Trainingstijd: 20 min. Getrained met afbeeldingen van stedelijke gebieden en resultaat is goed. Niet getrained met dunne wegen.
- rectsize=5, trainingsteps=100, lineslimit=200000, 5 training 2 test img. Trainingstijd: 23 minuten. Getrained met dunne wegen, Prima resultaten maar weg is erg dun.
- rectsize=5, trainingsteps=100, lineslimit=200000, 7 training 2 test img. Trainingstijd: 15 minuten. Getrained op afbeeldingen zonder snelwegen. waaardeloos reulstaat, waarschijnlijk doordat in de test wel snelwegen stonden.
- rectsize=5, trainingsteps=100, lineslimit=200000, 7 training 2 test img. Trainingstijd: 22 minuten. Getrained op afbeeldingen zonder snelwegen met verdunde wegen en getest op afbeeldingen zonder snelwegen. Slechte resultaten. conclusie: gewoon snelwegen bewaren.
- rectsize=5, trainingsteps=100, lineslimit=200000, 7 training 2 test img. Nieuw netwerk: 150x200x150x100: resultaat is niet enorm veel beter dan normaal. wel hogere accuracy!!!
# Tests voor grafieken en final tests
- rectsize=5, trainingsteps=100, lineslimit=400000, 7 training 2 test img, acc= 0.68!!!. 

# Donderdag 24 januari

### Iedereen | 1 uur
- Meeting met Caitlin

### Midas | 6 uur
- Het netwerk testen met Conv Nets

### Alex | 6 uur
- Testen/trainen op bijvoorbeeld enkel stedelijk gebied of enkel platteland

### Bob | 6 uur
- Classificeren met de dunnere wegen
- Dunnere wegen in het technisch rapport

### Rutger | 6 uur
- NIR aan Multi-segmentation toevoegen
- Dunnere wegen aan Multi-segmentation toevoegen

# Vijdag 25 januari


### Midas | 7 uur
- Het netwerk testen met Conv Nets

### Alex | 7 uur
- Het netwerk testen met 1 soort weg (snelweg)

### Bob | 6 uur
- Technisch rapport aanvullen

### Rutger | 7 uur
- Multi-segmentation debuggen