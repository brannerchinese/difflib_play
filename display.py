#! /usr/bin/env python
# display.py
# David Prager Branner
# 20140625

class Display():
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.values = []
        self.formattedvalues = []
        self.blocks = []
        self.formattedblocks = []

    def display_values_terminal(self):
        a = self.a
        b = self.b
        last_value = None
        for value in self.values:
            if value == last_value:
                continue
            last_value = value
            # Retrieve values of matching indices and length.
            i, j, k = value
            i_end = i + k
            j_end = j + k
            # Prepare pairs of sentences.
            self.formattedvalues.append(
                    (''.join([str(self.a[0:i]), '\033[5;41;32m',
                        str(self.a[i:i_end]), '\033[0m', str(self.a[i_end:])]),
                    ''.join([str(self.b[0:j]), '\033[5;41;32m',
                        str(self.b[j:j_end]), '\033[0m', str(self.b[j_end:])]))
                    )
        for item in self.formattedvalues:
            print('{}\n{}\n\n)'.format(*item))

    def display_blocks_terminal(self):
        print('\n\nBlocks:\b')
        a = self.a
        b = self.b
        for block in self.blocks:
            # Retrieve values of matching indices and length.
            i, j, k = block
            i_end = i + k
            j_end = j + k
            # Prepare pairs of sentences.
            self.formattedblocks.append(
                    (''.join([str(self.a[0:i]), '\033[5;41;32m',
                        str(self.a[i:i_end]), '\033[0m', str(self.a[i_end:])]),
                    ''.join([str(self.b[0:j]), '\033[5;41;32m',
                        str(self.b[j:j_end]), '\033[0m', str(self.b[j_end:])]))
                    )
        for item in self.formattedblocks:
            print('{}\n{}\n\n)'.format(*item))
