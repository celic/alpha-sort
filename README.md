alpha-sort
==========

Problem description
-------------------

You are working for a large company that routinely gets the following dataset: a list of `n` (with `n ≥ 1bil`) positive integers and wants to test whether or not the given list is `α-approximately-sorted`. An `α-approximately-sorted` list (for `0 ≤ α ≤ 1`) is a list of integers where at least `αn` of its entries are sorted. It is best to consider cases where `α` is close to 1, (i.e. `α ≥ .9`).

Your manager wants an algorithm that given the above input, outputs `YES` or `NO`, thus answering the question whether the list is `α-approximately-sorted` or not. He absolutely does not want an `O(n)` solution; there is not enough time for that. He is willing to accept an output that is not always correct (i.e., he can live with some failure probability). This immediately brings to your mind happy memories from the Randomized Algorithms course that you took at Rensselaer, and you go back to your drawing board, your books, and your notes, in order to design a randomized algorithm that takes as input a list of integers `a1, a2, . . . , an` and outputs `YES/NO` to indicate whether the list is `α-approximately-sorted` or not.

It is beneficial to provide a theoretical analysis and an experimental one (ONLY ON DATA OF SIZE `1bil` OR LARGER). 

