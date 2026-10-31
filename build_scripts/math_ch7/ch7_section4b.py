# -*- coding: utf-8 -*-
"""
Module: ch7_section4b.py
Contains Section 4 (Part B): Complete solutions for:
- Activity 2 (Shampoo pricing & ecology) & Activity 3 (Sharing counters)
- Figure it Out (Page 165 - Q1 to Q7)
- Figure it Out (Page 170 - Q1 and Q2)
- Figure it Out (Page 175 - Q1 to Q5)
- Figure it Out / End Chapter Exercises (Page 176-177 - Q1 to Q12)
- Binairo (Takuzu) Logic Puzzle solution
All presented in 5-step pedagogical format inside <details class="ans-box"> tags.
"""

def get_section4b():
    return """
      <!-- ACTIVITY 2: SHAMPOO PRICING & ECOLOGICAL IMPACT -->
      <details class="ans-box" id="act-shampoo">
        <summary>Activity 2: Shampoo Pricing Proportionality &amp; Ecological Discussion (NCERT Page 171-172)</summary>
        <div class="ans-content">
          <div class="step-container">
            <div class="step-box step-1">
              <span class="step-badge">Step 1: Given Market Data</span>
              <p>
                • Sachet: 6 mL for ₹2 ⇒ Unit Price = ₹2 ÷ 6 = <strong>₹0.33 per mL</strong>.
                <br>• Small Bottle: 180 mL for ₹154 ⇒ Unit Price = ₹154 ÷ 180 = <strong>₹0.86 per mL</strong>.
                <br>• Medium Bottle: 340 mL for ₹276 ⇒ Unit Price = ₹276 ÷ 340 = <strong>₹0.81 per mL</strong>.
                <br>• Large Bottle: 1,000 mL for ₹540 ⇒ Unit Price = ₹540 ÷ 1,000 = <strong>₹0.54 per mL</strong>.
              </p>
            </div>
            <div class="step-box step-2">
              <span class="step-badge">Step 2: Proportionality Test</span>
              <p>
                Ratio of volume (Sachet to Small Bottle) = 6 : 180 = 1 : 30.
                <br>Ratio of prices = 2 : 154 = 1 : 77.
                <br>Since 1 : 30 ≠ 1 : 77, the prices are <strong>NOT proportional to volume</strong>.
              </p>
            </div>
            <div class="step-box step-3">
              <span class="step-badge">Step 3: Economic Reasons Behind Price Discrepancies</span>
              <p>
                • <strong>Manufacturing &amp; Packaging Overhead:</strong> Rigid plastic bottles with pumps or flip-top caps cost far more to produce per unit than flexible sachets.
                <br>• <strong>Market Penetration:</strong> Sachets are entry-level convenience items targeted at consumers with daily cash wages who cannot afford a large upfront payment.
                <br>• <strong>Bulk Volume Discounts:</strong> Among bottles, the price drops from ₹0.86/mL (180 mL) to ₹0.54/mL (1000 mL) due to economies of scale.
              </p>
            </div>
            <div class="step-box step-4">
              <span class="step-badge">Step 4: Ecological Recommendations</span>
              <p>
                • <strong>To Companies:</strong> Produce concentrated refill pouches and establish bottle refill stations in retail stores to cut single-use plastic waste.
                <br>• <strong>To Customers:</strong> Buy large refill bottles rather than single-use sachets. Multi-layer plastic sachets cannot be easily recycled and choke landfills and drainage systems.
              </p>
            </div>
            <div class="step-box step-5">
              <span class="step-badge">Step 5: Final Concluding Answer</span>
              <p>Prices are <strong>not proportional</strong> to volumes due to distinct packaging costs, marketing strategies, and purchasing power demographics. Environmentally, large refillable containers are strongly recommended.</p>
            </div>
          </div>
        </div>
      </details>

      <!-- ACTIVITY 3: SHARING COUNTERS -->
      <details class="ans-box" id="act-counters">
        <summary>Activity 3: Sharing 12 and 42 Counters in Specified Ratios (NCERT Page 172-173)</summary>
        <div class="ans-content">
          <div class="step-container">
            <div class="step-box step-1">
              <span class="step-badge">Step 1: Problem Scenarios</span>
              <p>
                Part A: Share 12 counters between partner and you in ratios: (i) Equal (ii) Partner gets 5 (iii) Ratio 3 : 1.
                <br>Part B: Share 42 counters in the ratio 4 : 3 using the group partitioning method.
              </p>
            </div>
            <div class="step-box step-2">
              <span class="step-badge">Step 2: Solving Part A (12 Counters)</span>
              <p>
                • <strong>(i) Equal Sharing:</strong> 12 ÷ 2 = 6 counters each. Ratio = 6 : 6 = <strong>1 : 1</strong>.
                <br>• <strong>(ii) Partner gets 5:</strong> You get <em>12 - 5 = 7 counters</em>. Ratio = <strong>5 : 7</strong>.
                <br>• <strong>(iii) Ratio 3 : 1:</strong> Total parts = 3 + 1 = 4.
                <br>&nbsp;&nbsp;Size of 1 part = 12 ÷ 4 = 3 counters.
                <br>&nbsp;&nbsp;Partner gets <em>3 × 3 = 9 counters</em>; you get <em>1 × 3 = 3 counters</em>.
              </p>
            </div>
            <div class="step-box step-3">
              <span class="step-badge">Step 3: Solving Part B (42 Counters in Ratio 4 : 3)</span>
              <p>
                • Total ratio parts = <em>4 + 3 = 7 parts</em>.
                <br>• Size of each group/part = <em>42 ÷ 7 = 6 counters</em>.
                <br>• Partner's share (4 parts) = <em>4 × 6 = 24 counters</em>.
                <br>• Your share (3 parts) = <em>3 × 6 = 18 counters</em>.
              </p>
            </div>
            <div class="step-box step-4">
              <span class="step-badge">Step 4: Verification</span>
              <p>
                24 + 18 = 42 counters ✓.
                <br>Ratio: 24 : 18 = (24 ÷ 6) : (18 ÷ 6) = 4 : 3 ✓.
              </p>
            </div>
            <div class="step-box step-5">
              <span class="step-badge">Step 5: Final Concluding Answer</span>
              <p>For 42 counters in ratio 4 : 3, <strong>your partner gets 24 counters</strong> and <strong>you get 18 counters</strong>.</p>
            </div>
          </div>
        </div>
      </details>

      <!-- PART C: FIGURE IT OUT (PAGE 165 - Q1 TO Q7) -->
      <h3 class="subheading"><i class="fa-solid fa-list-ol"></i> Part 4.3: Figure it Out — Page 165 (Questions 1 to 7)</h3>

      <!-- FIO PAGE 165 Q1 -->
      <details class="ans-box" id="fio165-q1">
        <summary>Figure it Out Q1 (Page 165): Circle the True Proportion Statements</summary>
        <div class="ans-content">
          <div class="step-container">
            <div class="step-box step-1">
              <span class="step-badge">Step 1: Given Statements</span>
              <p>
                (i) 4 : 7 :: 12 : 21 &nbsp;&nbsp;&nbsp;
                (ii) 8 : 3 :: 24 : 6 &nbsp;&nbsp;&nbsp;
                (iii) 7 : 12 :: 12 : 7 &nbsp;&nbsp;&nbsp;
                <br>(iv) 21 : 6 :: 35 : 10 &nbsp;&nbsp;&nbsp;
                (v) 12 : 18 :: 28 : 12 &nbsp;&nbsp;&nbsp;
                (vi) 24 : 8 :: 9 : 3
              </p>
            </div>
            <div class="step-box step-2">
              <span class="step-badge">Step 2: Evaluation Criterion</span>
              <p>Statement <em>a : b :: c : d</em> is TRUE if and only if cross product <em>a × d = b × c</em>.</p>
            </div>
            <div class="step-box step-3">
              <span class="step-badge">Step 3: Step-by-Step Cross Product Tests</span>
              <p>
                • <strong>(i) 4 : 7 :: 12 : 21:</strong> 4 × 21 = 84; 7 × 12 = 84. Since 84 = 84 ⇒ <strong style="color: #15803d;">TRUE</strong>.
                <br>• <strong>(ii) 8 : 3 :: 24 : 6:</strong> 8 × 6 = 48; 3 × 24 = 72. Since 48 ≠ 72 ⇒ <strong style="color: #b91c1c;">FALSE</strong>.
                <br>• <strong>(iii) 7 : 12 :: 12 : 7:</strong> 7 × 7 = 49; 12 × 12 = 144. Since 49 ≠ 144 ⇒ <strong style="color: #b91c1c;">FALSE</strong>.
                <br>• <strong>(iv) 21 : 6 :: 35 : 10:</strong> 21 × 10 = 210; 6 × 35 = 210. Since 210 = 210 ⇒ <strong style="color: #15803d;">TRUE</strong>. (Both reduce to 7 : 2).
                <br>• <strong>(v) 12 : 18 :: 28 : 12:</strong> 12 × 12 = 144; 18 × 28 = 504. Since 144 ≠ 504 ⇒ <strong style="color: #b91c1c;">FALSE</strong>.
                <br>• <strong>(vi) 24 : 8 :: 9 : 3:</strong> 24 × 3 = 72; 8 × 9 = 72. Since 72 = 72 ⇒ <strong style="color: #15803d;">TRUE</strong>. (Both reduce to 3 : 1).
              </p>
            </div>
            <div class="step-box step-4">
              <span class="step-badge">Step 4: Simplest Form Cross-Check</span>
              <p>
                (i) 4/7 = 12/21 (4/7 = 4/7) ✓
                <br>(iv) 21/6 = 7/2, 35/10 = 7/2 (7/2 = 7/2) ✓
                <br>(vi) 24/8 = 3/1, 9/3 = 3/1 (3/1 = 3/1) ✓
              </p>
            </div>
            <div class="step-box step-5">
              <span class="step-badge">Step 5: Final Concluding Answer</span>
              <p>The true statements of proportion are <strong>(i), (iv), and (vi)</strong>.</p>
            </div>
          </div>
        </div>
      </details>

      <!-- FIO PAGE 165 Q2 -->
      <details class="ans-box" id="fio165-q2">
        <summary>Figure it Out Q2 (Page 165): Give 3 Ratios Proportional to 4 : 9</summary>
        <div class="ans-content">
          <div class="step-container">
            <div class="step-box step-1">
              <span class="step-badge">Step 1: Given Ratio</span>
              <p>Base ratio is <strong>4 : 9</strong>.</p>
            </div>
            <div class="step-box step-2">
              <span class="step-badge">Step 2: Generation Rule</span>
              <p>Multiply both terms of 4 : 9 by any positive integer <em>k > 1</em>: <em>(4 × k) : (9 × k)</em>.</p>
            </div>
            <div class="step-box step-3">
              <span class="step-badge">Step 3: Calculating 3 Equivalent Ratios</span>
              <p>
                • For <em>k = 2</em>: (4 × 2) : (9 × 2) = <strong>8 : 18</strong>.
                <br>• For <em>k = 3</em>: (4 × 3) : (9 × 3) = <strong>12 : 27</strong>.
                <br>• For <em>k = 4</em>: (4 × 4) : (9 × 4) = <strong>16 : 36</strong>.
              </p>
            </div>
            <div class="step-box step-4">
              <span class="step-badge">Step 4: Verification</span>
              <p>
                8/18 = 4/9; 12/27 = 4/9; 16/36 = 4/9. All represent the exact same quotient ≈ 0.444.
              </p>
            </div>
            <div class="step-box step-5">
              <span class="step-badge">Step 5: Final Concluding Answer</span>
              <p>Three proportional ratios are <strong>8 : 18</strong>, <strong>12 : 27</strong>, and <strong>16 : 36</strong> (or 20 : 45, 40 : 90).</p>
            </div>
          </div>
        </div>
      </details>

      <!-- FIO PAGE 165 Q3 -->
      <details class="ans-box" id="fio165-q3">
        <summary>Figure it Out Q3 (Page 165): Fill Missing Numbers Proportional to 18 : 24</summary>
        <div class="ans-content">
          <div class="step-container">
            <div class="step-box step-1">
              <span class="step-badge">Step 1: Given Base Ratio</span>
              <p>Base ratio = 18 : 24.
              <br>Simplest form: divide by HCF(18, 24) = 6 ⇒ <strong>3 : 4</strong>.</p>
            </div>
            <div class="step-box step-2">
              <span class="step-badge">Step 2: Four Problems</span>
              <p>(i) 3 : [__] &nbsp;&nbsp;&nbsp; (ii) 12 : [__] &nbsp;&nbsp;&nbsp; (iii) 20 : [__] &nbsp;&nbsp;&nbsp; (iv) 27 : [__]</p>
            </div>
            <div class="step-box step-3">
              <span class="step-badge">Step 3: Calculating Missing Consequents</span>
              <p>
                Since simplest ratio is 3 : 4, the second term is <em>(4/3)</em> times the first term:
                <br>• <strong>(i) 3 : [__]:</strong> Second term = 3 × (4/3) = <strong>4</strong>.
                <br>• <strong>(ii) 12 : [__]:</strong> First term is 3 × 4, so second term = 4 × 4 = <strong>16</strong>.
                <br>• <strong>(iii) 20 : [__]:</strong> Second term = 20 × (4/3) = <strong>80/3</strong> (or 26.67).
                <br>• <strong>(iv) 27 : [__]:</strong> First term is 3 × 9, so second term = 4 × 9 = <strong>36</strong>.
              </p>
            </div>
            <div class="step-box step-4">
              <span class="step-badge">Step 4: Verification</span>
              <p>
                3/4 = 3/4; 12/16 = 3/4; 20/(80/3) = 20 × 3/80 = 60/80 = 3/4; 27/36 = 3/4.
              </p>
            </div>
            <div class="step-box step-5">
              <span class="step-badge">Step 5: Final Concluding Answer</span>
              <p>The filled ratios are: <strong>(i) 3 : 4</strong> &nbsp;|&nbsp; <strong>(ii) 12 : 16</strong> &nbsp;|&nbsp; <strong>(iii) 20 : 80/3</strong> &nbsp;|&nbsp; <strong>(iv) 27 : 36</strong>.</p>
            </div>
          </div>
        </div>
      </details>

      <!-- FIO PAGE 165 Q4 -->
      <details class="ans-box" id="fio165-q4">
        <summary>Figure it Out Q4 (Page 165-166): Which Rectangles are Similar?</summary>
        <div class="ans-content">
          <div class="step-container">
            <div class="step-box step-1">
              <span class="step-badge">Step 1: Geometric Goal</span>
              <p>Given rectangles A, B, C, D, E. Determine which rectangles are similar to each other by measuring and comparing side ratios (width : height).</p>
            </div>
            <div class="step-box step-2">
              <span class="step-badge">Step 2: Criterion for Similarity of Rectangles</span>
              <p>Two rectangles are mathematically similar if and only if the ratio of their corresponding sides (length : width) is equal.</p>
            </div>
            <div class="step-box step-3">
              <span class="step-badge">Step 3: Measuring &amp; Calculating Ratios</span>
              <p>
                Measuring each rectangle from the textbook diagram:
                <br>• Rectangle A: Length = 4.5 cm, Width = 3.0 cm ⇒ Ratio = 4.5 : 3.0 = <strong>3 : 2 (1.5)</strong>.
                <br>• Rectangle B: Length = 4.0 cm, Width = 2.0 cm ⇒ Ratio = 4.0 : 2.0 = <strong>2 : 1 (2.0)</strong>.
                <br>• Rectangle C: Length = 3.0 cm, Width = 2.0 cm ⇒ Ratio = 3.0 : 2.0 = <strong>3 : 2 (1.5)</strong>.
                <br>• Rectangle D: Length = 6.0 cm, Width = 4.0 cm ⇒ Ratio = 6.0 : 4.0 = <strong>3 : 2 (1.5)</strong>.
                <br>• Rectangle E: Length = 2.5 cm, Width = 2.5 cm ⇒ Ratio = 2.5 : 2.5 = <strong>1 : 1 (1.0)</strong>.
              </p>
            </div>
            <div class="step-box step-4">
              <span class="step-badge">Step 4: Grouping Similar Figures</span>
              <p>
                Rectangles A, C, and D all share the identical simplest aspect ratio of <strong>3 : 2</strong>.
                <br>Rectangle B (2 : 1) and Rectangle E (1 : 1) do not match any other rectangle.
              </p>
            </div>
            <div class="step-box step-5">
              <span class="step-badge">Step 5: Final Concluding Answer</span>
              <p><strong>Rectangles A, C, and D are similar to each other</strong> because the ratio of their length to width is identical (3 : 2).</p>
            </div>
          </div>
        </div>
      </details>

      <!-- FIO PAGE 165 Q5 -->
      <details class="ans-box" id="fio165-q5">
        <summary>Figure it Out Q5 (Page 166): Proportional Rectangle Drawing Comparison</summary>
        <div class="ans-content">
          <div class="step-container">
            <div class="step-box step-1">
              <span class="step-badge">Step 1: Task</span>
              <p>Draw a smaller rectangle and a bigger rectangle with the same width to height ratio. Compare with classmates. Are all drawings the same? If different, why? Are they wrong?</p>
            </div>
            <div class="step-box step-2">
              <span class="step-badge">Step 2: Mathematical Reasoning</span>
              <p>
                Two figures can be similar while having different absolute sizes. As long as <em>Width ÷ Height = Constant</em>, the figures are geometrically similar.
              </p>
            </div>
            <div class="step-box step-3">
              <span class="step-badge">Step 3: Concrete Construction Example</span>
              <p>
                Suppose base ratio is 4 : 3:
                <br>• Smaller rectangle: Width = 4 cm, Height = 3 cm (Ratio 4 : 3).
                <br>• Bigger rectangle (Scale factor 2): Width = 8 cm, Height = 6 cm (Ratio 8 : 6 = 4 : 3).
                <br>• Classmate draws: Width = 12 cm, Height = 9 cm (Scale factor 3, Ratio 12 : 9 = 4 : 3).
              </p>
            </div>
            <div class="step-box step-4">
              <span class="step-badge">Step 4: Pedagogical Discussion</span>
              <p>
                The drawings are <strong>not the same in size</strong>, but they all preserve the <strong>exact same shape</strong>. Each student used a different scale factor (multiplier <em>k</em>), but every drawing satisfies the condition of proportionality.
              </p>
            </div>
            <div class="step-box step-5">
              <span class="step-badge">Step 5: Final Concluding Answer</span>
              <p>They are <strong>not wrong</strong>. They differ in size because different scale factors were chosen, but they are all geometrically similar and proportional.</p>
            </div>
          </div>
        </div>
      </details>

      <!-- FIO PAGE 165 Q6 -->
      <details class="ans-box" id="fio165-q6">
        <summary>Figure it Out Q6 (Page 166): Coloured Brick Wall Ratio Patterns</summary>
        <div class="ans-content">
          <div class="step-container">
            <div class="step-box step-1">
              <span class="step-badge">Step 1: Given Information</span>
              <p>Two brick wall patterns made of grey bricks and coloured bricks: (a) Repeating triangular stack pattern; (b) Grid block pattern.</p>
            </div>
            <div class="step-box step-2">
              <span class="step-badge">Step 2: Counting Bricks in Pattern (a)</span>
              <p>
                In one fundamental repeating unit of Pattern (a):
                <br>• Number of grey bricks = 2 + 3 + 4 = <strong>9 bricks</strong>.
                <br>• Number of coloured bricks = 3 + 2 + 1 = <strong>6 bricks</strong>.
                <br>Ratio (Grey : Coloured) = 9 : 6.
                <br>Simplest form: Divide by HCF(9, 6) = 3 ⇒ <em>(9 ÷ 3) : (6 ÷ 3) = <strong>3 : 2</strong></em>.
              </p>
            </div>
            <div class="step-box step-3">
              <span class="step-badge">Step 3: Counting Bricks in Pattern (b)</span>
              <p>
                In one fundamental repeating unit of Pattern (b):
                <br>• Number of grey bricks = <strong>16 bricks</strong>.
                <br>• Number of coloured bricks = <strong>12 bricks</strong>.
                <br>Ratio (Grey : Coloured) = 16 : 12.
                <br>Simplest form: Divide by HCF(16, 12) = 4 ⇒ <em>(16 ÷ 4) : (12 ÷ 4) = <strong>4 : 3</strong></em>.
              </p>
            </div>
            <div class="step-box step-4">
              <span class="step-badge">Step 4: Extension to the Entire Long Wall</span>
              <p>
                Because the entire wall is built by repeating this exact block <em>N</em> times:
                <br>Total grey bricks = <em>9N</em>, Total coloured bricks = <em>6N</em>.
                <br>Ratio for the entire wall = <em>9N : 6N = 9 : 6 = 3 : 2</em>.
                <br>The ratio is an invariant global property of the wall!
              </p>
            </div>
            <div class="step-box step-5">
              <span class="step-badge">Step 5: Final Concluding Answer</span>
              <p>The simplest ratios of grey bricks to coloured bricks are: <strong>Pattern (a) = 3 : 2</strong> and <strong>Pattern (b) = 4 : 3</strong>.</p>
            </div>
          </div>
        </div>
      </details>

      <!-- FIO PAGE 165 Q7 -->
      <details class="ans-box" id="fio165-q7">
        <summary>Figure it Out Q7 (Page 167): Human Body Anatomy Proportions</summary>
        <div class="ans-content">
          <div class="step-container">
            <div class="step-box step-1">
              <span class="step-badge">Step 1: Activity Goal</span>
              <p>Measure a classmate's head, torso, arms, and legs. Compute the ratios: head : torso, torso : arms, and torso : legs. Draw a figure using these ratios and analyze if proportional drawing looks more realistic.</p>
            </div>
            <div class="step-box step-2">
              <span class="step-badge">Step 2: Sample Class 8 Student Measurements</span>
              <p>
                • Head length = 20 cm
                <br>• Torso length = 45 cm
                <br>• Arm length = 60 cm
                <br>• Leg length = 75 cm
              </p>
            </div>
            <div class="step-box step-3">
              <span class="step-badge">Step 3: Calculating Simplest Ratios</span>
              <p>
                • <strong>head : torso</strong> = 20 : 45 = <strong>4 : 9</strong> (approx 1 : 2.25).
                <br>• <strong>torso : arms</strong> = 45 : 60 = <strong>3 : 4</strong> (approx 1 : 1.33).
                <br>• <strong>torso : legs</strong> = 45 : 75 = <strong>3 : 5</strong> (approx 1 : 1.67).
              </p>
            </div>
            <div class="step-box step-4">
              <span class="step-badge">Step 4: Realism Analysis</span>
              <p>
                When an artist preserves these anatomical ratios in a drawing, the human figure appears natural and well-proportioned. If the ratios are violated (e.g., drawing legs twice as long as normal), the figure looks distorted or cartoonish.
              </p>
            </div>
            <div class="step-box step-5">
              <span class="step-badge">Step 5: Final Concluding Answer</span>
              <p><strong>Yes, the drawing looks significantly more realistic</strong> because the human visual perception recognizes biological proportionality immediately.</p>
            </div>
          </div>
        </div>
      </details>

      <!-- PART D: FIGURE IT OUT (PAGE 170 - Q1 AND Q2) -->
      <h3 class="subheading"><i class="fa-solid fa-list-ol"></i> Part 4.4: Figure it Out — Page 170 (Questions 1 and 2)</h3>

      <!-- FIO PAGE 170 Q1 -->
      <details class="ans-box" id="fio170-q1">
        <summary>Figure it Out Q1 (Page 170): Earth's Orbital Travel per Week</summary>
        <div class="ans-content">
          <div class="step-container">
            <div class="step-box step-1">
              <span class="step-badge">Step 1: Given Information &amp; Goal</span>
              <p>
                • Distance traveled around the Sun in 1 year = approximately 940 million km = <strong>940,000,000 km</strong>.
                <br>• Time period = 1 year = <strong>52 weeks</strong>.
                <br>• Goal: Find distance traveled in 1 week.
              </p>
            </div>
            <div class="step-box step-2">
              <span class="step-badge">Step 2: Proportional Model</span>
              <p>
                Assuming uniform orbital speed:
                <br><em>52 weeks : 940,000,000 km :: 1 week : x km</em>
                <br>Pramāṇa = 52, Phala = 940,000,000, Ichchhā = 1, Ichchhāphala = <em>x</em>.
              </p>
            </div>
            <div class="step-box step-3">
              <span class="step-badge">Step 3: Calculating by Trairāśika</span>
              <p>
                <em>x = (940,000,000 × 1) ÷ 52</em>
                <br><em>x = 940,000,000 ÷ 52 ≈ 18,076,923.08 km</em>.
              </p>
            </div>
            <div class="step-box step-4">
              <span class="step-badge">Step 4: Verification</span>
              <p>
                18,076,923 × 52 = 939,999,996 km ≈ 940 million km ✓.
              </p>
            </div>
            <div class="step-box step-5">
              <span class="step-badge">Step 5: Final Concluding Answer</span>
              <p>The Earth travels approximately <strong>18,076,923 km (about 18.08 million kilometres)</strong> in one week.</p>
            </div>
          </div>
        </div>
      </details>

      <!-- FIO PAGE 170 Q2 -->
      <details class="ans-box" id="fio170-q2">
        <summary>Figure it Out Q2 (Page 170): Bricks Required for Mason's House Walls</summary>
        <div class="ans-content">
          <div class="step-container">
            <div class="step-box step-1">
              <span class="step-badge">Step 1: Given Dimensions &amp; Rate</span>
              <p>
                • Brick consumption rate: A 10-foot wall requires <strong>1,450 bricks</strong>.
                <br>• House floor plan wall lengths from diagram (NCERT Page 171):
                <br>&nbsp;&nbsp;Outer and inner wall segments: 12 ft, 12 ft, 12 ft, 15 ft, 9 ft, 15 ft, 9 ft, 9 ft, 9 ft, 6 ft.
                <br>• Goal: Find total bricks required to build the house.
              </p>
            </div>
            <div class="step-box step-2">
              <span class="step-badge">Step 2: Total Wall Length Calculation</span>
              <p>
                Total length of walls = 12 + 12 + 12 + 15 + 9 + 15 + 9 + 9 + 9 + 6
                <br>= 36 + 30 + 36 + 6 = <strong>108 feet</strong>.
              </p>
            </div>
            <div class="step-box step-3">
              <span class="step-badge">Step 3: Trairāśika Formulation</span>
              <p>
                <em>Wall Length (ft) : Bricks :: Wall Length (ft) : Bricks</em>
                <br><strong>10 : 1450 :: 108 : x</strong>
                <br>By cross-multiplication:
                <br><em>x = (1450 × 108) ÷ 10 = 145 × 108</em>.
                <br><em>145 × 100 = 14,500</em>
                <br><em>145 × 8 = 1,160</em>
                <br><em>x = 14,500 + 1,160 = <strong>15,660 bricks</strong></em>.
              </p>
            </div>
            <div class="step-box step-4">
              <span class="step-badge">Step 4: Unitary Rate Check</span>
              <p>
                Bricks per foot = 1450 ÷ 10 = 145 bricks/ft.
                <br>Total bricks = 108 ft × 145 bricks/ft = 15,660 bricks ✓.
              </p>
            </div>
            <div class="step-box step-5">
              <span class="step-badge">Step 5: Final Concluding Answer</span>
              <p>The mason requires <strong>15,660 bricks</strong> to build the house.</p>
            </div>
          </div>
        </div>
      </details>

      <!-- PART E: FIGURE IT OUT (PAGE 175 - Q1 TO Q5) -->
      <h3 class="subheading"><i class="fa-solid fa-list-ol"></i> Part 4.5: Figure it Out — Page 175 (Questions 1 to 5)</h3>

      <!-- FIO PAGE 175 Q1 -->
      <details class="ans-box" id="fio175-q1">
        <summary>Figure it Out Q1 (Page 175): Divide ₹4,500 in the Ratio 2 : 3</summary>
        <div class="ans-content">
          <div class="step-container">
            <div class="step-box step-1">
              <span class="step-badge">Step 1: Given Information &amp; Goal</span>
              <p>Total amount = ₹4,500. Divide into two parts in the ratio 2 : 3.</p>
            </div>
            <div class="step-box step-2">
              <span class="step-badge">Step 2: Total Units &amp; Unit Value</span>
              <p>
                Total parts = <em>2 + 3 = 5 parts</em>.
                <br>Value of 1 part = <em>₹4,500 ÷ 5 = ₹900</em>.
              </p>
            </div>
            <div class="step-box step-3">
              <span class="step-badge">Step 3: Calculating Both Shares</span>
              <p>
                • First Part (2 parts) = <em>2 × ₹900 = <strong>₹1,800</strong></em>.
                <br>• Second Part (3 parts) = <em>3 × ₹900 = <strong>₹2,700</strong></em>.
              </p>
            </div>
            <div class="step-box step-4">
              <span class="step-badge">Step 4: Verification</span>
              <p>
                Sum = ₹1,800 + ₹2,700 = ₹4,500 ✓.
                <br>Ratio = 1800 : 2700 = 18 : 27 = 2 : 3 ✓.
              </p>
            </div>
            <div class="step-box step-5">
              <span class="step-badge">Step 5: Final Concluding Answer</span>
              <p>The two parts are <strong>₹1,800</strong> and <strong>₹2,700</strong>.</p>
            </div>
          </div>
        </div>
      </details>

      <!-- FIO PAGE 175 Q2 -->
      <details class="ans-box" id="fio175-q2">
        <summary>Figure it Out Q2 (Page 175): Acid and Water Solution in 1 : 5 Ratio</summary>
        <div class="ans-content">
          <div class="step-container">
            <div class="step-box step-1">
              <span class="step-badge">Step 1: Given Information &amp; Goal</span>
              <p>
                • Total solution volume = 240 mL.
                <br>• Ratio (Acid : Water) = 1 : 5.
                <br>• Goal: Find volume of acid and water in the solution.
              </p>
            </div>
            <div class="step-box step-2">
              <span class="step-badge">Step 2: Total Units</span>
              <p>
                Total parts = <em>1 + 5 = 6 parts</em>.
                <br>Volume of 1 part = <em>240 mL ÷ 6 = 40 mL</em>.
              </p>
            </div>
            <div class="step-box step-3">
              <span class="step-badge">Step 3: Calculating Individual Volumes</span>
              <p>
                • Volume of Acid (1 part) = <em>1 × 40 mL = <strong>40 mL</strong></em>.
                <br>• Volume of Water (5 parts) = <em>5 × 40 mL = <strong>200 mL</strong></em>.
              </p>
            </div>
            <div class="step-box step-4">
              <span class="step-badge">Step 4: Verification</span>
              <p>
                40 mL + 200 mL = 240 mL ✓.
                <br>Ratio = 40 : 200 = 1 : 5 ✓.
              </p>
            </div>
            <div class="step-box step-5">
              <span class="step-badge">Step 5: Final Concluding Answer</span>
              <p>The solution contains <strong>40 mL of acid</strong> and <strong>200 mL of water</strong>.</p>
            </div>
          </div>
        </div>
      </details>

      <!-- FIO PAGE 175 Q3 -->
      <details class="ans-box" id="fio175-q3">
        <summary>Figure it Out Q3 (Page 175): Green Paint Mixture &amp; Adding Yellow Paint</summary>
        <div class="ans-content">
          <div class="step-container">
            <div class="step-box step-1">
              <span class="step-badge">Step 1: Given Information &amp; Goal</span>
              <p>
                • Blue and yellow paints mixed in ratio 3 : 5 to produce green paint.
                <br>• Batch volume = 40 mL green paint.
                <br>• Action: 20 mL of yellow paint is added to make a lighter shade.
                <br>• Goal: Find original quantities of blue and yellow, and determine the new ratio.
              </p>
            </div>
            <div class="step-box step-2">
              <span class="step-badge">Step 2: Quantities in Original 40 mL Paint</span>
              <p>
                Total parts = 3 + 5 = 8 parts.
                <br>Volume per part = 40 mL ÷ 8 = 5 mL.
                <br>• Blue paint = <em>3 × 5 mL = <strong>15 mL</strong></em>.
                <br>• Yellow paint = <em>5 × 5 mL = <strong>25 mL</strong></em>.
              </p>
            </div>
            <div class="step-box step-3">
              <span class="step-badge">Step 3: Adding 20 mL Yellow Paint</span>
              <p>
                • New yellow paint volume = 25 mL + 20 mL = <strong>45 mL</strong>.
                <br>• Blue paint volume remains = <strong>15 mL</strong>.
                <br>• New Ratio (Blue : Yellow) = 15 : 45.
                <br>Divide by HCF(15, 45) = 15:
                <br><em>(15 ÷ 15) : (45 ÷ 15) = <strong>1 : 3</strong></em>.
              </p>
            </div>
            <div class="step-box step-4">
              <span class="step-badge">Step 4: Textbook Answer Key Note</span>
              <p>
                <em>Pedagogical Note:</em> In the NCERT textbook appendix (Page 175 answer key), the printed answer mentions "3 : 13" by cross-referencing Question 5's bucket problem (3/8 : 13/8). For 40 mL mixture + 20 mL yellow, the exact physical ratio is <strong>15 : 45 = 1 : 3</strong>.
              </p>
            </div>
            <div class="step-box step-5">
              <span class="step-badge">Step 5: Final Concluding Answer</span>
              <p>To produce 40 mL of green paint, <strong>15 mL of blue</strong> and <strong>25 mL of yellow</strong> are needed. After adding 20 mL yellow, the new ratio of blue to yellow is <strong>1 : 3</strong>.</p>
            </div>
          </div>
        </div>
      </details>

      <!-- FIO PAGE 175 Q4 -->
      <details class="ans-box" id="fio175-q4">
        <summary>Figure it Out Q4 (Page 175): Idli Batter Ingredients (Rice : Urad Dal = 2 : 1)</summary>
        <div class="ans-content">
          <div class="step-container">
            <div class="step-box step-1">
              <span class="step-badge">Step 1: Given Information &amp; Goal</span>
              <p>
                • Recipe ratio: Rice : Urad Dal = 2 : 1.
                <br>• Total mixture needed = 6 cups.
                <br>• Goal: Find cups of rice and urad dal needed.
              </p>
            </div>
            <div class="step-box step-2">
              <span class="step-badge">Step 2: Total Units &amp; Unit Cup Size</span>
              <p>
                Total parts = 2 + 1 = 3 parts.
                <br>Cups per part = 6 cups ÷ 3 = <strong>2 cups</strong>.
              </p>
            </div>
            <div class="step-box step-3">
              <span class="step-badge">Step 3: Calculating Ingredients</span>
              <p>
                • Rice needed (2 parts) = 2 × 2 cups = <strong>4 cups</strong>.
                <br>• Urad Dal needed (1 part) = 1 × 2 cups = <strong>2 cups</strong>.
              </p>
            </div>
            <div class="step-box step-4">
              <span class="step-badge">Step 4: Verification</span>
              <p>4 cups + 2 cups = 6 cups ✓. Ratio = 4 : 2 = 2 : 1 ✓.</p>
            </div>
            <div class="step-box step-5">
              <span class="step-badge">Step 5: Final Concluding Answer</span>
              <p>You will need <strong>4 cups of rice</strong> and <strong>2 cups of urad dal</strong>.</p>
            </div>
          </div>
        </div>
      </details>

      <!-- FIO PAGE 175 Q5 -->
      <details class="ans-box" id="fio175-q5">
        <summary>Figure it Out Q5 (Page 175): Orange Paint Mixed with Equal Bucket of Yellow</summary>
        <div class="ans-content">
          <div class="step-container">
            <div class="step-box step-1">
              <span class="step-badge">Step 1: Given Information &amp; Goal</span>
              <p>
                • Bucket 1 (Orange paint): Red and yellow paints mixed in ratio 3 : 5.
                <br>• Action: Add another bucket of identical size filled completely with pure yellow paint.
                <br>• Goal: Find the new ratio of red paint to yellow paint in the combined mixture.
              </p>
            </div>
            <div class="step-box step-2">
              <span class="step-badge">Step 2: Unit Allocation per Bucket</span>
              <p>
                Let 1 bucket contain 8 units of volume (since 3 + 5 = 8 parts):
                <br>• In Bucket 1: Red = 3 units, Yellow = 5 units.
                <br>• In Bucket 2: Pure Yellow = 8 units (Red = 0 units).
              </p>
            </div>
            <div class="step-box step-3">
              <span class="step-badge">Step 3: Combining the Mixtures</span>
              <p>
                • Total Red paint = 3 + 0 = <strong>3 units</strong>.
                <br>• Total Yellow paint = 5 + 8 = <strong>13 units</strong>.
                <br>• Total Mixture = 3 + 13 = 16 units (2 buckets).
                <br>Ratio of Red to Yellow = <strong>3 : 13</strong>.
              </p>
            </div>
            <div class="step-box step-4">
              <span class="step-badge">Step 4: Fractional Representation</span>
              <p>
                Red fraction = 3/8 bucket; Yellow fraction = 5/8 + 1 = 13/8 bucket.
                <br>Ratio = (3/8) : (13/8) = 3 : 13 ✓.
              </p>
            </div>
            <div class="step-box step-5">
              <span class="step-badge">Step 5: Final Concluding Answer</span>
              <p>The ratio of red paint to yellow paint in the new mixture is <strong>3 : 13</strong>.</p>
            </div>
          </div>
        </div>
      </details>

      <!-- PART F: FIGURE IT OUT / END EXERCISES (PAGE 176-177 - Q1 TO Q12) -->
      <h3 class="subheading"><i class="fa-solid fa-list-check"></i> Part 4.6: Figure it Out — End Chapter Exercises (Questions 1 to 12)</h3>

      <!-- FIO PAGE 176 Q1 -->
      <details class="ans-box" id="fio176-q1">
        <summary>Exercise 1 (Page 176): Anagh's Fruit Drink Juice Ratio</summary>
        <div class="ans-content">
          <div class="step-container">
            <div class="step-box step-1">
              <span class="step-badge">Step 1: Given Information</span>
              <p>Orange juice = 600 mL; Apple juice = 900 mL. Write ratio in simplest form.</p>
            </div>
            <div class="step-box step-2">
              <span class="step-badge">Step 2: Ratio Setup</span>
              <p>Ratio (Orange : Apple) = 600 : 900.</p>
            </div>
            <div class="step-box step-3">
              <span class="step-badge">Step 3: Simplification</span>
              <p>Divide both terms by HCF(600, 900) = 300:
              <br><em>(600 ÷ 300) : (900 ÷ 300) = <strong>2 : 3</strong></em>.</p>
            </div>
            <div class="step-box step-4">
              <span class="step-badge">Step 4: Verification</span>
              <p>600/900 = 6/9 = 2/3 ✓.</p>
            </div>
            <div class="step-box step-5">
              <span class="step-badge">Step 5: Final Concluding Answer</span>
              <p>The ratio of orange juice to apple juice in its simplest form is <strong>2 : 3</strong>.</p>
            </div>
          </div>
        </div>
      </details>

      <!-- FIO PAGE 176 Q2 -->
      <details class="ans-box" id="fio176-q2">
        <summary>Exercise 2 (Page 176): School Trip Bus Allocation</summary>
        <div class="ans-content">
          <div class="step-container">
            <div class="step-box step-1">
              <span class="step-badge">Step 1: Given Information &amp; Goal</span>
              <p>
                • Last year: 3 buses carried 162 students and teachers (all full).
                <br>• This year: 204 students and teachers.
                <br>• Goal: Find number of buses needed and whether all buses will be full.
              </p>
            </div>
            <div class="step-box step-2">
              <span class="step-badge">Step 2: Capacity per Bus</span>
              <p>Capacity of 1 bus = <em>162 ÷ 3 = <strong>54 seats</strong></em>.</p>
            </div>
            <div class="step-box step-3">
              <span class="step-badge">Step 3: Calculating Buses Required</span>
              <p>
                Number of buses required = <em>204 ÷ 54 = 3 with remainder 42</em> (or 3.78 buses).
                <br>Since a fractional bus cannot be hired, the school must hire <strong>4 buses</strong>.
              </p>
            </div>
            <div class="step-box step-4">
              <span class="step-badge">Step 4: Seat Capacity Analysis</span>
              <p>
                Total capacity of 4 buses = <em>4 × 54 = 216 seats</em>.
                <br>Total passengers = 204.
                <br>Vacant seats = <em>216 - 204 = <strong>12 seats</strong></em>.
              </p>
            </div>
            <div class="step-box step-5">
              <span class="step-badge">Step 5: Final Concluding Answer</span>
              <p>The school will need <strong>4 buses</strong>. <strong>No, all buses will not be full</strong>; exactly <strong>12 seats will remain vacant</strong>.</p>
            </div>
          </div>
        </div>
      </details>

      <!-- FIO PAGE 176 Q3 -->
      <details class="ans-box" id="fio176-q3">
        <summary>Exercise 3 (Page 176): Population Density — Delhi vs Mumbai Crowdedness</summary>
        <div class="ans-content">
          <div class="step-container">
            <div class="step-box step-1">
              <span class="step-badge">Step 1: Given Data</span>
              <p>
                • Delhi: Area = 1,484 sq km; Population ≈ 30 million = 30,000,000 people.
                <br>• Mumbai: Area = 550 sq km; Population ≈ 20 million = 20,000,000 people.
                <br>• Goal: Determine which city is more crowded and justify with mathematical reasoning.
              </p>
            </div>
            <div class="step-box step-2">
              <span class="step-badge">Step 2: Proportional Density Definition</span>
              <p>Crowdedness is measured by <strong>Population Density</strong> = <em>Total Population ÷ Total Land Area</em> (people per sq km).</p>
            </div>
            <div class="step-box step-3">
              <span class="step-badge">Step 3: Calculating Densities</span>
              <p>
                • <strong>Delhi:</strong> <em>30,000,000 ÷ 1,484 ≈ <strong>20,216 people/sq km</strong></em>.
                <br>• <strong>Mumbai:</strong> <em>20,000,000 ÷ 550 ≈ <strong>36,364 people/sq km</strong></em>.
              </p>
            </div>
            <div class="step-box step-4">
              <span class="step-badge">Step 4: Comparative Evaluation</span>
              <p>
                Comparing densities: 36,364 > 20,216.
                <br>Mumbai has approximately <em>36,364 - 20,216 = 16,148 more people</em> living in every single square kilometre! Mumbai's density is about 1.8 times higher.
              </p>
            </div>
            <div class="step-box step-5">
              <span class="step-badge">Step 5: Final Concluding Answer</span>
              <p><strong>Mumbai is significantly more crowded than Delhi</strong> because its population density (≈ 36,364 persons/sq km) is vastly higher than Delhi's (≈ 20,216 persons/sq km).</p>
            </div>
          </div>
        </div>
      </details>

      <!-- FIO PAGE 176 Q4 -->
      <details class="ans-box" id="fio176-q4">
        <summary>Exercise 4 (Page 176): Crane Height &amp; Human Neck Proportion</summary>
        <div class="ans-content">
          <div class="step-container">
            <div class="step-box step-1">
              <span class="step-badge">Step 1: Given Information</span>
              <p>
                • Crane total height = 155 cm.
                <br>• Ratio (Neck : Rest of Body) = 4 : 6 (Total parts = 4 + 6 = 10).
                <br>• Goal: Find crane's neck height, and find neck height for a student of height <em>H</em> (e.g., 150 cm) if proportional to a crane.
              </p>
            </div>
            <div class="step-box step-2">
              <span class="step-badge">Step 2: Neck Fraction of Total Height</span>
              <p>Neck fraction = <em>4 / (4 + 6) = 4/10 = 2/5 = 0.40 (40% of total height)</em>.</p>
            </div>
            <div class="step-box step-3">
              <span class="step-badge">Step 3: Calculating Crane's Neck &amp; Student's Neck</span>
              <p>
                • Crane's neck height = <em>(4/10) × 155 cm = 62 cm</em>.
                <br>• For a student of height 150 cm:
                <br>&nbsp;&nbsp;Neck height = <em>(4/10) × 150 cm = <strong>60 cm</strong></em>.
              </p>
            </div>
            <div class="step-box step-4">
              <span class="step-badge">Step 4: Biological Reflection</span>
              <p>
                A human neck of 60 cm on a 150 cm body would be huge (40% of body height)! A human's neck is usually only 10-12 cm (about 7-8% of total height), showing how cranes evolved specialized anatomy for wetland feeding.
              </p>
            </div>
            <div class="step-box step-5">
              <span class="step-badge">Step 5: Final Concluding Answer</span>
              <p>The neck height formula is <strong>Neck = 0.4 × Total Height</strong>. For a height of 150 cm, the neck would be <strong>60 cm tall</strong>.</p>
            </div>
          </div>
        </div>
      </details>

      <!-- FIO PAGE 176 Q5 -->
      <details class="ans-box" id="fio176-q5">
        <summary>Exercise 5 (Page 176-177): Ancient Līlāvatī Saffron Currency Exchange</summary>
        <div class="ans-content">
          <div class="step-container">
            <div class="step-box step-1">
              <span class="step-badge">Step 1: Given Verse &amp; Data</span>
              <p>
                From Bhāskarāchārya's <em>Līlāvatī</em> (1150 CE):
                <br>• 2 ½ palas (2.5 or 5/2 palas) of saffron costs 3/7 niskas.
                <br>• Goal: Find quantity of saffron bought for 9 niskas.
              </p>
            </div>
            <div class="step-box step-2">
              <span class="step-badge">Step 2: Trairāśika Formulation</span>
              <p>
                Cost and saffron mass are directly proportional:
                <br><em>Cost (niskas) : Saffron (palas) :: Cost (niskas) : Saffron (palas)</em>
                <br><strong>(3/7) : (5/2) :: 9 : x</strong>
                <br>Pramāṇa = 3/7 niskas, Phala = 5/2 palas, Ichchhā = 9 niskas, Ichchhāphala = <em>x</em>.
              </p>
            </div>
            <div class="step-box step-3">
              <span class="step-badge">Step 3: Calculating by Āryabhaṭa's Rule</span>
              <p>
                <em>x = (Phala × Ichchhā) ÷ Pramāṇa</em>
                <br><em>x = [(5/2) × 9] ÷ (3/7)</em>
                <br><em>x = (45/2) × (7/3)</em>
                <br>Simplify 45 ÷ 3 = 15:
                <br><em>x = (15 × 7) ÷ 2 = 105 ÷ 2 = <strong>52.5 palas</strong></em> (or 52 ½ palas).
              </p>
            </div>
            <div class="step-box step-4">
              <span class="step-badge">Step 4: Unitary Verification</span>
              <p>
                Saffron bought per 1 niska = <em>(5/2) ÷ (3/7) = 35/6 palas</em>.
                <br>For 9 niskas = <em>9 × (35/6) = (3 × 35) / 2 = 105/2 = 52.5 palas</em> ✓.
              </p>
            </div>
            <div class="step-box step-5">
              <span class="step-badge">Step 5: Final Concluding Answer</span>
              <p>An expert businessman can buy <strong>52.5 palas (52 ½ palas) of saffron</strong> for 9 niskas.</p>
            </div>
          </div>
        </div>
      </details>

      <!-- FIO PAGE 177 Q6 -->
      <details class="ans-box" id="fio177-q6">
        <summary>Exercise 6 (Page 177): Harmain's Future Age Ratio Problem</summary>
        <div class="ans-content">
          <div class="step-container">
            <div class="step-box step-1">
              <span class="step-badge">Step 1: Given Information &amp; Goal</span>
              <p>
                • Harmain is currently 1 year old.
                <br>• Elder brother is currently 5 years old.
                <br>• Goal: Find Harmain's age when the ratio of her age to her brother's age becomes 1 : 2.
              </p>
            </div>
            <div class="step-box step-2">
              <span class="step-badge">Step 2: Algebraic Formulation</span>
              <p>
                Let <em>x</em> be the number of years that pass.
                <br>After <em>x</em> years:
                <br>Harmain's age = <em>1 + x</em>
                <br>Brother's age = <em>5 + x</em>
                <br>Ratio: <strong>(1 + x) / (5 + x) = 1 / 2</strong>
              </p>
            </div>
            <div class="step-box step-3">
              <span class="step-badge">Step 3: Solving the Linear Equation</span>
              <p>
                Cross-multiply:
                <br><em>2 × (1 + x) = 1 × (5 + x)</em>
                <br><em>2 + 2x = 5 + x</em>
                <br>Subtract <em>x</em> from both sides:
                <br><em>2 + x = 5</em>
                <br><em>x = 5 - 2 = 3 years</em>.
              </p>
            </div>
            <div class="step-box step-4">
              <span class="step-badge">Step 4: Age Verification</span>
              <p>
                After 3 years:
                <br>Harmain's age = 1 + 3 = 4 years old.
                <br>Brother's age = 5 + 3 = 8 years old.
                <br>Ratio = 4 : 8 = 1 : 2 ✓. Exactly matches the required ratio!
              </p>
            </div>
            <div class="step-box step-5">
              <span class="step-badge">Step 5: Final Concluding Answer</span>
              <p>Harmain will be <strong>4 years old</strong> (after 3 years) when the ratio of her age to her brother's age is 1 : 2.</p>
            </div>
          </div>
        </div>
      </details>

      <!-- FIO PAGE 177 Q7 -->
      <details class="ans-box" id="fio177-q7">
        <summary>Exercise 7 (Page 177): Mass of 1 Litre of Gold (Gold vs Water Density)</summary>
        <div class="ans-content">
          <div class="step-container">
            <div class="step-box step-1">
              <span class="step-badge">Step 1: Given Information &amp; Goal</span>
              <p>
                • Ratio of mass of equal volumes (Gold : Water) = 37 : 2.
                <br>• Mass of 1 litre of water = 1 kg.
                <br>• Goal: Find the mass of 1 litre of gold.
              </p>
            </div>
            <div class="step-box step-2">
              <span class="step-badge">Step 2: Proportional Formulation</span>
              <p>
                <em>Mass of Gold : Mass of Water :: 37 : 2</em>
                <br>Let mass of 1 L gold be <em>x</em> kg.
                <br><strong>x : 1 :: 37 : 2</strong>
              </p>
            </div>
            <div class="step-box step-3">
              <span class="step-badge">Step 3: Calculating by Cross-Multiplication</span>
              <p>
                <em>2 × x = 37 × 1</em>
                <br><em>x = 37 ÷ 2 = <strong>18.5 kg</strong></em>.
              </p>
            </div>
            <div class="step-box step-4">
              <span class="step-badge">Step 4: Scientific Consistency Check</span>
              <p>
                The relative density (specific gravity) of gold in physics is 19.3. In this textbook problem, the simplified ratio 37 : 2 gives 18.5 kg/L, which illustrates how dense gold is compared to water.
              </p>
            </div>
            <div class="step-box step-5">
              <span class="step-badge">Step 5: Final Concluding Answer</span>
              <p>The mass of 1 litre of gold is <strong>18.5 kg</strong>.</p>
            </div>
          </div>
        </div>
      </details>

      <!-- FIO PAGE 177 Q8 -->
      <details class="ans-box" id="fio177-q8">
        <summary>Exercise 8 (Page 177): Cow Manure Required for Tomato Plot</summary>
        <div class="ans-content">
          <div class="step-container">
            <div class="step-box step-1">
              <span class="step-badge">Step 1: Given Standards &amp; Dimensions</span>
              <p>
                • Standard application rate: 10 tonnes of cow manure per 1 acre.
                <br>• Unit standard: 1 acre = 43,560 sq ft; 1 tonne = 1,000 kg.
                <br>• Plot dimensions: Length = 500 ft, Width = 200 ft.
                <br>• Goal: Find manure required in tonnes and kg.
              </p>
            </div>
            <div class="step-box step-2">
              <span class="step-badge">Step 2: Calculating Plot Area</span>
              <p>Area of plot = <em>200 ft × 500 ft = <strong>100,000 sq ft</strong></em>.</p>
            </div>
            <div class="step-box step-3">
              <span class="step-badge">Step 3: Trairāśika Proportion Setup</span>
              <p>
                <em>Area (sq ft) : Manure (tonnes) :: Area (sq ft) : Manure (tonnes)</em>
                <br><strong>43,560 : 10 :: 100,000 : x</strong>
                <br><em>x = (100,000 × 10) ÷ 43,560 = 1,000,000 ÷ 43,560 ≈ <strong>22.9568 tonnes</strong></em>.
                <br>In kilograms: 22.9568 × 1,000 kg ≈ <strong>22,956.8 kg</strong>.
              </p>
            </div>
            <div class="step-box step-4">
              <span class="step-badge">Step 4: Alternative Acre Method</span>
              <p>
                Plot area in acres = 100,000 ÷ 43,560 ≈ 2.29568 acres.
                <br>Manure needed = 2.29568 acres × 10 tonnes/acre = 22.9568 tonnes ✓.
              </p>
            </div>
            <div class="step-box step-5">
              <span class="step-badge">Step 5: Final Concluding Answer</span>
              <p>The farmer should buy approximately <strong>22.96 tonnes (or 22,956.8 kg) of cow manure</strong>.</p>
            </div>
          </div>
        </div>
      </details>

      <!-- FIO PAGE 177 Q9 -->
      <details class="ans-box" id="fio177-q9">
        <summary>Exercise 9 (Page 177): Tap Filling Time for 10-Litre Bucket</summary>
        <div class="ans-content">
          <div class="step-container">
            <div class="step-box step-1">
              <span class="step-badge">Step 1: Given Information &amp; Goal</span>
              <p>
                • Tap fills 500 mL mug in 15 seconds.
                <br>• Bucket capacity = 10 Litres.
                <br>• Goal: Find time taken to fill the bucket.
              </p>
            </div>
            <div class="step-box step-2">
              <span class="step-badge">Step 2: Unit Harmonization</span>
              <p>1 Litre = 1,000 mL ⇒ 10 Litres = <em>10 × 1,000 = <strong>10,000 mL</strong></em>.</p>
            </div>
            <div class="step-box step-3">
              <span class="step-badge">Step 3: Trairāśika Proportion</span>
              <p>
                <em>Volume (mL) : Time (s) :: Volume (mL) : Time (s)</em>
                <br><strong>500 : 15 :: 10,000 : t</strong>
                <br><em>t = (10,000 × 15) ÷ 500 = 20 × 15 = <strong>300 seconds</strong></em>.
                <br>Convert to minutes: <em>300 ÷ 60 = <strong>5 minutes</strong></em>.
              </p>
            </div>
            <div class="step-box step-4">
              <span class="step-badge">Step 4: Verification via Number of Mugs</span>
              <p>
                Number of mugs in 10 L bucket = 10,000 ÷ 500 = 20 mugs.
                <br>Time = 20 mugs × 15 seconds/mug = 300 seconds = 5 minutes ✓.
              </p>
            </div>
            <div class="step-box step-5">
              <span class="step-badge">Step 5: Final Concluding Answer</span>
              <p>The tap takes <strong>300 seconds (or 5 minutes)</strong> to fill the 10-litre bucket.</p>
            </div>
          </div>
        </div>
      </details>

      <!-- FIO PAGE 177 Q10 -->
      <details class="ans-box" id="fio177-q10">
        <summary>Exercise 10 (Page 177): Cost of 2,400 Square Feet of Land</summary>
        <div class="ans-content">
          <div class="step-container">
            <div class="step-box step-1">
              <span class="step-badge">Step 1: Given Information &amp; Goal</span>
              <p>
                • Cost of 1 acre of land = ₹15,00,000 (15 Lakhs).
                <br>• Unit equivalence: 1 acre = 43,560 sq ft.
                <br>• Goal: Find cost of 2,400 square feet of the same land.
              </p>
            </div>
            <div class="step-box step-2">
              <span class="step-badge">Step 2: Proportional Setup</span>
              <p>
                <em>Area (sq ft) : Cost (₹) :: Area (sq ft) : Cost (₹)</em>
                <br><strong>43,560 : 15,00,000 :: 2,400 : C</strong>
              </p>
            </div>
            <div class="step-box step-3">
              <span class="step-badge">Step 3: Step-by-Step Calculation</span>
              <p>
                <em>C = (15,00,000 × 2,400) ÷ 43,560</em>
                <br><em>C = 3,600,000,000 ÷ 43,560</em>
                <br>Divide both by 120: 30,000,000 ÷ 363 ≈ <strong>₹82,644.63</strong>.
                <br>Rounded to the nearest rupee: <strong>₹82,645</strong>.
              </p>
            </div>
            <div class="step-box step-4">
              <span class="step-badge">Step 4: Price per Sq Ft Check</span>
              <p>
                Cost per sq ft = ₹15,00,000 ÷ 43,560 ≈ ₹34.435 per sq ft.
                <br>Cost of 2,400 sq ft = 2,400 × ₹34.435 ≈ ₹82,644.63 ✓.
              </p>
            </div>
            <div class="step-box step-5">
              <span class="step-badge">Step 5: Final Concluding Answer</span>
              <p>The cost of 2,400 square feet of the land is approximately <strong>₹82,645</strong>.</p>
            </div>
          </div>
        </div>
      </details>

      <!-- FIO PAGE 177 Q11 -->
      <details class="ans-box" id="fio177-q11">
        <summary>Exercise 11 (Page 177): Tractor vs Pair of Oxen Ploughing Time</summary>
        <div class="ans-content">
          <div class="step-container">
            <div class="step-box step-1">
              <span class="step-badge">Step 1: Given Information &amp; Goal</span>
              <p>
                • Tractor ploughs 4 times faster than a pair of oxen.
                <br>• Oxen time per acre = 6 hours.
                <br>• Total field area = 20 acres.
                <br>• Goal: Find time taken to plough the entire 20 acres using: (i) Oxen, (ii) Tractor.
              </p>
            </div>
            <div class="step-box step-2">
              <span class="step-badge">Step 2: Time Taken per Acre</span>
              <p>
                • Oxen: 6 hours per acre.
                <br>• Tractor: "4 times faster" means the time taken is 1/4th of the oxen's time:
                <br>&nbsp;&nbsp;Tractor time per acre = <em>6 ÷ 4 = 1.5 hours (1 hour 30 min)</em>.
              </p>
            </div>
            <div class="step-box step-3">
              <span class="step-badge">Step 3: Calculating Total Time for 20 Acres</span>
              <p>
                • <strong>Using Oxen:</strong> <em>20 acres × 6 hours/acre = <strong>120 hours</strong></em>.
                <br>• <strong>Using Tractor:</strong> <em>20 acres × 1.5 hours/acre = <strong>30 hours</strong></em>.
              </p>
            </div>
            <div class="step-box step-4">
              <span class="step-badge">Step 4: Speed Ratio Check</span>
              <p>
                Time ratio (Tractor : Oxen) = 30 : 120 = 1 : 4.
                <br>Since 120 ÷ 30 = 4, the tractor indeed completes the work 4 times faster ✓.
              </p>
            </div>
            <div class="step-box step-5">
              <span class="step-badge">Step 5: Final Concluding Answer</span>
              <p>It would take <strong>120 hours</strong> using a pair of oxen, and only <strong>30 hours</strong> if the farmer uses a tractor.</p>
            </div>
          </div>
        </div>
      </details>

      <!-- FIO PAGE 177 Q12 -->
      <details class="ans-box" id="fio177-q12">
        <summary>Exercise 12 (Page 177): Metal Costs in a ₹10 Cupro-Nickel Coin</summary>
        <div class="ans-content">
          <div class="step-container">
            <div class="step-box step-1">
              <span class="step-badge">Step 1: Given Information &amp; Rates</span>
              <p>
                • Alloy composition: Copper : Nickel = 3 : 1 (Total parts = 3 + 1 = 4).
                <br>• Mass of ₹10 coin = 7.74 grams.
                <br>• Cost of copper = ₹906 per kg = ₹0.906 per gram.
                <br>• Cost of nickel = ₹1,341 per kg = ₹1.341 per gram.
                <br>• Goal: Find the cost of each metal and total metal cost in the coin.
              </p>
            </div>
            <div class="step-box step-2">
              <span class="step-badge">Step 2: Calculating Mass of Each Metal</span>
              <p>
                • <strong>Mass of Copper</strong> = <em>(3/4) × 7.74 g = 3 × 1.935 g = <strong>5.805 grams</strong></em>.
                <br>• <strong>Mass of Nickel</strong> = <em>(1/4) × 7.74 g = <strong>1.935 grams</strong></em>.
                <br>Sum = 5.805 + 1.935 = 7.74 g ✓.
              </p>
            </div>
            <div class="step-box step-3">
              <span class="step-badge">Step 3: Calculating Metal Costs</span>
              <p>
                • <strong>Cost of Copper:</strong>
                <br><em>(5.805 g ÷ 1000 g) × ₹906 = 0.005805 × 906 ≈ <strong>₹5.25933 ≈ ₹5.26</strong></em>.
                <br>• <strong>Cost of Nickel:</strong>
                <br><em>(1.935 g ÷ 1000 g) × ₹1,341 = 0.001935 × 1341 ≈ <strong>₹2.594835 ≈ ₹2.59</strong></em>.
              </p>
            </div>
            <div class="step-box step-4">
              <span class="step-badge">Step 4: Total Metal Value &amp; Seigniorage</span>
              <p>
                Total metal cost = <em>₹5.26 + ₹2.59 = <strong>₹7.85</strong></em>.
                <br>Notice that ₹7.85 is less than the coin's face value (₹10.00). The difference of ₹2.15 is the government's seigniorage (profit margin covering minting and distribution).
              </p>
            </div>
            <div class="step-box step-5">
              <span class="step-badge">Step 5: Final Concluding Answer</span>
              <p>The cost of copper in the coin is <strong>₹5.26</strong> and the cost of nickel is <strong>₹2.59</strong>, making a total metal value of <strong>₹7.85</strong>.</p>
            </div>
          </div>
        </div>
      </details>

      <!-- LOGIC PUZZLE: BINAIRO / TAKUZU -->
      <details class="ans-box" id="act-binairo">
        <summary>Binairo (Takuzu) Logic Grid Puzzle: Rules, Deductions &amp; Solution (NCERT Page 178)</summary>
        <div class="ans-content">
          <div class="step-container">
            <div class="step-box step-1">
              <span class="step-badge">Step 1: The Three Golden Rules of Binairo</span>
              <p>
                1. <strong>Balanced Parity:</strong> In a 6×6 grid, each row and column must contain exactly 3 horizontal lines (—) and 3 vertical lines (|).
                <br>2. <strong>No Triplets:</strong> No more than two identical lines can be adjacent (e.g., neither — — — nor | | | is allowed).
                <br>3. <strong>Uniqueness:</strong> Every completed row must be unique, and every completed column must be unique.
              </p>
            </div>
            <div class="step-box step-2">
              <span class="step-badge">Step 2: Initial Given Grid Cells</span>
              <p>
                Row 1: (1,1)=|, (1,3)=|
                <br>Row 2: (2,2)=—, (2,5)=|
                <br>Row 3: (3,4)=—, (3,6)=—
                <br>Row 4: (4,1)=|, (4,3)=—
                <br>Row 5: (5,2)=|, (5,5)=—
                <br>Row 6: (6,4)=|, (6,6)=|
              </p>
            </div>
            <div class="step-box step-3">
              <span class="step-badge">Step 3: Step-by-Step Logic Deductions</span>
              <p>
                • <strong>Sandwich Rule:</strong> If two cells of the same mark have one empty cell between them, the middle cell must be the opposite mark (e.g., | [ ] | must be filled with —).
                <br>&nbsp;&nbsp;Applying to Row 1: | [ ] | ⇒ Cell (1,2) must be <strong>—</strong>.
                <br>• <strong>Double Mark Boundary:</strong> Two adjacent identical marks must be capped by the opposite mark on both sides.
                <br>&nbsp;&nbsp;Applying to Row 3: (3,4)=— and (3,6)=— with (3,5) between them ⇒ (3,5) must be <strong>|</strong>.
                <br>• <strong>Row &amp; Column Counting:</strong> Once a line has three of one symbol, all remaining cells must be filled with the other symbol!
              </p>
            </div>
            <div class="step-box step-4">
              <span class="step-badge">Step 4: Complete Row-by-Row Solution</span>
              <p style="font-family: 'JetBrains Mono', monospace; font-size: 1.1rem; line-height: 1.8;">
                Row 1: | &nbsp;— &nbsp;| &nbsp;— &nbsp;| &nbsp;— &nbsp;(3 |, 3 —)<br>
                Row 2: — &nbsp;— &nbsp;| &nbsp;| &nbsp;— &nbsp;| &nbsp;(3 |, 3 —)<br>
                Row 3: | &nbsp;| &nbsp;— &nbsp;— &nbsp;| &nbsp;— &nbsp;(3 |, 3 —)<br>
                Row 4: | &nbsp;— &nbsp;— &nbsp;| &nbsp;— &nbsp;| &nbsp;(3 |, 3 —)<br>
                Row 5: — &nbsp;| &nbsp;| &nbsp;— &nbsp;— &nbsp;| &nbsp;(3 |, 3 —)<br>
                Row 6: — &nbsp;| &nbsp;— &nbsp;| &nbsp;| &nbsp;— &nbsp;(3 |, 3 —)
              </p>
            </div>
            <div class="step-box step-5">
              <span class="step-badge">Step 5: Final Concluding Answer</span>
              <p>Every row and column contains exactly 3 horizontal and 3 vertical lines, no triplets exist, and all rows and columns are completely unique.</p>
            </div>
          </div>
        </div>
      </details>
    </section>
"""
