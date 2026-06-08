# 🛰️ AI Developer Challenge — „Standort-Agent"

Version 1.0 · 2026-06 · Kontakt: AI:AT Hiring Team

> Synthetisch / vereinfacht, Stand 2026-06 — keine offizielle AI:AT-Position.

Hi 👋 — schön, dass du dabei bist! Das hier ist kein Trick-Test. Es ist ein kleines, echtes Stück von dem, was wir im Venture Studio & n8n CoE täglich tun: **mit KI schnell etwas Lauffähiges bauen, das ein echtes Entscheidungsproblem zerlegt.** Diesmal etwas ambitionierter — ein **Multi-Agent-System**.

Es gibt keine Musterlösung, die du treffen musst. Wir schauen, wie du ein unscharf spezifiziertes Problem in Teilaufgaben zerlegst, eine Architektur entwirfst, Entscheidungen triffst und KI als Hebel einsetzt — und prüfst.

## Die Mission

Eine Standortentscheidung ist für ein expandierendes österreichisches Unternehmen (Filialist, Händler, Logistiker) ein **€500K+-Commitment** — und wird heute oft aus dem Bauch oder über teure Beratung getroffen. Bau einen **„Standort-Agent"**: ein System, das ein **Business-Profil** nimmt (z. B. Retail, 200 m², Zielgruppe junge Berufstätige, Mietbudget) und ein **begründetes Standort-Ranking** über österreichische Gemeinden liefert — pro Gemeinde mit nachvollziehbarer Begründung, plus ein **interaktiver HTML-Report**.

Der Clou: Standortbewertung ist **mehrdimensional** — Demografie, POI-/Umfeld-Dichte, Mietkosten, ÖV-Anbindung ziehen in unterschiedliche Richtungen. Genau das macht es zu einer schönen **Multi-Agent-Aufgabe**: pro Signal ein spezialisierter Subagent, ein Orchestrator, der aggregiert und gewichtet.

**Wir liefern dir:** ein Seed-Dataset mit 20 Gemeinden (`municipalities.json` + `municipalities.csv`, Felder dokumentiert) + 2–3 Beispiel-Profile. **Kein Domänenwissen nötig** — alles, was du brauchst, steckt im Dataset.

> 📂 **Im Repo:** [`../data/`](../data/) — `municipalities.json` + `municipalities.csv` + Beispiel-Profile unter [`../data/examples/`](../data/examples/) (Feld-Doku: [`../data/README.md`](../data/README.md)).

### Teil A — Bau den PoC

- **Input:** ein Business-Profil (`branche`, `flaeche_m2`, `zielgruppe`, `budget_miete_eur`, `region_praeferenz`). Dein Tool soll **mindestens eines der mitgelieferten Beispiel-Profile** verarbeiten — *wie* du Profile reinreichst (Datei, CLI-Argument …), ist dir überlassen.
- **Verarbeitung:** vier Signale — **Demografie** (Altersstruktur ↔ Zielgruppe), **POI/Umfeld** (POI-Dichte ↔ Branche), **Miete** (Mietindex ↔ Budget), **ÖV** (Anbindung ↔ Zielgruppe). Jedes Signal wird zu einem Teil-Score; der Orchestrator aggregiert sie zu einem **gewichteten Gesamt-Ranking**.
- **Output:** ein **begründetes Ranking** der passendsten Gemeinden — z. B. die **Top 3–5** (die Zahl ist deine Entscheidung, begründe sie kurz) — je „passt, weil… / passt nicht, weil…" pro Signal + ein **interaktiver HTML-Report** mit Ranking-Tabelle und Begründungen.
- **Form:** lauffähiges **Git-Repo** mit echtem Code + ein README, das uns das Ding in **< 5 min** zum Laufen bringt. Stack: **Python** (≥ 3.11). Welche Libraries, ob CLI oder mehr — dir überlassen.

