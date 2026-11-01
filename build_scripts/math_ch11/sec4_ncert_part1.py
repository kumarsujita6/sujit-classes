# -*- coding: utf-8 -*-
"""
Section 4 Module Part 1: 100% Solved NCERT Textbook Questions (Pages 71-87)
Class 8 Mathematics Chapter 11: Exploring Some Geometric Themes
"""

def get_section_4_part1():
    return """
    <!-- SECTION 4: 100% SOLVED NCERT QUESTIONS (PART 1) -->
    <section id="section4" class="section-box">
      <div class="section-header">
        <div class="section-header-left">
          <span class="section-tag">Textbook Mastery</span>
          <h2 class="section-title">§ 4. 100% Solved NCERT Questions & Activities (Part 1: Pages 71–87)</h2>
          <p class="section-desc">
            Complete, zero-omission solutions for every single in-text prompt, 'Figure it Out', 'Math Talk', and 'Try This' activity from pages 71 through 87, presented in the CBSE topper 5-step structured format.
          </p>
        </div>
        <div>
          <span class="badge badge-emerald"><i class="fa-solid fa-check-double"></i> Complete Solutions (Part 1)</span>
        </div>
      </div>

      <!-- Q1: SIERPINSKI CARPET SEQUENCE & DERIVATION -->
      <details class="ans-box">
        <summary>
          <span><span class="step-pill">Activity & Derivation</span> Page 71: Draw initial steps of Sierpinski Carpet, analyze patterns of remaining squares (Rₙ) and holes (Hₙ), and derive general formulas.</span>
        </summary>
        <div class="ans-content">
          <div class="ans-step">
            <div class="ans-step-title">Step 1: Conceptual Identification & Given Data</div>
            <p>We are given an initial solid square (Step 0) of side length <span class="math-inline">s</span> and area <span class="math-inline">A₀</span>. At each successive iteration, each remaining square is divided into 9 congruent squares of side <span class="math-inline">s/3</span>, and the single central square is removed as a hole.</p>
          </div>
          <div class="ans-step">
            <div class="ans-step-title">Step 2: Mathematical Recurrence Relations</div>
            <p>1. <strong>Remaining Squares (<span class="math-inline">Rₙ</span>):</strong> Every square remaining at Step <span class="math-inline">n</span> spawns exactly 8 remaining squares at Step <span class="math-inline">n+1</span>. Thus: <span class="math-inline">Rₙ₊₁ = 8 · Rₙ</span>.<br>
            2. <strong>Holes (<span class="math-inline">Hₙ</span>):</strong> All previous holes persist, and each remaining square at Step <span class="math-inline">n</span> contributes exactly 1 new hole. Thus: <span class="math-inline">Hₙ₊₁ = Hₙ + Rₙ</span>.</p>
          </div>
          <div class="ans-step">
            <div class="ans-step-title">Step 3: Step-by-Step Execution & Calculation</div>
            <p>• <strong>Step 0:</strong> <span class="math-inline">R₀ = 1</span>, <span class="math-inline">H₀ = 0</span>, <span class="math-inline">A₀ = 1</span>.<br>
            • <strong>Step 1:</strong> <span class="math-inline">R₁ = 8 × 1 = 8</span>. <span class="math-inline">H₁ = 0 + 1 = 1</span>. Area <span class="math-inline">A₁ = 8/9</span>.<br>
            • <strong>Step 2:</strong> <span class="math-inline">R₂ = 8 × 8 = 8² = 64</span>. <span class="math-inline">H₂ = 1 + 8 = 9</span>. Area <span class="math-inline">A₂ = (8/9)² = 64/81</span>.<br>
            • <strong>Step 3:</strong> <span class="math-inline">R₃ = 8 × 64 = 8³ = 512</span>. <span class="math-inline">H₃ = 9 + 64 = 73</span>. Area <span class="math-inline">A₃ = (8/9)³ = 512/729</span>.<br>
            • <strong>Step 4:</strong> <span class="math-inline">R₄ = 8⁴ = 4096</span>. <span class="math-inline">H₄ = 73 + 512 = 585</span>. Area <span class="math-inline">A₄ = (8/9)⁴ = 4096/6561</span>.<br>
            • <strong>General Step n:</strong>
            <br><span class="math-inline">Rₙ = 8ⁿ</span>
            <br><span class="math-inline">Hₙ = ∑_{k=0}^{n-1} 8ᵏ = (8ⁿ - 1) / (8 - 1) = (8ⁿ - 1) / 7</span>.</p>
          </div>
          <div class="ans-step">
            <div class="ans-step-title">Step 4: Verification & Consistency Check</div>
            <p>Check for <span class="math-inline">n = 3</span>: <span class="math-inline">H₃ = (8³ - 1)/7 = (512 - 1)/7 = 511/7 = 73</span>. Exactly matches our recursive sum <span class="math-inline">1 + 8 + 64 = 73</span>! Formula is verified.</p>
          </div>
          <div class="ans-step">
            <div class="ans-step-title">Step 5: Final Concluding Answer</div>
            <p><strong>General Formulas:</strong> Number of remaining squares is <span class="math-inline">Rₙ = 8ⁿ</span>; Cumulative holes is <span class="math-inline">Hₙ = (8ⁿ - 1)/7</span>; Remaining area is <span class="math-inline">Aₙ = (8/9)ⁿ · A₀</span>.</p>
          </div>
        </div>
      </details>

      <!-- Q2: SIERPINSKI GASKET MIDPOINT DIVISION PROOF -->
      <details class="ans-box">
        <summary>
          <span><span class="step-pill">Geometric Proof</span> Page 72: Show that by joining the midpoints of an equilateral triangle, we divide it into 4 identical equilateral triangles.</span>
        </summary>
        <div class="ans-content">
          <div class="ans-step">
            <div class="ans-step-title">Step 1: Conceptual Identification & Given Data</div>
            <p>Let <span class="math-inline">△ABC</span> be an equilateral triangle of side length <span class="math-inline">s</span>. Let <span class="math-inline">D, E, F</span> be the midpoints of sides <span class="math-inline">BC, CA, AB</span> respectively. Line segments <span class="math-inline">DE, EF, FD</span> are drawn.</p>
          </div>
          <div class="ans-step">
            <div class="ans-step-title">Step 2: Mathematical Theorem (Midpoint Theorem)</div>
            <p>The Midpoint Theorem states that the line segment connecting the midpoints of any two sides of a triangle is parallel to the third side and equal to half of its length:
            <br>• <span class="math-inline">EF ∥ BC</span> and <span class="math-inline">EF = ½ BC = s/2</span>.
            <br>• <span class="math-inline">FD ∥ CA</span> and <span class="math-inline">FD = ½ CA = s/2</span>.
            <br>• <span class="math-inline">DE ∥ AB</span> and <span class="math-inline">DE = ½ AB = s/2</span>.</p>
          </div>
          <div class="ans-step">
            <div class="ans-step-title">Step 3: Step-by-Step Proof of Congruence</div>
            <p>1. In the top corner triangle <span class="math-inline">△AFE</span>: <span class="math-inline">AF = s/2</span>, <span class="math-inline">AE = s/2</span>, and <span class="math-inline">EF = s/2</span>. All 3 sides are equal to <span class="math-inline">s/2</span>, so <span class="math-inline">△AFE</span> is an equilateral triangle.<br>
            2. In the bottom-left corner triangle <span class="math-inline">△FBD</span>: <span class="math-inline">FB = s/2</span>, <span class="math-inline">BD = s/2</span>, and <span class="math-inline">FD = s/2</span>. All 3 sides are equal to <span class="math-inline">s/2</span>, so <span class="math-inline">△FBD</span> is an equilateral triangle.<br>
            3. In the bottom-right corner triangle <span class="math-inline">△EDC</span>: <span class="math-inline">EC = s/2</span>, <span class="math-inline">DC = s/2</span>, and <span class="math-inline">DE = s/2</span>. All 3 sides are equal to <span class="math-inline">s/2</span>, so <span class="math-inline">△EDC</span> is an equilateral triangle.<br>
            4. In the central inverted triangle <span class="math-inline">△DEF</span>: Its three sides are <span class="math-inline">DE = s/2</span>, <span class="math-inline">EF = s/2</span>, and <span class="math-inline">FD = s/2</span>. All 3 sides are equal to <span class="math-inline">s/2</span>, so <span class="math-inline">△DEF</span> is also an equilateral triangle.</p>
          </div>
          <div class="ans-step">
            <div class="ans-step-title">Step 4: Verification & Congruence Criteria</div>
            <p>By SSS Congruence Criterion (Side-Side-Side), all 4 smaller triangles have three sides equal to <span class="math-inline">s/2</span>. Thus: <span class="math-inline">△AFE ≅ △FBD ≅ △EDC ≅ △DEF</span>.</p>
          </div>
          <div class="ans-step">
            <div class="ans-step-title">Step 5: Final Concluding Answer</div>
            <p><strong>Proved:</strong> The four triangles are identically sized equilateral triangles, each having side length <span class="math-inline">s/2</span> and area equal to exactly <span class="math-inline">¼</span> of the original triangle's area.</p>
          </div>
        </div>
      </details>

      <!-- Q3: FIGURE IT OUT PAGE 72 (SIERPINSKI TRIANGLE HOLES & REMAINING TRIANGLES) -->
      <details class="ans-box">
        <summary>
          <span><span class="step-pill">Figure it Out</span> Page 72 (Q1 & Q2): Draw initial steps of Sierpinski Triangle; find number of holes and remaining triangles at each step.</span>
        </summary>
        <div class="ans-content">
          <div class="ans-step">
            <div class="ans-step-title">Step 1: Conceptual Identification & Given Data</div>
            <p>Start with 1 equilateral triangle. At each iteration, the central inverted equilateral triangle is carved out and removed. We need to determine <span class="math-inline">Rₙ</span> (remaining triangles) and <span class="math-inline">Hₙ</span> (cumulative holes).</p>
          </div>
          <div class="ans-step">
            <div class="ans-step-title">Step 2: Recurrence Relationships</div>
            <p>Each remaining triangle at Step <span class="math-inline">n</span> is partitioned into 4 smaller triangles, the center 1 is removed, leaving 3 triangles.
            <br>• Recurrence for triangles: <span class="math-inline">Rₙ₊₁ = 3 · Rₙ</span>.
            <br>• Recurrence for holes: <span class="math-inline">Hₙ₊₁ = Hₙ + Rₙ</span>.</p>
          </div>
          <div class="ans-step">
            <div class="ans-step-title">Step 3: Calculation for Steps 0, 1, 2, 3, n</div>
            <p>• <strong>Step 0:</strong> <span class="math-inline">R₀ = 1</span>, <span class="math-inline">H₀ = 0</span>.<br>
            • <strong>Step 1:</strong> <span class="math-inline">R₁ = 3 × 1 = 3</span>. <span class="math-inline">H₁ = 0 + 1 = 1</span>.<br>
            • <strong>Step 2:</strong> <span class="math-inline">R₂ = 3 × 3 = 3² = 9</span>. <span class="math-inline">H₂ = 1 + 3 = 4</span>.<br>
            • <strong>Step 3:</strong> <span class="math-inline">R₃ = 3 × 9 = 3³ = 27</span>. <span class="math-inline">H₃ = 4 + 9 = 13</span>.<br>
            • <strong>General Step n:</strong>
            <br><span class="math-inline">Rₙ = 3ⁿ</span>
            <br><span class="math-inline">Hₙ = ∑_{k=0}^{n-1} 3ᵏ = (3ⁿ - 1) / (3 - 1) = (3ⁿ - 1) / 2</span>.</p>
          </div>
          <div class="ans-step">
            <div class="ans-step-title">Step 4: Verification</div>
            <p>For <span class="math-inline">n = 3</span>: <span class="math-inline">H₃ = (3³ - 1)/2 = (27 - 1)/2 = 13</span>. Matches perfectly!</p>
          </div>
          <div class="ans-step">
            <div class="ans-step-title">Step 5: Final Concluding Answer</div>
            <p>At Step <span class="math-inline">n</span>, the number of remaining triangles is <span class="math-inline">3ⁿ</span>, and the cumulative number of removed triangular holes is <span class="math-inline">(3ⁿ - 1)/2</span>.</p>
          </div>
        </div>
      </details>

      <!-- Q4: FIGURE IT OUT PAGE 72 (AREA REMAINING IN BOTH FRACTALS) -->
      <details class="ans-box">
        <summary>
          <span><span class="step-pill">Figure it Out</span> Page 72 (Q3): Find the area remaining at the nth step in both Sierpinski Carpet and Sierpinski Triangle (starting area = 1 sq. unit).</span>
        </summary>
        <div class="ans-content">
          <div class="ans-step">
            <div class="ans-step-title">Step 1: Conceptual Identification & Given Data</div>
            <p>Initial Area for both fractals: <span class="math-inline">A₀ = 1  sq. unit</span>. We need to compute <span class="math-inline">Aₙ</span> for both fractals and examine their asymptotic behavior as <span class="math-inline">n → ∞</span>.</p>
          </div>
          <div class="ans-step">
            <div class="ans-step-title">Step 2: Area Multiplication Factors</div>
            <p>• <strong>Carpet:</strong> In each square, 1 of 9 parts is removed, retaining <span class="math-inline">8/9</span> of the previous area.
            <br>• <strong>Triangle (Gasket):</strong> In each triangle, 1 of 4 parts is removed, retaining <span class="math-inline">3/4</span> of the previous area.</p>
          </div>
          <div class="ans-step">
            <div class="ans-step-title">Step 3: Derivation of nth Step Areas</div>
            <p>1. <strong>Sierpinski Carpet:</strong>
            <br><span class="math-inline">A₁ = (8/9) · 1 = 8/9</span>
            <br><span class="math-inline">A₂ = (8/9) · A₁ = (8/9)² = 64/81</span>
            <br><span class="math-inline">Aₙ = (8/9)ⁿ  sq. units</span>.
            <br><br>
            2. <strong>Sierpinski Triangle:</strong>
            <br><span class="math-inline">A₁ = (3/4) · 1 = 3/4</span>
            <br><span class="math-inline">A₂ = (3/4) · A₁ = (3/4)² = 9/16</span>
            <br><span class="math-inline">Aₙ = (3/4)ⁿ  sq. units</span>.</p>
          </div>
          <div class="ans-step">
            <div class="ans-step-title">Step 4: Asymptotic Limit Analysis</div>
            <p>Since both common ratios are strictly less than 1 (<span class="math-inline">8/9 &lt; 1</span> and <span class="math-inline">3/4 &lt; 1</span>):
            <br><span class="math-inline">Limit as n → ∞: (8/9)ⁿ = 0</span> and <span class="math-inline">Limit as n → ∞: (3/4)ⁿ = 0</span>.
            <br>In both cases, the remaining area asymptotically decays to <strong>zero</strong>.</p>
          </div>
          <div class="ans-step">
            <div class="ans-step-title">Step 5: Final Concluding Answer</div>
            <p>Area of Sierpinski Carpet at Step <span class="math-inline">n</span> is <span class="math-inline">(8/9)ⁿ  sq. units</span>. Area of Sierpinski Triangle at Step <span class="math-inline">n</span> is <span class="math-inline">(3/4)ⁿ  sq. units</span>. In both cases, the area approaches 0 as <span class="math-inline">n → ∞</span>.</p>
          </div>
        </div>
      </details>

      <!-- Q5: KOCH SNOWFLAKE (FIGURE IT OUT PAGE 73 - SIDES & PERIMETER) -->
      <details class="ans-box">
        <summary>
          <span><span class="step-pill">Figure it Out</span> Page 73 (Q1, Q2 & Q3): Find the number of sides (Nₙ) and perimeter (Pₙ) at the nth step of the Koch Snowflake (initial sidelength = 1 unit).</span>
        </summary>
        <div class="ans-content">
          <div class="ans-step">
            <div class="ans-step-title">Step 1: Conceptual Identification & Given Data</div>
            <p>Start with an equilateral triangle of side <span class="math-inline">s = 1</span> unit. At each step, every side is divided into 3 equal segments of length <span class="math-inline">1/3</span>, and an equilateral bump is added over the middle segment, replacing 1 segment of length <span class="math-inline">L</span> with 4 segments of length <span class="math-inline">L/3</span>.</p>
          </div>
          <div class="ans-step">
            <div class="ans-step-title">Step 2: Recurrence Formulations</div>
            <p>1. Number of sides: <span class="math-inline">Nₙ₊₁ = 4 · Nₙ</span>.
            <br>2. Segment length: <span class="math-inline">Lₙ₊₁ = Lₙ / 3</span>.
            <br>3. Perimeter: <span class="math-inline">Pₙ = Nₙ × Lₙ</span>.</p>
          </div>
          <div class="ans-step">
            <div class="ans-step-title">Step 3: Step-by-Step Calculation</div>
            <p>• <strong>Step 0:</strong> <span class="math-inline">N₀ = 3</span>, <span class="math-inline">L₀ = 1</span>, <span class="math-inline">P₀ = 3 × 1 = 3</span>.<br>
            • <strong>Step 1:</strong> <span class="math-inline">N₁ = 3 × 4 = 12</span> sides. <span class="math-inline">L₁ = 1/3</span>. <span class="math-inline">P₁ = 12 × (1/3) = 4 = 3 × (4/3)¹</span>.<br>
            • <strong>Step 2:</strong> <span class="math-inline">N₂ = 12 × 4 = 48</span> sides. <span class="math-inline">L₂ = 1/9</span>. <span class="math-inline">P₂ = 48 × (1/9) = 16/3 = 3 × (4/3)² ≈ 5.33</span>.<br>
            • <strong>Step 3:</strong> <span class="math-inline">N₃ = 48 × 4 = 192</span> sides. <span class="math-inline">L₃ = 1/27</span>. <span class="math-inline">P₃ = 192 × (1/27) = 64/9 = 3 × (4/3)³ ≈ 7.11</span>.<br>
            • <strong>General Step n:</strong>
            <br><span class="math-inline">Nₙ = 3 · 4ⁿ</span> sides.
            <br><span class="math-inline">Lₙ = 1 / 3ⁿ</span> units.
            <br><span class="math-inline">Pₙ = Nₙ · Lₙ = (3 · 4ⁿ) · (1 / 3ⁿ) = 3 · (4/3)ⁿ  units</span>.</p>
          </div>
          <div class="ans-step">
            <div class="ans-step-title">Step 4: Asymptotic Limit Verification</div>
            <p>Since the base <span class="math-inline">4/3 = 1.333... &gt; 1</span>, as <span class="math-inline">n → ∞</span>, <span class="math-inline">(4/3)ⁿ → ∞</span>. Thus, the perimeter diverges to <strong>infinity</strong>.</p>
          </div>
          <div class="ans-step">
            <div class="ans-step-title">Step 5: Final Concluding Answer</div>
            <p>Number of sides at Step <span class="math-inline">n</span> is <span class="math-inline">Nₙ = 3 · 4ⁿ</span>. Perimeter at Step <span class="math-inline">n</span> is <span class="math-inline">Pₙ = 3 · (4/3)ⁿ  units</span> (approaching infinity as <span class="math-inline">n → ∞</span>).</p>
          </div>
        </div>
      </details>

      <!-- Q6: IMAGINATION EXERCISES (PAGE 76: Q1, Q2, Q3, Q4) -->
      <details class="ans-box">
        <summary>
          <span><span class="step-pill">Visualisation</span> Page 76: Mental Dissection Prompts 1, 2, 3 & 4 (Backwards name, cutting corners of square & triangle).</span>
        </summary>
        <div class="ans-content">
          <div class="ans-step">
            <div class="ans-step-title">Prompt 1: Picture your name backwards by sight</div>
            <p><strong>Solution:</strong> If your name is "SUJIT", visualize the letters in your mind's eye: S - U - J - I - T. Reading backwards letter by letter from right to left gives: <strong>T - I - J - U - S</strong>.</p>
          </div>
          <div class="ans-step">
            <div class="ans-step-title">Prompt 2: Cut off 4 corners of square between edge midpoints</div>
            <p><strong>Analysis:</strong> Let a square have side <span class="math-inline">s</span> and area <span class="math-inline">s²</span>. Slicing through adjacent edge midpoints cuts off 4 right-angled isosceles triangles, each having legs <span class="math-inline">s/2</span> and area <span class="math-inline">½ (s/2)(s/2) = s²/8</span>.
            <br>• Shape left over: A <strong>rotated square (diamond)</strong> tilted at 45°. Its side length by Pythagoras is <span class="math-inline">√((s/2)² + (s/2)²) = s/√2</span>, and its area is <span class="math-inline">(s/√2)² = s²/2</span> (half the original area!).
            <br>• Reassembly: The 4 cut-off corner triangles (each of area <span class="math-inline">s²/8</span>) can be paired along their hypotenuses or joined at their right angles to form <strong>another identical square</strong> of side <span class="math-inline">s/√2</span> and area <span class="math-inline">4 × (s²/8) = s²/2</span>.</p>
          </div>
          <div class="ans-step">
            <div class="ans-step-title">Prompt 3: Mark sides of equilateral triangle into thirds, cut off corners</div>
            <p><strong>Analysis:</strong> Let an equilateral triangle have side <span class="math-inline">s</span>. Each side is divided into three segments of length <span class="math-inline">s/3</span>. Slicing across these 1/3 marks removes 3 small equilateral corner triangles of side <span class="math-inline">s/3</span>.
            <br>• Shape left over: A <strong>regular hexagon</strong> having 6 equal sides of length <span class="math-inline">s/3</span> and 6 internal angles of 120°!</p>
          </div>
          <div class="ans-step">
            <div class="ans-step-title">Prompt 4: Mark sides of square into thirds, cut off corners</div>
            <p><strong>Analysis:</strong> Each side of the square is divided into 3 equal parts of length <span class="math-inline">s/3</span>. Slicing off the 4 right-angled corner triangles leaves an <strong>octagon</strong>. It has 4 edges along the original square sides of length <span class="math-inline">s/3</span>, and 4 corner cut edges of length <span class="math-inline">√((s/3)² + (s/3)²) = (s√2)/3</span>.</p>
          </div>
          <div class="ans-step">
            <div class="ans-step-title">Final Summary</div>
            <p>Prompt 2 yields a square of half area; Prompt 3 yields a regular hexagon; Prompt 4 yields an octagon.</p>
          </div>
        </div>
      </details>

      <!-- Q7: CONTRASTING PROFILES (PAGE 77: Q5 - Q12) -->
      <details class="ans-box">
        <summary>
          <span><span class="step-pill">Spatial Reasoning</span> Page 77: Prompts 5–12: Solids with specified profiles (Square, Circle, Triangle, and Contrasting Pairs).</span>
        </summary>
        <div class="ans-content">
          <div class="ans-step">
            <div class="ans-step-title">Prompts 5, 6 & 7: Single Profile Outlines</div>
            <p>• <strong>Q5 (Square outline):</strong> A <strong>Cube</strong> (viewed perpendicular to any face), a <strong>Cylinder</strong> whose height equals its diameter (<span class="math-inline">h = 2r</span>) viewed from the side, or a <strong>Square Pyramid</strong> viewed directly from above.
            <br>• <strong>Q6 (Circular outline):</strong> A <strong>Sphere</strong> (from any viewpoint!), a <strong>Cylinder</strong> viewed from top or bottom, or a <strong>Cone</strong> viewed directly from its base.
            <br>• <strong>Q7 (Triangular outline):</strong> A <strong>Cone</strong> viewed from the side, a <strong>Triangular Prism</strong> viewed from either triangular base, or a <strong>Pyramid</strong> viewed from the side.</p>
          </div>
          <div class="ans-step">
            <div class="ans-step-title">Prompts 8, 9 & 10: Contrasting Profiles</div>
            <p>• <strong>Q8 (Rectangular from one viewpoint, Circular from another):</strong> A <strong>Cylinder</strong>. Looking down the circular axis gives a circle; looking perpendicular to its curved surface gives a rectangle of width <span class="math-inline">2r</span> and height <span class="math-inline">h</span>.
            <br>• <strong>Q9 (Circular from one viewpoint, Triangular from another):</strong> A <strong>Cone</strong>. Looking directly from the base gives a circle; looking horizontally from the side gives an isosceles triangle.
            <br>• <strong>Q10 (Rectangular from one viewpoint, Triangular from another):</strong> A <strong>Triangular Prism</strong> (or a doorstop wedge). Looking from the triangular ends gives a triangle; looking from any of the three lateral sides gives a rectangle.</p>
          </div>
          <div class="ans-step">
            <div class="ans-step-title">Prompts 11 & 12: Advanced Contrasting Profiles & Uniqueness</div>
            <p>• <strong>Q11 (Trapezium from one viewpoint, Circular from another):</strong> A <strong>Frustum of a Cone</strong> (a truncated cone, like a drinking glass, bucket, or flowerpot). Looking from the side yields an isosceles trapezium; looking from top or bottom yields concentric circles.
            <br>• <strong>Q12 (Pentagonal from one viewpoint, Rectangular from another):</strong> A <strong>Pentagonal Prism</strong>. Looking perpendicular to its bases yields a pentagon; looking perpendicular to any lateral face yields a rectangle.
            <br>• <strong>Are these solids unique?</strong> <strong>No, they are NOT unique!</strong> For example, for Q8, an elliptical cylinder or a rounded rectangular bar can also yield rectangles and rounded shapes. For Q9, a cone, a teardrop solid, or a solid formed by rotating a parabolic curve can produce circular and triangular silhouettes.</p>
          </div>
          <div class="ans-step">
            <div class="ans-step-title">Final Summary</div>
            <p>Every profile condition can be satisfied by classic geometric solids (Cylinder, Cone, Triangular Prism, Frustum, Pentagonal Prism), and none of them are mathematically unique.</p>
          </div>
        </div>
      </details>

      <!-- Q8: PRISMS & PYRAMIDS IN-TEXT (PAGE 79) -->
      <details class="ans-box">
        <summary>
          <span><span class="step-pill">Formula Derivation</span> Page 79: Faces, Vertices & Edges for 10-sided and n-sided Prisms and Pyramids.</span>
        </summary>
        <div class="ans-content">
          <div class="ans-step">
            <div class="ans-step-title">Part A: Prisms with n-sided and 10-sided Polygons</div>
            <p>A prism has two congruent parallel <span class="math-inline">n</span>-gon bases connected by <span class="math-inline">n</span> parallelogram lateral faces:
            <br>• <strong>Faces (F):</strong> 2 base faces + <span class="math-inline">n</span> lateral faces = <span class="math-inline">n + 2</span>.
            <br>• <strong>Vertices (V):</strong> <span class="math-inline">n</span> vertices on top base + <span class="math-inline">n</span> on bottom base = <span class="math-inline">2n</span>.
            <br>• <strong>Edges (E):</strong> <span class="math-inline">n</span> edges on top + <span class="math-inline">n</span> on bottom + <span class="math-inline">n</span> vertical joining edges = <span class="math-inline">3n</span>.
            <br><strong>For a 10-sided Prism (Decagonal Prism, n = 10):</strong>
            <br><span class="math-inline">F = 10 + 2 = 12</span> faces.
            <br><span class="math-inline">V = 2 × 10 = 20</span> vertices.
            <br><span class="math-inline">E = 3 × 10 = 30</span> edges.
            <br><em>Euler Check:</em> <span class="math-inline">F + V - E = 12 + 20 - 30 = 2</span> (Verified!).</p>
          </div>
          <div class="ans-step">
            <div class="ans-step-title">Part B: Pyramids with n-sided and 10-sided Base</div>
            <p>A pyramid has one <span class="math-inline">n</span>-gon base and <span class="math-inline">n</span> triangular lateral faces meeting at a single apex vertex:
            <br>• <strong>Faces (F):</strong> 1 base face + <span class="math-inline">n</span> triangular faces = <span class="math-inline">n + 1</span>.
            <br>• <strong>Vertices (V):</strong> <span class="math-inline">n</span> base vertices + 1 apex vertex = <span class="math-inline">n + 1</span>.
            <br>• <strong>Edges (E):</strong> <span class="math-inline">n</span> base edges + <span class="math-inline">n</span> edges connecting to apex = <span class="math-inline">2n</span>.
            <br><strong>For a 10-sided Pyramid (Decagonal Pyramid, n = 10):</strong>
            <br><span class="math-inline">F = 10 + 1 = 11</span> faces.
            <br><span class="math-inline">V = 10 + 1 = 11</span> vertices.
            <br><span class="math-inline">E = 2 × 10 = 20</span> edges.
            <br><em>Euler Check:</em> <span class="math-inline">F + V - E = 11 + 11 - 20 = 2</span> (Verified!).</p>
          </div>
          <div class="ans-step">
            <div class="ans-step-title">Final Concluding Answer</div>
            <p>For an <span class="math-inline">n</span>-gon prism: <span class="math-inline">F = n+2</span>, <span class="math-inline">V = 2n</span>, <span class="math-inline">E = 3n</span> (for <span class="math-inline">n=10</span>: 12, 20, 30). For an <span class="math-inline">n</span>-gon pyramid: <span class="math-inline">F = n+1</span>, <span class="math-inline">V = n+1</span>, <span class="math-inline">E = 2n</span> (for <span class="math-inline">n=10</span>: 11, 11, 20).</p>
          </div>
        </div>
      </details>

      <!-- Q9: FIGURE IT OUT PAGE 80 - 81 (NETS OF CUBE & CUBOIDS) -->
      <details class="ans-box">
        <summary>
          <span><span class="step-pill">Figure it Out</span> Pages 80–81: Identify nets of cube; find all 11 nets; draw nets of cuboids 5×3×1 and 6×3×2.</span>
        </summary>
        <div class="ans-content">
          <div class="ans-step">
            <div class="ans-step-title">Question 1: Which of the given arrangements fold into a cube?</div>
            <p>• Arrangement (i): A Latin cross (1-4-1 pattern). <strong>YES</strong>, it folds into a cube.<br>
            • Arrangement (ii): A 2 × 2 block with 2 attached squares. <strong>NO</strong>, contains a 2 × 2 square cluster, faces overlap.<br>
            • Arrangement (iii): A 1-4-1 pattern with top and bottom flaps on opposite sides. <strong>YES</strong>, folds into a cube.<br>
            • Arrangement (iv): 5 squares in a row. <strong>NO</strong>, wraps over itself.<br>
            • Arrangement (v): 1-3-2 step pattern. <strong>YES</strong>, folds into a cube.<br>
            • Arrangement (vi): Both single flaps on the SAME side of 4-row. <strong>NO</strong>, flaps collide and leave bottom open.</p>
          </div>
          <div class="ans-step">
            <div class="ans-step-title">Question 2: The 11 Distinct Nets of a Cube</div>
            <p>Every cube net belongs to one of 4 patterns up to rotation and reflection:
            <br>1. <strong>Class "1-4-1" (6 nets):</strong> Top flap can be placed in 4 positions; bottom flap in remaining non-symmetric positions. Gives 6 distinct hexaminoes.
            <br>2. <strong>Class "1-3-2" (3 nets):</strong> A central row of 3 squares, 1 on top, 2 below forming stairs.
            <br>3. <strong>Class "2-2-2" (1 net):</strong> A zigzag staircase of three pairs of squares.
            <br>4. <strong>Class "3-3" (1 net):</strong> Two strips of 3 squares offset by 1 square.
            <br>Total = <span class="math-inline">6 + 3 + 1 + 1 = 11  nets</span>.</p>
          </div>
          <div class="ans-step">
            <div class="ans-step-title">Question 3: Nets of Given Cuboids</div>
            <p>• <strong>(i) Cuboid 5 cm × 3 cm × 1 cm:</strong> Consists of 3 pairs of rectangular faces: two of <span class="math-inline">5 × 3</span>, two of <span class="math-inline">5 × 1</span>, and two of <span class="math-inline">3 × 1</span>. Draw a central strip alternating <span class="math-inline">5 × 3</span>, <span class="math-inline">5 × 1</span>, <span class="math-inline">5 × 3</span>, <span class="math-inline">5 × 1</span> (total length = <span class="math-inline">3 + 1 + 3 + 1 = 8 cm</span> and height = 5 cm), with two <span class="math-inline">3 × 1 cm</span> end caps attached to the <span class="math-inline">5 × 3</span> face.
            <br>• <strong>(ii) Cuboid 6 cm × 3 cm × 2 cm:</strong> Faces: two <span class="math-inline">6 × 3</span>, two <span class="math-inline">6 × 2</span>, and two <span class="math-inline">3 × 2</span>. Draw a central strip alternating <span class="math-inline">6 × 3</span>, <span class="math-inline">6 × 2</span>, <span class="math-inline">6 × 3</span>, <span class="math-inline">6 × 2</span> (length = <span class="math-inline">3 + 2 + 3 + 2 = 10 cm</span>, height = 6 cm), with two <span class="math-inline">3 × 2 cm</span> side caps.</p>
          </div>
          <div class="ans-step">
            <div class="ans-step-title">Final Concluding Answer</div>
            <p>A cube has exactly 11 distinct nets. Cuboids unfold into 6 rectangular faces joined in an alternating cross or step pattern.</p>
          </div>
        </div>
      </details>

      <!-- Q10: NETS OF OTHER SOLIDS (PAGES 81 - 84) -->
      <details class="ans-box">
        <summary>
          <span><span class="step-pill">Math Talk & Inquiry</span> Pages 81–84: Nets of regular tetrahedron, cylinder, cone, octahedron, dodecahedron & impossibility of sphere net.</span>
        </summary>
        <div class="ans-content">
          <div class="ans-step">
            <div class="ans-step-title">1. Regular Tetrahedron (Page 81)</div>
            <p>Has 4 equilateral triangular faces. A regular tetrahedron has exactly <strong>2 distinct nets</strong>:
            <br>• Net A: A large equilateral triangle partitioned into 4 smaller equilateral triangles by joining edge midpoints.
            <br>• Net B: A chain/strip of 4 equilateral triangles placed base-to-base in an alternating row.</p>
          </div>
          <div class="ans-step">
            <div class="ans-step-title">2. Cylinder & Cone Nets (Pages 82–83)</div>
            <p>• <strong>Cylinder of radius r and height h:</strong> Unfolds into a single <strong>rectangle</strong> of length equal to base circumference <span class="math-inline">2πr</span> and width equal to height <span class="math-inline">h</span>, plus <strong>two circular disks</strong> of radius <span class="math-inline">r</span> attached at opposite edges.
            <br>• <strong>Cone of base radius r and slant height l:</strong> Unrolls into a <strong>sector of a circle</strong> of radius <span class="math-inline">l</span> whose arc length equals the base circumference <span class="math-inline">2πr</span> (central angle <span class="math-inline">θ = (r/l) × 360°</span>), plus a <strong>circular base</strong> of radius <span class="math-inline">r</span>.</p>
          </div>
          <div class="ans-step">
            <div class="ans-step-title">3. Octahedron & Dodecahedron (Pages 83–84)</div>
            <p>• <strong>Regular Octahedron:</strong> 8 equilateral triangles. Just like the cube, an octahedron has exactly <strong>11 distinct nets</strong>!
            <br>• <strong>Regular Dodecahedron:</strong> 12 regular pentagons. Mathematicians have proven it has <strong>43,380 distinct nets</strong>!</p>
          </div>
          <div class="ans-step">
            <div class="ans-step-title">4. Why Can a Sphere Have No Flat Net? (Page 84)</div>
            <p>By Gauss's <em>Theorema Egregium</em>, a flat plane has zero Gaussian curvature (<span class="math-inline">K = 0</span>), whereas a sphere of radius <span class="math-inline">R</span> has positive Gaussian curvature (<span class="math-inline">K = 1/R²</span>). Because Gaussian curvature is an intrinsic invariant, no region of a sphere can be flattened onto a 2D plane without stretching, tearing, or wrinkling.</p>
          </div>
          <div class="ans-step">
            <div class="ans-step-title">Final Concluding Answer</div>
            <p>Tetrahedron has 2 nets; Cube and Octahedron each have 11 nets; Dodecahedron has 43,380 nets; Sphere has 0 flat nets.</p>
          </div>
        </div>
      </details>

      <!-- Q11: SHORTEST PATHS ON CUBOID (PAGES 84 - 87) -->
      <details class="ans-box">
        <summary>
          <span><span class="step-pill">Geodesic Challenge</span> Pages 84–87: Shortest paths between Ant and Laddu on a cube, on an 8×4×4 cuboid, and the 30×12×12 tricky case.</span>
        </summary>
        <div class="ans-content">
          <div class="ans-step">
            <div class="ans-step-title">Problem A: Cube with Ant at side center and Laddu at top center (Page 84)</div>
            <p>Let cube have side <span class="math-inline">s</span>. Unfold the side face and top face into two adjacent squares of size <span class="math-inline">s × s</span> sharing an edge.
            <br>• Ant is at <span class="math-inline">(s/2, s/2)</span> of side face. Laddu is at <span class="math-inline">(s/2, s/2)</span> of top face.
            <br>• They share the same lateral coordinate. Distance across the hinge edge = <span class="math-inline">s/2 + s/2 = s</span>.
            <br>• Straight line distance = <span class="math-inline">s</span> units. The straight red line on the net is the shortest path!</p>
          </div>
          <div class="ans-step">
            <div class="ans-step-title">Problem B: The 8 cm × 4 cm × 4 cm Cuboid (Page 86)</div>
            <p>Ant is at center of one 4×4 end face. Laddu is at center of opposite 4×4 end face.
            <br>• If unfolded in a straight line: The ant walks across the 8×4 top face.
            <br>Distance = <span class="math-inline">2 cm (to edge) + 8 cm (across face) + 2 cm (to laddu) = 12 cm</span>.
            <br>• Why the line went outside the net in the textbook diagram: The net was unfolded along side flaps that were disconnected from the top face! A path on a net is only physically valid if it traverses continuous paper without jumping across open air.</p>
          </div>
          <div class="ans-step">
            <div class="ans-step-title">Problem C: The 30 cm × 12 cm × 12 cm Tricky Case (Page 87)</div>
            <p>Ant is 1 cm from top on front 12×12 face, centered laterally. Laddu is 1 cm from bottom on rear 12×12 face, centered laterally.
            <br>• <strong>Unfolding 1 (Direct via Ceiling):</strong> <span class="math-inline">d = 1 + 30 + 11 = 42 cm</span>.
            <br>• <strong>Unfolding 2 (Single Side Wall):</strong> <span class="math-inline">d = √(42² + 10²) = √1864 ≈ 43.17 cm</span>.
            <br>• <strong>Unfolding 3 (Helical Spiral via 5 Faces):</strong>
            <br>Horizontal leg = <span class="math-inline">32 cm</span>.
            <br>Vertical leg = <span class="math-inline">24 cm</span>.
            <br>By Baudhāyana-Pythagoras theorem:
            <br><span class="math-inline">d = √(32² + 24²) = √(1024 + 576) = √1600 = 40.0 cm</span>!</p>
          </div>
          <div class="ans-step">
            <div class="ans-step-title">Step 4: Comparison & Verification</div>
            <p><span class="math-inline">40.0 cm &lt; 42.0 cm &lt; 43.17 cm</span>. The 40 cm path is the absolute global minimum geodesic!</p>
          </div>
          <div class="ans-step">
            <div class="ans-step-title">Step 5: Final Concluding Answer</div>
            <p>The length of the shortest path between the ant and the laddu is <strong>40 cm</strong>.</p>
          </div>
        </div>
      </details>
    </section>
"""
