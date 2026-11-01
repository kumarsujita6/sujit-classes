# -*- coding: utf-8 -*-
"""Assembles all Chapter 5 parts into the master study note file."""

import os
import sys

# Ensure current dir is in path
current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.insert(0, current_dir)

from ch5_styles_head import STYLES_HEAD_CONTENT
from ch5_section1 import SECTION1_CONTENT
from ch5_section2a import SECTION2A_CONTENT
from ch5_section2b import SECTION2B_CONTENT
from ch5_section3 import SECTION3_CONTENT
from ch5_section4a import SECTION4A_CONTENT
from ch5_section4b import SECTION4B_CONTENT
from ch5_section5 import SECTION5_CONTENT
from ch5_section6_footer import SECTION6_FOOTER_CONTENT

target_path = os.path.abspath(os.path.join(current_dir, '..', '..', 'english', 'class7', 'math-ch5-parallel-and-intersecting-lines.html'))

full_content = (
    STYLES_HEAD_CONTENT +
    SECTION1_CONTENT +
    SECTION2A_CONTENT +
    SECTION2B_CONTENT +
    SECTION3_CONTENT +
    SECTION4A_CONTENT +
    SECTION4B_CONTENT +
    SECTION5_CONTENT +
    SECTION6_FOOTER_CONTENT
)

with open(target_path, 'w', encoding='utf-8') as f:
    f.write(full_content)

file_size = os.path.getsize(target_path)
print(f"Successfully generated: {target_path}")
print(f"File size: {file_size} bytes ({file_size / 1024:.2f} KB)")
