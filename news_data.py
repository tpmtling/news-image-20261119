"""Stories for Thursday, 19 November 2026.

Researched on the day from the outlets named in each ``source`` field.
The lead story is flagged with ``lead=True``; the rest run in two
columns, and ``briefs`` fill the strip along the foot of the page.
"""

STORIES = [
    {
        "kicker": "WORLD DIPLOMACY",
        "headline": "Trump, Xi and Putin Hold First-Ever Trilateral Summit in Shenzhen",
        "deck": (
            "Donald Trump, Xi Jinping and Vladimir Putin met in Shenzhen on "
            "Thursday for the first three-way summit of the US, Chinese and "
            "Russian leaders. Xi greeted Trump at the airport and called ties "
            "with Russia a source of stability; Ukraine, Iran, energy and "
            "nuclear arms control topped the agenda."
        ),
        "source": "The Hindu / The New York Times / SBS News",
        "lead": True,
    },
    {
        "kicker": "ENERGY & SHIPPING",
        "headline": "Three Oil Tankers Catch Fire After Hitting Mines Near Hormuz",
        "deck": (
            "Iran said three oil tankers caught fire after striking mines "
            "east of the Strait of Hormuz, the chokepoint for a fifth of the "
            "world's oil. Tehran's Revolutionary Guard said passage through "
            "the waterway must now be coordinated with Iran."
        ),
        "source": "NDTV World",
        "lead": False,
    },
    {
        "kicker": "WORLD COURT",
        "headline": "World Court Rules on Myanmar's Alleged Rohingya Genocide",
        "deck": (
            "Judges at The Hague delivered their verdict in the genocide "
            "case over Myanmar's 2017 crackdown. In Bangladesh, 1.2 million "
            "Rohingya in the Cox's Bazar camps followed a judgment read out "
            "over 90 minutes."
        ),
        "source": "NDTV World / BBC via NewsBites",
        "lead": False,
    },
    {
        "kicker": "MIDDLE EAST",
        "headline": "Israeli Tanks Advance Across Gaza Cease-Fire Line",
        "deck": (
            "Israeli forces launched a rare ground incursion beyond Gaza's "
            "Yellow Line as Australia, Canada, Italy and Britain jointly "
            "urged Israel to let aid reach the flooded enclave without "
            "restriction."
        ),
        "source": "BBC via NewsBites / The Paris Eye",
        "lead": False,
    },
    {
        "kicker": "HUMANITY",
        "headline": "Record One in Four Children Now Live in Conflict Zones",
        "deck": (
            "Nearly one in four children worldwide now lives in a conflict "
            "zone, a record high, Save the Children reported on Thursday — "
            "the starkest measure yet of war's toll on the young."
        ),
        "source": "Save the Children via Scoop",
        "lead": False,
    },
    {
        "kicker": "CLIMATE — COP31",
        "headline": "At COP31, Rich Nations Fail to Meet Climate Finance Pledges",
        "deck": (
            "Wealthy countries were accused at COP31 of failing to meet the "
            "finance promises meant to help developing nations cope with a "
            "warming planet, as a new study warned nearly all coral reefs "
            "face extinction within 50 years."
        ),
        "source": "Global Climate and Health Alliance via Scoop / IUCN",
        "lead": False,
    },
    {
        "kicker": "SCIENCE",
        "headline": "Voyager 1 Reaches One Light-Day From Earth",
        "deck": (
            "NASA's Voyager 1, launched in 1977, was believed to have "
            "become the first human-made object one light-day from Earth — "
            "its radio signals now take a full 24 hours to arrive home."
        ),
        "source": "Science News / Jagran Josh",
        "lead": False,
    },
]

BRIEFS = [
    "ART — Van Gogh painting sells for a record $190.4m after a row over its Nazi-era history.",
    "EUROPE — EU proposes a €45bn loan for Ukraine, to be repaid once Russia pays reparations.",
    "CULTURE — Grand Theft Auto VI launches worldwide, ending a 13-year wait for gamers.",
    "ENERGY — Bangladesh switches on power from its first, Russian-built nuclear plant.",
]
