from glob import glob

lines = []
with open("README.md", "r") as f:
    for line in f.readlines():
        if "## Solved" in line:
            break
        lines.append(line)
lines.append("## Solved\n\n")
problems = []
for filename in glob("problems/*.py"):
    number, name = filename.replace("problems/", "").split("_", 1)
    name = name.replace(".py", "")
    url = "https://leetcode.com/problems/{}".format(name.replace("_", "-"))
    name = name.replace("_", " ").title()
    problems.append((number, name, filename, url))

problems = sorted(problems, key=lambda x: x[0])

for problem in problems:

    lines.append(
        " - [x] [{}]({}) - [:page_with_curl:]({})\n".format(
            problem[1], problem[3], problem[2]
        )
    )

with open("README.md", "w") as f:

    for line in lines:
        # print(line)
        f.write(line)
