# bump_version.py
"""
bump_version(name, width=2)
- If filename already ends with "_vNN" (NN = digits) just before the extension, increment NN by 1.
- Otherwise append "_v01" before the extension.
- Zero-pad to at least `width` digits (default 2). If number is larger, keep full digits (e.g. 100 -> "100").
- Preserves extension, including common multi-extensions like .tar.gz.
"""
import re
import os

KNOWN_MULTI_EXTS = ['.tar.gz', '.tar.bz2', '.tar.xz', '.tar.Z', '.tar.lz']

def _split_preserve_multiext(name: str):
    low = name.lower()
    for me in KNOWN_MULTI_EXTS:
        if low.endswith(me):
            return name[:-len(me)], name[-len(me):]
    return os.path.splitext(name)

def bump_version(name: str, width: int = 2) -> str:
    """
    Bumps filename version.
    Examples:
      report_v1.csv -> report_v02.csv
      summary.csv    -> summary_v01.csv
      log_v09.txt    -> log_v10.txt
    """
    base, ext = _split_preserve_multiext(name)
    # Match suffix like "..._v123" (capture the actual 'v' to preserve case)
    m = re.match(r'^(.*)_(v)(\d+)$', base, re.IGNORECASE)
    if m:
        root = m.group(1)
        v_char = m.group(2)  # preserve original case ("v" or "V")
        n = int(m.group(3))
        new_n = n + 1
        new_num_str = str(new_n).zfill(width)
        return f"{root}_{v_char}{new_num_str}{ext}"
    else:
        return f"{base}_v{str(1).zfill(width)}{ext}"

# Quick CLI if you can't run pytest
if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        for fn in sys.argv[1:]:
            print(f"{fn} -> {bump_version(fn)}")
    else:
        # INSERT_YOUR_CODE
        # Take input from the console, bump version, and print result
        inp = input("Enter filename(s) separated by spaces: ").strip()
        if inp:
            for fn in inp.split():
                print(f"{fn} -> {bump_version(fn)}")
                # INSERT_YOUR_CODE
