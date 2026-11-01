# -*- coding: utf-8 -*-
"""
Section 4: 100% Solved NCERT Questions Master Wrapper
"""
from gen_sec4_part1 import get_sec4_part1
from gen_sec4_part2 import get_sec4_part2
from gen_sec4_part3 import get_sec4_part3
from gen_sec4_part4 import get_sec4_part4

def get_section_4():
    p1 = get_sec4_part1()
    p2 = get_sec4_part2()
    p3 = get_sec4_part3()
    p4 = get_sec4_part4()

    return f'''
    <!-- SECTION 4: 100% SOLVED NCERT QUESTIONS -->
    <section id="section-4" class="study-section">
      <div class="section-header">
        <div class="section-icon icon-blue">
          <i class="fa-solid fa-square-check"></i>
        </div>
        <div>
          <h2>Section 4: 100% Solved NCERT Questions &amp; In-Text Activities</h2>
          <p>Every single in-text prompt, example, 'Figure it Out' exercise, and synthesis challenge solved in our rigorous 5-Step presentation format.</p>
        </div>
      </div>

      <div class="callout callout-def">
        <div class="callout-title"><i class="fa-solid fa-list-check"></i> Our Zero-Omission Guarantee</div>
        <p>
          In accordance with NEP 2020 curriculum guidelines, this section provides comprehensive, un-summarized solutions 
          to every single problem found in Ganita Prakash Grade 7 Chapter 2 (NCERT code: gegp102), including official solutions 
          from the NCERT Teachers' Guidebook. Every problem follows our structured 5-step format: 
          <strong>Problem &rarr; Strategy &rarr; Calculation &rarr; Alternative Reasoning &rarr; Final Takeaway</strong>.
        </p>
      </div>

      {p1}
      {p2}
      {p3}
      {p4}
    </section>
'''
