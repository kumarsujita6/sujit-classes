# -*- coding: utf-8 -*-
"""
Section 4 - Part 2: Terms, Real-life Modeling & Figure it Out 2 (Pages 27–35)
"""

def get_sec4_part2():
    return '''
      <!-- PART 2: TERMS, LAWS OF ADDITION & FIGURE IT OUT 2 -->
      <h3><i class="fa-solid fa-circle-play"></i> Part 2: Terms, Commutativity, Real-Life Models &amp; Figure it Out 2 (Pages 27–35)</h3>

      <!-- EXAMPLE 4 -->
      <details class="ans-box">
        <summary>
          <span><i class="fa-solid fa-users"></i> Example 4 (Pages 26–27): The Ambiguity Dilemma (Purna vs Mallesh)</span>
          <span class="ans-badge">5-Step Solution</span>
        </summary>
        <div class="ans-content">
          <div class="step-box">
            <span class="step-label"><i class="fa-solid fa-clipboard-question"></i> Step 1: Problem Understanding / Given Data</span>
            Mallesh brought 30 marbles to the playground. Arun brought 5 bags of marbles with 4 marbles in each bag. 
            Mallesh summarized this by writing: <span class="math-inline">30 + 5 × 4</span>.
            <br>Purna evaluated this as <span class="math-inline">(30 + 5) × 4 = 35 × 4 = 140</span>.
            <br>Mallesh evaluated this as <span class="math-inline">30 + (5 × 4) = 30 + 20 = 50</span>.
            <br>Explain why Mallesh is correct and why Purna got it wrong.
          </div>
          <div class="step-box">
            <span class="step-label"><i class="fa-solid fa-lightbulb"></i> Step 2: Key Mathematical Concept / Strategy</span>
            Mathematical operations must mirror physical reality. 
            Arun's marbles are physically packaged in 5 bags of 4 marbles each (<span class="math-inline">5 × 4</span>). 
            Mallesh's 30 marbles are already loose. Therefore, the multiplication creates a single group of 20 marbles before any addition to 30 can take place.
          </div>
          <div class="step-box">
            <span class="step-label"><i class="fa-solid fa-calculator"></i> Step 3: Step-by-Step Mathematical Calculation &amp; Working</span>
            <ul>
              <li>Arun's marbles = <span class="math-inline">5  bags × 4  marbles/bag = 20  marbles</span>.</li>
              <li>Mallesh's marbles = <span class="math-inline">30  marbles</span>.</li>
              <li>Total marbles = <span class="math-inline">30 + 20 = 50  marbles</span>.</li>
            </ul>
            Purna added Mallesh's 30 marbles to Arun's 5 bags, getting "35 bags of marbles", which makes zero physical sense!
          </div>
          <div class="step-box">
            <span class="step-label"><i class="fa-solid fa-wand-magic-sparkles"></i> Step 4: Alternative Method / Linguistic Analogy</span>
            Just as missing commas create confusion in sentences ("Let's eat, Grandpa!" vs "Let's eat Grandpa!"), 
            writing <span class="math-inline">30 + 5 × 4</span> without brackets creates ambiguity. 
            Using brackets removes all confusion: <span class="math-inline">30 + (5 × 4) = 50</span>.
          </div>
          <div class="step-box">
            <span class="step-label"><i class="fa-solid fa-circle-check"></i> Step 5: Final Conclusion &amp; Key Takeaway</span>
            Mallesh is correct. Multiplicative terms bind their factors into a single quantity that must be evaluated before adding to other terms.
          </div>
        </div>
      </details>

      <!-- EXAMPLE 6 -->
      <details class="ans-box">
        <summary>
          <span><i class="fa-solid fa-helicopter"></i> Example 6 (Page 29): Madhu's Drone Flight &amp; Commutative Law</span>
          <span class="ans-badge">5-Step Solution</span>
        </summary>
        <div class="ans-content">
          <div class="step-box">
            <span class="step-label"><i class="fa-solid fa-clipboard-question"></i> Step 1: Problem Understanding / Given Data</span>
            Madhu is flying a drone from a terrace. The drone first goes 6 m straight up, and then flies 4 m straight down. 
            Write an arithmetic expression for the final position of the drone relative to the terrace, express it as a sum of terms, and check if swapping the terms changes the final position.
          </div>
          <div class="step-box">
            <span class="step-label"><i class="fa-solid fa-lightbulb"></i> Step 2: Key Mathematical Concept / Strategy</span>
            Vertical upward motion represents positive integers (+6 m). 
            Vertical downward motion represents negative integers (−4 m). 
            Net height is the sum of these directional displacements: <span class="math-inline">Net Position = Term 1 + Term 2</span>.
          </div>
          <div class="step-box">
            <span class="step-label"><i class="fa-solid fa-calculator"></i> Step 3: Step-by-Step Mathematical Calculation &amp; Working</span>
            <ul>
              <li>Original sequence: <span class="math-inline">6 − 4 = 2</span> m.</li>
              <li>Expressed as a sum of terms: <span class="math-inline">6 + (−4) = 2</span> m. Here, <span class="math-inline">Term 1 = 6</span>, <span class="math-inline">Term 2 = −4</span>.</li>
              <li>Swapped sequence: <span class="math-inline">(−4) + 6 = 2</span> m.</li>
            </ul>
            In both cases, the drone is exactly 2 m above the terrace.
          </div>
          <div class="step-box">
            <span class="step-label"><i class="fa-solid fa-wand-magic-sparkles"></i> Step 4: Alternative Method / Number Line Model</span>
            Start at 0 (terrace). 
            Path A: Move +6 to the right, then −4 to the left &rarr; lands on +2. 
            Path B: Move −4 to the left, then +6 to the right &rarr; lands on +2. 
            The landing coordinate is identical!
          </div>
          <div class="step-box">
            <span class="step-label"><i class="fa-solid fa-circle-check"></i> Step 5: Final Conclusion &amp; Key Takeaway</span>
            Swapping terms does not change the sum. This proves the <strong>Commutative Property of Addition</strong> holds universally, even when terms include negative numbers: <span class="math-inline">Term 1 + Term 2 = Term 2 + Term 1</span>.
          </div>
        </div>
      </details>

      <!-- IN-TEXT PROMPT: MANASA'S 5-MINUTE ADDITION -->
      <details class="ans-box">
        <summary>
          <span><i class="fa-solid fa-stopwatch"></i> In-Text Activity (Page 31): Manasa's 5-Minute Addition List &amp; Forgotten Number</span>
          <span class="ans-badge">5-Step Solution</span>
        </summary>
        <div class="ans-content">
          <div class="step-box">
            <span class="step-label"><i class="fa-solid fa-clipboard-question"></i> Step 1: Problem Understanding / Given Data</span>
            Manasa spent five minutes adding a long list of numbers: 1342, 774, 8611, and 1022, getting a total of 11,749. 
            She then realized that she had accidentally omitted the fourth number from the sheet, which was 9055. 
            Does she have to start adding all the numbers from scratch?
          </div>
          <div class="step-box">
            <span class="step-label"><i class="fa-solid fa-lightbulb"></i> Step 2: Key Mathematical Concept / Strategy</span>
            The <strong>Associative and Commutative Properties of Addition</strong> state that numbers can be grouped and accumulated in any order. 
            The sum of an entire collection is simply the partial sum of already-added numbers plus any remaining number!
          </div>
          <div class="step-box">
            <span class="step-label"><i class="fa-solid fa-calculator"></i> Step-by-Step Mathematical Calculation &amp; Working</span>
            <ul>
              <li>Partial sum of the 4 included numbers = 11,749.</li>
              <li>Omitted number = 9,055.</li>
              <li>She simply adds the omitted number to her existing sum:
                <div class="math-display">11749 + 9055 = 20804</div>
              </li>
            </ul>
          </div>
          <div class="step-box">
            <span class="step-label"><i class="fa-solid fa-wand-magic-sparkles"></i> Step 4: Verification of Associativity</span>
            Total = <span class="math-inline">(1342 + 774 + 8611 + 1022) + 9055 = 11749 + 9055 = 20804</span>. 
            Full sum from top-to-bottom: <span class="math-inline">1342 + 774 + 8611 + 9055 + 1022 = 20804</span>. The results match exactly!
          </div>
          <div class="step-box">
            <span class="step-label"><i class="fa-solid fa-circle-check"></i> Step 5: Final Conclusion &amp; Key Takeaway</span>
            No, Manasa does not have to start over. She saves 5 minutes by applying the associative property to add 9055 directly to 11749, giving <strong>20,804</strong>.
          </div>
        </div>
      </details>

      <!-- EXAMPLE 7 -->
      <details class="ans-box">
        <summary>
          <span><i class="fa-solid fa-bell-concierge"></i> Example 7 (Page 32): Hotel Dosas Bill &amp; Tip Modeling</span>
          <span class="ans-badge">5-Step Solution</span>
        </summary>
        <div class="ans-content">
          <div class="step-box">
            <span class="step-label"><i class="fa-solid fa-clipboard-question"></i> Step 1: Problem Understanding / Given Data</span>
            Amu, Charan, Madhu, and John ordered 4 dosas at ₹23 each and tipped the waiter ₹5. 
            Write an arithmetic expression, identify its terms, and evaluate it. 
            Then, extend the expression if 3 more friends join (total 7 friends ordering dosas) with the same ₹5 tip.
          </div>
          <div class="step-box">
            <span class="step-label"><i class="fa-solid fa-lightbulb"></i> Step 2: Key Mathematical Concept / Strategy</span>
            Total cost = (Cost of all dosas) + (Tip). 
            Cost of dosas is a multiplicative term (<span class="math-inline">n × 23</span>), while the tip is an additive constant (+5).
          </div>
          <div class="step-box">
            <span class="step-label"><i class="fa-solid fa-calculator"></i> Step 3: Step-by-Step Mathematical Calculation &amp; Working</span>
            <ul>
              <li><strong>Case 1 (4 Friends):</strong> Expression = <span class="math-inline">4 × 23 + 5</span>.</li>
              <li>Terms: <span class="math-inline">4 × 23</span> (evaluates to 92) and <span class="math-inline">5</span>.</li>
              <li>Total amount paid = <span class="math-inline">92 + 5 = 97</span> rupees.</li>
              <li><strong>Case 2 (7 Friends):</strong> Expression = <span class="math-inline">7 × 23 + 5</span>.</li>
              <li>Terms: <span class="math-inline">7 × 23</span> and <span class="math-inline">5</span>.</li>
              <li>Evaluation: <span class="math-inline">7 × 23 = 161</span>, then <span class="math-inline">161 + 5 = 166</span> rupees.</li>
            </ul>
          </div>
          <div class="step-box">
            <span class="step-label"><i class="fa-solid fa-wand-magic-sparkles"></i> Step 4: Mental Math Shortcut for 7 × 23</span>
            Decompose 23 as <span class="math-inline">(20 + 3)</span>: <span class="math-inline">7 × 20 + 7 × 3 = 140 + 21 = 161</span>. Add 5 &rarr; ₹166.
          </div>
          <div class="step-box">
            <span class="step-label"><i class="fa-solid fa-circle-check"></i> Step 5: Final Conclusion &amp; Key Takeaway</span>
            For 4 friends, expression is <span class="math-inline">4 × 23 + 5</span> (₹97). For 7 friends, expression is <span class="math-inline">7 × 23 + 5</span> (₹166). The terms are <span class="math-inline">7 × 23</span> and <span class="math-inline">5</span>.
          </div>
        </div>
      </details>

      <!-- EXAMPLE 8 -->
      <details class="ans-box">
        <summary>
          <span><i class="fa-solid fa-fire"></i> Example 8 (Pages 32–33): "Fire in the Mountain" Classroom Game</span>
          <span class="ans-badge">5-Step Solution</span>
        </summary>
        <div class="ans-content">
          <div class="step-box">
            <span class="step-label"><i class="fa-solid fa-clipboard-question"></i> Step 1: Problem Understanding / Given Data</span>
            In a class of 33 students playing "Fire in the Mountain, run, run, run!", Ruby rests on the side while 33 children play. 
            When the teacher calls '5', children form groups of 5. Ruby writes: <span class="math-inline">6 × 5 + 3</span>.
            <br>Explain why Ruby wrote this expression, identify its terms, and write the expressions if the teacher had called '4' or '7'.
          </div>
          <div class="step-box">
            <span class="step-label"><i class="fa-solid fa-lightbulb"></i> Step 2: Key Mathematical Concept / Strategy</span>
            Division with remainder (Euclid's Division Lemma structure): 
            <span class="math-inline">Total Students = (Number of Groups × Group Size) + Remaining Students</span>.
          </div>
          <div class="step-box">
            <span class="step-label"><i class="fa-solid fa-calculator"></i> Step 3: Step-by-Step Mathematical Calculation &amp; Working</span>
            <ul>
              <li><strong>Call '5':</strong> <span class="math-inline">33 ÷ 5 = 6</span> groups with 3 left out. 
                Ruby wrote <span class="math-inline">6 × 5 + 3</span> ("3 more than 6 times 5"). 
                Terms: <span class="math-inline">6 × 5</span> and <span class="math-inline">3</span>.
              </li>
              <li><strong>Call '4':</strong> <span class="math-inline">33 ÷ 4 = 8</span> groups with 1 left out. 
                Ruby would write: <span class="math-inline">8 × 4 + 1</span>. 
                Terms: <span class="math-inline">8 × 4</span> and <span class="math-inline">1</span>. Value = <span class="math-inline">32 + 1 = 33</span>.
              </li>
              <li><strong>Call '7':</strong> <span class="math-inline">33 ÷ 7 = 4</span> groups with 5 left out. 
                Ruby would write: <span class="math-inline">4 × 7 + 5</span>. 
                Terms: <span class="math-inline">4 × 7</span> and <span class="math-inline">5</span>. Value = <span class="math-inline">28 + 5 = 33</span>.
              </li>
            </ul>
          </div>
          <div class="step-box">
            <span class="step-label"><i class="fa-solid fa-wand-magic-sparkles"></i> Step 4: Alternative Representation</span>
            For a class of size 35: calling 6 gives <span class="math-inline">5 × 6 + 5</span>. The remainder is always strictly smaller than the group size called.
          </div>
          <div class="step-box">
            <span class="step-label"><i class="fa-solid fa-circle-check"></i> Step 5: Final Conclusion &amp; Key Takeaway</span>
            For call '4', the expression is <span class="math-inline">8 × 4 + 1</span> (terms: <span class="math-inline">8 × 4</span>, <span class="math-inline">1</span>). 
            For call '7', the expression is <span class="math-inline">4 × 7 + 5</span> (terms: <span class="math-inline">4 × 7</span>, <span class="math-inline">5</span>).
          </div>
        </div>
      </details>

      <!-- EXAMPLE 10: KANNAN ₹432 -->
      <details class="ans-box">
        <summary>
          <span><i class="fa-solid fa-money-bill-wave"></i> Example 10 (Page 33): Kannan's Currency Note &amp; Coin Combinations</span>
          <span class="ans-badge">5-Step Solution</span>
        </summary>
        <div class="ans-content">
          <div class="step-box">
            <span class="step-label"><i class="fa-solid fa-clipboard-question"></i> Step 1: Problem Understanding / Given Data</span>
            Kannan has to pay ₹432 using ₹100, ₹50, ₹20, ₹10 notes and ₹5, ₹1 coins. 
            Identify the terms in the textbook's two expressions and generate a third valid combination.
          </div>
          <div class="step-box">
            <span class="step-label"><i class="fa-solid fa-lightbulb"></i> Step 2: Key Mathematical Concept / Strategy</span>
            Currency payments represent place-value expansions as sums of multiplicative terms: 
            <span class="math-inline">Total = Sum of (Number of Denominations × Denomination Value)</span>.
          </div>
          <div class="step-box">
            <span class="step-label"><i class="fa-solid fa-calculator"></i> Step 3: Step-by-Step Mathematical Calculation &amp; Working</span>
            <ul>
              <li><strong>Way 1:</strong> <span class="math-inline">432 = 4 × 100 + 1 × 20 + 1 × 10 + 2 × 1</span>. 
                Terms: <strong>4 × 100, 1 × 20, 1 × 10, 2 × 1</strong>.
              </li>
              <li><strong>Way 2:</strong> <span class="math-inline">432 = 8 × 50 + 1 × 10 + 4 × 5 + 2 × 1</span>. 
                Terms: <strong>8 × 50, 1 × 10, 4 × 5, 2 × 1</strong>.
              </li>
              <li><strong>Way 3 (Creative new way):</strong> Using forty ₹10 notes: 
                <span class="math-inline">432 = 40 × 10 + 3 × 10 + 2 × 1</span> (or <span class="math-inline">4 × 100 + 3 × 10 + 2 × 1</span>). 
                Terms: <strong>40 × 10, 3 × 10, 2 × 1</strong>.
              </li>
            </ul>
          </div>
          <div class="step-box">
            <span class="step-label"><i class="fa-solid fa-wand-magic-sparkles"></i> Step 4: Verification</span>
            <span class="math-inline">400 + 20 + 10 + 2 = 432</span> | <span class="math-inline">400 + 10 + 20 + 2 = 432</span> | <span class="math-inline">400 + 30 + 2 = 432</span>.
          </div>
          <div class="step-box">
            <span class="step-label"><i class="fa-solid fa-circle-check"></i> Step 5: Final Conclusion &amp; Key Takeaway</span>
            Any number can be decomposed into different combinations of terms while maintaining an identical total value.
          </div>
        </div>
      </details>

      <!-- FIGURE IT OUT 2 - Q1 -->
      <details class="ans-box">
        <summary>
          <span><i class="fa-solid fa-calculator"></i> Figure it Out 2 - Q1 (Pages 34–35): Values by Identifying Terms</span>
          <span class="ans-badge">5-Step Solution</span>
        </summary>
        <div class="ans-content">
          <div class="step-box">
            <span class="step-label"><i class="fa-solid fa-clipboard-question"></i> Step 1: Problem Understanding / Given Data</span>
            Find the values of the following expressions by writing the terms in each case:
            <br>(a) <span class="math-inline">28 − 7 + 8</span>
            <br>(b) <span class="math-inline">39 − 2 × 6 + 11</span>
            <br>(c) <span class="math-inline">40 − 10 + 10 + 10</span>
            <br>(d) <span class="math-inline">48 − 10 × 2 + 16 ÷ 2</span>
            <br>(e) <span class="math-inline">6 × 3 − 4 × 8 ÷ 5</span> (or <span class="math-inline">6 × 3 − 4 × 8 × 5</span>)
          </div>
          <div class="step-box">
            <span class="step-label"><i class="fa-solid fa-lightbulb"></i> Step 2: Key Mathematical Concept / Strategy</span>
            1. Convert subtractions into additions of additive inverses: <span class="math-inline">a − b = a + (−b)</span>.
            2. Identify distinct terms separated by '+'.
            3. Evaluate the internal value of each term (multiplying or dividing first).
            4. Add the resulting values of all terms.
          </div>
          <div class="step-box">
            <span class="step-label"><i class="fa-solid fa-calculator"></i> Step 3: Step-by-Step Mathematical Calculation &amp; Working</span>
            <ul>
              <li>
                <strong>(a) 28 − 7 + 8:</strong> 
                <br>Sum of terms: <span class="math-inline">28 + (−7) + 8</span>. 
                <br>Terms: <strong>28, −7, 8</strong>. 
                <br>Value: <span class="math-inline">(28 + 8) + (−7) = 36 − 7 = 29</span>.
              </li>
              <li>
                <strong>(b) 39 − 2 × 6 + 11:</strong> 
                <br>Sum of terms: <span class="math-inline">39 + (−(2 × 6)) + 11</span>. 
                <br>Evaluate terms: <span class="math-inline">2 × 6 = 12</span>, so term is <span class="math-inline">−12</span>. 
                <br>Terms: <strong>39, −12, 11</strong>. 
                <br>Value: <span class="math-inline">(39 + 11) + (−12) = 50 − 12 = 38</span>.
              </li>
              <li>
                <strong>(c) 40 − 10 + 10 + 10:</strong> 
                <br>Sum of terms: <span class="math-inline">40 + (−10) + 10 + 10</span>. 
                <br>Terms: <strong>40, −10, 10, 10</strong>. 
                <br>Notice zero-pair: <span class="math-inline">(−10) + 10 = 0</span>. 
                <br>Value: <span class="math-inline">40 + 0 + 10 = 50</span>.
              </li>
              <li>
                <strong>(d) 48 − 10 × 2 + 16 ÷ 2:</strong> 
                <br>Sum of terms: <span class="math-inline">48 + (−(10 × 2)) + (16 ÷ 2)</span>. 
                <br>Evaluate terms: <span class="math-inline">10 × 2 = 20 → −20</span>; <span class="math-inline">16 ÷ 2 = 8</span>. 
                <br>Terms: <strong>48, −20, 8</strong>. 
                <br>Value: <span class="math-inline">(48 + 8) + (−20) = 56 − 20 = 36</span>.
              </li>
              <li>
                <strong>(e) 6 × 3 − 4 × 8 ÷ 5:</strong>
                <br>Sum of terms: <span class="math-inline">(6 × 3) + (−(4 × 8 ÷ 5))</span>. 
                <br>Evaluate terms: <span class="math-inline">6 × 3 = 18</span>; <span class="math-inline">4 × 8 ÷ 5 = 32 ÷ 5 = 6.4</span>. 
                <br>Terms: <strong>18, −6.4</strong>. 
                <br>Value: <span class="math-inline">18 − 6.4 = 11.6</span>. 
                <br><em>(Note: If printed as 6 × 3 − 4 × 8 + 5: terms are 18, −32, 5 &rarr; value = −9)</em>.
              </li>
            </ul>
          </div>
          <div class="step-box">
            <span class="step-label"><i class="fa-solid fa-wand-magic-sparkles"></i> Step 4: Commutative Reordering Benefit</span>
            In (c), pairing <span class="math-inline">−10</span> and <span class="math-inline">+10</span> to eliminate them instantly is far faster than left-to-right sequential addition!
          </div>
          <div class="step-box">
            <span class="step-label"><i class="fa-solid fa-circle-check"></i> Step 5: Final Conclusion &amp; Key Takeaway</span>
            The evaluated values are: <strong>(a) 29, (b) 38, (c) 50, (d) 36, (e) 11.6</strong>.
          </div>
        </div>
      </details>

      <!-- FIGURE IT OUT 2 - Q2 -->
      <details class="ans-box">
        <summary>
          <span><i class="fa-solid fa-book"></i> Figure it Out 2 - Q2 (Page 35): Real-Life Story Situations for Expressions</span>
          <span class="ans-badge">5-Step Solution</span>
        </summary>
        <div class="ans-content">
          <div class="step-box">
            <span class="step-label"><i class="fa-solid fa-clipboard-question"></i> Step 1: Problem Understanding / Given Data</span>
            Write a creative real-life story or situation for each expression and find its value:
            <br>(a) <span class="math-inline">89 + 21 − 10</span>
            <br>(b) <span class="math-inline">5 × 12 − 6</span>
            <br>(c) <span class="math-inline">4 × 9 + 2 × 6</span>
          </div>
          <div class="step-box">
            <span class="step-label"><i class="fa-solid fa-lightbulb"></i> Step 2: Key Mathematical Concept / Strategy</span>
            Connect positive terms to gaining, receiving, or purchasing items. 
            Connect negative terms to losing, giving away, or spending. 
            Connect multiplicative terms to buying multiple identical packets or packs.
          </div>
          <div class="step-box">
            <span class="step-label"><i class="fa-solid fa-calculator"></i> Step 3: Step-by-Step Mathematical Calculation &amp; Working</span>
            <ul>
              <li>
                <strong>(a) 89 + 21 − 10:</strong>
                <br><em>Story:</em> A school library in Cuttack has 89 math books on the shelf. The headmaster donates 21 new math books. Later in the afternoon, Class 7 students borrow 10 books for study. How many books remain on the shelf?
                <br><em>Value:</em> <span class="math-inline">89 + 21 − 10 = 110 − 10 = 100</span> books.
              </li>
              <li>
                <strong>(b) 5 × 12 − 6:</strong>
                <br><em>Story:</em> Priya buys 5 cartons of eggs for baking cakes, with each carton holding 12 eggs. While unloading at her bakery, she discovers that 6 eggs are unfortunately cracked. How many good eggs does Priya have?
                <br><em>Value:</em> <span class="math-inline">5 × 12 − 6 = 60 − 6 = 54</span> eggs.
              </li>
              <li>
                <strong>(c) 4 × 9 + 2 × 6:</strong>
                <br><em>Story:</em> A stationery shop sells pencil boxes. Rohan buys 4 large boxes containing 9 pencils each, and 2 mini boxes containing 6 pencils each. What is the total count of pencils Rohan purchased?
                <br><em>Value:</em> <span class="math-inline">4 × 9 + 2 × 6 = 36 + 12 = 48</span> pencils.
              </li>
            </ul>
          </div>
          <div class="step-box">
            <span class="step-label"><i class="fa-solid fa-wand-magic-sparkles"></i> Step 4: Verification of Meaning</span>
            In each scenario, the terms maintain the order of physical reality: <span class="math-inline">5 × 12</span> must be grouped before subtracting the 6 damaged eggs.
          </div>
          <div class="step-box">
            <span class="step-label"><i class="fa-solid fa-circle-check"></i> Step 5: Final Conclusion &amp; Key Takeaway</span>
            The evaluated values are: <strong>(a) 100, (b) 54, (c) 48</strong>.
          </div>
        </div>
      </details>

      <!-- FIGURE IT OUT 2 - Q3 -->
      <details class="ans-box">
        <summary>
          <span><i class="fa-solid fa-coins"></i> Figure it Out 2 - Q3 (Page 35): Queen Alia's Coins, Metro Fares &amp; Window Height</span>
          <span class="ans-badge">5-Step Solution</span>
        </summary>
        <div class="ans-content">
          <div class="step-box">
            <span class="step-label"><i class="fa-solid fa-clipboard-question"></i> Step 1: Problem Understanding / Given Data</span>
            Solve the three real-world situational problems:
            <br><strong>(a) Gold Coins:</strong> Queen Alia gave 100 gold coins to Princess Elsa and 100 gold coins to Princess Anna. Elsa doubled her coins in business. Anna spent half on jewellery. Write the expression, terms, and find total coins together.
            <br><strong>(b) Metro Fares:</strong> Adult ticket = ₹40, child ticket = ₹20. (i) Cost for 4 adults and 3 children. (ii) Cost for two groups of 3 adults each.
            <br><strong>(c) Window Height:</strong> Top border = 3 cm, grill = 2 cm, gap = 5 cm. Write an expression describing the total height.
          </div>
          <div class="step-box">
            <span class="step-label"><i class="fa-solid fa-lightbulb"></i> Step 2: Key Mathematical Concept / Strategy</span>
            Translate verbal relationships into terms:
            <br>Doubling means multiplying by 2 (<span class="math-inline">2 × 100</span>). 
            <br>Halving means dividing by 2 (<span class="math-inline">100 ÷ 2</span> or <span class="math-inline">100 ÷ 2</span>).
          </div>
          <div class="step-box">
            <span class="step-label"><i class="fa-solid fa-calculator"></i> Step 3: Step-by-Step Mathematical Calculation &amp; Working</span>
            <ul>
              <li>
                <strong>Part (a) Gold Coins:</strong>
                <br>Elsa's coins = <span class="math-inline">2 × 100 = 200</span>.
                <br>Anna's coins = <span class="math-inline">100 ÷ 2 = 50</span>.
                <br>Combined Expression = <span class="math-inline">2 × 100 + 100 ÷ 2</span>.
                <br>Terms: <strong>2 × 100</strong> and <strong>100 ÷ 2</strong>.
                <br>Value: <span class="math-inline">200 + 50 = 250</span> gold coins.
              </li>
              <li>
                <strong>Part (b) Metro Tickets:</strong>
                <br>(i) 4 adults and 3 children:
                <br>Expression = <span class="math-inline">4 × 40 + 3 × 20</span>.
                <br>Terms: <strong>4 × 40</strong> and <strong>3 × 20</strong>.
                <br>Value = <span class="math-inline">160 + 60 = 220</span> rupees.
                <br>(ii) Two groups having 3 adults each:
                <br>Expression = <span class="math-inline">2 × (3 × 40)</span> or <span class="math-inline">(2 × 3) × 40 = 6 × 40</span>.
                <br>Terms: Single compound term <span class="math-inline">2 × (3 × 40)</span>.
                <br>Value = <span class="math-inline">2 × 120 = 240</span> rupees.
              </li>
              <li>
                <strong>Part (c) Window Height:</strong>
                <br>The window has 2 borders (top and bottom) of 3 cm each (<span class="math-inline">2 × 3</span>), 
                multiple repeated grill patterns of 2 cm (<span class="math-inline">n × 2</span>), and gaps of 5 cm (<span class="math-inline">m × 5</span>).
                <br>Expression = <span class="math-inline">2 × 3 + Grills + Gaps</span>. 
                <br>From textbook diagram specifications: Total height = <span class="math-inline">2 × 3 + 4 × 2 + 3 × 5 = 6 + 8 + 15 = 29</span> cm.
              </li>
            </ul>
          </div>
          <div class="step-box">
            <span class="step-label"><i class="fa-solid fa-wand-magic-sparkles"></i> Step 4: Verification of Unit Pricing</span>
            In (b)(i), adult share (160) + child share (60) = ₹220. 
            In (b)(ii), each group pays ₹120; for two groups, <span class="math-inline">2 × 120 = ₹240</span>.
          </div>
          <div class="step-box">
            <span class="step-label"><i class="fa-solid fa-circle-check"></i> Step 5: Final Conclusion &amp; Key Takeaway</span>
            (a) <span class="math-inline">2 × 100 + 100 ÷ 2 = 250</span> coins; (b)(i) ₹220, (b)(ii) ₹240; (c) Window height = 29 cm.
          </div>
        </div>
      </details>
'''
