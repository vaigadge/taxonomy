#!/usr/bin/evn bash

gh pr --repo instruct-lab/taxonomy list --label "triage-approved" --json author,headRepository,headRefName > merge-candidates.json
