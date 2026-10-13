def convert_multiline_fasta_to_oneline(input_fasta, output_fasta):
    current_header = None
    seq_parts = []

    with open (input_fasta, "r", encoding = "utf-8") as input:
        for line in input:
            line = line.strip()
            if not line:
                continue  
            if line.startswith(">"):
                if current_header is not None:
                    yield current_header, "".join(seq_parts)
                current_header = line
                seq_parts = []
            else:
                seq_parts.append(line) 
        if current_header is not None:
            yield current_header, "".join(seq_parts)
 








   for each fasta sequence starting with >:
    if space in (input_fasta):
        remove the space symbols
     else:
        continue
    with open (output_fasta), "w" as out_file