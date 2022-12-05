from collections import deque
from typing import Self, Optional, Deque

from solutions.base_solution import BaseSolver


class Path:

    def __init__(self, n_removed_blocks: int, keep: set[int], dispose: set[int], n_removed_chars: int):
        self.keep: set[int] = keep
        self.dispose: set[int] = dispose
        self.n_removed_chars = n_removed_chars
        self.n_removed_blocks = n_removed_blocks

    def __eq__(self, other: Self) -> bool:
        return self.keep == other.keep and self.dispose == other.dispose

    def is_valid(self, n_blocks: int, max_n_blocks: int = 3) -> bool:
        return (n_blocks - self.n_removed_blocks) <= max_n_blocks

    def combine_paths(self, other: Self) -> Optional[Self]:
        if self == other:
            return None

        if self.keep.isdisjoint(other.dispose) and self.dispose.isdisjoint(other.keep):
            return Path(
                n_removed_blocks=self.n_removed_blocks + other.n_removed_blocks,
                keep=self.keep.union(other.keep),
                dispose=self.dispose.union(other.dispose),
                n_removed_chars=self.n_removed_chars + other.n_removed_chars,
            )
        return None


def tree_search(paths: list[Path], n_blocks: int, max_num_blocks: int) -> int:
    """
    Combine compatible paths before searching
    Return the number of removed characters
    """
    queue: Deque[Path] = deque()
    best_path: Optional[Path] = None

    # Check overlaps
    compatible_paths: dict[frozenset[int], set[int]] = {}

    for i, p in enumerate(paths):
        overlaps = set()
        for j, sp in enumerate(paths):
            if i == j:
                continue
            if not p.combine_paths(sp):
                overlaps.add(j)

        frozen: frozenset = frozenset(overlaps)
        if frozen in compatible_paths:
            compatible_paths[frozen].add(i)
        else:
            compatible_paths[frozen] = {i}

    # Combine compatible paths
    for _, paths_idxs in compatible_paths.items():
        new_path: Path = paths[paths_idxs.pop()]

        while paths_idxs:
            new_path.combine_paths(paths[paths_idxs.pop()])

        queue.append(new_path)

    while queue:
        path: Path = queue.pop()

        if path.is_valid(n_blocks=n_blocks, max_n_blocks=max_num_blocks):
            if not best_path or path.n_removed_chars < best_path.n_removed_chars:
                best_path = path
        else:
            if best_path and path.n_removed_chars >= best_path.n_removed_chars:
                continue

            # Add children
            children: list[Path] = []
            for p in queue:
                if new := path.combine_paths(p):
                    children.append(new)

            queue.extendleft(children)

    return best_path.n_removed_chars


class PathIntersectionSolver(BaseSolver):
    MAX_NUM_BLOCKS: int = 3

    @classmethod
    def solve(cls, s: str) -> int:
        l: list[Path] = []
        path_to_rm_idxs: dict[str, set[int]] = {}
        path_n_blocks: dict[str, int] = {}  # n of blocks when the path was opened
        path_to_keep_idxs: dict[str, set[int]] = {}
        next_path_to_close: Optional[Path] = None
        blocks: list[str] = []

        current_char: str = ''

        for i, c in enumerate(s):
            if not current_char:
                blocks.append(c)
                current_char = c
                path_to_rm_idxs[c] = set()
                path_to_keep_idxs[c] = {i}
                path_n_blocks[c] = len(blocks)

            elif current_char != c:
                current_char = c

                # Create add block
                blocks.append(c)

                # Close path
                if next_path_to_close:
                    l.append(next_path_to_close)

                # Prepare next path to be closed
                if c in path_to_rm_idxs:
                    path_to_keep_idxs[c].add(i)

                    next_path_to_close = Path(
                        n_removed_blocks=len(blocks) - path_n_blocks[c],
                        keep=path_to_keep_idxs[c],
                        dispose=path_to_rm_idxs[c],
                        n_removed_chars=len(path_to_rm_idxs[c])
                    )
                    del path_to_rm_idxs[c]
                    del path_n_blocks[c]
                    del path_to_keep_idxs[c]

                # Open new path
                path_to_rm_idxs[c] = set()
                path_to_keep_idxs[c] = {i}
                path_n_blocks[c] = len(blocks)

            else:
                path_to_keep_idxs[c].add(i)
                if next_path_to_close:
                    next_path_to_close.keep.add(i)

                # Grow previous block
                blocks[-1] = f"{blocks[-1]}{c}"

            # Update paths with "to remove" idxs
            for char, pri in path_to_rm_idxs.items():
                if char != c:
                    pri.add(i)

        del path_to_rm_idxs
        del path_n_blocks
        del path_to_keep_idxs

        # Close last block if it was the same character
        if next_path_to_close and current_char == s[-1]:
            l.append(next_path_to_close)

        if len(blocks) <= cls.MAX_NUM_BLOCKS:
            return len(s)

        if l:
            # Tree search combinations
            return len(s) - tree_search(paths=l, max_num_blocks=cls.MAX_NUM_BLOCKS, n_blocks=len(blocks))

        # remove smaller blocks
        return sum(len(b) for b in sorted(blocks, key=len, reverse=True)[:3])

        return len(s)
