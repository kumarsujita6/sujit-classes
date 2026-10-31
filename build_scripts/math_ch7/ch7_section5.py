# -*- coding: utf-8 -*-
"""
Module: ch7_section5.py
Contains Section 5: Complete Exam Question Bank (Exhaustive 27 Questions):
- 5 Conceptual MCQs with interactive option buttons & trap feedback
- 5 Assertion & Reasoning questions
- 6 Short Answer Questions (2M/3M)
- 4 Long Answer Questions (5M) with point-by-point marking schemes
- 2 Competency-Based Case Studies with multi-part questions
- 5 Previous Years Questions (PYQs) & Most Probable Exam Questions
"""

def get_section5():
    return """
    <!-- ========================================== -->
    <!-- SECTION 5: COMPLETE EXAM QUESTION BANK     -->
    <!-- ========================================== -->
    <section id="section5">
      <div class="section-header">
        <div class="section-tag"><i class="fa-solid fa-award"></i> Board Examination Vault</div>
        <h2 class="section-title">Section 5: Complete Exam Question Bank</h2>
        <p class="section-desc">
          An exhaustive collection of 27 high-yield exam questions categorized by cognitive difficulty, featuring an interactive MCQ quiz engine, assertion-reasoning, structured marking schemes, case studies, and PYQs.
        </p>
      </div>

      <!-- PART 5.1: CONCEPTUAL MCQS (INTERACTIVE ENGINE) -->
      <h3 class="subheading"><i class="fa-solid fa-circle-question"></i> Part 5.1: Conceptual Multiple Choice Questions (Interactive Quiz Engine)</h3>
      <div style="display: flex; align-items: center; justify-content: space-between; background: #e0e7ff; padding: 0.75rem 1.25rem; border-radius: var(--radius-md); margin-bottom: 1.5rem;">
        <span style="font-weight: 700; color: #3730a3;"><i class="fa-solid fa-gamepad"></i> Interactive Self-Assessment Quiz</span>
        <span id="quizScoreDisplay" style="font-family: 'JetBrains Mono', monospace; font-weight: 800; color: #4338ca;">Score: 0 / 5</span>
      </div>

      <!-- MCQ 1 -->
      <div class="mcq-card" id="mcqCard1">
        <div class="mcq-question">
          <strong>Q1.</strong> Which of the following pairs of ratios does <strong>NOT</strong> form a mathematically valid proportion?
        </div>
        <div class="mcq-options">
          <button class="option-btn" onclick="checkMCQ(1, 'A', false)">
            <span>A</span> 14 : 35 and 16 : 40
          </button>
          <button class="option-btn" onclick="checkMCQ(1, 'B', false)">
            <span>B</span> 18 : 27 and 24 : 36
          </button>
          <button class="option-btn" onclick="checkMCQ(1, 'C', true)">
            <span>C</span> 15 : 25 and 18 : 28
          </button>
          <button class="option-btn" onclick="checkMCQ(1, 'D', false)">
            <span>D</span> 21 : 28 and 33 : 44
          </button>
        </div>
        <div class="mcq-feedback" id="mcqFeedback1">
          <strong>Correct Answer: C (15 : 25 and 18 : 28)</strong>
          <br><em>Pedagogical Trap Explanation:</em>
          <br>• In Option A: 14/35 = 2/5 and 16/40 = 2/5 (Proportional).
          <br>• In Option B: 18/27 = 2/3 and 24/36 = 2/3 (Proportional).
          <br>• In Option D: 21/28 = 3/4 and 33/44 = 3/4 (Proportional).
          <br>• In Option C: 15/25 = 3/5 = 0.60. But 18/28 = 9/14 ≈ 0.6428!
          <br>Notice the trap: 18 and 28 were formed by <em>adding 3</em> to 15 and 25 (15+3=18, 25+3=28). Adding a constant alters the ratio, so 15 : 25 and 18 : 28 are NOT proportional!
        </div>
      </div>

      <!-- MCQ 2 -->
      <div class="mcq-card" id="mcqCard2">
        <div class="mcq-question">
          <strong>Q2.</strong> The present ages of a mother and daughter are in the ratio 7 : 2. After 5 years, which statement about the new ratio of their ages must be <strong>TRUE</strong>?
        </div>
        <div class="mcq-options">
          <button class="option-btn" onclick="checkMCQ(2, 'A', false)">
            <span>A</span> The ratio will remain exactly 7 : 2.
          </button>
          <button class="option-btn" onclick="checkMCQ(2, 'B', false)">
            <span>B</span> The ratio will become (7 + 5) : (2 + 5) = 12 : 7.
          </button>
          <button class="option-btn" onclick="checkMCQ(2, 'C', true)">
            <span>C</span> The numerical value of the ratio will strictly decrease (become closer to 1).
          </button>
          <button class="option-btn" onclick="checkMCQ(2, 'D', false)">
            <span>D</span> The ratio will increase because both people grew older.
          </button>
        </div>
        <div class="mcq-feedback" id="mcqFeedback2">
          <strong>Correct Answer: C (The numerical value will strictly decrease towards 1)</strong>
          <br><em>Pedagogical Trap Explanation:</em>
          <br>Let mother's age be 35 and daughter's age be 10 (Ratio = 35 : 10 = 7 : 2 = 3.50).
          <br>After 5 years, mother is 40 and daughter is 15.
          <br>New ratio = 40 : 15 = 8 : 3 ≈ 2.67.
          <br>Notice that 2.67 &lt; 3.50. For any ratio <em>a/b &gt; 1</em>, adding a positive constant <em>k</em> to both terms decreases the ratio: <em>(a + k)/(b + k) &lt; a/b</em>. The gap in age remains constant, but daughter's age grows by a larger percentage!
        </div>
      </div>

      <!-- MCQ 3 -->
      <div class="mcq-card" id="mcqCard3">
        <div class="mcq-question">
          <strong>Q3.</strong> In ancient Indian Trairāśika (Rule of Three by Āryabhaṭa), if Pramāṇa = 8, Phala = 20, and Ichchhā = 18, what is the value of <strong>Ichchhāphala</strong>?
        </div>
        <div class="mcq-options">
          <button class="option-btn" onclick="checkMCQ(3, 'A', false)">
            <span>A</span> 36
          </button>
          <button class="option-btn" onclick="checkMCQ(3, 'B', true)">
            <span>B</span> 45
          </button>
          <button class="option-btn" onclick="checkMCQ(3, 'C', false)">
            <span>C</span> 40
          </button>
          <button class="option-btn" onclick="checkMCQ(3, 'D', false)">
            <span>D</span> 50
          </button>
        </div>
        <div class="mcq-feedback" id="mcqFeedback3">
          <strong>Correct Answer: B (45)</strong>
          <br><em>Pedagogical Trap Explanation:</em>
          <br>Āryabhaṭa's canonical Trairāśika formula states:
          <br><em>Ichchhāphala = (Phala × Ichchhā) ÷ Pramāṇa</em>
          <br>Substituting values:
          <br><em>Ichchhāphala = (20 × 18) ÷ 8 = 360 ÷ 8 = 45</em>.
        </div>
      </div>

      <!-- MCQ 4 -->
      <div class="mcq-card" id="mcqCard4">
        <div class="mcq-question">
          <strong>Q4.</strong> A sum of ₹7,200 is divided among three friends A, B, and C in the ratio 2 : 3 : 4. How much more money does C receive than A?
        </div>
        <div class="mcq-options">
          <button class="option-btn" onclick="checkMCQ(4, 'A', false)">
            <span>A</span> ₹800
          </button>
          <button class="option-btn" onclick="checkMCQ(4, 'B', false)">
            <span>B</span> ₹1,200
          </button>
          <button class="option-btn" onclick="checkMCQ(4, 'C', true)">
            <span>C</span> ₹1,600
          </button>
          <button class="option-btn" onclick="checkMCQ(4, 'D', false)">
            <span>D</span> ₹2,400
          </button>
        </div>
        <div class="mcq-feedback" id="mcqFeedback4">
          <strong>Correct Answer: C (₹1,600)</strong>
          <br><em>Pedagogical Trap Explanation:</em>
          <br>Total parts = 2 + 3 + 4 = 9 parts.
          <br>Value of 1 part = ₹7,200 ÷ 9 = ₹800.
          <br>Difference between C and A = 4 parts - 2 parts = 2 parts.
          <br>Difference in amount = 2 × ₹800 = <strong>₹1,600</strong>.
          <br>(Direct shortcut: do not waste time calculating B's share!).
        </div>
      </div>

      <!-- MCQ 5 -->
      <div class="mcq-card" id="mcqCard5">
        <div class="mcq-question">
          <strong>Q5.</strong> Which of the following relationships represents an <strong>INVERSE VARIATION</strong> rather than a direct proportion?
        </div>
        <div class="mcq-options">
          <button class="option-btn" onclick="checkMCQ(5, 'A', false)">
            <span>A</span> Litres of petrol filled and the total cost at the pump.
          </button>
          <button class="option-btn" onclick="checkMCQ(5, 'B', true)">
            <span>B</span> Number of workers constructing a bridge and the days required to finish.
          </button>
          <button class="option-btn" onclick="checkMCQ(5, 'C', false)">
            <span>C</span> Distance covered by a car traveling at constant speed and the time elapsed.
          </button>
          <button class="option-btn" onclick="checkMCQ(5, 'D', false)">
            <span>D</span> Weight of tomatoes purchased and total bill amount.
          </button>
        </div>
        <div class="mcq-feedback" id="mcqFeedback5">
          <strong>Correct Answer: B (Number of workers and construction days)</strong>
          <br><em>Pedagogical Trap Explanation:</em>
          <br>More workers finish the job in <em>fewer days</em>. Their product (<em>Workers × Days = Total Man-Days</em>) remains constant. This is the definition of inverse variation (<em>xy = C</em>). In all other options, increasing one variable causes a direct increase in the other.
        </div>
      </div>

      <!-- PART 5.2: ASSERTION & REASONING (5 QUESTIONS) -->
      <h3 class="subheading"><i class="fa-solid fa-scale-unbalanced-flip"></i> Part 5.2: Assertion &amp; Reasoning Questions (5 Questions)</h3>
      <p style="font-size: 0.9rem; color: #64748b; margin-bottom: 1.25rem;">
        <em>Directions:</em> In the following questions, a statement of Assertion (A) is followed by a statement of Reason (R). Choose the correct option:
        <br>(a) Both A and R are true and R is the correct explanation of A.
        <br>(b) Both A and R are true but R is NOT the correct explanation of A.
        <br>(c) A is true but R is false.
        <br>(d) A is false but R is true.
        <br>(e) Both A and R are false.
      </p>

      <!-- AR 1 -->
      <details class="ans-box">
        <summary>A&amp;R 1: Proportional Cross-Multiplication Property</summary>
        <div class="ans-content">
          <p><strong>Assertion (A):</strong> If 12 : 18 :: 20 : x, then the value of x must be 30.</p>
          <p><strong>Reason (R):</strong> In any proportion a : b :: c : d, the product of the extremes equals the product of the means (ad = bc).</p>
          <div style="background: #f0fdf4; border-left: 4px solid #16a34a; padding: 1rem; border-radius: var(--radius-sm); margin-top: 0.75rem;">
            <strong>Correct Answer: (a) Both A and R are true and R is the correct explanation of A.</strong>
            <br><em>Explanation:</em>
            <br>By Reason R, <em>12 × x = 18 × 20 ⇒ 12x = 360 ⇒ x = 360 ÷ 12 = 30</em>.
            <br>Both statements are mathematically true, and Reason R provides the exact theorem used to deduce Assertion A.
          </div>
        </div>
      </details>

      <!-- AR 2 -->
      <details class="ans-box">
        <summary>A&amp;R 2: Invariance under Addition Trap</summary>
        <div class="ans-content">
          <p><strong>Assertion (A):</strong> If the ratio of boys to girls in a hall is 3 : 2, and 5 boys and 5 girls enter the hall, the new ratio of boys to girls remains 3 : 2.</p>
          <p><strong>Reason (R):</strong> Adding the same positive quantity to both terms of a ratio preserves the ratio unchanged.</p>
          <div style="background: #fef2f2; border-left: 4px solid #dc2626; padding: 1rem; border-radius: var(--radius-sm); margin-top: 0.75rem;">
            <strong>Correct Answer: (e) Both A and R are FALSE!</strong>
            <br><em>Explanation:</em>
            <br>Suppose initially there are 15 boys and 10 girls (Ratio = 15 : 10 = 3 : 2).
            <br>When 5 boys and 5 girls enter: Boys = 20, Girls = 15.
            <br>New Ratio = 20 : 15 = 4 : 3 ≠ 3 : 2!
            <br>Adding a constant to both terms always changes the numerical ratio. Thus, both Assertion A and Reason R are fundamentally false.
          </div>
        </div>
      </details>

      <!-- AR 3 -->
      <details class="ans-box">
        <summary>A&amp;R 3: Geometric Similarity of Rectangles</summary>
        <div class="ans-content">
          <p><strong>Assertion (A):</strong> A rectangular photo of 12 cm × 8 cm is geometrically similar to a poster of 30 cm × 20 cm.</p>
          <p><strong>Reason (R):</strong> Two rectangles are geometrically similar if and only if the ratio of their corresponding lengths and widths is equal.</p>
          <div style="background: #f0fdf4; border-left: 4px solid #16a34a; padding: 1rem; border-radius: var(--radius-sm); margin-top: 0.75rem;">
            <strong>Correct Answer: (a) Both A and R are true and R is the correct explanation of A.</strong>
            <br><em>Explanation:</em>
            <br>Aspect ratio of photo = 12 : 8 = 3 : 2.
            <br>Aspect ratio of poster = 30 : 20 = 3 : 2.
            <br>Since their aspect ratios are equal (3 : 2 = 3 : 2), the rectangles are geometrically similar. Reason R correctly defines the geometric criterion.
          </div>
        </div>
      </details>

      <!-- AR 4 -->
      <details class="ans-box">
        <summary>A&amp;R 4: Unit Harmonization Requirement</summary>
        <div class="ans-content">
          <p><strong>Assertion (A):</strong> The ratio between 2.5 kg of sugar and 500 grams of salt cannot be written directly as 2.5 : 500.</p>
          <p><strong>Reason (R):</strong> A ratio is a dimensionless number comparing two quantities, and it requires both quantities to be expressed in the exact same unit before division.</p>
          <div style="background: #f0fdf4; border-left: 4px solid #16a34a; padding: 1rem; border-radius: var(--radius-sm); margin-top: 0.75rem;">
            <strong>Correct Answer: (a) Both A and R are true and R is the correct explanation of A.</strong>
            <br><em>Explanation:</em>
            <br>2.5 kg must first be converted to 2,500 grams. The true ratio is 2500 : 500 = 5 : 1. Writing 2.5 : 500 gives 1 : 200, which is wrong by a factor of 1,000! Reason R gives the fundamental physical reason.
          </div>
        </div>
      </details>

      <!-- AR 5 -->
      <details class="ans-box">
        <summary>A&amp;R 5: Travel Speed and Duration</summary>
        <div class="ans-content">
          <p><strong>Assertion (A):</strong> If a train doubles its speed from 50 km/h to 100 km/h, the time taken to travel a fixed distance of 200 km also doubles.</p>
          <p><strong>Reason (R):</strong> Speed and travel time are in direct proportion.</p>
          <div style="background: #fef2f2; border-left: 4px solid #dc2626; padding: 1rem; border-radius: var(--radius-sm); margin-top: 0.75rem;">
            <strong>Correct Answer: (e) Both A and R are FALSE!</strong>
            <br><em>Explanation:</em>
            <br>At 50 km/h, time = 200 / 50 = 4 hours.
            <br>At 100 km/h, time = 200 / 100 = 2 hours.
            <br>The time <em>halves</em>, it does not double! Speed and travel time are in <strong>inverse variation</strong>, not direct proportion. Thus both A and R are false.
          </div>
        </div>
      </details>

      <!-- PART 5.3: SHORT ANSWER QUESTIONS (2M / 3M - 6 QUESTIONS) -->
      <h3 class="subheading"><i class="fa-solid fa-pen-clip"></i> Part 5.3: Short Answer Questions (2M &amp; 3M - 6 Questions)</h3>

      <!-- SA 1 -->
      <details class="ans-box">
        <summary>SA 1 (2M): Find the value of x if 15 : x :: 45 : 84</summary>
        <div class="ans-content">
          <div class="step-container">
            <div class="step-box step-1">
              <span class="step-badge">Step 1: Given Information</span>
              <p>Proportion: <em>15 : x :: 45 : 84</em>. Extremes = 15, 84; Means = x, 45.</p>
            </div>
            <div class="step-box step-2">
              <span class="step-badge">Step 2: Cross-Multiplication Formula</span>
              <p><em>Product of Extremes = Product of Means ⇒ 15 × 84 = x × 45</em></p>
            </div>
            <div class="step-box step-3">
              <span class="step-badge">Step 3: Solving for x</span>
              <p>
                <em>x = (15 × 84) ÷ 45</em>
                <br>Simplify by dividing 15 and 45 by 15:
                <br><em>15 ÷ 15 = 1</em> and <em>45 ÷ 15 = 3</em>:
                <br><em>x = 84 ÷ 3 = <strong>28</strong></em>.
              </p>
            </div>
            <div class="step-box step-4">
              <span class="step-badge">Step 4: Verification</span>
              <p>15 : 28 = 15/28; 45 : 84 = 45/84 = 15/28 (dividing by 3) ✓.</p>
            </div>
            <div class="step-box step-5">
              <span class="step-badge">Step 5: Final Concluding Answer</span>
              <p><strong>x = 28</strong>.</p>
            </div>
          </div>
        </div>
      </details>

      <!-- SA 2 -->
      <details class="ans-box">
        <summary>SA 2 (2M): Two numbers in ratio 7 : 5 differ by 18. Find the numbers.</summary>
        <div class="ans-content">
          <div class="step-container">
            <div class="step-box step-1">
              <span class="step-badge">Step 1: Algebraic Representation</span>
              <p>Let the two numbers be <em>7k</em> and <em>5k</em>, where <em>k</em> is the common scaling factor.</p>
            </div>
            <div class="step-box step-2">
              <span class="step-badge">Step 2: Equation from Difference</span>
              <p>
                Given: <em>7k - 5k = 18</em>
                <br><em>2k = 18 ⇒ k = 18 ÷ 2 = 9</em>.
              </p>
            </div>
            <div class="step-box step-3">
              <span class="step-badge">Step 3: Calculating the Numbers</span>
              <p>
                • First number = <em>7 × 9 = <strong>63</strong></em>.
                <br>• Second number = <em>5 × 9 = <strong>45</strong></em>.
              </p>
            </div>
            <div class="step-box step-4">
              <span class="step-badge">Step 4: Verification</span>
              <p>Difference = 63 - 45 = 18 ✓. Ratio = 63 : 45 = 7 : 5 ✓.</p>
            </div>
            <div class="step-box step-5">
              <span class="step-badge">Step 5: Final Concluding Answer</span>
              <p>The two numbers are <strong>63 and 45</strong>.</p>
            </div>
          </div>
        </div>
      </details>

      <!-- SA 3 -->
      <details class="ans-box">
        <summary>SA 3 (3M): Architectural Blueprint Floor Area Calculation</summary>
        <div class="ans-content">
          <div class="step-container">
            <div class="step-box step-1">
              <span class="step-badge">Step 1: Given Blueprint Scale &amp; Dimensions</span>
              <p>
                • Blueprint scale: 1 cm = 4.5 metres.
                <br>• Room dimensions on blueprint: Length = 2.4 cm, Width = 1.8 cm.
                <br>• Goal: Find actual floor area in square metres.
              </p>
            </div>
            <div class="step-box step-2">
              <span class="step-badge">Step 2: Calculating Actual Length &amp; Width</span>
              <p>
                • Actual Length = <em>2.4 × 4.5 m = 10.8 metres</em>.
                <br>• Actual Width = <em>1.8 × 4.5 m = 8.1 metres</em>.
              </p>
            </div>
            <div class="step-box step-3">
              <span class="step-badge">Step 3: Calculating Actual Area</span>
              <p>
                Actual Area = <em>Length × Width = 10.8 m × 8.1 m = <strong>87.48 m²</strong></em>.
                <br><em>Alternative Method (Area Scale Factor):</em>
                <br>Blueprint Area = 2.4 × 1.8 = 4.32 cm².
                <br>Area Scale Factor = (4.5)² = 20.25 m²/cm².
                <br>Actual Area = 4.32 × 20.25 = <strong>87.48 m²</strong>.
              </p>
            </div>
            <div class="step-box step-4">
              <span class="step-badge">Step 4: Consistency Check</span>
              <p>Both methods yield the exact same result: 87.48 m² ✓.</p>
            </div>
            <div class="step-box step-5">
              <span class="step-badge">Step 5: Final Concluding Answer</span>
              <p>The actual floor area of the living room is <strong>87.48 square metres</strong>.</p>
            </div>
          </div>
        </div>
      </details>

      <!-- SA 4 -->
      <details class="ans-box">
        <summary>SA 4 (3M): Bronze Alloy Mass Partitioning (17 : 2 : 1)</summary>
        <div class="ans-content">
          <div class="step-container">
            <div class="step-box step-1">
              <span class="step-badge">Step 1: Given Information</span>
              <p>
                • Alloy composition: Copper : Tin : Zinc = 17 : 2 : 1.
                <br>• Total mass of casting = 40 kg.
                <br>• Goal: Find mass of copper, tin, and zinc.
              </p>
            </div>
            <div class="step-box step-2">
              <span class="step-badge">Step 2: Total Units</span>
              <p>
                Total parts = 17 + 2 + 1 = <strong>20 parts</strong>.
                <br>Mass per 1 part = <em>40 kg ÷ 20 = 2 kg</em>.
              </p>
            </div>
            <div class="step-box step-3">
              <span class="step-badge">Step 3: Calculating Individual Masses</span>
              <p>
                • Copper (17 parts) = <em>17 × 2 kg = <strong>34 kg</strong></em>.
                <br>• Tin (2 parts) = <em>2 × 2 kg = <strong>4 kg</strong></em>.
                <br>• Zinc (1 part) = <em>1 × 2 kg = <strong>2 kg</strong></em>.
              </p>
            </div>
            <div class="step-box step-4">
              <span class="step-badge">Step 4: Verification</span>
              <p>34 kg + 4 kg + 2 kg = 40 kg ✓. Ratio = 34 : 4 : 2 = 17 : 2 : 1 ✓.</p>
            </div>
            <div class="step-box step-5">
              <span class="step-badge">Step 5: Final Concluding Answer</span>
              <p>The bronze alloy contains <strong>34 kg of copper</strong>, <strong>4 kg of tin</strong>, and <strong>2 kg of zinc</strong>.</p>
            </div>
          </div>
        </div>
      </details>

      <!-- SA 5 -->
      <details class="ans-box">
        <summary>SA 5 (3M): Speed of Sound Thunder Delay Calculation</summary>
        <div class="ans-content">
          <div class="step-container">
            <div class="step-box step-1">
              <span class="step-badge">Step 1: Given Information &amp; Goal</span>
              <p>
                • Benchmark: Sound travels 1,020 metres in 3 seconds.
                <br>• Target distance: 5.1 kilometres.
                <br>• Goal: Find time taken for thunder to reach the observer.
              </p>
            </div>
            <div class="step-box step-2">
              <span class="step-badge">Step 2: Unit Harmonization</span>
              <p>5.1 km = <em>5.1 × 1,000 = <strong>5,100 metres</strong></em>.</p>
            </div>
            <div class="step-box step-3">
              <span class="step-badge">Step 3: Trairāśika Proportion Setup</span>
              <p>
                <em>Distance (m) : Time (s) :: Distance (m) : Time (s)</em>
                <br><strong>1,020 : 3 :: 5,100 : t</strong>
                <br><em>t = (5,100 × 3) ÷ 1,020 = 15,300 ÷ 1,020 = <strong>15 seconds</strong></em>.
              </p>
            </div>
            <div class="step-box step-4">
              <span class="step-badge">Step 4: Speed Verification</span>
              <p>Speed of sound = 1,020 ÷ 3 = 340 m/s. Time = 5,100 ÷ 340 = 15 seconds ✓.</p>
            </div>
            <div class="step-box step-5">
              <span class="step-badge">Step 5: Final Concluding Answer</span>
              <p>It will take <strong>15 seconds</strong> for the sound of thunder to reach the observer.</p>
            </div>
          </div>
        </div>
      </details>

      <!-- SA 6 -->
      <details class="ans-box">
        <summary>SA 6 (3M): Comparing Ratios 5 : 8 and 7 : 11 (Two Methods)</summary>
        <div class="ans-content">
          <div class="step-container">
            <div class="step-box step-1">
              <span class="step-badge">Step 1: Problem</span>
              <p>Determine which ratio is greater: <strong>5 : 8</strong> or <strong>7 : 11</strong>.</p>
            </div>
            <div class="step-box step-2">
              <span class="step-badge">Step 2: Method 1 — Common Denominator (LCM)</span>
              <p>
                Write as fractions: <em>5/8</em> and <em>7/11</em>.
                <br>LCM(8, 11) = 88.
                <br>• 5/8 = <em>(5 × 11) / (8 × 11) = <strong>55 / 88</strong></em>.
                <br>• 7/11 = <em>(7 × 8) / (11 × 8) = <strong>56 / 88</strong></em>.
                <br>Since 56 &gt; 55, it follows that <strong>7/11 &gt; 5/8</strong>.
              </p>
            </div>
            <div class="step-box step-3">
              <span class="step-badge">Step 3: Method 2 — Decimal &amp; Cross-Product Method</span>
              <p>
                • 5 ÷ 8 = <strong>0.625</strong>
                <br>• 7 ÷ 11 = <strong>0.6363...</strong>
                <br>Cross-product: 5 × 11 = 55 &nbsp;vs&nbsp; 8 × 7 = 56.
                <br>Since 56 &gt; 55, <strong>7 : 11 is strictly greater than 5 : 8</strong>.
              </p>
            </div>
            <div class="step-box step-4">
              <span class="step-badge">Step 4: Margin of Difference</span>
              <p>Difference = 56/88 - 55/88 = 1/88 ≈ 0.01136.</p>
            </div>
            <div class="step-box step-5">
              <span class="step-badge">Step 5: Final Concluding Answer</span>
              <p><strong>7 : 11 is greater than 5 : 8</strong>.</p>
            </div>
          </div>
        </div>
      </details>

      <!-- PART 5.4: LONG ANSWER QUESTIONS (5M - 4 QUESTIONS) -->
      <h3 class="subheading"><i class="fa-solid fa-file-signature"></i> Part 5.4: Long Answer Questions (5M - 4 Questions with Marking Schemes)</h3>

      <!-- LA 1 -->
      <details class="ans-box">
        <summary>LA 1 (5M): Three-Partner Business with Managing Partner Commission</summary>
        <div class="ans-content">
          <div class="step-container">
            <div class="step-box step-1">
              <span class="step-badge">Step 1: Given Information &amp; Problem Goal</span>
              <p>
                • Partners: Arun (₹1,20,000), Bina (₹1,80,000), Chitra (₹2,40,000).
                <br>• Total Annual Gross Profit = ₹1,35,000.
                <br>• Special condition: Bina receives 10% of gross profit as managing partner commission.
                <br>• The remaining profit is distributed among Arun, Bina, and Chitra in their investment ratio.
                <br>• Goal: Calculate total income received by Arun, Bina, and Chitra.
              </p>
            </div>
            <div class="step-box step-2">
              <span class="step-badge">Step 2: Commission Deduction &amp; Net Distributable Profit</span>
              <p>
                • Bina's Management Fee = <em>10% of ₹1,35,000 = 0.10 × 135000 = <strong>₹13,500</strong></em>. [Mark: 1M]
                <br>• Net Distributable Profit = <em>₹1,35,000 - ₹13,500 = <strong>₹1,21,500</strong></em>. [Mark: 1M]
              </p>
            </div>
            <div class="step-box step-3">
              <span class="step-badge">Step 3: Investment Ratio Simplification</span>
              <p>
                Ratio (Arun : Bina : Chitra) = 1,20,000 : 1,80,000 : 2,40,000.
                <br>Divide each term by 60,000:
                <br><strong>Ratio = 2 : 3 : 4</strong>. [Mark: 1M]
                <br>Total parts = 2 + 3 + 4 = 9 parts.
                <br>Value of 1 part = <em>₹1,21,500 ÷ 9 = <strong>₹13,500</strong></em>.
              </p>
            </div>
            <div class="step-box step-4">
              <span class="step-badge">Step 4: Calculating Profit Shares &amp; Total Incomes</span>
              <p>
                • <strong>Arun's Share:</strong> 2 parts × ₹13,500 = <strong>₹27,000</strong>.
                <br>• <strong>Bina's Profit Share:</strong> 3 parts × ₹13,500 = ₹40,500.
                <br>&nbsp;&nbsp;<em>Bina's Total Income</em> = Profit Share + Commission = ₹40,500 + ₹13,500 = <strong>₹54,000</strong>.
                <br>• <strong>Chitra's Share:</strong> 4 parts × ₹13,500 = <strong>₹54,000</strong>. [Mark: 1.5M]
                <br>Verification: ₹27,000 + ₹54,000 + ₹54,000 = ₹1,35,000 ✓.
              </p>
            </div>
            <div class="step-box step-5">
              <span class="step-badge">Step 5: Final Concluding Answer &amp; Step-by-Step Marking Summary</span>
              <p>
                <strong>Arun receives ₹27,000</strong>; <strong>Bina receives ₹54,000</strong>; <strong>Chitra receives ₹54,000</strong>. [Mark: 0.5M]
                <br><em>Official Marking Scheme:</em>
                <br>• Commission calculation (₹13,500): 1 Mark
                <br>• Net profit determination (₹1,21,500): 1 Mark
                <br>• Simplest investment ratio (2:3:4) &amp; unit part value: 1 Mark
                <br>• Individual profit shares calculation: 1.5 Marks
                <br>• Final total incomes with units: 0.5 Mark (Total: 5 Marks).
              </p>
            </div>
          </div>
        </div>
      </details>

      <!-- LA 2 -->
      <details class="ans-box">
        <summary>LA 2 (5M): Municipal Overhead Water Tank Filling &amp; Leakage Dynamics</summary>
        <div class="ans-content">
          <div class="step-container">
            <div class="step-box step-1">
              <span class="step-badge">Step 1: Given Information &amp; Rates</span>
              <p>
                • Tank capacity = 48,000 Litres.
                <br>• Inlet pipe inflow rate = 80 L/min.
                <br>• Bottom crack leakage rate = 16 L/min.
                <br>• Sub-questions:
                <br>&nbsp;&nbsp;(a) Find net filling rate (1M).
                <br>&nbsp;&nbsp;(b) Time to fill empty tank with leak active (2M).
                <br>&nbsp;&nbsp;(c) If leak is sealed at half-full mark (24,000 L), total time to fill tank (2M).
              </p>
            </div>
            <div class="step-box step-2">
              <span class="step-badge">Step 2: Sub-question (a) — Net Filling Rate</span>
              <p>
                Net Filling Rate = <em>Inflow Rate - Leakage Rate = 80 L/min - 16 L/min = <strong>64 L/min</strong></em>. [Mark: 1M]
              </p>
            </div>
            <div class="step-box step-3">
              <span class="step-badge">Step 3: Sub-question (b) — Time with Continuous Leak</span>
              <p>
                Time to fill 48,000 L at 64 L/min:
                <br><em>Time = 48,000 ÷ 64 = 750 minutes</em>.
                <br>In hours: <em>750 ÷ 60 = <strong>12.5 hours (12 hours 30 minutes)</strong></em>. [Mark: 2M]
              </p>
            </div>
            <div class="step-box step-4">
              <span class="step-badge">Step 4: Sub-question (c) — Two-Stage Filling Process</span>
              <p>
                • <strong>Stage 1 (0 to 24,000 L with leak):</strong>
                <br>Time = <em>24,000 ÷ 64 = 375 minutes (6 hours 15 minutes)</em>.
                <br>• <strong>Stage 2 (24,000 to 48,000 L with leak sealed):</strong>
                <br>Filling rate becomes full inlet rate = 80 L/min.
                <br>Remaining volume = 24,000 L.
                <br>Time = <em>24,000 ÷ 80 = 300 minutes (5 hours)</em>.
                <br>• <strong>Total Time:</strong>
                <br>Total = <em>375 + 300 = 675 minutes = <strong>11 hours 15 minutes</strong></em>. [Mark: 2M]
              </p>
            </div>
            <div class="step-box step-5">
              <span class="step-badge">Step 5: Final Concluding Answer</span>
              <p>
                (a) Net rate = <strong>64 L/min</strong>.
                <br>(b) Time with leak active = <strong>12 hours 30 minutes</strong>.
                <br>(c) Total time with leak sealed at half-way mark = <strong>11 hours 15 minutes</strong>.
              </p>
            </div>
          </div>
        </div>
      </details>

      <!-- LA 3 -->
      <details class="ans-box">
        <summary>LA 3 (5M): Bargarh Organic Agricultural Land Allocation &amp; Revenue</summary>
        <div class="ans-content">
          <div class="step-container">
            <div class="step-box step-1">
              <span class="step-badge">Step 1: Given Information</span>
              <p>
                • Total farm area = 5 hectares.
                <br>• Ratio (Paddy : Pulses) = 3 : 2.
                <br>• Standards: 1 ha = 10,000 m²; 1 ha = 2.471 acres.
                <br>• Paddy yield = 3.6 tonnes/ha; Paddy price = ₹22,000 per tonne.
              </p>
            </div>
            <div class="step-box step-2">
              <span class="step-badge">Step 2: Sub-question (a) — Unit Conversions</span>
              <p>
                • In square metres: <em>5 ha × 10,000 m²/ha = <strong>50,000 m²</strong></em>.
                <br>• In acres: <em>5 ha × 2.471 acres/ha = <strong>12.355 acres</strong></em>. [Mark: 1.5M]
              </p>
            </div>
            <div class="step-box step-3">
              <span class="step-badge">Step 3: Sub-question (b) — Area Partitioning</span>
              <p>
                Total parts = 3 + 2 = 5 parts.
                <br>• Paddy Area = <em>(3/5) × 5 ha = <strong>3 hectares</strong></em> (or 3 × 2.471 = <strong>7.413 acres</strong>).
                <br>• Pulses Area = <em>(2/5) × 5 ha = <strong>2 hectares</strong></em> (or 2 × 2.471 = <strong>4.942 acres</strong>). [Mark: 1.5M]
              </p>
            </div>
            <div class="step-box step-4">
              <span class="step-badge">Step 4: Sub-question (c) — Paddy Yield &amp; Revenue</span>
              <p>
                • Total Paddy Production = <em>3 ha × 3.6 tonnes/ha = <strong>10.8 tonnes</strong></em>.
                <br>• Gross Revenue = <em>10.8 tonnes × ₹22,000/tonne = <strong>₹2,37,600</strong></em>. [Mark: 1.5M]
              </p>
            </div>
            <div class="step-box step-5">
              <span class="step-badge">Step 5: Final Concluding Answer &amp; Summary</span>
              <p>
                Total farm = 50,000 m² (12.355 acres). Paddy occupies 3 ha (7.413 acres) and pulses occupy 2 ha (4.942 acres). Total gross revenue from the paddy harvest is <strong>₹2,37,600</strong>. [Mark: 0.5M]
              </p>
            </div>
          </div>
        </div>
      </details>

      <!-- LA 4 -->
      <details class="ans-box">
        <summary>LA 4 (5M): Multi-Stage Chemical Dilution and Concentration Adjustment</summary>
        <div class="ans-content">
          <div class="step-container">
            <div class="step-box step-1">
              <span class="step-badge">Step 1: Given Information</span>
              <p>
                • Total solution = 600 mL.
                <br>• Ratio (Acid : Water) = 3 : 7.
                <br>• Sub-questions:
                <br>&nbsp;&nbsp;(a) Initial volumes of acid and water (1.5M).
                <br>&nbsp;&nbsp;(b) Water added to dilute to 1 : 4 ratio (1.5M).
                <br>&nbsp;&nbsp;(c) Acid added to original mix to concentrate to 1 : 1 ratio (2M).
              </p>
            </div>
            <div class="step-box step-2">
              <span class="step-badge">Step 2: Sub-question (a) — Initial Quantities</span>
              <p>
                Total parts = 3 + 7 = 10 parts.
                <br>Volume per part = 600 mL ÷ 10 = 60 mL.
                <br>• Acid = <em>3 × 60 mL = <strong>180 mL</strong></em>.
                <br>• Water = <em>7 × 60 mL = <strong>420 mL</strong></em>. [Mark: 1.5M]
              </p>
            </div>
            <div class="step-box step-3">
              <span class="step-badge">Step 3: Sub-question (b) — Diluting to 1 : 4</span>
              <p>
                Acid remains 180 mL. New ratio Acid : Water = 1 : 4.
                <br><em>1 : 4 :: 180 : W_new</em>
                <br><em>W_new = 180 × 4 = 720 mL</em>.
                <br>Distilled water to add = <em>720 mL - 420 mL = <strong>300 mL</strong></em>. [Mark: 1.5M]
              </p>
            </div>
            <div class="step-box step-4">
              <span class="step-badge">Step 4: Sub-question (c) — Concentrating to 1 : 1</span>
              <p>
                In the original solution, water is 420 mL. To achieve 1 : 1 ratio, acid must equal water:
                <br><em>A_new : 420 :: 1 : 1 ⇒ A_new = 420 mL</em>.
                <br>Concentrated acid to add = <em>420 mL - 180 mL = <strong>240 mL</strong></em>. [Mark: 2M]
              </p>
            </div>
            <div class="step-box step-5">
              <span class="step-badge">Step 5: Final Concluding Answer</span>
              <p>
                (a) Original: <strong>180 mL acid</strong> and <strong>420 mL water</strong>.
                <br>(b) Water to add for 1 : 4 ratio = <strong>300 mL</strong>.
                <br>(c) Acid to add for 1 : 1 ratio = <strong>240 mL</strong>.
              </p>
            </div>
          </div>
        </div>
      </details>

      <!-- PART 5.5: COMPETENCY-BASED CASE STUDIES -->
      <h3 class="subheading"><i class="fa-solid fa-briefcase"></i> Part 5.5: Competency-Based Real-World Case Studies</h3>

      <!-- CASE STUDY 1 -->
      <details class="ans-box">
        <summary>Case Study 1: Smart Drip Irrigation in Mayurbhanj, Odisha (4 Sub-Questions)</summary>
        <div class="ans-content">
          <div style="background: #ecfdf5; border: 1px solid #a7f3d0; border-radius: var(--radius-md); padding: 1.25rem; margin-bottom: 1.25rem;">
            <h4 style="font-family: 'Space Grotesk', sans-serif; color: #065f46; margin-bottom: 0.5rem;">
              <i class="fa-solid fa-seedling"></i> Case Narrative: Precision Agriculture in tribal Odisha
            </h4>
            <p style="font-size: 0.95rem; color: #064e3b; margin-bottom: 0;">
              Farmer Sanatan owns a 4-acre organic brinjal and tomato plantation in Mayurbhanj. Under the PM Krishi Sinchayee Yojana, he installed a solar-powered drip irrigation system with calibrated drippers. The system delivers precisely 4 litres of water per hour per plant emitter. Sanatan mixes liquid organic bio-NPK fertilizer with water in a fertigation tank in the ratio 2 : 25.
            </p>
          </div>

          <p><strong>Sub-question 1.1 (1M):</strong> If 500 emitters run continuously for 3.5 hours, calculate the total volume of water discharged in Litres.</p>
          <p style="color: #065f46;">
            <em>Solution:</em>
            <br>Total Discharge = <em>500 emitters × 4 L/h × 3.5 h = <strong>7,000 Litres</strong></em>.
          </p>

          <p><strong>Sub-question 1.2 (1M):</strong> To prepare a fertigation solution containing 12.5 Litres of bio-NPK fertilizer in the ratio 2 : 25, how much water must Sanatan add?</p>
          <p style="color: #065f46;">
            <em>Solution:</em>
            <br><em>Bio-NPK : Water :: 2 : 25</em> ⇒ <em>12.5 : W :: 2 : 25</em>
            <br><em>W = (12.5 × 25) ÷ 2 = 312.5 ÷ 2 = <strong>156.25 Litres of water</strong></em>.
          </p>

          <p><strong>Sub-question 1.3 (1.5M):</strong> Sanatan's solar pump pumps water at a uniform rate of 2,400 litres per hour under direct sunlight. How long will the pump take to fill a 15,000-litre farm storage pond? Express answer in hours and minutes.</p>
          <p style="color: #065f46;">
            <em>Solution:</em>
            <br>Time = <em>15,000 ÷ 2,400 = 6.25 hours</em>.
            <br>0.25 hours = <em>0.25 × 60 = 15 minutes</em>.
            <br>Time = <strong>6 hours 15 minutes</strong>.
          </p>

          <p><strong>Sub-question 1.4 (1.5M):</strong> Conventional flood irrigation previously consumed 28,000 litres per acre per week. The new drip system uses only 11,200 litres per acre per week. Calculate the ratio of water saved to conventional water used, and express the water conservation as a percentage.</p>
          <p style="color: #065f46;">
            <em>Solution:</em>
            <br>Water saved per acre = <em>28,000 - 11,200 = 16,800 Litres</em>.
            <br>Ratio of Saved to Conventional = <em>16,800 : 28,000 = (168 ÷ 56) : (280 ÷ 56) = <strong>3 : 5</strong></em>.
            <br>Percentage Conservation = <em>(3/5) × 100% = <strong>60% water conserved</strong></em>!
          </p>
        </div>
      </details>

      <!-- CASE STUDY 2 -->
      <details class="ans-box">
        <summary>Case Study 2: Kalinga Metal Crafts &amp; Bell Metal (Kansa) Casting (4 Sub-Questions)</summary>
        <div class="ans-content">
          <div style="background: #fffbeb; border: 1px solid #fde68a; border-radius: var(--radius-md); padding: 1.25rem; margin-bottom: 1.25rem;">
            <h4 style="font-family: 'Space Grotesk', sans-serif; color: #92400e; margin-bottom: 0.5rem;">
              <i class="fa-solid fa-hammer"></i> Case Narrative: Heritage Bell Metal Utensil Casting in Balkati, Khordha
            </h4>
            <p style="font-size: 0.95rem; color: #78350f; margin-bottom: 0;">
              In the historic village of Balkati near Bhubaneswar, traditional coppersmiths (Kansari artisans) cast resonant <em>Kansa</em> (bell metal) dinner thalis and bowls. Standard bell metal is an alloy of copper and pure tin in the mass ratio 4 : 1. Raw copper ingots cost ₹920 per kg, while pure tin ingots cost ₹2,400 per kg. During crucible melting, 5% of the molten alloy is lost to oxidation slag.
            </p>
          </div>

          <p><strong>Sub-question 2.1 (1M):</strong> An artisan casts a heavy ceremonial Kansa thali of final mass 3.2 kg. Find the mass of copper and tin contained in the finished thali.</p>
          <p style="color: #78350f;">
            <em>Solution:</em>
            <br>Total parts = 4 + 1 = 5 parts. Mass per part = 3.2 kg ÷ 5 = 0.64 kg.
            <br>• Copper = <em>4 × 0.64 kg = <strong>2.56 kg (2,560 g)</strong></em>.
            <br>• Tin = <em>1 × 0.64 kg = <strong>0.64 kg (640 g)</strong></em>.
          </p>

          <p><strong>Sub-question 2.2 (1M):</strong> Calculate the raw material cost of the metals in the 3.2 kg thali.</p>
          <p style="color: #78350f;">
            <em>Solution:</em>
            <br>Cost of Copper = 2.56 kg × ₹920 = ₹2,355.20.
            <br>Cost of Tin = 0.64 kg × ₹2,400 = ₹1,536.00.
            <br>Total Metal Cost = <em>₹2,355.20 + ₹1,536.00 = <strong>₹3,891.20</strong></em>.
          </p>

          <p><strong>Sub-question 2.3 (1.5M):</strong> Because 5% of the total raw metal mass is lost as oxidation slag during furnace smelting, what total mass of raw metal ingots must be melted to obtain 3.2 kg of usable alloy?</p>
          <p style="color: #78350f;">
            <em>Solution:</em>
            <br>Let raw mass be <em>M</em>. Since 5% is lost, 95% remains:
            <br><em>0.95 × M = 3.2 kg ⇒ M = 3.2 ÷ 0.95 ≈ <strong>3.368 kg</strong></em>.
          </p>

          <p><strong>Sub-question 2.4 (1.5M):</strong> The artisan adds a hand-carving labor fee that is proportional to the raw metal cost in the ratio 3 : 8. Calculate the artisan's labor fee and the final retail price of the carved thali.</p>
          <p style="color: #78350f;">
            <em>Solution:</em>
            <br>Labor Fee = <em>(3/8) × Raw Metal Cost = (3/8) × ₹3,891.20 = 3 × ₹486.40 = <strong>₹1,459.20</strong></em>.
            <br>Final Retail Price = Raw Cost + Labor = <em>₹3,891.20 + ₹1,459.20 = <strong>₹5,350.40</strong></em>.
          </p>
        </div>
      </details>

      <!-- PART 5.6: PYQS & MOST PROBABLE EXAM QUESTIONS -->
      <h3 class="subheading"><i class="fa-solid fa-clock-rotate-left"></i> Part 5.6: Previous Years Questions (PYQs) &amp; Most Probable Exam Questions</h3>

      <!-- PYQ 1 -->
      <details class="ans-box">
        <summary>PYQ 1 (2M): Does the Ratio of Perimeter to Area of a Square Remain Constant?</summary>
        <div class="ans-content">
          <div class="step-container">
            <div class="step-box step-1">
              <span class="step-badge">Step 1: Formulas for Square</span>
              <p>For a square of side length <em>s</em>: Perimeter <em>P = 4s</em>; Area <em>A = s²</em>.</p>
            </div>
            <div class="step-box step-2">
              <span class="step-badge">Step 2: Ratio Formation</span>
              <p>Ratio <em>P : A = (4s) / s² = <strong>4 / s</strong></em>.</p>
            </div>
            <div class="step-box step-3">
              <span class="step-badge">Step 3: Testing with Numerical Values</span>
              <p>
                • For <em>s = 2 cm</em>: P = 8 cm, A = 4 cm² ⇒ Ratio = 8 : 4 = <strong>2 : 1</strong>.
                <br>• For <em>s = 4 cm</em>: P = 16 cm, A = 16 cm² ⇒ Ratio = 16 : 16 = <strong>1 : 1</strong>.
                <br>• For <em>s = 8 cm</em>: P = 32 cm, A = 64 cm² ⇒ Ratio = 32 : 64 = <strong>1 : 2</strong>.
              </p>
            </div>
            <div class="step-box step-4">
              <span class="step-badge">Step 4: Deduction</span>
              <p>The ratio <em>4/s</em> decreases as side length increases. It is not invariant.</p>
            </div>
            <div class="step-box step-5">
              <span class="step-badge">Step 5: Final Concluding Answer</span>
              <p><strong>No, the ratio does NOT remain constant.</strong> Perimeter grows linearly (<em>4s</em>) while area grows quadratically (<em>s²</em>), so the ratio <em>4/s</em> decreases as the square grows.</p>
            </div>
          </div>
        </div>
      </details>

      <!-- PYQ 2 -->
      <details class="ans-box">
        <summary>PYQ 2 (3M): Compound Trairāśika — Sambalpuri Fabric Dyeing</summary>
        <div class="ans-content">
          <div class="step-container">
            <div class="step-box step-1">
              <span class="step-badge">Step 1: Given Information &amp; Variables</span>
              <p>
                • 8 workers dye 240 m of fabric in 6 hours.
                <br>• Target: 14 workers working for 9 hours.
                <br>• Goal: Find total length of fabric dyed (<em>L</em>).
              </p>
            </div>
            <div class="step-box step-2">
              <span class="step-badge">Step 2: Unitary Rate per Man-Hour</span>
              <p>
                Total man-hours initially = <em>8 workers × 6 hours = 48 man-hours</em>.
                <br>Dyeing rate = <em>240 m ÷ 48 man-hours = <strong>5 metres per man-hour</strong></em>.
              </p>
            </div>
            <div class="step-box step-3">
              <span class="step-badge">Step 3: Calculating for Target Group</span>
              <p>
                Target man-hours = <em>14 workers × 9 hours = 126 man-hours</em>.
                <br>Total fabric dyed = <em>126 man-hours × 5 m/man-hour = <strong>630 metres</strong></em>.
              </p>
            </div>
            <div class="step-box step-4">
              <span class="step-badge">Step 4: Compound Ratio Formula Verification</span>
              <p>
                <em>L = 240 × (14 / 8) × (9 / 6) = 240 × 1.75 × 1.5 = 240 × 2.625 = 630 m</em> ✓.
              </p>
            </div>
            <div class="step-box step-5">
              <span class="step-badge">Step 5: Final Concluding Answer</span>
              <p>The 14 workers will dye <strong>630 metres of fabric</strong> in 9 hours.</p>
            </div>
          </div>
        </div>
      </details>

      <!-- PYQ 3 -->
      <details class="ans-box">
        <summary>PYQ 3 (3M): Two-Era Age Ratio System</summary>
        <div class="ans-content">
          <div class="step-container">
            <div class="step-box step-1">
              <span class="step-badge">Step 1: Given Information</span>
              <p>
                • 5 years ago: Ratio of ages (A : B) = 4 : 5.
                <br>• 10 years hence (from now): Ratio of ages (A : B) = 7 : 8.
                <br>• Goal: Find present ages of A and B.
              </p>
            </div>
            <div class="step-box step-2">
              <span class="step-badge">Step 2: Setting up Algebraic Variables</span>
              <p>
                Let ages 5 years ago be <em>4k</em> and <em>5k</em>.
                <br>Present ages: A = <em>4k + 5</em>, B = <em>5k + 5</em>.
                <br>Ages 10 years hence: A = <em>4k + 15</em>, B = <em>5k + 15</em>.
              </p>
            </div>
            <div class="step-box step-3">
              <span class="step-badge">Step 3: Solving the Proportion</span>
              <p>
                <em>(4k + 15) / (5k + 15) = 7 / 8</em>
                <br>Cross-multiply:
                <br><em>8(4k + 15) = 7(5k + 15)</em>
                <br><em>32k + 120 = 35k + 105</em>
                <br><em>35k - 32k = 120 - 105</em>
                <br><em>3k = 15 ⇒ k = 5</em>.
              </p>
            </div>
            <div class="step-box step-4">
              <span class="step-badge">Step 4: Present Ages</span>
              <p>
                • Present age of A = <em>4(5) + 5 = 20 + 5 = <strong>25 years</strong></em>.
                <br>• Present age of B = <em>5(5) + 5 = 25 + 5 = <strong>30 years</strong></em>.
                <br>Verification: 5 years ago: 20:25 = 4:5 ✓. 10 years hence: 35:40 = 7:8 ✓.
              </p>
            </div>
            <div class="step-box step-5">
              <span class="step-badge">Step 5: Final Concluding Answer</span>
              <p>A's present age is <strong>25 years</strong> and B's present age is <strong>30 years</strong>.</p>
            </div>
          </div>
        </div>
      </details>

      <!-- PYQ 4 -->
      <details class="ans-box">
        <summary>PYQ 4 (3M): Packaging Volume Discount &amp; Percentage Savings</summary>
        <div class="ans-content">
          <div class="step-container">
            <div class="step-box step-1">
              <span class="step-badge">Step 1: Given Pricing Options</span>
              <p>
                • Small tube: 50 mL for ₹85.
                <br>• Economy bottle: 200 mL for ₹260.
                <br>• Goal: Find percentage savings by purchasing the economy bottle instead of four 50 mL tubes.
              </p>
            </div>
            <div class="step-box step-2">
              <span class="step-badge">Step 2: Equivalent Volume Cost</span>
              <p>
                To get 200 mL using small tubes: <em>4 tubes × 50 mL = 200 mL</em>.
                <br>Cost of four 50 mL tubes = <em>4 × ₹85 = <strong>₹340</strong></em>.
                <br>Cost of one 200 mL bottle = <strong>₹260</strong>.
              </p>
            </div>
            <div class="step-box step-3">
              <span class="step-badge">Step 3: Calculating Absolute &amp; Percentage Savings</span>
              <p>
                • Absolute Savings = <em>₹340 - ₹260 = <strong>₹80</strong></em>.
                <br>• Percentage Savings = <em>(Savings ÷ Cost of Tubes) × 100%</em>
                <br><em>= (80 ÷ 340) × 100% = (8 / 34) × 100% = (4 / 17) × 100% ≈ <strong>23.53%</strong></em>.
              </p>
            </div>
            <div class="step-box step-4">
              <span class="step-badge">Step 4: Unit Cost Check</span>
              <p>
                Small tube: ₹85 / 50 mL = ₹1.70 per mL.
                <br>Bottle: ₹260 / 200 mL = ₹1.30 per mL.
                <br>Unit saving = ₹0.40/mL. Percentage = (0.40 / 1.70) × 100% ≈ 23.53% ✓.
              </p>
            </div>
            <div class="step-box step-5">
              <span class="step-badge">Step 5: Final Concluding Answer</span>
              <p>Purchasing the economy bottle provides an absolute saving of <strong>₹80</strong>, representing a <strong>23.53% discount</strong>.</p>
            </div>
          </div>
        </div>
      </details>

      <!-- PYQ 5 -->
      <details class="ans-box">
        <summary>PYQ 5 (3M): Temperature Equality Point (°C = °F Derivation)</summary>
        <div class="ans-content">
          <div class="step-container">
            <div class="step-box step-1">
              <span class="step-badge">Step 1: Formula Definition</span>
              <p>The conversion between Celsius (°C) and Fahrenheit (°F) is: <em>F = (9/5)C + 32</em>.</p>
            </div>
            <div class="step-box step-2">
              <span class="step-badge">Step 2: Condition for Numerical Equality</span>
              <p>Set <em>F = C = T</em>:
              <br><em>T = (9/5)T + 32</em></p>
            </div>
            <div class="step-box step-3">
              <span class="step-badge">Step 3: Solving the Algebraic Equation</span>
              <p>
                Multiply the entire equation by 5:
                <br><em>5T = 9T + 160</em>
                <br>Subtract 9T from both sides:
                <br><em>5T - 9T = 160</em>
                <br><em>-4T = 160</em>
                <br><em>T = 160 ÷ (-4) = <strong>-40</strong></em>.
              </p>
            </div>
            <div class="step-box step-4">
              <span class="step-badge">Step 4: Verification</span>
              <p>
                Substitute C = -40 into formula:
                <br>F = (9/5)(-40) + 32 = 9(-8) + 32 = -72 + 32 = -40 ✓.
                <br>Both thermometers read the exact same number at -40°!
              </p>
            </div>
            <div class="step-box step-5">
              <span class="step-badge">Step 5: Final Concluding Answer</span>
              <p>The unique temperature at which Celsius and Fahrenheit scales read the exact same number is <strong>-40° (-40 °C = -40 °F)</strong>.</p>
            </div>
          </div>
        </div>
      </details>
    </section>
"""
