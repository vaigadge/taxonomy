all open PRs with `triage-approved`
```
bash scripts/fetch-prs.sh
python scripts/gen-rc-bash.py
bash make-rc.sh
```

PRs with given PR numbers
```
bash scripts/fetch-prs.sh --all
python scripts/gen-rc-bash.py --prs 63,69,79,80,86,88,96,105,106,111,115,117,122,126,127,131,133
bash make-rc.sh
```