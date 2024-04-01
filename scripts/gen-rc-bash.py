#!/usr/bin/evn python

import argparse, json

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

    number_list = []
    if args.prs:
        number_list = [int(num) for num in args.prs.split(',')]

    with open(args.fp_in, 'r') as f:
        data = json.load(f)

    f = open(args.fp_out, "w")
    f.write("#!/usr/bin/env bash\n")
    f.write("\n")
    f.write(f'echo "making branch with {len(data)} candidate PRs"')
    f.write("\n")
    f.write("git checkout -b merge-candidates\n")
    f.write("\n")
    for d in data:
        if number_list and d["number"] not in number_list:
            continue
        a, b, c = d["author"]["login"], d["headRepository"]["name"], d["headRefName"]
        f.write(f"git remote add {a} git@github.com:{a}/{b}.git\n")
        f.write(f"git fetch {a}\n")
        f.write(f"git merge --no-edit {a}/{c}\n")
        f.write("\n")
    f.close()

if __name__ == "__main__":
    main()