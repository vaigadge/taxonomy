#!/usr/bin/evn python

import argparse, json

TAXONOMY_REPO_URL = "https://github.com/instruct-lab/taxonomy"

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--fp-in', type=str, default='tmp/pr-list.json', help='Path to the input JSON file'
    )
    parser.add_argument(
        '--fp-out', type=str, default='tmp/make-rc.sh', help='Path to the output Bash file'
    )
    parser.add_argument(
        '--prs', type=str, help='Comma-separated list of PR numbers'
    )
    args = parser.parse_args()

    with open(args.fp_in, 'r') as f:
        data = json.load(f)

    number_list = []
    if args.prs:
        number_list = [int(num) for num in args.prs.split(',')]

    if number_list:
        data = [d for d in data if d["number"] in number_list]

    f = open(args.fp_out, "w")
    f.write("#!/usr/bin/env bash\n")
    f.write("\n")
    f.write(f"echo 'making branch with {len(data)} candidate PRs'")
    f.write("\n")
    f.write("git checkout -b merge-candidates\n")
    f.write("\n")
    for d in data:
        pr_number = d["number"]
        gh_login = d["author"]["login"]
        repo_name = d["headRepository"]["name"]
        ref_name = d["headRefName"]
        f.write(f"echo 'merging PR #{pr_number} ({TAXONOMY_REPO_URL}/pull/{pr_number})'\n")
        f.write(f"git remote add {gh_login} git@github.com:{gh_login}/{repo_name}.git\n")
        f.write(f"git fetch {gh_login}\n")
        f.write(f"git merge --no-edit {gh_login}/{ref_name}\n")
        f.write("\n")
    f.close()

if __name__ == "__main__":
    main()