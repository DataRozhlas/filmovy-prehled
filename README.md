Datová analýza 125 let českého filmu pro články na serveru iROZHLAS.cz. 

Data jsou oscrapovaná z [Filmového přehledu](https://filmovyprehled.cz/), autoritativní databáze spravované Národním filmovým archivem. Pro bližší informace o datových položkách viz [vysvětlivky této databáze](https://www.filmovyprehled.cz/cs/clanek/vysvetlivky-a-zkratky):

> Jako primární zdroj informací při zpracování slouží jednotlivé filmy, pokud jsou dochované a dostupné na filmových kopiích, negativech nebo v digitální podobě ve sbírkách Národního filmového archivu. Čerpáno bylo z úvodních i závěrečných titulků, pokud možno původních, a zhlédnutím celého snímku.  
Doplnění těchto údajů dále probíhá ze sekundárních zdrojů. Těmi jsou myšleny například distribuční listy, presskity, tiskové zprávy, plakáty, údaje od distributorů a samotných producentů, zákonná nabídková a oznamovací povinnost, cenzurní spisy, ministerské věstníky, internetová média, mapy, databáze, literární a technické scénáře, titulkové, dialogové a honorářové listiny, herecké smlouvy, výrobní listy, filmový a nefilmový soudobý tisk i časopisy, fotografie, reklamní materiály, ročenky, memoárové knihy, rozhovory s tvůrci a pamětníky, filmografické práce, publikace o filmařích a hercích, soupisové a obrazové publikace, literární předlohy, tiskové a novinářské konference a projekce, archivní prameny, zahraniční zdroje, soudobé mapy a řada dalších.

## Struktura sešitů

- Od č. 001 do č. 099 scrapujeme a čistíme data; zásadní jsou při tom notebooky do č. 016. Z posloupnosti se vymykají sešity od 090 do 099, které doplňují a kontrolují informace v již oscrapovaných a vyčištěných dataframech a ukládají je pro další kolo čištění. To je však při naklonování repozitáře pro vlastní pokusy jedno, stačí ručně rozbalit ZIPy ve složce `data` a začít až notebooky s explorací od čísla 100 výš.

- Sešity od č. 100 až do hypotetického č. 899 zachycují exploraci. Vzhledem k opravám datasetů a refaktorizaci funkcí nebude při opětovném spuštění část z nich fungovat. I kdyby fungovaly, od výsledků jejich výpočtů dávám ruce pryč, protože jsem některé z nich opustil kvůli nalezeným chybám, které jsem se jal opravovat a k notebookům už jsem se pak často vůbec nevrátil. Zveřejňuji pouze pro inspiraci.

- Podstatné jsou sešity od č. 900 výše – obsahují co nejpřesnější možné výpočty, následně použité v článcích na iROZHLAS.cz.

## Další praktické informace

Data byla naposledy oscrapována 27. 5. 2023.

***Pozor***: Oscrapované a pročištěné dataframy nejsou ekvivalentní k originální databázi Filmového přehledu, a to z několika důvodů:

- Dataframe `filmy.json` pro jednodnost používá jména lidí tak, jak jsou uvedena na jejich profilu, ne v podobě z titulků či distribučních materiálů.

- Některé informace ve `filmy.json` chybí (výrobní společnosti bez vlastního profilu na stránkách FP), jiné jsou upravené (ve jménech chybí příznak "/ž/" a některé akademické tituly).

- Je možné, že se některé detaily některých filmů oscrapovaly chybně a ani několik desítek člověkohodin práce s datasetem k odhalení těchto chyb nevedly.

- Několik jednotlivých životopisných údajů v dataframe `persony.json` je doplněno z jiných zdrojů.