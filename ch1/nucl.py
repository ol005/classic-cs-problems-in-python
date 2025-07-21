# string to bit gene nucleotide compression
# ch1 1.2
import sys
from typing import Generator

# implementing wrapper around int to handle bitstrings
# question 2 in 1.7 excercises
class BitString:
    def __init__(self, start: int) -> None:
        self._bit_string: int = start
    
    def lshift(self, n: int) -> None:
        self._bit_string <<= n
    
    def append(self, bits: int) -> None:
        self._bit_string |= bits

    def __sizeof__(self) -> int:
        return sys.getsizeof(self._bit_string)
    
    def __len__(self) -> int:
        return self._bit_string.bit_length()-1
    
    def __iter__(self) -> Generator[int, None, None]:
        for i in range(0, len(self), 2):
            yield self._bit_string >> i & 0b11

    def __getitem__(self, index: int) -> int:
        if index < 0 or index > len(self):
            raise IndexError
        return self._bit_string >> index & 0b11

    def __str__(self) -> str:
        return bin(self._bit_string)
    
#rewrite compressed gene to use BitString class
class CompressedGene:
    def __init__(self, gene: str) -> None:
        self._compress(gene)
    
    def get_bstr(self) -> BitString:
        return self._b_str
    
    def _compress(self, gene: str) -> None:
        self._b_str: BitString = BitString(1)
        for nucleotide in gene.upper():
            self._b_str.lshift(2)
            if nucleotide == 'A':
                self._b_str.append(0b00)
            elif nucleotide == 'C':
                self._b_str.append(0b01)
            elif nucleotide == 'G':
               self._b_str.append(0b10)
            elif nucleotide == 'T':
              self._b_str.append(0b11)
            else:
                raise ValueError(f"Invalid Nucleaotide:{nucleotide}")

    def decompress(self) -> str:
        gene: str = ""
        for bits in self._b_str:
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
print(f"size of bit str: {sys.getsizeof(gene.get_bstr())}")
print(gene)