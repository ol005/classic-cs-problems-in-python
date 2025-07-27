from enum import IntEnum, auto
from generic_search import linear_contains, binary_contains

class Nucleotide(IntEnum):
    A = auto()
    C = auto()
    G = auto()
    T = auto()

type Codon = tuple[Nucleotide, Nucleotide, Nucleotide]
type Gene = list[Codon]


def str_to_gene(s: str) -> Gene:
    gene: Gene = []
    for i in range(0, len(s), 3):
        if i+2 >= len(s):
            return gene
        codon: Codon = (Nucleotide[s[i]], Nucleotide[s[i+1]], Nucleotide[s[i+2]])
        gene.append(codon)
    return gene



gene_str: str = "ATCGGGGGCTCTCTAACGTACGTACGTACAAAAAAATTTATATATACCCTAGGATCCCTTT"
gene = str_to_gene(gene_str)
gene.sort()

ggg: Codon = (Nucleotide.G, Nucleotide.G, Nucleotide.G)
atc: Codon = (Nucleotide.A, Nucleotide.T, Nucleotide.C)

print(linear_contains(gene, ggg))
print(linear_contains(gene, atc))

print(binary_contains(gene, ggg))
print(binary_contains(gene, atc))

print(binary_contains([1, 2, 3, 4, 10, 20, 30, 55, 66, 77, 88, 99], 30))


