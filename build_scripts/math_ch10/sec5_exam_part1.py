# -*- coding: utf-8 -*-
"""
Section 5: Complete Exam Question Bank (Part 1: MCQs, Assertion-Reasoning, Short Answer Questions)
Class 8 Mathematics Chapter 10: Proportional Reasoning - 2
"""

def get_section_5_part1():
    return """
    <!-- ==========================================================
         SECTION 5: COMPLETE EXAM QUESTION BANK (PART 1)
         ========================================================== -->
    <section id="section5" class="section-box">
      <div class="section-header">
        <div class="section-header-left">
          <span class="section-tag"><i class="fa-solid fa-graduation-cap"></i> Complete Exam Question Bank</span>
          <h2 class="section-title">Section 5: Complete Exam Question Bank</h2>
          <p class="section-desc">
            Exhaustive, examination-standard test repository featuring interactive MCQs with trap analysis, Assertion-Reasoning drills, and scored step-by-step Short Answer Questions.
          </p>
        </div>
        <div class="score-badge" id="quizScoreDisplay">
          <i class="fa-solid fa-trophy"></i> Score: 0 / 5
        </div>
      </div>

      <!-- Sub-Section 5A: 5 Conceptual MCQs with Traps -->
      <h3 style="font-size: 1.35rem; color: var(--primary-dark); margin: 1.5rem 0 1rem; border-bottom: 2px solid #e2e8f0; padding-bottom: 0.5rem;">
        <i class="fa-solid fa-circle-question"></i> Sub-Section 5A: Conceptual Multiple Choice Questions (Interactive Quiz)
      </h3>

      <!-- MCQ 1 -->
      <div class="mcq-card" id="mcqCard1">
        <div class="mcq-question">
          <strong>Q1.</strong> Which one of the following physical pairs of quantities varies in <strong>INVERSE PROPORTION</strong>?
        </div>
        <div class="options-grid">
          <button class="option-btn" onclick="evaluateMCQ(1, 'A', false, 'The number of articles bought and their total cost is in DIRECT proportion (more articles cost more money at a fixed rate: Cost = Price × Quantity).')">
            <span class="pos-badge">A</span> The number of identical articles purchased and the total cost paid.
          </button>
          <button class="option-btn" onclick="evaluateMCQ(1, 'B', true, 'Correct! For any fixed track distance, Speed × Time = Constant Distance. When speed doubles, travel time halves, which is the exact mathematical definition of inverse proportion (s · t = k).')">
            <span class="pos-badge">B</span> The speed of an express train and the time taken to cover a fixed track distance.
          </button>
          <button class="option-btn" onclick="evaluateMCQ(1, 'C', false, 'Age and height both increase during childhood, but they do NOT vary proportionally! When age doubles from 5 to 10 years, a child does not double in height from 100 cm to 200 cm.')">
            <span class="pos-badge">C</span> The biological age of a banyan tree and its height in metres.
          </button>
          <button class="option-btn" onclick="evaluateMCQ(1, 'D', false, 'The circumference of a circle is C = π · d. Circumference and diameter vary in DIRECT proportion with constant quotient π (approx 3.1416).')">
            <span class="pos-badge">D</span> The circumference of a circular bicycle wheel and its diameter.
          </button>
        </div>
        <div class="trap-feedback" id="feedback1"></div>
      </div>

      <!-- MCQ 2 -->
      <div class="mcq-card" id="mcqCard2">
        <div class="mcq-question">
          <strong>Q2.</strong> On a state cartographic atlas map with <code>RF 1 : 25,00,000</code>, the straight-line ruler distance between Puri and Konark measures <strong>1.4 cm</strong>. What is the actual geographical distance between the two holy towns on the ground?
        </div>
        <div class="options-grid">
          <button class="option-btn" onclick="evaluateMCQ(2, 'A', false, 'Unit conversion error! You divided by 10,000 instead of 1,00,000. 1 km contains 1,00,000 cm, not 10,000 cm.')">
            <span class="pos-badge">A</span> 350 km
          </button>
          <button class="option-btn" onclick="evaluateMCQ(2, 'B', true, 'Correct! Ground Distance = 1.4 cm × 25,00,000 = 35,00,000 cm. Since 1 km = 1,00,000 cm, 35,00,000 ÷ 1,00,000 = 35 km!')">
            <span class="pos-badge">B</span> 35 km
          </button>
          <button class="option-btn" onclick="evaluateMCQ(2, 'C', false, 'Arithmetic slip! Dividing 35,00,000 cm by 1,00,000 gives 35 km, not 3.5 km.')">
            <span class="pos-badge">C</span> 3.5 km
          </button>
          <button class="option-btn" onclick="evaluateMCQ(2, 'D', false, 'Arbitrary guess! Use the formula: Ground km = (Map cm × Scale Denominator) ÷ 1,00,000.')">
            <span class="pos-badge">D</span> 17.8 km
          </button>
        </div>
        <div class="trap-feedback" id="feedback2"></div>
      </div>

      <!-- MCQ 3 -->
      <div class="mcq-card" id="mcqCard3">
        <div class="mcq-question">
          <strong>Q3.</strong> An ancient temple bell metal alloy is forged by combining Copper, Tin, and Zinc in the multi-term ratio <code>15 : 4 : 1</code>. If a master bell weighing <strong>160 kg</strong> is cast, what is the exact weight of Tin contained in the bell?
        </div>
        <div class="options-grid">
          <button class="option-btn" onclick="evaluateMCQ(3, 'A', false, '120 kg is the mass of Copper (15 × 8 kg), not Tin!')">
            <span class="pos-badge">A</span> 120 kg
          </button>
          <button class="option-btn" onclick="evaluateMCQ(3, 'B', true, 'Correct! Sum of ratio terms = 15 + 4 + 1 = 20 parts. Value of 1 part = 160 kg ÷ 20 = 8 kg. Tin corresponds to 4 parts: 4 × 8 kg = 32 kg.')">
            <span class="pos-badge">B</span> 32 kg
          </button>
          <button class="option-btn" onclick="evaluateMCQ(3, 'C', false, '8 kg is the mass of Zinc (1 part), not Tin!')">
            <span class="pos-badge">C</span> 8 kg
          </button>
          <button class="option-btn" onclick="evaluateMCQ(3, 'D', false, 'Common trap! You computed 160 ÷ 4 = 40 kg. You must divide the whole by the SUM of all parts (20), not by Tin\'s individual ratio number!')">
            <span class="pos-badge">D</span> 40 kg
          </button>
        </div>
        <div class="trap-feedback" id="feedback3"></div>
      </div>

      <!-- MCQ 4 -->
      <div class="mcq-card" id="mcqCard4">
        <div class="mcq-question">
          <strong>Q4.</strong> In an urban transportation census, <strong>35%</strong> of commuters travel by rapid metro rail. If a statistical pie chart is drawn, what is the central sector angle subtended by the metro rail slice?
        </div>
        <div class="options-grid">
          <button class="option-btn" onclick="evaluateMCQ(4, 'A', false, 'The classic student blunder! 35% does NOT mean 35°! A full circle contains 360°, not 100°. You must compute 35% OF 360°.')">
            <span class="pos-badge">A</span> 35°
          </button>
          <button class="option-btn" onclick="evaluateMCQ(4, 'B', false, 'Incorrect. 70° would correspond to 70 ÷ 3.6 ≈ 19.4%, not 35%.')">
            <span class="pos-badge">B</span> 70°
          </button>
          <button class="option-btn" onclick="evaluateMCQ(4, 'C', true, 'Correct! Central Angle θ = (Percentage / 100) × 360° = 0.35 × 360° = 126°!')">
            <span class="pos-badge">C</span> 126°
          </button>
          <button class="option-btn" onclick="evaluateMCQ(4, 'D', false, 'Incorrect. 140° would represent 140 ÷ 3.6 ≈ 38.89%.')">
            <span class="pos-badge">D</span> 140°
          </button>
        </div>
        <div class="trap-feedback" id="feedback4"></div>
      </div>

      <!-- MCQ 5 -->
      <div class="mcq-card" id="mcqCard5">
        <div class="mcq-question">
          <strong>Q5.</strong> Inflow Pipe A fills an empty water reservoir in <strong>4 hours</strong>, while Outflow Drain Pipe B empties the full reservoir in <strong>6 hours</strong>. If both pipes are opened simultaneously when the reservoir is completely empty, how long will it take to fill the reservoir?
        </div>
        <div class="options-grid">
          <button class="option-btn" onclick="evaluateMCQ(5, 'A', false, 'You added the rates (1/4 + 1/6 = 5/12 ⇒ 2.4 hrs)! Pipe B is DRAINING water, so its rate must be SUBTRACTED!')">
            <span class="pos-badge">A</span> 2.4 hours
          </button>
          <button class="option-btn" onclick="evaluateMCQ(5, 'B', false, 'You averaged the times ((4 + 6) / 2 = 5 hrs). Completion times can never be averaged!')">
            <span class="pos-badge">B</span> 5 hours
          </button>
          <button class="option-btn" onclick="evaluateMCQ(5, 'C', false, 'Incorrect subtraction error.')">
            <span class="pos-badge">C</span> 10 hours
          </button>
          <button class="option-btn" onclick="evaluateMCQ(5, 'D', true, 'Correct! Inflow rate = +1/4 tank/hr. Outflow rate = -1/6 tank/hr. Net 1-hour rate = 1/4 - 1/6 = 3/12 - 2/12 = 1/12 tank/hr. Total filling time = 1 ÷ (1/12) = 12 hours!')">
            <span class="pos-badge">D</span> 12 hours
          </button>
        </div>
        <div class="trap-feedback" id="feedback5"></div>
      </div>

      <!-- Sub-Section 5B: 5 Assertion & Reasoning Questions -->
      <h3 style="font-size: 1.35rem; color: var(--secondary); margin: 2.5rem 0 1rem; border-bottom: 2px solid #e2e8f0; padding-bottom: 0.5rem;">
        <i class="fa-solid fa-circle-check"></i> Sub-Section 5B: Assertion &amp; Reasoning Questions
      </h3>
      <p style="font-size: 0.9rem; color: var(--text-muted); margin-bottom: 1.25rem;">
        <strong>Instructions:</strong> Choose from the standard CBSE examination options:<br>
        (A) Both Assertion (A) and Reason (R) are true and Reason (R) is the correct explanation of Assertion (A).<br>
        (B) Both Assertion (A) and Reason (R) are true but Reason (R) is NOT the correct explanation of Assertion (A).<br>
        (C) Assertion (A) is true but Reason (R) is false.<br>
        (D) Assertion (A) is false but Reason (R) is true.
      </p>

      <!-- A&R 1 -->
      <details class="ans-box">
        <summary>
          <span><span class="step-pill">A&amp;R 1</span> Paddy Harvesting Man-Days</span>
        </summary>
        <div class="ans-content">
          <p><strong>Assertion (A):</strong> If 12 agricultural workers can harvest a paddy field in 15 days, then 18 workers working at the same speed will complete harvesting the same field in 10 days.<br>
          <strong>Reason (R):</strong> When a fixed quantum of work is to be completed, the number of workers hired and the number of days required vary in inverse proportion (Workers × Days = Constant Work).</p>
          <div class="ans-step">
            <div class="ans-step-title">Evaluation &amp; Verification</div>
            <p>• Initial work quantum = <code>12 workers × 15 days = 180 worker-days</code>.<br>
            • Days required by 18 workers = <code>180 worker-days ÷ 18 workers = 10 days</code>. Thus, Assertion (A) is mathematically true.<br>
            • Reason (R) correctly formulates the inverse variation principle (w · d = k) which directly explains why Assertion (A) holds.</p>
          </div>
          <div class="ans-step">
            <div class="ans-step-title">Correct Option</div>
            <p><strong>(A) Both Assertion (A) and Reason (R) are true and Reason (R) is the correct explanation of Assertion (A).</strong></p>
          </div>
        </div>
      </details>

      <!-- A&R 2 -->
      <details class="ans-box">
        <summary>
          <span><span class="step-pill">A&amp;R 2</span> 25% Share in a Pie Chart</span>
        </summary>
        <div class="ans-content">
          <p><strong>Assertion (A):</strong> In any circular pie chart, an item that accounts for exactly 25% of the total frequency is represented by a right-angled sector measuring 90° at the centre.<br>
          <strong>Reason (R):</strong> The central angle θ of a sector in a pie chart is determined by the formula: <code>θ = (Percentage / 100) × 360°</code>.</p>
          <div class="ans-step">
            <div class="ans-step-title">Evaluation &amp; Verification</div>
            <p>• Applying the formula in Reason (R): <code>θ = (25 / 100) × 360° = 1/4 × 360° = 90°</code>.<br>
            • An angle of 90° is precisely a right angle. Thus, Assertion (A) is true.<br>
            • Reason (R) provides the exact mathematical law that generates Assertion (A).</p>
          </div>
          <div class="ans-step">
            <div class="ans-step-title">Correct Option</div>
            <p><strong>(A) Both Assertion (A) and Reason (R) are true and Reason (R) is the correct explanation of Assertion (A).</strong></p>
          </div>
        </div>
      </details>

      <!-- A&R 3 -->
      <details class="ans-box">
        <summary>
          <span><span class="step-pill">A&amp;R 3</span> Triangle Sidelength Ratio 3 : 4 : 5 and Congruence</span>
        </summary>
        <div class="ans-content">
          <p><strong>Assertion (A):</strong> All triangles constructed with sidelengths in the ratio <code>3 : 4 : 5</code> are congruent to each other.<br>
          <strong>Reason (R):</strong> When two triangles have their corresponding sidelengths in the identical ratio, their corresponding interior angles are equal, making them similar triangles.</p>
          <div class="ans-step">
            <div class="ans-step-title">Evaluation &amp; Verification</div>
            <p>• Triangles with sides in ratio 3 : 4 : 5 have lengths <code>(3k, 4k, 5k)</code>. A triangle with sides (3, 4, 5 cm) has area 6 cm², while one with sides (6, 8, 10 cm) has area 24 cm². They do NOT have equal size and cannot coincide. Therefore, they are <strong>NOT congruent</strong>! Hence, <strong>Assertion (A) is FALSE</strong>.<br>
            • By the AAA similarity criterion, equal side ratios guarantee that interior angles are identical (90°, 53.13°, 36.87°), making them <strong>similar</strong>. Hence, <strong>Reason (R) is TRUE</strong>.</p>
          </div>
          <div class="ans-step">
            <div class="ans-step-title">Correct Option</div>
            <p><strong>(D) Assertion (A) is false but Reason (R) is true.</strong></p>
          </div>
        </div>
      </details>

      <!-- A&R 4 -->
      <details class="ans-box">
        <summary>
          <span><span class="step-pill">A&amp;R 4</span> Cartographic Scale RF 1 : 50,000</span>
        </summary>
        <div class="ans-content">
          <p><strong>Assertion (A):</strong> On a topographic survey sheet with <code>RF 1 : 50,000</code>, a straight canal measuring <strong>4 cm</strong> on paper corresponds to an actual geographical distance of <strong>2 km</strong> on the ground.<br>
          <strong>Reason (R):</strong> One kilometre contains exactly 1,00,000 centimetres.</p>
          <div class="ans-step">
            <div class="ans-step-title">Evaluation &amp; Verification</div>
            <p>• Ground distance in cm = <code>4 cm × 50,000 = 2,00,000 cm</code>.<br>
            • Using Reason (R) that <code>1 km = 1,00,000 cm</code>, we divide: <code>2,00,000 cm ÷ 1,00,000 cm/km = 2 km</code>.<br>
            • Both Assertion (A) and Reason (R) are true, and Reason (R) directly explains the metric conversion in Assertion (A).</p>
          </div>
          <div class="ans-step">
            <div class="ans-step-title">Correct Option</div>
            <p><strong>(A) Both Assertion (A) and Reason (R) are true and Reason (R) is the correct explanation of Assertion (A).</strong></p>
          </div>
        </div>
      </details>

      <!-- A&R 5 -->
      <details class="ans-box">
        <summary>
          <span><span class="step-pill">A&amp;R 5</span> Speed and Travel Time Invariant</span>
        </summary>
        <div class="ans-content">
          <p><strong>Assertion (A):</strong> If a motorist doubles their cruising speed on an expressway, the time required to complete a fixed journey of 120 km is cut in half.<br>
          <strong>Reason (R):</strong> When distance is constant, speed and travel time are in direct proportion.</p>
          <div class="ans-step">
            <div class="ans-step-title">Evaluation &amp; Verification</div>
            <p>• Since <code>Speed × Time = Constant Distance</code>, multiplying speed by 2 divides time by 2 (e.g., 60 km/h takes 2 hours; 120 km/h takes 1 hour). Thus, <strong>Assertion (A) is TRUE</strong>.<br>
            • Reason (R) claims that speed and time are in <em>direct proportion</em>. That is completely FALSE! Speed and time vary in <strong>INVERSE PROPORTION</strong> (xy = k, not y/x = k). Hence, <strong>Reason (R) is FALSE</strong>.</p>
          </div>
          <div class="ans-step">
            <div class="ans-step-title">Correct Option</div>
            <p><strong>(C) Assertion (A) is true but Reason (R) is false.</strong></p>
          </div>
        </div>
      </details>

      <!-- Sub-Section 5C: 6 Short Answer Questions (2M / 3M) -->
      <h3 style="font-size: 1.35rem; color: var(--purple); margin: 2.5rem 0 1rem; border-bottom: 2px solid #e2e8f0; padding-bottom: 0.5rem;">
        <i class="fa-solid fa-pen-to-square"></i> Sub-Section 5C: Short Answer Questions (2M &amp; 3M) with Marking Schemes
      </h3>

      <!-- SAQ 1 -->
      <details class="ans-box">
        <summary>
          <span><span class="step-pill">SAQ 1 (2M)</span> Petrol Consumption &amp; Mileage (Direct Proportion)</span>
        </summary>
        <div class="ans-content">
          <p><strong>Question:</strong> A car consumes 8 litres of petrol to travel a distance of 144 km. How many litres of petrol are required to cover a distance of 360 km under identical driving conditions?</p>
          <div class="ans-step">
            <div class="ans-step-title">Step 1: Identifying Variation &amp; Variables [0.5 Mark]</div>
            <p>Distance travelled is directly proportional to fuel consumed: <code>d₁ / l₁ = d₂ / l₂</code>.<br>
            Given: <code>d₁ = 144 km</code>, <code>l₁ = 8 L</code>, <code>d₂ = 360 km</code>, <code>l₂ = x</code>.</p>
          </div>
          <div class="ans-step">
            <div class="ans-step-title">Step 2: Mathematical Proportion Setup [0.5 Mark]</div>
            <p><code>144 / 8 = 360 / x</code><br>
            Fuel consumption rate = <code>144 ÷ 8 = 18 km/litre</code>.</p>
          </div>
          <div class="ans-step">
            <div class="ans-step-title">Step 3: Calculation &amp; Final Answer [1.0 Mark]</div>
            <p><code>x = 360 ÷ 18 = 20 litres</code>.<br>
            <strong>Final Answer:</strong> <strong>20 litres</strong> of petrol are required to cover 360 km.</p>
          </div>
        </div>
      </details>

      <!-- SAQ 2 -->
      <details class="ans-box">
        <summary>
          <span><span class="step-pill">SAQ 2 (2M)</span> Garrison Food Provisions (Inverse Proportion)</span>
        </summary>
        <div class="ans-content">
          <p><strong>Question:</strong> A military garrison of 120 soldiers has food provisions that last for 30 days. If 30 more soldiers join the garrison, for how many days will the provisions last at the same daily consumption rate?</p>
          <div class="ans-step">
            <div class="ans-step-title">Step 1: Variable Identification &amp; Nature of Variation [0.5 Mark]</div>
            <p>More soldiers consuming from a fixed store of food means fewer days: <strong>Inverse Proportion</strong>.<br>
            Initial: <code>s₁ = 120 soldiers</code>, <code>d₁ = 30 days</code>.<br>
            New count: <code>s₂ = 120 + 30 = 150 soldiers</code>, <code>d₂ = x days</code>.</p>
          </div>
          <div class="ans-step">
            <div class="ans-step-title">Step 2: Equation Setup [0.5 Mark]</div>
            <p><code>s₁ · d₁ = s₂ · d₂ ⇒ 120 × 30 = 150 × x</code><br>
            <code>3600 = 150x</code>.</p>
          </div>
          <div class="ans-step">
            <div class="ans-step-title">Step 3: Simplification &amp; Final Answer [1.0 Mark]</div>
            <p><code>x = 3600 ÷ 150 = 360 ÷ 15 = 24 days</code>.<br>
            <strong>Final Answer:</strong> The provisions will last for <strong>24 days</strong>.</p>
          </div>
        </div>
      </details>

      <!-- SAQ 3 -->
      <details class="ans-box">
        <summary>
          <span><span class="step-pill">SAQ 3 (3M)</span> Startup Partnership Profit Partition (3 : 5 : 7)</span>
        </summary>
        <div class="ans-content">
          <p><strong>Question:</strong> Three business partners, Ananya, Bikas, and Chinmay, invest in an enterprise in the ratio <code>3 : 5 : 7</code>. If the company earns a net annual profit of <strong>₹1,80,000</strong>, compute each partner's share of the profit.</p>
          <div class="ans-step">
            <div class="ans-step-title">Step 1: Sum of Ratio Terms [0.5 Mark]</div>
            <p>Ratio: <code>Ananya : Bikas : Chinmay = 3 : 5 : 7</code>.<br>
            Sum of parts = <code>3 + 5 + 7 = 15 parts</code>.</p>
          </div>
          <div class="ans-step">
            <div class="ans-step-title">Step 2: Value of One Single Part [1.0 Mark]</div>
            <p><code>Value of 1 part = Total Profit ÷ Sum of Parts = ₹1,80,000 ÷ 15 = ₹12,000</code>.</p>
          </div>
          <div class="ans-step">
            <div class="ans-step-title">Step 3: Calculating Individual Shares &amp; Verification [1.5 Marks]</div>
            <p>• <strong>Ananya's Share:</strong> <code>3 × ₹12,000 = ₹36,000</code>.<br>
            • <strong>Bikas's Share:</strong> <code>5 × ₹12,000 = ₹60,000</code>.<br>
            • <strong>Chinmay's Share:</strong> <code>7 × ₹12,000 = ₹84,000</code>.<br>
            <em>Check:</em> <code>₹36,000 + ₹60,000 + ₹84,000 = ₹1,80,000</code>.<br>
            <strong>Final Answer:</strong> Ananya receives <strong>₹36,000</strong>, Bikas receives <strong>₹60,000</strong>, and Chinmay receives <strong>₹84,000</strong>.</p>
          </div>
        </div>
      </details>

      <!-- SAQ 4 -->
      <details class="ans-box">
        <summary>
          <span><span class="step-pill">SAQ 4 (3M)</span> Quadrilateral Interior Angles in Ratio 2 : 3 : 4 : 6</span>
        </summary>
        <div class="ans-content">
          <p><strong>Question:</strong> The four interior angles of a quadrilateral are in the ratio <code>2 : 3 : 4 : 6</code>. Find the exact measure of each angle and classify whether the quadrilateral is convex.</p>
          <div class="ans-step">
            <div class="ans-step-title">Step 1: Identifying Geometric Property [0.5 Mark]</div>
            <p>The sum of interior angles of any planar quadrilateral is strictly <strong>360°</strong>: <code>∠A + ∠B + ∠C + ∠D = 360°</code>.</p>
          </div>
          <div class="ans-step">
            <div class="ans-step-title">Step 2: Calculating Sum of Parts &amp; Multiplier [1.0 Mark]</div>
            <p>• Sum of parts = <code>2 + 3 + 4 + 6 = 15 parts</code>.<br>
            • Value of 1 part = <code>360° ÷ 15 = 24°</code>.</p>
          </div>
          <div class="ans-step">
            <div class="ans-step-title">Step 3: Calculating Angles &amp; Convexity Analysis [1.5 Marks]</div>
            <p>• <code>∠A = 2 × 24° = 48°</code><br>
            • <code>∠B = 3 × 24° = 72°</code><br>
            • <code>∠C = 4 × 24° = 96°</code><br>
            • <code>∠D = 6 × 24° = 144°</code><br>
            <em>Sum Check:</em> <code>48° + 72° + 96° + 144° = 360°</code>.<br>
            <strong>Convexity Check:</strong> Since every interior angle is strictly less than 180° (maximum is 144° &lt; 180°), this is a <strong>convex quadrilateral</strong>.<br>
            <strong>Final Answer:</strong> The four angles measure <strong>48°, 72°, 96°, and 144°</strong>, and the quadrilateral is convex.</p>
          </div>
        </div>
      </details>

      <!-- SAQ 5 -->
      <details class="ans-box">
        <summary>
          <span><span class="step-pill">SAQ 5 (3M)</span> Dual Water Cistern Taps (40 min &amp; 60 min)</span>
        </summary>
        <div class="ans-content">
          <p><strong>Question:</strong> Tap A can fill a water cistern in 40 minutes, while Tap B can fill the identical cistern in 60 minutes. If both taps are turned on simultaneously, how many minutes will it take to fill the cistern completely?</p>
          <div class="ans-step">
            <div class="ans-step-title">Step 1: Finding 1-Minute Inflow Rates [1.0 Mark]</div>
            <p>• Tap A fills <code>1/40 of the cistern per minute</code>.<br>
            • Tap B fills <code>1/60 of the cistern per minute</code>.</p>
          </div>
          <div class="ans-step">
            <div class="ans-step-title">Step 2: Summing the Inflow Rates [1.0 Mark]</div>
            <p>Find the LCM of 40 and 60, which is 120:<br>
            <code>Combined 1-minute rate = 1/40 + 1/60 = 3/120 + 2/120 = 5/120 = 1/24 of the cistern</code>.</p>
          </div>
          <div class="ans-step">
            <div class="ans-step-title">Step 3: Inverting Rate to Obtain Time [1.0 Mark]</div>
            <p><code>Total Time T = 1 ÷ (1/24) = 24 minutes</code>.<br>
            <em>Direct formula check:</em> <code>(40 × 60) ÷ (40 + 60) = 2400 ÷ 100 = 24 minutes</code>.<br>
            <strong>Final Answer:</strong> It will take exactly <strong>24 minutes</strong> to fill the cistern.</p>
          </div>
        </div>
      </details>

      <!-- SAQ 6 -->
      <details class="ans-box">
        <summary>
          <span><span class="step-pill">SAQ 6 (2M)</span> Book Typesetting: Pages vs. Lines Per Page</span>
        </summary>
        <div class="ans-content">
          <p><strong>Question:</strong> A novel contains 240 pages with an average of 35 lines on each page. If the publisher resets the book using a smaller font with 40 lines on each page, how many pages will the new edition contain?</p>
          <div class="ans-step">
            <div class="ans-step-title">Step 1: Identifying Invariant &amp; Nature of Variation [0.5 Mark]</div>
            <p>The total text content (total number of lines in the book) remains constant. More lines per page means fewer total pages: <strong>Inverse Proportion</strong>: <code>p₁ · l₁ = p₂ · l₂</code>.</p>
          </div>
          <div class="ans-step">
            <div class="ans-step-title">Step 2: Calculating Total Line Invariant [0.5 Mark]</div>
            <p><code>Total Lines = 240 pages × 35 lines/page = 8,400 lines</code>.</p>
          </div>
          <div class="ans-step">
            <div class="ans-step-title">Step 3: Calculating New Page Count [1.0 Mark]</div>
            <p><code>40 × p₂ = 8,400 ⇒ p₂ = 8,400 ÷ 40 = 210 pages</code>.<br>
            <strong>Final Answer:</strong> The new edition will contain <strong>210 pages</strong> (saving 30 pages of paper).</p>
          </div>
        </div>
      </details>
    </section>
"""
