import pytest

from scripts import utils


@pytest.mark.parametrize(
    "wikicode, expected",
    [
        ("", ""),
        ("{{absol}}", "(Absolument)"),
        ("{{adj-indéf-avec-de}}", "(Avec de)"),
        ("{{agri|fr}}", "(Agriculture)"),
        ("{{antiq|fr}}", "(Antiquité)"),
        ("{{ancre|sens_sexe}}", ""),
        ("{{emploi|au passif}}", "(Au passif)"),
        ("{{au pluriel}}", "(Au pluriel)"),
        ("{{au singulier}}", "(Au singulier)"),
        ("{{BE|fr}}", "(Belgique)"),
        ("{{bioch|nocat}}", "(Biochimie)"),
        ("{{couleur|#B0F2B6}}", "(Code RGB #B0F2B6)"),
        ("du XX{{e}} siècle", "du XX<sup>e</sup> siècle"),
        ("{{élec|fr}}", "(Électricité)"),
        ("{{finan|fr}}", "(Finance)"),
        ("{{FR|fr}}", "(France)"),
        ("{{géom|fr}}", "(Géométrie)"),
        ("{{graphe|fr}}", "(Théorie des graphes)"),
        ("{{improprement|fr}}", "(Usage critiqué)"),
        ("{{info|fr}}", "(Informatique)"),
        ("{{juri|fr}}", "(Droit)"),
        ("{{langage SMS}} ", "(Langage SMS)"),
        ("{{lien|étrange|fr}}", "étrange"),
        ("{{lien|D{{e}}}}", "D<sup>e</sup>"),
        ("{{ling|fr}}", "(Linguistique)"),
        ("{{math|fr}}", "(Mathématiques)"),
        ("{{mélio|fr}}", "(Mélioratif)"),
        ("{{méton|fr}}", "(Par métonymie)"),
        ("{{métrol|nocat=1}}", "(Métrologie)"),
        ("{{moderne}}", "(Moderne)"),
        ("{{néol|fr}}", "(Néologisme)"),
        ("{{nombre romain|12}}", "XII"),
        ("{{nombre romain|19}}", "XIX"),
        ("{{par ext}} ou {{figuré|fr}}", "(Par extension) ou (Figuré)"),
        ("{{part}}", "(En particulier)"),
        ("{{pronl|fr}}", "(Pronominal)"),
        ("{{QC|fr}}", "(Québec)"),
        ("{{région}}", "(Régionalisme)"),
        ("{{réf}}", ""),
        ("{{siècle2|XIX}}", "XIXème"),
        ("{{term|Du {{nombre romain|12}}{{e}} au {{nombre romain|19}}{{e}} siècle}}", "(Du XII<sup>e</sup> au XIX<sup>e</sup> siècle)"),
        ("{{term|Du XII{{e}} au XIX{{e}} siècle}}", "(Du XII<sup>e</sup> au XIX<sup>e</sup> siècle)"),
        ("{{unités|fr}}", "(Métrologie)"),
    ],
)
def test_clean_template(wikicode, expected):
    assert utils.clean(wikicode) == expected
