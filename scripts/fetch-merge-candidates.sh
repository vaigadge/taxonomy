#!/usr/bin/evn bash

gh pr --repo instruct-lab/taxonomy list --limit 1000 --state all --json number,author,headRepository,headRefName > merge-candidates.json
