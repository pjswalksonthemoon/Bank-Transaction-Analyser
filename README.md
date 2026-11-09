# Transaction Description Categoriser

A small Python command-line tool that groups transaction descriptions into Food, Transport, Entertainment, Shopping, Bills, Income, or Other. It uses keyword rules and Python's standard library; it does not read bank files.

## Run

Requires Python 3.11 or newer. From this repository's folder:

```sh
python "Work Experience Code.py"
```

Choose 1 to categorise a description, 2 to list categories, or 3 to exit. Matching ignores letter case and extra spacing. Descriptions without a known keyword return `Other`.

## Test

```sh
python -m unittest discover -s tests -v
```

## Limitations

The first matching keyword determines the category. These rules can misclassify ambiguous merchants; review results before relying on them for a budget. CSV import and machine learning are possible future additions.
