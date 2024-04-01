import json

if __name__ == "__main__":
    number_list = [63, 69, 79, 80, 86, 88, 96, 105, 106, 111, 115, 117, 122, 126, 127, 131, 133]

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
        if d["number"] not in number_list:
            continue
        a, b, c = d["author"]["login"], d["headRepository"]["name"], d["headRefName"]
        f.write(f"git remote add {a} git@github.com:{a}/{b}.git\n")
        f.write(f"git fetch {a}\n")
        f.write(f"git merge --no-edit {a}/{c}\n")
        f.write("\n")
    f.close()