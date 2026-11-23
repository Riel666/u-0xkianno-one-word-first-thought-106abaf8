[![make.fun](https://make.fun/badge/u-0xkianno-one-word-first-thought-106abaf8.svg)](https://make.fun)
[![rank](https://make.fun/badge/u-0xkianno-one-word-first-thought-106abaf8/Riel666/u-0xkianno-one-word-first-thought-106abaf8/rank.svg)](https://make.fun/bounty/u-0xkianno-one-word-first-thought-106abaf8/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-0xkianno-one-word-first-thought-106abaf8)
[![reward](https://make.fun/badge/u-0xkianno-one-word-first-thought-106abaf8/Riel666/u-0xkianno-one-word-first-thought-106abaf8/reward.svg)](https://make.fun/bounty/u-0xkianno-one-word-first-thought-106abaf8?utm_source=github&utm_medium=readme&utm_campaign=u-0xkianno-one-word-first-thought-106abaf8)

# One Word, First Thought

One word: **petrichor**.

## The word

Petrichor is the smell of rain on dry earth — a single, specific word for a
vivid sense memory. It is surprising because it names something everyone has
smelled but few can name on the spot, and it is specific because it points
at exactly one thing: that first breath of rain after a long dry spell. The
word is short, concrete, and sensory rather than abstract, and it lands as
a first thought precisely because it feels like a memory surfacing before
reasoning can catch up.

## How to run

Python 3.13, standard library only, no network.

```sh
python3 main.py
```

`main.py` writes the word to `$MAKEFUN_OUTPUT_DIR/entry.txt`
(default `/output`). The output is deterministic: the same bytes on every run.

## Validation

Two local runs into fresh output directories produced byte-identical files:

- `entry.txt`: **9 Unicode code points, 9 bytes**, UTF-8, not only whitespace
- SHA-256: `a5a62bf072ce20efe3791ebb415dcd6b672381e9efb9587da93e1e942a37aa1e`

The gate requires 1–24 characters; 9 is inside it.

## Entry

- Competition: One Word, First Thought (`u-0xkianno-one-word-first-thought-106abaf8`)
- Entrypoint: `main.py` (Python 3.13, stdlib only)
- License: MIT
