# -*- coding: utf-8 -*-
"""
Section 1: Visual Blueprint & Detailed Mind Map
"""
from gen_svgs import get_svg_mindmap

def get_section_1():
    svg_html = get_svg_mindmap()
    return f'''
    <!-- SECTION 1: VISUAL BLUEPRINT & MIND MAP -->
    <section id="section-1" class="study-section">
      <div class="section-header">
        <div class="section-icon icon-blue">
          <i class="fa-solid fa-compass-drafting"></i>
        </div>
        <div>
          <h2>Section 1: Visual Blueprint &amp; Detailed Mind Map</h2>
          <p>Holistic curricular navigation, pedagogical architecture, and structural mental models for Chapter 2.</p>
        </div>
      </div>

      <p>
        Welcome to <strong>Chapter 2: Arithmetic Expressions</strong> (ଗାଣିତିକ ରାଶି) of the NCERT Class 7 Ganita Prakash curriculum (NEP gegp102). 
        In our everyday lives, whether we are purchasing groceries, splitting an auto-rickshaw fare among friends, or computing the height of a building, 
        we perform multiple operations in sequence. However, when we write down these numerical operations on paper, an immediate question arises: 
        <em>Which operation must be carried out first? Does the order matter? What happens if someone adds before multiplying?</em>
      </p>

      <div class="callout callout-def">
        <div class="callout-title"><i class="fa-solid fa-graduation-cap"></i> Pedagogical Focus of NCERT Ganita Prakash (NEP 2020)</div>
        <p>
          Unlike older textbooks that simply instructed students to memorize the mechanical mnemonic "BODMAS" without understanding, 
          the new NEP syllabus develops the <strong>structural anatomy of mathematical terms</strong>. 
          By understanding that an expression is fundamentally a <em>sum of terms</em>, students naturally discover why multiplication 
          and division bind more tightly than addition, why subtraction is merely adding an additive inverse, and how grouping 
          and distributive laws simplify complicated calculations into effortless mental arithmetic.
        </p>
      </div>

      <h3><i class="fa-solid fa-sitemap"></i> Master Architecture of Arithmetic Expressions</h3>
      <p>
        The mind map below synthesizes all six conceptual pillars of this chapter into an integrated visual learning blueprint. 
        Take 2 minutes to study this map before diving into the detailed proofs and solved problems.
      </p>

      {svg_html}

      <h3><i class="fa-solid fa-layer-group"></i> The Five Foundational Pillars of this Chapter</h3>
      <p>
        To achieve complete mastery of this chapter, every Class 7 student needs to understand five interconnected ideas:
      </p>

      <ol>
        <li>
          <strong>The Value of an Arithmetic Expression:</strong> 
          An arithmetic expression is a meaningful combination of numbers and arithmetic operators (+, −, ×, ÷). 
          Every well-formed expression evaluates to a <em>single numerical value</em>. Two completely different looking expressions can share 
          the exact same value (for example, <span class="math-inline">10 + 2</span>, <span class="math-inline">15 − 3</span>, <span class="math-inline">3 × 4</span>, and <span class="math-inline">24 ÷ 2</span> all evaluate to 12).
        </li>
        <li>
          <strong>The "Term" (ପଦ) as the Atomic Building Block:</strong> 
          Instead of memorizing mechanical rules, we view any arithmetic expression as a collection of <strong>terms separated strictly by '+' signs</strong>. 
          Subtraction is never treated as a separate disruptive operation; rather, subtracting a number <span class="math-inline">b</span> is universally defined as adding its additive inverse: <span class="math-inline">a − b = a + (−b)</span>.
        </li>
        <li>
          <strong>Symmetry &amp; Freedom of Movement (Commutative &amp; Associative Laws):</strong> 
          Because an expression is a sum of its terms, and addition enjoys both the <em>Commutative Property</em> (swapping terms does not change the sum) 
          and the <em>Associative Property</em> (grouping terms does not change the sum), we are completely free to rearrange and pair up terms 
          in whatever sequence makes mental arithmetic most convenient!
        </li>
        <li>
          <strong>The Bracket Unpacking Machinery:</strong> 
          Parentheses <span class="math-inline">( )</span> act as packaging containers. 
          When removing brackets preceded by a positive sign (+), the internal terms emerge unaltered. 
          However, when removing brackets preceded by a negative sign (−), the subtraction operator acts as an <em>inversion gate</em>: 
          every positive term inside flips to negative, and every negative term inside flips to positive!
        </li>
        <li>
          <strong>The Distributive Property of Multiplication (ବଣ୍ଟନ ନିୟମ):</strong> 
          Multiplication distributes over both addition and subtraction: 
          <span class="math-inline">a × (b + c) = a × b + a × c</span> and <span class="math-inline">a × (b − c) = a × b − a × c</span>. 
          This remarkable law allows us to turn massive multiplication problems like <span class="math-inline">97 × 25</span> into lightning-fast mental math: <span class="math-inline">(100 − 3) × 25 = 2500 − 75 = 2425</span>.
        </li>
      </ol>

      <div class="callout callout-act">
        <div class="callout-title"><i class="fa-solid fa-chalkboard-user"></i> How To Use These Master Notes</div>
        <p>
          Each section is designed to take you from a curious beginner to a confident exam topper:
        </p>
        <ul>
          <li><strong>Section 2</strong> breaks down every line of theory with concrete real-life analogies (marbles, shopping bags, drone heights, and marching scouts) plus an exhaustive Odia-English glossary.</li>
          <li><strong>Section 3</strong> gives you instant revision tables, comparison heuristics, and mental calculation tricks.</li>
          <li><strong>Section 4</strong> contains 100% zero-omission solutions for every single textbook example, 'Figure it Out' exercise, and in-text puzzle, structured in our signature 5-Step presentation format.</li>
          <li><strong>Section 5</strong> features an exam bank of 27 high-yield questions including MCQs with clickable options, Assertion-Reasoning, Short/Long answers with marking schemes, and Case Studies.</li>
          <li><strong>Section 6</strong> warns you about the 5 fatal traps that cause students to lose marks in board exams, along with 15 rapid-fire revision points.</li>
        </ul>
      </div>
    </section>
'''
