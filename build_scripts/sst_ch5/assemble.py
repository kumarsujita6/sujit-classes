# -*- coding: utf-8 -*-
"""
Assembles all 8 parts of Class 8 Social Science Chapter 5 Master Note:
Universal Franchise and India's Electoral System (NCERT NEP code: hess105).
Target: 'english/class8/sst-ch5-universal-franchise-and-indias-electoral-system.html'
Benchmark Floor: >= 150 KB.
"""

import sys
import os

from part1_header import PART1_CONTENT
from part2_section1 import PART2_CONTENT
from part3_section2a import PART3_CONTENT
from part4_section2b import PART4_CONTENT
from part5_section3 import PART5_CONTENT
from part6_section4 import PART6_CONTENT
from part7_section5 import PART7_CONTENT
from part8_section6 import PART8_CONTENT

target_path = os.path.abspath(os.path.join(
    os.path.dirname(__file__),
    '..', '..', 'english', 'class8',
    'sst-ch5-universal-franchise-and-indias-electoral-system.html'
))

full_content = (
    PART1_CONTENT +
    PART2_CONTENT +
    PART3_CONTENT +
    PART4_CONTENT +
    PART5_CONTENT +
    PART6_CONTENT +
    PART7_CONTENT +
    PART8_CONTENT
)

with open(target_path, 'w', encoding='utf-8') as f:
    f.write(full_content)

file_size = os.path.getsize(target_path)
size_kb = file_size / 1024
print(f"Successfully assembled master note at: {target_path}")
print(f"File Size: {file_size} bytes ({size_kb:.2f} KB)")

if size_kb < 150:
    print(f"FAILED GUARDRAIL: File size {size_kb:.2f} KB is below the mandatory 150 KB floor!")
    sys.exit(1)
else:
    print(f"PASSED GUARDRAIL: File size {size_kb:.2f} KB exceeds the mandatory 150 KB floor!")
