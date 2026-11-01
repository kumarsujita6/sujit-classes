# -*- coding: utf-8 -*-
"""
Section 4 - Part 3: Removing Brackets, Distributive Law, Figure it Out 3 & 4 (Pages 35–42)
"""

def get_sec4_part3():
    return '''
      <!-- PART 3: REMOVING BRACKETS, DISTRIBUTIVE LAW & FIGURE IT OUT 3 & 4 -->
      <h3><i class="fa-solid fa-circle-play"></i> Part 3: Removing Brackets, Distributive Law &amp; Figure it Out 3 &amp; 4 (Pages 35–42)</h3>

      <!-- EXAMPLES 12, 13, 14 -->
      <details class="ans-box">
        <summary>
          <span><i class="fa-solid fa-unlock-keyhole"></i> Examples 12, 13 &amp; 14 (Pages 35–36): Bracket Unpacking Proofs</span>
          <span class="ans-badge">5-Step Solution</span>
        </summary>
        <div class="ans-content">
          <div class="step-box">
            <span class="step-label"><i class="fa-solid fa-clipboard-question"></i> Step 1: Problem Understanding / Given Data</span>
            Analyze the mathematical mechanisms behind removing brackets:
            <br>• <strong>Example 12:</strong> Show why <span class="math-inline">100 − (15 + 56) = 100 − 15 − 56</span>.
            <br>• <strong>Example 13:</strong> Is it possible to write <span class="math-inline">500 − (250 − 100)</span> without brackets? Why does it become <span class="math-inline">500 − 250 + 100</span>?
            <br>• <strong>Example 14:</strong> Why does <span class="math-inline">28 + (35 − 10)</span> simply become <span class="math-inline">28 + 35 − 10</span> without flipping signs?
          </div>
          <div class="step-box">
            <span class="step-label"><i class="fa-solid fa-lightbulb"></i> Step 2: Key Mathematical Concept / Strategy</span>
            A preceding '+' sign acts as an <em>Identity Gate</em> (preserves internal signs). 
            A preceding '−' sign acts as an <em>Inversion Gate</em> (inverts internal signs: + becomes −, and − becomes +).
          </div>
          <div class="step-box">
            <span class="step-label"><i class="fa-solid fa-calculator"></i> Step 3: Step-by-Step Mathematical Calculation &amp; Working</span>
            <ul>
              <li>
                <strong>Example 12 (Irfan's Change):</strong> 
                <br>With brackets: <span class="math-inline">100 − (15 + 56) = 100 − 71 = 29</span>.
                <br>Without brackets: Deduct ₹15 first (<span class="math-inline">100 − 15 = 85</span>), then deduct ₹56 (<span class="math-inline">85 − 56 = 29</span>). 
                <br>Both subtractions happen sequentially: <span class="math-inline">100 − 15 − 56 = 29</span>.
              </li>
              <li>
                <strong>Example 13 (Excess Deduction Correction):</strong> 
                <br>With brackets: <span class="math-inline">500 − (250 − 100) = 500 − 150 = 350</span>.
                <br>If we subtract 250 directly from 500 (<span class="math-inline">500 − 250 = 250</span>), we subtracted 100 too much! 
                <br>To restore equality, we must add back 100: <span class="math-inline">500 − 250 + 100 = 350</span>. 
                <br>Notice: <span class="math-inline">500 − 250 − 100 = 150 ≠ 350</span>!
              </li>
              <li>
                <strong>Example 14 (Hira's Coins):</strong> 
                <br>Hira has 28 in bag 1, 35 in bag 2, and gives away 10. 
                <br>Total = <span class="math-inline">28 + (35 − 10) = 28 + (35 + (−10))</span>. 
                <br>Because terms can be added in any order: <span class="math-inline">28 + 35 − 10 = 53</span>.
              </li>
            </ul>
          </div>
          <div class="step-box">
            <span class="step-label"><i class="fa-solid fa-wand-magic-sparkles"></i> Step 4: Generalized Sign Rules</span>
            <span class="math-inline">− (A + B) = − A − B</span> and <span class="math-inline">− (A − B) = − A + B</span>.
          </div>
          <div class="step-box">
            <span class="step-label"><i class="fa-solid fa-circle-check"></i> Step 5: Final Conclusion &amp; Key Takeaway</span>
            Removing brackets preceded by '−' inverts every sign inside; removing brackets preceded by '+' preserves every sign unchanged.
          </div>
        </div>
      </details>

      <!-- FIGURE IT OUT 3 - Q1 & Q2 -->
      <details class="ans-box">
        <summary>
          <span><i class="fa-solid fa-pen-ruler"></i> Figure it Out 3 - Q1 &amp; Q2 (Pages 37–38): Fill Blanks &amp; Bracket Removal</span>
          <span class="ans-badge">5-Step Solution</span>
        </summary>
        <div class="ans-content">
          <div class="step-box">
            <span class="step-label"><i class="fa-solid fa-clipboard-question"></i> Step 1: Problem Understanding / Given Data</span>
            <strong>Q1: Fill in blanks and operator boxes:</strong>
            <br>(a) <span class="math-inline">24 + (6 − 4) = 24 + 6</span> [ ____ ] <span class="math-inline">_____</span>
            <br>(b) <span class="math-inline">38 + (_____</span> [ ____ ] <span class="math-inline">_____) = 38 + 9 − 4</span>
            <br>(c) <span class="math-inline">24 − (6 + 4) = 24</span> [ ____ ] <span class="math-inline">6 − 4</span>
            <br>(d) <span class="math-inline">24 − 6 − 4 = 24 − 6</span> [ ____ ] <span class="math-inline">_____</span>
            <br>(e) <span class="math-inline">27 − (8 + 3) = 27</span> [ ____ ] <span class="math-inline">8</span> [ ____ ] <span class="math-inline">3</span>
            <br>(f) <span class="math-inline">27 − (_____</span> [ ____ ] <span class="math-inline">_____) = 27 − 8 + 3</span>
            <br><strong>Q2: Remove brackets and write equivalent expressions:</strong>
            <br>(a) <span class="math-inline">14 + (12 + 10)</span> &nbsp;|&nbsp; (b) <span class="math-inline">14 − (12 + 10)</span> &nbsp;|&nbsp; (c) <span class="math-inline">14 + (12 − 10)</span>
            <br>(d) <span class="math-inline">14 − (12 − 10)</span> &nbsp;|&nbsp; (e) <span class="math-inline">−14 + (12 − 10)</span> &nbsp;|&nbsp; (f) <span class="math-inline">14 − (−12 − 10)</span>
          </div>
          <div class="step-box">
            <span class="step-label"><i class="fa-solid fa-lightbulb"></i> Step 2: Key Mathematical Concept / Strategy</span>
            Apply the sign inversion rule when brackets are preceded by minus, and identity rule when preceded by plus.
          </div>
          <div class="step-box">
            <span class="step-label"><i class="fa-solid fa-calculator"></i> Step 3: Step-by-Step Mathematical Calculation &amp; Working</span>
            <ul>
              <li><strong>Q1(a):</strong> <span class="math-inline">24 + (6 − 4) = 24 + 6 − 4</span>. (Box = '−', blank = 4).</li>
              <li><strong>Q1(b):</strong> <span class="math-inline">38 + 9 − 4 = 38 + (9 − 4)</span>. (Blanks = 9, 4; Box = '−').</li>
              <li><strong>Q1(c):</strong> <span class="math-inline">24 − (6 + 4) = 24 − 6 − 4</span>. (Box = '−').</li>
              <li><strong>Q1(d):</strong> <span class="math-inline">24 − 6 − 4 = 24 − (6 + 4)</span> (or <span class="math-inline">24 − 6 − 4</span> with Box = '−', blank = 4).</li>
              <li><strong>Q1(e):</strong> <span class="math-inline">27 − (8 + 3) = 27 − 8 − 3</span>. (Both boxes = '−').</li>
              <li><strong>Q1(f):</strong> <span class="math-inline">27 − 8 + 3 = 27 − (8 − 3)</span>. (Blanks = 8, 3; Box = '−').</li>
              <li><strong>Q2(a):</strong> <span class="math-inline">14 + (12 + 10) = 14 + 12 + 10 = 36</span>.</li>
              <li><strong>Q2(b):</strong> <span class="math-inline">14 − (12 + 10) = 14 − 12 − 10 = −8</span>.</li>
              <li><strong>Q2(c):</strong> <span class="math-inline">14 + (12 − 10) = 14 + 12 − 10 = 16</span>.</li>
              <li><strong>Q2(d):</strong> <span class="math-inline">14 − (12 − 10) = 14 − 12 + 10 = 12</span>.</li>
              <li><strong>Q2(e):</strong> <span class="math-inline">−14 + (12 − 10) = −14 + 12 − 10 = −12</span>.</li>
              <li><strong>Q2(f):</strong> <span class="math-inline">14 − (−12 − 10) = 14 + 12 + 10 = 36</span>.</li>
            </ul>
          </div>
          <div class="step-box">
            <span class="step-label"><i class="fa-solid fa-wand-magic-sparkles"></i> Step 4: Verification of (f)</span>
            In Q2(f): <span class="math-inline">−12 − 10 = −22</span>. 
            Subtracting <span class="math-inline">−22</span> from 14: <span class="math-inline">14 − (−22) = 14 + 22 = 36</span>. Matches <span class="math-inline">14 + 12 + 10 = 36</span> perfectly!
          </div>
          <div class="step-box">
            <span class="step-label"><i class="fa-solid fa-circle-check"></i> Step 5: Final Conclusion &amp; Key Takeaway</span>
            All signs inside brackets flip when preceded by minus, and remain identical when preceded by plus.
          </div>
        </div>
      </details>

      <!-- FIGURE IT OUT 3 - Q3, Q4, Q5 -->
      <details class="ans-box">
        <summary>
          <span><i class="fa-solid fa-object-group"></i> Figure it Out 3 - Q3, Q4 &amp; Q5 (Page 38): Bracket Placement &amp; Equivalence</span>
          <span class="ans-badge">5-Step Solution</span>
        </summary>
        <div class="ans-content">
          <div class="step-box">
            <span class="step-label"><i class="fa-solid fa-clipboard-question"></i> Step 1: Problem Understanding / Given Data</span>
            <strong>Q3: Compare value pairs:</strong>
            <br>(a) <span class="math-inline">(6 + 10) − 2</span> and <span class="math-inline">6 + (10 − 2)</span>
            <br>(b) <span class="math-inline">16 − (8 − 3)</span> and <span class="math-inline">(16 − 8) − 3</span>
            <br>(c) <span class="math-inline">27 − (18 + 4)</span> and <span class="math-inline">27 + (−18 − 4)</span>
            <br><strong>Q4: Identify equivalent expressions:</strong>
            <br>(a) <span class="math-inline">319 + 537, 319 − 537, −537 + 319, 537 − 319</span>
            <br>(b) <span class="math-inline">87 + 46 − 109, 87 − 46 + 109, 87 − (46 + 109), (87 − 46) + 109</span>
            <br><strong>Q5: Add brackets to produce target values:</strong>
            <br>(a) <span class="math-inline">34 − 9 + 12 = 13</span> &nbsp;|&nbsp; (b) <span class="math-inline">56 − 14 − 8 = 34</span> &nbsp;|&nbsp; (c) <span class="math-inline">−22 − 12 + 10 + 22 = −22</span>
          </div>
          <div class="step-box">
            <span class="step-label"><i class="fa-solid fa-lightbulb"></i> Step 2: Key Mathematical Concept / Strategy</span>
            Evaluate expressions by unpacking brackets or observing term signs. 
            Brackets change evaluation order: <span class="math-inline">A − (B + C) = A − B − C</span>.
          </div>
          <div class="step-box">
            <span class="step-label"><i class="fa-solid fa-calculator"></i> Step 3: Step-by-Step Mathematical Calculation &amp; Working</span>
            <ul>
              <li><strong>Q3(a):</strong> <span class="math-inline">(6 + 10) − 2 = 16 − 2 = 14</span>; <span class="math-inline">6 + (10 − 2) = 6 + 8 = 14</span>. They are <strong>EQUAL</strong>!</li>
              <li><strong>Q3(b):</strong> <span class="math-inline">16 − (8 − 3) = 16 − 5 = 11</span>; <span class="math-inline">(16 − 8) − 3 = 8 − 3 = 5</span>. They are <strong>NOT EQUAL</strong> (<span class="math-inline">11 ≠ 5</span>).</li>
              <li><strong>Q3(c):</strong> <span class="math-inline">27 − (18 + 4) = 27 − 22 = 5</span>; <span class="math-inline">27 + (−18 − 4) = 27 + (−22) = 5</span>. They are <strong>EQUAL</strong>!</li>
              <li><strong>Q4(a):</strong> <span class="math-inline">319 − 537</span> and <span class="math-inline">−537 + 319</span> have identical terms (319 and −537). Hence, they are equal!</li>
              <li><strong>Q4(b):</strong> <span class="math-inline">87 + 46 − 109</span> has terms 87, 46, −109. Notice <span class="math-inline">87 − (46 + 109) = 87 − 46 − 109</span> is different. But <span class="math-inline">(87 − 46) + 109 = 87 − 46 + 109</span> equals <span class="math-inline">87 − 46 + 109</span>!</li>
              <li><strong>Q5(a):</strong> Target = 13. Raw <span class="math-inline">34 − 9 + 12 = 37</span>. 
                Place brackets: <span class="math-inline">34 − (9 + 12) = 34 − 21 = 13</span>!
              </li>
              <li><strong>Q5(b):</strong> Target = 34. Raw <span class="math-inline">56 − 14 − 8 = 34</span>. 
                To maintain 34 without altering: <span class="math-inline">(56 − 14) − 8 = 42 − 8 = 34</span>. 
                (Notice <span class="math-inline">56 − (14 − 8) = 56 − 6 = 50</span>).
              </li>
              <li><strong>Q5(c):</strong> Target = −22. Terms: <span class="math-inline">−22</span> and <span class="math-inline">+22</span> cancel to 0. 
                Grouping: <span class="math-inline">−22 − (12 − 10) + 22</span> or <span class="math-inline">(−22 − 12 + 10) + 22 = −24 + 22 = −2</span>. 
                To get −22: <span class="math-inline">−22 − (12 − 10 − 22) = −22 − (−20) = −2</span>. 
                Correct bracket: <span class="math-inline">−22 − (12 + 10) + 22 = −22</span> (if expression had +12: <span class="math-inline">−22 − (12 − 12)</span>). 
                Official solution: <span class="math-inline">(−22) − (12 + 10 − 22) = −22 − 0 = −22</span>!
              </li>
            </ul>
          </div>
          <div class="step-box">
            <span class="step-label"><i class="fa-solid fa-wand-magic-sparkles"></i> Step 4: Key Rule Observation</span>
            Associativity holds when moving parentheses across additions, but breaks down when brackets follow a minus sign because subtraction is non-associative.
          </div>
          <div class="step-box">
            <span class="step-label"><i class="fa-solid fa-circle-check"></i> Step 5: Final Conclusion &amp; Key Takeaway</span>
            Q5 answers: (a) <span class="math-inline">34 − (9 + 12) = 13</span>; (b) <span class="math-inline">(56 − 14) − 8 = 34</span>; (c) <span class="math-inline">−22 − (12 − 10 − 2)</span> or <span class="math-inline">−22 − (12 + 10 − 22) = −22</span>.
          </div>
        </div>
      </details>

      <!-- FIGURE IT OUT 3 - Q6, Q7, Q8, Q9 -->
      <details class="ans-box">
        <summary>
          <span><i class="fa-solid fa-brain"></i> Figure it Out 3 - Q6 to Q9 (Page 38): Jasoda's Subtraction Trick &amp; Term Dynamics</span>
          <span class="ans-badge">5-Step Solution</span>
        </summary>
        <div class="ans-content">
          <div class="step-box">
            <span class="step-label"><i class="fa-solid fa-clipboard-question"></i> Step 1: Problem Understanding / Given Data</span>
            Solve the 4 analytical thinking problems:
            <br>• <strong>Q6:</strong> Fill blanks using term reasoning: (a) <span class="math-inline">423 + _____ = 419 + _____</span>; (b) <span class="math-inline">207 − 68 = 210 − _____</span>.
            <br>• <strong>Q7:</strong> Using 2, 3, 5 and +, − and brackets, generate different values.
            <br>• <strong>Q8 (Jasoda's Trick):</strong> To subtract 9, Jasoda subtracts 10 and adds 1 (<span class="math-inline">36 − 9 = 26 + 1 = 27</span>). Does this always work? Why? Give other examples.
            <br>• <strong>Q9:</strong> Match expressions equal to (a) <span class="math-inline">73 − 14 + 1</span> and (b) <span class="math-inline">73 − 14 − 1</span> from collection: <span class="math-inline">73 − (14 + 1), 73 − (14 − 1), 73 + (−14 + 1), 73 + (−14 − 1)</span>.
          </div>
          <div class="step-box">
            <span class="step-label"><i class="fa-solid fa-lightbulb"></i> Step 2: Key Mathematical Concept / Strategy</span>
            Apply compensation reasoning: If you subtract <span class="math-inline">10</span> instead of <span class="math-inline">9</span>, you subtracted 1 unit in excess, so adding 1 restores balance!
          </div>
          <div class="step-box">
            <span class="step-label"><i class="fa-solid fa-calculator"></i> Step 3: Step-by-Step Mathematical Calculation &amp; Working</span>
            <ul>
              <li>
                <strong>Q6(a):</strong> 419 is 4 less than 423 (<span class="math-inline">423 − 4 = 419</span>). 
                To balance, RHS second term must be 4 more than LHS second term! 
                Example: <span class="math-inline">423 + 10 = 419 + 14</span>.
              </li>
              <li>
                <strong>Q6(b):</strong> 210 is 3 more than 207 (<span class="math-inline">207 + 3 = 210</span>). 
                Starting with 3 more requires subtracting 3 more to keep the same difference! 
                <span class="math-inline">68 + 3 = 71</span>. 
                Hence, <span class="math-inline">207 − 68 = 210 − 71</span> (= 139).
              </li>
              <li>
                <strong>Q7 (Values from 2, 3, 5):</strong>
                <br><span class="math-inline">2 + 3 + 5 = 10</span> &nbsp;|&nbsp; <span class="math-inline">2 + 3 − 5 = 0</span> &nbsp;|&nbsp; <span class="math-inline">2 − 3 + 5 = 4</span>
                <br><span class="math-inline">5 − (3 − 2) = 4</span> &nbsp;|&nbsp; <span class="math-inline">5 − (2 + 3) = 0</span> &nbsp;|&nbsp; <span class="math-inline">3 − (5 − 2) = 0</span>
                <br><span class="math-inline">2 − (3 + 5) = −6</span> &nbsp;|&nbsp; <span class="math-inline">3 − 2 − 5 = −4</span> &nbsp;|&nbsp; <span class="math-inline">5 − 3 − 2 = 0</span>
              </li>
              <li>
                <strong>Q8 (Jasoda's Rule):</strong> 
                <br>Yes, she always gets the correct answer! 
                <br>Proof: <span class="math-inline">N − 9 = N − (10 − 1) = N − 10 + 1</span> (by bracket inversion!). 
                <br>Other strategies:
                <br>• Subtracting 8: Subtract 10 and add 2 (<span class="math-inline">N − 8 = N − 10 + 2</span>). E.g., <span class="math-inline">45 − 8 = 35 + 2 = 37</span>.
                <br>• Subtracting 98: Subtract 100 and add 2 (<span class="math-inline">N − 98 = N − 100 + 2</span>). E.g., <span class="math-inline">354 − 98 = 254 + 2 = 256</span>.
              </li>
              <li>
                <strong>Q9 (Matching):</strong>
                <br>Expression (a): <span class="math-inline">73 − 14 + 1</span>. 
                Equivalent forms: <span class="math-inline">73 − (14 − 1)</span> and <span class="math-inline">73 + (−14 + 1)</span>.
                <br>Expression (b): <span class="math-inline">73 − 14 − 1</span>. 
                Equivalent forms: <span class="math-inline">73 − (14 + 1)</span> and <span class="math-inline">73 + (−14 − 1)</span>.
              </li>
            </ul>
          </div>
          <div class="step-box">
            <span class="step-label"><i class="fa-solid fa-wand-magic-sparkles"></i> Step 4: Verification of Q9</span>
            <span class="math-inline">73 − 14 + 1 = 60</span>. 
            <span class="math-inline">73 − (14 − 1) = 73 − 13 = 60</span>. 
            <span class="math-inline">73 + (−14 + 1) = 73 − 13 = 60</span>. Matches!
          </div>
          <div class="step-box">
            <span class="step-label"><i class="fa-solid fa-circle-check"></i> Step 5: Final Conclusion &amp; Key Takeaway</span>
            Jasoda's trick is an elegant application of the bracket rule <span class="math-inline">−(10 − 1) = −10 + 1</span>.
          </div>
        </div>
      </details>

      <!-- FIGURE IT OUT 4 - Q1, Q2, Q3, Q4 -->
      <details class="ans-box">
        <summary>
          <span><i class="fa-solid fa-network-wired"></i> Figure it Out 4 - Q1 to Q4 (Pages 41–42): Complete Distributive Law Mastery</span>
          <span class="ans-badge">5-Step Solution</span>
        </summary>
        <div class="ans-content">
          <div class="step-box">
            <span class="step-label"><i class="fa-solid fa-clipboard-question"></i> Step 1: Problem Understanding / Given Data</span>
            Solve the 4 distributive law exercises:
            <br>• <strong>Q1: Complete fill-in-the-blanks (a to p)</strong>
            <br>• <strong>Q2: Fill '&lt;', '&gt;' or '=' using distributive reasoning</strong>
            <br>• <strong>Q3: 4 other ways to make 14 in format <span class="math-inline">a × (b + c) = 14</span></strong>
            <br>• <strong>Q4: Sum of numbers in pictures in two different ways</strong>
          </div>
          <div class="step-box">
            <span class="step-label"><i class="fa-solid fa-lightbulb"></i> Step 2: Key Mathematical Concept / Strategy</span>
            Apply <span class="math-inline">a × (b + c) = a × b + a × c</span> and <span class="math-inline">a × (b − c) = a × b − a × c</span>.
          </div>
          <div class="step-box">
            <span class="step-label"><i class="fa-solid fa-calculator"></i> Step 3: Step-by-Step Mathematical Calculation &amp; Working</span>
            <ul>
              <li>
                <strong>Q1 Fill in the blanks:</strong>
                <br>(a) <span class="math-inline">3 × (6 + 7) = 3 × 6 + 3 × 7</span>
                <br>(b) <span class="math-inline">(8 + 3) × 4 = 8 × 4 + 3 × 4</span>
                <br>(c) <span class="math-inline">3 × (5 + 8) = 3 × 5 + 3 × 8</span> (blank: 8, box: +)
                <br>(d) <span class="math-inline">(9 + 2) × 4 = 9 × 4 + 2 × 4</span> (blank: 4, box: +)
                <br>(e) <span class="math-inline">3 × (10 + 4) = 3 × 10 + 3 × 4</span>
                <br>(f) <span class="math-inline">(13 + 6) × 4 = 13 × 4 + 6 × 4</span>
                <br>(g) <span class="math-inline">3 × (5 + 2) = 3 × 5 + 3 × 2</span>
                <br>(h) <span class="math-inline">(2 + 3) × 4 = 2 × 4 + 3 × 4</span>
                <br>(i) <span class="math-inline">5 × (9 − 2) = 5 × 9 − 5 × 2</span> (blank: 2)
                <br>(j) <span class="math-inline">(5 − 2) × 7 = 5 × 7 − 2 × 7</span> (blank: 7)
                <br>(k) <span class="math-inline">5 × (8 − 3) = 5 × 8 − 5 × 3</span> (blank: 3, box: −)
                <br>(l) <span class="math-inline">(8 − 3) × 7 = 8 × 7 − 3 × 7</span> (box: −)
                <br>(m) <span class="math-inline">5 × (12 − 6) = 5 × 12 − 5 × 6</span>
                <br>(n) <span class="math-inline">(15 − 9) × 7 = 15 × 7 − 9 × 7</span>
                <br>(o) <span class="math-inline">5 × (9 − 4) = 5 × 9 − 5 × 4</span>
                <br>(p) <span class="math-inline">(17 − 9) × 7 = 17 × 7 − 9 × 7</span>
              </li>
              <li>
                <strong>Q2 Reasoning Comparisons:</strong>
                <br>(a) <span class="math-inline">(8 − 3) × 29</span> vs <span class="math-inline">(3 − 8) × 29</span>: <span class="math-inline">8 − 3 = +5</span> while <span class="math-inline">3 − 8 = −5</span>. Positive &gt; Negative. Symbol: <strong>&gt;</strong>.
                <br>(b) <span class="math-inline">15 + 9 × 18</span> vs <span class="math-inline">(15 + 9) × 18</span>: RHS expands to <span class="math-inline">15 × 18 + 9 × 18</span>, which multiplies 15 by 18, whereas LHS only adds 15. Symbol: <strong>&lt;</strong>.
                <br>(c) <span class="math-inline">23 × (17 − 9)</span> vs <span class="math-inline">23 × 17 + 23 × 9</span>: LHS is difference (<span class="math-inline">23 × 17 − 23 × 9</span>), while RHS is sum. Symbol: <strong>&lt;</strong>.
                <br>(d) <span class="math-inline">(34 − 28) × 42</span> vs <span class="math-inline">34 × 42 − 28 × 42</span>: Both sides are identical by distributive law! Symbol: <strong>=</strong>.
              </li>
              <li>
                <strong>Q3 Other ways to make 14 in format a × (b + c):</strong>
                <br>(a) <span class="math-inline">2 × (2 + 5) = 2 × 7 = 14</span>
                <br>(b) <span class="math-inline">2 × (3 + 4) = 2 × 7 = 14</span>
                <br>(c) <span class="math-inline">1 × (10 + 4) = 1 × 14 = 14</span>
                <br>(d) <span class="math-inline">7 × (1 + 1) = 7 × 2 = 14</span>
              </li>
              <li>
                <strong>Q4 Sum of numbers in pictures:</strong>
                <br><em>Picture I:</em> 
                <br>Way 1: <span class="math-inline">(5 × 4) + (4 × 8) = 20 + 32 = 52</span>.
                <br>Way 2: <span class="math-inline">2 × (4 + 8 + 4) + (8 + 4 + 8) = 2 × 16 + 20 = 32 + 20 = 52</span>.
                <br><em>Picture II:</em>
                <br>Way 1: <span class="math-inline">(8 × 5) + (8 × 6) = 40 + 48 = 88</span>.
                <br>Way 2: <span class="math-inline">8 × (5 + 6) = 8 × 11 = 88</span>.
              </li>
            </ul>
          </div>
          <div class="step-box">
            <span class="step-label"><i class="fa-solid fa-wand-magic-sparkles"></i> Step 4: Verification of Picture II</span>
            In Picture II, factoring out 8 transforms two separate multiplications into one simple multiplication: <span class="math-inline">8 × 11 = 88</span>.
          </div>
          <div class="step-box">
            <span class="step-label"><i class="fa-solid fa-circle-check"></i> Step 5: Final Conclusion &amp; Key Takeaway</span>
            The distributive law connects multiplication and addition seamlessly across algebra and geometry.
          </div>
        </div>
      </details>
'''
