from __future__ import annotations
from enum import IntEnum, auto
from typing import TypeVar, Iterable, Sequence, Any, Protocol

class Nucleotide(IntEnum):
    A = auto()
    C = auto()
    G = auto()
    T = auto()

type Codon = tuple[Nucleotide, Nucleotide, Nucleotide]
type Gene = list[Codon]

T = TypeVar('T')
def linear_contains(iterable: Iterable[T], key: T) -> bool:
    for item in iterable:
        if item == key:
            return True
    return False



C = TypeVar("C", bound="Comparable")

class Comparable(Protocol):
    def __eq__(self, other: Any, /) -> bool:
        ...

    def __lt__(self: C, other: C, /) -> bool:
        ...

    def __gt__(self: C, other: C, /) -> bool:
        return (not self < other) and self != other

    def __le__(self: C, other: C, /) -> bool:
        return self < other or self == other

    def __ge__(self: C, other: C, /) -> bool:
        return not self < other




def str_to_gene(s: str) -> Gene:
    gene: Gene = []
    for i in range(0, len(s), 3):
        if i+2 >= len(s):
            return gene
        codon: Codon = (Nucleotide[s[i]], Nucleotide[s[i+1]], Nucleotide[s[i+2]])
        gene.append(codon)
    return gene



def binary_contains(sequence: Sequence[C], key: C) -> bool:
    low: int = 0
    high: int = len(sequence) - 1

    while low <= high:
        mid: int = (low + high) // 2
        if sequence[mid] < key:
            low = mid + 1
        elif sequence[mid] > key:
            high = mid-1
        else:
            return True
    return False


gene_str: str = "GGGGGCTCTCTAACGTACGTACGTACAAAAAAATTTATATATACCCTAGGATCCCTTT"
gene = str_to_gene(gene_str)
gene.sort()

ggg: Codon = (Nucleotide.G, Nucleotide.G, Nucleotide.G)
print(linear_contains(gene, ggg))
print(ggg in gene)
print(binary_contains(gene, ggg))

print(binary_contains([1, 2, 3, 4, 10, 20, 30, 55, 66, 77, 88, 99], 30))


