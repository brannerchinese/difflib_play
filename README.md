## Difflib Play

Visualize the workings of the `difflib` module.

 1. This is a Python3 program.

 1. At the moment, the only functionality visualized is that of two functions in `difflib.SequenceMatcher`, and visualization takes place only in the terminal window. To see, first set some pairs of sequences to values for which differencing will be useful:

        ```
L1 = 'Where T is the total number of elements in both sequences'
L2 = 'T is the total elements in and'
L3 = 'elemen elemen elements'
L4 = 'element'
L5 = L1.split()
L6 = L2.split()
        ```

   Import this program and then run some diff-calculations:

        ```
import diff_seq_match_play as S
S.SequenceMatcher(None, L1, L2).ratio()
S.SequenceMatcher(None, L3, L4).ratio()
S.SequenceMatcher(None, L5, L6).ratio()
        ```

   The program will display the successive matches of elements of the sequences L1 and L2 (etc). Then it will display the final blocks found. Both displays will have the matching portions shown in the context of the full, original sequences.

[end]
