import sys

if sys.version_info >= (3, 0):
    from .diff_match_patch import diff_match_patch, patch_obj, __author__, __doc__
else:
    from .diff_match_patch_py2 import diff_match_patch, patch_obj, __author__, __doc__

__version__ = "20181111"
__packager__ = "John Reese (john@noswap.com)"
