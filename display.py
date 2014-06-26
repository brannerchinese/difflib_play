#! /usr/bin/env python
# display.py
# David Prager Branner
# 20140625

class Display():
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.values = []
        self.formatted = []

    def display_terminal(self):
        a = self.a
        b = self.b
        for value, nextvalue in zip(self.values, self.values[1:]):
            # Omit duplicates (mainly due to lack of junk).
            if value == nextvalue:
                continue
            # Retrieve values of matching indices and length.
            i, j, k = value
            i_end = i + k + 1
            j_end = j + k + 1
            # Prepare pairs of sentences.
            self.formatted.append(
                    (''.join([str(self.a[0:i]), '\033[5;41;32m',
                        str(self.a[i:i_end]), '\033[0m', str(self.a[i_end:])]),
                    ''.join([str(self.b[0:j]), '\033[5;41;32m',
                        str(self.b[j:j_end]), '\033[0m', str(self.b[j_end:])]))
                    )
        for item in self.formatted:
            print('{}\n{}\n\n)'.format(*item))
