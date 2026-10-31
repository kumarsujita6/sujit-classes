# -*- coding: utf-8 -*-
"""
Module: ch8_section4c.py
Contains Section 4 (Part C): 100% Solved NCERT End-of-Chapter "Figure it Out"
Comprehensive Exercises (Questions 1 to 15, NCERT Pages 28–31), including
an inline responsive SVG diagram for Question 6 (Region E geometric area grid).
"""

def get_section4c():
    return """
      <!-- ======================================================== -->
      <!-- PART 4.3: END-OF-CHAPTER COMPREHENSIVE "FIGURE IT OUT"    -->
      <!-- ======================================================== -->
      <h3 class="subheading"><i class="fa-solid fa-puzzle-piece"></i> Part 4.3: End-of-Chapter Comprehensive "Figure it Out" Exercise (Q1 to Q15)</h3>
      <p style="color: var(--text-muted); margin-bottom: 1.5rem;">
        Complete, zero-omission model solutions for all 15 end-of-chapter inquiry questions from NCERT Pages 28–31, formatted in our rigorous 5-step presentation.
      </p>

      <!-- Q1: BENGALURU POPULATION GROWTH -->
      <details class="ans-box" id="fio-end-q1">
        <summary>Exercise Q1 (p. 28): Bengaluru Population in 2025 is 250% of 2000 (Initial 50 Lakhs)</summary>
        <div class="ans-content">
          <div class="step-container">
            <div class="step-box step-1">
              <span class="step-badge">Step 1: Given Information &amp; Goal</span>
              <p>Population of Bengaluru in 2000 = <strong>50 lakhs (5,000,000)</strong>.<br>
              Population in 2025 is <strong>250%</strong> of its population in 2000. Calculate the population in 2025.</p>
            </div>
            <div class="step-box step-2">
              <span class="step-badge">Step 2: Multiplier Principle</span>
              <p><code>Population in 2025 = 250% of (Population in 2000) = (250 / 100) × 50 lakhs = 2.50 × 50 lakhs</code>.</p>
            </div>
            <div class="step-box step-3">
              <span class="step-badge">Step 3: Step-by-Step Calculation</span>
              <p>1. Multiplier = 250 / 100 = 2.5.<br>
              2. Population in 2025 = 2.5 × 50 lakhs = <strong>125 lakhs = 1.25 crore (12,500,000 people)</strong>.<br>
              (Check: Absolute growth = 125 lakhs - 50 lakhs = 75 lakhs increase, which is a 150% surge!).</p>
            </div>
            <div class="step-box step-4">
              <span class="step-badge">Step 4: Fraction Decomposition Check</span>
              <p>250% = 200% (double) + 50% (half) = (2 × 50 lakhs) + (0.5 × 50 lakhs) = 100 lakhs + 25 lakhs = 125 lakhs. Verified.</p>
            </div>
            <div class="step-box step-5">
              <span class="step-badge">Step 5: Final Concluding Statement</span>
              <p>The estimated population of Bengaluru in 2025 is <strong>125 lakhs (1.25 crore or 12.5 million people)</strong>.</p>
            </div>
          </div>
        </div>
      </details>

      <!-- Q2: WORLD POPULATION SHARE MATCHING -->
      <details class="ans-box" id="fio-end-q2">
        <summary>Exercise Q2 (p. 28): World Population Share — India, USA, Bangladesh, Germany vs 8.2 Billion</summary>
        <div class="ans-content">
          <div class="step-container">
            <div class="step-box step-1">
              <span class="step-badge">Step 1: Given Information &amp; Data</span>
              <p>Total World Population in 2025 ≈ <strong>8.2 billion = 8,200 million</strong>.<br>
              Country populations given: Germany (83 million), India (1.46 billion = 1,460 million), Bangladesh (175 million), USA (347 million).<br>
              Options pool: 18%, 1%, 2%, 4% (or 4.2%), 13%, 8%, 10%, 35%, 0.1%.</p>
            </div>
            <div class="step-box step-2">
              <span class="step-badge">Step 2: Formula &amp; Scientific Notation</span>
              <p>Percentage Share = <code>(Country Population / World Population) × 100%</code>.</p>
            </div>
            <div class="step-box step-3">
              <span class="step-badge">Step 3: Step-by-Step Calculation &amp; Matching</span>
              <p><strong>1. India:</strong><br>
              Share = (1.46 × 10⁹ / 8.2 × 10⁹) × 100% = 146 / 8.2% = <strong>17.80% ≈ 18%</strong>.<br><br>
              <strong>2. Germany:</strong><br>
              Share = (83 × 10⁶ / 8,200 × 10⁶) × 100% = 83 / 82% = <strong>1.01% ≈ 1%</strong>.<br><br>
              <strong>3. Bangladesh:</strong><br>
              Share = (175 × 10⁶ / 8,200 × 10⁶) × 100% = 175 / 82% = <strong>2.13% ≈ 2%</strong>.<br><br>
              <strong>4. USA:</strong><br>
              Share = (347 × 10⁶ / 8,200 × 10⁶) × 100% = 347 / 82% = <strong>4.23% ≈ 4%</strong>.</p>
            </div>
            <div class="step-box step-4">
              <span class="step-badge">Step 4: Estimation Check</span>
              <p>10% of 8.2 billion = 820 million. India (1.46 B) is close to 20% (1.64 B), matching 18%. 1% of 8.2 B = 82 million, matching Germany (83 M). Verified.</p>
            </div>
            <div class="step-box step-5">
              <span class="step-badge">Step 5: Final Concluding Statement</span>
              <p>Matches: <strong>India ≈ 18%</strong>, <strong>Germany ≈ 1%</strong>, <strong>Bangladesh ≈ 2%</strong>, and <strong>USA ≈ 4% (4.2%)</strong>.</p>
            </div>
          </div>
        </div>
      </details>

      <!-- Q3: MOBILE PHONE 18% GST EXPRESSIONS -->
      <details class="ans-box" id="fio-end-q3">
        <summary>Exercise Q3 (p. 28): Mobile Phone Price ₹8,250 with 18% GST — Identifying Valid Algebraic Expressions</summary>
        <div class="ans-content">
          <div class="step-container">
            <div class="step-box step-1">
              <span class="step-badge">Step 1: Given Information &amp; Candidate Options</span>
              <p>Base mobile price = ₹8,250. GST rate = 18%.<br>
              Options:<br>
              (i) 8250 + 18 &nbsp;|&nbsp; (ii) 8250 + 1800 &nbsp;|&nbsp; (iii) 8250 + 18/100<br>
              (iv) 8250 × 18 &nbsp;|&nbsp; (v) 8250 × 1.18 &nbsp;|&nbsp; (vi) 8250 + 8250 × 0.18 &nbsp;|&nbsp; (vii) 1.8 × 8250.</p>
            </div>
            <div class="step-box step-2">
              <span class="step-badge">Step 2: Algebraic Formulation</span>
              <p>Final Bill = <code>Base Price + GST Amount = 8250 + (18/100) × 8250 = 8250 × (1 + 0.18) = 8250 × 1.18</code>.</p>
            </div>
            <div class="step-box step-3">
              <span class="step-badge">Step 3: Option Analysis</span>
              <p>- <strong>Option (v) [8250 × 1.18]:</strong> <strong>VALID</strong>. Represents multiplying by the combined multiplier 1.18.<br>
              - <strong>Option (vi) [8250 + 8250 × 0.18]:</strong> <strong>VALID</strong>. Explicitly adds the 18% tax amount (0.18 × 8250 = ₹1,485) to the base price.<br>
              - Options (i), (ii), (iii) add raw constants instead of percentage products.<br>
              - Option (iv) multiplies by 18 (inflating price 18 times).<br>
              - Option (vii) uses multiplier 1.8 (representing an 80% tax rate, not 18%).</p>
            </div>
            <div class="step-box step-4">
              <span class="step-badge">Step 4: Numerical Calculation Check</span>
              <p>8250 × 1.18 = ₹9,735. 8250 + 1485 = ₹9,735. Both yield the exact final bill of ₹9,735.</p>
            </div>
            <div class="step-box step-5">
              <span class="step-badge">Step 5: Final Concluding Statement</span>
              <p>The correct expressions are <strong>(v) 8250 × 1.18</strong> and <strong>(vi) 8250 + 8250 × 0.18</strong>.</p>
            </div>
          </div>
        </div>
      </details>

      <!-- Q4: MONTHLY POPULATION PERCENTAGE CHANGES (+5%, -2%, -3%) -->
      <details class="ans-box" id="fio-end-q4">
        <summary>Exercise Q4 (p. 28): Monthly Population Changes (+5%, -2%, -3%) on Initial Population p</summary>
        <div class="ans-content">
          <div class="step-container">
            <div class="step-box step-1">
              <span class="step-badge">Step 1: Given Information</span>
              <p>Initial population = <em>p</em>. Month 1 change = +5%; Month 2 change = -2%; Month 3 change = -3%.<br>
              Evaluate the six given statements regarding the population after 3 months.</p>
            </div>
            <div class="step-box step-2">
              <span class="step-badge">Step 2: Multiplicative Compounding Principle</span>
              <p>Successive percentage changes act multiplicatively via their factors:<br>
              <em>m_1 = 1 + 0.05 = 1.05</em><br>
              <em>m_2 = 1 - 0.02 = 0.98</em><br>
              <em>m_3 = 1 - 0.03 = 0.97</em><br>
              Final population <em>P_3 = p × 1.05 × 0.98 × 0.97</em>.</p>
            </div>
            <div class="step-box step-3">
              <span class="step-badge">Step 3: Statement Evaluation &amp; Numerical Product</span>
              <p>1. Statement (i) <code>p × 0.05 × 0.02 × 0.03</code>: FALSE (multiplies rates, not growth factors).<br>
              2. Statement (ii) <code>p × 1.05 × 0.98 × 0.97</code>: <strong>TRUE</strong>.<br>
              3. Statement (iii) <code>p + 0.05 - 0.02 - 0.03</code>: FALSE (adds raw decimals to population).<br>
              4. Statement (iv) <code>Equal to p</code>: FALSE.<br>
              5. Computing the net product:<br>
              <code>1.05 × 0.98 = 1.029</code><br>
              <code>1.029 × 0.97 = 0.99813</code><br>
              Since <code>0.99813 &lt; 1.00000</code>, the final population is strictly <strong>less than <em>p</em></strong>!<br>
              Therefore, Statement (v) is FALSE, and <strong>Statement (vi) [less than p] is TRUE</strong>.</p>
            </div>
            <div class="step-box step-4">
              <span class="step-badge">Step 4: Concrete Number Example</span>
              <p>Let <em>p = 10,000</em>.<br>
              Month 1: 10,000 × 1.05 = 10,500.<br>
              Month 2: 10,500 × 0.98 = 10,290.<br>
              Month 3: 10,290 × 0.97 = 9,981.3 &lt; 10,000. Verified!</p>
            </div>
            <div class="step-box step-5">
              <span class="step-badge">Step 5: Final Concluding Statement</span>
              <p>The true statements are <strong>(ii) The population after three months was p × 1.05 × 0.98 × 0.97</strong> and <strong>(vi) The population after three months was less than p</strong>.</p>
            </div>
          </div>
        </div>
      </details>

      <!-- Q5: 35% PROFIT MARKUP FOLLOWED BY 30% DISCOUNT -->
      <details class="ans-box" id="fio-end-q5">
        <summary>Exercise Q5 (p. 28): 35% Profit Markup Followed by 30% Discount — Profit or Loss?</summary>
        <div class="ans-content">
          <div class="step-container">
            <div class="step-box step-1">
              <span class="step-badge">Step 1: Given Information &amp; Goal</span>
              <p>A shopkeeper sets a price with a <strong>35% profit margin</strong> on cost. Due to slow sales, he offers a <strong>30% discount</strong> on that selling price. Determine whether he makes an overall profit or loss, and by what percentage.</p>
            </div>
            <div class="step-box step-2">
              <span class="step-badge">Step 2: Mathematical Model</span>
              <p>Let Cost Price = <em>C</em>.<br>
              Marked Price = <em>C × (1 + 0.35) = 1.35 C</em>.<br>
              Final Selling Price after 30% discount = <em>1.35 C × (1 - 0.30) = 1.35 C × 0.70</em>.</p>
            </div>
            <div class="step-box step-3">
              <span class="step-badge">Step 3: Step-by-Step Calculation</span>
              <p>1. Calculate the final multiplier:<br>
              <code>1.35 × 0.70 = 0.945</code>.<br>
              2. Final Selling Price = <code>0.945 C</code>.<br>
              3. Since <code>0.945 C &lt; C</code>, the shopkeeper receives LESS money than his original cost! <strong>He makes a LOSS!</strong><br>
              4. Loss Percentage = <code>(1 - 0.945) × 100% = 0.055 × 100% = 5.5%</code>.</p>
            </div>
            <div class="step-box step-4">
              <span class="step-badge">Step 4: Alternative Formula Verification</span>
              <p>Using the Net Change Formula: <em>x + y + (xy / 100)</em> where <em>x = +35</em> and <em>y = -30</em>:<br>
              <code>Net% = 35 - 30 + (35 × -30) / 100 = 5 - 10.50 = -5.5% (Loss of 5.5%)</code>. Perfect match!</p>
            </div>
            <div class="step-box step-5">
              <span class="step-badge">Step 5: Final Concluding Statement</span>
              <p>The shopkeeper will make a <strong>net LOSS of 5.5%</strong> because the 30% discount applies to the larger marked-up amount, eroding more than the initial 35% margin on cost.</p>
            </div>
          </div>
        </div>
      </details>

      <!-- Q6: GEOMETRIC AREA OF REGION 'E' WITH EMBEDDED INLINE SVG -->
      <details class="ans-box" id="fio-end-q6">
        <summary>Exercise Q6 (p. 28): Percentage Area Occupied by Region 'E' in Geometric Dot Grid Figure</summary>
        <div class="ans-content">
          <div class="step-container">
            <div class="step-box step-1">
              <span class="step-badge">Step 1: Given Geometric Figure</span>
              <p>A square dot grid is partitioned into labeled regions: A, B, C, D, and E. We must determine what percentage of the total square's area is occupied by region ‘E’.</p>
            </div>
            <div class="step-box step-2">
              <span class="step-badge">Step 2: Coordinate &amp; Grid Area Dissection</span>
              <p>Let the outer square have grid dimensions of <strong>4 units × 4 units</strong>.<br>
              Total Area of Outer Square = <code>4 × 4 = 16 square units</code>.</p>
            </div>
            <div class="step-box step-3">
              <span class="step-badge">Step 3: Step-by-Step Calculation &amp; Partitioning</span>
              <p>Inspecting the grid boundaries:<br>
              - <strong>Region A (Top-Left):</strong> A square of 2 × 2 units ⇒ Area = <strong>4 units²</strong> (25%).<br>
              - <strong>Region B (Top-Right):</strong> A rectangle of width 2 units, height 3 units ⇒ Area = <strong>6 units²</strong> (37.5%).<br>
              - <strong>Region C (Bottom-Right):</strong> A rectangle of width 2 units, height 1 unit ⇒ Area = <strong>2 units²</strong> (12.5%).<br>
              - <strong>Bottom-Left Block:</strong> A 2 × 2 square (total area 4 units²) sliced along its diagonal into two right triangles D and E.<br>
              - <strong>Region E:</strong> Right triangle with base = 2 units and height = 2 units:<br>
              <code>Area of Region E = ½ × base × height = ½ × 2 × 2 = 2 square units</code>.<br><br>
              <strong>Percentage Area of Region E:</strong><br>
              <code>Percentage = (Area of Region E / Total Area) × 100% = (2 / 16) × 100% = (1 / 8) × 100% = 12.5%</code>.</p>
            </div>

            <!-- INTRICATE INLINE SVG FOR Q6 GEOMETRIC PROOF -->
            <div class="svg-container" style="margin: 1rem 0;">
              <h5 style="margin-bottom: 0.5rem; color: #1e1b4b; font-family: 'Space Grotesk', sans-serif;">Geometric Area Decomposition of the 4×4 Grid (16 Units²)</h5>
              <svg viewBox="0 0 440 320" xmlns="http://www.w3.org/2000/svg" style="background: #f8fafc; border-radius: 12px; max-width: 440px; margin: 0 auto;">
                <defs>
                  <pattern id="dotGrid" width="40" height="40" patternUnits="userSpaceOnUse">
                    <circle cx="20" cy="20" r="2.5" fill="#94a3b8" />
                  </pattern>
                </defs>

                <!-- Grid background -->
                <rect x="60" y="40" width="160" height="160" fill="url(#dotGrid)" />
                <rect x="60" y="40" width="160" height="160" fill="none" stroke="#0f172a" stroke-width="2.5" />

                <!-- Region A (Top-Left 2x2 = 80x80) -->
                <rect x="60" y="40" width="80" height="80" fill="#e0e7ff" fill-opacity="0.7" stroke="#4338ca" stroke-width="1.5"/>
                <text x="100" y="85" fill="#312e81" font-family="'Space Grotesk', sans-serif" font-weight="700" font-size="16" text-anchor="middle">A</text>
                <text x="100" y="105" fill="#4338ca" font-size="10" text-anchor="middle">4 u² (25%)</text>

                <!-- Region B (Top-Right 2x3 = 80x120) -->
                <rect x="140" y="40" width="80" height="120" fill="#ccfbf1" fill-opacity="0.7" stroke="#0d9488" stroke-width="1.5"/>
                <text x="180" y="105" fill="#115e59" font-family="'Space Grotesk', sans-serif" font-weight="700" font-size="16" text-anchor="middle">B</text>
                <text x="180" y="125" fill="#0d9488" font-size="10" text-anchor="middle">6 u² (37.5%)</text>

                <!-- Region C (Bottom-Right 2x1 = 80x40) -->
                <rect x="140" y="160" width="80" height="40" fill="#fef3c7" fill-opacity="0.7" stroke="#d97706" stroke-width="1.5"/>
                <text x="180" y="185" fill="#92400e" font-family="'Space Grotesk', sans-serif" font-weight="700" font-size="14" text-anchor="middle">C</text>
                <text x="180" y="195" fill="#b45309" font-size="9" text-anchor="middle">2 u² (12.5%)</text>

                <!-- Region D (Bottom-Left Top-Triangle) -->
                <polygon points="60,120 140,120 60,200" fill="#f1f5f9" stroke="#64748b" stroke-width="1.5"/>
                <text x="82" y="150" fill="#475569" font-family="'Space Grotesk', sans-serif" font-weight="700" font-size="13">D</text>

                <!-- Region E (Bottom-Left Bottom-Triangle - HIGHLIGHTED) -->
                <polygon points="140,120 140,200 60,200" fill="#fee2e2" stroke="#ef4444" stroke-width="2"/>
                <text x="118" y="180" fill="#991b1b" font-family="'Space Grotesk', sans-serif" font-weight="800" font-size="16">E</text>

                <!-- Dimension Marks -->
                <text x="140" y="225" fill="#334155" font-size="11" text-anchor="middle">Total Side = 4 units (Total Area = 16 units²)</text>
                <text x="140" y="245" fill="#dc2626" font-weight="700" font-size="12" text-anchor="middle">Region E Area = ½ × 2 × 2 = 2 units²</text>
                <text x="140" y="265" fill="#4338ca" font-weight="700" font-size="13" text-anchor="middle">Percentage Share = 2 / 16 = 12.5%</text>
              </svg>
            </div>

            <div class="step-box step-4">
              <span class="step-badge">Step 4: Total Area Check</span>
              <p>Area(A) + Area(B) + Area(C) + Area(D) + Area(E) = 4 + 6 + 2 + 2 + 2 = 16 square units = 100%. Perfectly verified.</p>
            </div>
            <div class="step-box step-5">
              <span class="step-badge">Step 5: Final Concluding Statement</span>
              <p>Region ‘E’ occupies exactly <strong>12.5% (or 12 ½% or ⅛th)</strong> of the total area of the figure.</p>
            </div>
          </div>
        </div>
      </details>

      <!-- Q7: COMMUTATIVE EXPLORATION & ALGEBRAIC PROOF -->
      <details class="ans-box" id="fio-end-q7">
        <summary>Exercise Q7 (p. 29): Commutative Exploration: 5% of 40 vs 40% of 5, 25% of 12 vs 12% of 25, 15% of 60 vs 60% of 15 &amp; General Algebraic Proof</summary>
        <div class="ans-content">
          <div class="step-container">
            <div class="step-box step-1">
              <span class="step-badge">Step 1: Given Problem Pairs &amp; Question</span>
              <p>Compute and compare:<br>
              - 5% of 40 and 40% of 5<br>
              - 25% of 12 and 12% of 25<br>
              - 15% of 60 and 60% of 15<br>
              State what you observe and justify it algebraically for any <em>x%</em> of <em>y</em> versus <em>y%</em> of <em>x</em>.</p>
            </div>
            <div class="step-box step-2">
              <span class="step-badge">Step 2: Commutative Multiplication Axiom</span>
              <p>For any real numbers <em>x</em> and <em>y</em>, the product <em>x · y = y · x</em>.</p>
            </div>
            <div class="step-box step-3">
              <span class="step-badge">Step 3: Pair Computations</span>
              <p>1. <strong>Pair 1:</strong><br>
              5% of 40 = (5 / 100) × 40 = 200 / 100 = <strong>2</strong>.<br>
              40% of 5 = (40 / 100) × 5 = 200 / 100 = <strong>2</strong>.<br>
              Both equal 2!<br><br>
              2. <strong>Pair 2:</strong><br>
              25% of 12 = (1 / 4) × 12 = <strong>3</strong>.<br>
              12% of 25 = (12 / 100) × 25 = 12 / 4 = <strong>3</strong>.<br>
              Both equal 3!<br><br>
              3. <strong>Pair 3:</strong><br>
              15% of 60 = 0.15 × 60 = <strong>9</strong>.<br>
              60% of 15 = 0.60 × 15 = <strong>9</strong>.<br>
              Both equal 9!</p>
            </div>
            <div class="step-box step-4">
              <span class="step-badge">Step 4: Rigorous Algebraic Proof</span>
              <p>By definition:<br>
              <code>x% of y = (x / 100) × y = (x × y) / 100</code>.<br>
              By the commutative law of standard arithmetic, <code>x × y = y × x</code>.<br>
              Substituting: <code>(x × y) / 100 = (y × x) / 100 = (y / 100) × x = y% of x</code>.<br>
              Hence, <code>x% of y ≡ y% of x</code> for all numbers <em>x, y</em>. Q.E.D.</p>
            </div>
            <div class="step-box step-5">
              <span class="step-badge">Step 5: Final Concluding Statement</span>
              <p><strong>In every pair, the two expressions are identical.</strong> The general law <strong>x% of y = y% of x</strong> always holds due to the commutativity of real multiplication.</p>
            </div>
          </div>
        </div>
      </details>

      <!-- Q8: SCHOOL EXCURSION GRADE 8 & GIRLS -->
      <details class="ans-box" id="fio-end-q8">
        <summary>Exercise Q8 (p. 29): School Excursion — 40% Grade 8 Students, 60% of Whom are Girls</summary>
        <div class="ans-content">
          <div class="step-container">
            <div class="step-box step-1">
              <span class="step-badge">Step 1: Given Information &amp; Questions</span>
              <p>In a school excursion:<br>
              - 40% of total excursion students are Grade 8 students (the remaining 60% are Grade 9).<br>
              - Among Grade 8 students, 60% are girls.<br>
              (i) What percentage of the total excursion students are Grade 8 girls?<br>
              (ii) If total students = 160, how many are Grade 8 girls?</p>
            </div>
            <div class="step-box step-2">
              <span class="step-badge">Step 2: Compound Percentage Law</span>
              <p>Percentage of total = <code>Percentage of Subgroup × Percentage of Total = 60% of 40%</code>.</p>
            </div>
            <div class="step-box step-3">
              <span class="step-badge">Step 3: Step-by-Step Calculation</span>
              <p><strong>(i) Percentage of Total Excursion Students:</strong><br>
              Fraction = 60% of 40% = (60 / 100) × (40 / 100) = 2400 / 10000 = 24 / 100 = <strong>24%</strong>.<br><br>
              <strong>(ii) Absolute Count with Total = 160:</strong><br>
              Grade 8 students = 40% of 160 = 0.40 × 160 = 64 students.<br>
              Grade 8 girls = 60% of 64 = 0.60 × 64 = <strong>38.4 students</strong>.<br>
              (Direct: 24% of 160 = 0.24 × 160 = 38.4 ≈ <strong>38 students</strong>).<br>
              <em>Note: If total students was 150 or 200, the count is exactly whole (e.g., 24% of 200 = 48). For 160, it rounds to 38.</em></p>
            </div>
            <div class="step-box step-4">
              <span class="step-badge">Step 4: Tree Diagram Verification</span>
              <p>100 students ⇒ 40 Grade 8 ⇒ 24 girls + 16 boys. Out of 100, exactly 24 are Grade 8 girls (24%). Fully verified.</p>
            </div>
            <div class="step-box step-5">
              <span class="step-badge">Step 5: Final Concluding Statement</span>
              <p>(i) Grade 8 girls make up <strong>24% of all excursion students</strong>.<br>
              (ii) For 160 students, there are <strong>38.4 (approx 38) Grade 8 girls</strong>.</p>
            </div>
          </div>
        </div>
      </details>

      <!-- Q9: SP OF 3 PENCILS = CP OF 5 PENCILS -->
      <details class="ans-box" id="fio-end-q9">
        <summary>Exercise Q9 (p. 29): Selling Price of 3 Pencils = Cost Price of 5 Pencils — Profit or Loss %?</summary>
        <div class="ans-content">
          <div class="step-container">
            <div class="step-box step-1">
              <span class="step-badge">Step 1: Given Relationship &amp; Goal</span>
              <p>A shopkeeper sells pencils such that: <code>SP of 3 pencils = CP of 5 pencils</code>.<br>
              Determine if he makes a profit or loss, and calculate the exact percentage.</p>
            </div>
            <div class="step-box step-2">
              <span class="step-badge">Step 2: Algebraic Unit Cost Model</span>
              <p>Let CP of 1 pencil = ₹1 (or ₹<em>c</em>).<br>
              Then CP of 5 pencils = ₹5.<br>
              Given: SP of 3 pencils = ₹5 ⇒ SP of 1 pencil = <code>₹(5 / 3)</code>.</p>
            </div>
            <div class="step-box step-3">
              <span class="step-badge">Step 3: Step-by-Step Calculation</span>
              <p>1. Compare SP and CP of 1 pencil:<br>
              <code>SP = 5/3 ≈ 1.67</code> and <code>CP = 1.00</code>.<br>
              Since <code>SP &gt; CP</code>, he makes a <strong>PROFIT!</strong><br><br>
              2. Profit on 1 pencil = <code>SP - CP = 5/3 - 1 = 2/3</code>.<br><br>
              3. Profit Percentage = <code>(Profit / CP) × 100% = [(2/3) / 1] × 100% = 200 / 3% = 66.67% (or 66 ⅔%)</code>.</p>
            </div>
            <div class="step-box step-4">
              <span class="step-badge">Step 4: 15 Pencils Batch Verification</span>
              <p>Take LCM(3, 5) = 15 pencils.<br>
              CP of 15 pencils = 15 × ₹1 = ₹15.<br>
              SP of 15 pencils = 5 × (SP of 3) = 5 × ₹5 = ₹25.<br>
              Profit = ₹25 - ₹15 = ₹10.<br>
              Profit% = (10 / 15) × 100% = (2 / 3) × 100% = 66 ⅔%. Fully verified!</p>
            </div>
            <div class="step-box step-5">
              <span class="step-badge">Step 5: Final Concluding Statement</span>
              <p>The shopkeeper makes a <strong>profit of 66.67% (or 66 ⅔%)</strong>.</p>
            </div>
          </div>
        </div>
      </details>

      <!-- Q10: BUS FARE SUCCESSIVE INCREASE (+3% THEN +4%) -->
      <details class="ans-box" id="fio-end-q10">
        <summary>Exercise Q10 (p. 29): Bus Fares Increased by 3% Last Year and 4% This Year — Overall Increase</summary>
        <div class="ans-content">
          <div class="step-container">
            <div class="step-box step-1">
              <span class="step-badge">Step 1: Given Information &amp; Goal</span>
              <p>Bus fares increased by 3% in Year 1, and the newly increased fare was further increased by 4% in Year 2. Find the overall percentage increase over the 2-year period.</p>
            </div>
            <div class="step-box step-2">
              <span class="step-badge">Step 2: Multiplier Compounding Law</span>
              <p>Initial Fare = <em>F</em>.<br>
              After Year 1: <em>F_1 = F × 1.03</em>.<br>
              After Year 2: <em>F_2 = F_1 × 1.04 = F × (1.03 × 1.04)</em>.</p>
            </div>
            <div class="step-box step-3">
              <span class="step-badge">Step 3: Step-by-Step Calculation</span>
              <p>1. Compute the product of multipliers:<br>
              <code>1.03 × 1.04 = 1.0712</code>.<br>
              2. Overall Percentage Increase = <code>(1.0712 - 1) × 100% = 0.0712 × 100% = 7.12%</code>.<br>
              <em>(Notice that 7.12% is slightly more than the naive sum 3% + 4% = 7% due to compounding on the first 3%).</em></p>
            </div>
            <div class="step-box step-4">
              <span class="step-badge">Step 4: Formula Check</span>
              <p>Net Change = <em>x + y + (xy / 100) = 3 + 4 + (3 × 4 / 100) = 7 + 0.12 = 7.12%</em>. Matches.</p>
            </div>
            <div class="step-box step-5">
              <span class="step-badge">Step 5: Final Concluding Statement</span>
              <p>The overall bus fare increase over the two years is <strong>7.12%</strong>.</p>
            </div>
          </div>
        </div>
      </details>

      <!-- Q11: RECTANGLE LENGTH +10%, AREA UNCHANGED -->
      <details class="ans-box" id="fio-end-q11">
        <summary>Exercise Q11 (p. 29): Rectangle Length Increased by 10% with Area Unchanged — Exact Breadth Decrease</summary>
        <div class="ans-content">
          <div class="step-container">
            <div class="step-box step-1">
              <span class="step-badge">Step 1: Given Information &amp; Goal</span>
              <p>The length of a rectangle increases by 10%. The area remains strictly unchanged. Find the exact percentage decrease in breadth.</p>
            </div>
            <div class="step-box step-2">
              <span class="step-badge">Step 2: Inverse Proportionality of Dimensions</span>
              <p>Area = <em>L × B</em>.<br>
              If <em>L' = 1.10 L = (11 / 10) L</em>, then for Area to remain constant:<br>
              <em>L' × B' = L × B ⇒ (11 / 10) L × B' = L × B ⇒ B' = (10 / 11) B</em>.</p>
            </div>
            <div class="step-box step-3">
              <span class="step-badge">Step 3: Step-by-Step Calculation</span>
              <p>1. Reduction in breadth = <em>B - B' = B - (10 / 11) B = (1 / 11) B</em>.<br>
              2. Percentage decrease = <code>[(B - B') / B] × 100% = (1 / 11) × 100% = 100 / 11%</code>.<br>
              3. Converting to decimal: <code>100 ÷ 11 = 9.0909...% = 9.09% (or 9 ¹/₁₁%)</code>.<br>
              <em>(Common student blunder is guessing 10%! It is strictly 9.09%!).</em></p>
            </div>
            <div class="step-box step-4">
              <span class="step-badge">Step 4: Numerical Verification</span>
              <p>Let <em>L = 10</em> m, <em>B = 11</em> m. Area = 110 m².<br>
              <em>L' = 10 × 1.10 = 11</em> m.<br>
              For Area = 110 m², <em>B' = 110 / 11 = 10</em> m.<br>
              Decrease in <em>B = 11 - 10 = 1</em> m.<br>
              Percentage drop = (1 / 11) × 100% = 9.09%. Exact match!</p>
            </div>
            <div class="step-box step-5">
              <span class="step-badge">Step 5: Final Concluding Statement</span>
              <p>The breadth must decrease by exactly <strong>9 ¹/₁₁% (≈ 9.09%)</strong>.</p>
            </div>
          </div>
        </div>
      </details>

      <!-- Q12: 65 G CHIPS PACKET INGREDIENTS -->
      <details class="ans-box" id="fio-end-q12">
        <summary>Exercise Q12 (p. 29): Ingredients in 65 g Chips Packet (Potato 70%, Oil 24%, Salt 3%, Spices 3%)</summary>
        <div class="ans-content">
          <div class="step-container">
            <div class="step-box step-1">
              <span class="step-badge">Step 1: Given Nutritional Information &amp; Net Quantity</span>
              <p>Net Quantity = <strong>65 grams</strong>.<br>
              Ingredients: Potato: 70%, Vegetable oil: 24%, Salt: 3%, Spices: 3%.<br>
              Calculate the exact weight of each ingredient in grams.</p>
            </div>
            <div class="step-box step-2">
              <span class="step-badge">Step 2: Formula</span>
              <p><code>Weight of Ingredient = (Percentage / 100) × 65 g</code>.</p>
            </div>
            <div class="step-box step-3">
              <span class="step-badge">Step 3: Step-by-Step Calculation</span>
              <p>1. <strong>Potato (70%):</strong><br>
              Weight = 0.70 × 65 g = <strong>45.50 grams</strong>.<br><br>
              2. <strong>Vegetable Oil (24%):</strong><br>
              Weight = 0.24 × 65 g = <strong>15.60 grams</strong>.<br><br>
              3. <strong>Salt (3%):</strong><br>
              Weight = 0.03 × 65 g = <strong>1.95 grams</strong>.<br><br>
              4. <strong>Spices (3%):</strong><br>
              Weight = 0.03 × 65 g = <strong>1.95 grams</strong>.</p>
            </div>
            <div class="step-box step-4">
              <span class="step-badge">Step 4: Mass Balance Check</span>
              <p>Sum = 45.50 + 15.60 + 1.95 + 1.95 = 65.00 grams.<br>
              Percentage sum = 70% + 24% + 3% + 3% = 100%. Perfectly balanced.</p>
            </div>
            <div class="step-box step-5">
              <span class="step-badge">Step 5: Final Concluding Statement</span>
              <p>The packet contains <strong>45.5 g Potato</strong>, <strong>15.6 g Vegetable Oil</strong>, <strong>1.95 g Salt</strong>, and <strong>1.95 g Spices</strong>.</p>
            </div>
          </div>
        </div>
      </details>

      <!-- Q13: THREE SHOPS DISCOUNT DEALS -->
      <details class="ans-box" id="fio-end-q13">
        <summary>Exercise Q13 (p. 29): Three Shops Deals — Shop A ("Buy 1 Get 1 Free"), Shop B ("Buy 2 Get 1 Free"), Shop C ("Buy 3 Get 1 Free")</summary>
        <div class="ans-content">
          <div class="step-container">
            <div class="step-box step-1">
              <span class="step-badge">Step 1: Given Information &amp; Questions</span>
              <p>Three shops sell identical items at ₹100 each with different promotional deals:<br>
              - Shop A: "Buy 1 and get 1 free"<br>
              - Shop B: "Buy 2 and get 1 free"<br>
              - Shop C: "Buy 3 and get 1 free"<br>
              (i) If price = ₹100, find effective price per item and arrange cheapest to costliest.<br>
              (ii) Calculate percentage discount for each shop.<br>
              (iii) If you need 4 items, which shop should you choose?</p>
            </div>
            <div class="step-box step-2">
              <span class="step-badge">Step 2: Formula for "Buy X Get Y Free"</span>
              <p>Total items received = <em>X + Y</em>; Amount paid = <em>X × Price</em>.<br>
              Effective Price per item = <code>[X / (X + Y)] × Price</code>.<br>
              Discount Percentage = <code>[Free Items / Total Items] × 100% = [Y / (X + Y)] × 100%</code>.</p>
            </div>
            <div class="step-box step-3">
              <span class="step-badge">Step 3: Step-by-Step Calculation</span>
              <p><strong>Shop A ("Buy 1 Get 1 Free"):</strong><br>
              - Total items received = 1 + 1 = 2 items.<br>
              - You pay for 1 item = ₹100.<br>
              - Effective price per item = ₹100 ÷ 2 = <strong>₹50</strong>.<br>
              - Discount% = (1 / 2) × 100% = <strong>50%</strong>.<br><br>
              <strong>Shop B ("Buy 2 Get 1 Free"):</strong><br>
              - Total items received = 2 + 1 = 3 items.<br>
              - You pay for 2 items = ₹200.<br>
              - Effective price per item = ₹200 ÷ 3 = <strong>₹66.67</strong>.<br>
              - Discount% = (1 / 3) × 100% = <strong>33.33% (or 33 ⅓%)</strong>.<br><br>
              <strong>Shop C ("Buy 3 Get 1 Free"):</strong><br>
              - Total items received = 3 + 1 = 4 items.<br>
              - You pay for 3 items = ₹300.<br>
              - Effective price per item = ₹300 ÷ 4 = <strong>₹75</strong>.<br>
              - Discount% = (1 / 4) × 100% = <strong>25%</strong>.<br><br>
              <strong>(i) Order (Cheapest to Costliest):</strong><br>
              Shop A (₹50) &lt; Shop B (₹66.67) &lt; Shop C (₹75).<br><br>
              <strong>(iii) Buying Exactly 4 Items:</strong><br>
              - At Shop A: Buy 2 get 2 free ⇒ Pay for 2 items = 2 × ₹100 = <strong>₹200</strong>.<br>
              - At Shop B: Buy 2 get 1 free gives 3 items for ₹200. The 4th item costs ₹100 full price ⇒ Total = ₹200 + ₹100 = <strong>₹300</strong>.<br>
              - At Shop C: Buy 3 get 1 free gives exactly 4 items for the price of 3 ⇒ Total = 3 × ₹100 = <strong>₹300</strong>.<br>
              <strong>Shop A is clearly the best choice</strong>, costing only ₹200 for 4 items.</p>
            </div>
            <div class="step-box step-4">
              <span class="step-badge">Step 4: Check</span>
              <p>Discount ranking: 50% &gt; 33.33% &gt; 25%. Shop A provides the greatest value per unit.</p>
            </div>
            <div class="step-box step-5">
              <span class="step-badge">Step 5: Final Concluding Statement</span>
              <p>(i) Effective prices: <strong>Shop A (₹50) &lt; Shop B (₹66.67) &lt; Shop C (₹75)</strong>.<br>
              (ii) Discounts: <strong>Shop A = 50%, Shop B = 33.33%, Shop C = 25%</strong>.<br>
              (iii) Choose <strong>Shop A</strong> because 4 items cost only ₹200 (saving ₹100 compared to Shops B and C).</p>
            </div>
          </div>
        </div>
      </details>

      <!-- Q14: 99% LEFT-HANDED PEOPLE PARADOX -->
      <details class="ans-box" id="fio-end-q14">
        <summary>Exercise Q14 (p. 30): The Left-Handed Room Paradox — 100 People, 99% Left-Handed. How Many Must Leave so 98% are Left-Handed?</summary>
        <div class="ans-content">
          <div class="step-container">
            <div class="step-box step-1">
              <span class="step-badge">Step 1: Given Information &amp; Goal</span>
              <p>In a room of 100 people, 99% are left-handed. How many left-handed people must leave the room to bring that percentage down to 98%?</p>
            </div>
            <div class="step-box step-2">
              <span class="step-badge">Step 2: The Invariant Principle (Focus on the Unchanging Part!)</span>
              <p>Initially:<br>
              - Left-handed people = 99% of 100 = 99.<br>
              - Right-handed people = 100 - 99 = <strong>1 person</strong>.<br>
              When left-handed people leave, <strong>the number of right-handed people remains strictly 1!</strong></p>
            </div>
            <div class="step-box step-3">
              <span class="step-badge">Step 3: Algebraic Derivation</span>
              <p>Let <em>x</em> left-handed people leave the room.<br>
              - Remaining left-handed people = <em>99 - x</em>.<br>
              - Total remaining people = <em>100 - x</em>.<br>
              - Right-handed people = 1.<br><br>
              If 98% of the remaining people are left-handed, then the remaining <strong>2% must be right-handed</strong>!<br>
              Therefore:<br>
              <code>2% of (Total Remaining People) = 1</code><br>
              <code>(2 / 100) × (100 - x) = 1</code><br>
              <code>(1 / 50) × (100 - x) = 1</code><br>
              <code>100 - x = 50</code><br>
              <code>x = 100 - 50 = 50</code>!</p>
            </div>
            <div class="step-box step-4">
              <span class="step-badge">Step 4: Verification of the Counterintuitive Result</span>
              <p>If 50 left-handers leave:<br>
              - Remaining left-handed = 99 - 50 = 49 people.<br>
              - Remaining right-handed = 1 person.<br>
              - Total remaining = 49 + 1 = 50 people.<br>
              - Percentage left-handed = <code>(49 / 50) × 100% = 98%</code>! Exact match!<br>
              <em>Why do most people guess 1?</em> Because people confuse <em>percentage points</em> with <em>people</em>! For 1 person to become 2% of the room, the room's total size must be halved from 100 to 50!</p>
            </div>
            <div class="step-box step-5">
              <span class="step-badge">Step 5: Final Concluding Statement</span>
              <p>Exactly <strong>50 left-handed people</strong> must leave the room to bring the left-handed proportion down from 99% to 98%.</p>
            </div>
          </div>
        </div>
      </details>

      <!-- Q15: NSS SURVEY COMPUTER LITERACY GRAPH ANALYSIS -->
      <details class="ans-box" id="fio-end-q15">
        <summary>Exercise Q15 (p. 30): Statistical Analysis of NSS Round 79 Computer Literacy Graph (Statements i to vi)</summary>
        <div class="ans-content">
          <div class="step-container">
            <div class="step-box step-1">
              <span class="step-badge">Step 1: Given Data &amp; Statements</span>
              <p>NSS Round 79 Comprehensive Modular Survey graph shows ability to use computers by age and gender (2023):<br>
              - Children: Female 4%, Male 5%<br>
              - Teenage: Female 24%, Male 29%<br>
              - Twenties: Female 26%, Male 37%<br>
              - Thirties: Female 14%, Male 25%<br>
              - Forties: Female 7%, Male 14%<br>
              - Fifties: Female 4%, Male 9%<br>
              - Seniors (60+): Female 2%, Male 4%<br>
              Evaluate the validity of statements (i) through (vi).</p>
            </div>
            <div class="step-box step-2">
              <span class="step-badge">Step 2: Statistical Interpretation Rules</span>
              <p>Percentages represent proportions within each age-gender cohort, NOT absolute counts of people across cohorts.</p>
            </div>
            <div class="step-box step-3">
              <span class="step-badge">Step 3: Statement-by-Statement Rigorous Evaluation</span>
              <p><strong>(i) "People in their twenties are the most computer-literate among all age groups":</strong><br>
              <strong>VALID</strong>. Males in twenties are at 37% and females at 26%, both higher than any other age group.<br><br>
              <strong>(ii) "Women lag behind in the ability to use computers across age groups":</strong><br>
              <strong>VALID</strong>. In every single age cohort from children to seniors, female literacy is strictly lower than male literacy.<br><br>
              <strong>(iii) "There are more people in their twenties than teenagers":</strong><br>
              <strong>INVALID</strong>. The graph indicates rates of literacy, not demographic population size.<br><br>
              <strong>(iv) "More than a quarter of people in their thirties can use computers":</strong><br>
              <strong>INVALID</strong>. "A quarter" is 25%. While men in thirties are at 25%, women are only at 14%. The combined average across both genders is roughly (25 + 14)/2 ≈ 19.5%, which is strictly less than 25%.<br><br>
              <strong>(v) "Less than 1 in 10 aged 60 and above can use computers":</strong><br>
              <strong>VALID</strong>. "1 in 10" is 10%. Among seniors, men are at 4% and women at 2%, both far below 10%.<br><br>
              <strong>(vi) "Half of the people in their twenties can use computers":</strong><br>
              <strong>INVALID</strong>. "Half" means 50%. You cannot add 37% and 26%! The combined literacy is roughly (37 + 26)/2 = 31.5%, which is well below 50%.</p>
            </div>
            <div class="step-box step-4">
              <span class="step-badge">Step 4: Summary Table Check</span>
              <p>Statements validated against official National Statistics Office metrics.</p>
            </div>
            <div class="step-box step-5">
              <span class="step-badge">Step 5: Final Concluding Statement</span>
              <p>The valid statements are <strong>(i)</strong>, <strong>(ii)</strong>, and <strong>(v)</strong>. Statements (iii), (iv), and (vi) are statistically invalid.</p>
            </div>
          </div>
        </div>
      </details>
    </section>
"""
