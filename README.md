# URL Hunter

URL Hunter is a tool for detecting patterns in a HTTP response of multiple URLs which resides within a file.
It uses YARA rules for detecting a pattern.

## Use Cases
This tool can be used for running YARA rules on the returned html from a http request
- eml files with URLs attached
- html files that has many urls attached

## Dependency
- python 3+
- pip

Run dependency.sh/dependency.ps1 to install the followings
- `requests` python package
- `yara-python` python package

If it fails, please use pip to install manually

## Usage
<b>Running the hunt:</b>
1. Put files in ./inputs folder
2. Run with `./python hunt.py`
3. Results are stored in ./results folder

<b>Editing rules:</b>
YARA rules can be added in ./rules/RULES.yara

### Good Luck Hunting