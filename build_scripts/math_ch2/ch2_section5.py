# -*- coding: utf-8 -*-
"""
Module: ch2_section5.py
Contains Section 5: Complete Exam Question Bank (27 CBE & Board Models)
Includes:
- 5 Interactive MCQs with button quiz engine, instant feedback & trap explanations
- 5 Assertion & Reasoning Questions
- 6 Short Answer Questions (2M/3M)
- 4 Long Answer Questions (5M) with step-by-step marking schemes
- 2 Competency-Based Case Studies (with 4 sub-questions each = 8 sub-questions)
- 5 Previous Years Questions (PYQs) & Most Probable Exam Models
"""

def get_section_5():
    return """
    <!-- ============================================================ -->
    <!-- SECTION 5: COMPLETE EXAM QUESTION BANK (27 HIGH-YIELD MODELS)-->
    <!-- ============================================================ -->
    <section id="section-5" class="study-section">
      <div class="section-header">
        <span class="section-badge"><i class="fa-solid fa-file-signature"></i> Examination Mastery</span>
        <h2 class="section-title">Complete Exam Question Bank (27 CBE & Board Models)</h2>
        <p class="section-subtitle">
          Exhaustive testing suite aligned with CBSE Competency-Based Education (CBE) and NEP 2020 patterns. Includes instant-evaluation interactive MCQs, Assertion-Reasoning, 2M/3M Short Answers, 5M Long Answers with marking schemes, Case Studies, and PYQs.
        </p>
      </div>

      <!-- Real-Time Quiz Scoreboard -->
      <div class="quiz-scoreboard">
        <div>
          <div class="scoreboard-title"><i class="fa-solid fa-gamepad"></i> Interactive MCQ Self-Assessment Tracker</div>
          <div style="font-size: 0.85rem; color: #94a3b8;">Click options below to test your exam-hall readiness with instant scoring!</div>
        </div>
        <div class="score-badge" id="quizScoreDisplay">Score: 0 / 5</div>
      </div>

      <!-- ======================================================== -->
      <!-- 1. CONCEPTUAL MCQS WITH INTERACTIVE ENGINE -->
      <!-- ======================================================== -->
      <h3 class="topic-title"><i class="fa-solid fa-circle-check"></i> 1. Conceptual Multiple Choice Questions (Interactive)</h3>

      <!-- MCQ 1 -->
      <div class="quiz-card" id="mcq-card-1">
        <div class="quiz-question">
          Q1. What is the simplified numerical value of <span class="math-font">(2⁰ + 3⁰ + 4⁰)²</span>?
        </div>
        <div class="quiz-options">
          <button class="option-btn" onclick="handleMcqChoice(1, 'A', false, 'mcq-card-1')">
            A) 1
          </button>
          <button class="option-btn" onclick="handleMcqChoice(1, 'B', true, 'mcq-card-1')">
            B) 9
          </button>
          <button class="option-btn" onclick="handleMcqChoice(1, 'C', false, 'mcq-card-1')">
            C) 81
          </button>
          <button class="option-btn" onclick="handleMcqChoice(1, 'D', false, 'mcq-card-1')">
            D) 0
          </button>
        </div>
        <div class="quiz-feedback" id="feedback-1">
          <strong>Teacher Explanation & Trap Alert:</strong>
          <br>• <em>The Trap:</em> Careless students often mistake <span class="math-font">a⁰ = 0</span>, getting <span class="math-font">(0 + 0 + 0)² = 0</span>, or they add exponents <span class="math-font">2⁰+3⁰+4⁰ = 9⁰ = 1</span>.
          <br>• <em>Correct Method:</em> By Zero Exponent Law, <span class="math-font">2⁰ = 1</span>, <span class="math-font">3⁰ = 1</span>, and <span class="math-font">4⁰ = 1</span>.
          <br>Inside parentheses: <span class="math-font">1 + 1 + 1 = 3</span>.
          <br>Squaring the sum: <span class="math-font">3² = 3 × 3 = 9</span>!
          <br><strong>Correct Option: B</strong>
        </div>
      </div>

      <!-- MCQ 2 -->
      <div class="quiz-card" id="mcq-card-2">
        <div class="quiz-question">
          Q2. If <span class="math-font">2ˣ⁻¹ + 2ˣ⁺¹ = 320</span>, then what is the value of <span class="math-font">x</span>?
        </div>
        <div class="quiz-options">
          <button class="option-btn" onclick="handleMcqChoice(2, 'A', false, 'mcq-card-2')">
            A) 5
          </button>
          <button class="option-btn" onclick="handleMcqChoice(2, 'B', false, 'mcq-card-2')">
            B) 6
          </button>
          <button class="option-btn" onclick="handleMcqChoice(2, 'C', true, 'mcq-card-2')">
            C) 7
          </button>
          <button class="option-btn" onclick="handleMcqChoice(2, 'D', false, 'mcq-card-2')">
            D) 8
          </button>
        </div>
        <div class="quiz-feedback" id="feedback-2">
          <strong>Teacher Explanation & Trap Alert:</strong>
          <br>• <em>Correct Method:</em> Factor out <span class="math-font">2ˣ</span>:
          <br><span class="math-font">2ˣ × 2⁻¹ + 2ˣ × 2¹ = 320 ⇒ 2ˣ (1/2 + 2) = 320</span>.
          <br><span class="math-font">2ˣ (5/2) = 320 ⇒ 2ˣ = 320 × (2/5) = 64 × 2 = 128</span>.
          <br>Since <span class="math-font">128 = 2⁷</span>, we equate exponents: <span class="math-font">x = 7</span>!
          <br><strong>Correct Option: C</strong>
        </div>
      </div>

      <!-- MCQ 3 -->
      <div class="quiz-card" id="mcq-card-3">
        <div class="quiz-question">
          Q3. Express the decimal number <span class="math-font">0.00000678</span> in standard scientific notation:
        </div>
        <div class="quiz-options">
          <button class="option-btn" onclick="handleMcqChoice(3, 'A', true, 'mcq-card-3')">
            A) 6.78 × 10⁻⁶
          </button>
          <button class="option-btn" onclick="handleMcqChoice(3, 'B', false, 'mcq-card-3')">
            B) 67.8 × 10⁻⁷
          </button>
          <button class="option-btn" onclick="handleMcqChoice(3, 'C', false, 'mcq-card-3')">
            C) 6.78 × 10⁶
          </button>
          <button class="option-btn" onclick="handleMcqChoice(3, 'D', false, 'mcq-card-3')">
            D) 0.678 × 10⁻⁵
          </button>
        </div>
        <div class="quiz-feedback" id="feedback-3">
          <strong>Teacher Explanation & Trap Alert:</strong>
          <br>• <em>The Trap:</em> Standard scientific form strictly requires <span class="math-font">1 ≤ m &lt; 10</span>. Option B has <span class="math-font">m = 67.8</span> (too large), and Option D has <span class="math-font">m = 0.678</span> (less than 1).
          <br>• <em>Correct Method:</em> To place the decimal after the first non-zero digit 6, move the decimal point 6 places to the <strong>right</strong>: exponent is <span class="math-font">–6</span>.
          <br>Hence: <span class="math-font">6.78 × 10⁻⁶</span>.
          <br><strong>Correct Option: A</strong>
        </div>
      </div>

      <!-- MCQ 4 -->
      <div class="quiz-card" id="mcq-card-4">
        <div class="quiz-question">
          Q4. What is the value of <span class="math-font">[ (–1/3)⁻² ]⁻¹</span>?
        </div>
        <div class="quiz-options">
          <button class="option-btn" onclick="handleMcqChoice(4, 'A', false, 'mcq-card-4')">
            A) 9
          </button>
          <button class="option-btn" onclick="handleMcqChoice(4, 'B', false, 'mcq-card-4')">
            B) –9
          </button>
          <button class="option-btn" onclick="handleMcqChoice(4, 'C', true, 'mcq-card-4')">
            C) 1/9
          </button>
          <button class="option-btn" onclick="handleMcqChoice(4, 'D', false, 'mcq-card-4')">
            D) –1/9
          </button>
        </div>
        <div class="quiz-feedback" id="feedback-4">
          <strong>Teacher Explanation & Trap Alert:</strong>
          <br>• <em>Method 1 (Power of Power Law):</em> Multiply exponents first: <span class="math-font">(–2) × (–1) = +2</span>.
          <br>Then evaluate: <span class="math-font">(–1/3)² = (–1/3) × (–1/3) = +1/9</span>!
          <br>• <em>Method 2 (Inside Out):</em> <span class="math-font">(–1/3)⁻² = (–3/1)² = 9</span>. Then <span class="math-font">(9)⁻¹ = 1/9</span>!
          <br><strong>Correct Option: C</strong>
        </div>
      </div>

      <!-- MCQ 5 -->
      <div class="quiz-card" id="mcq-card-5">
        <div class="quiz-question">
          Q5. Which of the following two astronomical numbers is greater: <span class="math-font">2³⁰⁰</span> or <span class="math-font">3²⁰⁰</span>?
        </div>
        <div class="quiz-options">
          <button class="option-btn" onclick="handleMcqChoice(5, 'A', false, 'mcq-card-5')">
            A) 2³⁰⁰
          </button>
          <button class="option-btn" onclick="handleMcqChoice(5, 'B', true, 'mcq-card-5')">
            B) 3²⁰⁰
          </button>
          <button class="option-btn" onclick="handleMcqChoice(5, 'C', false, 'mcq-card-5')">
            C) Both are equal
          </button>
          <button class="option-btn" onclick="handleMcqChoice(5, 'D', false, 'mcq-card-5')">
            D) Cannot be compared without a calculator
          </button>
        </div>
        <div class="quiz-feedback" id="feedback-5">
          <strong>Teacher Explanation & Trap Alert:</strong>
          <br>• <em>The Trap:</em> Students see exponent 300 &gt; 200 and assume <span class="math-font">2³⁰⁰</span> must be greater.
          <br>• <em>Correct Method:</em> Make the exponents equal by finding the HCF of 300 and 200, which is 100!
          <br><span class="math-font">2³⁰⁰ = (2³)¹⁰⁰ = 8¹⁰⁰</span>.
          <br><span class="math-font">3²⁰⁰ = (3²)¹⁰⁰ = 9¹⁰⁰</span>.
          <br>Now compare bases: since <span class="math-font">9 &gt; 8</span>, raising both to power 100 preserves the inequality: <span class="math-font">9¹⁰⁰ &gt; 8¹⁰⁰ ⇒ 3²⁰⁰ &gt; 2³⁰⁰</span>!
          <br><strong>Correct Option: B</strong>
        </div>
      </div>

      <!-- ======================================================== -->
      <!-- 2. ASSERTION & REASONING QUESTIONS -->
      <!-- ======================================================== -->
      <h3 class="topic-title"><i class="fa-solid fa-scale-balanced"></i> 2. Assertion & Reasoning Questions (CBSE Pattern)</h3>
      <p>
        Directions: In the following questions, two statements are given — one labelled <strong>Assertion (A)</strong> and the other labelled <strong>Reason (R)</strong>. Choose the correct option:
        <br><strong>(A)</strong> Both (A) and (R) are true, and (R) is the correct explanation of (A).
        <br><strong>(B)</strong> Both (A) and (R) are true, but (R) is NOT the correct explanation of (A).
        <br><strong>(C)</strong> (A) is true, but (R) is false.
        <br><strong>(D)</strong> (A) is false, but (R) is true.
      </p>

      <!-- AR 1 -->
      <details class="ans-box">
        <summary>
          <span>Assertion & Reasoning 1: Negative Exponent Reciprocal Relation</span>
          <span class="ans-badge"><i class="fa-solid fa-chevron-down"></i> Solution</span>
        </summary>
        <div class="ans-content">
          <p><strong>Assertion (A):</strong> For any non-zero integer <span class="math-font">a</span>, <span class="math-font">a⁻ᵐ = 1 / aᵐ</span>.</p>
          <p><strong>Reason (R):</strong> The multiplicative inverse of <span class="math-font">aᵐ</span> is <span class="math-font">a⁻ᵐ</span>, because <span class="math-font">aᵐ × a⁻ᵐ = aᵐ⁺⁽⁻ᵐ⁾ = a⁰ = 1</span>.</p>
          <div class="step-box">
            <div class="step-label"><i class="fa-solid fa-square-check"></i> Evaluation & Verdict</div>
            <p><strong>Answer: (A) Both (A) and (R) are true, and (R) is the correct explanation of (A).</strong>
              <br><em>Justification:</em> Two numbers are multiplicative inverses when their product is 1. Since <span class="math-font">aᵐ × a⁻ᵐ = a⁰ = 1</span>, <span class="math-font">a⁻ᵐ</span> is indeed the multiplicative inverse (reciprocal) of <span class="math-font">aᵐ</span>, which proves why <span class="math-font">a⁻ᵐ = 1 / aᵐ</span>.
            </p>
          </div>
        </div>
      </details>

      <!-- AR 2 -->
      <details class="ans-box">
        <summary>
          <span>Assertion & Reasoning 2: Parity Sum of Negative One Powers</span>
          <span class="ans-badge"><i class="fa-solid fa-chevron-down"></i> Solution</span>
        </summary>
        <div class="ans-content">
          <p><strong>Assertion (A):</strong> The value of <span class="math-font">(–1)¹⁰⁰ + (–1)¹⁰¹</span> equals <span class="math-font">0</span>.</p>
          <p><strong>Reason (R):</strong> For any integer <span class="math-font">n</span>, <span class="math-font">(–1)ⁿ = +1</span> when <span class="math-font">n</span> is an even number, and <span class="math-font">(–1)ⁿ = –1</span> when <span class="math-font">n</span> is an odd number.</p>
          <div class="step-box">
            <div class="step-label"><i class="fa-solid fa-square-check"></i> Evaluation & Verdict</div>
            <p><strong>Answer: (A) Both (A) and (R) are true, and (R) is the correct explanation of (A).</strong>
              <br><em>Justification:</em> 100 is even, so <span class="math-font">(–1)¹⁰⁰ = +1</span>. 101 is odd, so <span class="math-font">(–1)¹⁰¹ = –1</span>. Their sum is <span class="math-font">(+1) + (–1) = 0</span>. The Reason directly explains why the Assertion holds.
            </p>
          </div>
        </div>
      </details>

      <!-- AR 3 -->
      <details class="ans-box">
        <summary>
          <span>Assertion & Reasoning 3: Adding Exponents with Different Bases Trap</span>
          <span class="ans-badge"><i class="fa-solid fa-chevron-down"></i> Solution</span>
        </summary>
        <div class="ans-content">
          <p><strong>Assertion (A):</strong> <span class="math-font">2³ × 3² = 6⁵</span>.</p>
          <p><strong>Reason (R):</strong> When multiplying two numbers, bases are multiplied and exponents are added.</p>
          <div class="step-box">
            <div class="step-label"><i class="fa-solid fa-square-check"></i> Evaluation & Verdict</div>
            <p><strong>Answer: Both (A) and (R) are completely FALSE.</strong> (In standard CBSE options: (C) / (D) depending on phrasing, but here Assertion is false and Reason is a false rule).
              <br><em>Justification:</em> <span class="math-font">2³ × 3² = 8 × 9 = 72</span>, whereas <span class="math-font">6⁵ = 7,776</span>. They are not equal! You can only add exponents when bases are IDENTICAL (<span class="math-font">aᵐ × aⁿ = aᵐ⁺ⁿ</span>).
            </p>
          </div>
        </div>
      </details>

      <!-- AR 4 -->
      <details class="ans-box">
        <summary>
          <span>Assertion & Reasoning 4: Why Zero Raised to Zero is Undefined</span>
          <span class="ans-badge"><i class="fa-solid fa-chevron-down"></i> Solution</span>
        </summary>
        <div class="ans-content">
          <p><strong>Assertion (A):</strong> The expression <span class="math-font">0⁰</span> (zero raised to the power zero) is undefined in arithmetic.</p>
          <p><strong>Reason (R):</strong> Applying the quotient rule <span class="math-font">a⁰ = aⁿ ÷ aⁿ</span> when <span class="math-font">a = 0</span> yields <span class="math-font">0 / 0</span>, which is an indeterminate form with no unique value.</p>
          <div class="step-box">
            <div class="step-label"><i class="fa-solid fa-square-check"></i> Evaluation & Verdict</div>
            <p><strong>Answer: (A) Both (A) and (R) are true, and (R) is the correct explanation of (A).</strong>
              <br><em>Justification:</em> Division by zero is undefined. Hence, the identity <span class="math-font">a⁰ = 1</span> holds universally for all real numbers except zero.
            </p>
          </div>
        </div>
      </details>

      <!-- AR 5 -->
      <details class="ans-box">
        <summary>
          <span>Assertion & Reasoning 5: Standard Scientific Form Constraint</span>
          <span class="ans-badge"><i class="fa-solid fa-chevron-down"></i> Solution</span>
        </summary>
        <div class="ans-content">
          <p><strong>Assertion (A):</strong> The distance from Earth to Sun, 149,600,000 km, is written in scientific notation as <span class="math-font">1.496 × 10⁸ km</span>.</p>
          <p><strong>Reason (R):</strong> A number in standard scientific form <span class="math-font">m × 10ᵏ</span> requires that <span class="math-font">1 ≤ m &lt; 10</span>, where <span class="math-font">k</span> is an integer.</p>
          <div class="step-box">
            <div class="step-label"><i class="fa-solid fa-square-check"></i> Evaluation & Verdict</div>
            <p><strong>Answer: (A) Both (A) and (R) are true, and (R) is the correct explanation of (A).</strong>
              <br><em>Justification:</em> Shifting the decimal 8 places left yields <span class="math-font">1.496</span>, which satisfies <span class="math-font">1 ≤ 1.496 &lt; 10</span>.
            </p>
          </div>
        </div>
      </details>

      <!-- ======================================================== -->
      <!-- 3. SHORT ANSWER QUESTIONS (2M / 3M) -->
      <!-- ======================================================== -->
      <h3 class="topic-title"><i class="fa-solid fa-pen-ruler"></i> 3. Short Answer Questions (2-Mark & 3-Mark Models)</h3>

      <!-- SA 1 -->
      <details class="ans-box">
        <summary>
          <span>Short Answer 1 (2M): Find x if (5/3)⁻⁵ × (5/3)⁻¹¹ = (5/3)⁸ˣ</span>
          <span class="ans-badge"><i class="fa-solid fa-chevron-down"></i> Solution</span>
        </summary>
        <div class="ans-content">
          <div class="step-box">
            <div class="step-label"><i class="fa-solid fa-bullseye"></i> Step-by-Step Model Answer (2 Marks)</div>
            <p><strong>Step 1:</strong> Apply Product Law on LHS: <span class="math-font">aᵐ × aⁿ = aᵐ⁺ⁿ</span>.
              <br><span class="math-font">((5/3))^{-5 + (-11)} = ((5/3))^{-16}</span>. [1 Mark]
            </p>
            <p><strong>Step 2:</strong> Equate LHS and RHS:
              <br><span class="math-font">((5/3))^{-16} = ((5/3))^{8x}</span>.
              <br>Since the bases are equal and non-zero, equate exponents:
              <br><span class="math-font">8x = -16 ⇒ x = (-16/8) = -2</span>. [1 Mark]
            </p>
            <p><strong>Final Answer:</strong> <span class="math-font">x = –2</span>.</p>
          </div>
        </div>
      </details>

      <!-- SA 2 -->
      <details class="ans-box">
        <summary>
          <span>Short Answer 2 (2M): By What Number Should (–6)⁻¹ Be Multiplied to Get 9⁻¹?</span>
          <span class="ans-badge"><i class="fa-solid fa-chevron-down"></i> Solution</span>
        </summary>
        <div class="ans-content">
          <div class="step-box">
            <div class="step-label"><i class="fa-solid fa-bullseye"></i> Step-by-Step Model Answer (2 Marks)</div>
            <p><strong>Step 1:</strong> Let the required unknown multiplier be <span class="math-font">x</span>.
              <br>According to question: <span class="math-font">(–6)⁻¹ × x = 9⁻¹</span>. [0.5 Mark]
            </p>
            <p><strong>Step 2:</strong> Convert negative exponents to fractions using <span class="math-font">a⁻¹ = 1/a</span>:
              <br><span class="math-font">-\frac{1}{6} × x = (1/9)</span>. [0.5 Mark]
            </p>
            <p><strong>Step 3:</strong> Solve for <span class="math-font">x</span>:
              <br><span class="math-font">x = (1/9) ÷ (-\frac{1}{6}) = (1/9) × (–6) = -(6/9) = -\frac{2}{3}</span>. [1 Mark]
            </p>
            <p><strong>Final Answer:</strong> The number is <strong>–2/3</strong>.</p>
          </div>
        </div>
      </details>

      <!-- SA 3 -->
      <details class="ans-box">
        <summary>
          <span>Short Answer 3 (3M): Simplify (25 × t⁻⁴) / (5⁻³ × 10 × t⁻⁸) (t ≠ 0)</span>
          <span class="ans-badge"><i class="fa-solid fa-chevron-down"></i> Solution</span>
        </summary>
        <div class="ans-content">
          <div class="step-box">
            <div class="step-label"><i class="fa-solid fa-bullseye"></i> Step-by-Step Model Answer (3 Marks)</div>
            <p><strong>Step 1:</strong> Express all composite numbers in powers of prime factors (5 and 2):
              <br><span class="math-font">25 = 5²</span> and <span class="math-font">10 = 2 × 5¹</span>. [1 Mark]
            </p>
            <p><strong>Step 2:</strong> Substitute into fraction:
              <br><span class="math-font">\frac{5² × t⁻⁴}{5⁻³ × (2 × 5¹) × t⁻⁸} = \frac{5² × t⁻⁴}{2 × 5⁻³⁺¹ × t⁻⁸} = (5² × t⁻⁴) / (2 × 5⁻² × t⁻⁸)</span>. [1 Mark]
            </p>
            <p><strong>Step 3:</strong> Apply Quotient Law for powers of 5 and powers of <span class="math-font">t</span>:
              <br>Powers of 5: <span class="math-font">5² ÷ 5⁻² = 5²⁻⁽⁻²⁾ = 5⁴ = 625</span>.
              <br>Powers of <span class="math-font">t</span>: <span class="math-font">t⁻⁴ ÷ t⁻⁸ = t⁻⁴⁻⁽⁻⁸⁾ = t⁴</span>.
              <br>Denominator contains constant factor 2.
              <br>Hence, result = <span class="math-font">(625 t⁴ / 2)</span> (or <span class="math-font">312.5 t⁴</span>). [1 Mark]
            </p>
            <p><strong>Final Answer:</strong> <span class="math-font">(625 t⁴ / 2)</span>.</p>
          </div>
        </div>
      </details>

      <!-- SA 4 -->
      <details class="ans-box">
        <summary>
          <span>Short Answer 4 (2M): Evaluate [ (1/3)⁻¹ – (1/4)⁻¹ ]⁻¹</span>
          <span class="ans-badge"><i class="fa-solid fa-chevron-down"></i> Solution</span>
        </summary>
        <div class="ans-content">
          <div class="step-box">
            <div class="step-label"><i class="fa-solid fa-bullseye"></i> Step-by-Step Model Answer (2 Marks)</div>
            <p><strong>Step 1:</strong> Evaluate inside expressions using reciprocal rule <span class="math-font">(1/a)⁻¹ = a</span>:
              <br><span class="math-font">(1/3)⁻¹ = 3</span> and <span class="math-font">(1/4)⁻¹ = 4</span>. [1 Mark]
            </p>
            <p><strong>Step 2:</strong> Perform subtraction inside brackets:
              <br><span class="math-font">3 – 4 = –1</span>.
            </p>
            <p><strong>Step 3:</strong> Apply outer negative exponent:
              <br><span class="math-font">(–1)⁻¹ = 1 / (-1) = –1</span>. [1 Mark]
            </p>
            <p><strong>Final Answer:</strong> <strong>–1</strong>.</p>
          </div>
        </div>
      </details>

      <!-- SA 5 -->
      <details class="ans-box">
        <summary>
          <span>Short Answer 5 (3M): Compare Diameter of Sun (1.4 × 10⁹ m) with Earth (1.2756 × 10⁷ m)</span>
          <span class="ans-badge"><i class="fa-solid fa-chevron-down"></i> Solution</span>
        </summary>
        <div class="ans-content">
          <div class="step-box">
            <div class="step-label"><i class="fa-solid fa-bullseye"></i> Step-by-Step Model Answer (3 Marks)</div>
            <p><strong>Step 1:</strong> Identify given diameters:
              <br>Diameter of Sun <span class="math-font">Dₛ = 1.4 × 10⁹ m</span>.
              <br>Diameter of Earth <span class="math-font">Dₑ = 1.2756 × 10⁷ m ≈ 1.3 × 10⁷ m</span>. [1 Mark]
            </p>
            <p><strong>Step 2:</strong> Set up the ratio <span class="math-font">Dₛ / Dₑ</span>:
              <br><span class="math-font">Ratio = (1.4 × 10⁹) / (1.2756 × 10⁷) = ((1.4 / 1.2756)) × 10⁹⁻⁷ = 1.0975 × 10² ≈ 109.75</span>. [1.5 Marks]
            </p>
            <p><strong>Step 3:</strong> Round off to meaningful whole number comparison:
              <br><span class="math-font">109.75 ≈ 100 to }110 times}</span>. [0.5 Mark]
            </p>
            <p><strong>Final Answer:</strong> The diameter of the Sun is approximately <strong>109 to 110 times larger</strong> than the diameter of the Earth.</p>
          </div>
        </div>
      </details>

      <!-- SA 6 -->
      <details class="ans-box">
        <summary>
          <span>Short Answer 6 (2M): Find m if (–3)ᵐ⁺¹ × (–3)⁵ = (–3)⁷</span>
          <span class="ans-badge"><i class="fa-solid fa-chevron-down"></i> Solution</span>
        </summary>
        <div class="ans-content">
          <div class="step-box">
            <div class="step-label"><i class="fa-solid fa-bullseye"></i> Step-by-Step Model Answer (2 Marks)</div>
            <p><strong>Step 1:</strong> Apply Product Law on LHS:
              <br><span class="math-font">(–3)⁽ᵐ⁺¹⁾⁺⁵ = (–3)ᵐ⁺⁶</span>. [1 Mark]
            </p>
            <p><strong>Step 2:</strong> Equate with RHS:
              <br><span class="math-font">(–3)ᵐ⁺⁶ = (–3)⁷</span>.
              <br>Equating exponents: <span class="math-font">m + 6 = 7 ⇒ m = 7 – 6 = 1</span>. [1 Mark]
            </p>
            <p><strong>Final Answer:</strong> <span class="math-font">m = 1</span>.</p>
          </div>
        </div>
      </details>

      <!-- ======================================================== -->
      <!-- 4. LONG ANSWER QUESTIONS (5-MARK CBSE TOYS) -->
      <!-- ======================================================== -->
      <h3 class="topic-title"><i class="fa-solid fa-award"></i> 4. Long Answer Questions (5-Mark Comprehensive Models with Marking Schemes)</h3>

      <!-- LA 1 -->
      <details class="ans-box">
        <summary>
          <span>Long Answer 1 (5M): Simplify (3⁻⁵ × 10⁻⁵ × 125) / (5⁻⁷ × 6⁻⁵) with CBSE Marking Scheme</span>
          <span class="ans-badge"><i class="fa-solid fa-chevron-down"></i> Solution</span>
        </summary>
        <div class="ans-content">
          <div class="step-box">
            <div class="step-label"><i class="fa-solid fa-clipboard-list"></i> Official CBSE Marking Rubric (5 Marks Total)</div>
            <ul>
              <li>Decompose all composite bases (10, 125, 6) into prime factors: <strong>1.5 Marks</strong></li>
              <li>Apply Power of a Product Law to distribute exponents: <strong>1.0 Mark</strong></li>
              <li>Group identical bases together in numerator and denominator: <strong>1.0 Mark</strong></li>
              <li>Apply Quotient Law <span class="math-font">aᵐ ÷ aⁿ = aᵐ⁻ⁿ</span>: <strong>1.0 Mark</strong></li>
              <li>Compute final correct integer: <strong>0.5 Mark</strong></li>
            </ul>
          </div>
          <div class="step-box">
            <div class="step-label"><i class="fa-solid fa-calculator"></i> Step-by-Step Execution</div>
            <p><strong>Step 1 (Prime Decomposition):</strong>
              <br><span class="math-font">10 = 2 × 5 ⇒ 10⁻⁵ = (2 × 5)⁻⁵ = 2⁻⁵ × 5⁻⁵</span>
              <br><span class="math-font">125 = 5³</span>
              <br><span class="math-font">6 = 2 × 3 ⇒ 6⁻⁵ = (2 × 3)⁻⁵ = 2⁻⁵ × 3⁻⁵</span>
            </p>
            <p><strong>Step 2 (Substitute into Expression):</strong>
              <br><span class="math-font">Numerator = 3⁻⁵ × (2⁻⁵ × 5⁻⁵) × 5³ = 2⁻⁵ × 3⁻⁵ × 5⁻⁵⁺³ = 2⁻⁵ × 3⁻⁵ × 5⁻²</span>.
              <br><span class="math-font">Denominator = 5⁻⁷ × (2⁻⁵ × 3⁻⁵) = 2⁻⁵ × 3⁻⁵ × 5⁻⁷</span>.
            </p>
            <p><strong>Step 3 (Divide Like Bases):</strong>
              <br><span class="math-font">\frac{2⁻⁵ × 3⁻⁵ × 5⁻²}{2⁻⁵ × 3⁻⁵ × 5⁻⁷} = 2⁻⁵⁻⁽⁻⁵⁾ × 3⁻⁵⁻⁽⁻⁵⁾ × 5⁻²⁻⁽⁻⁷⁾</span>.
              <br><span class="math-font">= 2⁰ × 3⁰ × 5⁻²⁺⁷ = 1 × 1 × 5⁵ = 5⁵</span>.
            </p>
            <p><strong>Step 4 (Final Evaluation):</strong>
              <br><span class="math-font">5⁵ = 5 × 5 × 5 × 5 × 5 = 3,125</span>.
            </p>
          </div>
          <p><strong>Final Answer:</strong> <strong>5⁵ = 3,125</strong>.</p>
        </div>
      </details>

      <!-- LA 2 -->
      <details class="ans-box">
        <summary>
          <span>Long Answer 2 (5M): If 2ˣ = 3ʸ = 6⁻ᶻ, Prove that 1/x + 1/y + 1/z = 0 (Topper Challenge)</span>
          <span class="ans-badge"><i class="fa-solid fa-chevron-down"></i> Solution</span>
        </summary>
        <div class="ans-content">
          <div class="step-box">
            <div class="step-label"><i class="fa-solid fa-clipboard-list"></i> Official Marking Rubric (5 Marks Total)</div>
            <ul>
              <li>Introduce auxiliary constant <span class="math-font">k</span>: <strong>1.0 Mark</strong></li>
              <li>Express 2, 3, and 6 in terms of fractional powers of <span class="math-font">k</span>: <strong>1.5 Marks</strong></li>
              <li>Formulate fundamental multiplicative relationship <span class="math-font">2 × 3 = 6</span>: <strong>1.0 Mark</strong></li>
              <li>Apply Product Law to add exponents: <strong>1.0 Mark</strong></li>
              <li>Conclude <span class="math-font">1/x + 1/y + 1/z = 0</span>: <strong>0.5 Mark</strong></li>
            </ul>
          </div>
          <div class="step-box">
            <div class="step-label"><i class="fa-solid fa-calculator"></i> Step-by-Step Proof</div>
            <p><strong>Step 1:</strong> Let <span class="math-font">2ˣ = 3ʸ = 6⁻ᶻ = k</span> (where <span class="math-font">k ≠ 0, k ≠ 1</span>).</p>
            <p><strong>Step 2:</strong> Invert each power:
              <br><span class="math-font">2ˣ = k ⇒ 2 = k^{1/x}</span>
              <br><span class="math-font">3ʸ = k ⇒ 3 = k^{1/y}</span>
              <br><span class="math-font">6⁻ᶻ = k ⇒ 6 = k^{-1/z}</span>
            </p>
            <p><strong>Step 3:</strong> We know the elementary arithmetic identity:
              <br><span class="math-font">2 × 3 = 6</span>.
            </p>
            <p><strong>Step 4:</strong> Substitute the expressions in terms of <span class="math-font">k</span>:
              <br><span class="math-font">k^{1/x} × k^{1/y} = k^{-1/z}</span>.
              <br>By Product Law:
              <br><span class="math-font">k^{1/x + 1/y} = k^{-1/z}</span>.
            </p>
            <p><strong>Step 5:</strong> Equating exponents on identical base <span class="math-font">k</span>:
              <br><span class="math-font">(1/x) + (1/y) = -(1/z) ⇒ (1/x) + (1/y) + (1/z) = 0</span>.
              <br><strong>Hence Proved!</strong>
            </p>
          </div>
        </div>
      </details>

      <!-- LA 3 -->
      <details class="ans-box">
        <summary>
          <span>Long Answer 3 (5M): Paper Fold Thickness Calculation at Fold 20 vs Building Height</span>
          <span class="ans-badge"><i class="fa-solid fa-chevron-down"></i> Solution</span>
        </summary>
        <div class="ans-content">
          <div class="step-box">
            <div class="step-label"><i class="fa-solid fa-clipboard-list"></i> Marking Rubric (5 Marks Total)</div>
            <ul>
              <li>Formula setup <span class="math-font">T = 0.001 × 2²⁰ cm</span>: <strong>1.0 Mark</strong></li>
              <li>Accurate calculation of <span class="math-font">2²⁰ = 10,48,576</span>: <strong>1.0 Mark</strong></li>
              <li>Unit conversion from centimetres to metres: <strong>1.0 Mark</strong></li>
              <li>Comparison with 3-storey building height (~10 m): <strong>1.0 Mark</strong></li>
              <li>Percentage error calculation of approximation: <strong>1.0 Mark</strong></li>
            </ul>
          </div>
          <div class="step-box">
            <div class="step-label"><i class="fa-solid fa-calculator"></i> Step-by-Step Execution</div>
            <p><strong>1. Formula:</strong> Initial thickness = <span class="math-font">0.001 cm</span>.
              <br>After 20 folds: <span class="math-font">T = 0.001 × 2²⁰ cm</span>.
            </p>
            <p><strong>2. Evaluate 2²⁰:</strong>
              <br><span class="math-font">2²⁰ = (2¹⁰)² = 1024² = 10,48,576</span>.
            </p>
            <p><strong>3. Calculate Thickness in Metres:</strong>
              <br><span class="math-font">T = 0.001 × 10,48,576 cm = 1,048.576 cm</span>.
              <br>Convert to metres (<span class="math-font">÷ 100</span>):
              <br><span class="math-font">T = 10.48576 m</span>.
            </p>
            <p><strong>4. Comparison:</strong> A standard building storey is roughly 3.3 m tall. A 3-storey building is <span class="math-font">3 × 3.3 ≈ 10 m</span> tall. The folded paper stack of 10.486 m matches the height of a 3-storey school building!
            </p>
            <p><strong>5. Percentage Error:</strong>
              <br><span class="math-font">Absolute Error = |10.48576 – 10| = 0.48576 m</span>.
              <br><span class="math-font">Percentage Error = (0.48576 / 10.48576) × 100% ≈ 4.63%</span>.
            </p>
          </div>
          <p><strong>Final Answer:</strong> Exact thickness is <strong>10.486 m</strong>, with an estimation error of under <strong>4.7%</strong>.</p>
        </div>
      </details>

      <!-- LA 4 -->
      <details class="ans-box">
        <summary>
          <span>Long Answer 4 (5M): Light-Year Distance in Kilometres & Solar Travel Time to Earth</span>
          <span class="ans-badge"><i class="fa-solid fa-chevron-down"></i> Solution</span>
        </summary>
        <div class="ans-content">
          <div class="step-box">
            <div class="step-label"><i class="fa-solid fa-clipboard-list"></i> Marking Rubric (5 Marks Total)</div>
            <ul>
              <li>Convert 1 Julian year (365.25 days) to seconds in scientific notation: <strong>1.5 Marks</strong></li>
              <li>Calculate 1 light year in km in standard form <span class="math-font">m × 10ᵏ</span>: <strong>1.5 Marks</strong></li>
              <li>Set up solar travel time to Earth (<span class="math-font">t = D / c</span>): <strong>1.0 Mark</strong></li>
              <li>Convert time to minutes and seconds: <strong>1.0 Mark</strong></li>
            </ul>
          </div>
          <div class="step-box">
            <div class="step-label"><i class="fa-solid fa-calculator"></i> Step-by-Step Execution</div>
            <p><strong>Part A: Calculating 1 Light Year:</strong>
              <br>Speed of light <span class="math-font">c = 3.0 × 10⁸ m/s = 3.0 × 10⁵ km/s</span>.
              <br>Seconds in 1 year = <span class="math-font">365.25 × 24 × 3600 = 3,15,57,600 s = 3.15576 × 10⁷ s</span>.
              <br>Distance = <span class="math-font">Speed × Time = (3.0 × 10⁵ km/s) × (3.15576 × 10⁷ s)</span>.
              <br><span class="math-font">= 9.46728 × 10⁵⁺⁷ = 9.46728 × 10¹² km</span> (approx. <strong>9.47 trillion km</strong>).
            </p>
            <p><strong>Part B: Solar Travel Time to Earth:</strong>
              <br>Distance Sun to Earth = <span class="math-font">1.496 × 10¹¹ m</span>.
              <br><span class="math-font">Time t = (1.496 × 10¹¹ m) / (3.0 × 10⁸ m/s) = ((1.496 / 3.0)) × 10¹¹⁻⁸ = 0.49867 × 10³ s = 498.67 seconds</span>.
              <br>Convert to minutes:
              <br><span class="math-font">498.67 ÷ 60 = 8 minutes and } 18.67 seconds}</span> (approx. <strong>8 minutes 19 seconds</strong>).
            </p>
          </div>
          <p><strong>Final Answer:</strong> 1 light year = <strong>9.467 × 10¹² km</strong>; Sunlight reaches Earth in approximately <strong>8 minutes 19 seconds</strong>.</p>
        </div>
      </details>

      <!-- ======================================================== -->
      <!-- 5. COMPETENCY-BASED CASE STUDIES -->
      <!-- ======================================================== -->
      <h3 class="topic-title"><i class="fa-solid fa-briefcase"></i> 5. Competency-Based Real-World Case Studies</h3>

      <!-- Case Study 1 -->
      <div class="concept-card" style="margin-bottom: 2rem; background: #f0f9ff; border-left: 5px solid #0284c7;">
        <h4 class="subtopic-title" style="margin-top:0; color:#0369a1;">
          <i class="fa-solid fa-satellite"></i> Case Study 1: The ISRO Deep Space Odyssey & Telemetry Transmission
        </h4>
        <p>
          ISRO (Indian Space Research Organisation) tracks interplanetary space probes using deep space antennas in Byalalu, Karnataka. In mission control, radio signals travel at the speed of light (<span class="math-font">3.0 × 10⁸ m/s = 3.0 × 10⁵ km/s</span>). The average distance between Earth and the Moon is <span class="math-font">3,84,400 km</span>. During a Mars mission, the closest distance between Earth and Mars is <span class="math-font">5.46 × 10⁷ km</span>. Answer the following four questions:
        </p>

        <details class="ans-box">
          <summary>
            <span>Sub-Q 1 (1M): Express Earth-Moon Distance in Metres in Standard Form</span>
            <span class="ans-badge"><i class="fa-solid fa-chevron-down"></i> Solution</span>
          </summary>
          <div class="ans-content">
            <p><span class="math-font">3,84,400 km = 3,84,400 × 10³ m = 38,44,00,000 m = 3.844 × 10⁸ m</span>.</p>
          </div>
        </details>

        <details class="ans-box">
          <summary>
            <span>Sub-Q 2 (1M): How Many Times Farther is Mars than the Moon at Closest Approach?</span>
            <span class="ans-badge"><i class="fa-solid fa-chevron-down"></i> Solution</span>
          </summary>
          <div class="ans-content">
            <p><span class="math-font">Ratio = (5.46 × 10⁷ km) / (3.844 × 10⁵ km) = ((5.46 / 3.844)) × 10⁷⁻⁵ = 1.42 × 10² = 142</span> times farther!</p>
          </div>
        </details>

        <details class="ans-box">
          <summary>
            <span>Sub-Q 3 (2M): Radio Signal Transmission Delay to Mars</span>
            <span class="ans-badge"><i class="fa-solid fa-chevron-down"></i> Solution</span>
          </summary>
          <div class="ans-content">
            <p><span class="math-font">Time = \frac{Distance}{Speed} = (5.46 × 10⁷ km) / (3.0 × 10⁵ km/s) = ((5.46 / 3.0)) × 10⁷⁻⁵ = 1.82 × 10² = 182 seconds}</span>.
              <br>In minutes: <span class="math-font">182 / 60 = 3 minutes and } 2 seconds}</span>.
            </p>
          </div>
        </details>

        <details class="ans-box">
          <summary>
            <span>Sub-Q 4 (1M): Radio Signal Round-Trip (Two-Way Communication)</span>
            <span class="ans-badge"><i class="fa-solid fa-chevron-down"></i> Solution</span>
          </summary>
          <div class="ans-content">
            <p>A round-trip command takes double the one-way time: <span class="math-font">182 × 2 = 364 seconds} = 6.07 minutes}</span> (approx. 6 minutes 4 seconds).</p>
          </div>
        </details>
      </div>

      <!-- Case Study 2 -->
      <div class="concept-card" style="margin-bottom: 2rem; background: #f0fdfa; border-left: 5px solid #0d9488;">
        <h4 class="subtopic-title" style="margin-top:0; color:#0f766e;">
          <i class="fa-solid fa-bacterium"></i> Case Study 2: Microbiology Lab & Exponential Bacterial Culture
        </h4>
        <p>
          In a high school biology laboratory, students place a sample containing <span class="math-font">100 bacteria</span> (<span class="math-font">10²</span>) into a nutrient-rich warm agar petri dish. The bacteria undergo binary fission, doubling their population every 20 minutes under ideal conditions. Answer the following four questions:
        </p>

        <details class="ans-box">
          <summary>
            <span>Sub-Q 1 (1M): General Formula for Bacterial Population After n Doubling Periods</span>
            <span class="ans-badge"><i class="fa-solid fa-chevron-down"></i> Solution</span>
          </summary>
          <div class="ans-content">
            <p><span class="math-font">P(n) = 100 × 2ⁿ = 10² × 2ⁿ</span>, where <span class="math-font">n</span> is the number of 20-minute periods elapsed.</p>
          </div>
        </details>

        <details class="ans-box">
          <summary>
            <span>Sub-Q 2 (1M): Bacterial Population After Exactly 1 Hour</span>
            <span class="ans-badge"><i class="fa-solid fa-chevron-down"></i> Solution</span>
          </summary>
          <div class="ans-content">
            <p>1 hour has <span class="math-font">60 / 20 = 3</span> doubling periods (<span class="math-font">n = 3</span>).
              <br><span class="math-font">P(3) = 100 × 2³ = 100 × 8 = 800 bacteria}</span>.
            </p>
          </div>
        </details>

        <details class="ans-box">
          <summary>
            <span>Sub-Q 3 (2M): Bacterial Population After 5 Hours in Scientific Standard Notation</span>
            <span class="ans-badge"><i class="fa-solid fa-chevron-down"></i> Solution</span>
          </summary>
          <div class="ans-content">
            <p>5 hours has <span class="math-font">5 × (60 / 20) = 5 × 3 = 15</span> doubling periods (<span class="math-font">n = 15</span>).
              <br><span class="math-font">P(15) = 100 × 2¹⁵ = 100 × 32,768 = 32,76,800 bacteria}</span>.
              <br>In standard scientific form: <span class="math-font">3.2768 × 10⁶ bacteria</span> (approx. 3.28 million!).
            </p>
          </div>
        </details>

        <details class="ans-box">
          <summary>
            <span>Sub-Q 4 (1M): Colony Population Under Antibiotic Decay</span>
            <span class="ans-badge"><i class="fa-solid fa-chevron-down"></i> Solution</span>
          </summary>
          <div class="ans-content">
            <p>Starting colony = <span class="math-font">1.6 × 10⁵ = 1,60,000</span>. Antibiotic scales population by <span class="math-font">2⁻⁴</span> each hour.
              <br>After 1 hour: <span class="math-font">1,60,000 × 2⁻⁴ = 1,60,000 × (1/16) = 10,000</span>.
              <br>After 2 hours: <span class="math-font">10,000 × (1/16) = 625 bacteria}</span>.
              <br>In scientific form: <span class="math-font">6.25 × 10² bacteria</span>.
            </p>
          </div>
        </details>
      </div>

      <!-- ======================================================== -->
      <!-- 6. PREVIOUS YEARS & MOST PROBABLE EXAM QUESTIONS -->
      <!-- ======================================================== -->
      <h3 class="topic-title"><i class="fa-solid fa-fire"></i> 6. Previous Years Questions (PYQs) & Most Probable Exam Models</h3>

      <!-- PYQ 1 -->
      <details class="ans-box">
        <summary>
          <span>PYQ 1 [CBSE 2023]: Simplify [ (1/3)⁻² – (1/2)⁻³ ] ÷ (1/4)⁻²</span>
          <span class="ans-badge"><i class="fa-solid fa-chevron-down"></i> Solution</span>
        </summary>
        <div class="ans-content">
          <div class="step-box">
            <div class="step-label"><i class="fa-solid fa-check"></i> Complete Step-by-Step Model Answer</div>
            <p><strong>Step 1:</strong> Apply reciprocal law <span class="math-font">(1/a)⁻ⁿ = aⁿ</span> to each term:
              <br><span class="math-font">(1/3)⁻² = 3² = 9</span>
              <br><span class="math-font">(1/2)⁻³ = 2³ = 8</span>
              <br><span class="math-font">(1/4)⁻² = 4² = 16</span>
            </p>
            <p><strong>Step 2:</strong> Evaluate within brackets:
              <br><span class="math-font">9 – 8 = 1</span>.
            </p>
            <p><strong>Step 3:</strong> Perform division:
              <br><span class="math-font">1 ÷ 16 = 1/16</span> (or <span class="math-font">4⁻² = 2⁻⁴</span>).
            </p>
            <p><strong>Final Answer:</strong> <strong>1/16</strong>.</p>
          </div>
        </div>
      </details>

      <!-- PYQ 2 -->
      <details class="ans-box">
        <summary>
          <span>PYQ 2 [CBSE 2022]: Find x if (2/9)³ × (2/9)⁻⁶ = (2/9)²ˣ⁻¹</span>
          <span class="ans-badge"><i class="fa-solid fa-chevron-down"></i> Solution</span>
        </summary>
        <div class="ans-content">
          <div class="step-box">
            <div class="step-label"><i class="fa-solid fa-check"></i> Complete Step-by-Step Model Answer</div>
            <p><strong>Step 1:</strong> Apply Product Law on LHS:
              <br><span class="math-font">((2/9))^{3 + (-6)} = ((2/9))^{-3}</span>.
            </p>
            <p><strong>Step 2:</strong> Equate with RHS:
              <br><span class="math-font">((2/9))^{-3} = ((2/9))^{2x - 1}</span>.
            </p>
            <p><strong>Step 3:</strong> Equate exponents:
              <br><span class="math-font">2x – 1 = –3 ⇒ 2x = –3 + 1 = –2 ⇒ x = (-2/2) = –1</span>.
            </p>
            <p><strong>Final Answer:</strong> <span class="math-font">x = –1</span>.</p>
          </div>
        </div>
      </details>

      <!-- PYQ 3 -->
      <details class="ans-box">
        <summary>
          <span>PYQ 3 [NCERT Exemplar]: Express Plant Cell (0.00001275 m) & Paper (0.0016 cm) in Standard Form</span>
          <span class="ans-badge"><i class="fa-solid fa-chevron-down"></i> Solution</span>
        </summary>
        <div class="ans-content">
          <div class="step-box">
            <div class="step-label"><i class="fa-solid fa-check"></i> Complete Step-by-Step Model Answer</div>
            <p><strong>(i) Plant Cell Size:</strong> <span class="math-font">0.00001275 m</span>.
              <br>Shift decimal 5 places right to get first digit 1:
              <br><span class="math-font">1.275 × 10⁻⁵ m</span>.
            </p>
            <p><strong>(ii) Paper Thickness:</strong> <span class="math-font">0.0016 cm</span>.
              <br>In cm: Shift decimal 3 places right: <span class="math-font">1.6 × 10⁻³ cm</span>.
              <br>In metres: <span class="math-font">0.0016 × 10⁻² m = 1.6 × 10⁻⁵ m</span>.
            </p>
            <p><strong>Final Answer:</strong> Plant cell = <span class="math-font">1.275 × 10⁻⁵ m</span>; Paper = <span class="math-font">1.6 × 10⁻³ cm</span> (or <span class="math-font">1.6 × 10⁻⁵ m</span>).</p>
          </div>
        </div>
      </details>

      <!-- PYQ 4 -->
      <details class="ans-box">
        <summary>
          <span>PYQ 4 [Board Model]: Total Combined Mass of Earth (5.97 × 10²⁴ kg) and Moon (7.35 × 10²² kg)</span>
          <span class="ans-badge"><i class="fa-solid fa-chevron-down"></i> Solution</span>
        </summary>
        <div class="ans-content">
          <div class="step-box">
            <div class="step-label"><i class="fa-solid fa-check"></i> Complete Step-by-Step Model Answer</div>
            <p><strong>Step 1:</strong> Identify given masses:
              <br><span class="math-font">M_E = 5.97 × 10²⁴ kg</span>
              <br><span class="math-font">M_M = 7.35 × 10²² kg</span>.
            </p>
            <p><strong>Step 2:</strong> To add numbers in scientific notation, <strong>make their powers of 10 identical</strong>!
              <br>Convert Moon's mass to order <span class="math-font">10²⁴</span>:
              <br><span class="math-font">7.35 × 10²² = 7.35 × 10⁻² × 10²⁴ = 0.0735 × 10²⁴ kg</span>.
            </p>
            <p><strong>Step 3:</strong> Factor out <span class="math-font">10²⁴</span> and add coefficients:
              <br><span class="math-font">Total Mass = (5.97 + 0.0735) × 10²⁴ = 6.0435 × 10²⁴ kg</span>.
            </p>
            <p><strong>Final Answer:</strong> Total combined mass = <strong>6.0435 × 10²⁴ kg</strong>.</p>
          </div>
        </div>
      </details>

      <!-- PYQ 5 -->
      <details class="ans-box">
        <summary>
          <span>PYQ 5 [Exemplar Challenge]: If a = 2 and b = 3, Find the Value of (aᵇ + bᵃ)⁻¹</span>
          <span class="ans-badge"><i class="fa-solid fa-chevron-down"></i> Solution</span>
        </summary>
        <div class="ans-content">
          <div class="step-box">
            <div class="step-label"><i class="fa-solid fa-check"></i> Complete Step-by-Step Model Answer</div>
            <p><strong>Step 1:</strong> Substitute <span class="math-font">a = 2</span> and <span class="math-font">b = 3</span> into the expression:
              <br><span class="math-font">aᵇ = 2³ = 2 × 2 × 2 = 8</span>.
              <br><span class="math-font">bᵃ = 3² = 3 × 3 = 9</span>.
            </p>
            <p><strong>Step 2:</strong> Add the evaluated values:
              <br><span class="math-font">aᵇ + bᵃ = 8 + 9 = 17</span>.
            </p>
            <p><strong>Step 3:</strong> Apply the negative power <span class="math-font">–1</span>:
              <br><span class="math-font">(17)⁻¹ = 1/17</span>.
            </p>
            <p><strong>Final Answer:</strong> <strong>1/17</strong>.</p>
          </div>
        </div>
      </details>
    </section>
"""
