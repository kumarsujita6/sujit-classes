# -*- coding: utf-8 -*-
"""
Section 5: Complete Exam Question Bank (27 High-Yield Questions)
"""

def get_section_5():
    return '''
    <!-- SECTION 5: COMPLETE EXAM QUESTION BANK -->
    <section id="section-5" class="study-section">
      <div class="section-header">
        <div class="section-icon icon-amber">
          <i class="fa-solid fa-graduation-cap"></i>
        </div>
        <div>
          <h2>Section 5: Complete Exam Question Bank (27 CBE &amp; Board Models)</h2>
          <p>Exhaustive question bank featuring interactive MCQs, Assertion-Reasoning, Short/Long answers with marking schemes, Case Studies, and PYQs.</p>
        </div>
      </div>

      <!-- INTERACTIVE QUIZ SCORE BANNER -->
      <div class="quiz-score-banner">
        <div>
          <h4><i class="fa-solid fa-trophy"></i> Interactive MCQ Performance Engine</h4>
          <p style="margin:0; font-size: 0.9rem; color: #e0f2fe;">Click any option to test your mastery. Correct choices turn green instantly; traps are explained below each question.</p>
        </div>
        <div style="text-align: right;">
          <span style="font-size: 1.8rem; font-weight: 800; font-family: 'JetBrains Mono', monospace;" id="userQuizScore">0 / 5</span>
          <div style="font-size: 0.75rem; text-transform: uppercase; letter-spacing: 0.05em; color: #bae6fd;">Live Score Tracker</div>
        </div>
      </div>

      <!-- SUB-SECTION 5.1: 5 MCQS -->
      <h3><i class="fa-solid fa-list-check"></i> 5.1 Conceptual Multiple Choice Questions (Interactive)</h3>

      <!-- MCQ 1 -->
      <div class="quiz-card" id="quiz-card-1">
        <div class="quiz-question">
          1. What are the distinct mathematical terms in the arithmetic expression: <span class="math-inline">45 − 6 × 3 + 28 ÷ 4</span>?
        </div>
        <div class="quiz-options">
          <button class="option-btn" onclick="checkQuizAnswer(1, this, 'A')">A) 45, 6, 3, 28, 4</button>
          <button class="option-btn" onclick="checkQuizAnswer(1, this, 'B')">B) 45, −(6 × 3), 28 ÷ 4</button>
          <button class="option-btn" onclick="checkQuizAnswer(1, this, 'C')">C) 45 − 6, 3 + 28, 4</button>
          <button class="option-btn" onclick="checkQuizAnswer(1, this, 'D')">D) 45, 6 × 3, 28 ÷ 4</button>
        </div>
        <div class="quiz-feedback" id="feedback-1"></div>
      </div>

      <!-- MCQ 2 -->
      <div class="quiz-card" id="quiz-card-2">
        <div class="quiz-question">
          2. Upon removing the brackets in the expression <span class="math-inline">75 − (25 − 15)</span>, which equivalent form is produced?
        </div>
        <div class="quiz-options">
          <button class="option-btn" onclick="checkQuizAnswer(2, this, 'A')">A) 75 − 25 − 15</button>
          <button class="option-btn" onclick="checkQuizAnswer(2, this, 'B')">B) 75 + 25 − 15</button>
          <button class="option-btn" onclick="checkQuizAnswer(2, this, 'C')">C) 75 − 25 + 15</button>
          <button class="option-btn" onclick="checkQuizAnswer(2, this, 'D')">D) 75 + 25 + 15</button>
        </div>
        <div class="quiz-feedback" id="feedback-2"></div>
      </div>

      <!-- MCQ 3 -->
      <div class="quiz-card" id="quiz-card-3">
        <div class="quiz-question">
          3. Which of the following equations correctly exemplifies the Distributive Property of Multiplication over Subtraction?
        </div>
        <div class="quiz-options">
          <button class="option-btn" onclick="checkQuizAnswer(3, this, 'A')">A) 18 × (20 − 5) = 18 × 20 − 5</button>
          <button class="option-btn" onclick="checkQuizAnswer(3, this, 'B')">B) 18 × (20 − 5) = 18 × 20 − 18 × 5</button>
          <button class="option-btn" onclick="checkQuizAnswer(3, this, 'C')">C) 18 × (20 − 5) = (18 − 20) × (18 − 5)</button>
          <button class="option-btn" onclick="checkQuizAnswer(3, this, 'D')">D) 18 × (20 − 5) = 18 × 20 + 18 × 5</button>
        </div>
        <div class="quiz-feedback" id="feedback-3"></div>
      </div>

      <!-- MCQ 4 -->
      <div class="quiz-card" id="quiz-card-4">
        <div class="quiz-question">
          4. Which expression has a strictly greater value without performing exhaustive calculation?
        </div>
        <div class="quiz-options">
          <button class="option-btn" onclick="checkQuizAnswer(4, this, 'A')">A) 540 − 12 × 15</button>
          <button class="option-btn" onclick="checkQuizAnswer(4, this, 'B')">B) 540 − 12 × 18</button>
          <button class="option-btn" onclick="checkQuizAnswer(4, this, 'C')">C) Both are strictly equal</button>
          <button class="option-btn" onclick="checkQuizAnswer(4, this, 'D')">D) Cannot be determined without calculating</button>
        </div>
        <div class="quiz-feedback" id="feedback-4"></div>
      </div>

      <!-- MCQ 5 -->
      <div class="quiz-card" id="quiz-card-5">
        <div class="quiz-question">
          5. A snail climbs 4 cm up during the daytime and slips 2 cm down at night on a 14 cm post with food at the top. On which day does it reach the food?
        </div>
        <div class="quiz-options">
          <button class="option-btn" onclick="checkQuizAnswer(5, this, 'A')">A) Day 7</button>
          <button class="option-btn" onclick="checkQuizAnswer(5, this, 'B')">B) Day 6</button>
          <button class="option-btn" onclick="checkQuizAnswer(5, this, 'C')">C) Day 5</button>
          <button class="option-btn" onclick="checkQuizAnswer(5, this, 'D')">D) Day 8</button>
        </div>
        <div class="quiz-feedback" id="feedback-5"></div>
      </div>

      <!-- SUB-SECTION 5.2: 5 ASSERTION & REASONING -->
      <h3><i class="fa-solid fa-circle-question"></i> 5.2 Assertion &amp; Reasoning Questions</h3>
      <p style="font-size: 0.95rem; color: #475569;">
        <strong>Directions:</strong> In each question, a statement of Assertion (A) is given followed by a statement of Reason (R). Choose:
        <br><strong>(A)</strong> Both (A) and (R) are true, and (R) is the correct explanation of (A).
        <br><strong>(B)</strong> Both (A) and (R) are true, but (R) is NOT the correct explanation of (A).
        <br><strong>(C)</strong> (A) is true, but (R) is false.
        <br><strong>(D)</strong> (A) is false, but (R) is true.
      </p>

      <!-- AR 1 -->
      <details class="ans-box">
        <summary>
          <span>Q6 (AR 1): Commutative Property &amp; Subtraction Invariance</span>
          <span class="ans-badge">Model Answer</span>
        </summary>
        <div class="ans-content">
          <p><strong>Assertion (A):</strong> The expression <span class="math-inline">14 − 9 + 5</span> has the exact same value as <span class="math-inline">14 + 5 − 9</span>.</p>
          <p><strong>Reason (R):</strong> When an expression is expressed as a sum of terms, swapping the order of the terms does not change the value of the expression due to the Commutative Property of Addition.</p>
          <div class="step-box">
            <span class="step-label">Diagnostic Analysis</span>
            The terms in <span class="math-inline">14 − 9 + 5</span> are 14, −9, and +5. 
            Writing it as a sum of terms: <span class="math-inline">14 + (−9) + 5</span>. 
            Swapping the second and third terms gives <span class="math-inline">14 + 5 + (−9) = 14 + 5 − 9</span>. 
            Both evaluate to 10. The Commutative Property of Addition is the exact mathematical reason.
          </div>
          <p><strong>Correct Option:</strong> <strong>(A) Both (A) and (R) are true, and (R) is the correct explanation of (A).</strong></p>
        </div>
      </details>

      <!-- AR 2 -->
      <details class="ans-box">
        <summary>
          <span>Q7 (AR 2): Bracket Preceded by Minus Sign</span>
          <span class="ans-badge">Model Answer</span>
        </summary>
        <div class="ans-content">
          <p><strong>Assertion (A):</strong> <span class="math-inline">200 − (50 − 20)</span> is equal to <span class="math-inline">200 − 50 − 20</span>.</p>
          <p><strong>Reason (R):</strong> When removing brackets preceded by a negative sign, all terms inside the bracket must change their signs.</p>
          <div class="step-box">
            <span class="step-label">Diagnostic Analysis</span>
            LHS: <span class="math-inline">200 − (50 − 20) = 200 − 30 = 170</span>. 
            Unpacking correctly using sign inversion gives: <span class="math-inline">200 − 50 + 20 = 170</span>. 
            However, the assertion claims it equals <span class="math-inline">200 − 50 − 20 = 130</span>, which is FALSE! 
            Meanwhile, Reason (R) is a completely true mathematical law.
          </div>
          <p><strong>Correct Option:</strong> <strong>(D) (A) is false, but (R) is true.</strong></p>
        </div>
      </details>

      <!-- AR 3 -->
      <details class="ans-box">
        <summary>
          <span>Q8 (AR 3): Distributive Property &amp; Mental Arithmetic</span>
          <span class="ans-badge">Model Answer</span>
        </summary>
        <div class="ans-content">
          <p><strong>Assertion (A):</strong> The product <span class="math-inline">98 × 16</span> can be evaluated as <span class="math-inline">100 × 16 − 2 × 16 = 1600 − 32 = 1568</span>.</p>
          <p><strong>Reason (R):</strong> According to the Distributive Property, multiplying a number by a difference equals the difference of the individual products: <span class="math-inline">(a − b) × c = a × c − b × c</span>.</p>
          <div class="step-box">
            <span class="step-label">Diagnostic Analysis</span>
            Since <span class="math-inline">98 = (100 − 2)</span>, multiplying by 16 yields <span class="math-inline">(100 − 2) × 16 = 100 × 16 − 2 × 16</span>. 
            This is the exact statement and application of the distributive property over subtraction. Both statements are true and (R) correctly explains (A).
          </div>
          <p><strong>Correct Option:</strong> <strong>(A) Both (A) and (R) are true, and (R) is the correct explanation of (A).</strong></p>
        </div>
      </details>

      <!-- AR 4 -->
      <details class="ans-box">
        <summary>
          <span>Q9 (AR 4): Division &amp; Subtraction Non-Commutativity</span>
          <span class="ans-badge">Model Answer</span>
        </summary>
        <div class="ans-content">
          <p><strong>Assertion (A):</strong> <span class="math-inline">24 ÷ 6</span> has the same value as <span class="math-inline">6 ÷ 24</span>.</p>
          <p><strong>Reason (R):</strong> The operations of division and subtraction do NOT satisfy the commutative property.</p>
          <div class="step-box">
            <span class="step-label">Diagnostic Analysis</span>
            <span class="math-inline">24 ÷ 6 = 4</span>, whereas <span class="math-inline">6 ÷ 24 = 1/4 = 0.25</span>. Clearly, <span class="math-inline">4 ≠ 0.25</span>, so Assertion (A) is completely FALSE. 
            Reason (R) correctly states that division is non-commutative, which is TRUE.
          </div>
          <p><strong>Correct Option:</strong> <strong>(D) (A) is false, but (R) is true.</strong></p>
        </div>
      </details>

      <!-- AR 5 -->
      <details class="ans-box">
        <summary>
          <span>Q10 (AR 5): Multiplicative Terms Priority</span>
          <span class="ans-badge">Model Answer</span>
        </summary>
        <div class="ans-content">
          <p><strong>Assertion (A):</strong> In the expression <span class="math-inline">18 + 4 × 5</span>, the multiplication <span class="math-inline">4 × 5</span> must be evaluated before adding to 18.</p>
          <p><strong>Reason (R):</strong> Terms are the parts of an expression separated by '+' signs, and each term must be evaluated to a single numerical value before adding.</p>
          <div class="step-box">
            <span class="step-label">Diagnostic Analysis</span>
            The expression has two terms: 18 and <span class="math-inline">4 × 5</span>. 
            Because terms are evaluated before being added together, <span class="math-inline">4 × 5 = 20</span> must be computed first, yielding <span class="math-inline">18 + 20 = 38</span>. 
            Both (A) and (R) are true, and (R) provides the definitive structural reason.
          </div>
          <p><strong>Correct Option:</strong> <strong>(A) Both (A) and (R) are true, and (R) is the correct explanation of (A).</strong></p>
        </div>
      </details>

      <!-- SUB-SECTION 5.3: 6 SHORT ANSWER QUESTIONS -->
      <h3><i class="fa-solid fa-pen-fancy"></i> 5.3 Short Answer Questions (2M &amp; 3M)</h3>

      <!-- SA 1 -->
      <details class="ans-box">
        <summary>
          <span>Q11 (2 Marks): Decomposition of Expression into Terms</span>
          <span class="ans-badge">Model Answer</span>
        </summary>
        <div class="ans-content">
          <p><strong>Question:</strong> Convert the expression <span class="math-inline">52 − 7 × 4 + 36 ÷ 9</span> into a sum of terms, list each term, and find its final value.</p>
          <div class="step-box">
            <span class="step-label">Step-by-Step Model Solution</span>
            1. Replace subtraction with addition of additive inverse:
            <div class="math-display">52 + (−(7 × 4)) + (36 ÷ 9)</div>
            2. The distinct terms are: <strong>52</strong>, <strong>−(7 × 4)</strong>, and <strong>(36 ÷ 9)</strong>.
            <br>3. Evaluate internal terms:
            <br>• Term 1 = 52
            <br>• Term 2 = <span class="math-inline">−(28) = −28</span>
            <br>• Term 3 = <span class="math-inline">36 ÷ 9 = 4</span>
            <br>4. Sum terms: <span class="math-inline">(52 + 4) + (−28) = 56 − 28 = 28</span>.
          </div>
          <p><strong>Final Answer:</strong> Terms: <strong>52, −28, 4</strong>. Evaluated Value: <strong>28</strong>.</p>
        </div>
      </details>

      <!-- SA 2 -->
      <details class="ans-box">
        <summary>
          <span>Q12 (2 Marks): Reasoning Comparison Without Calculating</span>
          <span class="ans-badge">Model Answer</span>
        </summary>
        <div class="ans-content">
          <p><strong>Question:</strong> Without calculating the values, determine which is greater: <span class="math-inline">415 − 89</span> or <span class="math-inline">418 − 93</span>? Explain your reasoning in two simple sentences.</p>
          <div class="step-box">
            <span class="step-label">Step-by-Step Model Solution</span>
            1. Compare the minuends: 418 is 3 units greater than 415 (+3 gain).
            <br>2. Compare the subtrahends: 93 is 4 units greater than 89, which means we are subtracting 4 units more (−4 loss).
            <br>3. Net effect on the second expression = <span class="math-inline">+3 − 4 = −1</span>. 
            <br>Since the second expression ends up with 1 unit less, <span class="math-inline">415 − 89 &gt; 418 − 93</span>.
          </div>
          <p><strong>Final Answer:</strong> <span class="math-inline">415 − 89 &gt; 418 − 93</span> because subtracting 4 extra units outweighs starting with only 3 extra units.</p>
        </div>
      </details>

      <!-- SA 3 -->
      <details class="ans-box">
        <summary>
          <span>Q13 (3 Marks): Distributive Property Mental Calculation</span>
          <span class="ans-badge">Model Answer</span>
        </summary>
        <div class="ans-content">
          <p><strong>Question:</strong> Given that <span class="math-inline">48 × 15 = 720</span>, evaluate the following using the Distributive Property:
          <br>(a) <span class="math-inline">58 × 15</span> &nbsp;&nbsp;&nbsp;&nbsp; (b) <span class="math-inline">48 × 16</span></p>
          <div class="step-box">
            <span class="step-label">Step-by-Step Model Solution</span>
            <strong>Part (a):</strong>
            <br>Notice that <span class="math-inline">58 = 48 + 10</span>.
            <div class="math-display">58 × 15 = (48 + 10) × 15 = 48 × 15 + 10 × 15</div>
            Substitute known value: <span class="math-inline">720 + 150 = 870</span>.
            <br><br>
            <strong>Part (b):</strong>
            <br>Notice that <span class="math-inline">16 = 15 + 1</span>.
            <div class="math-display">48 × 16 = 48 × (15 + 1) = 48 × 15 + 48 × 1</div>
            Substitute known value: <span class="math-inline">720 + 48 = 768</span>.
          </div>
          <p><strong>Final Answer:</strong> (a) <strong>870</strong>; (b) <strong>768</strong>.</p>
        </div>
      </details>

      <!-- SA 4 -->
      <details class="ans-box">
        <summary>
          <span>Q14 (3 Marks): Sign Inversion Proof with Brackets</span>
          <span class="ans-badge">Model Answer</span>
        </summary>
        <div class="ans-content">
          <p><strong>Question:</strong> Simplify the expression by removing brackets and writing it as a sum of terms:
          <div class="math-display">120 − (45 − 25 + 10)</div>
          Verify your result by evaluating the bracket first.</p>
          <div class="step-box">
            <span class="step-label">Step-by-Step Model Solution</span>
            <strong>Method 1 (Removing Brackets via Inversion Gate):</strong>
            <br>The bracket is preceded by a minus sign. Every sign inside inverts:
            <div class="math-display">120 − 45 + 25 − 10</div>
            Group positive and negative terms:
            <br><span class="math-inline">(120 + 25) − (45 + 10) = 145 − 55 = 90</span>.
            <br><br>
            <strong>Method 2 (Evaluating Inside Bracket First):</strong>
            <br><span class="math-inline">45 − 25 + 10 = 20 + 10 = 30</span>.
            <br><span class="math-inline">120 − 30 = 90</span>.
          </div>
          <p><strong>Final Answer:</strong> Unpacked form: <span class="math-inline">120 − 45 + 25 − 10</span>. Evaluated value = <strong>90</strong>.</p>
        </div>
      </details>

      <!-- SA 5 -->
      <details class="ans-box">
        <summary>
          <span>Q15 (2 Marks): Real-World Word Problem Modeling</span>
          <span class="ans-badge">Model Answer</span>
        </summary>
        <div class="ans-content">
          <p><strong>Question:</strong> An amusement park charges ₹60 for an adult ride and ₹35 for a child ride. Write an arithmetic expression for the total cost for 3 adults and 4 children, identify its terms, and evaluate the total cost.</p>
          <div class="step-box">
            <span class="step-label">Step-by-Step Model Solution</span>
            1. Target Expression: <span class="math-inline">3 × 60 + 4 × 35</span>.
            <br>2. Terms: <strong>3 × 60</strong> and <strong>4 × 35</strong>.
            <br>3. Evaluation:
            <br>• Adult term: <span class="math-inline">3 × 60 = 180</span>
            <br>• Child term: <span class="math-inline">4 × 35 = 140</span>
            <br>• Total cost: <span class="math-inline">180 + 140 = 320</span> rupees.
          </div>
          <p><strong>Final Answer:</strong> Expression: <span class="math-inline">3 × 60 + 4 × 35</span>. Terms: <span class="math-inline">3 × 60</span>, <span class="math-inline">4 × 35</span>. Total: <strong>₹320</strong>.</p>
        </div>
      </details>

      <!-- SA 6 -->
      <details class="ans-box">
        <summary>
          <span>Q16 (3 Marks): Bracket Insertion Challenge</span>
          <span class="ans-badge">Model Answer</span>
        </summary>
        <div class="ans-content">
          <p><strong>Question:</strong> Insert brackets in the expression <span class="math-inline">7 + 3 × 8 − 5</span> to obtain:
          <br>(a) A value of 75 &nbsp;&nbsp;&nbsp;&nbsp; (b) A value of 16 &nbsp;&nbsp;&nbsp;&nbsp; (c) A value of 26</p>
          <div class="step-box">
            <span class="step-label">Step-by-Step Model Solution</span>
            <strong>(a) Target = 75:</strong>
            <br>Group addition first: <span class="math-inline">(7 + 3) = 10</span>. 
            <br>Then multiply and subtract: <span class="math-inline">(7 + 3) × 8 − 5 = 10 × 8 − 5 = 80 − 5 = 75</span>!
            <br><br>
            <strong>(b) Target = 16:</strong>
            <br>Group subtraction at the end: <span class="math-inline">(8 − 5) = 3</span>.
            <br>Then: <span class="math-inline">7 + 3 × (8 − 5) = 7 + 3 × 3 = 7 + 9 = 16</span>!
            <br><br>
            <strong>(c) Target = 26:</strong>
            <br>Raw evaluation without extra brackets: <span class="math-inline">7 + (3 × 8) − 5 = 7 + 24 − 5 = 31 − 5 = 26</span>.
          </div>
          <p><strong>Final Answer:</strong> (a) <span class="math-inline">(7 + 3) × 8 − 5 = 75</span>; (b) <span class="math-inline">7 + 3 × (8 − 5) = 16</span>; (c) <span class="math-inline">7 + (3 × 8) − 5 = 26</span>.</p>
        </div>
      </details>

      <!-- SUB-SECTION 5.4: 4 LONG ANSWER QUESTIONS WITH MARKING SCHEME -->
      <h3><i class="fa-solid fa-file-invoice"></i> 5.4 Long Answer Questions (5 Marks Each with Step-by-Step Marking Schemes)</h3>

      <!-- LA 1 -->
      <details class="ans-box">
        <summary>
          <span>Q17 (5M): Complete Derivation &amp; Proof of Distributive Laws</span>
          <span class="ans-badge">5-Step Solution + Marking Scheme</span>
        </summary>
        <div class="ans-content">
          <p><strong>Question:</strong> 
          (a) State the Distributive Property of Multiplication over Addition and Subtraction. (1 Mark)
          <br>(b) Illustrate the property geometrically using an Area Model for <span class="math-inline">6 × (10 + 4)</span>. (2 Marks)
          <br>(c) Use the property to compute <span class="math-inline">996 × 25</span> using mental arithmetic. (2 Marks)
          </p>
          <div class="step-box">
            <span class="step-label">Step-by-Step Model Solution</span>
            <strong>Part (a): Statement (1 Mark)</strong>
            <br>The Distributive Property states that multiplying a number by a sum (or difference) yields the same result as multiplying the number by each addend (or subtrahend) individually and combining the products:
            <div class="math-display">a × (b + c) = a × b + a × c &nbsp;&nbsp;&nbsp;&nbsp; a × (b − c) = a × b − a × c</div>
            <br>
            <strong>Part (b): Geometric Area Model (2 Marks)</strong>
            <br>Consider a large rectangle with height = 6 units and total base = <span class="math-inline">(10 + 4) = 14</span> units.
            <br>• Sub-rectangle 1: Dimensions <span class="math-inline">6 × 10</span> &rarr; <span class="math-inline">Area = 60</span> sq units.
            <br>• Sub-rectangle 2: Dimensions <span class="math-inline">6 × 4</span> &rarr; <span class="math-inline">Area = 24</span> sq units.
            <br>• Total combined area = <span class="math-inline">60 + 24 = 84</span> sq units.
            <br>• Direct calculation: <span class="math-inline">6 × 14 = 84</span> sq units. 
            <br>Both methods demonstrate identical area: <span class="math-inline">6 × (10 + 4) = 6 × 10 + 6 × 4 = 84</span>.
            <br><br>
            <strong>Part (c): Mental Arithmetic for 996 × 25 (2 Marks)</strong>
            <br>Express 996 as <span class="math-inline">(1000 − 4)</span>:
            <div class="math-display">996 × 25 = (1000 − 4) × 25 = 1000 × 25 − 4 × 25</div>
            <span class="math-inline">= 25000 − 100 = 24900</span>.
          </div>
          <div class="mark-scheme">
            <div class="mark-item"><span>Accurate algebraic statements of both distributive laws</span><span class="mark-val">1 Mark</span></div>
            <div class="mark-item"><span>Clear geometric rectangle division with dimensions 6x10 and 6x4 showing area equivalence</span><span class="mark-val">2 Marks</span></div>
            <div class="mark-item"><span>Decomposition (1000 − 4) × 25 with accurate expansion 25,000 − 100 = 24,900</span><span class="mark-val">2 Marks</span></div>
          </div>
        </div>
      </details>

      <!-- LA 2 -->
      <details class="ans-box">
        <summary>
          <span>Q18 (5M): The Alternating Series &amp; General Proof</span>
          <span class="ans-badge">5-Step Solution + Marking Scheme</span>
        </summary>
        <div class="ans-content">
          <p><strong>Question:</strong> Consider the alternating arithmetic expression:
          <div class="math-display">S = 1 − 2 + 3 − 4 + 5 − 6 + ... + 99 − 100</div>
          (a) Evaluate <span class="math-inline">S</span> by pairing consecutive terms. (2 Marks)
          <br>(b) Evaluate <span class="math-inline">S</span> by grouping all positive terms and all negative terms. (2 Marks)
          <br>(c) State the general formula for the sum of such an alternating series up to <span class="math-inline">2n</span> terms. (1 Mark)
          </p>
          <div class="step-box">
            <span class="step-label">Step-by-Step Model Solution</span>
            <strong>Part (a): Pairing Consecutive Terms (2 Marks)</strong>
            <br>Group the 100 terms into 50 consecutive pairs:
            <div class="math-display">S = (1 − 2) + (3 − 4) + (5 − 6) + ... + (99 − 100)</div>
            Each pair evaluates to <span class="math-inline">−1</span>:
            <div class="math-display">S = (−1) + (−1) + (−1) + ... + (−1) (50  pairs) = 50 × (−1) = −50</div>
            <br>
            <strong>Part (b): Separating Positive and Negative Terms (2 Marks)</strong>
            <br>Positive terms: <span class="math-inline">P = 1 + 3 + 5 + ... + 99</span> (Sum of first 50 odd numbers = <span class="math-inline">50^2 = 2500</span>).
            <br>Negative terms: <span class="math-inline">N = −(2 + 4 + 6 + ... + 100) = −2 × (1 + 2 + ... + 50) = −2 × (50 × 51) ÷ 2 = −2550</span>.
            <br>Combined total: <span class="math-inline">S = P + N = 2500 − 2550 = −50</span>.
            <br><br>
            <strong>Part (c): General Formula (1 Mark)</strong>
            <br>For any alternating series of <span class="math-inline">2n</span> integers:
            <div class="math-display">S_{2n} = −n</div>
          </div>
          <div class="mark-scheme">
            <div class="mark-item"><span>Grouping into 50 pairs of (−1) yielding −50</span><span class="mark-val">2 Marks</span></div>
            <div class="mark-item"><span>Correct summation of odds (2500) and evens (2550) yielding −50</span><span class="mark-val">2 Marks</span></div>
            <div class="mark-item"><span>Deduction of general theorem S = −n for 2n terms</span><span class="mark-val">1 Mark</span></div>
          </div>
        </div>
      </details>

      <!-- LA 3 -->
      <details class="ans-box">
        <summary>
          <span>Q19 (5M): Mathematical Expression Trees &amp; Nested Brackets</span>
          <span class="ans-badge">5-Step Solution + Marking Scheme</span>
        </summary>
        <div class="ans-content">
          <p><strong>Question:</strong> 
          Evaluate the complex nested expression step-by-step:
          <div class="math-display">85 − [ 30 + 2 × (18 − 6 ÷ 2) ] + 4 × 5</div>
          (a) Identify the outermost terms. (1 Mark)
          <br>(b) Evaluate the innermost bracket expression. (1.5 Marks)
          <br>(c) Evaluate the square bracket expression. (1.5 Marks)
          <br>(d) Compute the final evaluated value. (1 Mark)
          </p>
          <div class="step-box">
            <span class="step-label">Step-by-Step Model Solution</span>
            <strong>Part (a): Outermost Terms (1 Mark)</strong>
            <br>Rewritten as sum: <span class="math-inline">85 + (−[ 30 + 2 × (18 − 6 ÷ 2) ]) + (4 × 5)</span>.
            <br>The three terms are: <strong>85</strong>, <strong>−[ 30 + 2 × (18 − 6 ÷ 2) ]</strong>, and <strong>4 × 5</strong>.
            <br><br>
            <strong>Part (b): Innermost Parentheses (1.5 Marks)</strong>
            <br>Inside <span class="math-inline">(18 − 6 ÷ 2)</span>, division takes precedence:
            <br><span class="math-inline">6 ÷ 2 = 3</span>.
            <br>Then subtraction: <span class="math-inline">18 − 3 = 15</span>.
            <br><br>
            <strong>Part (c): Square Bracket Evaluation (1.5 Marks)</strong>
            <br>Substitute innermost value: <span class="math-inline">[ 30 + 2 × 15 ]</span>.
            <br>Multiplication takes precedence: <span class="math-inline">2 × 15 = 30</span>.
            <br>Then addition: <span class="math-inline">30 + 30 = 60</span>.
            <br><br>
            <strong>Part (d): Final Value Computation (1 Mark)</strong>
            <br>Substitute back: <span class="math-inline">85 − 60 + (4 × 5)</span>.
            <br><span class="math-inline">4 × 5 = 20</span>.
            <br><span class="math-inline">85 − 60 + 20 = 25 + 20 = 45</span>.
          </div>
          <div class="mark-scheme">
            <div class="mark-item"><span>Identification of 3 outermost terms separated by +</span><span class="mark-val">1 Mark</span></div>
            <div class="mark-item"><span>Accurate evaluation of innermost (18 − 3) = 15</span><span class="mark-val">1.5 Marks</span></div>
            <div class="mark-item"><span>Accurate evaluation of bracket [30 + 30] = 60</span><span class="mark-val">1.5 Marks</span></div>
            <div class="mark-item"><span>Correct final value = 45</span><span class="mark-val">1 Mark</span></div>
          </div>
        </div>
      </details>

      <!-- LA 4 -->
      <details class="ans-box">
        <summary>
          <span>Q20 (5M): Real-World Financial Budget Modeling</span>
          <span class="ans-badge">5-Step Solution + Marking Scheme</span>
        </summary>
        <div class="ans-content">
          <p><strong>Question:</strong> A school in Bhubaneswar plans an educational tour to Chilika Lake for 45 students and 4 teachers. 
          The costs are as follows:
          <br>• Bus rental: Flat ₹8,000 for the trip.
          <br>• Boat safari ticket: ₹120 per student, ₹180 per teacher.
          <br>• Lunch buffet: ₹150 per person (both students and teachers).
          <br>• Special concession: A bulk tourist discount of ₹1,500 is deducted from the final bill.
          <br>(a) Construct a single master arithmetic expression for the total trip cost. (2 Marks)
          <br>(b) Identify the independent terms in your expression. (1 Mark)
          <br>(c) Evaluate the total budget required for the tour. (2 Marks)
          </p>
          <div class="step-box">
            <span class="step-label">Step-by-Step Model Solution</span>
            <strong>Part (a): Master Arithmetic Expression (2 Marks)</strong>
            <br>Total persons = <span class="math-inline">45 + 4 = 49</span> persons.
            <div class="math-display">Cost = 8000 + (45 × 120 + 4 × 180) + (45 + 4) × 150 − 1500</div>
            <br>
            <strong>Part (b): Independent Terms (1 Mark)</strong>
            <br>The expression consists of four terms:
            <br>1. Bus rental: <span class="math-inline">8000</span>
            <br>2. Boat safari: <span class="math-inline">45 × 120 + 4 × 180</span>
            <br>3. Lunch: <span class="math-inline">49 × 150</span>
            <br>4. Discount: <span class="math-inline">−1500</span>
            <br><br>
            <strong>Part (c): Step-by-Step Evaluation (2 Marks)</strong>
            <br>• Bus = ₹8,000
            <br>• Safari = <span class="math-inline">5400 + 720 = 6120</span>
            <br>• Lunch = <span class="math-inline">49 × 150 = (50 − 1) × 150 = 7500 − 150 = 7350</span>
            <br>• Sum before discount = <span class="math-inline">8000 + 6120 + 7350 = 21470</span>
            <br>• Net budget after discount = <span class="math-inline">21470 − 1500 = 19970</span> rupees.
          </div>
          <div class="mark-scheme">
            <div class="mark-item"><span>Constructing complete expression with correct brackets and terms</span><span class="mark-val">2 Marks</span></div>
            <div class="mark-item"><span>Listing all 4 distinct terms separated by +</span><span class="mark-val">1 Mark</span></div>
            <div class="mark-item"><span>Accurate evaluation of safari (6120), lunch (7350) and final total ₹19,970</span><span class="mark-val">2 Marks</span></div>
          </div>
        </div>
      </details>

      <!-- SUB-SECTION 5.5: 2 COMPETENCY-BASED CASE STUDIES -->
      <h3><i class="fa-solid fa-briefcase"></i> 5.5 Competency-Based Case Studies (Real-World Applied Mathematics)</h3>

      <!-- CASE STUDY 1 -->
      <details class="ans-box">
        <summary>
          <span>Case Study 1: The Organic Farmer's Cooperative Market (Begur Agri-Cluster)</span>
          <span class="ans-badge">Competency-Based Case Study</span>
        </summary>
        <div class="ans-content">
          <p>
            <strong>Context:</strong> In the Begur Agricultural District Cooperative, three farming families supply organic produce daily. 
            The market operates all 7 days of the week.
            <br>• Farmer A (Rahim) supplies 15 kg of Alphonso mangoes and 10 kg of papayas each day.
            <br>• Farmer B (Shyam) supplies 25 kg of Alphonso mangoes and 14 kg of papayas each day.
            <br>• Farmer C (Anita) supplies 20 kg of Alphonso mangoes and 16 kg of papayas each day.
            <br>The wholesale selling prices are fixed: ₹80 per kg of mangoes and ₹40 per kg of papayas.
          </p>

          <p><strong>Sub-Question 1:</strong> Write an arithmetic expression using the Distributive Property for the total kilograms of mangoes supplied by all three farmers in one complete week.</p>
          <div class="step-box">
            <span class="step-label">Solution</span>
            Daily total mangoes = <span class="math-inline">15 + 25 + 20 = 60</span> kg. 
            For 7 days: <span class="math-inline">7 × (15 + 25 + 20)</span>. 
            Value: <span class="math-inline">7 × 60 = 420</span> kg.
          </div>

          <p><strong>Sub-Question 2:</strong> Write an expression for the total weekly revenue earned by Shyam from both mangoes and papayas.</p>
          <div class="step-box">
            <span class="step-label">Solution</span>
            Shyam's daily revenue = <span class="math-inline">25 × 80 + 14 × 40 = 2000 + 560 = 2560</span>. 
            Weekly revenue = <span class="math-inline">7 × (25 × 80 + 14 × 40) = 7 × 2560 = 17920</span> rupees.
          </div>

          <p><strong>Sub-Question 3:</strong> The cooperative spends ₹350 per day on collective transport and ₹50 per day on cleaning. Write an expression for the cooperative's total maintenance deduction over the week.</p>
          <div class="step-box">
            <span class="step-label">Solution</span>
            Daily expenditure = <span class="math-inline">350 + 50 = 400</span>. 
            Weekly deduction = <span class="math-inline">7 × (350 + 50) = 7 × 400 = 2800</span> rupees.
          </div>

          <p><strong>Sub-Question 4:</strong> If Rahim gives a ₹5 discount per kg on mangoes on Sundays only, write the expression for his total mango revenue in a week.</p>
          <div class="step-box">
            <span class="step-label">Solution</span>
            Rahim sells mangoes at ₹80 on 6 days, and at ₹75 on Sunday (1 day). 
            Expression = <span class="math-inline">6 × (15 × 80) + 1 × (15 × 75)</span> (or <span class="math-inline">7 × 15 × 80 − 15 × 5</span>). 
            Value: <span class="math-inline">8400 − 75 = 8325</span> rupees.
          </div>
        </div>
      </details>

      <!-- CASE STUDY 2 -->
      <details class="ans-box">
        <summary>
          <span>Case Study 2: Annual Sports Day Drill &amp; March-Past Formations</span>
          <span class="ans-badge">Competency-Based Case Study</span>
        </summary>
        <div class="ans-content">
          <p>
            <strong>Context:</strong> For the Class 7 Annual Sports Day march-past at Kalinga Stadium, students are arranged into rectangular platoons.
            <br>• Red Platoon: 6 rows with 8 boys and 4 girls in each row.
            <br>• Blue Platoon: 6 rows with 12 boys and 6 girls in each row.
            <br>• Green Platoon: 8 rows with 10 boys and 5 girls in each row.
          </p>

          <p><strong>Sub-Question 1:</strong> Using the Distributive Property, write an expression for the total number of students in the Red Platoon, and calculate its value.</p>
          <div class="step-box">
            <span class="step-label">Solution</span>
            Expression = <span class="math-inline">6 × (8 + 4) = 6 × 8 + 6 × 4</span>. 
            Value = <span class="math-inline">48 + 24 = 72</span> students.
          </div>

          <p><strong>Sub-Question 2:</strong> Show that the total number of girls in the Red and Blue platoons combined can be factored using the Distributive Property.</p>
          <div class="step-box">
            <span class="step-label">Solution</span>
            Girls in Red Platoon = <span class="math-inline">6 × 4</span>; Girls in Blue Platoon = <span class="math-inline">6 × 6</span>. 
            Combined Girls = <span class="math-inline">6 × 4 + 6 × 6 = 6 × (4 + 6) = 6 × 10 = 60</span> girls.
          </div>

          <p><strong>Sub-Question 3:</strong> Each student in the Green Platoon receives 2 flag ribbons and 1 energy drink. Write an expression for the total items distributed to the Green Platoon.</p>
          <div class="step-box">
            <span class="step-label">Solution</span>
            Students in Green Platoon = <span class="math-inline">8 × (10 + 5) = 8 × 15 = 120</span>. 
            Items per student = <span class="math-inline">2 + 1 = 3</span> items. 
            Total items = <span class="math-inline">[8 × (10 + 5)] × (2 + 1) = 120 × 3 = 360</span> items.
          </div>

          <p><strong>Sub-Question 4:</strong> During the rehearsal, 4 boys from each row of the Blue Platoon were called for flag duty. Write an expression for the remaining boys marching in the Blue Platoon.</p>
          <div class="step-box">
            <span class="step-label">Solution</span>
            Remaining boys per row = <span class="math-inline">12 − 4 = 8</span>. 
            Total marching boys = <span class="math-inline">6 × (12 − 4) = 6 × 8 = 48</span> boys (or <span class="math-inline">6 × 12 − 6 × 4 = 72 − 24 = 48</span>).
          </div>
        </div>
      </details>

      <!-- SUB-SECTION 5.6: 5 PYQS & MOST PROBABLE EXAM QUESTIONS -->
      <h3><i class="fa-solid fa-clock-rotate-left"></i> 5.6 Previous Years Questions (PYQs) &amp; Most Probable Exam Questions</h3>

      <!-- PYQ 1 -->
      <details class="ans-box">
        <summary>
          <span>PYQ 1 (CBSE Pattern): Evaluating Expression with Additive Inverses</span>
          <span class="ans-badge">Official Exam Model</span>
        </summary>
        <div class="ans-content">
          <p><strong>Question:</strong> Find the value of <span class="math-inline">45 + (−23) + (−15) + 33</span> by rearranging the terms strategically.</p>
          <div class="step-box">
            <span class="step-label">Step-by-Step Model Solution</span>
            By Commutative and Associative Properties, group positive terms together and negative terms together:
            <div class="math-display">[45 + 33] + [(−23) + (−15)]</div>
            1. Sum of positive terms = <span class="math-inline">45 + 33 = 78</span>.
            <br>2. Sum of negative terms = <span class="math-inline">−(23 + 15) = −38</span>.
            <br>3. Combine: <span class="math-inline">78 + (−38) = 78 − 38 = 40</span>.
          </div>
          <p><strong>Final Answer:</strong> <strong>40</strong>.</p>
        </div>
      </details>

      <!-- PYQ 2 -->
      <details class="ans-box">
        <summary>
          <span>PYQ 2 (BSE Odisha Pattern): Distributive Law over Subtraction</span>
          <span class="ans-badge">Official Exam Model</span>
        </summary>
        <div class="ans-content">
          <p><strong>Question:</strong> Evaluate <span class="math-inline">735 × 99</span> using the Distributive Property.</p>
          <div class="step-box">
            <span class="step-label">Step-by-Step Model Solution</span>
            Write 99 as <span class="math-inline">(100 − 1)</span>:
            <div class="math-display">735 × 99 = 735 × (100 − 1)</div>
            Apply Distributive Law:
            <div class="math-display">= 735 × 100 − 735 × 1</div>
            <span class="math-inline">= 73500 − 735 = 72765</span>.
          </div>
          <p><strong>Final Answer:</strong> <strong>72,765</strong>.</p>
        </div>
      </details>

      <!-- PYQ 3 -->
      <details class="ans-box">
        <summary>
          <span>PYQ 3 (Exemplar Model): Sign Inversion with Double Negatives</span>
          <span class="ans-badge">Official Exam Model</span>
        </summary>
        <div class="ans-content">
          <p><strong>Question:</strong> Simplify by removing brackets: <span class="math-inline">150 − [ 40 − (−20 + 5) ]</span>.</p>
          <div class="step-box">
            <span class="step-label">Step-by-Step Model Solution</span>
            1. Evaluate inside innermost parentheses: <span class="math-inline">−20 + 5 = −15</span>.
            <br>2. Expression becomes: <span class="math-inline">150 − [ 40 − (−15) ]</span>.
            <br>3. Remove inner bracket with minus sign: <span class="math-inline">40 − (−15) = 40 + 15 = 55</span>.
            <br>4. Finally: <span class="math-inline">150 − 55 = 95</span>.
          </div>
          <p><strong>Final Answer:</strong> <strong>95</strong>.</p>
        </div>
      </details>

      <!-- PYQ 4 -->
      <details class="ans-box">
        <summary>
          <span>PYQ 4 (KVS Model): Expression Equivalence Verification</span>
          <span class="ans-badge">Official Exam Model</span>
        </summary>
        <div class="ans-content">
          <p><strong>Question:</strong> Is <span class="math-inline">16 ÷ (4 ÷ 2)</span> equal to <span class="math-inline">(16 ÷ 4) ÷ 2</span>? What does this demonstrate about the associative property?</p>
          <div class="step-box">
            <span class="step-label">Step-by-Step Model Solution</span>
            • LHS: <span class="math-inline">16 ÷ (4 ÷ 2) = 16 ÷ 2 = 8</span>.
            <br>• RHS: <span class="math-inline">(16 ÷ 4) ÷ 2 = 4 ÷ 2 = 2</span>.
            <br>Since <span class="math-inline">8 ≠ 2</span>, the two expressions are NOT equal!
            <br><strong>Conclusion:</strong> Division does NOT satisfy the Associative Property: <span class="math-inline">a ÷ (b ÷ c) ≠ (a ÷ b) ÷ c</span>.
          </div>
          <p><strong>Final Answer:</strong> No, they are not equal (<span class="math-inline">8 ≠ 2</span>). This demonstrates that division is non-associative.</p>
        </div>
      </details>

      <!-- PYQ 5 -->
      <details class="ans-box">
        <summary>
          <span>PYQ 5 (Most Probable 2026-27): Factoring Out Common Factors</span>
          <span class="ans-badge">Official Exam Model</span>
        </summary>
        <div class="ans-content">
          <p><strong>Question:</strong> Evaluate <span class="math-inline">84 × 37 + 84 × 63</span> using a suitable property. Name the property used.</p>
          <div class="step-box">
            <span class="step-label">Step-by-Step Model Solution</span>
            Notice that 84 is a common factor in both terms. 
            Apply the reverse of the Distributive Property (factoring out):
            <div class="math-display">84 × 37 + 84 × 63 = 84 × (37 + 63)</div>
            Add inside the bracket: <span class="math-inline">37 + 63 = 100</span>.
            <br>Multiply: <span class="math-inline">84 × 100 = 8400</span>.
          </div>
          <p><strong>Final Answer:</strong> <strong>8,400</strong>. Property used: <strong>Distributive Property of Multiplication over Addition</strong>.</p>
        </div>
      </details>
    </section>
'''
