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
