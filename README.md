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

**TO2:** 39 863 928 optioner, 1 TO2 = 1 ny aktie. Teckningsperiod 16–30 november 2026, 70 % av VWAP 2–13 november med golv 0,48 kr och tak 1,60 kr. Uppskattad **bruttolikvid vid 100 % utnyttjande:** 19,1–63,8 miljoner kr. Faktisk likvid och nyttjandegrad är **inte verifierade** vid etableringen och räknas inte som nuvarande kassa. [Källa: emissionsvillkoren](https://mfn.se/all/a/isofol-medical/isofol-offentliggor-slutliga-villkor-i-foretradesemission-samt-for-en-potentiell-overtilldelningsemission).

**Riskdefinition:** Ny annonserad kontant aktie- eller unitemission inom 3, 6 eller 12 månader. Nyteckning med TO2 räknas inte som nytt beslut om emission i denna modell, men kan innebära betydande utspädning.

**Metod:** Användarvänlig subjektiv scenariomodell med 2,1 % månatligt grundantagande, justering för utvecklingskostnader och TO2-osäkerhet, samt en närhetsfaktor mot 30 september 2027. Sannolikheten bygger inte på en representativ frekvensundersökning och får inte tolkas som objektivt uppmätt eller statistiskt kalibrerad. Peer-fallen är åskådliga fallstudier, inte ett slumpmässigt urval. Intervallet är känslighetsanalys, inte konfidensintervall.

**Automatikens begränsningar:** Veckoskriptet räknar om med förfluten tid och försöker upptäcka nya officiella bolagsmeddelanden, TO2-utfall, rapporter och branschemmissioner. Den ändrar *inte* verifierade kassa-, TO2- eller finansieringsantaganden från enbart rubriker. När utfallet av TO2, en ny rapport eller ett partneravtal publicerats måste modellen granskas och de relevanta värdena uppdateras från fullständiga originalkällor. En lyckad körning betyder inte att varje nyhet i världen har hittats eller förståtts.

Denna sajt är **inte investeringsrådgivning**.
