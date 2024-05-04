import heapq 
from collections import defaultdict, Counter 


class Node:
    def __init__(self, char=None, freq=None):
        self.char = char
        self.freq = freq 
        self.left = None 
        self.right = None 

    def __lt__(self, other):
        return self.freq < other.freq
    

def huffman_encoding(text):
    freq_counter = Counter(text)
    print(freq_counter)

    min_heap = [Node(char, freq) for char, freq in freq_counter.items()]
    heapq.heapify(min_heap)

    # construct huffman tree
    while len(min_heap)>1:
        left = heapq.heappop(min_heap)
        right = heapq.heappop(min_heap)
        merged = Node(freq=left.freq+right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(min_heap, merged)
    
    root = min_heap[0]
    return root


huffman_codes = {}
def generate_codes(node, code=''):
    if node:
        if node.char:
            huffman_codes[node.char] = code 
        generate_codes(node.left, code+'0')
        generate_codes(node.right, code+'1')



def huffman_decoding(encoded_text, huffman_codes_dict):
    inverted_huffman_codes = {code: char for char, code in huffman_codes_dict.items()}

    decoded_text = ''
    code = ''

    for bit in encoded_text:
        code += bit
        if code in inverted_huffman_codes:
            decoded_text += inverted_huffman_codes[code]
            code = ''

    return decoded_text

if __name__ == "__main__":
    text = "to ensure that the height of the resulting tree is minimized"

    root = huffman_encoding(text)
    generate_codes(root)
    print(huffman_codes)
    encoded_text = ''.join(huffman_codes[char] for char in text)
    print(encoded_text)
    print("Total Bits Required: ", len(encoded_text))

    print(huffman_decoding(encoded_text, huffman_codes))