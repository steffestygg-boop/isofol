# Isofol Medical – investeraröversikt

Arbetsregler för alla uppdateringar: läs [AGENTS.md](AGENTS.md), följ varje följdändring tills inget återstår och kontrollera därefter de andra aktiesidorna.

Privat, inofficiell svensk investerarsida med aktieöversikt, TO2-scenarier, filtrerbar milstolpstidslinje och emissionsbarometer.


## Big Pharma-due diligence och riskbarometrar (17 november 2026)

Ramverk: [Vision Lifesciences – Pharma Due Diligence Checklist](https://visionlifesciences.com/insights/pharma-due-diligence-checklist). `data/financing_model.json → partner_due_diligence` innehåller den **manuellt granskade** bedömningen för sju områden: klinik, patent/IP, regulatoriskt, kommersiellt, finansiellt, tillverkning/CMC och juridik/avtal. Den visar också nästa tänkbara beslutströskel hos en köpare, kapitaltiming, tre finansieringsscenarier och okända faktorer. Sidan läser detta underlag direkt från JSON.

**Princip:** Klinisk/långsiktig potential, sannolikhet och **timing** för ett Big Pharma-avtal samt bolagets finansieringsbehov är olika frågor. Ett uteblivet avtal är inte bevis på en avvisad tillgång. Antag inga garanterade framtida upfrontbetalningar eller optionslikvider som kassa. Skilj verifierade rapportuppgifter från subjektiva DD-bedömningar och undvik att dubbelräkna risk.

Emissionsbarometerns publicerade 3/6/12-månadersscenarier inkluderar `calculation.partner_dd_multiplier` utöver de redan kända kass-, studie- och kreditfaktorerna. Multiplikatorn är en uttryckligt subjektiv antagandefaktor (Isofol ×1,10; SynAct ×1,08), inte statistiskt kalibrerad eller ett besked från en tänkbar partner. Justera endast efter källkontrollerad manuell granskning. Veckoskriptet använder samma faktor och förklaringsdialogen i HTML visar den.


## Emissionsbarometern

Samma presentationssätt och veckokörning som på [SynAct](https://github.com/steffestygg-boop/synact), men Isofols **egna verifierade finansieringsuppgifter och modellantaganden**.

- `index.html` – finansieringsavsnitt med 3/6/12 månaders scenariosannolikheter, kassaläge, TO2, förklaringar och dokumenterade referensfall.
- `data/financing_model.json` – modell, datakällor, känslighetsintervall och sju historiska, källänkade kapitalanskaffningar.
- `data/financing.json` – senaste veckoberäkning och tydlig status för källkontroll och granskningsbehov.
- `scripts/update_financing.py` – uppdaterar tidsfaktorn, letar efter nya Isofol- och branschnyheter och identifierar nya finansierings- eller TO2-besked.
- `.github/workflows/update-financing.yml` – schemalagd **måndagar kl. 07:25 UTC**, kan även köras manuellt under Actions. Dataändringar triggar automatisk GitHub Pages-publicering.

### Grunddata per 13 november 2026

**Likvida medel:** 98,087 miljoner kr per 30 september 2026. **Kassaflöde från verksamheten:** –16,911 miljoner kr under Q3 och –47,391 miljoner kr januari–september. Bolaget bedömer att befintliga medel täcker planerad verksamhet i minst 12 månader från balansdagen. [Källa: Q3-rapporten 12 november 2026](https://mfn.se/a/isofol-medical/isofol-medical-ab-publ-publicerar-delarsrapport-for-januari-september-2026).

**TO2 – officiellt beslut 13 november 2026:** Teckningskursen har fastställts till **0,95 kr per ny aktie**, efter cirka 1,35 kr i VWAP 2–13 november. **39 863 928 optioner**, 1 TO2 = 1 aktie. **Teckningsperiod 16–30 november; sista handelsdag 26 november.** Utfallet väntas meddelas **omkring 1 december 2026**. Vid full teckning blir bruttolikviden aritmetiskt **37,8707316 miljoner kr (cirka 37,9 miljoner kr)** medan pressmeddelandet anger **cirka 37,7 miljoner kr** – avvikelsen är inte förklarad. Utspädning vid full teckning är cirka 11,06 %. Utfallet och nettolikviden är okända och har inte lagts till kassan. [Officiellt TO2-besked på MFN](https://mfn.se/a/isofol-medical/teckningskursen-for-teckningsoptioner-av-serie-to2-i-isofol-har-faststallts-till-0-95-sek-och-nyttjandeperioden-inleds-den-16-november-2026).

**Riskdefinition:** Ny annonserad kontant aktie- eller unitemission inom 3, 6 eller 12 månader. Nyteckning med TO2 räknas inte som nytt beslut om emission i denna modell, men kan innebära betydande utspädning.

**Metod:** Användarvänlig subjektiv scenariomodell med 2,1 % månatligt grundantagande, justering för utvecklingskostnader och TO2-osäkerhet, samt en närhetsfaktor mot 30 september 2027. Sannolikheten bygger inte på en representativ frekvensundersökning och får inte tolkas som objektivt uppmätt eller statistiskt kalibrerad. Peer-fallen är åskådliga fallstudier, inte ett slumpmässigt urval. Intervallet är känslighetsanalys, inte konfidensintervall.

**Automatikens begränsningar:** Veckoskriptet räknar om med förfluten tid och försöker upptäcka nya officiella bolagsmeddelanden, TO2-utfall, rapporter och branschemmissioner. Den ändrar *inte* verifierade kassa-, TO2- eller finansieringsantaganden från enbart rubriker. När utfallet av TO2, en ny rapport eller ett partneravtal publicerats måste modellen granskas och de relevanta värdena uppdateras från fullständiga originalkällor. En lyckad körning betyder inte att varje nyhet i världen har hittats eller förståtts.

Denna sajt är **inte investeringsrådgivning**.


## Dagliga förvarningssignaler (ny funktion, 13 november 2026)

Båda investerarsidorna har nu ett särskilt avsnitt **Varningssignaler** direkt under emissionsbarometerns 3/6/12-månadersrisker.

- **Verifierad siffergrund:** kassa i relation till senaste kvartalets operativa kassaflöde (bevakning under 9 månader, högre prioritet under 6), kvarvarande tid till bolagets försiktiga finansieringsriktmärke (bevakning inom 12 månader, högre prioritet inom 6), villkorad Fenja-kredit eller ännu ej verifierat TO2-utfall, samt rapportunderlag äldre än 115 dagar.
- **Nyhetsrubriker som varningssignaler:** handelsstopp och börsmeddelanden, uttalat finansieringsbehov, likviditetsbrist, uppskjutna betalningar till CRO/leverantörer, nya lån/konvertibler, kursras och hög omsättning, studiekostnadsökningar, förlorade partneravtal och beslut om nyemission. Reglerna finns öppet i `scripts/risk_signals.py`.
- **Källhänvisning per signal:** datum, allvarlighetsgrad, om faktaunderlaget är bekräftat eller bara en rubrikträff, vad som faktiskt har indikerats och vad som ska kontrolleras i originalkällan.
- **Daglig kontroll:** `.github/workflows/check-financing-signals.yml` kör `python scripts/update_financing.py --signals-only` omkring kl. 10:50 UTC. Signalerna publiceras via `data/financing.json`; datum för senaste kontroll och ofullständig täckning visas på sidan. `scripts/risk_signals.py` har regressionstester i `tests/test_risk_signals.py`.
- **Veckovis sannolikhet som tidigare:** `.github/workflows/update-financing.yml` uppdaterar 3-, 6- och 12-månadersmodellen varje måndag. Den dagliga kontrollen ändrar **inte** procenttalen, bara varningssignaler och källstatus.

**Detta är inte realtidsövervakning.** RSS-sökning och presslistor kan misslyckas, försenas eller missa börsmeddelanden. En högprioriterad rubrik är därför inte bevis på handelsstopp, insiderinformation eller nyemission. Den måste bekräftas mot bolagets och börsens originalbesked innan nya förhållanden viktas in i riskprocenten. Kända, verifierade rapportförhållanden kan redan ingå i basmodellen och får inte dubbelräknas.

## Kvartalsplacering av framtida milstolpar (13 november 2026)

**Alla framtida milstolpar visas i ett specifikt kvartal (Q1–Q4), aldrig enbart under ett helt år.**

- Om bolaget kommunicerat ett bestämt kvartal står det i tidslinjen och i detaljrutan med källa.
- Om bolaget bara angivit ett halvår eller inget datum alls visas en försiktig analytisk kvartalsuppskattning med **≈-markering**. Det betyder inte att bolaget har lovat kvartalet.
- Klicka på en framtida milstolpe för utförlig **tidsbedömning**, bakgrund, osäkerhet och länk till originalkälla. Osäkra placeringar kan behöva omprövas när bolaget uppdaterar tidsplanen.
- Historiska händelser får fortsätta grupperas per år eller längre perioder.


## Uppdaterad avläsningsplan efter källgenomgång 13 november 2026

Tre **olika** resultatnivåer skiljs åt i tidslinjen:

- **Q2 2027 (≈)** – **fullständiga data från fas Ib**, enligt vd:s vårprognos i BioStock-intervju 11 november. Våren kan också innebära senare del av Q1; placeringen är inte ett fast datum.
- **Q1 2027 (≈)** – **start av fas II**, förväntad men fortfarande beroende av sista doskohorten, säkerhetskommitté och studiecentra. Markeras som uppskattning.
- **Q4 2027 (≈)** – **första preliminära resultatavläsningen från fas II**, eftersom vd i samma intervju uttryckligen anger hösten 2027. Höstfönstret omfattar delar av Q3 och Q4, varför Q4 används som försiktigare platsmarkör.
- **Q1 2029 (≈)** – **slutliga topline-data från hela fas II** som analytiskt tidsscenario, *inte* bolagsguidning. ClinicalTrials.gov [NCT06922383](https://clinicaltrials.gov/study/NCT06922383) (registrering senast uppdaterad 29 juni 2026) visar planerad primary completion 30 november 2028. Databearbetning krävs efter primär datainsamling. Det offentliga [EU CTIS-registret](https://euclinicaltrials.eu/ctis-public/view/2024-516802-43-00) visar ett annat preliminärt studieslut, 1 april 2028. Båda uppgifterna kan ha förändrats med det utökade studieprogrammet; inget publicerat definitivt topline-kvartal har hittats.

**Källor:** [BioStock-intervju med vd 11 nov 2026](https://biostock.se/2026/11/isofol-om-patienter-som-ovantat-blev-operabla-i-cancerstudien/), [Isofols uppdatering 10 nov 2026](https://www.mfn.se/a/isofol-medical/isofol-lamnar-ny-uppdatering-fran-pagaende-fas-ib-ii-studie-av-arfolitixorin), [Q3-rapport 12 nov 2026](https://www.mfn.se/a/isofol-medical/isofol-medical-ab-publ-publicerar-delarsrapport-for-januari-september-2026), [ClinicalTrials.gov](https://clinicaltrials.gov/study/NCT06922383), [EU CTIS](https://euclinicaltrials.eu/ctis-public/view/2024-516802-43-00).

Att bolaget redan presenterat *preliminära* fas Ib-avläsningar i februari och november 2026 betyder inte att de fullständiga fas Ib-data som väntas våren 2027 redan är rapporterade.


## Klickbara finansiella beräkningar

**∑** intill ett beräknat tal öppnar en separat, tangentbordstillgänglig dialog med formeln, de värden som faktiskt används, uträkningen, avrundat resultat och relevanta originalkällor. Tryck **Escape**, klicka utanför dialogen eller använd stängknappen för att stänga; fokus återgår till den ursprungliga knappen.

- På båda sidorna: emissionsrisk 3/6/12 månader och känslighetsintervall, Q3:s genomsnittliga månatliga operativa kassaflöde och antalet månader fram till finansieringsmodellens riktmärke.
- **Finansieringshorisont:** Bolagets uttalande är en *guidning från originalrapporten*, inte en matematisk slutsats härledd ur historiskt kassaflöde. Dialogen skiljer uttryckligen bolagets guidning från veckomodellens datumräkning och en separat, förenklad Q3-baserad kassakvot.
- Isofol: TO2:s antal nya aktier, ägarutspädning och bruttolikvid enligt vald nyttjandegrad. Maximala 37,9 Mkr vid 100 % teckning visas och förklaras alltid oberoende av aktuell inställning. Pressmeddelandets cirka 37,7 Mkr redovisas separat.
- Underlaget läses från `data/financing.json` och `data/financing_model.json`. Ingen data ersätts med en förmodad aktuell kurs eller likvid när filer inte kan läsas.

Begränsning: det är en beskrivning av modellens beräkningsgång och antaganden, **inte** en statistiskt kalibrerad riskprognos eller investeringsrekommendation.


## Veckans nyheter – söndagsarkiv

Avsnittet **Veckans nyheter** ligger direkt efter **Aktien** och hämtar `data/weekly_news.json`. Den senaste sammanställda ISO-veckan visas direkt; äldre veckor ligger hopfällda i ett arkiv med **år, veckonummer och datumintervall**.

- **Söndag kl. 19:30 UTC:** `.github/workflows/weekly-news.yml` kör `scripts/update_weekly_news.py`. Det motsvarar **20:30 svensk vintertid eller 21:30 svensk sommartid**.
- **Måndag kl. 09:30 UTC:** En kompletterande körning fångar sena söndagsnyheter och den ordinarie finansiella veckouppdateringen. Även manuella körningar kan startas i GitHub Actions.
- **Nyhetsunderlag:** publicerade, daterade nyhetsrubriker via Google News RSS; `data/news.json`; redan dokumenterade milstolpar; tillgängliga risk-/emissionsdata i `data/financing.json` och `data/financing_model.json`.
- **Analysförändringar:** veckans sparade modellvärden, nya finansieringsvarningar, emissionsstatus och ändrade milstolpar jämförs mot föregående veckoutgåvas ögonblicksbild. För Isofol och SynAct visas förändringen i emissionsbarometerns risk för 3, 6 och 12 månader när en jämförbar historisk veckoutgåva finns.
- **Källskillnad:** händelser från tidigare källgranskade dataposter märks som sådana. RSS-rubriker märks tydligt som **inte fulltextgranskade**; systemet drar inte egna slutsatser om klinisk effekt eller kassaförändringar utifrån rubriktext.
- **Historik:** äldre veckor bevaras i samma JSON-fil, inte som en ny uppsättning som skriver över förra veckan. De inledande veckorna är 2026-W45 och 2026-W46. Veckor som rekonstrueras i efterhand får inte tilldelas finansieringsdata som först blev kända en senare vecka.
- **Tester:** `python -m unittest discover -s tests -p 'test_weekly_news.py'` kontrollerar ISO-veckor, veckogränser, proveniens, daterade milstolpar och att äldre veckor inte får senare emissionsvärden.

**Begränsning:** GitHub Actions är en schemalagd best-effort-körning och RSS-sökning är inte heltäckande. Ett automatiskt skript kan inte i sig analysera hela innehållet i alla artiklar. Avsnittet ger källanknutna, korta händelseöversikter, inte garanterat varje relevant uppgift eller en självständig faktagranskad fulltextsanalys. Vid otillgängliga RSS-källor används även de redan sparade lokala källorna.

### Klickbara fördjupningar till Veckans nyheter – november 2026

- Varje händelse i **Händelser under veckan** är nu en **helklickbar, tangentbordsstyrd knapp**, som öppnar en informationsruta med rubrik, en konkret sammanfattning, viktiga siffror, bakgrund, ekonomisk/klinisk betydelse och länk till den granskade originalkällan. Stäng med **Escape**, stängknappen eller klick på bakgrunden; fokus återgår till händelsen.
- De korta händelsekorten visar också fakta och siffror **utan att man behöver klicka**. Exempelvis får analytikeruppdateringar tydliga tidigare och nya värden (ABG 1,80 → 2,10 kr), studier får antal patienter och finansieringsbesked får villkor och belopp.
- Generiska innehållstexter som `Rapporterad kassa och historiskt kassaflöde är inte en dagsaktuell finansieringsprognos` har tagits bort från händelsekorten. Om en obekräftad RSS-rubrik saknar tillräcklig information används **inte** en påhittad förklaring; källan kan öppnas från informationsrutan.
- `data/weekly_event_details.json` innehåller **källgranskade** fördjupningar för viktiga händelser. Söndagsjobbet använder dessa plus `body`/`meaning` från redan dokumenterade milstolpar när det skapar `data/weekly_news.json`, så att tidigare manuellt förtydligade nyheter inte skrivs över med generiskt standardinnehåll.
- Källgranskade uppgifter hålls åtskilda från automatiskt inlästa rubriker. Källgranskade analysscenarier är fortfarande inte traditionella garanterade kursmål.

## Aktiekurs – automatisk och tidsstämplad (november 2026)

Under **Aktien** visas nu kursen med samma utformning som på SynAct-sidan: stor kurs i kronor, källa och den **faktiska kurstidpunkten**. TradingViews separata inbäddade kursruta har ersatts med en direktläst kursruta; en länk till TradingView finns kvar för jämförelse. Kursen kan vara fördröjd.

- `scripts/update_stock_quote.py` hämtar Isofol Medical (Yahoo-symbol `ISOFOL.ST`) från Yahoo Finances chart-endpoint och kontrollerar bolagssymbol, SEK, positivt kursvärde och tidsstämpel. Hämtningen sker automatiskt via `.github/workflows/refresh-stock-quote.yml` ungefär var 20:e minut på vardagar, med hänsyn till att GitHub Actions kan fördröjas och den externa kurskällan ibland kan vara otillgänglig.
- Kursen sparas i `data/stock_quote.json`. Webbplatsen hämtar filen vid öppning och kontrollerar om den ändrats varannan minut. Om kursen är från föregående handelsdag ska **detta datum synas**, inte klockslaget då GitHub Actions senast körde.
- Kurser under en krona behåller fler decimaler för att inte förlora meningsfull prisprecision. Kurserna har ingen automatisk påverkan på analysens emissionsrisk, milstolpar eller andra finansieringsantaganden.
- Källa och tidsstämpel visas intill kursen. Vid fel i kursleverantören behålls senast verifierade kurs och den ska inte presenteras som dagens livekurs. Regressionstester i `tests/test_stock_quote.py` kontrollerar kursvalidering och kursrutan.


### Kontrollerad daglig nyhetsbevakning – november 2026

**09.00 svensk tid varje dag:** `.github/workflows/weekly-news.yml` startar två alternativa UTC-tidpunkter (07 eller 08 UTC). Skriptet väljer rätt starttid efter sommar-/vintertid med hjälp av **vilket cron-uttryck som utlöste körningen**, inte vilken minut GitHub Actions råkar starta jobbet. En giltig körning får därför inte falla bort om GitHub blir försenat. Manuell omkörning fungerar oavsett klockslag.

**Eftermiddagskontroll på vardagar:** ytterligare körning kl. 14.00 UTC (15.00 på vintern / 16.00 på sommaren) fångar nyheter som publiceras senare än morgonsökningen.

**Flera oberoende nyhetskällor:** systemet söker direkt i respektive bolags MFN-lista över originalpressmeddelanden, kompletterat med breda Google News-frågor och mer riktade sökningar mot bl.a. BioStock, Börsvärlden samt analysfirmornas publiceringsplattformar. Såväl kliniska nyheter som finansiering, VD-förändringar, styrelsebeslut, aktieköp och analytikeruppdateringar bevakas.

**Veckogränser och dubbletter:** innehållet för innevarande vecka avser måndag till dagens datum. Händelser som hör till en tidigare ISO-vecka flyttas inte av misstag till en ny vecka. Ursprungliga bolagsmeddelanden prioriteras framför sekundära rubriksammanfattningar och dubbla MFN-återgivningar filtreras. Tidigare veckors arkiv förblir läsbart.

**Källkvalitet:** automatiskt insamlade rubriker märks som sådana och får inte påhittade sammanfattningar. Källgranskade fördjupningar med verifierade nyckeltal i `data/weekly_event_details.json` visas som klickbara informationsrutor. GitHub Actions och Google News ger ingen absolut garanti för start exakt 09.00 eller att samtliga nyheter indexeras omedelbart.

**Separata analyser:** kursrutan kan uppdateras ungefär var 20:e minut på handelsdagar. Emissions-/finansieringsrisken samt kliniska milstolpar har andra egna datakällor och uppdateringsrutiner; den dagliga nyhetssökningen innebär inte att varje risk- eller milstolpsantagande automatiskt skrivs om utan underlag.
