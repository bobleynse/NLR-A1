# Maandag 7 januari 
### Iedereen | 2 uur
- Inleidend college van het project 
### Iedereen | 2 uur
- Meeting (presentatie) met NLR. Introductie en samenvatting van opdracht. Contactgegevens uitgewisseld. Github aangemaakt. Logboek aangemaakt.
- Uitzoeken hoe tiff bestanden werken.

# Dinsdag 8 januari
### Alex | 5 uur
- Uitgezocht hoe je Tensorflow installeert en hoe erin kunt werken. O.a. compatibiliteit met (geo)tiff bestanden, bestaande afbeeldingen labelen. (zie onderstaande installatiestappen)
- Tutorial handwriting recognition gevolgd
### Midas | 6 uur
- Uitgezocht hoe je werkt met Tiff-files en een voorbeeldbestand aangemaakt hoe je Tiff-fi
### Alex | 1 uur
- Start aan technisch rapport: onderzoeksvraag bedenken, opmaak in LaTeX zetten.

### Bob | 4 uur
- Een installatie-instructie gemaakt voor de programma's waar we mee werken
    - installeer python 3.6.7-amd64 (alleen hierin werkt tensorflow)
    - installeer matplotlib numpy en dergerlijke
    - pip install tensorflow
        - installeer GDAL (programma om tiffs te bewerken)   
        - Download van deze site: https://www.lfd.uci.edu/~gohlke/pythonlibs/#gdal deze file: GDAL‑2.3.3‑cp36‑cp36m‑win_amd64.whl
        - pip install vanuit je juiste folder in de terminal
        - py -m pip install GDAL-2.3.3-cp36-cp36m-win32.whl

### Rutger |
- Was heel de dag naar een begrafenis


# Woensdag 9 januari
### Iedereen | 1 uur
- Kennismakingsgesprek met onze TA. Uitkomsten:
    - Deep learning segmentation netwerken gaan het beste werken en worden ook door de opdrachtgever een klein beetje van ons verwacht.
    - Halverwege komende week moeten we weten of we iets kunnen met de segmentation netwerken
### Iedereen | 1 uur
- Analyse van voorgaande onderzoeken interessant zijn:
    - https://github.com/mahmoudmohsen213/airs
        - Een erg vergelijkbaar project maar niet heel uitgebreid gecommend
    - https://github.com/jremillard/images-to-osm
        - Ook erg vergelijkbaar maar heeft dagen de tijd nodig om te runnen
### Alex & Midas | 4 uur
- Verder verdiept in tiff bestanden. Met name in de controls van de verschillende colorbands
### Rutger | 4 uur
- installatie uitgezocht voor een Ubuntu systeem
### Bob | 2 uur
- Presentatie, logboek en wekelijks plan voorbereiden
### Bob | 2 uur
- Tiff maping uitgezocht
### Alex & Midas | 2 uur
- Data ontvangst van het NLR
- Bestandsformaten geanalyseerd
- Begonnen met het opknippen in kleinere delen zonder kwaliteitsverlies

# Donderdag 10 januari
### Alex & Midas | 4 uur
- Losse Tif RGB waardes gecombineerd tot een jpg om eerst een simpele segmentation network te kunnen leren
### Rutger & Bob | 4 uur
- Airs project gecommend en gekeken hoe we ons project hierin kunnen implementeren

# Vrijdag
### Bob | 2 uur
- Presentatie van Maandag voorbereid