with open("papers.bib", "r") as f:
    lines = f.readlines()
    output = []
    for line in lines:
        output.append(line)
        if "@" in line:
            output.append("  bibtex_show={true},\n")
    with open("papers_new.bib", "w") as f:
        f.writelines(output)