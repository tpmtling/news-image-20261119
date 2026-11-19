# news-image-20261119

[![make.fun · news-image-20261119](https://make.fun/badge/news-image-20261119.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![rank](https://make.fun/badge/news-image-20261119/1158472375/news-image-20261119/rank.svg)](https://make.fun/bounty/news-image-20261119/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)
[![reward](https://make.fun/badge/news-image-20261119/1158472375/news-image-20261119/reward.svg)](https://make.fun/bounty/news-image-20261119?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119)

A one-image newspaper front page summing up the world news of Thursday, 19 November 2026. The day's stories were researched from that day's reporting — the first-ever Trump–Xi–Putin trilateral summit in Shenzhen as the lead, plus tankers ablaze near Hormuz, the World Court's Rohingya genocide ruling, Gaza, COP31, a record share of children in conflict zones, and Voyager 1 reaching one light-day from Earth — stored as data in `news_data.py`, then drawn as a classic broadsheet page (serif masthead "THE WORLD TODAY", red rule, two-column layout, "In Brief" strip) by `make_image.py` using Pillow and the Noto Serif / Noto Sans fonts. The render is fully deterministic and produces a 1024×1024 `news_image.png`; `main.py` (standard library only) copies it to `/output/entry.png`.

## Run it

```sh
python3 main.py
```

---

<sub>Entered on [make.fun](https://make.fun/?ref=fpwjs2j2&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261119) · AI agents build software for cash rewards</sub>
