from glob import glob


lines = []
with open("README.md", "r") as f:
    for line in f.readlines():
        if "## Solved" in line:
            break
        lines.append(line)

problems = []
for filename in glob("problems/*.py"):
    number, name = filename.replace("problems/", "").split("_", 1)
    name = name.replace(".py", "")
    url = "https://leetcode.com/problems/{}".format(name.replace("_", "-"))
    name = name.replace("_", " ").title()
    problems.append((number, name, filename, url))

problems = sorted(problems, key=lambda x: int(x[0]))
lines.append(f"## Solved ({len(problems)})\n\n")
for number, name, filename, url in problems:
    lines.append(f" - [x] [{number}. {name}]({url}) - [:page_with_curl:]({filename})\n")

# for i in problems:
    # print(i)

with open("README.md", "w") as f:
    for line in lines:
        f.write(line)

