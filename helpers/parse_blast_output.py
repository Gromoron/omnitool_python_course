def parse_blast_output(input_fasta):
    descriptions = []
    in_table = False

    with open(input_fasta, "r", encoding="utf-8") as file:
        for line in file:
            if "Sequences producing significant alignments:" in line:
                in_table = True
                continue

            if not in_table:
                continue

            line = line.strip()
            if not line or line.startswith("Description"):
                continue

            if "No hits found" not in line:
                description, _score, _evalue = line.rsplit(None, 2)
                descriptions.append(description)

            in_table = False

    return descriptions
