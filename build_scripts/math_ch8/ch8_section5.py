# -*- coding: utf-8 -*-
"""
Module: ch8_section5.py
Contains Section 5: Complete Exam Question Bank (Exhaustive 27 Questions):
- 5 Conceptual MCQs with interactive option buttons & trap feedback
- 5 Assertion & Reasoning questions
- 6 Short Answer Questions (2M/3M)
- 4 Long Answer Questions (5M) with detailed marking schemes
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
          <strong>Q1.</strong> A garment retailer announces a promotional discount of <strong>“20% + 20% Off”</strong> on branded jeans. What is the actual single equivalent percentage discount?
        </div>
        <div class="mcq-options">
          <button class="option-btn" onclick="evaluateMCQ(1, 'A', false, 'A is the classic trap! 20% + 20% does NOT equal 40% because the second discount applies to the already discounted price.')">
            <span class="pos-badge">A</span> 40%
          </button>
          <button class="option-btn" onclick="evaluateMCQ(1, 'B', true, 'Correct! Multiplier = 0.80 × 0.80 = 0.64. Net discount = (1 - 0.64) × 100% = 36%.')">
            <span class="pos-badge">B</span> 36%
          </button>
          <button class="option-btn" onclick="evaluateMCQ(1, 'C', false, 'Incorrect. Calculate (1 - 0.80 × 0.80) × 100% = 36%.')">
            <span class="pos-badge">C</span> 38%
          </button>
          <button class="option-btn" onclick="evaluateMCQ(1, 'D', false, 'Incorrect. 32% would correspond to discounts of 20% and 15%.')">
            <span class="pos-badge">D</span> 32%
          </button>
        </div>
        <div class="trap-feedback" id="feedback1"></div>
      </div>

      <!-- MCQ 2 -->
      <div class="mcq-card" id="mcqCard2">
        <div class="mcq-question">
          <strong>Q2.</strong> If <strong>8% of 125</strong> is denoted by <em>K</em>, what is the value of <strong>125% of 8</strong>?
        </div>
        <div class="mcq-options">
          <button class="option-btn" onclick="evaluateMCQ(2, 'A', false, 'Incorrect. 125% of 8 does not halve the value.')">
            <span class="pos-badge">A</span> K / 2
          </button>
          <button class="option-btn" onclick="evaluateMCQ(2, 'B', false, 'Incorrect. Commutativity preserves the exact value; it does not double it.')">
            <span class="pos-badge">B</span> 2 K
          </button>
          <button class="option-btn" onclick="evaluateMCQ(2, 'C', true, 'Spot on! By the Commutative Law of Percentages, x% of y = y% of x. Both expressions equal (8 × 125) / 100 = 10.')">
            <span class="pos-badge">C</span> K
          </button>
          <button class="option-btn" onclick="evaluateMCQ(2, 'D', false, 'Incorrect. It is a linear relationship, not quadratic.')">
            <span class="pos-badge">D</span> K²
          </button>
        </div>
        <div class="trap-feedback" id="feedback2"></div>
      </div>

      <!-- MCQ 3 -->
      <div class="mcq-card" id="mcqCard3">
        <div class="mcq-question">
          <strong>Q3.</strong> A merchant marks his goods <strong>25% above cost price</strong>. What percentage discount must he offer on the marked price to sell them at cost price (break-even)?
        </div>
        <div class="mcq-options">
          <button class="option-btn" onclick="evaluateMCQ(3, 'A', false, 'A is the textbook trap! A 25% discount on 1.25x reduces price to 0.9375x, creating a 6.25% loss!')">
            <span class="pos-badge">A</span> 25%
          </button>
          <button class="option-btn" onclick="evaluateMCQ(3, 'B', true, 'Brilliant! Required discount = (1.25 - 1.00) / 1.25 = 0.25 / 1.25 = 1/5 = 20%.')">
            <span class="pos-badge">B</span> 20%
          </button>
          <button class="option-btn" onclick="evaluateMCQ(3, 'C', false, 'Incorrect. 15% discount would leave a 6.25% profit.')">
            <span class="pos-badge">C</span> 15%
          </button>
          <button class="option-btn" onclick="evaluateMCQ(3, 'D', false, 'Incorrect. 22.5% is an arbitrary average.')">
            <span class="pos-badge">D</span> 22.5%
          </button>
        </div>
        <div class="trap-feedback" id="feedback3"></div>
      </div>

      <!-- MCQ 4 -->
      <div class="mcq-card" id="mcqCard4">
        <div class="mcq-question">
          <strong>Q4.</strong> A sum of money doubles itself in <strong>8 years</strong> under Simple Interest. What is the annual rate of interest (<em>R</em>)?
        </div>
        <div class="mcq-options">
          <button class="option-btn" onclick="evaluateMCQ(4, 'A', false, 'Incorrect. At 10%, doubling takes 100/10 = 10 years.')">
            <span class="pos-badge">A</span> 10% p.a.
          </button>
          <button class="option-btn" onclick="evaluateMCQ(4, 'B', true, 'Correct! To double, interest must equal principal (SI = P). SI = (P × R × T)/100 ⇒ P = (P × R × 8)/100 ⇒ R = 100/8 = 12.5% p.a.')">
            <span class="pos-badge">B</span> 12.5% p.a.
          </button>
          <button class="option-btn" onclick="evaluateMCQ(4, 'C', false, 'Incorrect. At 15%, doubling takes 6.67 years.')">
            <span class="pos-badge">C</span> 15% p.a.
          </button>
          <button class="option-btn" onclick="evaluateMCQ(4, 'D', false, 'Incorrect. At 8%, doubling takes 12.5 years.')">
            <span class="pos-badge">D</span> 8% p.a.
          </button>
        </div>
        <div class="trap-feedback" id="feedback4"></div>
      </div>

      <!-- MCQ 5 -->
      <div class="mcq-card" id="mcqCard5">
        <div class="mcq-question">
          <strong>Q5.</strong> (The Potato Paradox): A 200 kg batch of fresh cucumbers consists of <strong>99% water</strong>. After resting in the sun, dehydration reduces the water content to <strong>98%</strong>. What is the new total weight of the cucumbers?
        </div>
        <div class="mcq-options">
          <button class="option-btn" onclick="evaluateMCQ(5, 'A', false, 'A is the universal psychological trap! People assume a 1% water loss means 200 - 2 = 198 kg.')">
            <span class="pos-badge">A</span> 198 kg
          </button>
          <button class="option-btn" onclick="evaluateMCQ(5, 'B', true, 'Astonishing and Correct! Non-water solid matter = 1% of 200 kg = 2 kg. In the dehydrated batch, this 2 kg makes up 2% of total weight. Total weight = 2 kg ÷ 0.02 = 100 kg! Exactly half the weight evaporated!')">
            <span class="pos-badge">B</span> 100 kg
          </button>
          <button class="option-btn" onclick="evaluateMCQ(5, 'C', false, 'Incorrect. Set 2 kg solid = 2% of new weight.')">
            <span class="pos-badge">C</span> 150 kg
          </button>
          <button class="option-btn" onclick="evaluateMCQ(5, 'D', false, 'Incorrect. 196 kg assumes 2% of 200 kg evaporated.')">
            <span class="pos-badge">D</span> 196 kg
          </button>
        </div>
        <div class="trap-feedback" id="feedback5"></div>
      </div>

      <!-- PART 5.2: ASSERTION & REASONING -->
      <h3 class="subheading"><i class="fa-solid fa-scale-unbalanced"></i> Part 5.2: Assertion &amp; Reasoning Questions</h3>
      <p style="font-size: 0.9rem; color: var(--text-muted); margin-bottom: 1rem;">
        <em>Directions: Choose (A) if both Assertion &amp; Reason are true and Reason is correct explanation; (B) if both are true but Reason is NOT correct explanation; (C) if Assertion is true but Reason is false; (D) if Assertion is false but Reason is true.</em>
      </p>

      <!-- AR 1 -->
      <details class="ans-box" id="ar1">
        <summary>AR 1: Price Increased by 20% and then Decreased by 20%</summary>
        <div class="ans-content">
          <div class="step-container">
            <div class="step-box step-1">
              <span class="step-badge">Assertion &amp; Reason Statements</span>
              <p><strong>Assertion (A):</strong> If the price of an article is increased by 20% and subsequently decreased by 20%, the final price is strictly less than the initial price.<br>
              <strong>Reason (R):</strong> In successive percentage changes, the second percentage reduction acts upon a larger numerical base than the original baseline.</p>
            </div>
            <div class="step-box step-2">
              <span class="step-badge">Evaluation</span>
              <p>Let original price = 100. After +20%, price = 120. A 20% reduction on 120 = 24, giving final price = 96 &lt; 100 (a 4% loss). Assertion (A) is TRUE. Reason (R) correctly explains that 20% of 120 (24) exceeds 20% of 100 (20). Reason (R) is TRUE and correctly explains (A).</p>
            </div>
            <div class="step-box step-5">
              <span class="step-badge">Correct Choice</span>
              <p><strong>(A) Both Assertion (A) and Reason (R) are true, and Reason (R) is the correct explanation of Assertion (A).</strong></p>
            </div>
          </div>
        </div>
      </details>

      <!-- AR 2 -->
      <details class="ans-box" id="ar2">
        <summary>AR 2: Base of Profit Percentage Calculation</summary>
        <div class="ans-content">
          <div class="step-container">
            <div class="step-box step-1">
              <span class="step-badge">Assertion &amp; Reason Statements</span>
              <p><strong>Assertion (A):</strong> In commercial transactions, profit percentage is always calculated on the Cost Price unless specifically stated otherwise.<br>
              <strong>Reason (R):</strong> Cost Price represents the true capital invested by the seller to acquire or produce the article.</p>
            </div>
            <div class="step-box step-2">
              <span class="step-badge">Evaluation</span>
              <p>Assertion (A) is TRUE: Profit% = (Profit / CP) × 100. Reason (R) is TRUE: Profit is the return on capital investment (CP). Reason correctly explains why CP is the canonical baseline.</p>
            </div>
            <div class="step-box step-5">
              <span class="step-badge">Correct Choice</span>
              <p><strong>(A) Both Assertion (A) and Reason (R) are true, and Reason (R) is the correct explanation of Assertion (A).</strong></p>
            </div>
          </div>
        </div>
      </details>

      <!-- AR 3 -->
      <details class="ans-box" id="ar3">
        <summary>AR 3: Commutative Property of Percentages</summary>
        <div class="ans-content">
          <div class="step-container">
            <div class="step-box step-1">
              <span class="step-badge">Assertion &amp; Reason Statements</span>
              <p><strong>Assertion (A):</strong> 15% of 80 is strictly equal to 80% of 15.<br>
              <strong>Reason (R):</strong> Multiplication of rational numbers satisfies the commutative property: <em>a × b = b × a</em>.</p>
            </div>
            <div class="step-box step-2">
              <span class="step-badge">Evaluation</span>
              <p>Assertion (A) is TRUE: (15 × 80)/100 = 12, and (80 × 15)/100 = 12. Reason (R) is TRUE: Since 15 × 80 = 80 × 15, dividing both by 100 guarantees equality. Reason is the exact algebraic foundation.</p>
            </div>
            <div class="step-box step-5">
              <span class="step-badge">Correct Choice</span>
              <p><strong>(A) Both Assertion (A) and Reason (R) are true, and Reason (R) is the correct explanation of Assertion (A).</strong></p>
            </div>
          </div>
        </div>
      </details>

      <!-- AR 4 -->
      <details class="ans-box" id="ar4">
        <summary>AR 4: Compound Interest Annual Accrual Rate</summary>
        <div class="ans-content">
          <div class="step-container">
            <div class="step-box step-1">
              <span class="step-badge">Assertion &amp; Reason Statements</span>
              <p><strong>Assertion (A):</strong> Under annual compounding, the interest earned during Year 3 is equal to the interest earned during Year 1.<br>
              <strong>Reason (R):</strong> Under compound interest, earned interest is reinvested into the principal at the end of each period, causing the principal to expand monotonically.</p>
            </div>
            <div class="step-box step-2">
              <span class="step-badge">Evaluation</span>
              <p>Assertion (A) is FALSE: Year 3 interest is strictly greater than Year 1 interest because the principal has increased twice. Reason (R) is TRUE: Compounding adds accumulated interest to principal.</p>
            </div>
            <div class="step-box step-5">
              <span class="step-badge">Correct Choice</span>
              <p><strong>(D) Assertion (A) is false, but Reason (R) is true.</strong></p>
            </div>
          </div>
        </div>
      </details>

      <!-- AR 5 -->
      <details class="ans-box" id="ar5">
        <summary>AR 5: Geometric Dimensions and Area Conservation</summary>
        <div class="ans-content">
          <div class="step-container">
            <div class="step-box step-1">
              <span class="step-badge">Assertion &amp; Reason Statements</span>
              <p><strong>Assertion (A):</strong> If the length of a rectangle increases by 25%, the breadth must decrease by 25% to keep the area constant.<br>
              <strong>Reason (R):</strong> Area of a rectangle equals length × breadth; when length increases by factor <em>k</em>, breadth must be multiplied by <em>1/k</em>.</p>
            </div>
            <div class="step-box step-2">
              <span class="step-badge">Evaluation</span>
              <p>Assertion (A) is FALSE: If <em>L' = 1.25 L = (5 / 4) L</em>, then <em>B' = (4 / 5) B = 0.80 B</em>, which is a 20% decrease, NOT 25%! Reason (R) is TRUE: <em>L' × B' = (k L) × (B/k) = L × B</em>.</p>
            </div>
            <div class="step-box step-5">
              <span class="step-badge">Correct Choice</span>
              <p><strong>(D) Assertion (A) is false, but Reason (R) is true.</strong></p>
            </div>
          </div>
        </div>
      </details>

      <!-- PART 5.3: SHORT ANSWER QUESTIONS (2M / 3M) -->
      <h3 class="subheading"><i class="fa-solid fa-pen-to-square"></i> Part 5.3: Short Answer Questions (2M / 3M)</h3>

      <!-- SA 1 -->
      <details class="ans-box" id="sa1">
        <summary>SA 1 (2M): Comparing Academic Test Scores — Math (36/45) vs Science (56/70)</summary>
        <div class="ans-content">
          <div class="step-container">
            <div class="step-box step-1">
              <span class="step-badge">Question</span>
              <p>A student scored 36 marks out of 45 in Mathematics and 56 marks out of 70 in Science. In which subject did the student perform better?</p>
            </div>
            <div class="step-box step-3">
              <span class="step-badge">Solution</span>
              <p>1. Mathematics Percentage = <code>(36 / 45) × 100% = (4 / 5) × 100% = 80.0%</code>.<br>
              2. Science Percentage = <code>(56 / 70) × 100% = (8 / 10) × 100% = 80.0%</code>.<br>
              3. Comparison: Both percentages are exactly identical (80.0%).</p>
            </div>
            <div class="step-box step-5">
              <span class="step-badge">Answer</span>
              <p>The student performed <strong>equally well in both subjects (80% in each)</strong>.</p>
            </div>
          </div>
        </div>
      </details>

      <!-- SA 2 -->
      <details class="ans-box" id="sa2">
        <summary>SA 2 (2M): Single Equivalent Discount for Successive 10% and 5%</summary>
        <div class="ans-content">
          <div class="step-container">
            <div class="step-box step-1">
              <span class="step-badge">Question</span>
              <p>Find the single equivalent discount for two successive discounts of 10% and 5%.</p>
            </div>
            <div class="step-box step-3">
              <span class="step-badge">Solution</span>
              <p>Net Multiplier = <code>(1 - 0.10) × (1 - 0.05) = 0.90 × 0.95 = 0.855</code>.<br>
              Single Equivalent Discount = <code>(1 - 0.855) × 100% = 0.145 × 100% = 14.5%</code>.<br>
              (Formula: <em>10 + 5 - (10 × 5 / 100) = 15 - 0.5 = 14.5%</em>).</p>
            </div>
            <div class="step-box step-5">
              <span class="step-badge">Answer</span>
              <p>The single equivalent discount is <strong>14.5%</strong>.</p>
            </div>
          </div>
        </div>
      </details>

      <!-- SA 3 -->
      <details class="ans-box" id="sa3">
        <summary>SA 3 (3M): TV Marked at ₹32,000 with 15% Discount and 18% GST</summary>
        <div class="ans-content">
          <div class="step-container">
            <div class="step-box step-1">
              <span class="step-badge">Question</span>
              <p>A TV set is marked at ₹32,000. A dealer offers a festival discount of 15%, and then charges 18% GST on the discounted price. Calculate the final bill amount.</p>
            </div>
            <div class="step-box step-3">
              <span class="step-badge">Solution</span>
              <p>1. Price after 15% discount = <code>₹32,000 × (1 - 0.15) = 32,000 × 0.85 = ₹27,200</code>.<br>
              2. GST Amount = <code>18% of ₹27,200 = 0.18 × 27,200 = ₹4,896</code>.<br>
              3. Final Bill Amount = <code>₹27,200 + ₹4,896 = ₹32,096</code>.<br>
              (Or: 27,200 × 1.18 = ₹32,096).</p>
            </div>
            <div class="step-box step-5">
              <span class="step-badge">Answer</span>
              <p>The final amount paid by the customer is <strong>₹32,096</strong>.</p>
            </div>
          </div>
        </div>
      </details>

      <!-- SA 4 -->
      <details class="ans-box" id="sa4">
        <summary>SA 4 (3M): Almirah with Overheads and 15% Profit</summary>
        <div class="ans-content">
          <div class="step-container">
            <div class="step-box step-1">
              <span class="step-badge">Question</span>
              <p>An almirah was bought for ₹14,360 and ₹240 was spent on its transportation and installation. It was then sold at a profit of 15%. Find the selling price.</p>
            </div>
            <div class="step-box step-3">
              <span class="step-badge">Solution</span>
              <p>1. Effective Cost Price = Purchase Price + Overheads = <code>₹14,360 + ₹240 = ₹14,600</code>.<br>
              2. Profit Amount = <code>15% of ₹14,600 = 0.15 × 14,600 = ₹2,190</code>.<br>
              3. Selling Price = <code>Effective CP + Profit = ₹14,600 + ₹2,190 = ₹16,790</code>.</p>
            </div>
            <div class="step-box step-5">
              <span class="step-badge">Answer</span>
              <p>The selling price of the almirah is <strong>₹16,790</strong>.</p>
            </div>
          </div>
        </div>
      </details>

      <!-- SA 5 -->
      <details class="ans-box" id="sa5">
        <summary>SA 5 (3M): CP of 18 Mangoes = SP of 15 Mangoes</summary>
        <div class="ans-content">
          <div class="step-container">
            <div class="step-box step-1">
              <span class="step-badge">Question</span>
              <p>If the cost price of 18 mangoes is equal to the selling price of 15 mangoes, find the profit or loss percentage.</p>
            </div>
            <div class="step-box step-3">
              <span class="step-badge">Solution</span>
              <p>Let CP of 1 mango = ₹1. Then CP of 15 mangoes = ₹15.<br>
              Given: SP of 15 mangoes = CP of 18 mangoes = ₹18.<br>
              Profit on 15 mangoes = SP - CP = ₹18 - ₹15 = ₹3.<br>
              Profit% = <code>(Profit / CP) × 100% = (3 / 15) × 100% = (1 / 5) × 100% = 20%</code>.</p>
            </div>
            <div class="step-box step-5">
              <span class="step-badge">Answer</span>
              <p>The seller makes a <strong>profit of 20%</strong>.</p>
            </div>
          </div>
        </div>
      </details>

      <!-- SA 6 -->
      <details class="ans-box" id="sa6">
        <summary>SA 6 (3M): Town Population Growth at 5% p.a. for 2 Years</summary>
        <div class="ans-content">
          <div class="step-container">
            <div class="step-box step-1">
              <span class="step-badge">Question</span>
              <p>The population of a town was 64,000 two years ago. It increased at the rate of 5% per annum. Find the present population.</p>
            </div>
            <div class="step-box step-3">
              <span class="step-badge">Solution</span>
              <p>Initial Population <em>P = 64,000</em>, Rate <em>R = 5%</em> p.a., Time <em>n = 2</em> years.<br>
              Present Population = <code>P × (1 + R/100)² = 64,000 × (1.05)² = 64,000 × 1.1025 = 70,560</code>.<br>
              (Check: Year 1 = 64,000 + 3,200 = 67,200; Year 2 = 67,200 + 3,360 = 70,560).</p>
            </div>
            <div class="step-box step-5">
              <span class="step-badge">Answer</span>
              <p>The present population of the town is <strong>70,560</strong>.</p>
            </div>
          </div>
        </div>
      </details>

      <!-- PART 5.4: LONG ANSWER QUESTIONS (5M) WITH MARKING SCHEMES -->
      <h3 class="subheading"><i class="fa-solid fa-file-lines"></i> Part 5.4: Long Answer Questions (5M) with Step-by-Step Marking Schemes</h3>

      <!-- LA 1 -->
      <details class="ans-box" id="la1">
        <summary>LA 1 (5M): Comprehensive SI vs CI Comparison on ₹40,000 @ 8% for 3 Years (With Marking Scheme)</summary>
        <div class="ans-content">
          <div class="step-container">
            <div class="step-box step-1">
              <span class="step-badge">Question</span>
              <p>Shreya invests ₹40,000 in a fixed deposit scheme at 8% per annum for 3 years. Calculate and compare:<br>
              (a) The total simple interest and maturity amount under linear non-compounding.<br>
              (b) The year-by-year compound interest and final maturity amount compounded annually.<br>
              (c) The exact surplus interest earned due to compounding.</p>
            </div>
            <div class="step-box step-3">
              <span class="step-badge">Complete Model Solution</span>
              <p><strong>Part (a): Simple Interest Scheme [1.5 Marks]</strong><br>
              Principal <em>P = ₹40,000</em>, <em>R = 8%</em>, <em>T = 3</em> years.<br>
              <em>SI = (P × R × T / 100) = (40,000 × 8 × 3 / 100) = 400 × 24 = ₹9,600</em>.<br>
              <em>Amount (SI) = P + SI = 40,000 + 9,600 = <strong>₹49,600</strong></em>.<br><br>
              <strong>Part (b): Compound Interest Scheme (Year-by-Year) [2.5 Marks]</strong><br>
              - <em>Year 1:</em> Interest = <em>8%  of  40,000 = ₹3,200</em>.<br>
              Principal for Year 2 = <em>40,000 + 3,200 = ₹43,200</em>.<br>
              - <em>Year 2:</em> Interest = <em>8%  of  43,200 = 0.08 × 43,200 = ₹3,456</em>.<br>
              Principal for Year 3 = <em>43,200 + 3,456 = ₹46,656</em>.<br>
              - <em>Year 3:</em> Interest = <em>8%  of  46,656 = 0.08 × 46,656 = ₹3,732.48</em>.<br>
              Final Compound Amount = <em>46,656 + 3,732.48 = <strong>₹50,388.48</strong></em>.<br>
              Total Compound Interest = <em>₹50,388.48 - ₹40,000 = <strong>₹10,388.48</strong></em>.<br><br>
              <strong>Part (c): Surplus Compounding Gain [1 Mark]</strong><br>
              Surplus = <em>CI - SI = 10,388.48 - 9,600 = <strong>₹788.48</strong></em>.</p>
            </div>
            <div class="step-box step-4">
              <span class="step-badge">Step-by-Step Marking Scheme</span>
              <ul>
                <li>Correct SI formula and calculation of ₹9,600 and ₹49,600: <strong>[1.5 M]</strong></li>
                <li>Year-by-year interest calculation (Year 1: ₹3,200; Year 2: ₹3,456; Year 3: ₹3,732.48): <strong>[1.5 M]</strong></li>
                <li>Final CI Amount ₹50,388.48 and CI ₹10,388.48: <strong>[1.0 M]</strong></li>
                <li>Difference calculation (₹788.48) with concluding statement: <strong>[1.0 M]</strong></li>
              </ul>
            </div>
            <div class="step-box step-5">
              <span class="step-badge">Answer</span>
              <p>SI Amount = <strong>₹49,600</strong>; CI Amount = <strong>₹50,388.48</strong>; Surplus Compounding Profit = <strong>₹788.48</strong>.</p>
            </div>
          </div>
        </div>
      </details>

      <!-- LA 2 -->
      <details class="ans-box" id="la2">
        <summary>LA 2 (5M): Multi-Tier Retail Supply Chain &amp; GST Billing (With Marking Scheme)</summary>
        <div class="ans-content">
          <div class="step-container">
            <div class="step-box step-1">
              <span class="step-badge">Question</span>
              <p>A wholesaler supplies a washing machine to a retailer for ₹24,000. The retailer incurs ₹800 on freight and loading. The retailer marks the machine to earn a 25% profit margin on his total cost. During a festival sale, he offers a 10% discount to a customer, and GST is charged at 18%. Calculate:<br>
              (i) Effective Cost Price for the retailer.<br>
              (ii) Marked Price of the machine.<br>
              (iii) Discount amount and Selling Price.<br>
              (iv) GST amount charged.<br>
              (v) Final bill amount paid by the customer.</p>
            </div>
            <div class="step-box step-3">
              <span class="step-badge">Complete Model Solution</span>
              <p><strong>(i) Effective Cost Price:</strong><br>
              <code>Effective CP = 24,000 + 800 = ₹24,800</code> [1 M].<br><br>
              <strong>(ii) Marked Price (with 25% Markup on Cost):</strong><br>
              <code>MP = 24,800 × (1 + 0.25) = 24,800 × 1.25 = ₹31,000</code> [1 M].<br><br>
              <strong>(iii) Discount &amp; Selling Price:</strong><br>
              Discount = 10% of ₹31,000 = ₹3,100.<br>
              <code>SP = 31,000 - 3,100 = ₹27,900</code> [1 M].<br><br>
              <strong>(iv) GST Amount:</strong><br>
              <code>GST = 18% of ₹27,900 = 0.18 × 27,900 = ₹5,022</code> [1 M].<br><br>
              <strong>(v) Customer's Final Invoice Bill:</strong><br>
              <code>Final Bill = SP + GST = 27,900 + 5,022 = ₹32,922</code> [1 M].</p>
            </div>
            <div class="step-box step-4">
              <span class="step-badge">Marking Scheme Breakdown</span>
              <ul>
                <li>(i) Calculation of Effective CP (₹24,800): <strong>[1.0 M]</strong></li>
                <li>(ii) Marked Price calculation (₹31,000): <strong>[1.0 M]</strong></li>
                <li>(iii) Net Selling Price (₹27,900): <strong>[1.0 M]</strong></li>
                <li>(iv) GST calculation (₹5,022): <strong>[1.0 M]</strong></li>
                <li>(v) Final invoice total (₹32,922): <strong>[1.0 M]</strong></li>
              </ul>
            </div>
            <div class="step-box step-5">
              <span class="step-badge">Answer</span>
              <p>Effective CP = <strong>₹24,800</strong>; MP = <strong>₹31,000</strong>; SP = <strong>₹27,900</strong>; GST = <strong>₹5,022</strong>; Customer Bill = <strong>₹32,922</strong>.</p>
            </div>
          </div>
        </div>
      </details>

      <!-- LA 3 -->
      <details class="ans-box" id="la3">
        <summary>LA 3 (5M): Bus Fleet Depreciation &amp; Escalating Maintenance Costs (With Marking Scheme)</summary>
        <div class="ans-content">
          <div class="step-container">
            <div class="step-box step-1">
              <span class="step-badge">Question</span>
              <p>A transport operator buys a passenger bus for ₹18,00,000. Its value depreciates at 10% per annum for the first 2 years and at 15% in the 3rd year. Simultaneously, annual maintenance starts at ₹25,000 in Year 1 and escalates by 20% each subsequent year.<br>
              (a) Determine the depreciated book value of the bus at the end of 3 years.<br>
              (b) Calculate the total maintenance expenditure incurred over the 3-year period.</p>
            </div>
            <div class="step-box step-3">
              <span class="step-badge">Complete Model Solution</span>
              <p><strong>Part (a): Depreciated Asset Value [3 Marks]</strong><br>
              - End of Year 1 (10% decay): <em>18,00,000 × 0.90 = ₹16,20,000</em>.<br>
              - End of Year 2 (10% decay): <em>16,20,000 × 0.90 = ₹14,58,000</em>.<br>
              - End of Year 3 (15% decay): <em>14,58,000 × (1 - 0.15) = 14,58,000 × 0.85 = <strong>₹12,39,300</strong></em>.<br><br>
              <strong>Part (b): Escalating Maintenance Costs [2 Marks]</strong><br>
              - Year 1 Maintenance = ₹25,000.<br>
              - Year 2 Maintenance (+20%): <em>25,000 × 1.20 = ₹30,000</em>.<br>
              - Year 3 Maintenance (+20%): <em>30,000 × 1.20 = ₹36,000</em>.<br>
              Total Maintenance = <em>25,000 + 30,000 + 36,000 = <strong>₹91,000</strong></em>.</p>
            </div>
            <div class="step-box step-4">
              <span class="step-badge">Marking Scheme Breakdown</span>
              <ul>
                <li>Year 1 and Year 2 depreciated values (₹16.2L and ₹14.58L): <strong>[1.5 M]</strong></li>
                <li>Year 3 depreciated value (₹12,39,300): <strong>[1.5 M]</strong></li>
                <li>Maintenance escalation for Year 2 and Year 3 (₹30,000 and ₹36,000): <strong>[1.0 M]</strong></li>
                <li>Sum of maintenance costs (₹91,000): <strong>[1.0 M]</strong></li>
              </ul>
            </div>
            <div class="step-box step-5">
              <span class="step-badge">Answer</span>
              <p>Depreciated Bus Value = <strong>₹12,39,300</strong>; Total Maintenance = <strong>₹91,000</strong>.</p>
            </div>
          </div>
        </div>
      </details>

      <!-- LA 4 -->
      <details class="ans-box" id="la4">
        <summary>LA 4 (5M): Democratic Election Modeling &amp; Geometric Area Distortion (With Marking Scheme)</summary>
        <div class="ans-content">
          <div class="step-container">
            <div class="step-box step-1">
              <span class="step-badge">Question</span>
              <p>(a) In an election between candidate A and candidate B, 15% of registered voters did not vote, and 5% of votes cast were declared invalid. Candidate A secured 55% of the valid votes and won by a majority of 1,710 votes. Find the total number of registered voters.<br>
              (b) If the length of a rectangular park is increased by 20%, by what percentage must the width be decreased so that the total area decreases by 4%?</p>
            </div>
            <div class="step-box step-3">
              <span class="step-badge">Complete Model Solution</span>
              <p><strong>Part (a): Election Voter Turnout &amp; Tally [3 Marks]</strong><br>
              Let total registered voters = <em>V</em>.<br>
              - Voters who cast votes = <em>85%  of  V = 0.85 V</em>.<br>
              - Valid votes = <em>95%  of  0.85 V = 0.95 × 0.85 V = 0.8075 V</em>.<br>
              - Candidate A got 55% of valid votes ⇒ Candidate B got 45% of valid votes.<br>
              - Winning majority = <em>55% - 45% = 10%  of valid votes</em>.<br>
              <code>0.10 × (0.8075 V) = 1,710</code><br>
              <code>0.08075 V = 1,710 ⇒ V = 1,710 / 0.08075 = <strong>21,176.47 ≈ 21,176  voters</strong></em></code>.<br>
              <em>(If majority is 1,615: <em>V = 1615 / 0.08075 = 20,000</em> exactly).</em><br><br>
              <strong>Part (b): Rectangular Area Change [2 Marks]</strong><br>
              Let original dimensions be <em>L</em> and <em>W</em>. Area <em>A = L × W</em>.<br>
              New Length <em>L' = 1.20 L</em>. Required New Area <em>A' = 0.96 A</em>.<br>
              <em>L' × W' = 0.96 (L × W) ⇒ 1.20 L × W' = 0.96 L × W</em>.<br>
              <em>W' = (0.96 / 1.20) W = 0.80 W</em>.<br>
              Decrease in width = <em>(1 - 0.80) × 100% = <strong>20%</strong></em>.</p>
            </div>
            <div class="step-box step-4">
              <span class="step-badge">Marking Scheme Breakdown</span>
              <ul>
                <li>Formulating valid votes <em>0.8075 V</em> and majority gap (10%): <strong>[1.5 M]</strong></li>
                <li>Solving for total voter roll <em>V</em>: <strong>[1.5 M]</strong></li>
                <li>Setting up area equation <em>1.20 × W' = 0.96 W</em>: <strong>[1.0 M]</strong></li>
                <li>Finding width decrease = 20%: <strong>[1.0 M]</strong></li>
              </ul>
            </div>
            <div class="step-box step-5">
              <span class="step-badge">Answer</span>
              <p>(a) Total registered voters ≈ <strong>21,176</strong>.<br>
              (b) Width must decrease by exactly <strong>20%</strong>.</p>
            </div>
          </div>
        </div>
      </details>

      <!-- PART 5.5: COMPETENCY-BASED CASE STUDIES -->
      <h3 class="subheading"><i class="fa-solid fa-briefcase"></i> Part 5.5: Competency-Based Case Studies (Real-World Applications)</h3>

      <!-- CASE STUDY 1 -->
      <details class="ans-box" id="cs1">
        <summary>Case Study 1: E-Commerce Festival Discounts, Dynamic Pricing &amp; GST Billing</summary>
        <div class="ans-content">
          <div class="step-container">
            <div class="step-box step-1">
              <span class="step-badge">Case Context</span>
              <p>During the festive "Diwali Mega Sale", an e-commerce platform lists a premium laptop at a Marked Price (MP) of <strong>₹60,000</strong>. The platform features three distinct promotional tiers:<br>
              - <strong>Tier 1:</strong> Flat 20% platform discount on Marked Price.<br>
              - <strong>Tier 2:</strong> Additional 10% instant bank card discount applied on the discounted price.<br>
              - <strong>Tier 3:</strong> Government GST of 18% charged on the final transaction value.</p>
            </div>
            <div class="step-box step-3">
              <span class="step-badge">Multi-Part Questions &amp; Solutions</span>
              <p><strong>Sub-Question (i):</strong> What is the price of the laptop after the Tier 1 platform discount?<br>
              <em>Solution:</em> Tier 1 Price = 80% of ₹60,000 = <code>0.80 × 60,000 = <strong>₹48,000</strong></code>.<br><br>
              <strong>Sub-Question (ii):</strong> What is the price after applying the Tier 2 bank card discount?<br>
              <em>Solution:</em> Tier 2 Price = 90% of ₹48,000 = <code>0.90 × 48,000 = <strong>₹43,200</strong></code>.<br><br>
              <strong>Sub-Question (iii):</strong> What single equivalent discount percentage do Tier 1 and Tier 2 combine to represent?<br>
              <em>Solution:</em> Net Multiplier = 0.80 × 0.90 = 0.72. Single discount = <code>(1 - 0.72) × 100% = <strong>28%</strong></code> (NOT 30%!).<br><br>
              <strong>Sub-Question (iv):</strong> Calculate the GST amount and the final invoice total charged to the customer.<br>
              <em>Solution:</em> GST = 18% of ₹43,200 = <code>0.18 × 43,200 = <strong>₹7,776</strong></code>.<br>
              Final Invoice Total = <code>₹43,200 + ₹7,776 = <strong>₹50,976</strong></code>.</p>
            </div>
            <div class="step-box step-5">
              <span class="step-badge">Answer</span>
              <p>(i) <strong>₹48,000</strong> | (ii) <strong>₹43,200</strong> | (iii) <strong>28% net discount</strong> | (iv) <strong>GST = ₹7,776, Final Bill = ₹50,976</strong>.</p>
            </div>
          </div>
        </div>
      </details>

      <!-- CASE STUDY 2 -->
      <details class="ans-box" id="cs2">
        <summary>Case Study 2: Green Energy Micro-Financing &amp; Agricultural Yield Compounding</summary>
        <div class="ans-content">
          <div class="step-container">
            <div class="step-box step-1">
              <span class="step-badge">Case Context</span>
              <p>Ramesh, a progressive farmer in Bargarh, Odisha, obtained a micro-finance loan of <strong>₹80,000</strong> from a rural cooperative bank at <strong>6% per annum compound interest</strong> to install a solar-powered irrigation pump. With reliable year-round solar irrigation, his annual paddy harvest jumped from <strong>40 quintals</strong> to <strong>64 quintals</strong> in Year 1, and grew by another <strong>10%</strong> in Year 2.</p>
            </div>
            <div class="step-box step-3">
              <span class="step-badge">Multi-Part Questions &amp; Solutions</span>
              <p><strong>Sub-Question (i):</strong> What was the percentage increase in Ramesh's paddy harvest in Year 1?<br>
              <em>Solution:</em> Increase = 64 - 40 = 24 quintals.<br>
              Percentage Increase = <code>(24 / 40) × 100% = (3 / 5) × 100% = <strong>60%</strong></code>.<br><br>
              <strong>Sub-Question (ii):</strong> What was his harvest in Year 2?<br>
              <em>Solution:</em> Year 2 Harvest = 110% of 64 quintals = <code>1.10 × 64 = <strong>70.4  quintals</strong></code>.<br><br>
              <strong>Sub-Question (iii):</strong> What is the total debt amount Ramesh owes the cooperative bank after 2 years if no repayments were made?<br>
              <em>Solution:</em> Compound Amount <em>A = P(1 + R/100)² = 80,000 × (1.06)² = 80,000 × 1.1236 = <strong>₹89,888</strong></em>.<br><br>
              <strong>Sub-Question (iv):</strong> How much extra interest did compounding add compared to simple interest over these 2 years?<br>
              <em>Solution:</em> SI = (80,000 × 6 × 2) / 100 = ₹9,600.<br>
              CI = ₹89,888 - ₹80,000 = ₹9,888.<br>
              Extra compounding interest = <code>₹9,888 - ₹9,600 = <strong>₹288</strong></code>.</p>
            </div>
            <div class="step-box step-5">
              <span class="step-badge">Answer</span>
              <p>(i) <strong>60% increase</strong> | (ii) <strong>70.4 quintals</strong> | (iii) <strong>₹89,888 total debt</strong> | (iv) <strong>₹288 extra compounding cost</strong>.</p>
            </div>
          </div>
        </div>
      </details>

      <!-- PART 5.6: PREVIOUS YEARS QUESTIONS (PYQS) & PROBABLE QUESTIONS -->
      <h3 class="subheading"><i class="fa-solid fa-clock-rotate-left"></i> Part 5.6: Previous Years Questions (PYQs) &amp; Most Probable Questions</h3>

      <!-- PYQ 1 -->
      <details class="ans-box" id="pyq1">
        <summary>PYQ 1: Milkman Adulteration &amp; Profit Percentage (CBSE Class 8 Term Exam)</summary>
        <div class="ans-content">
          <div class="step-container">
            <div class="step-box step-1">
              <span class="step-badge">Question</span>
              <p>A milkman bought 100 liters of milk at ₹45 per liter. He added 20 liters of water (free of cost) and sold the mixture at ₹50 per liter. Find his profit percentage.</p>
            </div>
            <div class="step-box step-3">
              <span class="step-badge">Solution</span>
              <p>1. Total Cost Price CP = 100 liters × ₹45 = <strong>₹4,500</strong>.<br>
              2. Total mixture volume = 100 + 20 = 120 liters.<br>
              3. Total Selling Price SP = 120 liters × ₹50 = <strong>₹6,000</strong>.<br>
              4. Profit = SP - CP = ₹6,000 - ₹4,500 = ₹1,500.<br>
              5. Profit% = <code>(1,500 / 4,500) × 100% = (1 / 3) × 100% = 33 ⅓% (≈ 33.33%)</code>.</p>
            </div>
            <div class="step-box step-5">
              <span class="step-badge">Answer</span>
              <p>The milkman earned a <strong>profit of 33.33% (or 33 ⅓%)</strong>.</p>
            </div>
          </div>
        </div>
      </details>

      <!-- PYQ 2 -->
      <details class="ans-box" id="pyq2">
        <summary>PYQ 2: Finding Principal when Compound Amount is ₹9,261 in 3 Years @ 5% p.a.</summary>
        <div class="ans-content">
          <div class="step-container">
            <div class="step-box step-1">
              <span class="step-badge">Question</span>
              <p>What principal sum will amount to ₹9,261 in 3 years at 5% per annum compound interest, compounded annually?</p>
            </div>
            <div class="step-box step-3">
              <span class="step-badge">Solution</span>
              <p>Formula: <em>A = P × (1 + R/100)³</em>.<br>
              Given: <em>A = 9,261</em>, <em>R = 5%</em>, <em>n = 3</em>.<br>
              <em>9,261 = P × (1 + 5/100)³ = P × (21/20)³ = P × (9,261 / 8,000)</em>.<br>
              <em>P = 9,261 × (8,000 / 9,261) = <strong>₹8,000</strong></em>.</p>
            </div>
            <div class="step-box step-5">
              <span class="step-badge">Answer</span>
              <p>The principal sum is <strong>₹8,000</strong>.</p>
            </div>
          </div>
        </div>
      </details>

      <!-- PYQ 3 -->
      <details class="ans-box" id="pyq3">
        <summary>PYQ 3: Relative Salary Asymmetry — A's Salary 25% More than B's (Olympiad Challenge)</summary>
        <div class="ans-content">
          <div class="step-container">
            <div class="step-box step-1">
              <span class="step-badge">Question</span>
              <p>If A's salary is 25% more than B's salary, by what percentage is B's salary less than A's salary?</p>
            </div>
            <div class="step-box step-3">
              <span class="step-badge">Solution</span>
              <p>Let B's salary = ₹100.<br>
              Then A's salary = 100 + 25% of 100 = ₹125.<br>
              Difference in salary = ₹125 - ₹100 = ₹25.<br>
              To find how much B is less than A, the base is <strong>A's salary (₹125)</strong>:<br>
              Percentage less = <code>(Difference / A's Salary) × 100% = (25 / 125) × 100% = (1 / 5) × 100% = 20%</code>.<br>
              <em>(Notice it is 20%, NOT 25%!).</em></p>
            </div>
            <div class="step-box step-5">
              <span class="step-badge">Answer</span>
              <p>B's salary is <strong>20% less than A's salary</strong>.</p>
            </div>
          </div>
        </div>
      </details>

      <!-- PYQ 4 -->
      <details class="ans-box" id="pyq4">
        <summary>PYQ 4: Manufacturer Marked Price, Trade Discount &amp; 20% Profit</summary>
        <div class="ans-content">
          <div class="step-container">
            <div class="step-box step-1">
              <span class="step-badge">Question</span>
              <p>A manufacturer marks an article at ₹1,200. He allows a discount of 15% to a retailer and still makes a profit of 20%. What is the cost price for the manufacturer?</p>
            </div>
            <div class="step-box step-3">
              <span class="step-badge">Solution</span>
              <p>1. Marked Price MP = ₹1,200.<br>
              2. Selling Price after 15% discount = <code>1,200 × (1 - 0.15) = 1,200 × 0.85 = ₹1,020</code>.<br>
              3. The manufacturer makes a 20% profit on CP:<br>
              <code>SP = CP × (1 + 0.20) ⇒ 1.20 × CP = 1,020</code>.<br>
              4. <code>CP = 1,020 / 1.20 = 10,200 / 12 = ₹850</code>.</p>
            </div>
            <div class="step-box step-5">
              <span class="step-badge">Answer</span>
              <p>The cost price for the manufacturer is <strong>₹850</strong>.</p>
            </div>
          </div>
        </div>
      </details>

      <!-- PYQ 5 -->
      <details class="ans-box" id="pyq5">
        <summary>PYQ 5: Machine Depreciation Retrograde — Value 2 Years Ago</summary>
        <div class="ans-content">
          <div class="step-container">
            <div class="step-box step-1">
              <span class="step-badge">Question</span>
              <p>The value of a factory machine depreciates at 10% every year. If its present value is ₹1,62,000, what was its purchase value 2 years ago?</p>
            </div>
            <div class="step-box step-3">
              <span class="step-badge">Solution</span>
              <p>Let original value 2 years ago = <em>P</em>.<br>
              Annual depreciation rate = 10% (multiplier = 0.90).<br>
              Present Value = <em>P × (1 - 0.10)² = P × (0.90)² = 0.81 P</em>.<br>
              Given: <em>0.81 P = 1,62,000</em>.<br>
              <em>P = 1,62,000 / 0.81 = 16,200,000 / 81 = <strong>₹2,00,000</strong></em>.</p>
            </div>
            <div class="step-box step-5">
              <span class="step-badge">Answer</span>
              <p>The value of the machine 2 years ago was <strong>₹2,00,000</strong>.</p>
            </div>
          </div>
        </div>
      </details>
    </section>
"""
