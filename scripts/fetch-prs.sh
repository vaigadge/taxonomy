#!/usr/bin/evn bash

ALL=$1

if [ "$ALL" == "--all" ]
then
    filter="--state all"
else
    filter="--label 'triage-approved'"
fi

eval "gh --repo instruct-lab/taxonomy pr list --limit 10000 $filter --json number,author,headRepository,headRefName > tmp/pr-list.json"