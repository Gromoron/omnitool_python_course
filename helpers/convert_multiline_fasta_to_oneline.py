def parse_multiline_fasta(input_fasta):
    """
    Генератор: читает FASTA-файл и по очереди отдаёт пары (header, sequence),
    где sequence - вся последовательность записи одной строкой.
    Пустые строки пропускаются.
    """
    header = None
    parts = []

    with open(input_fasta, encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            if line.startswith(">"):
                if header is not None:
                    yield header, "".join(parts)
                header = line
                parts = []
            else:
                parts.append(line)

    if header is not None:
        yield header, "".join(parts)
