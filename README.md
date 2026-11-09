# Transaction Description Categoriser

A Python command-line program for sorting transaction descriptions into Food, Transport, Entertainment, Shopping, Bills, Income, or Other. I made it as a small rules-based project; it does not read bank files or make changes to an account.

## Run it

Requires Python 3.11 or newer. From this folder:

```sh
python "Work Experience Code.py"
```

Choose **1** to enter a description, **2** to list categories, or **3** to exit. For example, `TESCO Express` returns `Food`. Matching ignores case and extra spaces. Unknown descriptions return `Other`.

## Test it

```sh
python -m unittest discover -s tests -v
```

GitHub Actions runs the tests on pushes and pull requests.

## How it works

`KEYWORD_MAPPING` holds the rules. The program checks keywords in order and returns the first match, so ambiguous merchant names may need a manual check.
