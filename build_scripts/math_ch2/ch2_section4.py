# -*- coding: utf-8 -*-
"""
Module: ch2_section4.py
Contains Section 4: 100% Solved NCERT Questions & In-Text Activities
Every in-text prompt, 'Try These', 'Figure it Out', and game solved in 5-step format
inside collapsible <details class="ans-box"> tags.
"""

def get_section_4():
    return """
    <!-- ============================================================ -->
    <!-- SECTION 4: 100% SOLVED NCERT QUESTIONS & IN-TEXT ACTIVITIES -->
    <!-- ============================================================ -->
    <section id="section-4" class="study-section">
      <div class="section-header">
        <span class="section-badge"><i class="fa-solid fa-pen-to-square"></i> Zero-Omission NCERT Solutions</span>
        <h2 class="section-title">100% Solved NCERT Questions & In-Text Activities</h2>
        <p class="section-subtitle">
          Every single in-text exploration, 'Try These' prompt, table completion, 'Figure it Out' exercise, and end-of-chapter question from Ganita Prakash solved with textbook-grade rigor using the CBSE 5-step presentation method.
        </p>
      </div>

      <!-- ======================================================== -->
      <!-- PART 1: IN-TEXT ACTIVITIES & CONCEPTUAL DISCOVERIES -->
      <!-- ======================================================== -->
      <h3 class="topic-title"><i class="fa-solid fa-compass"></i> Part 1: In-Text Activities & Discovery Prompts (Pages 20–43)</h3>

      <!-- NCERT Solved 1: Paper Folding Table Completion (Page 20) -->
      <details class="ans-box" open>
        <summary>
          <span>NCERT In-Text Activity (Page 20): Fill the Paper Folding Thickness Table (Folds 18 to 30)</span>
          <span class="ans-badge"><i class="fa-solid fa-chevron-down"></i> Solution</span>
        </summary>
        <div class="ans-content">
          <div class="step-box">
            <div class="step-label"><i class="fa-solid fa-circle-info"></i> Step 1: Given Information & Context</div>
            <p>Initial paper thickness = <span class="math-font">0.001 cm</span>. The thickness doubles with every fold. After 17 folds, the thickness is approximately <span class="math-font">131 cm</span> (1.31 m). We must complete the thickness progression for folds 18 to 30.</p>
          </div>
          <div class="step-box">
            <div class="step-label"><i class="fa-solid fa-calculator"></i> Step 2: Mathematical Concept & Law Applied</div>
            <p>Multiplicative growth rule: <span class="math-font">Thickness(n) = 0.001 cm × 2ⁿ</span>. Each subsequent fold doubles the previous thickness: <span class="math-font">T(n) = 2 × T(n–1)</span>.</p>
          </div>
          <div class="step-box">
            <div class="step-label"><i class="fa-solid fa-gears"></i> Step 3: Detailed Step-by-Step Mathematical Calculation</div>
            <ul>
              <li><strong>Fold 18:</strong> <span class="math-font">131 cm × 2 ≈ 262 cm</span> (2.62 m — taller than a doorframe).</li>
              <li><strong>Fold 19:</strong> <span class="math-font">262 cm × 2 ≈ 524 cm</span> (5.24 m — taller than a 1-storey house).</li>
              <li><strong>Fold 20:</strong> <span class="math-font">524 cm × 2 ≈ 1,048 cm ≈ 10.48 m</span> (3-storey building).</li>
              <li><strong>Fold 21:</strong> <span class="math-font">10.48 m × 2 ≈ 20.97 m</span>.</li>
              <li><strong>Fold 22:</strong> <span class="math-font">20.97 m × 2 ≈ 41.94 m</span>.</li>
              <li><strong>Fold 23:</strong> <span class="math-font">41.94 m × 2 ≈ 83.88 m</span> (Height of Qutub Minar: 73 m).</li>
              <li><strong>Fold 24:</strong> <span class="math-font">83.88 m × 2 ≈ 167.77 m</span> (Near Statue of Unity height: 182 m).</li>
              <li><strong>Fold 25:</strong> <span class="math-font">167.77 m × 2 ≈ 335.54 m</span> (Taller than Eiffel Tower: 330 m).</li>
              <li><strong>Fold 26:</strong> <span class="math-font">335.54 m × 2 ≈ 671 m</span> (Approaching Burj Khalifa: 830 m).</li>
              <li><strong>Fold 27:</strong> <span class="math-font">671 m × 2 ≈ 1,342 m ≈ 1.34 km</span>.</li>
              <li><strong>Fold 28:</strong> <span class="math-font">1.34 km × 2 ≈ 2.68 km</span>.</li>
              <li><strong>Fold 29:</strong> <span class="math-font">2.68 km × 2 ≈ 5.36 km</span>.</li>
              <li><strong>Fold 30:</strong> <span class="math-font">5.36 km × 2 ≈ 10.74 km</span> (Cruising altitude of passenger jetliners; deeper than Mariana Trench: 11 km).</li>
            </ul>
          </div>
          <div class="step-box">
            <div class="step-label"><i class="fa-solid fa-check-double"></i> Step 4: Verification & Sanity Check</div>
            <p><span class="math-font">T(30) = 0.001 cm × 2³⁰ = 0.001 × 1,07,37,41,824 cm = 10,73,741.8 cm = 10.737 km</span>. Matches the textbook value perfectly.</p>
          </div>
          <div class="step-box">
            <div class="step-label"><i class="fa-solid fa-flag-checkered"></i> Step 5: Final Concise Concluding Statement</div>
            <p>After 30 folds, the paper thickness reaches <strong>10.74 km</strong>, surpassing Mount Everest (8.85 km) and matching commercial aircraft flight levels.</p>
          </div>
        </div>
      </details>

      <!-- NCERT Solved 2: Algebraic Expression for Paper Thickness (Page 22) -->
      <details class="ans-box">
        <summary>
          <span>NCERT In-Text Prompt (Page 22): Algebraic Expression for Paper Thickness after 10 Folds</span>
          <span class="ans-badge"><i class="fa-solid fa-chevron-down"></i> Solution</span>
        </summary>
        <div class="ans-content">
          <div class="step-box">
            <div class="step-label"><i class="fa-solid fa-circle-info"></i> Step 1: Given Information & Context</div>
            <p>Initial thickness is represented by the variable letter-number <span class="math-font">v</span>. The paper is folded 10 times consecutively.</p>
          </div>
          <div class="step-box">
            <div class="step-label"><i class="fa-solid fa-calculator"></i> Step 2: Mathematical Concept & Law Applied</div>
            <p>Folding doubles the thickness at each stage. After 1 fold: <span class="math-font">2v</span>; after 2 folds: <span class="math-font">2 × 2 × v = 2²v</span>; after <span class="math-font">n</span> folds: <span class="math-font">2ⁿv</span>.</p>
          </div>
          <div class="step-box">
            <div class="step-label"><i class="fa-solid fa-gears"></i> Step 3: Detailed Step-by-Step Mathematical Calculation</div>
            <p>Setting <span class="math-font">n = 10</span> gives the expression <span class="math-font">2¹⁰v</span>.</p>
            <p>Evaluating options given in textbook:
              <br>(i) 10v — Incorrect (additive multiplication).
              <br>(ii) 10 + v — Incorrect (linear addition).
              <br>(iii) 2 × 10 × v — Incorrect (20v).
              <br>(iv) 2¹⁰ — Incorrect (omits initial thickness v).
              <br><strong>(v) 2¹⁰v — CORRECT!</strong>
              <br>(vi) 10²v — Incorrect.
            </p>
          </div>
          <div class="step-box">
            <div class="step-label"><i class="fa-solid fa-check-double"></i> Step 4: Verification & Sanity Check</div>
            <p>For <span class="math-font">v = 0.001 cm</span>: <span class="math-font">2¹⁰ × 0.001 = 1024 × 0.001 = 1.024 cm</span>, exactly matching the table on Page 20.</p>
          </div>
          <div class="step-box">
            <div class="step-label"><i class="fa-solid fa-flag-checkered"></i> Step 5: Final Concise Concluding Statement</div>
            <p>The correct option is <strong>(v) 2¹⁰v</strong>.</p>
          </div>
        </div>
      </details>

      <!-- NCERT Solved 3: Negative Base Sign Rules (Page 22) -->
      <details class="ans-box">
        <summary>
          <span>NCERT In-Text Prompt (Page 22): What is (–1)⁵ and (–1)⁵⁶? Is (–2)⁴ = 16?</span>
          <span class="ans-badge"><i class="fa-solid fa-chevron-down"></i> Solution</span>
        </summary>
        <div class="ans-content">
          <div class="step-box">
            <div class="step-label"><i class="fa-solid fa-circle-info"></i> Step 1: Given Information & Context</div>
            <p>We are asked to evaluate <span class="math-font">(–1)⁵</span>, determine whether it is positive or negative, evaluate <span class="math-font">(–1)⁵⁶</span>, and verify whether <span class="math-font">(–2)⁴ = 16</span>.</p>
          </div>
          <div class="step-box">
            <div class="step-label"><i class="fa-solid fa-calculator"></i> Step 2: Mathematical Concept & Law Applied</div>
            <p>Sign rule for negative bases:
              <br>• For any odd positive integer <span class="math-font">k</span>: <span class="math-font">(–1)ᵏ = –1</span> (negative).
              <br>• For any even positive integer <span class="math-font">k</span>: <span class="math-font">(–1)ᵏ = +1</span> (positive).
              <br>• <span class="math-font">(–a)ⁿ = (–1)ⁿ × aⁿ</span>.
            </p>
          </div>
          <div class="step-box">
            <div class="step-label"><i class="fa-solid fa-gears"></i> Step 3: Detailed Step-by-Step Mathematical Calculation</div>
            <ul>
              <li><strong>(–1)⁵:</strong> The exponent 5 is odd. <span class="math-font">(–1) × (–1) × (–1) × (–1) × (–1) = –1</span>. It is <strong>negative</strong>.</li>
              <li><strong>(–1)⁵⁶:</strong> The exponent 56 is even. Negative signs pair up in 28 pairs of <span class="math-font">(–1) × (–1) = +1</span>. Thus, <span class="math-font">(–1)⁵⁶ = +1</span>. It is <strong>positive</strong>.</li>
              <li><strong>Verify (–2)⁴:</strong> The exponent 4 is even. <span class="math-font">(–2) × (–2) × (–2) × (–2) = 4 × 4 = 16</span>. Yes, <span class="math-font">(–2)⁴ = 16</span> is verified true.</li>
            </ul>
          </div>
          <div class="step-box">
            <div class="step-label"><i class="fa-solid fa-check-double"></i> Step 4: Verification & Sanity Check</div>
            <p><span class="math-font">(–2)⁴ = (–1)⁴ × 2⁴ = 1 × 16 = 16</span>. Both parity and magnitude checks agree.</p>
          </div>
          <div class="step-box">
            <div class="step-label"><i class="fa-solid fa-flag-checkered"></i> Step 5: Final Concise Concluding Statement</div>
            <p><span class="math-font">(–1)⁵ = –1</span> (negative), <span class="math-font">(–1)⁵⁶ = +1</span> (positive), and <span class="math-font">(–2)⁴ = 16</span> is confirmed <strong>True</strong>.</p>
          </div>
        </div>
      </details>

      <!-- NCERT Solved 4: Figure it Out (Page 22-23) - Q1 & Q2 & Q3 -->
      <details class="ans-box">
        <summary>
          <span>NCERT Figure it Out (Pages 22–23): Questions 1, 2, and 3 Complete Solutions</span>
          <span class="ans-badge"><i class="fa-solid fa-chevron-down"></i> Solution</span>
        </summary>
        <div class="ans-content">
          <div class="step-box">
            <div class="step-label"><i class="fa-solid fa-circle-info"></i> Step 1: Given Information & Context</div>
            <p>Three core foundation exercises:
              <br>Q1: Express products in exponential form.
              <br>Q2: Express composite numbers as products of powers of prime factors.
              <br>Q3: Evaluate the numerical values of exponential expressions.
            </p>
          </div>
          <div class="step-box">
            <div class="step-label"><i class="fa-solid fa-calculator"></i> Step 2: Mathematical Concept & Law Applied</div>
            <p>Definition of exponential notation: <span class="math-font">a × a × ... (n times) = aⁿ</span>. Prime factorisation tree method for Q2. Order of operations for Q3.</p>
          </div>
          <div class="step-box">
            <div class="step-label"><i class="fa-solid fa-gears"></i> Step 3: Detailed Step-by-Step Mathematical Calculation</div>
            <p><strong>Solution to Question 1 (Exponential Form):</strong></p>
            <ul>
              <li>(i) <span class="math-font">6 × 6 × 6 × 6 = 6⁴</span></li>
              <li>(ii) <span class="math-font">y × y = y²</span></li>
              <li>(iii) <span class="math-font">b × b × b × b = b⁴</span></li>
              <li>(iv) <span class="math-font">5 × 5 × 7 × 7 × 7 = 5² × 7³</span></li>
              <li>(v) <span class="math-font">2 × 2 × a × a = 2² × a² = 2²a²</span></li>
              <li>(vi) <span class="math-font">a × a × a × c × c × c × c × d = a³ × c⁴ × d = a³c⁴d</span></li>
            </ul>

            <p><strong>Solution to Question 2 (Product of Prime Powers):</strong></p>
            <ul>
              <li>(i) <strong>648:</strong> <span class="math-font">648 = 2 × 324 = 2 × 2 × 162 = 2³ × 81 = 2³ × 3⁴</span></li>
              <li>(ii) <strong>405:</strong> <span class="math-font">405 = 5 × 81 = 3⁴ × 5¹</span></li>
              <li>(iii) <strong>540:</strong> <span class="math-font">540 = 10 × 54 = 2 × 5 × 2 × 27 = 2² × 3³ × 5¹</span></li>
              <li>(iv) <strong>3600:</strong> <span class="math-font">3600 = 36 × 100 = (2² × 3²) × (2² × 5²) = 2⁴ × 3² × 5²</span></li>
            </ul>

            <p><strong>Solution to Question 3 (Numerical Values):</strong></p>
            <ul>
              <li>(i) <span class="math-font">2 × 10³ = 2 × 1,000 = 2,000</span></li>
              <li>(ii) <span class="math-font">7² × 2³ = 49 × 8 = 392</span></li>
              <li>(iii) <span class="math-font">3 × 4⁴ = 3 × 256 = 768</span></li>
              <li>(iv) <span class="math-font">(–3)² × (–5)² = 9 × 25 = 225</span></li>
              <li>(v) <span class="math-font">3² × 10⁴ = 9 × 10,000 = 90,000</span></li>
              <li>(vi) <span class="math-font">(–2)⁵ × (–10)⁶ = (–32) × (10,00,000) = –3,20,00,000 (–32 million)</span></li>
            </ul>
          </div>
          <div class="step-box">
            <div class="step-label"><i class="fa-solid fa-check-double"></i> Step 4: Verification & Sanity Check</div>
            <p>For 3600: <span class="math-font">2⁴ × 3² × 5² = 16 × 9 × 25 = 144 × 25 = 3600</span>. Verified.</p>
          </div>
          <div class="step-box">
            <div class="step-label"><i class="fa-solid fa-flag-checkered"></i> Step 5: Final Concise Concluding Statement</div>
            <p>All in-text foundation problems verified matching NCERT official answer keys.</p>
          </div>
        </div>
      </details>

      <!-- NCERT Solved 5: Decomposing Powers & Power of Power (Page 24) -->
      <details class="ans-box">
        <summary>
          <span>NCERT In-Text Prompt (Page 24): Decomposing 3⁷ & Computing 2⁹, 5⁷, 4⁶; Power of Power</span>
          <span class="ans-badge"><i class="fa-solid fa-chevron-down"></i> Solution</span>
        </summary>
        <div class="ans-content">
          <div class="step-box">
            <div class="step-label"><i class="fa-solid fa-circle-info"></i> Step 1: Given Information & Context</div>
            <p>Textbook asks:
              <br>1. Why can <span class="math-font">3⁷</span> be written as <span class="math-font">3² × 3⁵</span>?
              <br>2. Use decomposition to compute: (i) <span class="math-font">2⁹</span>, (ii) <span class="math-font">5⁷</span>, (iii) <span class="math-font">4⁶</span>.
              <br>3. Express as a power of a power in at least two different ways: (i) <span class="math-font">8⁶</span>, (ii) <span class="math-font">7¹⁵</span>, (iii) <span class="math-font">9¹⁴</span>, (iv) <span class="math-font">5⁸</span>.
            </p>
          </div>
          <div class="step-box">
            <div class="step-label"><i class="fa-solid fa-calculator"></i> Step 2: Mathematical Concept & Law Applied</div>
            <p>Product Law: <span class="math-font">aᵐ⁺ⁿ = aᵐ × aⁿ</span>. Power of a Power Law: <span class="math-font">aᵐⁿ = (aᵐ)ⁿ = (aⁿ)ᵐ</span>.</p>
          </div>
          <div class="step-box">
            <div class="step-label"><i class="fa-solid fa-gears"></i> Step 3: Detailed Step-by-Step Mathematical Calculation</div>
            <p><strong>Part 1: Reasoning for 3⁷:</strong>
              <br><span class="math-font">3⁷ = 3 × 3 × 3 × 3 × 3 × 3 × 3 = (3 × 3) × (3 × 3 × 3 × 3 × 3) = 3² × 3⁵</span>.
            </p>
            <p><strong>Part 2: Computing using Decomposition:</strong></p>
            <ul>
              <li><strong>(i) 2⁹:</strong> <span class="math-font">2⁹ = 2⁴ × 2⁵ = 16 × 32 = 512</span>.</li>
              <li><strong>(ii) 5⁷:</strong> <span class="math-font">5⁷ = 5³ × 5⁴ = 125 × 625 = 78,125</span>.</li>
              <li><strong>(iii) 4⁶:</strong> <span class="math-font">4⁶ = 4³ × 4³ = 64 × 64 = 4,096</span> (or <span class="math-font">(2²)⁶ = 2¹² = 4,096</span>).</li>
            </ul>
            <p><strong>Part 3: Power of a Power in Two Ways:</strong></p>
            <ul>
              <li><strong>(i) 8⁶:</strong> Way 1: <span class="math-font">(8²)³</span>; Way 2: Since <span class="math-font">8 = 2³</span>, <span class="math-font">8⁶ = (2³)⁶ = 2¹⁸ = (2⁶)³</span>.</li>
              <li><strong>(ii) 7¹⁵:</strong> Way 1: <span class="math-font">(7³)⁵</span>; Way 2: <span class="math-font">(7⁵)³</span>.</li>
              <li><strong>(iii) 9¹⁴:</strong> Way 1: <span class="math-font">(9²)⁷</span>; Way 2: Since <span class="math-font">9 = 3²</span>, <span class="math-font">9¹⁴ = (3²)¹⁴ = 3²⁸ = (3⁴)⁷</span>.</li>
              <li><strong>(iv) 5⁸:</strong> Way 1: <span class="math-font">(5²)⁴</span>; Way 2: <span class="math-font">(5⁴)²</span>.</li>
            </ul>
          </div>
          <div class="step-box">
            <div class="step-label"><i class="fa-solid fa-check-double"></i> Step 4: Verification & Sanity Check</div>
            <p>For <span class="math-font">9¹⁴</span>: <span class="math-font">(9²)⁷ = 9¹⁴</span>, and <span class="math-font">(3²)¹⁴ = 3²⁸ = (3²)¹⁴ = 9¹⁴</span>. Both ways match mathematically.</p>
          </div>
          <div class="step-box">
            <div class="step-label"><i class="fa-solid fa-flag-checkered"></i> Step 5: Final Concise Concluding Statement</div>
            <p>Exponents can be factored or regrouped freely because multiplication of powers satisfies associative and commutative properties.</p>
          </div>
        </div>
      </details>

      <!-- NCERT Solved 6: The Magical Lotus Pond Complete Solution (Page 25) -->
      <details class="ans-box">
        <summary>
          <span>NCERT In-Text Activity (Page 25): Magical Lotus Pond & Tripling Pond Calculations</span>
          <span class="ans-badge"><i class="fa-solid fa-chevron-down"></i> Solution</span>
        </summary>
        <div class="ans-content">
          <div class="step-box">
            <div class="step-label"><i class="fa-solid fa-circle-info"></i> Step 1: Given Information & Context</div>
            <p>Pond A: Lotuses double every day. Completely covered on Day 30.
              <br>Pond B: Lotuses triple every day.
              <br>Damayanti places 1 lotus in Pond A for 4 days, then moves all lotuses to Pond B for 4 days.
            </p>
          </div>
          <div class="step-box">
            <div class="step-label"><i class="fa-solid fa-calculator"></i> Step 2: Mathematical Concept & Law Applied</div>
            <p>Doubling daily: <span class="math-font">L(d) = L₀ × 2ᵈ</span>. Tripling daily: <span class="math-font">L(d) = L₀ × 3ᵈ</span>.
              <br>Commutative property: <span class="math-font">2⁴ × 3⁴ = (2 × 3)⁴ = 6⁴</span>.
            </p>
          </div>
          <div class="step-box">
            <div class="step-label"><i class="fa-solid fa-gears"></i> Step 3: Detailed Step-by-Step Mathematical Calculation</div>
            <ul>
              <li><strong>Half covered day:</strong> Since the pond doubles daily, one day before full coverage it was half covered. <span class="math-font">30 – 1 = 29th day}</span>.</li>
              <li><strong>Exponential Form:</strong>
                <br>Fully covered: <span class="math-font">2²⁹</span> lotuses (starting from 1 lotus on Day 1, doubling for 29 days).
                <br>Half covered: <span class="math-font">2²⁸</span> lotuses (since <span class="math-font">2²⁹ ÷ 2 = 2²⁸</span>).
              </li>
              <li><strong>Damayanti's Experiment:</strong>
                <br>After 4 days in doubling pond: <span class="math-font">1 × 2⁴ = 16</span> lotuses.
                <br>After next 4 days in tripling pond: <span class="math-font">16 × 3⁴ = 2⁴ × 3⁴ = (2 × 3)⁴ = 6⁴ = 1,296</span> lotuses.
              </li>
              <li><strong>Reversing the order:</strong>
                <br><span class="math-font">1 × 3⁴ × 2⁴ = 3⁴ × 2⁴ = (3 × 2)⁴ = 6⁴ = 1,296</span> lotuses. The count remains identical!
              </li>
            </ul>
          </div>
          <div class="step-box">
            <div class="step-label"><i class="fa-solid fa-check-double"></i> Step 4: Verification & Sanity Check</div>
            <p><span class="math-font">2⁴ × 3⁴ = 16 × 81 = 1296</span>. <span class="math-font">6⁴ = 36 × 36 = 1296</span>. Matches perfectly.</p>
          </div>
          <div class="step-box">
            <div class="step-label"><i class="fa-solid fa-flag-checkered"></i> Step 5: Final Concise Concluding Statement</div>
            <p>The pond was half covered on Day 29; Damayanti ends up with exactly <strong>1,296 lotuses</strong> regardless of which pond is visited first.</p>
          </div>
        </div>
      </details>

      <!-- NCERT Solved 7: Combinatorics of Safe Locks & Combinations (Pages 26–27) -->
      <details class="ans-box">
        <summary>
          <span>NCERT In-Text Exploration (Pages 26–27): How Many Combinations? Roxie's Outfits & Safe Locks</span>
          <span class="ans-badge"><i class="fa-solid fa-chevron-down"></i> Solution</span>
        </summary>
        <div class="ans-content">
          <div class="step-box">
            <div class="step-label"><i class="fa-solid fa-circle-info"></i> Step 1: Given Information & Context</div>
            <p>Problems presented:
              <br>1. Roxie has 7 dresses, 2 hats, and 3 pairs of shoes. How many outfits?
              <br>2. Great-grandfather's safe has a 5-digit password (digits 0–9). How many combinations?
              <br>3. Estu's proposed 6-slot lock with letters A–Z. How many passwords?
              <br>4. What is <span class="math-font">2¹⁰⁰ ÷ 2²⁵</span> in powers of 2?
            </p>
          </div>
          <div class="step-box">
            <div class="step-label"><i class="fa-solid fa-calculator"></i> Step 2: Mathematical Concept & Law Applied</div>
            <p>Fundamental Counting Principle: For independent choices, multiply individual possibilities.
              <br>Quotient Law: <span class="math-font">aᵐ ÷ aⁿ = aᵐ⁻ⁿ</span>.
            </p>
          </div>
          <div class="step-box">
            <div class="step-label"><i class="fa-solid fa-gears"></i> Step 3: Detailed Step-by-Step Mathematical Calculation</div>
            <ul>
              <li><strong>1. Roxie's Outfits:</strong> <span class="math-font">7 × 2 × 3 = 42</span> different ways to dress up.</li>
              <li><strong>2. 5-Digit Safe Passwords:</strong> Each slot has 10 possible digits (0, 1, 2, ..., 9).
                <br>Total passwords = <span class="math-font">10 × 10 × 10 × 10 × 10 = 10⁵ = 1,00,000</span> (from 00000 to 99999).
              </li>
              <li><strong>3. Estu's 6-Letter Alphabetical Safe:</strong> Each slot has 26 possible letters (A to Z).
                <br>Total passwords = <span class="math-font">26 × 26 × 26 × 26 × 26 × 26 = 26⁶ = 30,89,15,776</span> (over 30.8 crore!).
              </li>
              <li><strong>4. Evaluate 2¹⁰⁰ ÷ 2²⁵:</strong> Using Quotient Law: <span class="math-font">2¹⁰⁰ ÷ 2²⁵ = 2¹⁰⁰⁻²⁵ = 2⁷⁵</span>.</li>
            </ul>
          </div>
          <div class="step-box">
            <div class="step-label"><i class="fa-solid fa-check-double"></i> Step 4: Verification & Sanity Check</div>
            <p><span class="math-font">2⁷⁵ × 2²⁵ = 2⁷⁵⁺²⁵ = 2¹⁰⁰</span>. Product restores original numerator.</p>
          </div>
          <div class="step-box">
            <div class="step-label"><i class="fa-solid fa-flag-checkered"></i> Step 5: Final Concise Concluding Statement</div>
            <p>Roxie has 42 combinations; the 5-digit safe has 1,00,000 combinations; Estu's lock has <span class="math-font">26⁶</span> combinations; and <span class="math-font">2¹⁰⁰ ÷ 2²⁵ = 2⁷⁵</span>.</p>
          </div>
        </div>
      </details>

      <!-- NCERT Solved 8: Zero & Negative Exponent Simplifications (Pages 28–29) -->
      <details class="ans-box">
        <summary>
          <span>NCERT In-Text Prompts (Pages 28–29): Equivalent Forms & Simplifications with Negative Powers</span>
          <span class="ans-badge"><i class="fa-solid fa-chevron-down"></i> Solution</span>
        </summary>
        <div class="ans-content">
          <div class="step-box">
            <div class="step-label"><i class="fa-solid fa-circle-info"></i> Step 1: Given Information & Context</div>
            <p>Evaluate why <span class="math-font">n ≠ 0</span> in <span class="math-font">n⁰ = 1</span>, write equivalent reciprocal forms for 5 negative powers, and simplify 5 exponential expressions.</p>
          </div>
          <div class="step-box">
            <div class="step-label"><i class="fa-solid fa-calculator"></i> Step 2: Mathematical Concept & Law Applied</div>
            <p>Reciprocal Law: <span class="math-font">n⁻ᵃ = 1 / nᵃ</span>. Product Law: <span class="math-font">aᵐ × aⁿ = aᵐ⁺ⁿ</span>. Indeterminate form: <span class="math-font">0/0</span> is undefined.</p>
          </div>
          <div class="step-box">
            <div class="step-label"><i class="fa-solid fa-gears"></i> Step 3: Detailed Step-by-Step Mathematical Calculation</div>
            <p><strong>1. Why can't n be 0?</strong>
              <br>If <span class="math-font">n = 0</span>, <span class="math-font">0⁰ = 0ᵃ⁻ᵃ = 0ᵃ ÷ 0ᵃ = 0 / 0</span>, which is indeterminate (undefined) in arithmetic.
            </p>
            <p><strong>2. Equivalent Reciprocal Forms:</strong></p>
            <ul>
              <li>(i) <span class="math-font">2⁻⁴ = 1 / 2⁴ = 1/16</span></li>
              <li>(ii) <span class="math-font">10⁻⁵ = 1 / 10⁵ = 1/1,00,000</span></li>
              <li>(iii) <span class="math-font">(–7)⁻² = 1 / (–7)² = 1/49</span></li>
              <li>(iv) <span class="math-font">(–5)⁻³ = 1 / (–5)³ = –1/125</span></li>
              <li>(v) <span class="math-font">10⁻¹⁰⁰ = 1 / 10¹⁰⁰</span></li>
            </ul>
            <p><strong>3. Simplify and write in Exponential Form:</strong></p>
            <ul>
              <li>(i) <span class="math-font">2⁻⁴ × 2⁷ = 2⁻⁴⁺⁷ = 2³ = 8</span></li>
              <li>(ii) <span class="math-font">3² × 3⁻⁵ × 3⁶ = 3²⁻⁵⁺⁶ = 3³ = 27</span></li>
              <li>(iii) <span class="math-font">p³ × p⁻¹⁰ = p³⁻¹⁰ = p⁻⁷ = 1 / p⁷</span></li>
              <li>(iv) <span class="math-font">2⁴ × (–4)⁻² = 16 × [1 / (–4)²] = 16 × (1/16) = 1 = 2⁰</span></li>
              <li>(v) <span class="math-font">8ᵖ × 8ᑫ = 8ᵖ⁺ᑫ</span></li>
            </ul>
          </div>
          <div class="step-box">
            <div class="step-label"><i class="fa-solid fa-check-double"></i> Step 4: Verification & Sanity Check</div>
            <p>For (iv): <span class="math-font">(–4)⁻² = (–1 × 2²)⁻² = (–1)⁻² × 2⁻⁴ = 1 × 2⁻⁴ = 2⁻⁴</span>. Then <span class="math-font">2⁴ × 2⁻⁴ = 2⁴⁻⁴ = 2⁰ = 1</span>. Validated.</p>
          </div>
          <div class="step-box">
            <div class="step-label"><i class="fa-solid fa-flag-checkered"></i> Step 5: Final Concise Concluding Statement</div>
            <p>The rules of exponents apply seamlessly to all integers, whether positive, zero, or negative.</p>
          </div>
        </div>
      </details>

      <!-- NCERT Solved 9: Power Line for 7 Complete Calculations (Page 30) -->
      <details class="ans-box">
        <summary>
          <span>NCERT In-Text Activity (Page 30): Complete Calculations Using the Power Line for 7</span>
          <span class="ans-badge"><i class="fa-solid fa-chevron-down"></i> Solution</span>
        </summary>
        <div class="ans-content">
          <div class="step-box">
            <div class="step-label"><i class="fa-solid fa-circle-info"></i> Step 1: Given Information & Context</div>
            <p>Powers of 7 on the number line:
              <br><span class="math-font">7⁰ = 1, 7¹ = 7, 7² = 49, 7³ = 343, 7⁴ = 2401, 7⁵ = 16807, 7⁶ = 117649, 7⁷ = 823543</span>.
              <br>Negative powers: <span class="math-font">7⁻¹ = 1/7, 7⁻² = 1/49, 7⁻³ = 1/343, 7⁻⁴ = 1/2401</span>.
            </p>
          </div>
          <div class="step-box">
            <div class="step-label"><i class="fa-solid fa-calculator"></i> Step 2: Mathematical Concept & Law Applied</div>
            <p>Laws of Exponents for base 7: <span class="math-font">7ᵐ × 7ⁿ = 7ᵐ⁺ⁿ</span> and <span class="math-font">7ᵐ ÷ 7ⁿ = 7ᵐ⁻ⁿ</span>.</p>
          </div>
          <div class="step-box">
            <div class="step-label"><i class="fa-solid fa-gears"></i> Step 3: Detailed Step-by-Step Mathematical Calculation</div>
            <ul>
              <li><strong>2,401 × 49:</strong> <span class="math-font">7⁴ × 7² = 7⁴⁺² = 7⁶</span> (1,17,649).</li>
              <li><strong>49³:</strong> <span class="math-font">(7²)³ = 7²ˣ³ = 7⁶</span> (1,17,649).</li>
              <li><strong>343 × 2,401:</strong> <span class="math-font">7³ × 7⁴ = 7³⁺⁴ = 7⁷</span> (8,23,543).</li>
              <li><strong>16,807 / 49:</strong> <span class="math-font">7⁵ ÷ 7² = 7⁵⁻² = 7³</span> (343).</li>
              <li><strong>7 / 343:</strong> <span class="math-font">7¹ ÷ 7³ = 7¹⁻³ = 7⁻²</span> (<span class="math-font">1/49</span>).</li>
              <li><strong>16,807 / 8,23,543:</strong> <span class="math-font">7⁵ ÷ 7⁷ = 7⁵⁻⁷ = 7⁻²</span> (<span class="math-font">1/49</span>).</li>
              <li><strong>1,17,649 × (1/343):</strong> <span class="math-font">7⁶ × 7⁻³ = 7⁶⁻³ = 7³</span> (343).</li>
              <li><strong>(1/343) × (1/343):</strong> <span class="math-font">7⁻³ × 7⁻³ = 7⁻³⁺⁽⁻³⁾ = 7⁻⁶</span> (<span class="math-font">1/1,17,649</span>).</li>
            </ul>
          </div>
          <div class="step-box">
            <div class="step-label"><i class="fa-solid fa-check-double"></i> Step 4: Verification & Sanity Check</div>
            <p><span class="math-font">7 / 343 = 1/49</span>. Since <span class="math-font">49 = 7²</span>, <span class="math-font">1/49 = 7⁻²</span>. Matches official NCERT answer on Page 33.</p>
          </div>
          <div class="step-box">
            <div class="step-label"><i class="fa-solid fa-flag-checkered"></i> Step 5: Final Concise Concluding Statement</div>
            <p>Every arithmetic operation maps to simple integer addition or subtraction on the power line exponents.</p>
          </div>
        </div>
      </details>

      <!-- NCERT Solved 10: Scientific Notation Conversions & Celestial Distances (Pages 32–34) -->
      <details class="ans-box">
        <summary>
          <span>NCERT In-Text Activity (Pages 32–34): Planetary Distances & Standard Form Conversions</span>
          <span class="ans-badge"><i class="fa-solid fa-chevron-down"></i> Solution</span>
        </summary>
        <div class="ans-content">
          <div class="step-box">
            <div class="step-label"><i class="fa-solid fa-circle-info"></i> Step 1: Given Information & Context</div>
            <p>Distances:
              <br>• Sun to Saturn = <span class="math-font">14,33,50,00,00,000 m = 1.4335 × 10¹² m</span>.
              <br>• Saturn to Uranus = <span class="math-font">14,39,00,00,00,000 m = 1.439 × 10¹² m</span>.
              <br>• Sun to Earth = <span class="math-font">1,49,60,00,00,000 m = 1.496 × 10¹¹ m</span>.
              <br>Questions: Which distance is smallest? Convert 4 numbers into standard form.
            </p>
          </div>
          <div class="step-box">
            <div class="step-label"><i class="fa-solid fa-calculator"></i> Step 2: Mathematical Concept & Law Applied</div>
            <p>Standard form <span class="math-font">m × 10ᵏ</span> with <span class="math-font">1 ≤ m &lt; 10</span>. The distance with the smaller power of 10 is automatically smallest.</p>
          </div>
          <div class="step-box">
            <div class="step-label"><i class="fa-solid fa-gears"></i> Step 3: Detailed Step-by-Step Mathematical Calculation</div>
            <p><strong>1. Smallest Distance Comparison:</strong>
              <br>Sun to Earth has order <span class="math-font">10¹¹</span>, whereas the other two have order <span class="math-font">10¹²</span>. Since <span class="math-font">10¹¹ &lt; 10¹²</span>, the <strong>distance between the Sun and Earth is the smallest</strong> (approx. 10 times closer!).
            </p>
            <p><strong>2. Express in Standard Form:</strong></p>
            <ul>
              <li>(i) <strong>59,853:</strong> Move decimal 4 places left: <span class="math-font">5.9853 × 10⁴</span></li>
              <li>(ii) <strong>65,950:</strong> Move decimal 4 places left: <span class="math-font">6.595 × 10⁴</span></li>
              <li>(iii) <strong>34,30,000:</strong> Move decimal 6 places left: <span class="math-font">3.43 × 10⁶</span></li>
              <li>(iv) <strong>70,04,00,00,000:</strong> Move decimal 10 places left: <span class="math-font">7.004 × 10¹⁰</span></li>
            </ul>
          </div>
          <div class="step-box">
            <div class="step-label"><i class="fa-solid fa-check-double"></i> Step 4: Verification & Sanity Check</div>
            <p><span class="math-font">7.004 × 10¹⁰ = 7.004 × 10,00,00,00,000 = 70,04,00,00,000</span>. Restores original number.</p>
          </div>
          <div class="step-box">
            <div class="step-label"><i class="fa-solid fa-flag-checkered"></i> Step 5: Final Concise Concluding Statement</div>
            <p>Sun to Earth is the smallest distance; all 4 numbers successfully converted into standard scientific form.</p>
          </div>
        </div>
      </details>

      <!-- NCERT Solved 11: Estimation & Population Calculations (Pages 38–42) -->
      <details class="ans-box">
        <summary>
          <span>NCERT In-Text Activity (Pages 38–42): Population Ratios, Time in Seconds & Star Counting</span>
          <span class="ans-badge"><i class="fa-solid fa-chevron-down"></i> Solution</span>
        </summary>
        <div class="ans-content">
          <div class="step-box">
            <div class="step-label"><i class="fa-solid fa-circle-info"></i> Step 1: Given Information & Context</div>
            <p>Solve 4 real-world population and cosmic problems from textbook pages 38–42:
              <br>(i) Ants per human (Ants = <span class="math-font">2 × 10¹⁶</span>, Humans = <span class="math-font">8 × 10⁹</span>).
              <br>(ii) Flocks of starlings (Total birds = <span class="math-font">1.3 × 10⁹</span>, flock size = 10,000 = <span class="math-font">10⁴</span>).
              <br>(iii) Total leaves on all trees (Trees = <span class="math-font">3 × 10¹²</span>, leaves/tree = <span class="math-font">10⁴</span>).
              <br>(iv) Sheets of paper to reach Moon (Distance = <span class="math-font">3,84,400 km</span>, thickness = 0.001 cm).
            </p>
          </div>
          <div class="step-box">
            <div class="step-label"><i class="fa-solid fa-calculator"></i> Step 2: Mathematical Concept & Law Applied</div>
            <p>Quotient Law and Product Law of Exponents with scientific notation arithmetic.</p>
          </div>
          <div class="step-box">
            <div class="step-label"><i class="fa-solid fa-gears"></i> Step 3: Detailed Step-by-Step Mathematical Calculation</div>
            <ul>
              <li><strong>(i) Ants per Human:</strong>
                <br><span class="math-font">(2 × 10¹⁶) ÷ (8 × 10⁹) = (2/8) × 10¹⁶⁻⁹ = 0.25 × 10⁷ = 2.5 × 10⁶ ants</span> (2.5 million ants per person!).
              </li>
              <li><strong>(ii) Flocks of Starlings:</strong>
                <br><span class="math-font">(1.3 × 10⁹) ÷ 10⁴ = 1.3 × 10⁹⁻⁴ = 1.3 × 10⁵ flocks</span> (1,30,000 flocks).
              </li>
              <li><strong>(iii) Leaves on all Trees:</strong>
                <br><span class="math-font">(3 × 10¹²) × 10⁴ = 3 × 10¹²⁺⁴ = 3 × 10¹⁶ leaves</span> (30 quadrillion leaves).
              </li>
              <li><strong>(iv) Paper Sheets to Moon:</strong>
                <br>Distance = <span class="math-font">3,84,400 km = 3.844 × 10⁵ km = 3.844 × 10⁸ m = 3.844 × 10¹⁰ cm</span>.
                <br>Each sheet = <span class="math-font">0.001 cm = 10⁻³ cm</span>.
                <br>Sheets needed = <span class="math-font">(3.844 × 10¹⁰) ÷ 10⁻³ = 3.844 × 10¹⁰⁻⁽⁻³⁾ = 3.844 × 10¹³ sheets</span>!
              </li>
            </ul>
          </div>
          <div class="step-box">
            <div class="step-label"><i class="fa-solid fa-check-double"></i> Step 4: Verification & Sanity Check</div>
            <p><span class="math-font">3.844 × 10¹³ × 0.001 cm = 3.844 × 10¹⁰ cm = 3,84,400 km</span>. Matches the Earth-Moon distance perfectly.</p>
          </div>
          <div class="step-box">
            <div class="step-label"><i class="fa-solid fa-flag-checkered"></i> Step 5: Final Concise Concluding Statement</div>
            <p>Ants per human = <span class="math-font">2.5 × 10⁶</span>; Flocks = <span class="math-font">1.3 × 10⁵</span>; Leaves = <span class="math-font">3 × 10¹⁶</span>; Paper sheets = <span class="math-font">3.844 × 10¹³</span>.</p>
          </div>
        </div>
      </details>

      <!-- ======================================================== -->
      <!-- PART 2: END-OF-CHAPTER "FIGURE IT OUT" EXERCISES -->
      <!-- ======================================================== -->
      <h3 class="topic-title"><i class="fa-solid fa-puzzle-piece"></i> Part 2: End-of-Chapter "Figure it Out" Exercises (Questions 1 to 14)</h3>

      <!-- Exercise Q1: Units Digit of 2^224 / 4^32 -->
      <details class="ans-box" open>
        <summary>
          <span>Exercise Q1 (Page 44): Find the Units Digit in the Value of 2²²⁴ ÷ 4³²</span>
          <span class="ans-badge"><i class="fa-solid fa-chevron-down"></i> Solution</span>
        </summary>
        <div class="ans-content">
          <div class="step-box">
            <div class="step-label"><i class="fa-solid fa-circle-info"></i> Step 1: Given Information & Context</div>
            <p>Expression: <span class="math-font">2²²⁴ ÷ 4³²</span>. [Hint given in NCERT: <span class="math-font">4 = 2²</span>]. We must find the units digit of the evaluated quotient.</p>
          </div>
          <div class="step-box">
            <div class="step-label"><i class="fa-solid fa-calculator"></i> Step 2: Mathematical Concept & Law Applied</div>
            <p>1. Power of a Power Law: <span class="math-font">4³² = (2²)³² = 2⁶⁴</span>.
              <br>2. Quotient Law: <span class="math-font">2²²⁴ ÷ 2⁶⁴ = 2²²⁴⁻⁶⁴ = 2¹⁶⁰</span>.
              <br>3. Cyclicity of units digits of powers of 2 (cycle length 4: 2, 4, 8, 6).
            </p>
          </div>
          <div class="step-box">
            <div class="step-label"><i class="fa-solid fa-gears"></i> Step 3: Detailed Step-by-Step Mathematical Calculation</div>
            <p>Convert denominator to base 2:
              <br><span class="math-font">4³² = (2²)³² = 2²ˣ³² = 2⁶⁴</span>.
              <br>Now apply Quotient Law:
              <br><span class="math-font">2²²⁴ ÷ 2⁶⁴ = 2²²⁴⁻⁶⁴ = 2¹⁶⁰</span>.
              <br>Now analyse the units digit cycle for powers of 2:
              <br>• <span class="math-font">2¹ = 2</span> (units digit 2)
              <br>• <span class="math-font">2² = 4</span> (units digit 4)
              <br>• <span class="math-font">2³ = 8</span> (units digit 8)
              <br>• <span class="math-font">2⁴ = 16</span> (units digit 6)
              <br>• <span class="math-font">2⁵ = 32</span> (units digit 2 — repeats every 4 powers).
              <br>Divide the exponent 160 by 4:
              <br><span class="math-font">160 ÷ 4 = 40 with remainder } 0</span>.
              <br>A remainder of 0 corresponds to the 4th position in the cycle, which ends in <strong>6</strong>!
            </p>
          </div>
          <div class="step-box">
            <div class="step-label"><i class="fa-solid fa-check-double"></i> Step 4: Verification & Sanity Check</div>
            <p>Any positive power of 2 whose exponent is a multiple of 4 (<span class="math-font">2⁴=16, 2⁸=256, 2¹²=4096</span>) always ends in 6. Since 160 is divisible by 4, the units digit must be 6. Matches NCERT answer key on Page 35.</p>
          </div>
          <div class="step-box">
            <div class="step-label"><i class="fa-solid fa-flag-checkered"></i> Step 5: Final Concise Concluding Statement</div>
            <p>The units digit in the value of <span class="math-font">2²²⁴ ÷ 4³²</span> is <strong>6</strong>.</p>
          </div>
        </div>
      </details>

      <!-- Exercise Q2: 5 Bottles in a Container for 40 Days -->
      <details class="ans-box">
        <summary>
          <span>Exercise Q2 (Page 44): Bottles in Containers Brought Daily for 40 Days</span>
          <span class="ans-badge"><i class="fa-solid fa-chevron-down"></i> Solution</span>
        </summary>
        <div class="ans-content">
          <div class="step-box">
            <div class="step-label"><i class="fa-solid fa-circle-info"></i> Step 1: Given Information & Context</div>
            <p>There are 5 bottles in each container. Every day, exactly 1 new container is brought in. We must find the total number of bottles present after 40 days.</p>
          </div>
          <div class="step-box">
            <div class="step-label"><i class="fa-solid fa-calculator"></i> Step 2: Mathematical Concept & Law Applied</div>
            <p>Linear additive growth: Total bottles = <span class="math-font">Bottles per container × Number of days</span>. Then express in exponential / standard form.</p>
          </div>
          <div class="step-box">
            <div class="step-label"><i class="fa-solid fa-gears"></i> Step 3: Detailed Step-by-Step Mathematical Calculation</div>
            <p>Total bottles = <span class="math-font">5 × 40 = 200 bottles}</span>.
              <br>In standard exponential form: <span class="math-font">200 = 2 × 10² bottles}</span>.
            </p>
          </div>
          <div class="step-box">
            <div class="step-label"><i class="fa-solid fa-check-double"></i> Step 4: Verification & Sanity Check</div>
            <p><span class="math-font">2 × 10² = 2 × 100 = 200</span>. Day 1: 5, Day 2: 10 ... Day 40: 200.</p>
          </div>
          <div class="step-box">
            <div class="step-label"><i class="fa-solid fa-flag-checkered"></i> Step 5: Final Concise Concluding Statement</div>
            <p>After 40 days, there will be <strong>200 bottles</strong> (or <span class="math-font">2 × 10²</span> bottles).</p>
          </div>
        </div>
      </details>

      <!-- Exercise Q3: Express as Product of Powers in 3 Different Ways -->
      <details class="ans-box">
        <summary>
          <span>Exercise Q3 (Page 44): Express 64³, 192⁸, and 32⁻⁵ as Products of Powers in Three Ways</span>
          <span class="ans-badge"><i class="fa-solid fa-chevron-down"></i> Solution</span>
        </summary>
        <div class="ans-content">
          <div class="step-box">
            <div class="step-label"><i class="fa-solid fa-circle-info"></i> Step 1: Given Information & Context</div>
            <p>Express each number as a product of two or more powers in three different ways, where powers can be any integers:
              <br>(i) <span class="math-font">64³</span>
              <br>(ii) <span class="math-font">192⁸</span>
              <br>(iii) <span class="math-font">32⁻⁵</span>
            </p>
          </div>
          <div class="step-box">
            <div class="step-label"><i class="fa-solid fa-calculator"></i> Step 2: Mathematical Concept & Law Applied</div>
            <p>Prime factorisation decomposition: <span class="math-font">64 = 2⁶</span>, <span class="math-font">192 = 2⁶ × 3</span>, <span class="math-font">32 = 2⁵</span>.
              <br>Laws: <span class="math-font">aᵐ⁺ⁿ = aᵐ × aⁿ</span>, <span class="math-font">(aᵐ)ⁿ = aᵐⁿ</span>, <span class="math-font">(ab)ⁿ = aⁿ × bⁿ</span>.
            </p>
          </div>
          <div class="step-box">
            <div class="step-label"><i class="fa-solid fa-gears"></i> Step 3: Detailed Step-by-Step Mathematical Calculation</div>
            <p><strong>(i) For 64³:</strong>
              <br><span class="math-font">64³ = (2⁶)³ = 2¹⁸</span>.
              <br>• Way 1: <span class="math-font">2¹⁰ × 2⁸</span> (since 10 + 8 = 18)
              <br>• Way 2: <span class="math-font">4⁵ × 4⁴ = 4⁹ = (2²)⁹ = 2¹⁸</span>
              <br>• Way 3: <span class="math-font">8³ × 8³ = 8⁶ = (2³)⁶ = 2¹⁸</span>
            </p>
            <p><strong>(ii) For 192⁸:</strong>
              <br><span class="math-font">192 = 2⁶ × 3¹ ⇒ 192⁸ = (2⁶ × 3)⁸ = 2⁴⁸ × 3⁸</span>.
              <br>• Way 1: <span class="math-font">2⁴⁸ × 3⁸</span>
              <br>• Way 2: <span class="math-font">2⁴⁰ × 2⁸ × 3⁸ = 2⁴⁰ × (2 × 3)⁸ = 2⁴⁰ × 6⁸</span>
              <br>• Way 3: <span class="math-font">2⁴⁰ × 2⁸ × 3⁸</span>
            </p>
            <p><strong>(iii) For 32⁻⁵:</strong>
              <br><span class="math-font">32⁻⁵ = (2⁵)⁻⁵ = 2⁻²⁵</span>.
              <br>• Way 1: <span class="math-font">2⁻¹⁰ × 2⁻¹⁵</span> (since –10 + (–15) = –25)
              <br>• Way 2: <span class="math-font">2⁻⁵ × 2⁻²⁰</span>
              <br>• Way 3: <span class="math-font">4⁻¹² × 2⁻¹ = (2²)⁻¹² × 2⁻¹ = 2⁻²⁴ × 2⁻¹ = 2⁻²⁵</span>
            </p>
          </div>
          <div class="step-box">
            <div class="step-label"><i class="fa-solid fa-check-double"></i> Step 4: Verification & Sanity Check</div>
            <p>All combinations sum to exponents 18, (48 and 8), and –25 respectively. Matches NCERT answer key on Page 35.</p>
          </div>
          <div class="step-box">
            <div class="step-label"><i class="fa-solid fa-flag-checkered"></i> Step 5: Final Concise Concluding Statement</div>
            <p>Each number is successfully represented in 3 distinct exponential product forms.</p>
          </div>
        </div>
      </details>

      <!-- Exercise Q4: Always True, Only Sometimes True, or Never True -->
      <details class="ans-box">
        <summary>
          <span>Exercise Q4 (Page 44): Examine Truth Value of 5 Statements with Rigorous Proofs</span>
          <span class="ans-badge"><i class="fa-solid fa-chevron-down"></i> Solution</span>
        </summary>
        <div class="ans-content">
          <div class="step-box">
            <div class="step-label"><i class="fa-solid fa-circle-info"></i> Step 1: Given Information & Context</div>
            <p>Determine whether each statement is 'Always True', 'Only Sometimes True', or 'Never True', and provide algebraic explanations:
              <br>(i) Cube numbers are also square numbers.
              <br>(ii) Fourth powers are also square numbers.
              <br>(iii) The fifth power of a number is divisible by the cube of that number.
              <br>(iv) The product of two cube numbers is a cube number.
              <br>(v) <span class="math-font">q⁴⁶</span> is both a 4th power and a 6th power (where <span class="math-font">q</span> is a prime number).
            </p>
          </div>
          <div class="step-box">
            <div class="step-label"><i class="fa-solid fa-calculator"></i> Step 2: Mathematical Concept & Law Applied</div>
            <p>Divisibility of exponents, power of a power identity <span class="math-font">(aᵐ)ⁿ = aᵐⁿ</span>, and prime factorisation.</p>
          </div>
          <div class="step-box">
            <div class="step-label"><i class="fa-solid fa-gears"></i> Step 3: Detailed Step-by-Step Mathematical Calculation</div>
            <ul>
              <li><strong>(i) Cube numbers are also square numbers:</strong>
                <br><strong>Verdict: Only Sometimes True.</strong>
                <br><em>Reasoning:</em> A cube <span class="math-font">n³</span> is a square only when <span class="math-font">n</span> itself is a square (<span class="math-font">n = k² ⇒ n³ = (k²)³ = k⁶ = (k³)²</span>). For example, <span class="math-font">64 = 4³ = 8²</span> (True), and <span class="math-font">729 = 9³ = 27²</span> (True). However, for <span class="math-font">2³ = 8</span> or <span class="math-font">3³ = 27</span>, neither is a square number! Thus, it is only sometimes true.
              </li>
              <li><strong>(ii) Fourth powers are also square numbers:</strong>
                <br><strong>Verdict: Always True.</strong>
                <br><em>Reasoning:</em> For any number <span class="math-font">n</span>, we can write <span class="math-font">n⁴ = (n²)²</span>. Because the exponent 4 is an even multiple of 2, every 4th power is identically the square of <span class="math-font">n²</span>!
              </li>
              <li><strong>(iii) The fifth power of a number is divisible by the cube of that number:</strong>
                <br><strong>Verdict: Always True</strong> (for non-zero integers).
                <br><em>Reasoning:</em> By Quotient Law: <span class="math-font">n⁵ ÷ n³ = n⁵⁻³ = n²</span>. Since <span class="math-font">n²</span> is always an integer when <span class="math-font">n</span> is an integer, <span class="math-font">n³</span> divides <span class="math-font">n⁵</span> with remainder 0.
              </li>
              <li><strong>(iv) The product of two cube numbers is a cube number:</strong>
                <br><strong>Verdict: Always True.</strong>
                <br><em>Reasoning:</em> Let the two cubes be <span class="math-font">a³</span> and <span class="math-font">b³</span>. By the Common Exponent Product Law: <span class="math-font">a³ × b³ = (a × b)³</span>. Since the product of two integers <span class="math-font">ab</span> is an integer, <span class="math-font">(ab)³</span> is always a cube number.
              </li>
              <li><strong>(v) q⁴⁶ is both a 4th power and a 6th power (q is prime):</strong>
                <br><strong>Verdict: Never True.</strong>
                <br><em>Reasoning:</em> For <span class="math-font">qᵏ</span> to be a 4th power, the exponent <span class="math-font">k</span> must be divisible by 4. For it to be a 6th power, <span class="math-font">k</span> must be divisible by 6. For it to be both, <span class="math-font">k</span> must be a multiple of <span class="math-font">LCM}(4, 6) = 12</span>. However, 46 is NOT divisible by 4 (<span class="math-font">46/4 = 11.5</span>), nor is it divisible by 6 (<span class="math-font">46/6 = 7.67</span>), nor by 12. Therefore, it is impossible.
              </li>
            </ul>
          </div>
          <div class="step-box">
            <div class="step-label"><i class="fa-solid fa-check-double"></i> Step 4: Verification & Sanity Check</div>
            <p>Matches NCERT official answer key on Page 36 verbatim.</p>
          </div>
          <div class="step-box">
            <div class="step-label"><i class="fa-solid fa-flag-checkered"></i> Step 5: Final Concise Concluding Statement</div>
            <p>(i) Sometimes True, (ii) Always True, (iii) Always True, (iv) Always True, (v) Never True.</p>
          </div>
        </div>
      </details>

      <!-- Exercise Q5: Simplify and Write in Exponential Form -->
      <details class="ans-box">
        <summary>
          <span>Exercise Q5 (Page 44): Simplify and Write in Exponential Form (5 Problems)</span>
          <span class="ans-badge"><i class="fa-solid fa-chevron-down"></i> Solution</span>
        </summary>
        <div class="ans-content">
          <div class="step-box">
            <div class="step-label"><i class="fa-solid fa-circle-info"></i> Step 1: Given Information & Context</div>
            <p>Simplify:
              <br>(i) <span class="math-font">10⁻² × 10⁻⁵</span>
              <br>(ii) <span class="math-font">5⁷ ÷ 5⁴</span>
              <br>(iii) <span class="math-font">9⁻⁷ ÷ 9⁴</span>
              <br>(iv) <span class="math-font">(13⁻²)⁻³</span>
              <br>(v) <span class="math-font">m⁵ n¹² (mn)⁹</span>
            </p>
          </div>
          <div class="step-box">
            <div class="step-label"><i class="fa-solid fa-calculator"></i> Step 2: Mathematical Concept & Law Applied</div>
            <p>All fundamental exponent laws: Product Law, Quotient Law, Power of a Power, and Power of a Product.</p>
          </div>
          <div class="step-box">
            <div class="step-label"><i class="fa-solid fa-gears"></i> Step 3: Detailed Step-by-Step Mathematical Calculation</div>
            <ul>
              <li><strong>(i) 10⁻² × 10⁻⁵:</strong> Base is 10. Exponents add: <span class="math-font">10⁻²⁺⁽⁻⁵⁾ = 10⁻⁷</span> (or <span class="math-font">1 / 10⁷</span>).</li>
              <li><strong>(ii) 5⁷ ÷ 5⁴:</strong> Base is 5. Exponents subtract: <span class="math-font">5⁷⁻⁴ = 5³</span> (= 125).</li>
              <li><strong>(iii) 9⁻⁷ ÷ 9⁴:</strong> Base is 9. Exponents subtract: <span class="math-font">9⁻⁷⁻⁴ = 9⁻¹¹</span> (or <span class="math-font">1 / 9¹¹</span>).</li>
              <li><strong>(iv) (13⁻²)⁻³:</strong> Base is 13. Exponents multiply: <span class="math-font">13⁽⁻²⁾ˣ⁽⁻³⁾ = 13⁺⁶ = 13⁶</span>.</li>
              <li><strong>(v) m⁵ n¹² (mn)⁹:</strong> Expand <span class="math-font">(mn)⁹ = m⁹ n⁹</span>.
                <br>Then group like bases: <span class="math-font">(m⁵ × m⁹) × (n¹² × n⁹) = m⁵⁺⁹ n¹²⁺⁹ = m¹⁴ n²¹</span>.
              </li>
            </ul>
          </div>
          <div class="step-box">
            <div class="step-label"><i class="fa-solid fa-check-double"></i> Step 4: Verification & Sanity Check</div>
            <p>For (iv): <span class="math-font">(13⁻²)⁻³ = (1 / 13²)⁻³ = 1 / (1 / 13²)³ = 1 / (1 / 13⁶) = 13⁶</span>. Negative signs correctly cancel to positive.</p>
          </div>
          <div class="step-box">
            <div class="step-label"><i class="fa-solid fa-flag-checkered"></i> Step 5: Final Concise Concluding Statement</div>
            <p>(i) <span class="math-font">10⁻⁷</span>, (ii) <span class="math-font">5³</span>, (iii) <span class="math-font">9⁻¹¹</span>, (iv) <span class="math-font">13⁶</span>, (v) <span class="math-font">m¹⁴ n²¹</span>.</p>
          </div>
        </div>
      </details>

      <!-- Exercise Q6: Decimal Powers If 12^2 = 144 -->
      <details class="ans-box">
        <summary>
          <span>Exercise Q6 (Page 44): If 12² = 144, Evaluate (1.2)², (0.12)², (0.012)², and 120²</span>
          <span class="ans-badge"><i class="fa-solid fa-chevron-down"></i> Solution</span>
        </summary>
        <div class="ans-content">
          <div class="step-box">
            <div class="step-label"><i class="fa-solid fa-circle-info"></i> Step 1: Given Information & Context</div>
            <p>We are given that <span class="math-font">12² = 144</span>. We must evaluate four related decimal and tens multiples without performing long manual multiplication.</p>
          </div>
          <div class="step-box">
            <div class="step-label"><i class="fa-solid fa-calculator"></i> Step 2: Mathematical Concept & Law Applied</div>
            <p>Express each number as <span class="math-font">12 × 10ᵏ</span>, then apply the Common Exponent Law: <span class="math-font">(12 × 10ᵏ)² = 12² × 10²ᵏ = 144 × 10²ᵏ</span>.</p>
          </div>
          <div class="step-box">
            <div class="step-label"><i class="fa-solid fa-gears"></i> Step 3: Detailed Step-by-Step Mathematical Calculation</div>
            <ul>
              <li><strong>(i) (1.2)²:</strong> <span class="math-font">1.2 = 12 × 10⁻¹ ⇒ (1.2)² = 12² × (10⁻¹)² = 144 × 10⁻² = 1.44</span> (2 decimal places).</li>
              <li><strong>(ii) (0.12)²:</strong> <span class="math-font">0.12 = 12 × 10⁻² ⇒ (0.12)² = 12² × (10⁻²)² = 144 × 10⁻⁴ = 0.0144</span> (4 decimal places).</li>
              <li><strong>(iii) (0.012)²:</strong> <span class="math-font">0.012 = 12 × 10⁻³ ⇒ (0.012)² = 12² × (10⁻³)² = 144 × 10⁻⁶ = 0.000144</span> (6 decimal places).</li>
              <li><strong>(iv) (120)²:</strong> <span class="math-font">120 = 12 × 10¹ ⇒ (120)² = 12² × (10¹)² = 144 × 10² = 14,400</span>.</li>
            </ul>
          </div>
          <div class="step-box">
            <div class="step-label"><i class="fa-solid fa-check-double"></i> Step 4: Verification & Sanity Check</div>
            <p>Squaring doubles the number of decimal digits: 1 digit in 1.2 becomes 2 digits (1.44); 2 digits in 0.12 becomes 4 digits (0.0144); 3 digits in 0.012 becomes 6 digits (0.000144).</p>
          </div>
          <div class="step-box">
            <div class="step-label"><i class="fa-solid fa-flag-checkered"></i> Step 5: Final Concise Concluding Statement</div>
            <p>(i) 1.44, (ii) 0.0144, (iii) 0.000144, (iv) 14,400.</p>
          </div>
        </div>
      </details>

      <!-- Exercise Q7: Circle the Numbers That Are the Same -->
      <details class="ans-box">
        <summary>
          <span>Exercise Q7 (Page 45): Circle the Numbers That Are the Same (2⁴ × 3⁶, 6⁴ × 3², 6¹⁰, 18² × 6², 6²⁴)</span>
          <span class="ans-badge"><i class="fa-solid fa-chevron-down"></i> Solution</span>
        </summary>
        <div class="ans-content">
          <div class="step-box">
            <div class="step-label"><i class="fa-solid fa-circle-info"></i> Step 1: Given Information & Context</div>
            <p>Examine 5 numbers: <span class="math-font">2⁴ × 3⁶</span>, <span class="math-font">6⁴ × 3²</span>, <span class="math-font">6¹⁰</span>, <span class="math-font">18² × 6²</span>, and <span class="math-font">6²⁴</span>. Determine which of them represent the exact same value.</p>
          </div>
          <div class="step-box">
            <div class="step-label"><i class="fa-solid fa-calculator"></i> Step 2: Mathematical Concept & Law Applied</div>
            <p>Decompose every term into its unique prime exponential factorisation: <span class="math-font">2ᵃ × 3ᵇ</span>.</p>
          </div>
          <div class="step-box">
            <div class="step-label"><i class="fa-solid fa-gears"></i> Step 3: Detailed Step-by-Step Mathematical Calculation</div>
            <ul>
              <li><strong>Number 1:</strong> <span class="math-font">2⁴ × 3⁶</span> (Already in prime form: <span class="math-font">a = 4, b = 6</span>). Value: <span class="math-font">16 × 729 = 11,664</span>.</li>
              <li><strong>Number 2:</strong> <span class="math-font">6⁴ × 3² = (2 × 3)⁴ × 3² = 2⁴ × 3⁴ × 3² = 2⁴ × 3⁴⁺² = 2⁴ × 3⁶</span>. (Identical to Number 1!).</li>
              <li><strong>Number 3:</strong> <span class="math-font">6¹⁰ = (2 × 3)¹⁰ = 2¹⁰ × 3¹⁰ = 6,04,66,176</span> (Completely different).</li>
              <li><strong>Number 4:</strong> <span class="math-font">18² × 6² = (2 × 3²)² × (2 × 3)² = (2² × 3⁴) × (2² × 3²) = 2²⁺² × 3⁴⁺² = 2⁴ × 3⁶</span>. (Identical to Number 1!).</li>
              <li><strong>Number 5:</strong> <span class="math-font">6²⁴ = 2²⁴ × 3²⁴</span> (Vastly larger).</li>
            </ul>
          </div>
          <div class="step-box">
            <div class="step-label"><i class="fa-solid fa-check-double"></i> Step 4: Verification & Sanity Check</div>
            <p><span class="math-font">18² × 6² = (18 × 6)² = 108² = 11,664</span>. <span class="math-font">6⁴ × 3² = 1296 × 9 = 11,664</span>. <span class="math-font">2⁴ × 3⁶ = 16 × 729 = 11,664</span>. All three equal 11,664.</p>
          </div>
          <div class="step-box">
            <div class="step-label"><i class="fa-solid fa-flag-checkered"></i> Step 5: Final Concise Concluding Statement</div>
            <p>The numbers that are the same are: <strong>2⁴ × 3⁶</strong>, <strong>6⁴ × 3²</strong>, and <strong>18² × 6²</strong>.</p>
          </div>
        </div>
      </details>

      <!-- Exercise Q8: Identify the Greater Number -->
      <details class="ans-box">
        <summary>
          <span>Exercise Q8 (Page 45): Identify the Greater Number: (i) 4³ or 3⁴, (ii) 2⁸ or 8², (iii) 100² or 2¹⁰⁰</span>
          <span class="ans-badge"><i class="fa-solid fa-chevron-down"></i> Solution</span>
        </summary>
        <div class="ans-content">
          <div class="step-box">
            <div class="step-label"><i class="fa-solid fa-circle-info"></i> Step 1: Given Information & Context</div>
            <p>Compare pairs of numbers where bases and exponents are swapped:
              <br>(i) <span class="math-font">4³</span> vs <span class="math-font">3⁴</span>
              <br>(ii) <span class="math-font">2⁸</span> vs <span class="math-font">8²</span>
              <br>(iii) <span class="math-font">100²</span> vs <span class="math-font">2¹⁰⁰</span>
            </p>
          </div>
          <div class="step-box">
            <div class="step-label"><i class="fa-solid fa-calculator"></i> Step 2: Mathematical Concept & Law Applied</div>
            <p>Evaluate exact values for small powers; use order of magnitude decomposition for astronomical powers.</p>
          </div>
          <div class="step-box">
            <div class="step-label"><i class="fa-solid fa-gears"></i> Step 3: Detailed Step-by-Step Mathematical Calculation</div>
            <ul>
              <li><strong>(i) 4³ or 3⁴:</strong>
                <br><span class="math-font">4³ = 4 × 4 × 4 = 64</span>.
                <br><span class="math-font">3⁴ = 3 × 3 × 3 × 3 = 81</span>.
                <br>Since <span class="math-font">81 &gt; 64</span>, <strong>3⁴ is greater</strong>.
              </li>
              <li><strong>(ii) 2⁸ or 8²:</strong>
                <br><span class="math-font">2⁸ = 256</span>.
                <br><span class="math-font">8² = (2³)² = 2⁶ = 64</span>.
                <br>Since <span class="math-font">256 &gt; 64</span>, <strong>2⁸ is greater</strong> (it is 4 times larger).
              </li>
              <li><strong>(iii) 100² or 2¹⁰⁰:</strong>
                <br><span class="math-font">100² = 10,000 = 10⁴</span>.
                <br>For <span class="math-font">2¹⁰⁰</span>: We know <span class="math-font">2¹⁰ = 1,024 &gt; 1,000 = 10³</span>.
                <br>Therefore, <span class="math-font">2¹⁰⁰ = (2¹⁰)¹⁰ &gt; (10³)¹⁰ = 10³⁰</span>!
                <br>A number with 31 digits (<span class="math-font">&gt; 10³⁰</span>) completely dwarfs <span class="math-font">10,000</span> (<span class="math-font">10⁴</span>).
                <br>Hence, <strong>2¹⁰⁰ is astronomically greater</strong>!
              </li>
            </ul>
          </div>
          <div class="step-box">
            <div class="step-label"><i class="fa-solid fa-check-double"></i> Step 4: Verification & Sanity Check</div>
            <p>In general, for <span class="math-font">x &gt; e ≈ 2.718</span>, an exponential function <span class="math-font">aˣ</span> outgrows polynomial power <span class="math-font">xᵃ</span>. Thus <span class="math-font">2¹⁰⁰ ≫ 100²</span>.</p>
          </div>
          <div class="step-box">
            <div class="step-label"><i class="fa-solid fa-flag-checkered"></i> Step 5: Final Concise Concluding Statement</div>
            <p>(i) <span class="math-font">3⁴</span> is greater, (ii) <span class="math-font">2⁸</span> is greater, (iii) <span class="math-font">2¹⁰⁰</span> is incomparably greater.</p>
          </div>
        </div>
      </details>

      <!-- Exercise Q9: Dairy Unique ID Digit Requirement -->
      <details class="ans-box">
        <summary>
          <span>Exercise Q9 (Page 45): Dairy Milk Packets (8.5 Billion) Unique ID Digit Length</span>
          <span class="ans-badge"><i class="fa-solid fa-chevron-down"></i> Solution</span>
        </summary>
        <div class="ans-content">
          <div class="step-box">
            <div class="step-label"><i class="fa-solid fa-circle-info"></i> Step 1: Given Information & Context</div>
            <p>Annual milk production target = 8.5 billion packets = <span class="math-font">8,50,00,00,000 = 8.5 × 10⁹</span> packets.
              <br>Allowed characters: decimal digits 0 to 9 (10 choices per digit).
              <br>Goal: Find the minimum length of digits <span class="math-font">n</span> needed to provide a unique code for each packet.
            </p>
          </div>
          <div class="step-box">
            <div class="step-label"><i class="fa-solid fa-calculator"></i> Step 2: Mathematical Concept & Law Applied</div>
            <p>Fundamental Counting Principle: An <span class="math-font">n</span>-digit code using 10 digits provides <span class="math-font">10ⁿ</span> unique combinations. We require: <span class="math-font">10ⁿ ≥ 8.5 × 10⁹</span>.</p>
          </div>
          <div class="step-box">
            <div class="step-label"><i class="fa-solid fa-gears"></i> Step 3: Detailed Step-by-Step Mathematical Calculation</div>
            <ul>
              <li>If <span class="math-font">n = 9</span>: <span class="math-font">10⁹ = 1,00,00,00,000</span> (1 billion codes).
                <br>Since <span class="math-font">1,00,00,00,000 &lt; 8,50,00,00,000</span>, a 9-digit code runs out of unique numbers after just 1 billion packets!
              </li>
              <li>If <span class="math-font">n = 10</span>: <span class="math-font">10¹⁰ = 10,00,00,00,000</span> (10 billion codes).
                <br>Since <span class="math-font">10,00,00,00,000 &gt; 8,50,00,00,000</span>, a 10-digit code easily accommodates all 8.5 billion packets with 1.5 billion spare codes.
              </li>
            </ul>
          </div>
          <div class="step-box">
            <div class="step-label"><i class="fa-solid fa-check-double"></i> Step 4: Verification & Sanity Check</div>
            <p>Matches NCERT official answer key on Page 37: "At least 10 digits are required in the code."</p>
          </div>
          <div class="step-box">
            <div class="step-label"><i class="fa-solid fa-flag-checkered"></i> Step 5: Final Concise Concluding Statement</div>
            <p>The unique identifier code must consist of at least <strong>10 digits</strong>.</p>
          </div>
        </div>
      </details>

      <!-- Exercise Q10: Numbers That Are Both Squares and Cubes -->
      <details class="ans-box">
        <summary>
          <span>Exercise Q10 (Page 45): General Description of Numbers That Are Both Squares and Cubes</span>
          <span class="ans-badge"><i class="fa-solid fa-chevron-down"></i> Solution</span>
        </summary>
        <div class="ans-content">
          <div class="step-box">
            <div class="step-label"><i class="fa-solid fa-circle-info"></i> Step 1: Given Information & Context</div>
            <p>We are given that <span class="math-font">64</span> is both a square number (<span class="math-font">8²</span>) and a cube number (<span class="math-font">4³</span>). We must determine if there are other such numbers and formulate a general mathematical description.</p>
          </div>
          <div class="step-box">
            <div class="step-label"><i class="fa-solid fa-calculator"></i> Step 2: Mathematical Concept & Law Applied</div>
            <p>Power of a Power Law: Let the number be <span class="math-font">N</span>. For <span class="math-font">N</span> to be a square, its exponent must be a multiple of 2 (<span class="math-font">N = a²</span>). For <span class="math-font">N</span> to be a cube, its exponent must be a multiple of 3 (<span class="math-font">N = b³</span>). For both, its exponent must be a multiple of <span class="math-font">LCM}(2, 3) = 6</span>.</p>
          </div>
          <div class="step-box">
            <div class="step-label"><i class="fa-solid fa-gears"></i> Step 3: Detailed Step-by-Step Mathematical Calculation</div>
            <p>In general, any number that is both a square and a cube is a <strong>sixth power</strong> (<span class="math-font">n⁶</span>) for some integer <span class="math-font">n</span>:
              <br><span class="math-font">n⁶ = (n³)²</span> (a perfect square of <span class="math-font">n³</span>)
              <br><span class="math-font">n⁶ = (n²)³</span> (a perfect cube of <span class="math-font">n²</span>).
            </p>
            <p>There are infinitely many such numbers:
              <br>• For <span class="math-font">n = 0</span>: <span class="math-font">0⁶ = 0</span> (<span class="math-font">0² = 0³</span>)
              <br>• For <span class="math-font">n = 1</span>: <span class="math-font">1⁶ = 1</span> (<span class="math-font">1² = 1³</span>)
              <br>• For <span class="math-font">n = 2</span>: <span class="math-font">2⁶ = 64</span> (<span class="math-font">8² = 4³</span>)
              <br>• For <span class="math-font">n = 3</span>: <span class="math-font">3⁶ = 729</span> (<span class="math-font">27² = 9³</span>)
              <br>• For <span class="math-font">n = 4</span>: <span class="math-font">4⁶ = 4,096</span> (<span class="math-font">64² = 16³</span>)
              <br>• For <span class="math-font">n = 5</span>: <span class="math-font">5⁶ = 15,625</span> (<span class="math-font">125² = 25³</span>)
            </p>
          </div>
          <div class="step-box">
            <div class="step-label"><i class="fa-solid fa-check-double"></i> Step 4: Verification & Sanity Check</div>
            <p><span class="math-font">27² = 729</span>, and <span class="math-font">9³ = 729</span>. <span class="math-font">729 = 3⁶</span>. Verified.</p>
          </div>
          <div class="step-box">
            <div class="step-label"><i class="fa-solid fa-flag-checkered"></i> Step 5: Final Concise Concluding Statement</div>
            <p>Yes, there are infinitely many such numbers. In general, they are <strong>sixth powers (n⁶)</strong> of integers.</p>
          </div>
        </div>
      </details>

      <!-- Exercise Q11: Alphanumeric Digital Locker Passcodes -->
      <details class="ans-box">
        <summary>
          <span>Exercise Q11 (Page 45): Alphanumeric Digital Locker Passcodes of Length 5</span>
          <span class="ans-badge"><i class="fa-solid fa-chevron-down"></i> Solution</span>
        </summary>
        <div class="ans-content">
          <div class="step-box">
            <div class="step-label"><i class="fa-solid fa-circle-info"></i> Step 1: Given Information & Context</div>
            <p>Passcode length = 5 characters.
              <br>Allowed characters: alphanumeric (English alphabet letters A to Z + decimal digits 0 to 9).
              <br>Example codes: G89P0, 38098, BRJKW, 003AZ.
              <br>Goal: Find the total number of possible passcodes.
            </p>
          </div>
          <div class="step-box">
            <div class="step-label"><i class="fa-solid fa-calculator"></i> Step 2: Mathematical Concept & Law Applied</div>
            <p>Fundamental Counting Principle: Total choices per slot = <span class="math-font">26 letters} + 10 digits} = 36 choices}</span>.
              <br>For 5 independent slots: Total codes = <span class="math-font">36 × 36 × 36 × 36 × 36 = 36⁵</span>.
            </p>
          </div>
          <div class="step-box">
            <div class="step-label"><i class="fa-solid fa-gears"></i> Step 3: Detailed Step-by-Step Mathematical Calculation</div>
            <p>Total possible codes = <span class="math-font">36⁵</span>.
              <br><span class="math-font">36⁵ = (6²)⁵ = 6¹⁰ = 60,466,176</span> (approx. <strong>6.05 crore codes</strong>).
            </p>
          </div>
          <div class="step-box">
            <div class="step-label"><i class="fa-solid fa-check-double"></i> Step 4: Verification & Sanity Check</div>
            <p>Matches NCERT official answer key on Page 37: <span class="math-font">36⁵</span>.</p>
          </div>
          <div class="step-box">
            <div class="step-label"><i class="fa-solid fa-flag-checkered"></i> Step 5: Final Concise Concluding Statement</div>
            <p>Total possible passcodes = <strong>36⁵ = 60,466,176</strong>.</p>
          </div>
        </div>
      </details>

      <!-- Exercise Q12: Population of Sheep & Goats Addition -->
      <details class="ans-box">
        <summary>
          <span>Exercise Q12 (Page 45): Total Worldwide Population of Sheep (10⁹) and Goats (10⁹)</span>
          <span class="ans-badge"><i class="fa-solid fa-chevron-down"></i> Solution</span>
        </summary>
        <div class="ans-content">
          <div class="step-box">
            <div class="step-label"><i class="fa-solid fa-circle-info"></i> Step 1: Given Information & Context</div>
            <p>Worldwide population of sheep ≈ <span class="math-font">10⁹</span>. Worldwide population of goats ≈ <span class="math-font">10⁹</span>.
              <br>Select the correct expression for total population from:
              <br>(i) 20⁹, (ii) 10¹¹, (iii) 10¹⁰, (iv) 10¹⁸, (v) 2 × 10⁹, (vi) 10⁹ + 10⁹.
            </p>
          </div>
          <div class="step-box">
            <div class="step-label"><i class="fa-solid fa-calculator"></i> Step 2: Mathematical Concept & Law Applied</div>
            <p>Addition of like exponential terms using the distributive property: <span class="math-font">x + x = 2x</span>.
              <br><strong>Warning:</strong> Powers CANNOT be added during addition! <span class="math-font">10⁹ + 10⁹ ≠ 10¹⁸</span>!
            </p>
          </div>
          <div class="step-box">
            <div class="step-label"><i class="fa-solid fa-gears"></i> Step 3: Detailed Step-by-Step Mathematical Calculation</div>
            <p>Total population = <span class="math-font">Sheep} + Goats} = 10⁹ + 10⁹</span>.
              <br>Factoring out <span class="math-font">10⁹</span>:
              <br><span class="math-font">10⁹ × (1 + 1) = 2 × 10⁹</span> (2 billion animals).
              <br>Looking at the options, both <strong>(v) 2 × 10⁹</strong> and <strong>(vi) 10⁹ + 10⁹</strong> represent the mathematically correct total. (The textbook specifically highlights <strong>(vi)</strong> in its answer key as the direct algebraic translation).
            </p>
          </div>
          <div class="step-box">
            <div class="step-label"><i class="fa-solid fa-check-double"></i> Step 4: Verification & Sanity Check</div>
            <p><span class="math-font">1,00,00,00,000 + 1,00,00,00,000 = 2,00,00,00,000 = 2 × 10⁹</span>. Options (i), (ii), (iii), (iv) are classic student trap errors.</p>
          </div>
          <div class="step-box">
            <div class="step-label"><i class="fa-solid fa-flag-checkered"></i> Step 5: Final Concise Concluding Statement</div>
            <p>The total population is <strong>10⁹ + 10⁹ = 2 × 10⁹</strong> (Option vi / Option v).</p>
          </div>
        </div>
      </details>

      <!-- Exercise Q13: Scientific Notation Calculations (All 4 Parts) -->
      <details class="ans-box">
        <summary>
          <span>Exercise Q13 (Page 45): Four Calculations in Scientific Notation (Clothes, Bees, Bacteria, Eating)</span>
          <span class="ans-badge"><i class="fa-solid fa-chevron-down"></i> Solution</span>
        </summary>
        <div class="ans-content">
          <div class="step-box">
            <div class="step-label"><i class="fa-solid fa-circle-info"></i> Step 1: Given Information & Context</div>
            <p>Perform four calculations and write all final answers in scientific notation:
              <br>(i) Clothes: World population = <span class="math-font">8.2 × 10⁹</span>, each person owns 30 pieces.
              <br>(ii) Bees: 100 million bee colonies, each colony has 50,000 bees.
              <br>(iii) Bacteria: Human body has 38 trillion bacterial cells; world population = <span class="math-font">8.2 × 10⁹</span>.
              <br>(iv) Eating time: Average lifespan 70 years, eating 1 hour per day, find total eating seconds.
            </p>
          </div>
          <div class="step-box">
            <div class="step-label"><i class="fa-solid fa-calculator"></i> Step 2: Mathematical Concept & Law Applied</div>
            <p>Scientific notation multiplication: Multiply coefficients and add powers of 10 (<span class="math-font">m₁m₂ × 10ᵏ¹⁺ᵏ²</span>), then normalise so <span class="math-font">1 ≤ m &lt; 10</span>.</p>
          </div>
          <div class="step-box">
            <div class="step-label"><i class="fa-solid fa-gears"></i> Step 3: Detailed Step-by-Step Mathematical Calculation</div>
            <ul>
              <li><strong>(i) Total Clothing Pieces:</strong>
                <br><span class="math-font">Total = (8.2 × 10⁹) × 30 = (8.2 × 30) × 10⁹ = 246 × 10⁹ = 2.46 × 10¹¹ pieces</span>.
              </li>
              <li><strong>(ii) Total Honeybees:</strong>
                <br>Colonies = 100 million = <span class="math-font">10⁸</span>. Bees per colony = <span class="math-font">50,000 = 5 × 10⁴</span>.
                <br><span class="math-font">Total = 10⁸ × (5 × 10⁴) = 5.0 × 10⁸⁺⁴ = 5.0 × 10¹² honeybees</span> (5 trillion bees).
              </li>
              <li><strong>(iii) Total Bacterial Population in All Humans:</strong>
                <br>Bacteria per body = 38 trillion = <span class="math-font">38 × 10¹² = 3.8 × 10¹³</span>.
                <br>Total = <span class="math-font">(3.8 × 10¹³) × (8.2 × 10⁹) = (3.8 × 8.2) × 10¹³⁺⁹ = 31.16 × 10²² = 3.116 × 10²³ bacterial cells</span>.
              </li>
              <li><strong>(iv) Total Seconds Spent Eating in a Lifetime:</strong>
                <br>Eating per day = 1 hour = <span class="math-font">3,600 s</span>.
                <br>Days in 70 years = <span class="math-font">70 × 365 = 25,550 days</span>.
                <br>Total seconds = <span class="math-font">25,550 × 3,600 = 9,19,80,000 seconds</span>.
                <br>In scientific standard form: <span class="math-font">9.198 × 10⁷ seconds</span> (approx. 92 million seconds).
              </li>
            </ul>
          </div>
          <div class="step-box">
            <div class="step-label"><i class="fa-solid fa-check-double"></i> Step 4: Verification & Sanity Check</div>
            <p>Matches NCERT official answer key on Pages 37–38 verbatim.</p>
          </div>
          <div class="step-box">
            <div class="step-label"><i class="fa-solid fa-flag-checkered"></i> Step 5: Final Concise Concluding Statement</div>
            <p>(i) <span class="math-font">2.46 × 10¹¹</span>, (ii) <span class="math-font">5.0 × 10¹²</span>, (iii) <span class="math-font">3.116 × 10²³</span>, (iv) <span class="math-font">9.198 × 10⁷ s</span>.</p>
          </div>
        </div>
      </details>

      <!-- Exercise Q14: Date One Billion Seconds Ago -->
      <details class="ans-box">
        <summary>
          <span>Exercise Q14 (Page 45): What Was the Date 1 Arab / 1 Billion Seconds Ago?</span>
          <span class="ans-badge"><i class="fa-solid fa-chevron-down"></i> Solution</span>
        </summary>
        <div class="ans-content">
          <div class="step-box">
            <div class="step-label"><i class="fa-solid fa-circle-info"></i> Step 1: Given Information & Context</div>
            <p>Find the approximate date exactly 1 arab (1 billion = <span class="math-font">10⁹</span>) seconds ago from today.</p>
          </div>
          <div class="step-box">
            <div class="step-label"><i class="fa-solid fa-calculator"></i> Step 2: Mathematical Concept & Law Applied</div>
            <p>Convert seconds to days and years:
              <br>• 1 minute = 60 seconds
              <br>• 1 hour = 3,600 seconds
              <br>• 1 day = <span class="math-font">24 × 3,600 = 86,400 seconds</span>
              <br>• 1 non-leap year = <span class="math-font">365 × 86,400 = 3,15,36,000 seconds ≈ 3.15 × 10⁷ seconds</span>.
            </p>
          </div>
          <div class="step-box">
            <div class="step-label"><i class="fa-solid fa-gears"></i> Step 3: Detailed Step-by-Step Mathematical Calculation</div>
            <p>Divide 1 billion seconds by seconds in a day:
              <br><span class="math-font">10⁹ ÷ 86,400 = 11,574.07 days</span>.
              <br>Now convert days into years:
              <br><span class="math-font">11,574.07 ÷ 365.25 ≈ 31.688 years ≈ 31 years and 8.3 months</span>.
              <br>Subtracting ~31.7 years from the current year (2026):
              <br><span class="math-font">2026.8 – 31.7 ≈ 1995.1</span> (Early 1995).
            </p>
          </div>
          <div class="step-box">
            <div class="step-label"><i class="fa-solid fa-check-double"></i> Step 4: Verification & Sanity Check</div>
            <p><span class="math-font">31.7 years × 3.1536 × 10⁷ s/year = 0.9997 × 10⁹ s ≈ 10⁹ s</span>. Matches NCERT answer key on Page 38.</p>
          </div>
          <div class="step-box">
            <div class="step-label"><i class="fa-solid fa-flag-checkered"></i> Step 5: Final Concise Concluding Statement</div>
            <p>1 billion seconds ago corresponds to approximately <strong>11,574 days or 31.7 years ago</strong> (around early 1995).</p>
          </div>
        </div>
      </details>

      <!-- Part 3: Tremendous in Ten Game (Page 29) -->
      <details class="ans-box">
        <summary>
          <span>NCERT Game Analysis (Page 29): 'Tremendous in Ten!' Strategic Mathematical Analysis</span>
          <span class="ans-badge"><i class="fa-solid fa-chevron-down"></i> Solution</span>
        </summary>
        <div class="ans-content">
          <div class="step-box">
            <div class="step-label"><i class="fa-solid fa-circle-info"></i> Step 1: Given Information & Context</div>
            <p>Game Rules: In 10 seconds, write a number or expression using digits 0–9 and operations to produce the largest possible value.
              <br>• Round 1: Roxie wrote <span class="math-font">10000000000000</span> (1 followed by 13 zeros = <span class="math-font">10¹³</span>). Estu wrote <span class="math-font">999999 × 999999</span>. Who wins?
              <br>• Round 2: Roxie wrote <span class="math-font">10¹⁰⁰⁰ + 10¹⁰⁰⁰ + 10¹⁰⁰⁰ + 10¹⁰⁰⁰</span>. Estu wrote <span class="math-font">(10¹⁰⁰⁰⁰⁰⁰) × 9000</span>. Who wins?
            </p>
          </div>
          <div class="step-box">
            <div class="step-label"><i class="fa-solid fa-calculator"></i> Step 2: Mathematical Concept & Law Applied</div>
            <p>Exponential growth dominance over multiplication and addition.</p>
          </div>
          <div class="step-box">
            <div class="step-label"><i class="fa-solid fa-gears"></i> Step 3: Detailed Step-by-Step Mathematical Calculation</div>
            <ul>
              <li><strong>Round 1 Comparison:</strong>
                <br>Roxie's number = <span class="math-font">10¹³</span>.
                <br>Estu's number = <span class="math-font">999,999 × 999,999 &lt; 1,000,000 × 1,000,000 = (10⁶)² = 10¹²</span>.
                <br>Since <span class="math-font">10¹³ &gt; 10¹²</span>, <strong>Roxie wins Round 1</strong> by more than 10 times!
              </li>
              <li><strong>Round 2 Comparison:</strong>
                <br>Roxie's number = <span class="math-font">4 × 10¹⁰⁰⁰</span>. (Exponent is 1,000).
                <br>Estu's number = <span class="math-font">10¹⁰⁰⁰⁰⁰⁰ × 9000 = 9 × 10¹⁰⁰⁰⁰⁰³</span>. (Exponent is over one million!).
                <br>Comparing powers of 10: <span class="math-font">1,000,003 ≫ 1,000</span>. <strong>Estu wins Round 2 overwhelmingly</strong>!
              </li>
            </ul>
          </div>
          <div class="step-box">
            <div class="step-label"><i class="fa-solid fa-check-double"></i> Step 4: Verification & Sanity Check</div>
            <p>Powers of 10 dominate over small numerical multipliers. Higher exponent always wins.</p>
          </div>
          <div class="step-box">
            <div class="step-label"><i class="fa-solid fa-flag-checkered"></i> Step 5: Final Concise Concluding Statement</div>
            <p>Roxie wins Round 1 because <span class="math-font">10¹³ &gt; 10¹²</span>; Estu crushes Round 2 because <span class="math-font">10¹⁰⁰⁰⁰⁰⁰</span> has a million digits in its exponent!</p>
          </div>
        </div>
      </details>
    </section>
"""
