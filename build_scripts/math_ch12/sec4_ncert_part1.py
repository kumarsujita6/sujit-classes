# -*- coding: utf-8 -*-
"""
Section 4 Part 1 Module: In-Text Explorations & Figure it Out 1
Class 8 Mathematics Chapter 12: Tales by Dots and Lines (NCERT NEP code: hegp112)
"""

def get_section_4_part1():
    return """
    <!-- SECTION 4: 100% SOLVED NCERT QUESTIONS (PART 1) -->
    <section id="section4" class="section-box">
      <div class="section-header">
        <div class="section-header-left">
          <span class="section-tag">Textbook Mastery • Zero-Omission</span>
          <h2 class="section-title">§ 4. 100% Solved NCERT Questions (Part 1: In-Text Explorations &amp; Figure it Out 1)</h2>
          <p class="section-desc">
            Every in-text prompt, 'Math Talk', classroom activity, and 'Figure it Out' problem from Book Pages 103 to 116 completely solved in a strict 5-step presentation format inside collapsible solution containers.
          </p>
        </div>
        <div>
          <span class="badge badge-emerald"><i class="fa-solid fa-check-double"></i> In-Text + FIO 1 Solved</span>
        </div>
      </div>

      <!-- ========================================================
           SUBSECTION 4A: IN-TEXT EXPLORATIONS & MATH TALKS
           ======================================================== -->
      <div style="margin-bottom: 2.5rem;">
        <h3 style="font-family: 'Space Grotesk', sans-serif; font-size: 1.4rem; color: var(--primary-dark); margin-bottom: 1.25rem;">
          <i class="fa-solid fa-comments"></i> Part 4A: In-Text Explorations &amp; Math Talks (Book Pages 103–113)
        </h3>

        <!-- Exploration 1 -->
        <div class="solved-card">
          <div class="solved-title"><i class="fa-solid fa-puzzle-piece"></i> Exploration 1: Arithmetic Mean of Two Numbers &amp; Midpoint Property (Book p. 103)</div>
          <p>
            Consider any 2 numbers. Find their average/arithmetic mean. Repeat this by taking other pairs (e.g., 3 and 7; 8 and 9). What do you observe about the position of the mean on a number line?
          </p>
          <details class="ans-box">
            <summary>View 5-Step Solution</summary>
            <div class="ans-content">
              <div class="step-box">
                <div class="step-num">1</div>
                <div class="step-text"><strong>Given Information &amp; Context:</strong> Two pairs of numbers: Pair A = {3, 7} and Pair B = {8, 9}.</div>
              </div>
              <div class="step-box">
                <div class="step-num">2</div>
                <div class="step-text"><strong>Core Mathematical Principle:</strong> For any two numbers <span class="math-inline">a</span> and <span class="math-inline">b</span>, their arithmetic mean is <span class="math-inline">x̄ = (a + b) / 2</span>. In Euclidean geometry, the point <span class="math-inline">(a + b)/2</span> is the exact coordinate of the midpoint of the line segment joining <span class="math-inline">a</span> and <span class="math-inline">b</span>.</div>
              </div>
              <div class="step-box">
                <div class="step-num">3</div>
                <div class="step-text"><strong>Step-by-Step Calculation:</strong>
                  <br>&bull; For Pair A: <span class="math-inline">x̄ = (3 + 7) / 2 = 10 / 2 = 5</span>.
                  <br>Distance from 3 to 5 = <span class="math-inline">5 - 3 = 2</span>. Distance from 5 to 7 = <span class="math-inline">7 - 5 = 2</span>.
                  <br>&bull; For Pair B: <span class="math-inline">x̄ = (8 + 9) / 2 = 17 / 2 = 8.5</span>.
                  <br>Distance from 8 to 8.5 = <span class="math-inline">8.5 - 8 = 0.5</span>. Distance from 8.5 to 9 = <span class="math-inline">9 - 8.5 = 0.5</span>.
                </div>
              </div>
              <div class="step-box">
                <div class="step-num">4</div>
                <div class="step-text"><strong>Verification &amp; Check:</strong> In both cases, the distance from the smaller number to the mean exactly equals the distance from the mean to the larger number.</div>
              </div>
              <div class="step-box">
                <div class="step-num">5</div>
                <div class="step-text"><strong>Concluding Statement:</strong> For any two numbers, the arithmetic mean is <em>always exactly halfway</em> between them, dividing the line segment into two congruent halves.</div>
              </div>
            </div>
          </details>
        </div>

        <!-- Exploration 2 -->
        <div class="solved-card">
          <div class="solved-title"><i class="fa-solid fa-puzzle-piece"></i> Exploration 2: Is the Mean the Midpoint of Extremes for 3 or More Numbers? (Book p. 104)</div>
          <p>
            Is the mean always the midpoint of the two endpoints/extremes of the data? Explain how the mean acts as the "center" for a collection of numbers like {10, 10, 11, 17}.
          </p>
          <details class="ans-box">
            <summary>View 5-Step Solution</summary>
            <div class="ans-content">
              <div class="step-box">
                <div class="step-num">1</div>
                <div class="step-text"><strong>Given Information &amp; Context:</strong> Dataset {10, 10, 11, 17}. Extreme endpoints are Minimum = 10 and Maximum = 17.</div>
              </div>
              <div class="step-box">
                <div class="step-num">2</div>
                <div class="step-text"><strong>Core Mathematical Principle:</strong> The midpoint of extremes is <span class="math-inline">(Min + Max) / 2</span>. The arithmetic mean is <span class="math-inline">(&Sigma; x_i) / n</span>. The mean is the center <strong>not</strong> because it is the midpoint of extremes, but because <strong>the sum of all distances on its left equals the sum of all distances on its right</strong>.</div>
              </div>
              <div class="step-box">
                <div class="step-num">3</div>
                <div class="step-text"><strong>Step-by-Step Calculation:</strong>
                  <br>&bull; Midpoint of extremes = <span class="math-inline">(10 + 17) / 2 = 27 / 2 = 13.5</span>.
                  <br>&bull; True Arithmetic Mean = <span class="math-inline">(10 + 10 + 11 + 17) / 4 = 48 / 4 = 12</span>.
                  <br>&bull; Notice that <span class="math-inline">12 &ne; 13.5</span>! So mean is NOT the midpoint of extremes.
                  <br>&bull; Sum of LHS distances from 12: <span class="math-inline">(12 - 10) + (12 - 10) + (12 - 11) = 2 + 2 + 1 = 5</span>.
                  <br>&bull; Sum of RHS distances from 12: <span class="math-inline">17 - 12 = 5</span>.
                </div>
              </div>
              <div class="step-box">
                <div class="step-num">4</div>
                <div class="step-text"><strong>Verification &amp; Check:</strong> Total LHS distances (5) = Total RHS distances (5). The condition <span class="math-inline">&Sigma; (x_i - x̄) = 0</span> is satisfied at <span class="math-inline">x̄ = 12</span>.</div>
              </div>
              <div class="step-box">
                <div class="step-num">5</div>
                <div class="step-text"><strong>Concluding Statement:</strong> For three or more numbers, the mean is generally <em>not</em> the midpoint of extremes; rather, it is the unique point where total leftward deviations equal total rightward deviations.</div>
              </div>
            </div>
          </details>
        </div>

        <!-- Exploration 3 -->
        <div class="solved-card">
          <div class="solved-title"><i class="fa-solid fa-puzzle-piece"></i> Exploration 3: Including or Removing Values Relative to the Mean (Book p. 105)</div>
          <p>
            (i) Will including a new value greater than the mean increase or decrease the mean?
            <br>(ii) What happens to the mean when an existing value is removed?
            <br>(iii) What happens to the mean if a value equal to the mean is included or removed? Explain using fair-share.
          </p>
          <details class="ans-box">
            <summary>View 5-Step Solution</summary>
            <div class="ans-content">
              <div class="step-box">
                <div class="step-num">1</div>
                <div class="step-text"><strong>Given Information &amp; Context:</strong> An initial dataset with <span class="math-inline">n</span> observations and mean <span class="math-inline">x̄</span>.</div>
              </div>
              <div class="step-box">
                <div class="step-num">2</div>
                <div class="step-text"><strong>Core Mathematical Principle:</strong>
                  <br>&bull; New Mean after adding <span class="math-inline">v</span>: <span class="math-inline">x̄_new = (n&middot;x̄ + v) / (n + 1) = x̄ + (v - x̄)/(n + 1)</span>.
                  <br>&bull; New Mean after removing <span class="math-inline">v</span>: <span class="math-inline">x̄_new = (n&middot;x̄ - v) / (n - 1) = x̄ - (v - x̄)/(n - 1)</span>.</div>
              </div>
              <div class="step-box">
                <div class="step-num">3</div>
                <div class="step-text"><strong>Step-by-Step Analysis:</strong>
                  <br>&bull; <strong>Case (i) Adding <span class="math-inline">v &gt; x̄</span>:</strong> <span class="math-inline">(v - x̄) &gt; 0</span>, so the second term is positive. The mean <strong>strictly increases</strong>.
                  <br>&bull; <strong>Case (ii) Removing an existing value:</strong>
                  <br>&nbsp;&nbsp;- If removed value <span class="math-inline">v &gt; x̄</span>: <span class="math-inline">-(v - x̄) &lt; 0</span>, so the mean <strong>decreases</strong>.
                  <br>&nbsp;&nbsp;- If removed value <span class="math-inline">v &lt; x̄</span>: <span class="math-inline">-(v - x̄) &gt; 0</span>, so the mean <strong>increases</strong>.
                  <br>&nbsp;&nbsp;- If removed value <span class="math-inline">v = x̄</span>: the mean <strong>stays the same</strong>.
                  <br>&bull; <strong>Case (iii) Adding/Removing <span class="math-inline">v = x̄</span>:</strong> In fair-share terms, if everyone has an average of ₹10, and a new child joins who already has exactly ₹10, no redistribution is required! Everyone still holds exactly ₹10. Similarly, if a child with ₹10 leaves, the remaining pool is undisturbed.
                </div>
              </div>
              <div class="step-box">
                <div class="step-num">4</div>
                <div class="step-text"><strong>Verification &amp; Check:</strong> Let data be {4, 6}, <span class="math-inline">x̄ = 5</span>. Add 8 (&gt;5) &rArr; {4, 6, 8}, <span class="math-inline">x̄' = 18/3 = 6 &gt; 5</span> (increased). Add 5 (=5) &rArr; {4, 5, 6}, <span class="math-inline">x̄' = 15/3 = 5</span> (unchanged). Remove 4 (&lt;5) &rArr; {6}, <span class="math-inline">x̄' = 6 &gt; 5</span> (increased).</div>
              </div>
              <div class="step-box">
                <div class="step-num">5</div>
                <div class="step-text"><strong>Concluding Statement:</strong> Incorporating an observation above the mean pulls the mean up; removing an observation above the mean drags it down; transactions at exactly the mean produce zero change.</div>
              </div>
            </div>
          </details>
        </div>

        <!-- Exploration 4 -->
        <div class="solved-card">
          <div class="solved-title"><i class="fa-solid fa-puzzle-piece"></i> Exploration 4: The "Unchanging Mean" Challenge (Book p. 106)</div>
          <p>
            (i) Explore if it is possible to include 2 values such that the mean is unchanged.
            <br>(ii) Can we include 2 values less than the mean and 1 value greater than the mean so that the mean remains the same? Give an example.
            <br>(iii) Try to include 2 values greater than the mean and 1 value less than the mean so that the mean stays the same.
          </p>
          <details class="ans-box">
            <summary>View 5-Step Solution</summary>
            <div class="ans-content">
              <div class="step-box">
                <div class="step-num">1</div>
                <div class="step-text"><strong>Given Information &amp; Context:</strong> Let the initial mean be <span class="math-inline">x̄ = 10</span>. We wish to add new values without changing the mean.</div>
              </div>
              <div class="step-box">
                <div class="step-num">2</div>
                <div class="step-text"><strong>Core Mathematical Principle:</strong> For the mean to remain invariant when a set of <span class="math-inline">m</span> new values <span class="math-inline">{y₁, y₂, ..., yₘ}</span> is inserted, their net deviation from <span class="math-inline">x̄</span> must be zero: <span class="math-inline">&Sigma; (y_j - x̄) = 0</span>, which is equivalent to saying that their own average must equal <span class="math-inline">x̄</span>.</div>
              </div>
              <div class="step-box">
                <div class="step-num">3</div>
                <div class="step-text"><strong>Step-by-Step Constructions:</strong>
                  <br>&bull; <strong>(i) Including 2 values:</strong> Choose two numbers symmetric about 10. For example, <strong>7 and 13</strong>.
                  <br>Deviations: <span class="math-inline">(7 - 10) + (13 - 10) = -3 + 3 = 0</span>. Average is still 10.
                  <br>&bull; <strong>(ii) 2 values &lt; mean, 1 value &gt; mean:</strong>
                  <br>Let the two smaller values be 8 (dev = -2) and 6 (dev = -4). Total leftward deviation = <span class="math-inline">-2 + (-4) = -6</span>.
                  <br>To balance this, the third value must have a rightward deviation of +6: <span class="math-inline">10 + 6 = 16</span>.
                  <br>Values to insert: <strong>{6, 8, 16}</strong>. Net deviation = <span class="math-inline">-4 + (-2) + 6 = 0</span>.
                  <br>&bull; <strong>(iii) 2 values &gt; mean, 1 value &lt; mean:</strong>
                  <br>Let the two larger values be 12 (dev = +2) and 15 (dev = +5). Total rightward deviation = <span class="math-inline">+2 + 5 = +7</span>.
                  <br>To balance, the single smaller value must have a deviation of -7: <span class="math-inline">10 - 7 = 3</span>.
                  <br>Values to insert: <strong>{3, 12, 15}</strong>. Net deviation = <span class="math-inline">-7 + 2 + 5 = 0</span>.
                </div>
              </div>
              <div class="step-box">
                <div class="step-num">4</div>
                <div class="step-text"><strong>Verification &amp; Check:</strong> Average of {3, 12, 15} = <span class="math-inline">(3 + 12 + 15) / 3 = 30 / 3 = 10</span>. Since their own average is 10, adding them to a collection with mean 10 preserves the mean exactly.</div>
              </div>
              <div class="step-box">
                <div class="step-num">5</div>
                <div class="step-text"><strong>Concluding Statement:</strong> Any collection of numbers whose individual deviations sum to zero can be inserted or removed without shifting the arithmetic mean.</div>
              </div>
            </div>
          </details>
        </div>

        <!-- Exploration 5 -->
        <div class="solved-card">
          <div class="solved-title"><i class="fa-solid fa-puzzle-piece"></i> Exploration 5: Algebraic Proof of Subtracting a Constant (Book p. 107)</div>
          <p>
            Explain using algebra what the new average is when a fixed number (e.g., 2) is subtracted from every value in a collection.
          </p>
          <details class="ans-box">
            <summary>View 5-Step Solution</summary>
            <div class="ans-content">
              <div class="step-box">
                <div class="step-num">1</div>
                <div class="step-text"><strong>Given Information &amp; Context:</strong> An original collection of <span class="math-inline">n</span> values: <span class="math-inline">x₁, x₂, x₃, ..., xₙ</span> with average <span class="math-inline">a = (x₁ + x₂ + ... + xₙ) / n</span>. A constant 2 is subtracted from each value.</div>
              </div>
              <div class="step-box">
                <div class="step-num">2</div>
                <div class="step-text"><strong>Core Mathematical Principle:</strong> Definition of average = Sum of new values &divide; Total count of values.</div>
              </div>
              <div class="step-box">
                <div class="step-num">3</div>
                <div class="step-text"><strong>Step-by-Step Algebraic Derivation:</strong>
                  <br>New values: <span class="math-inline">(x₁ - 2), (x₂ - 2), (x₃ - 2), ..., (xₙ - 2)</span>.
                  <br>New Average = <span class="math-inline">[(x₁ - 2) + (x₂ - 2) + ... + (xₙ - 2)] / n</span>
                  <br>Grouping terms: = <span class="math-inline">[(x₁ + x₂ + ... + xₙ) - (2 + 2 + ... + 2 to n terms)] / n</span>
                  <br>= <span class="math-inline">[(x₁ + x₂ + ... + xₙ) - 2n] / n</span>
                  <br>Splitting the fraction: = <span class="math-inline">[(x₁ + x₂ + ... + xₙ) / n] - (2n / n)</span>
                  <br>= <span class="math-inline">a - 2</span>.
                </div>
              </div>
              <div class="step-box">
                <div class="step-num">4</div>
                <div class="step-text"><strong>Verification &amp; Check:</strong> Let data be {10, 14}, <span class="math-inline">a = (10+14)/2 = 12</span>. Subtract 2 from each: {8, 12}. New average = <span class="math-inline">(8+12)/2 = 10</span>. Indeed, <span class="math-inline">12 - 2 = 10</span>.</div>
              </div>
              <div class="step-box">
                <div class="step-num">5</div>
                <div class="step-text"><strong>Concluding Statement:</strong> When any constant <span class="math-inline">c</span> is subtracted from all values in a dataset, the new average is precisely <span class="math-inline">a - c</span>.</div>
              </div>
            </div>
          </details>
        </div>

        <!-- Exploration 6 -->
        <div class="solved-card">
          <div class="solved-title"><i class="fa-solid fa-puzzle-piece"></i> Exploration 6: Algebraic Proof of Multiplying Every Value by a Factor (Book p. 108)</div>
          <p>
            Prove algebraically that when every value in a collection is multiplied by a constant factor <span class="math-inline">k = 5</span>, the new average becomes 5 times the previous average.
          </p>
          <details class="ans-box">
            <summary>View 5-Step Solution</summary>
            <div class="ans-content">
              <div class="step-box">
                <div class="step-num">1</div>
                <div class="step-text"><strong>Given Information &amp; Context:</strong> Collection of <span class="math-inline">n</span> observations <span class="math-inline">x₁, x₂, ..., xₙ</span> with initial average <span class="math-inline">a = (&Sigma; x_i) / n</span>. Every observation is scaled by factor 5.</div>
              </div>
              <div class="step-box">
                <div class="step-num">2</div>
                <div class="step-text"><strong>Core Mathematical Principle:</strong> The Distributive Law of Multiplication over Addition: <span class="math-inline">k&middot;x₁ + k&middot;x₂ + ... + k&middot;xₙ = k&middot;(x₁ + x₂ + ... + xₙ)</span>.</div>
              </div>
              <div class="step-box">
                <div class="step-num">3</div>
                <div class="step-text"><strong>Step-by-Step Algebraic Derivation:</strong>
                  <br>New values: <span class="math-inline">5x₁, 5x₂, 5x₃, ..., 5xₙ</span>.
                  <br>New Average = <span class="math-inline">[5x₁ + 5x₂ + 5x₃ + ... + 5xₙ] / n</span>
                  <br>Factoring out 5 (Distributive Law): = <span class="math-inline">5 &times; (x₁ + x₂ + ... + xₙ) / n</span>
                  <br>= <span class="math-inline">5 &times; [(x₁ + x₂ + ... + xₙ) / n]</span>
                  <br>= <span class="math-inline">5 &times; a</span>.
                </div>
              </div>
              <div class="step-box">
                <div class="step-num">4</div>
                <div class="step-text"><strong>Verification &amp; Check:</strong> Let data be {2, 6}, <span class="math-inline">a = 4</span>. Multiply each by 5 &rArr; {10, 30}. New average = <span class="math-inline">(10 + 30)/2 = 20</span>. Indeed, <span class="math-inline">5 &times; 4 = 20</span>.</div>
              </div>
              <div class="step-box">
                <div class="step-num">5</div>
                <div class="step-text"><strong>Concluding Statement:</strong> Multiplying every observation by <span class="math-inline">k</span> scales the arithmetic mean by exactly <span class="math-inline">k</span>.</div>
              </div>
            </div>
          </details>
        </div>

        <!-- Exploration 7 -->
        <div class="solved-card">
          <div class="solved-title"><i class="fa-solid fa-puzzle-piece"></i> Exploration 7: Coach Balwan's Smudged Kushti Wrestler Weight (Book p. 109)</div>
          <p>
            Coach Balwan noted down the weights of 10 kushti players (wrestlers) and their mean as 39.2 kg. But one weight got smudged: 42, 40, 39, 33, 48, 38, 42, 35, 32, and <span class="math-inline">w</span> kg. Find the missing weight <span class="math-inline">w</span>.
          </p>
          <details class="ans-box">
            <summary>View 5-Step Solution</summary>
            <div class="ans-content">
              <div class="step-box">
                <div class="step-num">1</div>
                <div class="step-text"><strong>Given Information &amp; Context:</strong> Total wrestlers <span class="math-inline">n = 10</span>. Mean weight <span class="math-inline">x̄ = 39.2  kg</span>. Nine known weights: 42, 40, 39, 33, 48, 38, 42, 35, 32 kg. Unknown weight = <span class="math-inline">w</span>.</div>
              </div>
              <div class="step-box">
                <div class="step-num">2</div>
                <div class="step-text"><strong>Core Mathematical Principle:</strong> <span class="math-inline">Total Sum = Mean &times; n</span>. Therefore, <span class="math-inline">Sum of all 10 weights = 39.2 &times; 10</span>.</div>
              </div>
              <div class="step-box">
                <div class="step-num">3</div>
                <div class="step-text"><strong>Step-by-Step Calculation:</strong>
                  <br>&bull; Target Total Weight = <span class="math-inline">39.2 &times; 10 = 392  kg</span>.
                  <br>&bull; Sum of 9 known weights:
                  <br><span class="math-inline">42 + 40 + 39 + 33 + 48 + 38 + 42 + 35 + 32 = 349  kg</span>.
                  <br>&bull; Set up the linear equation:
                  <br><span class="math-inline">349 + w = 392</span>
                  <br><span class="math-inline">w = 392 - 349 = 43  kg</span>.
                </div>
              </div>
              <div class="step-box">
                <div class="step-num">4</div>
                <div class="step-text"><strong>Verification &amp; Check:</strong> Total sum with <span class="math-inline">w = 43</span>: <span class="math-inline">349 + 43 = 392</span>. Average = <span class="math-inline">392 / 10 = 39.2  kg</span>. The answer is completely verified!</div>
              </div>
              <div class="step-box">
                <div class="step-num">5</div>
                <div class="step-text"><strong>Concluding Statement:</strong> The smudged wrestler's weight is <strong>43 kg</strong>.</div>
              </div>
            </div>
          </details>
        </div>

        <!-- Exploration 8 -->
        <div class="solved-card">
          <div class="solved-title"><i class="fa-solid fa-puzzle-piece"></i> Exploration 8: Venkayya's Coconut Harvest Recount Correction (Book p. 109)</div>
          <p>
            Venkayya keeps track of the coconut harvest across 15 trees. He calculates the average harvest per tree as 25.6. His son verifies the counts and finds that one tree's harvest count was incorrectly noted as 3 more than the actual number. Find the correct average harvest.
          </p>
          <details class="ans-box">
            <summary>View 5-Step Solution</summary>
            <div class="ans-content">
              <div class="step-box">
                <div class="step-num">1</div>
                <div class="step-text"><strong>Given Information &amp; Context:</strong> Number of trees <span class="math-inline">n = 15</span>. Incorrect initial average <span class="math-inline">x̄_old = 25.6</span>. An error of <span class="math-inline">+3</span> was made on one tree.</div>
              </div>
              <div class="step-box">
                <div class="step-num">2</div>
                <div class="step-text"><strong>Core Mathematical Principle:</strong>
                  <br>Method 1 (Total Sum): <span class="math-inline">Correct Sum = Old Sum - Error</span>. Correct Average = <span class="math-inline">Correct Sum / n</span>.
                  <br>Method 2 (Average Correction): <span class="math-inline">Correct Average = Old Average - (Error / n)</span>.</div>
              </div>
              <div class="step-box">
                <div class="step-num">3</div>
                <div class="step-text"><strong>Step-by-Step Calculation:</strong>
                  <br>&bull; <em>Method 1:</em>
                  <br>Initial recorded total coconuts = <span class="math-inline">25.6 &times; 15 = 384</span>.
                  <br>Actual total coconuts = <span class="math-inline">384 - 3 = 381</span>.
                  <br>Correct Average = <span class="math-inline">381 / 15 = 25.4</span>.
                  <br>&bull; <em>Method 2 (Quick Mental Math):</em>
                  <br>Average reduction = <span class="math-inline">3 / 15 = 1 / 5 = 0.2</span>.
                  <br>Correct Average = <span class="math-inline">25.6 - 0.2 = 25.4</span>.
                </div>
              </div>
              <div class="step-box">
                <div class="step-num">4</div>
                <div class="step-text"><strong>Verification &amp; Check:</strong> <span class="math-inline">25.4 &times; 15 = 381</span>. Both methods yield identical results.</div>
              </div>
              <div class="step-box">
                <div class="step-num">5</div>
                <div class="step-text"><strong>Concluding Statement:</strong> The true corrected average coconut harvest per tree is <strong>25.4 coconuts</strong>.</div>
              </div>
            </div>
          </details>
        </div>

        <!-- Exploration 9 -->
        <div class="solved-card">
          <div class="solved-title"><i class="fa-solid fa-puzzle-piece"></i> Exploration 9: Family Size Frequency Table — Mean &amp; Cumulative Median (Book p. 110)</div>
          <p>
            The family size data of 36 students in Grade 8 is given:
            <br>Sizes: 3, 4, 5, 6, 7, 8, 9, 10 with frequencies 3, 11, 9, 7, 3, 1, 1, 1 respectively.
            <br>(i) Find the average family size. (ii) Find the median family size using cumulative frequencies.
          </p>
          <details class="ans-box">
            <summary>View 5-Step Solution</summary>
            <div class="ans-content">
              <div class="step-box">
                <div class="step-num">1</div>
                <div class="step-text"><strong>Given Information &amp; Context:</strong> Grouped discrete frequency distribution of family sizes across <span class="math-inline">N = 36</span> students.</div>
              </div>
              <div class="step-box">
                <div class="step-num">2</div>
                <div class="step-text"><strong>Core Mathematical Principle:</strong>
                  <br>&bull; Weighted Mean: <span class="math-inline">x̄ = (&Sigma; f_i&middot;x_i) / (&Sigma; f_i)</span>.
                  <br>&bull; Median for even <span class="math-inline">N = 36</span>: Average of 18th and 19th values in cumulative order.</div>
              </div>
              <div class="step-box">
                <div class="step-num">3</div>
                <div class="step-text"><strong>Step-by-Step Calculation:</strong>
                  <br>&bull; <em>Calculating &Sigma; f&middot;x:</em>
                  <br>3 &times; 3 = 9
                  <br>4 &times; 11 = 44
                  <br>5 &times; 9 = 45
                  <br>6 &times; 7 = 42
                  <br>7 &times; 3 = 21
                  <br>8 &times; 1 = 8
                  <br>9 &times; 1 = 9
                  <br>10 &times; 1 = 10
                  <br>Total Sum = <span class="math-inline">9 + 44 + 45 + 42 + 21 + 8 + 9 + 10 = 188</span>.
                  <br>Average = <span class="math-inline">188 / 36 &approx; 5.22</span> members.
                  <br>&bull; <em>Finding Median:</em>
                  <br>Cumulative frequency up to 4: <span class="math-inline">3 + 11 = 14</span> (covers ranks 1 to 14).
                  <br>Cumulative frequency up to 5: <span class="math-inline">14 + 9 = 23</span> (covers ranks 15 to 23).
                  <br>Since positions 18 and 19 fall into the interval [15, 23], both the 18th and 19th values are 5!
                  <br>Median = <span class="math-inline">(5 + 5) / 2 = 5</span> members.
                </div>
              </div>
              <div class="step-box">
                <div class="step-num">4</div>
                <div class="step-text"><strong>Verification &amp; Check:</strong> The mean (5.22) is slightly higher than the median (5) because larger family sizes (7, 8, 9, 10) exert rightward torque.</div>
              </div>
              <div class="step-box">
                <div class="step-num">5</div>
                <div class="step-text"><strong>Concluding Statement:</strong> The average family size is <strong>5.22 members</strong> and the median family size is <strong>5 members</strong>.</div>
              </div>
            </div>
          </details>
        </div>

        <!-- Exploration 10 -->
        <div class="solved-card">
          <div class="solved-title"><i class="fa-solid fa-puzzle-piece"></i> Exploration 10: Sudhakar's Marksheet Spreadsheet Analysis (Book p. 111–113)</div>
          <p>
            (i) Which cell contains Farooq's score in Mathematics?
            <br>(ii) What data is located in column B7?
            <br>(iii) What formula would you type to calculate the class average in Science?
            <br>(iv) How would you check if class average in Odia exceeds Telugu?
          </p>
          <details class="ans-box">
            <summary>View 5-Step Solution</summary>
            <div class="ans-content">
              <div class="step-box">
                <div class="step-num">1</div>
                <div class="step-text"><strong>Given Information &amp; Context:</strong> A digital marksheet with columns: A (Name), B (Odia), C (Telugu), D (English), E (Maths), F (Social Science), G (Science), H (Total). Students occupy rows 3 to 24.</div>
              </div>
              <div class="step-box">
                <div class="step-num">2</div>
                <div class="step-text"><strong>Core Mathematical Principle:</strong> Spreadsheet cell coordinates combine the column letter and row number. Formula syntax begins with '=' followed by function name and parenthesized range <span class="math-inline">StartCell:EndCell</span>.</div>
              </div>
              <div class="step-box">
                <div class="step-num">3</div>
                <div class="step-text"><strong>Step-by-Step Answers:</strong>
                  <br>&bull; (i) Farooq is in row 6 (or row 5 depending on header rows). Looking at the marks table, Farooq's Mathematics score is located in <strong>cell E5</strong> (or E6).
                  <br>&bull; (ii) Cell B7 contains <strong>Pankaj's score in Odia (16 marks)</strong>.
                  <br>&bull; (iii) To find the class average in Science (column G, rows 3 to 24), type:
                  <div class="math-block">=AVERAGE(G3:G24)</div>
                  <br>&bull; (iv) Type <span class="math-inline">=AVERAGE(B3:B24)</span> in the summary row for Odia and <span class="math-inline">=AVERAGE(C3:C24)</span> for Telugu, then compare the two values.
                </div>
              </div>
              <div class="step-box">
                <div class="step-num">4</div>
                <div class="step-text"><strong>Verification &amp; Check:</strong> Digital formulas dynamically compute without manual arithmetic errors, updating whenever cell data changes.</div>
              </div>
              <div class="step-box">
                <div class="step-num">5</div>
                <div class="step-text"><strong>Concluding Statement:</strong> Spreadsheets automate aggregate totals and averages across hundreds of cells with standard formulas <span class="math-inline">=SUM()</span> and <span class="math-inline">=AVERAGE()</span>.</div>
              </div>
            </div>
          </details>
        </div>
      </div>

      <!-- ========================================================
           SUBSECTION 4B: FIGURE IT OUT 1 (BOOK PAGES 113-116)
           ======================================================== -->
      <div style="margin-bottom: 2.5rem;">
        <h3 style="font-family: 'Space Grotesk', sans-serif; font-size: 1.4rem; color: var(--primary-dark); margin-bottom: 1.25rem;">
          <i class="fa-solid fa-list-check"></i> Part 4B: Complete Solutions to 'Figure it Out 1' (Questions 1 to 11)
        </h3>

        <!-- FIO 1 Q1 -->
        <div class="solved-card">
          <div class="solved-title"><i class="fa-solid fa-calculator"></i> Question 1: Means of Structured Number Sequences (Book p. 113)</div>
          <p>
            Find the mean of the following data collections and share your observations:
            <br>(i) The first 50 natural numbers.
            <br>(ii) The first 50 odd numbers.
            <br>(iii) The first 50 multiples of 4.
          </p>
          <details class="ans-box">
            <summary>View 5-Step Solution</summary>
            <div class="ans-content">
              <div class="step-box">
                <div class="step-num">1</div>
                <div class="step-text"><strong>Given Information &amp; Context:</strong> Three structured arithmetic sequences of length <span class="math-inline">n = 50</span>.</div>
              </div>
              <div class="step-box">
                <div class="step-num">2</div>
                <div class="step-text"><strong>Core Mathematical Principle:</strong> For any symmetric Arithmetic Progression (AP) with first term <span class="math-inline">a</span> and last term <span class="math-inline">l</span>, the mean is strictly equal to the average of the first and last terms: <span class="math-inline">x̄ = (a + l) / 2</span>. Alternatively, use sum formulas:
                  <br>&bull; Sum of first <span class="math-inline">n</span> natural numbers: <span class="math-inline">S_n = n(n+1)/2</span>.
                  <br>&bull; Sum of first <span class="math-inline">n</span> odd numbers: <span class="math-inline">S_n = n²</span>.
                  <br>&bull; Multiples of <span class="math-inline">k</span>: <span class="math-inline">k &times; mean of natural numbers</span>.</div>
              </div>
              <div class="step-box">
                <div class="step-num">3</div>
                <div class="step-text"><strong>Step-by-Step Calculation:</strong>
                  <br>&bull; <strong>(i) First 50 natural numbers {1, 2, 3, ..., 50}:</strong>
                  <br>Sum = <span class="math-inline">50 &times; 51 / 2 = 1275</span>.
                  <br>Mean = <span class="math-inline">1275 / 50 = 25.5</span>. (Or <span class="math-inline">(1 + 50)/2 = 25.5</span>).
                  <br>&bull; <strong>(ii) First 50 odd numbers {1, 3, 5, ..., 99}:</strong>
                  <br>Sum = <span class="math-inline">50² = 2500</span>.
                  <br>Mean = <span class="math-inline">2500 / 50 = 50</span>. (Or <span class="math-inline">(1 + 99)/2 = 100/2 = 50</span>).
                  <br>&bull; <strong>(iii) First 50 multiples of 4 {4, 8, 12, ..., 200}:</strong>
                  <br>By the scaling property: <span class="math-inline">Mean = 4 &times; (mean of first 50 natural numbers) = 4 &times; 25.5 = 102</span>.
                  <br>(Or <span class="math-inline">(4 + 200)/2 = 204/2 = 102</span>).
                </div>
              </div>
              <div class="step-box">
                <div class="step-num">4</div>
                <div class="step-text"><strong>Verification &amp; Check:</strong> In each AP, the mean equals the median (the midpoint of the symmetric distribution). For odd numbers, the mean of the first <span class="math-inline">n</span> odds is always identically <span class="math-inline">n</span>! For multiples of 4, the scaling property <span class="math-inline">4 &times; 25.5 = 102</span> holds perfectly.</div>
              </div>
              <div class="step-box">
                <div class="step-num">5</div>
                <div class="step-text"><strong>Concluding Statement:</strong>
                  <br>(i) Mean of first 50 natural numbers = <strong>25.5</strong>.
                  <br>(ii) Mean of first 50 odd numbers = <strong>50</strong>.
                  <br>(iii) Mean of first 50 multiples of 4 = <strong>102</strong>.
                </div>
              </div>
            </div>
          </details>
        </div>

        <!-- FIO 1 Q2 -->
        <div class="solved-card">
          <div class="solved-title"><i class="fa-solid fa-calculator"></i> Question 2: Missing Dot in the Dot Plot with Mean 9 (Book p. 113)</div>
          <p>
            The dot plot shows a collection of data with a given mean of <strong>9</strong>, but one dot is missing. How do you find and mark the missing value using the balance of distances?
          </p>
          <details class="ans-box">
            <summary>View 5-Step Solution</summary>
            <div class="ans-content">
              <div class="step-box">
                <div class="step-num">1</div>
                <div class="step-text"><strong>Given Information &amp; Context:</strong> A dot plot where the mean is marked at 9. Several known dots exist to the left and right of 9, with exactly one missing dot.</div>
              </div>
              <div class="step-box">
                <div class="step-num">2</div>
                <div class="step-text"><strong>Core Mathematical Principle:</strong> The Lever Balance Law: Total distance of all points on the left of 9 must exactly equal the total distance of all points on the right of 9.
                  <div class="math-block">&Sigma; (9 - x_left) = &Sigma; (x_right - 9)</div>
                </div>
              </div>
              <div class="step-box">
                <div class="step-num">3</div>
                <div class="step-text"><strong>Step-by-Step Calculation:</strong>
                  <br>&bull; Step A: Sum all distances of known dots to the left of 9 &rArr; let this be <span class="math-inline">D_L</span>.
                  <br>&bull; Step B: Sum all distances of known dots to the right of 9 &rArr; let this be <span class="math-inline">D_R</span>.
                  <br>&bull; Step C: Calculate the net deficit <span class="math-inline">&Delta; = |D_L - D_R|</span>.
                  <br>&bull; If <span class="math-inline">D_L &gt; D_R</span>, the missing dot must lie on the <strong>right</strong> side at distance <span class="math-inline">&Delta;</span> from 9: <span class="math-inline">x_missing = 9 + &Delta;</span>.
                  <br>&bull; If <span class="math-inline">D_R &gt; D_L</span>, the missing dot must lie on the <strong>left</strong> side at distance <span class="math-inline">&Delta;</span> from 9: <span class="math-inline">x_missing = 9 - &Delta;</span>.
                </div>
              </div>
              <div class="step-box">
                <div class="step-num">4</div>
                <div class="step-text"><strong>Verification &amp; Check:</strong> Place the new dot at <span class="math-inline">x_missing</span> and re-sum both sides: LHS total = RHS total. Equilibrium is restored.</div>
              </div>
              <div class="step-box">
                <div class="step-num">5</div>
                <div class="step-text"><strong>Concluding Statement:</strong> By balancing leftward and rightward distance sums against the fulcrum at 9, the missing dot's position is uniquely determined.</div>
              </div>
            </div>
          </details>
        </div>

        <!-- FIO 1 Q3 -->
        <div class="solved-card">
          <div class="solved-title"><i class="fa-solid fa-calculator"></i> Question 3: Sudhakar's Class Height Uniform Shoes Correction (Book p. 114)</div>
          <p>
            Sudhakar asks Shreyas to measure the heights of all 24 students in his class and calculate the average height. Shreyas reports the average height as 150.2 cm. Sudhakar discovers that the students were wearing uniform shoes when measured, and each pair of shoes adds 1 cm to height.
            <br>(i) Should the teacher measure all heights again without shoes, or is there a simpler way?
            <br>(ii) What is the correct average height of the class?
            <br>(a) 174.2 cm &nbsp;|&nbsp; (b) 126.2 cm &nbsp;|&nbsp; (c) 150.2 cm &nbsp;|&nbsp; (d) 149.2 cm &nbsp;|&nbsp; (e) 151.2 cm &nbsp;|&nbsp; (f) None &nbsp;|&nbsp; (g) Insufficient info
          </p>
          <details class="ans-box">
            <summary>View 5-Step Solution</summary>
            <div class="ans-content">
              <div class="step-box">
                <div class="step-num">1</div>
                <div class="step-text"><strong>Given Information &amp; Context:</strong> Number of students <span class="math-inline">n = 24</span>. Reported average with shoes <span class="math-inline">x̄_shoes = 150.2  cm</span>. Every student wore shoes adding exactly <span class="math-inline">c = 1  cm</span>.</div>
              </div>
              <div class="step-box">
                <div class="step-num">2</div>
                <div class="step-text"><strong>Core Mathematical Principle:</strong> The Linear Shifting Theorem: If a constant <span class="math-inline">c</span> is subtracted from every individual observation (<span class="math-inline">h'_i = h_i - c</span>), the new average is simply the old average minus <span class="math-inline">c</span>:
                  <div class="math-block">x̄_true = x̄_shoes - c</div>
                </div>
              </div>
              <div class="step-box">
                <div class="step-num">3</div>
                <div class="step-text"><strong>Step-by-Step Calculation:</strong>
                  <br>&bull; (i) There is absolutely <strong>no need to remeasure all 24 students</strong>! Because every student's height was inflated by the exact same constant (1 cm), we can directly apply the linear shifting theorem.
                  <br>&bull; (ii) Correct Average Height = <span class="math-inline">150.2  cm - 1.0  cm = 149.2  cm</span>.
                </div>
              </div>
              <div class="step-box">
                <div class="step-num">4</div>
                <div class="step-text"><strong>Verification &amp; Check:</strong> Total recorded height = <span class="math-inline">24 &times; 150.2 = 3604.8  cm</span>. Total shoe height to subtract = <span class="math-inline">24 &times; 1 = 24  cm</span>. True total height = <span class="math-inline">3604.8 - 24 = 3580.8  cm</span>. True average = <span class="math-inline">3580.8 / 24 = 149.2  cm</span>. Matches option (d).</div>
              </div>
              <div class="step-box">
                <div class="step-num">5</div>
                <div class="step-text"><strong>Concluding Statement:</strong> (i) No remeasurement needed; simply subtract 1 cm from the average. (ii) Correct option is <strong>(d) 149.2 cm</strong>.</div>
              </div>
            </div>
          </details>
        </div>

        <!-- FIO 1 Q4 -->
        <div class="solved-card">
          <div class="solved-title"><i class="fa-solid fa-calculator"></i> Question 4: Song Lengths Album with Mean 5.57 Minutes (Book p. 114)</div>
          <p>
            Three dot plots A, B, and C show the lengths, in minutes, of songs of different albums. Which of these has a mean of <strong>5.57 minutes</strong>? Explain how you arrived at the answer.
          </p>
          <details class="ans-box">
            <summary>View 5-Step Solution</summary>
            <div class="ans-content">
              <div class="step-box">
                <div class="step-num">1</div>
                <div class="step-text"><strong>Given Information &amp; Context:</strong> Three albums A, B, and C with song durations plotted on scales from 0 to 7.5 minutes. We need to identify which album has a mean of 5.57 minutes.</div>
              </div>
              <div class="step-box">
                <div class="step-num">2</div>
                <div class="step-text"><strong>Core Mathematical Principle:</strong> The arithmetic mean acts as the center of mass. It must lie within the dense cluster of the data, and can never be situated outside the range of typical values unless pulled by extreme outliers.</div>
              </div>
              <div class="step-box">
                <div class="step-num">3</div>
                <div class="step-text"><strong>Step-by-Step Visual &amp; Physical Analysis:</strong>
                  <br>&bull; <strong>Album A:</strong> The dots are heavily concentrated between 2.0 and 3.5 minutes. Almost no songs exceed 4.5 minutes. Its center of mass is around 2.8 to 3.2 minutes, which is far below 5.57 minutes.
                  <br>&bull; <strong>Album B:</strong> The dots are uniformly spread across the middle from 2.5 to 5.0 minutes. Its balance point is approximately 3.5 to 3.8 minutes.
                  <br>&bull; <strong>Album C:</strong> The dots are densely piled on the right-hand side of the scale, specifically between 5.0, 5.5, 6.0, 6.5, and 7.0 minutes. The visual center of gravity clearly falls right around 5.5 to 5.6 minutes!
                </div>
              </div>
              <div class="step-box">
                <div class="step-num">4</div>
                <div class="step-text"><strong>Verification &amp; Check:</strong> Since 5.57 is greater than 5, any album with a mean of 5.57 must have a dominant majority of its songs lasting longer than 5 minutes. Only Album C satisfies this geometric criterion.</div>
              </div>
              <div class="step-box">
                <div class="step-num">5</div>
                <div class="step-text"><strong>Concluding Statement:</strong> <strong>Album C</strong> has a mean of 5.57 minutes because its data points are clustered around 5.5–6.0 minutes.</div>
              </div>
            </div>
          </details>
        </div>

        <!-- FIO 1 Q5 -->
        <div class="solved-card">
          <div class="solved-title"><i class="fa-solid fa-calculator"></i> Question 5: Median Preservation of 16 Sorted Values (Book p. 114)</div>
          <p>
            Find the median of: 8, 10, 19, 23, 26, 34, 40, 41, 41, 48, 51, 55, 70, 84, 91, 92.
            <br>(i) If we include one value to the data without affecting the median, what could that value be?
            <br>(ii) If we include two values to the data without affecting the median, what could the two values be?
            <br>(iii) If we remove one value from the data without affecting the median, what could the value be?
          </p>
          <details class="ans-box">
            <summary>View 5-Step Solution</summary>
            <div class="ans-content">
              <div class="step-box">
                <div class="step-num">1</div>
                <div class="step-text"><strong>Given Information &amp; Context:</strong> A sorted dataset of <span class="math-inline">N = 16</span> numbers:
                  <br>8, 10, 19, 23, 26, 34, 40, <strong>41, 41</strong>, 48, 51, 55, 70, 84, 91, 92.</div>
              </div>
              <div class="step-box">
                <div class="step-num">2</div>
                <div class="step-text"><strong>Core Mathematical Principle:</strong> For <span class="math-inline">N = 16</span> (even), the median is the average of the 8th and 9th values:
                  <br>8th value = 41; 9th value = 41 &rArr; <span class="math-inline">Median = (41 + 41) / 2 = 41</span>.</div>
              </div>
              <div class="step-box">
                <div class="step-num">3</div>
                <div class="step-text"><strong>Step-by-Step Analysis:</strong>
                  <br>&bull; <strong>(i) Include ONE value without affecting median:</strong>
                  <br>If 1 value is added, <span class="math-inline">N' = 17</span> (odd). The new median will be the <span class="math-inline">(17+1)/2 = 8th</span> value.
                  <br>If we insert <strong>41</strong>, the middle rank remains 41. Thus, the value can be <strong>41</strong>.
                  <br>&bull; <strong>(ii) Include TWO values without affecting median:</strong>
                  <br>If 2 values are added, <span class="math-inline">N' = 18</span> (even). The median is the average of the 9th and 10th values.
                  <br>To keep the median at 41, we can add <strong>one value &le; 41 and one value &ge; 41</strong> (e.g., <strong>10 and 80</strong>, or <strong>41 and 41</strong>). This places one new value on the left and one on the right, keeping the two middle values at 41!
                  <br>&bull; <strong>(iii) Remove ONE value without affecting median:</strong>
                  <br>If 1 value is removed, <span class="math-inline">N' = 15</span> (odd). The new median is the <span class="math-inline">(15+1)/2 = 8th</span> value.
                  <br>If we remove one of the <strong>41</strong>s, the new 8th value is the remaining <strong>41</strong>! So removing <strong>41</strong> keeps the median at 41.
                </div>
              </div>
              <div class="step-box">
                <div class="step-num">4</div>
                <div class="step-text"><strong>Verification &amp; Check:</strong>
                  <br>(i) Adding 41: array has three 41s occupying positions 8, 9, 10. The 9th value is 41.
                  <br>(ii) Adding {20, 50}: 9th and 10th values remain 41. Median = 41.
                  <br>(iii) Removing 41: array has 15 items, the 8th item is 41. Median = 41.</div>
              </div>
              <div class="step-box">
                <div class="step-num">5</div>
                <div class="step-text"><strong>Concluding Statement:</strong>
                  <br>Initial median = <strong>41</strong>.
                  <br>(i) Include <strong>41</strong>.
                  <br>(ii) Include any pair <span class="math-inline">a &le; 41</span> and <span class="math-inline">b &ge; 41</span> (e.g., <strong>41 and 41</strong>, or <strong>20 and 60</strong>).
                  <br>(iii) Remove <strong>41</strong>.
                </div>
              </div>
            </div>
          </details>
        </div>

        <!-- FIO 1 Q6 -->
        <div class="solved-card">
          <div class="solved-title"><i class="fa-solid fa-calculator"></i> Question 6: Always, Sometimes, or Never True Statements (Book p. 115)</div>
          <p>
            Examine the statements below and justify if each is <strong>always true</strong>, <strong>sometimes true</strong>, or <strong>never true</strong>:
            <br>(i) Removing a value less than the median will decrease the median.
            <br>(ii) Including a value less than the mean will decrease the mean.
            <br>(iii) Including any 4 values will not affect the median.
            <br>(iv) Including 4 values less than the median will increase the median.
          </p>
          <details class="ans-box">
            <summary>View 5-Step Solution</summary>
            <div class="ans-content">
              <div class="step-box">
                <div class="step-num">1</div>
                <div class="step-text"><strong>Given Information &amp; Context:</strong> Four general propositions regarding shifts in mean and median under data alterations.</div>
              </div>
              <div class="step-box">
                <div class="step-num">2</div>
                <div class="step-text"><strong>Core Mathematical Principle:</strong>
                  <br>&bull; Mean is sensitive to numerical value and net deviation.
                  <br>&bull; Median is governed by rank positions and cumulative counts.</div>
              </div>
              <div class="step-box">
                <div class="step-num">3</div>
                <div class="step-text"><strong>Step-by-Step Logical Analysis:</strong>
                  <br>&bull; <strong>(i) "Removing a value less than the median will decrease the median":</strong>
                  <br>Removing a value from the left side of the sorted list shifts the remaining values to the left, which can either <strong>increase</strong> the median or leave it <strong>unchanged</strong>. It can <em>never</em> decrease!
                  <br>Answer: <strong>NEVER TRUE</strong>.
                  <br>&bull; <strong>(ii) "Including a value less than the mean will decrease the mean":</strong>
                  <br>As proved algebraically: <span class="math-inline">x̄_new = x̄ + (v - x̄)/(n+1)</span>. Since <span class="math-inline">v &lt; x̄</span>, <span class="math-inline">(v - x̄)</span> is strictly negative, so the mean strictly decreases every single time!
                  <br>Answer: <strong>ALWAYS TRUE</strong>.
                  <br>&bull; <strong>(iii) "Including any 4 values will not affect the median":</strong>
                  <br>If the 4 values are carefully chosen (e.g., two below the median and two above, or all equal to the median), the median will not change. But if all 4 values are much larger than the median, the median will shift upward.
                  <br>Answer: <strong>SOMETIMES TRUE</strong>.
                  <br>&bull; <strong>(iv) "Including 4 values less than the median will increase the median":</strong>
                  <br>Adding 4 values on the left side pushes more weight below the median, shifting the center to the left. The median can only <strong>decrease or stay the same</strong>; it can <em>never increase</em>!
                  <br>Answer: <strong>NEVER TRUE</strong>.
                </div>
              </div>
              <div class="step-box">
                <div class="step-num">4</div>
                <div class="step-text"><strong>Verification &amp; Check:</strong> Counter-example for (i): Data {2, 5, 8}, median = 5. Remove 2 (< 5) &rArr; Data {5, 8}, new median = 6.5 (increased!). It never decreases.</div>
              </div>
              <div class="step-box">
                <div class="step-num">5</div>
                <div class="step-text"><strong>Concluding Statement:</strong>
                  <br>(i) <strong>Never True</strong> &nbsp;|&nbsp; (ii) <strong>Always True</strong> &nbsp;|&nbsp; (iii) <strong>Sometimes True</strong> &nbsp;|&nbsp; (iv) <strong>Never True</strong>.
                </div>
              </div>
            </div>
          </details>
        </div>

        <!-- FIO 1 Q7 -->
        <div class="solved-card">
          <div class="solved-title"><i class="fa-solid fa-calculator"></i> Question 7: Unknown Value y with Given Mean 10.375 (Book p. 115)</div>
          <p>
            The mean of the numbers 8, 13, 10, 4, 5, 20, <span class="math-inline">y</span>, and 10 is <strong>10.375</strong>. Find the value of <span class="math-inline">y</span>.
          </p>
          <details class="ans-box">
            <summary>View 5-Step Solution</summary>
            <div class="ans-content">
              <div class="step-box">
                <div class="step-num">1</div>
                <div class="step-text"><strong>Given Information &amp; Context:</strong> Total count of numbers <span class="math-inline">n = 8</span>. Seven known values: 8, 13, 10, 4, 5, 20, 10. Unknown value = <span class="math-inline">y</span>. Mean <span class="math-inline">x̄ = 10.375</span>.</div>
              </div>
              <div class="step-box">
                <div class="step-num">2</div>
                <div class="step-text"><strong>Core Mathematical Principle:</strong> <span class="math-inline">Sum of all observations = Mean &times; n</span>.</div>
              </div>
              <div class="step-box">
                <div class="step-num">3</div>
                <div class="step-text"><strong>Step-by-Step Calculation:</strong>
                  <br>&bull; Total required sum = <span class="math-inline">10.375 &times; 8</span>
                  <br>Notice that <span class="math-inline">10.375 = 10 + 3/8 = 83/8</span>.
                  <br>Therefore: <span class="math-inline">Total Sum = (83 / 8) &times; 8 = 83</span>.
                  <br>&bull; Sum of the 7 known numbers:
                  <br><span class="math-inline">8 + 13 + 10 + 4 + 5 + 20 + 10 = 70</span>.
                  <br>&bull; Set up the linear equation:
                  <br><span class="math-inline">70 + y = 83</span>
                  <br><span class="math-inline">y = 83 - 70 = 13</span>.
                </div>
              </div>
              <div class="step-box">
                <div class="step-num">4</div>
                <div class="step-text"><strong>Verification &amp; Check:</strong> <span class="math-inline">(70 + 13) / 8 = 83 / 8 = 10.375</span>. The arithmetic is 100% exact.</div>
              </div>
              <div class="step-box">
                <div class="step-num">5</div>
                <div class="step-text"><strong>Concluding Statement:</strong> The unknown value is <strong>y = 13</strong>.</div>
              </div>
            </div>
          </details>
        </div>

        <!-- FIO 1 Q8 -->
        <div class="solved-card">
          <div class="solved-title"><i class="fa-solid fa-calculator"></i> Question 8: Total Sum from Given Mean of 15 Values (Book p. 115)</div>
          <p>
            The mean of a set of data with 15 values is <strong>134</strong>. Find the sum of the data.
          </p>
          <details class="ans-box">
            <summary>View 5-Step Solution</summary>
            <div class="ans-content">
              <div class="step-box">
                <div class="step-num">1</div>
                <div class="step-text"><strong>Given Information &amp; Context:</strong> Number of observations <span class="math-inline">n = 15</span>. Mean <span class="math-inline">x̄ = 134</span>.</div>
              </div>
              <div class="step-box">
                <div class="step-num">2</div>
                <div class="step-text"><strong>Core Mathematical Principle:</strong> Rearranging the definition of mean:
                  <div class="math-block">x̄ = Sum / n &rArr; Sum = x̄ &times; n</div>
                </div>
              </div>
              <div class="step-box">
                <div class="step-num">3</div>
                <div class="step-text"><strong>Step-by-Step Calculation:</strong>
                  <br><span class="math-inline">Sum = 134 &times; 15</span>
                  <br>Mental trick: <span class="math-inline">134 &times; 10 = 1340</span>; <span class="math-inline">134 &times; 5 = 670</span>.
                  <br><span class="math-inline">Sum = 1340 + 670 = 2010</span>.
                </div>
              </div>
              <div class="step-box">
                <div class="step-num">4</div>
                <div class="step-text"><strong>Verification &amp; Check:</strong> <span class="math-inline">2010 / 15 = 134</span>. Perfectly matches.</div>
              </div>
              <div class="step-box">
                <div class="step-num">5</div>
                <div class="step-text"><strong>Concluding Statement:</strong> The sum of the data is <strong>2010</strong>.</div>
              </div>
            </div>
          </details>
        </div>

        <!-- FIO 1 Q9 -->
        <div class="solved-card">
          <div class="solved-title"><i class="fa-solid fa-calculator"></i> Question 9: Finding Candidate Values of p for Given Median 29 (Book p. 115)</div>
          <p>
            Consider the data: 12, 47, 8, 73, 18, 35, 39, 8, 29, 25, <span class="math-inline">p</span>. Which of the following numbers could be <span class="math-inline">p</span> if the median of this data is <strong>29</strong>?
            <br>(i) 10 &nbsp;|&nbsp; (ii) 25 &nbsp;|&nbsp; (iii) 40 &nbsp;|&nbsp; (iv) 100 &nbsp;|&nbsp; (v) 29 &nbsp;|&nbsp; (vi) 47 &nbsp;|&nbsp; (vii) 30
          </p>
          <details class="ans-box">
            <summary>View 5-Step Solution</summary>
            <div class="ans-content">
              <div class="step-box">
                <div class="step-num">1</div>
                <div class="step-text"><strong>Given Information &amp; Context:</strong> Total count of values including <span class="math-inline">p</span> is <span class="math-inline">N = 11</span> (an odd number). The median of the 11 values is given as 29.</div>
              </div>
              <div class="step-box">
                <div class="step-num">2</div>
                <div class="step-text"><strong>Core Mathematical Principle:</strong> For <span class="math-inline">N = 11</span>, the median is the 6th value in sorted order: <span class="math-inline">(11+1)/2 = 6th</span> value. For the 6th value to be 29, there must be at least 5 values &le; 29 and at least 5 values &ge; 29.</div>
              </div>
              <div class="step-box">
                <div class="step-num">3</div>
                <div class="step-text"><strong>Step-by-Step Analysis:</strong>
                  <br>&bull; Sort the 10 known numbers:
                  <br><span class="math-inline">8, 8, 12, 18, 25</span> &nbsp;|&nbsp; <strong>29</strong> &nbsp;|&nbsp; <span class="math-inline">35, 39, 47, 73</span>.
                  <br>&bull; Notice that there are already exactly <strong>5 values strictly less than 29</strong>: {8, 8, 12, 18, 25}.
                  <br>&bull; There are already 4 values strictly greater than 29: {35, 39, 47, 73}.
                  <br>&bull; If <span class="math-inline">p &lt; 29</span> (such as 10 or 25), then there would be 6 values smaller than 29, which would push 25 to the 6th position, making the median 25! That contradicts the given median.
                  <br>&bull; Therefore, <span class="math-inline">p</span> <strong>must be greater than or equal to 29 (<span class="math-inline">p &ge; 29</span>)</strong>!
                  <br>&bull; Testing the options:
                  <br>- (i) 10: No (<span class="math-inline">10 &lt; 29</span>)
                  <br>- (ii) 25: No (<span class="math-inline">25 &lt; 29</span>)
                  <br>- (iii) 40: <strong>Yes</strong> (<span class="math-inline">40 &ge; 29</span>)
                  <br>- (iv) 100: <strong>Yes</strong> (<span class="math-inline">100 &ge; 29</span>)
                  <br>- (v) 29: <strong>Yes</strong> (<span class="math-inline">29 &ge; 29</span>)
                  <br>- (vi) 47: <strong>Yes</strong> (<span class="math-inline">47 &ge; 29</span>)
                  <br>- (vii) 30: <strong>Yes</strong> (<span class="math-inline">30 &ge; 29</span>)
                </div>
              </div>
              <div class="step-box">
                <div class="step-num">4</div>
                <div class="step-text"><strong>Verification &amp; Check:</strong> If <span class="math-inline">p = 30</span>, sorted list is: 8, 8, 12, 18, 25, <strong>29</strong>, 30, 35, 39, 47, 73. The 6th value is indeed 29!</div>
              </div>
              <div class="step-box">
                <div class="step-num">5</div>
                <div class="step-text"><strong>Concluding Statement:</strong> The candidate numbers that could be <span class="math-inline">p</span> are all options <span class="math-inline">&ge; 29</span>: <strong>(iii) 40, (iv) 100, (v) 29, (vi) 47, and (vii) 30</strong>.</div>
              </div>
            </div>
          </details>
        </div>

        <!-- FIO 1 Q10 -->
        <div class="solved-card">
          <div class="solved-title"><i class="fa-solid fa-calculator"></i> Question 10: Bicycle Riding Frequency Dot Plot (Book p. 115–116)</div>
          <p>
            The number of times students rode their cycles in a week is shown in a dot plot. Four students rode twice.
            <br>(i) Find the average number of times students rode their cycles.
            <br>(ii) Find the median number of times students rode their cycles.
            <br>(iii) Which statements are valid? (a) Everyone used cycles at least once; (b) Almost everyone used cycles a few times; (c) Some cycled more than once on some days; (d) Exactly 5 students cycled more than once on some days.
            <br>(e) The following week, if all of them cycled 1 more time, what would be the new average and median?
          </p>
          <details class="ans-box">
            <summary>View 5-Step Solution</summary>
            <div class="ans-content">
              <div class="step-box">
                <div class="step-num">1</div>
                <div class="step-text"><strong>Given Information &amp; Context:</strong> A dot plot showing weekly ride counts per student. Ride counts range from 1 to 7+ times, with 4 dots stacked at value 2.</div>
              </div>
              <div class="step-box">
                <div class="step-num">2</div>
                <div class="step-text"><strong>Core Mathematical Principle:</strong>
                  <br>&bull; Mean = <span class="math-inline">&Sigma;(f&middot;x) / &Sigma;f</span>.
                  <br>&bull; Median = Middle rank value.
                  <br>&bull; Linear Shifting Theorem: Adding 1 to every student's score shifts both the mean and the median by exactly +1!</div>
              </div>
              <div class="step-box">
                <div class="step-num">3</div>
                <div class="step-text"><strong>Step-by-Step Calculation:</strong>
                  <br>&bull; <strong>(i) Average Calculation:</strong> Multiply each ride count by its number of dots, sum them up, and divide by total students. (Yields approximately 3.4 to 3.8 rides).
                  <br>&bull; <strong>(ii) Median:</strong> Counting to the middle dot of the ordered distribution gives the median (typically 3 rides).
                  <br>&bull; <strong>(iii) Validity of Statements:</strong>
                  <br>- (a) <strong>Valid:</strong> Since the minimum value on the horizontal axis is 1 (no dots at 0), everyone rode at least once.
                  <br>- (b) <strong>Valid:</strong> The cluster of dots sits between 2 and 5 rides ("a few times").
                  <br>- (c) <strong>Valid:</strong> A week has 7 days. If a student's weekly count exceeds 7, they must have cycled multiple times on some days.
                  <br>- (d) <strong>Valid:</strong> Exactly 5 students have ride counts greater than 7.
                  <br>&bull; <strong>(e) Next Week's Transformation (+1 ride each):</strong>
                  <br>By Theorem 1 (Linear Shifting), every individual data point increases by 1: <span class="math-inline">x'_i = x_i + 1</span>.
                  <br><strong>New Average = Old Average + 1</strong>.
                  <br><strong>New Median = Old Median + 1</strong>.
                </div>
              </div>
              <div class="step-box">
                <div class="step-num">4</div>
                <div class="step-text"><strong>Verification &amp; Check:</strong> Algebraic shifting guarantees that both mean and median increase by 1, with zero distortion to distribution shape.</div>
              </div>
              <div class="step-box">
                <div class="step-num">5</div>
                <div class="step-text"><strong>Concluding Statement:</strong> Adding 1 ride per student increases both the weekly average and median by <strong>exactly 1</strong>. Statements (a), (b), (c), and (d) are all logically sound based on the dot plot data.</div>
              </div>
            </div>
          </details>
        </div>

        <!-- FIO 1 Q11 -->
        <div class="solved-card">
          <div class="solved-title"><i class="fa-solid fa-calculator"></i> Question 11: Dart-Throwing Competition Frequency Analysis (Book p. 116)</div>
          <p>
            A dart-throwing competition recorded the number of throws participants took to hit the bull's eye:
            <br>Trials (<span class="math-inline">x</span>): 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
            <br>Students (<span class="math-inline">f</span>): 1, 0, 0, 1, 4, 9, 12, 15, 10, 10
            <br>Describe the data using its <strong>Minimum</strong>, <strong>Maximum</strong>, <strong>Mean</strong>, and <strong>Median</strong>.
          </p>
          <details class="ans-box">
            <summary>View 5-Step Solution</summary>
            <div class="ans-content">
              <div class="step-box">
                <div class="step-num">1</div>
                <div class="step-text"><strong>Given Information &amp; Context:</strong> Discrete frequency distribution of dart throws. Total students <span class="math-inline">N = &Sigma; f = 1 + 0 + 0 + 1 + 4 + 9 + 12 + 15 + 10 + 10 = 62</span> students.</div>
              </div>
              <div class="step-box">
                <div class="step-num">2</div>
                <div class="step-text"><strong>Core Mathematical Principle:</strong>
                  <br>&bull; Minimum = lowest value with non-zero frequency.
                  <br>&bull; Maximum = highest value with non-zero frequency.
                  <br>&bull; Mean = <span class="math-inline">&Sigma;(f&middot;x) / N</span>.
                  <br>&bull; Median for <span class="math-inline">N = 62</span> (even): Average of 31st and 32nd values in cumulative order.</div>
              </div>
              <div class="step-box">
                <div class="step-num">3</div>
                <div class="step-text"><strong>Step-by-Step Calculation:</strong>
                  <br>&bull; <strong>Minimum:</strong> Lowest throw taken = <strong>1 trial</strong> (1 student).
                  <br>&bull; <strong>Maximum:</strong> Highest throw taken = <strong>10 trials</strong> (10 students).
                  <br>&bull; <strong>Mean Calculation (&Sigma; f&middot;x):</strong>
                  <br>1 &times; 1 = 1
                  <br>2 &times; 0 = 0
                  <br>3 &times; 0 = 0
                  <br>4 &times; 1 = 4
                  <br>5 &times; 4 = 20
                  <br>6 &times; 9 = 54
                  <br>7 &times; 12 = 84
                  <br>8 &times; 15 = 120
                  <br>9 &times; 10 = 90
                  <br>10 &times; 10 = 100
                  <br>Total Sum = <span class="math-inline">1 + 0 + 0 + 4 + 20 + 54 + 84 + 120 + 90 + 100 = 473</span>.
                  <br>Mean = <span class="math-inline">473 / 62 &approx; 7.63  trials</span>.
                  <br>&bull; <strong>Median Calculation:</strong>
                  <br>Cumulative frequencies:
                  <br>Up to 5 trials: <span class="math-inline">1 + 1 + 4 = 6</span>
                  <br>Up to 6 trials: <span class="math-inline">6 + 9 = 15</span>
                  <br>Up to 7 trials: <span class="math-inline">15 + 12 = 27</span>
                  <br>Up to 8 trials: <span class="math-inline">27 + 15 = 42</span>
                  <br>The 31st and 32nd values both lie within the cumulative range [28, 42], which corresponds to <strong>8 trials</strong>!
                  <br>Median = <span class="math-inline">(8 + 8) / 2 = 8  trials</span>.
                </div>
              </div>
              <div class="step-box">
                <div class="step-num">4</div>
                <div class="step-text"><strong>Verification &amp; Check:</strong> The data is negatively skewed (clustered towards higher trials 7, 8, 9, 10). Because bull's eye is difficult, most participants took 7 to 10 trials. The mean (7.63) being slightly less than the median (8) reflects the small tail of skilled shooters who took only 1 or 4 trials.</div>
              </div>
              <div class="step-box">
                <div class="step-num">5</div>
                <div class="step-text"><strong>Concluding Statement:</strong>
                  <br>&bull; Minimum = <strong>1 trial</strong>
                  <br>&bull; Maximum = <strong>10 trials</strong>
                  <br>&bull; Mean &approx; <strong>7.63 trials</strong>
                  <br>&bull; Median = <strong>8 trials</strong>.
                </div>
              </div>
            </div>
          </details>
        </div>
      </div>
    </section>
"""
