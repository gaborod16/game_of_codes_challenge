from typing import Type

from solutions.path_intersection_solution import PathIntersectionSolver


class TestThreeLetterBlock:
    solver: Type[PathIntersectionSolver] = PathIntersectionSolver

    def test_strings_two_unique_chars_0(self) -> None:
        s: str = 'aaaaaaaaaaaaaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb'
        assert self.solver.solve(s) == 71

    def test_strings_two_unique_chars_1(self) -> None:
        s: str = 'aaabbbaaa'
        assert self.solver.solve(s) == 9

    def test_strings_two_unique_chars_2(self) -> None:
        s: str = 'aaabbbaaabbb'
        assert self.solver.solve(s) == 9

    def test_strings_two_unique_chars_3(self) -> None:
        s: str = 'aaabaaabbb'
        assert self.solver.solve(s) == 9

    def test_strings_two_unique_chars_4(self) -> None:
        s: str = 'aabbbbaabbbbaa'
        assert self.solver.solve(s) == 12

    def test_strings_two_unique_chars_5(self) -> None:
        s: str = 'aaaaaabbbabbbbbbb'
        assert self.solver.solve(s) == 16

    def test_strings_two_unique_chars_6(self) -> None:
        s: str = 'aabbababaa'
        assert self.solver.solve(s) == 8

    def test_strings_two_unique_chars_7(self) -> None:
        s: str = 'baaaaabbaaaaab'
        assert self.solver.solve(s) == 12

    def test_strings_two_unique_chars_8(self) -> None:
        s: str = 'ababababababababa'
        assert self.solver.solve(s) == 10

    def test_strings_several_chars_0(self) -> None:
        s: str = 'abcd'
        assert self.solver.solve(s) == 3

    def test_strings_several_chars_1(self) -> None:
        s: str = 'aaaabbbcccddefgggggg'
        assert self.solver.solve(s) == 13

    def test_strings_several_chars_2(self) -> None:
        s: str = 'abcdefghijkl'
        assert self.solver.solve(s) == 3

    def test_strings_several_chars_3(self) -> None:
        s: str = 'aaabbdcbdccabb'
        assert self.solver.solve(s) == 8

    def test_strings_several_chars_4(self) -> None:
        s: str = 'aaabacbba'
        assert self.solver.solve(s) == 7

    def test_strings_several_chars_5(self) -> None:
        s: str = 'aabxbaba'
        assert self.solver.solve(s) == 6

    def test_strings_several_chars_6(self) -> None:
        s: str = 'aaabbcabbaa'
        assert self.solver.solve(s) == 9

    def test_strings_extreme_1(self) -> None:
        s: str = 'fourth example test'
        assert self.solver.solve(s) == 5

    def test_strings_extreme_2(self) -> None:
        s: str = 'aabababaaabsbsbabsbdbajsjdjbawbdbabwjajdbwajdbwajbsbdbwajdwbasbbdwjabsdbjwabdsbababajwdb'
        assert self.solver.solve(s) > 15
