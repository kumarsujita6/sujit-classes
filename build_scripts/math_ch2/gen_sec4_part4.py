# -*- coding: utf-8 -*-
"""
Section 4 - Part 4: End-of-Chapter Master Exercises & Expression Engineer (Pages 42–45)
"""

def get_sec4_part4():
    return '''
      <!-- PART 4: END-OF-CHAPTER MASTER EXERCISE (FIGURE IT OUT 5) & EXPRESSION ENGINEER -->
      <h3><i class="fa-solid fa-circle-play"></i> Part 4: Master Synthesis Exercises &amp; Expression Engineer (Pages 42–45)</h3>

      <!-- FIGURE IT OUT 5 - Q1 -->
      <details class="ans-box">
        <summary>
          <span><i class="fa-solid fa-seedling"></i> Figure it Out 5 - Q1 (Pages 42–43): Begur Mango Market, Binu's Savings &amp; Snail Post Puzzle</span>
          <span class="ans-badge">5-Step Solution</span>
        </summary>
        <div class="ans-content">
          <div class="step-box">
            <span class="step-label"><i class="fa-solid fa-clipboard-question"></i> Step 1: Problem Understanding / Given Data</span>
            Solve the 3 comprehensive real-life word problems:
            <br>• <strong>(a) Begur Mango Market:</strong> Market runs 7 days/week. Rahim supplies 9 kg/day, Shyam supplies 11 kg/day. Find total mangoes supplied in a week.
            <br>• <strong>(b) Binu's Annual Savings:</strong> Binu earns ₹20,000/month. Monthly expenses: ₹5,000 rent, ₹5,000 food, ₹2,000 other. What is her total savings by the end of 1 year (12 months)?
            <br>• <strong>(c) Snail on the 10 cm Post:</strong> Post height = 10 cm. Snail climbs 3 cm during daytime, and slips down 2 cm during the night while asleep. Delicious treat is at 10 cm top. In how many days will the snail reach the treat?
          </div>
          <div class="step-box">
            <span class="step-label"><i class="fa-solid fa-lightbulb"></i> Step 2: Key Mathematical Concept / Strategy</span>
            • (a) Total = <span class="math-inline">7 × (Rahim + Shyam)</span> (Distributive Law).
            <br>• (b) Annual Savings = <span class="math-inline">12 × [Income − (Rent + Food + Other)]</span>.
            <br>• (c) <strong>Critical Snail Logic:</strong> Once the snail touches the treat at 10 cm during daytime, it DOES NOT slip back down! It has already reached the treat.
          </div>
          <div class="step-box">
            <span class="step-label"><i class="fa-solid fa-calculator"></i> Step 3: Step-by-Step Mathematical Calculation &amp; Working</span>
            <ul>
              <li>
                <strong>Part (a) Mango Supply:</strong>
                <br><em>Method 1:</em> <span class="math-inline">7 × (9 + 11) = 7 × 20 = 140</span> kg.
                <br><em>Method 2:</em> <span class="math-inline">7 × 9 + 7 × 11 = 63 + 77 = 140</span> kg.
                <br>Total mangoes supplied = <strong>140 kg</strong>.
              </li>
              <li>
                <strong>Part (b) Binu's Annual Savings:</strong>
                <br>Monthly expenditure = <span class="math-inline">5000 + 5000 + 2000 = 12000</span> rupees.
                <br>Monthly savings = <span class="math-inline">20000 − 12000 = 8000</span> rupees.
                <br>Annual expression = <span class="math-inline">12 × [20000 − (5000 + 5000 + 2000)] = 12 × 8000 = 96000</span>.
                <br>Total savings by year end = <strong>₹96,000</strong>.
              </li>
              <li>
                <strong>Part (c) The Snail Climbing Puzzle:</strong>
                <br>Daily net progress (Day climb − Night slip) = <span class="math-inline">3 − 2 = 1</span> cm per 24-hour cycle.
                <br>Let us track day-by-day progress:
                <br>• End of Day 1 (after night): <span class="math-inline">1 × 1 = 1</span> cm
                <br>• End of Day 2: <span class="math-inline">2 × 1 = 2</span> cm
                <br>• End of Day 7 (after night): <span class="math-inline">7 × 1 = 7</span> cm height.
                <br>• <strong>On Day 8 Daytime:</strong> Snail starts at 7 cm and climbs 3 cm:
                <div class="math-display">7 + 3 = 10  cm</div>
                The snail reaches the top and gets the treat on <strong>Day 8</strong> before nightfall!
              </li>
            </ul>
          </div>
          <div class="step-box">
            <span class="step-label"><i class="fa-solid fa-wand-magic-sparkles"></i> Step 4: The Classic Trap in Part (c)</span>
            Students who naively calculate <span class="math-inline">10 ÷ 1 = 10  days</span> forget that on Day 8, the snail reaches the top and eats the treat; it does not slip down at night!
          </div>
          <div class="step-box">
            <span class="step-label"><i class="fa-solid fa-circle-check"></i> Step 5: Final Conclusion &amp; Key Takeaway</span>
            (a) 140 kg mangoes; (b) ₹96,000 savings; (c) The snail reaches the treat in <strong>8 days</strong>!
          </div>
        </div>
      </details>

      <!-- FIGURE IT OUT 5 - Q2 -->
      <details class="ans-box">
        <summary>
          <span><i class="fa-solid fa-book-open"></i> Figure it Out 5 - Q2 (Page 43): Melvin's Reading Schedule</span>
          <span class="ans-badge">5-Step Solution</span>
        </summary>
        <div class="ans-content">
          <div class="step-box">
            <span class="step-label"><i class="fa-solid fa-clipboard-question"></i> Step 1: Problem Understanding / Given Data</span>
            Melvin reads a two-page story every day EXCEPT on Tuesdays and Saturdays. 
            How many stories would he complete reading in 8 weeks? 
            Which of the expressions below describe this scenario?
            <br>(a) <span class="math-inline">5 × 2 × 8</span> &nbsp;|&nbsp; (b) <span class="math-inline">(7 − 2) × 8</span> &nbsp;|&nbsp; (c) <span class="math-inline">8 × 7</span> &nbsp;|&nbsp; (d) <span class="math-inline">7 × 2 × 8</span>
            <br>(e) <span class="math-inline">7 × 5 − 2</span> &nbsp;|&nbsp; (f) <span class="math-inline">(7 + 2) × 8</span> &nbsp;|&nbsp; (g) <span class="math-inline">7 × 8 − 2 × 8</span> &nbsp;|&nbsp; (h) <span class="math-inline">(7 − 5) × 8</span>
          </div>
          <div class="step-box">
            <span class="step-label"><i class="fa-solid fa-lightbulb"></i> Step 2: Key Mathematical Concept / Strategy</span>
            A week has 7 days. Melvin skips 2 days (Tuesday and Saturday). 
            Therefore, he reads on <span class="math-inline">7 − 2 = 5</span> days each week. 
            On each reading day, he completes <strong>1 story</strong> (which is a two-page story). 
            Thus, stories per week = <span class="math-inline">(7 − 2) = 5</span> stories. 
            For 8 weeks, total stories = <span class="math-inline">(7 − 2) × 8</span>.
          </div>
          <div class="step-box">
            <span class="step-label"><i class="fa-solid fa-calculator"></i> Step 3: Step-by-Step Mathematical Calculation &amp; Working</span>
            <ul>
              <li>Reading days per week = <span class="math-inline">7 − 2 = 5</span> days.</li>
              <li>Stories read per week = 5 stories (1 story every reading day).</li>
              <li>Total stories in 8 weeks = <span class="math-inline">5 × 8 = 40</span> stories.</li>
              <li>Examining the expressions:
                <br>• (b) <span class="math-inline">(7 − 2) × 8 = 5 × 8 = 40</span> &rarr; <strong>MATCHES!</strong>
                <br>• (g) <span class="math-inline">7 × 8 − 2 × 8 = 56 − 16 = 40</span> &rarr; <strong>MATCHES!</strong> (Distributive expansion of (b)).
                <br>• (a) <span class="math-inline">5 × 2 × 8 = 80</span> represents the <em>total pages read</em>, not the number of stories!
              </li>
            </ul>
          </div>
          <div class="step-box">
            <span class="step-label"><i class="fa-solid fa-wand-magic-sparkles"></i> Step 4: Linguistic Distinction</span>
            Always distinguish between "number of stories" (40) and "number of pages" (80). The question explicitly asked for <em>how many stories</em>!
          </div>
          <div class="step-box">
            <span class="step-label"><i class="fa-solid fa-circle-check"></i> Step 5: Final Conclusion &amp; Key Takeaway</span>
            The expressions describing the total stories completed are <strong>(b) (7 − 2) × 8</strong> and <strong>(g) 7 × 8 − 2 × 8</strong>. Value = <strong>40 stories</strong>.
          </div>
        </div>
      </details>

      <!-- FIGURE IT OUT 5 - Q3 -->
      <details class="ans-box">
        <summary>
          <span><i class="fa-solid fa-plus-minus"></i> Figure it Out 5 - Q3 (Page 43): Alternating Sign Series Evaluation</span>
          <span class="ans-badge">5-Step Solution</span>
        </summary>
        <div class="ans-content">
          <div class="step-box">
            <span class="step-label"><i class="fa-solid fa-clipboard-question"></i> Step 1: Problem Understanding / Given Data</span>
            Find different ways of evaluating the following expressions:
            <br>(a) <span class="math-inline">1 − 2 + 3 − 4 + 5 − 6 + 7 − 8 + 9 − 10</span>
            <br>(b) <span class="math-inline">1 − 1 + 1 − 1 + 1 − 1 + 1 − 1 + 1 − 1</span>
          </div>
          <div class="step-box">
            <span class="step-label"><i class="fa-solid fa-lightbulb"></i> Step 2: Key Mathematical Concept / Strategy</span>
            Take advantage of the Commutative and Associative Properties:
            <br>• Way 1: Group adjacent pairs of consecutive terms.
            <br>• Way 2: Separate all positive terms and all negative terms into two distinct sums.
          </div>
          <div class="step-box">
            <span class="step-label"><i class="fa-solid fa-calculator"></i> Step 3: Step-by-Step Mathematical Calculation &amp; Working</span>
            <ul>
              <li>
                <strong>Part (a): 1 − 2 + 3 − 4 + 5 − 6 + 7 − 8 + 9 − 10</strong>
                <br><em>Way 1 (Pairing consecutive neighbors):</em>
                <br>Group into 5 pairs: <span class="math-inline">(1 − 2) + (3 − 4) + (5 − 6) + (7 − 8) + (9 − 10)</span>
                <br><span class="math-inline">= (−1) + (−1) + (−1) + (−1) + (−1) = 5 × (−1) = −5</span>.
                <br><em>Way 2 (Separating positive and negative terms):</em>
                <br>Sum of positives = <span class="math-inline">1 + 3 + 5 + 7 + 9 = 25</span>.
                <br>Sum of negatives = <span class="math-inline">−(2 + 4 + 6 + 8 + 10) = −30</span>.
                <br>Total = <span class="math-inline">25 − 30 = −5</span>.
              </li>
              <li>
                <strong>Part (b): 1 − 1 + 1 − 1 + 1 − 1 + 1 − 1 + 1 − 1</strong>
                <br><em>Way 1 (Zero-pair grouping):</em>
                <br><span class="math-inline">(1 − 1) + (1 − 1) + (1 − 1) + (1 − 1) + (1 − 1) = 0 + 0 + 0 + 0 + 0 = 0</span>.
                <br><em>Way 2 (Tallying 1s):</em>
                <br>There are 5 positive ones (+5) and 5 negative ones (−5): <span class="math-inline">5 − 5 = 0</span>.
              </li>
            </ul>
          </div>
          <div class="step-box">
            <span class="step-label"><i class="fa-solid fa-wand-magic-sparkles"></i> Step 4: General Pattern Insight</span>
            For any alternating series of natural numbers from 1 to <span class="math-inline">2n</span>, the sum is always equal to <span class="math-inline">−n</span>. Here <span class="math-inline">2n = 10 ⇒ n = 5 ⇒ Sum = −5</span>!
          </div>
          <div class="step-box">
            <span class="step-label"><i class="fa-solid fa-circle-check"></i> Step 5: Final Conclusion &amp; Key Takeaway</span>
            The evaluated values are: <strong>(a) −5</strong> and <strong>(b) 0</strong>.
          </div>
        </div>
      </details>

      <!-- FIGURE IT OUT 5 - Q4 -->
      <details class="ans-box">
        <summary>
          <span><i class="fa-solid fa-code-compare"></i> Figure it Out 5 - Q4 (Pages 43–44): Deep Pairwise Expression Comparison</span>
          <span class="ans-badge">5-Step Solution</span>
        </summary>
        <div class="ans-content">
          <div class="step-box">
            <span class="step-label"><i class="fa-solid fa-clipboard-question"></i> Step 1: Problem Understanding / Given Data</span>
            Compare the eight pairs of expressions using '&lt;', '&gt;', or '=' by reasoning rather than routine calculations:
            <br>(a) <span class="math-inline">49 − 7 + 8</span> _____ <span class="math-inline">49 − 7 + 8</span>
            <br>(b) <span class="math-inline">83 × 42 − 18</span> _____ <span class="math-inline">83 × 40 − 18</span>
            <br>(c) <span class="math-inline">145 − 17 × 8</span> _____ <span class="math-inline">145 − 17 × 6</span>
            <br>(d) <span class="math-inline">23 × 48 − 35</span> _____ <span class="math-inline">23 × (48 − 35)</span>
            <br>(e) <span class="math-inline">(16 − 11) × 12</span> _____ <span class="math-inline">−11 × 12 + 16 × 12</span>
            <br>(f) <span class="math-inline">(76 − 53) × 88</span> _____ <span class="math-inline">88 × (53 − 76)</span>
            <br>(g) <span class="math-inline">25 × (42 + 16)</span> _____ <span class="math-inline">25 × (43 + 15)</span>
            <br>(h) <span class="math-inline">36 × (28 − 16)</span> _____ <span class="math-inline">35 × (27 − 15)</span>
          </div>
          <div class="step-box">
            <span class="step-label"><i class="fa-solid fa-lightbulb"></i> Step 2: Key Mathematical Concept / Strategy</span>
            Apply properties of operations (order, distributivity, common factor comparison, sign comparison).
          </div>
          <div class="step-box">
            <span class="step-label"><i class="fa-solid fa-calculator"></i> Step 3: Step-by-Step Mathematical Calculation &amp; Working</span>
            <ul>
              <li><strong>(a):</strong> Identical expressions on both sides. Symbol: <strong>=</strong>.</li>
              <li><strong>(b):</strong> Both expressions subtract 18. Since <span class="math-inline">42 &gt; 40</span>, <span class="math-inline">83 × 42 &gt; 83 × 40</span>. Symbol: <strong>&gt;</strong>.</li>
              <li><strong>(c):</strong> Both start at 145. Subtracting 8 groups of 17 removes more than subtracting 6 groups of 17. Symbol: <strong>&lt;</strong>.</li>
              <li><strong>(d):</strong> RHS expands to <span class="math-inline">23 × 48 − 23 × 35</span>. LHS only subtracts 35 (1 group of 35), while RHS subtracts 23 groups of 35. Therefore LHS &gt; RHS. Symbol: <strong>&gt;</strong>.</li>
              <li><strong>(e):</strong> LHS expands by distributive law to <span class="math-inline">16 × 12 − 11 × 12</span>. RHS has identical terms swapped commutatively. Symbol: <strong>=</strong>.</li>
              <li><strong>(f):</strong> LHS = <span class="math-inline">(+23) × 88 &gt; 0</span>. RHS = <span class="math-inline">88 × (−23) &lt; 0</span>. Positive is always greater than negative. Symbol: <strong>&gt;</strong>.</li>
              <li><strong>(g):</strong> <span class="math-inline">42 + 16 = 58</span> and <span class="math-inline">43 + 15 = 58</span>. Both evaluate to <span class="math-inline">25 × 58</span>. Symbol: <strong>=</strong>.</li>
              <li><strong>(h):</strong> In LHS, <span class="math-inline">28 − 16 = 12</span>, so LHS = <span class="math-inline">36 × 12</span>. In RHS, <span class="math-inline">27 − 15 = 12</span>, so RHS = <span class="math-inline">35 × 12</span>. Since <span class="math-inline">36 &gt; 35</span>, LHS &gt; RHS. Symbol: <strong>&gt;</strong>.</li>
            </ul>
          </div>
          <div class="step-box">
            <span class="step-label"><i class="fa-solid fa-wand-magic-sparkles"></i> Step 4: Rapid Mental Check</span>
            (a) 50 = 50 | (b) 3468 &gt; 3302 | (c) 9 &lt; 43 | (d) 1069 &gt; 299 | (e) 60 = 60 | (f) 2024 &gt; −2024 | (g) 1450 = 1450 | (h) 432 &gt; 420.
          </div>
          <div class="step-box">
            <span class="step-label"><i class="fa-solid fa-circle-check"></i> Step 5: Final Conclusion &amp; Key Takeaway</span>
            The comparison results are: <strong>(a) =, (b) &gt;, (c) &lt;, (d) &gt;, (e) =, (f) &gt;, (g) =, (h) &gt;</strong>.
          </div>
        </div>
      </details>

      <!-- FIGURE IT OUT 5 - Q5 -->
      <details class="ans-box">
        <summary>
          <span><i class="fa-solid fa-filter"></i> Figure it Out 5 - Q5 (Page 44): Structural Equivalence Identification</span>
          <span class="ans-badge">5-Step Solution</span>
        </summary>
        <div class="ans-content">
          <div class="step-box">
            <span class="step-label"><i class="fa-solid fa-clipboard-question"></i> Step 1: Problem Understanding / Given Data</span>
            Identify which of the following expressions are equal to the given expression without computation:
            <br><strong>(a) Target: <span class="math-inline">83 − 37 − 12</span></strong>
            <br>(i) <span class="math-inline">84 − 38 − 12</span> &nbsp;|&nbsp; (ii) <span class="math-inline">84 − (37 + 12)</span> &nbsp;|&nbsp; (iii) <span class="math-inline">83 − 38 − 13</span> &nbsp;|&nbsp; (iv) <span class="math-inline">−37 + 83 − 12</span>
            <br><strong>(b) Target: <span class="math-inline">93 + 37 × 44 + 76</span></strong>
            <br>(i) <span class="math-inline">37 + 93 × 44 + 76</span> &nbsp;|&nbsp; (ii) <span class="math-inline">93 + 37 × 76 + 44</span> &nbsp;|&nbsp; (iii) <span class="math-inline">(93 + 37) × (44 + 76)</span> &nbsp;|&nbsp; (iv) <span class="math-inline">37 × 44 + 93 + 76</span>
          </div>
          <div class="step-box">
            <span class="step-label"><i class="fa-solid fa-lightbulb"></i> Step 2: Key Mathematical Concept / Strategy</span>
            Rewrite using terms:
            <br>In (a), terms are <strong>83, −37, −12</strong>. 
            <br>In (b), terms are <strong>93, 37 × 44, 76</strong>. By commutativity, terms can appear in any order!
          </div>
          <div class="step-box">
            <span class="step-label"><i class="fa-solid fa-calculator"></i> Step 3: Step-by-Step Mathematical Calculation &amp; Working</span>
            <ul>
              <li>
                <strong>Part (a): Target is 83 − 37 − 12 (= 34)</strong>
                <br>• Option (i): <span class="math-inline">84 − 38 − 12</span>. Notice 84 is +1 and 38 is +1, so <span class="math-inline">84 − 38 = 83 − 37</span>. 
                Thus <span class="math-inline">84 − 38 − 12 = 34</span> &rarr; <strong>EQUAL!</strong>
                <br>• Option (iv): <span class="math-inline">−37 + 83 − 12</span>. Terms are −37, 83, −12. This is simply a commutative rearrangement of the target's terms! &rarr; <strong>EQUAL!</strong>
                <br>• Options (ii) and (iii) change values and are NOT equal.
              </li>
              <li>
                <strong>Part (b): Target is 93 + 37 × 44 + 76 (= 1797)</strong>
                <br>• Option (iv): <span class="math-inline">37 × 44 + 93 + 76</span>. The terms are identical: <span class="math-inline">37 × 44</span>, <span class="math-inline">93</span>, and <span class="math-inline">76</span>, rearranged commutatively! &rarr; <strong>EQUAL!</strong>
                <br>• Options (i), (ii), and (iii) violate the structure of terms and are NOT equal.
              </li>
            </ul>
          </div>
          <div class="step-box">
            <span class="step-label"><i class="fa-solid fa-wand-magic-sparkles"></i> Step 4: Verification of (a)(i)</span>
            <span class="math-inline">84 − 38 = 46</span>, and <span class="math-inline">46 − 12 = 34</span>. Target: <span class="math-inline">83 − 37 = 46</span>, and <span class="math-inline">46 − 12 = 34</span>. Exact match!
          </div>
          <div class="step-box">
            <span class="step-label"><i class="fa-solid fa-circle-check"></i> Step 5: Final Conclusion &amp; Key Takeaway</span>
            Equal expressions are: <strong>For (a): (i) and (iv)</strong>; <strong>For (b): (iv)</strong>.
          </div>
        </div>
      </details>

      <!-- EXPRESSION ENGINEER ACTIVITY -->
      <details class="ans-box">
        <summary>
          <span><i class="fa-solid fa-gears"></i> Expression Engineer! (Page 45): The Four 4s &amp; Digit Puzzles</span>
          <span class="ans-badge">5-Step Solution</span>
        </summary>
        <div class="ans-content">
          <div class="step-box">
            <span class="step-label"><i class="fa-solid fa-clipboard-question"></i> Step 1: Problem Understanding / Given Data</span>
            Solve the 3 legendary "Expression Engineer" mathematical challenges:
            <br>1. Using exactly four 4s and operations (+, −, ×, ÷, brackets), create expressions for all integer values from 1 to 10.
            <br>2. Using the numbers 1, 2, 3, 4, 5 exactly once each, create expressions for values between −5 and +5.
            <br>3. Using the digits 0 to 9 exactly once each, make an expression with a value of 100.
          </div>
          <div class="step-box">
            <span class="step-label"><i class="fa-solid fa-lightbulb"></i> Step 2: Key Mathematical Concept / Strategy</span>
            Creative algebraic assembly: Use grouping brackets to alter order of operations, form fractions like <span class="math-inline">4/4 = 1</span>, and utilize <span class="math-inline">4 − 4 = 0</span>.
          </div>
          <div class="step-box">
            <span class="step-label"><i class="fa-solid fa-calculator"></i> Step 3: Step-by-Step Mathematical Calculation &amp; Working</span>
            <ul>
              <li><strong>Challenge 1: The Four 4s (Values 1 to 10):</strong>
                <br>• Value 1: <span class="math-inline">(4 + 4) ÷ (4 + 4) = 8 ÷ 8 = 1</span> (or <span class="math-inline">4/4 + 4 − 4 = 1</span>)
                <br>• Value 2: <span class="math-inline">(4 ÷ 4) + (4 ÷ 4) = 1 + 1 = 2</span>
                <br>• Value 3: <span class="math-inline">(4 + 4 + 4) ÷ 4 = 12 ÷ 4 = 3</span>
                <br>• Value 4: <span class="math-inline">4 + (4 − 4) ÷ 4 = 4 + 0 = 4</span>
                <br>• Value 5: <span class="math-inline">(4 × 4 + 4) ÷ 4 = 20 ÷ 4 = 5</span>
                <br>• Value 6: <span class="math-inline">4 + (4 + 4) ÷ 4 = 4 + 2 = 6</span>
                <br>• Value 7: <span class="math-inline">4 + 4 − (4 ÷ 4) = 8 − 1 = 7</span>
                <br>• Value 8: <span class="math-inline">(4 + 4) × (4 ÷ 4) = 8 × 1 = 8</span> (or <span class="math-inline">4 + 4 + 4 − 4</span>)
                <br>• Value 9: <span class="math-inline">4 + 4 + (4 ÷ 4) = 8 + 1 = 9</span>
                <br>• Value 10: <span class="math-inline">(44 − 4) ÷ 4 = 40 ÷ 4 = 10</span>
              </li>
              <li><strong>Challenge 2: Digits 1, 2, 3, 4, 5 (Targeting 0, 1, 2, 3):</strong>
                <br>• Target 0: <span class="math-inline">(5 − 4 − 1) × (2 + 3) = 0 × 5 = 0</span>
                <br>• Target 1: <span class="math-inline">(5 + 4) − (3 × 2 + 1) = 9 − 7 = 2</span> &rarr; for 1: <span class="math-inline">(5 − 4) + (3 − 2 − 1) = 1 + 0 = 1</span>
                <br>• Target 2: <span class="math-inline">(5 + 1) − (4 + 3 − 2) = 6 − 5 = 1</span>; <span class="math-inline">(5 − 3) + (4 − 2 − 2)</span> &rarr; <span class="math-inline">5 + 4 − 3 − 2 − 2</span> &rarr; <span class="math-inline">(5 + 2) − (4 + 3 − 1) = 7 − 6 = 1</span>; <span class="math-inline">(5 + 3) − (4 + 2 × 1) = 8 − 6 = 2</span>
              </li>
              <li><strong>Challenge 3: Digits 0 to 9 Once Each to Equal 100:</strong>
                <br>Classic Mathematical Solution:
                <div class="math-display">1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 × 9 + 0 = 28 + 72 + 0 = 100</div>
                (Digits used: 1, 2, 3, 4, 5, 6, 7, 8, 9, 0 — all 10 digits used exactly once!)
              </li>
            </ul>
          </div>
          <div class="step-box">
            <span class="step-label"><i class="fa-solid fa-wand-magic-sparkles"></i> Step 4: Verification of 100 Solution</span>
            <span class="math-inline">1 + 2 + 3 + 4 + 5 + 6 + 7 = 28</span>. 
            <span class="math-inline">8 × 9 = 72</span>. 
            <span class="math-inline">28 + 72 + 0 = 100</span>! Perfect beauty.
          </div>
          <div class="step-box">
            <span class="step-label"><i class="fa-solid fa-circle-check"></i> Step 5: Final Conclusion &amp; Key Takeaway</span>
            Expression Engineering demonstrates that mathematical operations and brackets provide infinite creative power to model any number.
          </div>
        </div>
      </details>
    </section>
'''
