# -*- coding: utf-8 -*-
"""
Assembly and Verification Script for Class 8 Science Chapter 6:
Pressure, Winds, Storms, and Cyclones (NCERT NEP code: hecu106)
Target: english/class8/sci-ch6-pressure-winds-storms-and-cyclones.html
"""

import os
import sys
import re

# Add current directory to path
sys.path.insert(0, os.path.dirname(__file__))

from build_ch6.header_and_styles import get_header_and_styles
from build_ch6.section1_blueprint import get_section1
from build_ch6.section2_concept_mastery import get_section2
from build_ch6.section3_fact_formula_bank import get_section3
from build_ch6.section4_ncert_solutions import get_section4
from build_ch6.section5_exam_bank import get_section5
from build_ch6.section6_traps_and_revision import get_section6

def assemble():
    parts = [
        get_header_and_styles(),
        get_section1(),
        get_section2(),
        get_section3(),
        get_section4(),
        get_section5(),
        get_section6()
    ]
    
    full_html = "".join(parts)
    
    target_path = os.path.join("english", "class8", "sci-ch6-pressure-winds-storms-and-cyclones.html")
    
    with open(target_path, "w", encoding="utf-8") as f:
        f.write(full_html)
        
    size_bytes = os.path.getsize(target_path)
    size_kb = size_bytes / 1024
    
    print("=" * 60)
    print(f"ASSEMBLY COMPLETE: {target_path}")
    print(f"File Size: {size_bytes:,} bytes ({size_kb:.2f} KB)")
    print("=" * 60)
    
    # Validation checks
    min_kb = 150.0
    if size_kb < min_kb:
        print(f"WARNING: File size {size_kb:.2f} KB is below minimum floor of {min_kb} KB!")
    else:
        print(f"PASSED: File size {size_kb:.2f} KB exceeds minimum floor of {min_kb} KB.")
        
    # Check for raw LaTeX
    raw_latex = re.findall(r'(?<!\\)\$[^\$]+\$', full_html)
    if raw_latex:
        print(f"FAILED: Found {len(raw_latex)} instances of raw LaTeX: {raw_latex[:5]}")
    else:
        print("PASSED: Zero raw LaTeX math entities found.")
        
    # Check Odia characters
    odia_chars = re.findall(r'[\u0B00-\u0B7F]', full_html)
    print(f"Odia Characters Count: {len(odia_chars)}")
    if len(odia_chars) < 200:
        print("WARNING: Fewer than 200 Odia characters found in bilingual table!")
    else:
        print("PASSED: Rich authentic Odia vocabulary embedded.")
        
    # Check SVGs
    svg_count = full_html.count("<svg")
    print(f"Inline SVGs Count: {svg_count}")
    if svg_count < 4:
        print(f"WARNING: Found only {svg_count} SVGs, expected at least 4-6.")
    else:
        print("PASSED: Sufficient intricate inline SVGs embedded.")
        
    # Check collapsible answers
    ans_box_count = full_html.count('class="ans-box"')
    print(f"Collapsible Answer Boxes Count: {ans_box_count}")
    
    return size_kb >= min_kb

if __name__ == "__main__":
    assemble()