> 🧭 **Die interessante Architektur-Entscheidung:** Wir nennen es bewusst „Multi-Agent" — ein **Orchestrator, der spezialisierte Subagents koordiniert**, ist die erwartete Form und die natürliche Zerlegung dieses Problems. **Wie** du sie umsetzt (eigene Klassen/Funktionen, ein Agent-Framework, ein LLM pro Subagent oder reine Heuristik) ist genau die Stelle, an der wir dein Urteil sehen. Ein sauber begründeter Nicht-Multi-Agent-Ansatz ist nicht automatisch falsch — aber dann erwarten wir die Begründung, *warum* die Zerlegung hier anders besser ist.

> 🎯 **Die andere Urteils-Stelle:** Die Signale stehen in **unterschiedlichen Einheiten und Skalen** (z. B. Bevölkerungsanteile 0–1, Dichte-Scores 0–10, Mietindex in €/m²) — und manche sind ein **Vorteil** (mehr = besser), manche ein **Kosten-/Risiko-Faktor** (mehr = schlechter). Wie du beides auf eine vergleichbare Basis bringst, bevor du gewichtet zusammenrechnest, ist deine Designentscheidung — wir achten auf die **Begründung**, nicht auf eine vorgegebene Formel.

> 💡 Echte LLM-Calls (z. B. für die generierten Begründungen) sind erlaubt, aber **nicht Pflicht** — eine deterministisch/templatebasiert erzeugte Begründung ist völlig okay. **Kein API-Key nötig**, falls du keinen hast: der Basis-Lauf muss ohne Schlüssel funktionieren.

### Teil B — Code-Review (~15 min)

Wir geben dir ein kurzes, KI-generiertes Code-Snippet (Python; **Tipp:** vergleiche, was der Doc-Kommentar *verspricht*, mit dem, was der Code *tut* — und denk an den Hinweis zu Skalen/Richtung oben). **Es gibt einen zentralen funktionalen Bug — finde *den*, fixe ihn, und begründe in 3–5 Sätzen, warum es einer ist.** Sag uns **auch, was dir sonst auffällt** (fehlende Edge-Cases, fragwürdige Annahmen, fehlende Validierung) — diese weiterführende Kritik zählt für uns genauso wie der Fix selbst. (Wir wollen sehen, ob du KI-Output beurteilen kannst — nicht nur erzeugen.)

> 📄 Das Snippet liegt als Datei unter [`code-review/snippet.py`](./code-review/snippet.py) — und ist unten in **Anhang A** abgedruckt.

## Spielregeln

- ⏱️ **Aufwand: ~4–6 fokussierte Stunden.** Du hast eine Woche — die ist für *Flexibilität*, nicht zum Durchgrinden. Bitte nicht überinvestieren: **wir bewerten Denken & Urteil, nicht Politur.** *(Die 4–6 h schließen Walkthrough + Decision-Log ein — Loom: 1 Take, 3–5 min; Decision-Log: 5–10 Zeilen Stichworte.)*
- 🤖 **Nutze jede KI, jede Library, google frei.** Wird erwartet, nicht nur erlaubt. Cursor, Claude, Copilot, Coding-Agents — leg los.
- 🎯 **Der Kern (A + B) ist die Latte** — dazu gehören auch **ein paar sinnvolle Tests** (kein Coverage-Theater; zählen mit 10 %). Echte Stretch-Goals (echte API-Integration via OSM Overpass, UI, Eval-Set, Deployment, LLM-generierte Begründungen, Konfidenzintervalle) sind zum Glänzen — komplett optional.

> **Wichtig:** Ein rauer Kern mit klarem Denken schlägt eine polierte, aber oberflächliche Umsetzung. Wir meinen das ernst — bitte nicht überinvestieren. Mehr Stunden bedeuten bei uns **nicht** mehr Punkte; wir bewerten das Kern-Ergebnis, nicht den Zeitaufwand. Eine saubere, gut begründete 4-Signal-Architektur schlägt zehn halbgare Subagents.

AI Factory Austria steht für Chancengleichheit. Brauchst du Unterstützung oder Anpassungen im Prozess, sag uns Bescheid — wir helfen. Ob Uni, Bootcamp oder self-taught: es zählt, wie du denkst und mit KI arbeitest.

## Was du abgibst

