# -*- coding: utf-8 -*-
"""
Script to assemble all parts of Chapter 7: Proportional Reasoning - 1
and write the final master study notes to english/class8/math-ch7-proportional-reasoning-1.html.
"""

import os
import sys

from ch7_styles_head import get_head_and_hero
from ch7_section1 import get_section1
from ch7_section2 import get_section2
from ch7_section3 import get_section3
from ch7_section4a import get_section4a
from ch7_section4b import get_section4b
from ch7_section5 import get_section5
from ch7_section6_footer import get_section6_and_footer

def assemble_chapter7():
    print("Assembling Chapter 7 components...")

    parts = [
        get_head_and_hero(),
        get_section1(),
        get_section2(),
        get_section3(),
        get_section4a(),
        get_section4b(),
        get_section5(),
        get_section6_and_footer()
    ]

    full_html = "\n".join(parts)

    output_path = os.path.join("..", "..", "english", "class8", "math-ch7-proportional-reasoning-1.html")
    # Resolve relative path if run from root or from math_ch7 directory
    if not os.path.exists(os.path.dirname(output_path)):
        output_path = os.path.join("english", "class8", "math-ch7-proportional-reasoning-1.html")

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(full_html)

    file_size_bytes = os.path.getsize(output_path)
    file_size_kb = file_size_bytes / 1024

    print(f"Assembly complete!")
    print(f"Destination: {output_path}")
    print(f"File Size: {file_size_bytes:,} bytes ({file_size_kb:.2f} KB)")

    min_required_kb = 150.0
    if file_size_kb >= min_required_kb:
        print(f"SUCCESS: File size ({file_size_kb:.2f} KB) comfortably exceeds the 150 KB minimum floor!")
    else:
        print(f"WARNING: File size ({file_size_kb:.2f} KB) is below the 150 KB minimum floor!")

if __name__ == "__main__":
    assemble_chapter7()
