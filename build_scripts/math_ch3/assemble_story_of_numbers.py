# -*- coding: utf-8 -*-
"""
Module: assemble_story_of_numbers.py
Assembles all modules into english/class8/math-ch3-a-story-of-numbers.html
and validates that the file size strictly exceeds the 150 KB floor benchmark.
"""

import os
import sys

# Ensure current directory is in path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from ch3_styles_head import get_head_and_hero
from ch3_section1 import get_section_1
from ch3_section2 import get_section_2
from ch3_section3 import get_section_3
from ch3_section4 import get_section_4
from ch3_section5 import get_section_5
from ch3_section6_footer import get_section_6_and_footer

def assemble():
    base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    target_path = os.path.join(base_dir, "english", "class8", "math-ch3-a-story-of-numbers.html")
    
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
    print("=" * 60)
    print(f"Target File: {target_path}")
    print(f"Generated File Size: {size_bytes:,} bytes ({size_kb:.2f} KB)")
    print("=" * 60)
    
    if size_kb < 150.0:
        print(f"ERROR: File size {size_kb:.2f} KB is BELOW the strict 150 KB floor! Automatic rejection.")
        sys.exit(1)
    else:
        print(f"SUCCESS: File size {size_kb:.2f} KB comfortably exceeds the 150 KB benchmark!")
        print("Ready for deployment.")

if __name__ == "__main__":
    assemble()
