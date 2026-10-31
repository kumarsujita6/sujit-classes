# -*- coding: utf-8 -*-
"""Assembles all 8 parts into the master file for Class 8 Science Chapter 11."""

import os
import sys

# Add directory to path
sys.path.insert(0, os.path.dirname(__file__))

from part1_head_css import PART1_CONTENT
from part2_section1 import PART2_CONTENT
from part3_section2a import PART3_CONTENT
from part4_section2b import PART4_CONTENT
from part5_section3 import PART5_CONTENT
from part6_section4 import PART6_CONTENT
from part7_section5 import PART7_CONTENT
from part8_section6 import PART8_CONTENT

target_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'english', 'class8', 'sci-ch11-keeping-time-with-the-skies.html'))

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
print(f"Successfully generated: {target_path}")
print(f"File size: {file_size} bytes ({file_size / 1024:.2f} KB)")
if file_size >= 153600:
    print(f"SUCCESS: File size ({file_size / 1024:.2f} KB) surpasses the 150 KB floor!")
else:
    print(f"WARNING: File size ({file_size / 1024:.2f} KB) is below 150 KB. Needs expansion.")
