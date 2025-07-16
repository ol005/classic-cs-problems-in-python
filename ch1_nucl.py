# string to bit gene nucleotide compression
import sys

class CompressedGene:
    def __init__(self, gene: str) -> None:
        self._compress(gene)
    
    def _compress(self, gene: str) -> None:
        self.bit_string: int = 1
        for nucleotide in gene.upper():
            self.bit_string <<= 2
            if nucleotide == 'A':
                self.bit_string |= 0b00
            elif nucleotide == 'C':
                self.bit_string |= 0b01
            elif nucleotide == 'G':
                self.bit_string |= 0b10
            elif nucleotide == 'T':
                self.bit_string |= 0b11
            else:
                raise ValueError(f"Invalid Nucleaotide:{nucleotide}")

    def decompress(self) -> str:
        gene: str = ""
        for i in range(0, self.bit_string.bit_length()-1, 2):
            bits: int = self.bit_string >> i & 0b11
            if bits == 0b00:
                gene += 'A'
            elif bits == 0b01:
                gene += 'C'
            elif bits == 0b10:
                gene += 'G'
            elif bits == 0b11:
                gene += 'T'
            else:
                raise ValueError(f"Invalid bits: {bits}")
        return gene[::-1]

    def __str__(self) -> str:
        return self.decompress()
    
txt = "TAGGGATTAACCGTTATATATATATAGCCATGGATCGATTATATAGGGATTAACCGTTATATATATATAGCCATGGATCGATTATA" * 100
gene = CompressedGene(txt)
print(f"size of str: {sys.getsizeof(txt)}")
#print(bin(gene.bit_string))
print(f"size of bit str: {sys.getsizeof(gene.bit_string)}")
#print(gene)