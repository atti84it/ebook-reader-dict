import pytest

from scripts import utils


@pytest.mark.parametrize(
    "wikicode, expected",
    [
        ("", ""),
        ("{{}}", ""),
        ("{{absol}}", "<i>(Absolument)</i>"),
        ("{{adj-indéf-avec-de}}", "<i>(Avec de)</i>"),
        ("{{agri|fr}}", "<i>(Agriculture)</i>"),
        ("{{antiq|fr}}", "<i>(Antiquité)</i>"),
        ("{{ancre|sens_sexe}}", ""),
        ("{{fchim|H|2|O}}", "H<sub>2</sub>O"),
        ("{{emploi|au passif}}", "<i>(Au passif)</i>"),
        ("{{au pluriel}}", "<i>(Au pluriel)</i>"),
        ("{{au singulier}}", "<i>(Au singulier)</i>"),
        ("{{BE|fr}}", "<i>(Belgique)</i>"),
        ("{{bioch|nocat}}", "<i>(Biochimie)</i>"),
        ("{{calque|la|fr}}", "latin"),
        (
            "{{calque|en|fr|mot=to date|sens=à ce jour}}",
            "anglais <i>to date</i> (« à ce jour »)",
        ),
        (
            "{{calque|sa|fr|mot=वज्रयान|tr=vajrayāna|sens=véhicule du diamant}}",
            "sanskrit वज्रयान, <i>vajrayāna</i> (« véhicule du diamant »)",
        ),
        ("{{cf|immortelle}}", "→ voir immortelle"),
        ("{{cf|lang=fr|faire}}", "→ voir faire"),
        ("{{couleur|#B0F2B6}}", "[RGB #B0F2B6]"),
        ("{{couleur | #B0F2B6}}", "[RGB #B0F2B6]"),
        ("du XX{{e}} siècle", "du XX<sup>e</sup> siècle"),
        ("[[J·K-1|'''J·K{{e|-1}}''']]", "<b>J·K<sup>-1</sup></b>"),
        ("{{élec|fr}}", "<i>(Électricité)</i>"),
        ("{{étyl|grc|fr}}", "grec ancien"),
        ("{{étyl|no|fr|mot=ski}}", "norvégien <i>ski</i>"),
        (
            "{{étyl|grc|fr|λόγος|lógos|étude|type=nom|lien=1}}",
            "grec ancien λόγος, <i>lógos</i> (« étude »)",
        ),
        ("{{finan|fr}}", "<i>(Finance)</i>"),
        (
            "''({{formatnum:-1000000}} à {{formatnum:-300000}} environ avant J.-C.)''",
            "<i>(-1 000 000 à -300 000 environ avant J.-C.)</i>",
        ),
        ("{{FR|fr}}", "<i>(France)</i>"),
        ("{{géom|fr}}", "<i>(Géométrie)</i>"),
        ("{{graphe|fr}}", "<i>(Théorie des graphes)</i>"),
        ("{{improprement|fr}}", "<i>(Usage critiqué)</i>"),
        ("{{info|fr}}", "<i>(Informatique)</i>"),
        ("{{juri|fr}}", "<i>(Droit)</i>"),
        ("{{langage SMS}} ", "<i>(Langage SMS)</i>"),
        ("{{lien|étrange|fr}}", "étrange"),
        ("{{lien|D{{e}}}}", "D<sup>e</sup>"),
        ("{{ling|fr}}", "<i>(Linguistique)</i>"),
        ("{{in|5}}", "<sub>5</sub>"),
        ("{{math|fr}}", "<i>(Mathématiques)</i>"),
        ("{{mélio|fr}}", "<i>(Mélioratif)</i>"),
        ("{{méton|fr}}", "<i>(Par métonymie)</i>"),
        ("{{métrol|nocat=1}}", "<i>(Métrologie)</i>"),
        (
            "{{nom w pc|Aldous|Huxley}}",
            "Aldous <span style='font-variant:small-caps'>Huxley</span>",
        ),
        ("{{nom w pc|L. L. Zamenhof}}", "L. L. Zamenhof"),
        (
            "{{nom w pc|Théodore Agrippa d’|Aubigné|'=oui}}",
            "Théodore Agrippa d’<span style='font-variant:small-caps'>Aubigné</span>",
        ),
        ("{{moderne}}", "<i>(Moderne)</i>"),
        ("{{néol|fr}}", "<i>(Néologisme)</i>"),
        ("{{nombre romain|12}}", "XII"),
        ("{{nombre romain|19}}", "XIX"),
        ("{{par ext}} ou {{figuré|fr}}", "<i>(Par extension)</i> ou <i>(Figuré)</i>"),
        ("{{part}}", "<i>(En particulier)</i>"),
        ("{{pronl|fr}}", "<i>(Pronominal)</i>"),
        ("{{QC|fr}}", "<i>(Québec)</i>"),
        ("{{région}}", "<i>(Régionalisme)</i>"),
        ("{{région|Lorraine et Dauphiné}}", "<i>(Lorraine et Dauphiné)</i>"),
        ("{{réf}}", ""),
        ("{{siècle|XVI}}", "<i>(XVI<sup>e</sup> siècle)</i>"),
        (
            "{{siècle|XVIII|XIX}}",
            "<i>(XVIII<sup>e</sup> siècle - XIX<sup>e</sup> siècle)</i>",
        ),
        ("{{siècle2|XIX}}", "XIXème"),
        ("{{sport|fr}}", "<i>(Sport)</i>"),
        ("{{sport|fr|collectif}}", "<i>(Sport collectif)</i>"),
        ("{{superlatif de|petit|fr}}", "Superlatif de petit"),
        ("{{term|au {{f}}}}", "<i>(Au <i>féminin</i>)</i>"),
        (
            "{{term|Avec un mot négatif}} Presque.",
            "<i>(Avec un mot négatif)</i> Presque.",
        ),
        ("{{term|Avec ''[[le#fr-art-déf|le]]''}}", "<i>(Avec <i>le</i>)</i>"),
        (
            "{{term|Avec un [[déterminant]] défini comme ''[[le#fr-art-déf|le]]'', ''[[mon#fr-adj-pos|mon]]'', etc., et avec un adjectif ou un adverbe}}",  # noqa
            "<i>(Avec un déterminant défini comme <i>le</i>, <i>mon</i>, etc., et avec un adjectif ou un adverbe)</i>",
        ),
        ("{{term|ne … guère que}}", "<i>(Ne … guère que)</i>"),
        ("{{term|Souvent en [[apposition]]}}", "<i>(Souvent en apposition)</i>"),
        (
            "{{term|Du {{nombre romain|12}}{{e}} au {{nombre romain|19}}{{e}} siècle}} Béni.",
            "<i>(Du XII<sup>e</sup> au XIX<sup>e</sup> siècle)</i> Béni.",
        ),
        (
            "{{term|Du XII{{e}} au XIX{{e}} siècle}}",
            "<i>(Du XII<sup>e</sup> au XIX<sup>e</sup> siècle)</i>",
        ),
        ("{{trad+|conv|Sitophilus granarius}}", "Sitophilus granarius"),
        ("{{term|{{antonomase|fr|m=1}}}}", "<i>(Antonomase)</i>"),
        ("{{unités|fr}}", "<i>(Métrologie)</i>"),
        ("{{unité|92|%}}", "92%"),
        ("{{ws|Bible Segond 1910/Livre de Daniel|Livre de Daniel}}", "Livre de Daniel"),
        (
            "{{ws|Les Grenouilles qui demandent un Roi}}",
            "Les Grenouilles qui demandent un Roi",
        ),
        ("{{wsp|Panthera pardus|''Panthera pardus''}}", "<i>Panthera pardus</i>"),
        ("{{wsp|Brassicaceae}}", "Brassicaceae"),
    ],
)
def test_clean_template(wikicode, expected):
    assert utils.clean("foo", wikicode) == expected
