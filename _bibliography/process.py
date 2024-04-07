# with open("papers.bib", "r") as f:
#     lines = f.readlines()
#     output = []
#     for line in lines:
#         output.append(line)
#         if "@" in line:
#             output.append("  bibtex_show={true},\n")
#     with open("papers_new.bib", "w") as f:
#         f.writelines(output)

with open("papers.bib", "r") as f:
    lines = f.readlines()
    flag = True
    name = ""
    for line in lines:
        if "@" in line:
            name = line
        elif "author" in line or "editor" in line:
            if flag == True:
                print(name)
                a = input()
            if flag == False:
                flag = True
        elif "bibtex_show" in line:
            if flag == False:
                print(name)
                a = input()
            else:
                flag = False