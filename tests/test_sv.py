import pytest

from scripts.get import parse_word
from scripts.utils import clean


@pytest.mark.parametrize(
    "word, pronunciation, genre, definitions",
    [
        ("auto", "", "", ["automatisk; självgående", "automatiskt läge", "autostart"]),
        (
            "en",
            "eːn/, /ɛn/, /en",
            "",
            [
                "ungefär; omkring",
                "obestämd artikel singular utrum",
                "objektsform av <i>man</i>",
                "<i>(vardagligt, dialektalt)</i> man",
                "<i>(dialektalt)</i> honom, 'an",
                "syftar tillbaka på det tidigare nämnda substantivet",
                "<i>(träd)</i> en vintergrön barrväxt, en buske eller ett träd med tätt "
                "grenverk och vassa barr, av arten <i>Juniperus communis</i> inom släktet "
                "enar (<i>Juniperus</i>) och familjen cypressväxter (Cupressaceae)",
            ],
        ),
        (
            "-hörning",
            "",
            "",
            [
                "<i>(geometri, vardagligt)</i> <i>suffix för månghörningar</i>",
                "<i>suffix i ord som har med djurs horn att göra</i>",
            ],
        ),
        (
            "min",
            "mɪn",
            "",
            [
                "possessivt pronomen som indikerar ägande av eller tillhörighet till den talande (jag) om det ägda eller tillhörande är i ental och har n-genus; possessivt pronomen i första person singular med huvudordet i singular utrum",  # noqa
                "ovanstående i självständig form",
                "reflexivt possessivt pronomen som syftar tillbaka på och indikerar ägande av eller tillhörighet till subjektet om subjektet är i första person singular (jag) och om det ägda eller tillhörande är i ental och har n-genus; reflexivt possessivt pronomen i första person singular med huvudordet i singular utrum",  # noqa
                "känslouttryck i ansiktet",
                "<i>förkortning för</i> minut",
                "<i>förkortning för</i> minimum",
            ],
        ),
        ("og", "", "", []),
        (
            "sand",
            "sand",
            "",
            [
                "sten som blivit till små korn, antingen genom väder och vind eller på konstgjord väg",
                "<i>(geologi)</i> jordart med kornstorlek mellan 0,06 och 2 mm",
            ],
        ),
        (
            "svenska",
            "",
            "",
            [
                "nordiskt språk som talas i Sverige och Finland (officiellt i Finland)",
                "svensk kvinna",
            ],
        ),
    ],
)
def test_find_sections_and_definitions(word, pronunciation, genre, definitions, page):
    """Test the sections finder and definitions getter."""
    code = page(word, "sv")
    details = parse_word(word, code, "sv", force=True)
    assert pronunciation == details[0]
    assert genre == details[1]
    assert definitions == details[2]


@pytest.mark.parametrize(
    "wikicode, expected",
    [
        ("{{avledning|sv|mälta|ordform=prespart}}", "<i>presensparticip av</i> mälta"),
        ("{{tagg|historia}}", "<i>(historia)</i>"),
        (
            "{{tagg|kat=nedsättande|text=något nedsättande}}",
            "<i>(något nedsättande)</i>",
        ),
        ("{{uttal|sv|ipa=mɪn}}", "<b>uttal:</b> /mɪn/"),
        ("{{uttal|sv|ipa=eːn/, /ɛn/, /en}}", "<b>uttal:</b> /eːn/, /ɛn/, /en/"),
    ],
)
def test_clean_template(wikicode, expected):
    """Test templates handling."""
    assert clean("foo", wikicode, "sv") == expected
