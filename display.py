#! /usr/bin/env python
# display.py
# David Prager Branner
# 20140625

"""Display the in-progress workings of the Difflib module."""

class Display():
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.values = []
        self.formattedvalues = []
        self.blocks = []
        self.formattedblocks = []

    def display_values_terminal(self):
        """Display matching blocks in the terminal as they accumulate."""
        a = self.a
        b = self.b
        last_value = None
        for value in self.values:
            if value == last_value:
                continue
            last_value = value
            # Retrieve values of matching indices and length.
            i, j, k = value
            # Prepare pairs of sentences.
            self.formattedvalues.append(
                    (''.join([str(a[0:i]), '\033[5;41;32m',
                        str(a[i:i+k]), '\033[0m', str(a[i+k:])]),
                    ''.join([str(b[0:j]), '\033[5;41;32m',
                        str(b[j:j+k]), '\033[0m', str(b[j+k:])]))
                    )
        for item in self.formattedvalues:
            print('{}\n{}\n\n)'.format(*item))

    def display_blocks_terminal(self):
        """Display final matching blocks in the terminal."""
        print('\n\nBlocks:\b')
        a = self.a
        b = self.b
        for block in self.blocks:
            # Retrieve values of matching indices and length.
            i, j, k = block
            # Prepare pairs of sentences.
            self.formattedblocks.append(
                    (''.join([str(a[0:i]), '\033[5;41;32m',
                        str(a[i:i+k]), '\033[0m', str(a[i+k:])]),
                    ''.join([str(b[0:j]), '\033[5;41;32m',
                        str(b[j:j+k]), '\033[0m', str(b[j+k:])]))
                    )
        for item in self.formattedblocks:
            print('{}\n{}\n\n)'.format(*item))
