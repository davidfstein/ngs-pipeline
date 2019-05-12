from Bio import Entrez, SeqIO
import data_retrieval

def write_record_to_disk(sequence, extension='fa'):
    with open(sequence.name + '.' + extension, 'w+') as file:
        file.write(sequence)

def read_record_from_file(path, type='fasta'):
    with open(path, 'r') as file:
        record = SeqIO.parse(file, type)
        return record

if __name__ == '__main__':
    data_retrieval.set_ncbi_email('david.f.stein@gmail.com')
    records = search_db('nucleotide', '["NM_002299"]', 'fasta')
    response = data_retrieval.extract_sequence(, records)
    sequence = SeqIO.read(response, 'fasta')
