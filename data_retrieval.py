from Bio import Entrez, SeqIO

def set_ncbi_email(email):
    Entrez.email = email

def search_db(db_name, term, rettype='gb'):
    handle = Entrez.esearch(db=db_name, term=term, ret_type=rettype)
    rec_list = Entrez.read(handle)
    if rec_list['RetMax'] < rec_list['Count']:
        handle = Entrez.esearch(db=db_name, term=term, retmax=rec_list['Count'])
        rec_list = Entrez.read(handle)
    id_list = rec_list['IdList']
    records = Entrez.efetch(db=db_name, id=id_list, rettype='gb')
    parsed_records = list(SeqIO.parse(records, 'gb'))
    return parsed_records

def extract_record_features(record):
    for feature in rec.features:
        if feature.type == 'gene':
            print(feature.qualifiers['gene'])
        elif feature.type == 'exon':
            loc = feature.location
            print(loc.start, loc.end, loc.strand)
        else:
            print('not processed:\n%s' % feature)

def extract_annotations(record):
    for name, value in rec.annotations.items():
        print('%s=%s' % (name, value))

def extract_sequence(gene_name, record):
    for rec in recs:
        if rec.name == gene_name:
            break
    return rec.seq

if __name__ == '__main__':
    set_ncbi_email('david.f.stein@gmail.com')
    recs = search_db('nucleotide', 'CRT[Gene Name] AND "Plasmodium falciparum"[Organism]')
    for rec in recs:
        if rec.name == 'KM288867':
            break
    # print(rec.name)
    # print(rec.description)
    # extract_record_features(rec)
    # print('\n')
    # extract_annotations(rec)
    sequence = extract_sequence(rec)
    # print(len(sequence))
    return sequence
