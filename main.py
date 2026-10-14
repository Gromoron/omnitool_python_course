import os

from helpers.fastq import (
    read_fastq,
    write_fastq,
    check_gc,
    check_length,
    check_quality,
)
from helpers.convert_multiline_fasta_to_oneline import parse_multiline_fasta
from helpers.parse_blast_output import parse_blast_output as get_blast_descriptions


def filter_fastq(
    input_fastq,
    output_fastq,
    gc_bounds=(0, 100),
    length_bounds=(0, 2**32),
    quality_threshold=0,
):
    """
    Фильтрует FASTQ-последовательности на лету по длине, GC-составу и среднему качеству.
    Сохраняет прошедшие риды в папку filtered/ с именем output_fastq.
    """
    # Создаем папку filtered, если она еще не создана
    os.makedirs("filtered", exist_ok=True)
    output_path = os.path.join("filtered", output_fastq)

    # Записываем каждый рид по очереди, не перегружая память компьютера
    with open(output_path, "w", encoding="utf-8") as out_file:
        for header, seq, comment, qual in read_fastq(input_fastq):
            # Если какая-то проверка не пройдена, переходим к следующему риду
            if not check_length(seq, length_bounds):
                continue
            if not check_gc(seq, gc_bounds):
                continue
            if not check_quality(qual, quality_threshold):
                continue

            # Если все пройдено - записываем в файл
            write_fastq(out_file, header, seq, comment, qual)


def convert_multiline_fasta_to_oneline(input_fasta, output_fasta=None):
    """
    Конвертирует многострочный FASTA в однострочный.
    Если output_fasta не указан, создаёт файл с суффиксом 'singlelined.fasta'.
    """
    if output_fasta is None:
        base_name, _ = os.path.splitext(input_fasta)
        output_fasta = f"{base_name}singlelined.fasta"

    # Потоково записываем склеенные последовательности
    with open(output_fasta, "w", encoding="utf-8") as out_file:
        for header, sequence in parse_multiline_fasta(input_fasta):
            out_file.write(f"{header}\n{sequence}\n")


def parse_blast_output(input_file, output_file):
    """
    Читает txt-файл BLAST, извлекает описания лучших хитов для заданных query
    последовательностей, сортирует их по алфавиту и записывает в output_file.
    """
    descriptions = get_blast_descriptions(input_file)
    descriptions.sort()

    with open(output_file, "w", encoding="utf-8") as out:
        for desc in descriptions:
            out.write(f"{desc}\n")


# проверка запуска из терминала или же через Python script
if __name__ == "__main__":
    pass
