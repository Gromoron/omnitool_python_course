import os


def is_in_boundsds(value, bounds):
    """
    Проверяет, числа указанные как границы. Если это одно число то считает автоматически его верхней границей, а 0 - нижней.
    """
    if isinstance(bounds, (int, float)):
        lower, upper = 0, bounds
    else:
        lower, upper = bounds
    return lower <= value <= upper


def check_gc(sequence, gc_bounds):
    """
    Проверяет что GC состав находится в заданных рамках или меньше определенного значения.
    """
    if not sequence:
        return False

    seq_upper = sequence.upper()
    gc_count = seq_upper.count("G") + seq_upper.count("C")
    gc_percent = (gc_count / len(sequence)) * 100

    return is_in_bounds(gc_percent, gc_bounds)


def check_length(sequence, length_bounds):
    """
    Проверяет, входит ли длина последовательности рида в заданный диапазон. по дефолту - 2**32
    """
    return is_in_bounds(len(sequence), length_bounds)


def check_quality(quality_str, quality_threshold):
    """
    Проверяет, не ниже ли среднее Phred33 качество рида заданного порога.
    """
    if not quality_str:
        return False

    # Таблица ASCII -> Phred33 (ord(char) - 33)
    total_quality = sum(ord(char) - 33 for char in quality_str)
    mean_quality = total_quality / len(quality_str)

    return mean_quality >= quality_threshold


def read_fastq(file_path):
    """
     читает FASTQ файл по 4 строки (1 рид)
    Использует yield, чтобы не загружать весь файл в память.

    """
    with open(file_path, "r", encoding="utf-8") as file:
        while True:
            header = file.readline().strip()
            if not header:
                break
            seq = file.readline().strip()
            comment = file.readline().strip()
            qual = file.readline().strip()
            yield header, seq, comment, qual


def write_fastq(file_handle, header, seq, comment, qual):
    """
    Записывает все 4 строки от одного рида в файл
    """
    file_handle.write(f"{header}\n{seq}\n{comment}\n{qual}\n")
