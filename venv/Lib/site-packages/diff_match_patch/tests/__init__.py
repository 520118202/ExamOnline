import sys

if sys.version_info >= (3, 0):
    from .diff_match_patch_test import DiffTest, MatchTest, PatchTest
else:
    from .diff_match_patch_test_py2 import DiffTest, MatchTest, PatchTest
