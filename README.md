# game_of_codes_challenge
Challenge attempt - Game of Codes
Read description of the problem in this [**link**](https://app.codility.com/programmers/task/three_letters_blocks/).

## Approach

### Trivial cases:

Count how many blocks we have.
If we have less than the maximum number of blocks.
- Trivial answer, we return `len(s)`.

Check if a block's character is also the representative in another block.
If there are no repeated characters among blocks.
- Trivial answer, we return the sum the number of elements in the `[max_number_blocks]` biggest blocks.

### Non-trivial cases

I implemented a path intersection solution.

What I do is to look for "paths".
A "path" is basically a range between one block to another block that shares the same character.

It consists on: 
- Set of indexes to keep (indexes of the blocks with the same character)
- Set of indexes to remove (indexes of any other block in between)
- Number of blocks removed (by applying this path)
- Number of characters removed (by applying this path)

With this information I am able to combine compatible paths and find the optimal combinations of paths that maximises the `len(s)`.

**Example**: 
```python
# AABBAABBAA -> Three paths
#
# Process:
#
# AA  BB  AA  BB  AA
# ^   ^   ^   ^   ^
# B1  B2  B3  B4  B5
# 
# Three paths are found:
#
# Path 1 -> (B1 -> B3)
# Path 2 -> (B2 -> B4)
# Path 3 -> (B3 -> B5)
#
# Note: A path from B1 -> B5 is not gathered since it will not be worth it to delete B3 in the middle.
```

I ran through the combinations using a *Breath-First-Search* algorithm. 
**However**, the combinations grow with a complexity of `O(2**k)`.

### Conclusion

- The `len(s)` can be big, as long as the number of paths is small
- The solution struggles when the number of paths is high. In other words, when many blocks share the same character.