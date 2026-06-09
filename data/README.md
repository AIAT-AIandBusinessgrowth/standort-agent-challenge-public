# Seed-Dataset: Felder & Hinweise

> ⚠️ Synthetisch / vereinfacht, Stand 2026-06, keine offizielle AI:AT-Position. Die Gemeindenamen sind an reale österreichische Gemeinden/Bezirke angelehnt; die Werte (Einwohner, Altersverteilung, POI-Dichte, Mietindex, ÖV-Score) sind vereinfacht/gerundet und nicht für den produktiven Einsatz gedacht. Kein Domänenwissen nötig: die Felder unten verstehst du ohne Vorwissen.

## `municipalities.json` / `municipalities.csv` (20 Gemeinden/Bezirke, alle 9 Bundesländer)

`municipalities.json` und `municipalities.csv` enthalten dieselben Daten. Die CSV öffnest du bequem in Excel/Sheets; die JSON ist praktisch zum Einlesen im Code.

| Feld | Typ | Bedeutung |
|---|---|---|
| `gemeinde` | string | Name der Gemeinde / des Bezirks |
| `bundesland` | string | Bundesland (alle 9 sind vertreten) |
| `einwohner` | number | Einwohnerzahl im Bezirk (vereinfacht) |
| `altersverteilung` | object | Anteile `18_34`, `35_54`, `55_plus` (Summe ≈ `1.0`) |
| `poi_dichte` | number | Points-of-Interest-Dichte im Umfeld (`0`–`10`, synthetisch); mehr = belebter |
| `mietindex_eur_m2` | number | Durchschnittlicher Gewerbemietindex in EUR/m² (vereinfacht); mehr = teurer |
| `oev_score` | number | Öffentlicher-Verkehr-Score (`0`–`10`, vereinfacht); mehr = besser angebunden |

> **Achtung Skalen & Richtung:** Die Felder stehen in unterschiedlichen Einheiten (Anteile `0`–`1`, Dichte/ÖV `0`–`10`, Mietindex in €/m²) und zeigen nicht alle in dieselbe Richtung: ein hoher `mietindex_eur_m2` ist ein Kosten-/Risiko-Faktor (eher schlechter), eine hohe `poi_dichte` oder ein hoher `oev_score` ist ein Vorteil (eher besser). Wie du beides auf eine vergleichbare Basis bringst, bevor du gewichtet zusammenrechnest, ist deine Designentscheidung.

### CSV-Format

Die `municipalities.csv` beginnt direkt mit der Header-Zeile (der Disclaimer steht hier im README, damit Excel/Sheets die CSV sauber einlesen). Die verschachtelte `altersverteilung` ist in der CSV auf drei flache Spalten aufgeteilt: `altersverteilung_18_34`, `altersverteilung_35_54`, `altersverteilung_55_plus`.

`municipalities.json` trägt zusätzlich ein Top-Level-`_hinweis`-Feld sowie ein `_hinweis`-Feld je Eintrag, beide mit dem Synthetik-Vermerk.

> **Zwei Hinweise zum Dataset:**
> - **Die Gemeinde-Auswahl ist illustrativ.** Sie deckt alle 9 Bundesländer ab, ist aber keine vollständige oder repräsentative Liste. Das ist beabsichtigt und ein realistischer Praxisfall fürs Standort-Matching, keine Marktaussage.
> - **Du musst nicht jedes Feld nutzen.** Wähle, was für dein Ranking bzw. deine Analyse sinnvoll ist (ob z. B. `einwohner` als eigenes Signal einfließt, entscheidest du und begründest es kurz).

## `examples/profil_*.json` (Beispiel-Business-Profile)

Ausgangspunkt für deine Arbeit, ein Business-/Standort-Profil eines expandierenden Unternehmens:

| Feld | Typ | Bedeutung |
|---|---|---|
| `branche` | string | Branche / Geschäftstyp (Freitext) |
| `flaeche_m2` | number | Benötigte Fläche in m² |
| `zielgruppe` | string | Zielkundengruppe (Freitext) |
| `budget_miete_eur` | number | Maximales Monatsbudget für Gewerbemiete in EUR |
| `region_praeferenz` | string | Gewünschte Region / Bundesland (oder „Österreich" = keine Einschränkung) |
