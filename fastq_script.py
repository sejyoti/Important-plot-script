#!/home/sejyoti/miniconda3/bin/python
from Bio import Entrez, SeqIO

# Define the list of accession IDs
accession_ids = [
    'HM854261', 'GU994860', 'GU994860', 'HM854261', 'FJ390481', 'HM854261',
    'EU855200', 'MH712970.1', 'MK880647.1', 'KM822751.1', 'KF424713.1', 'MH301320.1',
    'ICX502834.1', 'KX503027.1', 'MT761800.1', 'MG973003.1', 'NR_161141.1', 'KR085914.1',
    'CP013236.1', 'MH855790.1', 'MH865730.1', 'AB649025.1', 'KR857378.1', 'MH790889.1',
    'MH864914.1', 'MH858769.1', 'KT369945.1', 'KR085837.1', 'JQ422166.1', 'MF555712.1',
    'MK726114.1', 'NR_044431.1', 'MF467855.1', 'MK587683.1', 'DQ792502.1', 'MF467855.1',
    'LC085212.1', 'CP033231.1', 'LC514968.1', 'MH859482.1', 'EF641871.1', 'KU877334',
    'KF021891', 'KF021901', 'KF021902', 'KF021907', 'MK608363.1', 'MH819728.1', 'MK608706.1',
    'MK719896.1', 'MK719898.1', 'MK719897.1', 'MK608775.1', 'MK608841.1', 'MK719894.1',
    'MK611551.1', 'MK611552.1', 'MK719892.1', 'MK719893.1', 'MK611456.1', 'MK611559.1',
    'MK611560.1', 'MK719895.1', 'KX462780', 'KX462781', 'KX462782', 'KX788166', 'MN251628',
    'MN211551', 'MN108025', 'MK386888', 'KP793145', 'NR_074945', 'KJ466897', 'JN681794',
    'JN681816', 'JN681810', 'JN681774', 'OP811462', 'OP811485', 'MN889031', 'MF034061',
    'MF034062', 'MF034063', 'MF034064', 'MF034065', 'MF034066', 'MF034067', 'MF034068',
    'MF034069', 'MF034070', 'MF034071', 'MF034072', 'HQ023428', 'KC683896', 'HE793513',
    'EU307933', 'LN846832', 'KM215730', 'GU082482', 'EF463077', 'EF070205', 'HM101166',
    'HQ023428', 'MF399051', 'MN334776', 'NR121703'
]

# Set your email
Entrez.email = "sejyotichakraborty@gmail.com"

# Fetch the sequences using the accession IDs
fetch_handle = Entrez.efetch(db="nucleotide", id=accession_ids, rettype="fasta", retmode="text")
sequences = SeqIO.parse(fetch_handle, "fasta")

# Process the retrieved sequences
for sequence in sequences:
    print(sequence.id)
    print(sequence.seq)

# Close the fetch handle
fetch_handle.close()

