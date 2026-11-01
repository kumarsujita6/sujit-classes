# -*- coding: utf-8 -*-
"""
Master Assembly Script for Class 7 Mathematics Chapter 2: Arithmetic Expressions
"""
import os
import sys

from gen_modules import get_head_and_styles
from gen_hero import get_hero_and_nav
from gen_sec1 import get_section_1
from gen_sec2 import get_section_2
from gen_sec3 import get_section_3
from gen_sec4 import get_section_4
from gen_sec5 import get_section_5
from gen_sec6 import get_section_6

def build():
    print("Building Class 7 Mathematics Chapter 2 Master Study Note...")
    parts = [
        get_head_and_styles(),
        get_hero_and_nav(),
        get_section_1(),
        get_section_2(),
        get_section_3(),
        get_section_4(),
        get_section_5(),
        get_section_6()
    ]

    full_html = "\n".join(parts)
    
    target_path = os.path.join("english", "class7", "math-ch2-arithmetic-expressions.html")
    
    with open(target_path, "w", encoding="utf-8") as f:
        f.write(full_html)
        
    file_size_bytes = os.path.getsize(target_path)
    file_size_kb = file_size_bytes / 1024.0
    print(f"Successfully generated: {target_path}")
    print(f"File Size: {file_size_bytes:,} bytes ({file_size_kb:.2f} KB)")
    
    if file_size_kb < 150.0:
        print(f"WARNING: File size {file_size_kb:.2f} KB is below the 150 KB floor guardrail!")
    else:
        print(f"SUCCESS: File size {file_size_kb:.2f} KB satisfies the 150 KB+ benchmark requirement.")

if __name__ == "__main__":
    build()
