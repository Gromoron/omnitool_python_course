# omnitool_python_course

A small collection of bioinformatics tools written in Python:

- **`filter_fastq`** – filter FASTQ reads by length, GC content and mean quality
- **`convert_multiline_fasta_to_oneline`** – convert a multiline FASTA file into a single-line FASTA
- **`parse_blast_output`** – extract the best-hit descriptions from a BLAST text report and save them sorted alphabetically

## Requirements

- Python 3.10 or newer
- No any other packages except mine

## Installation

```bash
git clone https://github.com/Gromoron/omnitool_python_course.git
cd omnitool_python_course
```

## Project structure

```
omnitool_python_course/
├── main.py        # public functions of the toolkit
├── helpers/       # helper modules used by main.py
└── README.md
```

## Usage

`main.py` does not have a command-line interface yet, so the functions are used from Python. Run Python from the project folder (so that `main` and `helpers` can be imported):

```bash
python
```

```python
from main import (
    filter_fastq,
    convert_multiline_fasta_to_oneline,
    parse_blast_output,
)
```

### 1. Filter FASTQ reads

```python
filter_fastq(
    "reads.fastq",
    "reads_filtered.fastq",
    gc_bounds=(40, 60),
    length_bounds=(50, 300),
    quality_threshold=20,
)
```

| Argument | Default | Description |
|---|---|---|
| `input_fastq` | – | path to the input FASTQ file |
| `output_fastq` | – | name of the output file |
| `gc_bounds` | `(0, 100)` | allowed GC content range, in % |
| `length_bounds` | `(0, 2**32)` | allowed read length range |
| `quality_threshold` | `0` | minimum mean read quality |

The reads that passed all checks are written to `filtered/reads_filtered.fastq`. The `filtered/` folder is created automatically.

### 2. Convert multiline FASTA to single-line FASTA

```python
convert_multiline_fasta_to_oneline("genes.fasta", "genes_oneline.fasta")
```

If `output_fasta` is not given, the result is saved next to the input file with the `_singlelined.fasta` suffix (for `genes.fasta` it will be `genes_singlelined.fasta`).

### 3. Parse a BLAST report

```python
parse_blast_output("blast_report.txt", "best_hits.txt")
```

The input is a BLAST report in plain text format. For every query, the description of the best hit is taken from the *"Sequences producing significant alignments"* table. Queries with no hits are skipped. The descriptions are sorted alphabetically and written to the output file, one per line.

## Notes

- Files are processed line by line, so large files do not have to fit into memory.
- If you run into import errors, make sure you start Python from the project root folder.
