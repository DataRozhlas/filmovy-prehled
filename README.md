Scraping a analýza dat o 125 letech českého filmu pro články na serveru iROZHLAS.cz. 

Data pocházejí z [Filmového přehledu](https://filmovyprehled.cz/), autoritativní databáze spravované Národním filmovým archivem. Pro bližší informace o datových položkách viz [vysvětlivky této databáze](https://www.filmovyprehled.cz/cs/clanek/vysvetlivky-a-zkratky):

> Jako primární zdroj informací při zpracování slouží jednotlivé filmy, pokud jsou dochované a dostupné na filmových kopiích, negativech nebo v digitální podobě ve sbírkách Národního filmového archivu. Čerpáno bylo z úvodních i závěrečných titulků, pokud možno původních, a zhlédnutím celého snímku.  
Doplnění těchto údajů dále probíhá ze sekundárních zdrojů. Těmi jsou myšleny například distribuční listy, presskity, tiskové zprávy, plakáty, údaje od distributorů a samotných producentů, zákonná nabídková a oznamovací povinnost, cenzurní spisy, ministerské věstníky, internetová média, mapy, databáze, literární a technické scénáře, titulkové, dialogové a honorářové listiny, herecké smlouvy, výrobní listy, filmový a nefilmový soudobý tisk i časopisy, fotografie, reklamní materiály, ročenky, memoárové knihy, rozhovory s tvůrci a pamětníky, filmografické práce, publikace o filmařích a hercích, soupisové a obrazové publikace, literární předlohy, tiskové a novinářské konference a projekce, archivní prameny, zahraniční zdroje, soudobé mapy a řada dalších.

Struktura sešitů:

- Od č. 001 do č. 099 stahujeme a čistíme data. Z posloupnosti se vymykají sešity od 090 do 099, které doplňují a kontrolují informace v již oscrapovaných a vyčištěných dataframech a ukládají je pro další kolo čištění. To je však při naklonování repozitáře pro vlastní pokusy jedno, stačí ručně rozbalit ZIPy ve složce `data a začít až notebooky s explorací od čísla 100 výš. Získáte tím přístup k doposud nejčistějším datům. (Oscrapováno na jaře 2023.)

- Sešity od č. 100 do ??? zachycují exploraci – je pravděpodobné, že vzhledem k opravám datasetů a refaktorizaci funkcí nebude část z nich fungovat. I kdyby fungovaly, od výsledků jejich výpočtů dávám ruce pryč, protože jsem některé z nich opustil kvůli nalezeným chybám, které jsem se jal opravovat a k notebookům už jsem se pak často vůbec nevrátil. Zveřejňuji pouze pro inspiraci.

- Podstatné jsou sešity od č. 900 výše – obsahují co nejpřesnější možné výpočty, následně použité v článcích na iROZHLAS.cz.

Další praktické informace:

***Pozor***: Oscrapované a pročištěné dataframy nejsou ekvivalentní k originální databázi Filmového přehledu, a to z několika důvodů:

- Dataframe `filmy.json` pro jednodnost používá jména lidí tak, jak jsou uvedena na jejich profilu, ne v podobě z titulků či distribučních materiálů.

- Některé informace ve `filmy.json` chybí (výrobní společnosti bez vlastního profilu na stránkách FP), jiné jsou upravené (ve jménech chybí příznak "/ž" a některé akademické tituly).

- Je možné, že se některé detaily některých filmů oscrapovaly chybně a ani několik desítek člověkohodin práce s datasetem k odhalení těchto chyb nevedly.

- Dataframe `persony.json` vyzobává jen některá vyznamenání; několik jednotlivých životopisných údajů je v něm doplněno či opraveno z jiných zdrojů. 

Herectvo lze analyzovat dvěma způsoby. Méně preferovaný, zato jednodušší je nahrát dataframe `herectvo.json`, kde jsou však jen herci a herečky s vlastním ID a profilem na Filmovém přehledu. S tímto dataframe dává smysl pracovat tam, kde potřebujeme informace o rolích. Ve většině případů je vhodnější nahrát dataframe `filmy.json` a pracovat se sloupcem `Hrají`, protože v něm jsou i lidé, kteří se nedočkali vlastního profilu v databázi Filmového přehledu. Biografické údaje lze (nejen k herectvu) doplnit z dataframe `persony.json`.