# c6-88 teken- en taalset

Dit document `c6-7` is het hoofddocument van de `c6-88` teken- en taalset.
`c6-88` is oorspronkelijk ontworpen door `c4-88` in het Nederlands.
De  internetthuisbasis van `c6-88` ofwel `c6-6` is <https://www.c6-88.org>.

## Missie

Tekens en talen beïnvloeden hoe leden in de gemeenschap (kunnen) communiceren, onthouden en denken. 
De missie is om de gemeenschap met `c6-88` nieuwe mogelijkheden te bieden voor het onderhouden en vernieuwen van de gemeenschap zelf.

## Schrijfwijze

`c6-88` wordt beschreven in Nederlands, gebaseerd op het Latijnse schrift en Arabische cijfers.
De documentatie is opgemaakt met [Github Flavored Markdown (GFM)](https://github.github.com/gfm/) om de teksten meer visuele structuur te geven voor de lezer.
Alle `c6-88` codes in de documentatie worden tussen twee grafen (\`) geplaatst om duidelijk te maken dat het om `c6-88`-codes gaat. 
Soms wordt in de broncode de combinatie van terugstreep en koppelteken of graaf (\\- of \\\`) gebruikt om een koppelteken (-) of graaf (\`) weer te geven om bepaalde opmaak door GFM te voorkomen.


## Hiërarchie

Documenten van `c6-88` bestaan in een stricte hiërarchie.
Ieder document moet geïnterpreteerd worden vanuit documenten hoger in de hiërarchie.
De hiërarchie op het hoogste niveau staat in onderstaande lijst:
1. [`c6-7`](README.md) is de top van de documenthiërarchie van `c6-88` en schept daarmee de context voor al het andere.
2. [`c6-8`](REGELS.md) bevat de regels voor het gebruik en de ontwikkeling van `c6-88`.
3. [`c6-9`](LICENCE) bevat de licentie rondom de auteursrechten en aanverwante zaken van `c6-88`.
4. [`c6-10`](CODE_OF_CONDUCT.md) bevat de gedragscode voor de gemeenschap die deelneemt aan `c6-88`.
5. [`c6-11`](CONTRIBUTING.md) bevat de richtlijnen voor deelnemers die willen bijdragen aan de ontwikkeling van `c6-88`.

Ontwikkelde code die geen documentatie is, dient te voldoen aan de documentatie.

## Tekenset

Met het woord 'tekens' bedoelen we exclusief de 12 tekens waarmee in `c6-88` gecommuniceerd wordt.
Andere elementen van de taal, zoals onder andere 'code', 'symbolen', 'letters' en 'cijfers', worden gevormd door een combinatie van tekens.
Om in het Nederlands te kunnen verwijzen naar de tekens, hebben zij elk een naam gekregen.
Het onderstaande overzicht bevat op de bovenste rij de `c6-88` tekens en op de onderste rij hun naam.
Dit zijn achtereenvolgens de cijfers 1 tot en met 9, het cijfer 0, het koppelteken en de c.

![De 12 `c6-88` basistekens](https://raw.githubusercontent.com/bvangils/c6-88/main/tekens/c6-88-namen.png)

## Taalsets

Losse tekens betekenen niets, dat doen zij pas in de context van een taalset.
Er zijn 6 taalsets gedefinieerd.
Elke set heeft een gebruiksdoel:
* [`c1-` set](taalsets/c1-.md): Het alfabet, interpunctie en symbolen voor communicatie van tekst.
* [`c2-` set](taalsets/c2-.md): Cijfers, symbolen en operators voor rekenkundige communicatie in het achttallig stelsel.
* [`c3-` set](taalsets/c3-.md): Beperkte set concepten voor efficiëntere communicatie van basisboodschappen dan met de `c1-` of `c2-` set.
* [`c4-` set](taalsets/c4-.md): Eigennamen die verwijzen naar unieke, levende entiteiten.
* [`c5-` set](taalsets/c5-.md): Codes om programmering van een microprocessor of -controller over te dragen.
* [`c6-` set](taalsets/c6-.md): Eigennamen die verwijzen naar unieke, niet-levende entiteiten, zoals plaatsen, tijden en voorwerpen.

## Berichten

Elk bericht begint met het teken `c`.
Het tweede teken is één van de tekens uit {`1`, `2`, `3`, `4`, `5`, `6`} en geeft aan welke taalset gebruikt gaat worden in het bericht.
Het derde teken is de `-`.
Hierna volgen codes in de geselecteerde taalset.
Elk bericht eindigt expliciet met de code `c-` of impliciet door geen tekens meer te noteren of versturen.

Voorbeeldberichten:  
`c3-5-8c-` betekent 'Veilig?' (expliciet berichteinde)  
`c3-3` betekent 'Ja' (impliciet berichteinde)

Tijdens een bericht kan er van taalset gewisseld worden.
Dit gebeurt door tijdens een bericht een code te verzenden zoals aan het begin van een bericht.

Voorbeeldbericht:  
`c3-5-c1-5069716978-c3-11-7-5--12-c1-90797878737114c-` betekent 'Regen bij jou? Hier zonnig.'


## Status

* De eerste officiële uitgave van `c6-88` is v1.0.0. - Timmerman.
    Voor die uitgave kunnen er onaangekondigd nog flinke, niet samenwerkende veranderingen plaatsvinden in de code.
    Na die uitgave werken aanvullingen en foutherstellingen samen met terugwerkende kracht.
    Niet samenwerkende veranderingen vinden pas weer plaats bij uitgave v2.0.0
    Die versie wordt pas ontwikkeld na minimaal een jaar praktijkervaring met uitgave v1.0.0. door 8 gebruikers.
