import json

if __name__ == "__main__":
    with open('merge-candidates.json', 'r') as file:
        data = json.load(file)

    f = open("make-local-merge-branch.sh", "w")
    f.write("#!/usr/bin/evn bash\n")
    f.write("\n")
    f.write(f'echo "making branch with {len(data)} candidate PRs"')
    f.write("\n")
    f.write("git checkout -b merge-candidates\n")
    f.write("\n")
    for d in data:
        a, b, c = d["author"]["login"], d["headRepository"]["name"], d["headRefName"]
        f.write(f"git remote add {a} git@github.com:{a}/{b}.git\n")
        f.write(f"git fetch {a}\n")
        f.write(f"git merge --no-edit {a}/{c}\n")
        f.write("\n")
    f.close()