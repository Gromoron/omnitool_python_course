def parse_blast_output(input_fasta):
    annot = []
    seq_header = False

    with open(input_fasta, "r", encoding="utf-8") as file:
        for line in file:
            if "Sequences producing significant alignments:" in line:
                seq_header = True
                continue

            # Если есть заголовок, то ищем первую строку с последовательностью
            if seq_header:
                clean_line = line.strip()

                # Пропускаем пустые строки или строку заголовка таблицы 'Description'
                if not clean_line or clean_line.startswith("Description"):
                    continue

                # пропустить все строки если не было совпадений
                if "No hits found" in clean_line:
                    seq_header = False
                    continue

                # Первая содержательная строка — это лучшее совпадение!
                # В выводе BLAST описание занимает первые ~66-67 символов строки,
                # после чего идут пробелы и колонки Score / E-value.
                # Срезаем первые 66 символов (или берем всю строку, если она короче):
                desc = clean_line[:66].strip()
                descriptions.append(desc)

                # Сбрасываем флаг: для текущего Query лучший хит найден,
                # ждем следующего 'Sequences producing significant alignments:'
                seq_header = False

    return descriptions
