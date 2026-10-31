# -*- coding: utf-8 -*-
"""
Assembler Script for Class 8 Mathematics Chapter 10 Master Study Note
Proportional Reasoning - 2 (NCERT NEP code: hegp110)
Target: english/class8/math-ch10-proportional-reasoning-2.html
"""

import os
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.insert(0, current_dir)

from styles import get_head_and_styles
from sec1_blueprint import get_section_1
from sec2_concepts import get_section_2
from sec3_tables import get_section_3
from sec4_ncert_part1 import get_section_4_part1
from sec4_ncert_part2 import get_section_4_part2
from sec5_exam_part1 import get_section_5_part1
from sec5_exam_part2 import get_section_5_part2
from sec6_traps import get_section_6

def assemble():
    html_parts = [
        get_head_and_styles(),
        get_section_1(),
        get_section_2(),
        get_section_3(),
        get_section_4_part1(),
        get_section_4_part2(),
        get_section_5_part1(),
        get_section_5_part2(),
        get_section_6()
    ]
    
    full_html = "".join(html_parts)
    
    # Path to target
    root_dir = os.path.dirname(os.path.dirname(current_dir))
    target_path = os.path.join(root_dir, "english", "class8", "math-ch10-proportional-reasoning-2.html")
    
    with open(target_path, "w", encoding="utf-8") as f:
        f.write(full_html)
        
    size_bytes = os.path.getsize(target_path)
    size_kb = size_bytes / 1024
    print(f"Generated: {target_path}")
    print(f"File Size: {size_bytes} bytes ({size_kb:.2f} KB)")
    
    if size_kb < 150:
        print(f"WARNING: File size {size_kb:.2f} KB is below the 150 KB floor!")
    else:
        print(f"SUCCESS: File size exceeds the 150 KB floor benchmark! ({size_kb:.2f} KB)")
        
    return size_kb

if __name__ == "__main__":
    assemble()