1. **Repo-Link** (GitHub/GitLab) mit Code + README + dem generierten HTML-Report (oder der Anleitung, ihn zu erzeugen).
2. **Code-Review-Antwort** (Teil B) — als Datei im Repo oder kurzes Doc.
3. **Walkthrough (1 Take, 3–5 min, max. 5):** ein Loom/Screen-Recording — zeig dein Ergebnis und erklär *wie* du gebaut hast, vor allem die Architektur-Entscheidungen und die KI-Schritte. *(Kein Video möglich oder gewünscht? Ein knappes schriftliches Walkthrough-Skript zählt als gleichwertig — sag einfach Bescheid.)*
4. **Kurzes Decision-Log + Schlüssel-Prompts:** 5–10 Zeilen Entscheidungen/Trade-offs (Subagent-Schnitt, Gewichtung, Umgang mit den unterschiedlichen Signal-Skalen) + die KI-Prompts, die den Unterschied gemacht haben. Zeig uns, *wie du mit KI zusammenarbeitest* — das ist genau die Fähigkeit, für die wir die Rolle besetzen.
5. **Selbst-Report:** wie viele Stunden hast du investiert? (Ehrlich — kein Maluspunkt.)

## So bewerten wir (transparent)

| Dimension | Gewicht |
|---|---|
| Funktionalität (läuft es, erfüllt es den Kern: Orchestrator + Subagents → Ranking + Report) | 20% |
| Decomposition & Urteil (Multi-Agent-Schnitt sinnvoll, gute Trade-offs, Ambiguität gelöst) | 20% |
| AI-Collaboration / Prozess (wie du KI gehebelt & geprüft hast) | 20% |
| Code-Qualität & Taste (lesbar, wartbar, konsistentes Subagent-Interface, KI-„Slop" erkannt) | 15% |
| Kommunikation / Doku (README, Decision-Log, Walkthrough) | 15% |
| Tests (sinnvolle Tests, kein Coverage-Theater) | 10% |

> Teil B (Code-Review) fließt **nicht** in die obige Gewichtung ein — es ist ein **separates Signal** mit besonders hohem Informationsgehalt über dein Urteil zu KI-Code und kann bei knappen Entscheidungen den Ausschlag geben.

## Abgabe & Zeitplan

- 🗓️ **Deadline:** **die Begleit-E-Mail nennt das verbindliche Abgabedatum** (Richtwert: 7 Kalendertage ab Erhalt).
- 📤 **Abgabe:** per E-Mail an aiandbusinessgrowth@ai-at.eu.
- ⏳ **Rückmeldung:** Wir melden uns innerhalb von ~10 Werktagen — mit einem Termin für den Live-Teil oder einer kurzen Rückmeldung.

> 💡 Die konkreten Daten (Abgabedatum, ggf. Upload-Link) findest du in der Begleit-E-Mail zu diesem Brief.

## Danach

Kurzer **Live-Walkthrough (30–45 min)**: du zeigst dein Ergebnis, wir setzen *live eine neue Anforderung* drauf — z. B. ein **fünftes Signal / einen neuen Subagent** hinzufügen — und schauen, wie du deine eigene Architektur erweiterst. Die neue Anforderung ist bewusst klein — es geht darum, wie du laut denkst, nicht um ein perfektes Ergebnis in 10 Minuten. Deine gewohnten KI-Tools darfst du dabei nutzen, genau wie beim Bauen. Danach zeigen wir dir unsere eigene Lösung — und wir reden ehrlich darüber. **Jede:r bekommt Feedback**, egal wie's ausgeht.

> **Fair & transparent.** Diese Challenge ist unbezahlt — dafür bekommst du echten Gegenwert: Nach dem Debrief zeigen wir dir **unsere eigene Lösung** — mit echten Entscheidungen, Prompts und Trade-offs. Das ist unser „Learn"-Versprechen in Aktion, kein Einblick, den du anderswo bekommst. Und: **strukturiertes, ehrliches Feedback für jede:n** — egal wie der Prozess ausgeht. Kein Ghosting. Nie.

Viel Spaß — wir sind gespannt, wie du mit KI ein Multi-Agent-System baust, das eine €500K-Entscheidung nachvollziehbar macht. 🚀

## Datenschutz

> **Datenschutz.** Deine Unterlagen (Repo-Link, Loom-Link, Dokumente, Prompts) nutzen wir ausschließlich für die Besetzungsentscheidung, geben sie nicht an unbeteiligte Dritte weiter und löschen sie spätestens **sechs Monate** nach Abschluss des Auswahlverfahrens (oder früher auf deinen Wunsch) — gemäß DSGVO. Rechtsgrundlage ist die Anbahnung eines möglichen Arbeitsverhältnisses (Art. 6 DSGVO); du kannst jederzeit Auskunft oder Löschung verlangen. **Was du erstellst, bleibt deins** — wir verwenden es nur zur Bewertung, nie produktiv. Dein Repo kannst du auch privat halten und uns Zugriff geben; deinen Walkthrough sehen nur wir intern. Von dir gewählte Hosting-Dienste (z.B. GitHub, Loom) unterliegen deren eigenen Datenschutzbestimmungen. Fragen: aiandbusinessgrowth@ai-at.eu.

## Anhang A — Code-Snippet (Teil B)

Das ist das Snippet für Teil B — finde den Bug, fixe ihn, kritisiere kurz. (Auch als Datei: [`code-review/snippet.py`](./code-review/snippet.py).) Das Snippet ist eine **vereinfachte Illustration** — nicht der Code aus deinem PoC.

```python
"""
score_municipalities: berechnet ein gewichtetes Standort-Ranking.

Nimmt für jede Gemeinde vier Signale entgegen (Demografie, POI-Dichte, Mietindex, ÖV)
und gibt einen gewichteten Gesamt-Score zurück.

Jedes Signal wird mit seinem Gewicht multipliziert, die Ergebnisse werden summiert.
Die Gewichte sind so kalibriert, dass sie gemeinsam 1.0 ergeben und jedes Signal
proportional zu seiner Wichtigkeit beiträgt.

Args:
    municipalities: Liste von Dicts mit Felder demographics_score, poi_score,
                    rent_score, transit_score (je ein numerischer Wert pro Gemeinde)
    weights: Dict mit Gewichten für jedes Signal (Summe = 1.0)

Returns:
    Sortierte Liste von (gemeinde_name, gesamt_score) Tuples, absteigend.
"""

from typing import Any


def score_municipalities(
    municipalities: list[dict[str, Any]],
    weights: dict[str, float] | None = None,
) -> list[tuple[str, float]]:
    if weights is None:
        weights = {
            "demographics_score": 0.30,
            "poi_score": 0.25,
            "rent_score": 0.30,
            "transit_score": 0.15,
        }

    results = []
    for m in municipalities:
        total = 0.0
        for signal, weight in weights.items():
            total += m[signal] * weight
        results.append((m["gemeinde"], total))

    results.sort(key=lambda x: x[1], reverse=True)
    return results


# ---------------------------------------------------------------------------
# Demo
# ---------------------------------------------------------------------------

municipalities = [
    {
        "gemeinde": "Wien (7., Neubau)",
        "demographics_score": 0.42,   # Anteil 18–34-Jährige
        "poi_score": 8.7,             # POI-Dichte (0–10)
        "rent_score": 22.0,           # Mietindex in EUR/m²
        "transit_score": 9.5,         # ÖV-Score (0–10)
    },
    {
        "gemeinde": "Graz (Innere Stadt)",
        "demographics_score": 0.38,
        "poi_score": 7.4,
        "rent_score": 14.5,
        "transit_score": 8.2,
    },
    {
        "gemeinde": "Klagenfurt (Innenstadt)",
        "demographics_score": 0.31,
        "poi_score": 5.9,
        "rent_score": 11.8,
        "transit_score": 6.5,
    },
]

ranking = score_municipalities(municipalities)

print("Standort-Ranking:")
for rang, (gemeinde, score) in enumerate(ranking, 1):
    print(f"  {rang}. {gemeinde}: {score:.3f}")
```
