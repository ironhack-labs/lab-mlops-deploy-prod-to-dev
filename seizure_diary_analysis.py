"""Analyse d'un journal de crises (donnees synthetiques).

Projet minimal servant de support au lab MLOps DEV -> PROD.

Ce que fait le script :
  1. genere un journal de crises synthetique reproductible (aucune donnee reelle) ;
  2. calcule quelques indicateurs utiles en unite de monitoring :
     frequence mensuelle, plus long intervalle sans crise, repartition horaire ;
  3. ecrit deux sorties dans ./outputs : un resume CSV et un graphique PNG.

Usage :
    python seizure_diary_analysis.py

Le script est deterministe (graine fixee) : deux executions produisent
exactement les memes chiffres. C'est ce qui permet au Gatekeeper de verifier
que l'environnement est correctement reproduit.
"""

from __future__ import annotations

import argparse
from pathlib import Path

import matplotlib

matplotlib.use("Agg")  # backend sans affichage : le script doit tourner sans interface
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

GRAINE = 42
DOSSIER_SORTIE = Path("outputs")


def generer_journal(n_crises: int = 120, jours: int = 365) -> pd.DataFrame:
    """Cree un journal de crises synthetique.

    Les crises sont plus frequentes la nuit et au petit matin, ce qui reproduit
    grossierement une distribution observee en pratique. Aucune donnee patient
    n'est utilisee.
    """
    rng = np.random.default_rng(GRAINE)

    debut = pd.Timestamp("2025-01-01")
    jour_de_crise = rng.integers(0, jours, size=n_crises)

    # Heures tirees d'un melange de deux modes : nuit (2h) et fin d'apres-midi (18h)
    mode_nuit = rng.random(n_crises) < 0.6
    heures = np.where(
        mode_nuit,
        rng.normal(2, 2.5, n_crises),
        rng.normal(18, 3.0, n_crises),
    ) % 24

    journal = pd.DataFrame({
        "horodatage": debut + pd.to_timedelta(jour_de_crise, unit="D")
                            + pd.to_timedelta(heures, unit="h"),
        "duree_s": np.clip(rng.normal(75, 30, n_crises), 10, None).round(0),
        "type": rng.choice(["focale", "focale_bilateralisee", "absence"],
                           size=n_crises, p=[0.6, 0.25, 0.15]),
    })

    return journal.sort_values("horodatage").reset_index(drop=True)


def calculer_indicateurs(journal: pd.DataFrame) -> pd.DataFrame:
    """Indicateurs synthetiques du journal."""
    duree_suivi_j = (journal["horodatage"].max() - journal["horodatage"].min()).days
    intervalles_j = journal["horodatage"].diff().dt.total_seconds() / 86400

    indicateurs = {
        "nb_crises": len(journal),
        "duree_suivi_jours": duree_suivi_j,
        "frequence_par_30j": round(len(journal) / duree_suivi_j * 30, 2),
        "duree_moyenne_s": round(journal["duree_s"].mean(), 1),
        "duree_mediane_s": round(journal["duree_s"].median(), 1),
        "plus_long_intervalle_jours": round(intervalles_j.max(), 1),
        "part_nocturnes_0h_6h": round(
            journal["horodatage"].dt.hour.between(0, 5).mean(), 3
        ),
    }
    for type_crise, part in journal["type"].value_counts(normalize=True).items():
        indicateurs[f"part_{type_crise}"] = round(part, 3)

    return pd.DataFrame([indicateurs]).T.rename(columns={0: "valeur"})


def tracer(journal: pd.DataFrame, chemin: Path) -> None:
    """Deux vues : repartition horaire et frequence mensuelle."""
    fig, ax = plt.subplots(1, 2, figsize=(11, 4))

    ax[0].hist(journal["horodatage"].dt.hour, bins=24, range=(0, 24),
               edgecolor="white")
    ax[0].set_xlabel("heure de la journee")
    ax[0].set_ylabel("nombre de crises")
    ax[0].set_title("Repartition horaire")
    ax[0].set_xticks(range(0, 25, 3))

    par_mois = journal.set_index("horodatage").resample("ME").size()
    ax[1].plot(par_mois.index, par_mois.values, marker="o")
    ax[1].set_ylabel("crises par mois")
    ax[1].set_title("Frequence mensuelle")
    ax[1].tick_params(axis="x", rotation=45)
    ax[1].grid(alpha=0.3)

    fig.tight_layout()
    fig.savefig(chemin, dpi=120)
    plt.close(fig)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--crises", type=int, default=120,
                        help="nombre de crises a generer (defaut : 120)")
    args = parser.parse_args()

    DOSSIER_SORTIE.mkdir(exist_ok=True)

    journal = generer_journal(n_crises=args.crises)
    journal.to_csv(DOSSIER_SORTIE / "journal_crises.csv", index=False)

    indicateurs = calculer_indicateurs(journal)
    indicateurs.to_csv(DOSSIER_SORTIE / "indicateurs.csv")

    tracer(journal, DOSSIER_SORTIE / "figures.png")

    print(f"{len(journal)} crises generees\n")
    print(indicateurs.to_string())
    print(f"\nSorties ecrites dans {DOSSIER_SORTIE.resolve()} :")
    for fichier in sorted(DOSSIER_SORTIE.iterdir()):
        print(f"   - {fichier.name}")


if __name__ == "__main__":
    main()
