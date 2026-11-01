# -*- coding: utf-8 -*-
"""
Module: assemble_power_play.py
Assembles all modules into english/class8/math-ch2-power-play.html and checks file size.
"""

import os
import sys

from ch2_styles_head import get_head_and_hero
from ch2_section1 import get_section_1
from ch2_section2 import get_section_2
from ch2_section3 import get_section_3
from ch2_section4 import get_section_4
from ch2_section5 import get_section_5
from ch2_section6_footer import get_section_6_and_footer

def assemble():
    target_path = os.path.join("english", "class8", "math-ch2-power-play.html")
    
    parts = [
        get_head_and_hero(),
        get_section_1(),
        get_section_2(),
        get_section_3(),
        get_section_4(),
        get_section_5(),
        get_section_6_and_footer()
    ]
    
    full_html = "\n".join(parts)
    
    with open(target_path, "w", encoding="utf-8") as f:
        f.write(full_html)
        
    size_bytes = os.path.getsize(target_path)
    size_kb = size_bytes / 1024.0
    print(f"Successfully generated {target_path}")
    print(f"File size: {size_bytes} bytes ({size_kb:.2f} KB)")
    
    if size_kb < 150.0:
        print(f"WARNING: File size {size_kb:.2f} KB is below the 150 KB floor!")
    else:
        print(f"SUCCESS: File size exceeds the 150 KB floor benchmark!")

if __name__ == "__main__":
    assemble()
