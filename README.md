# Isofol Medical – investeraröversikt

Privat, inofficiell svensk investerarsida med aktieöversikt, TO2-scenarier, filtrerbar milstolpstidslinje och emissionsbarometer.

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
