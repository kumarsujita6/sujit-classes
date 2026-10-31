# -*- coding: utf-8 -*-
"""
Section 4: 100% Solved NCERT Questions & Inquiries (Part 2: Inverse Proportions, Work Rates, End-of-Chapter Exercises)
Class 8 Mathematics Chapter 10: Proportional Reasoning - 2
"""

def get_section_4_part2():
    return """
      <!-- Part 2: Section 3.6 & End-of-Chapter Figure It Out Exercises -->
      <h3 style="font-size: 1.35rem; color: var(--secondary); margin: 2.5rem 0 1rem; border-bottom: 2px solid #e2e8f0; padding-bottom: 0.5rem;">
        <i class="fa-solid fa-arrows-left-right"></i> Sub-Section 4B: Inverse Proportions, Speed-Time, Worker Rates &amp; Chapter Exercises
      </h3>

      <!-- 20. In-Text Page 63 Example 1: 5 workers move 4500 bricks -->
      <details class="ans-box">
        <summary>
          <span><span class="step-pill">In-Text Pg 63 Ex 1</span> Moving Bricks: Direct Proportion Rule of Three</span>
        </summary>
        <div class="ans-content">
          <p><strong>Problem Statement:</strong> If 5 workers can move 4,500 bricks in a day, how many workers are needed to move 18,000 bricks in a day?</p>
          <div class="ans-step">
            <div class="ans-step-title">Step 1: Identifying Given Data &amp; Variables</div>
            <p>• Initial state: <code>b₁ = 4,500 bricks</code>, <code>w₁ = 5 workers</code>.<br>
            • Target state: <code>b₂ = 18,000 bricks</code>, <code>w₂ = x workers</code>.<br>
            • Time duration is fixed at 1 day.</p>
          </div>
          <div class="ans-step">
            <div class="ans-step-title">Step 2: Determining Nature of Variation</div>
            <p>Direct proportion. More bricks to move in the same timeframe requires more workers at the identical rate: <code>w₁ / b₁ = w₂ / b₂</code>.</p>
          </div>
          <div class="ans-step">
            <div class="ans-step-title">Step 3: Setting Up Proportion Equation</div>
            <p><code>4,500 : 18,000 :: 5 : x</code><br>
            By the Rule of Three: <code>x = (18,000 × 5) / 4,500</code>.</p>
          </div>
          <div class="ans-step">
            <div class="ans-step-title">Step 4: Step-by-Step Calculation</div>
            <p>• Scaling factor = <code>18,000 ÷ 4,500 = 4</code> (4 times more bricks).<br>
            • <code>x = 5 × 4 = 20 workers</code>.</p>
          </div>
          <div class="ans-step">
            <div class="ans-step-title">Step 5: Final Statement &amp; Real-World Sense Check</div>
            <p><strong>Conclusion:</strong> Exactly <strong>20 workers</strong> are needed to move 18,000 bricks in one day.</p>
          </div>
        </div>
      </details>

      <!-- 21. In-Text Page 63-64 Example 2: Lucknow to Kanpur speed-time table -->
      <details class="ans-box">
        <summary>
          <span><span class="step-pill">In-Text Pg 63-64 Ex 2</span> Lucknow to Kanpur Travel: Verification of Inverse Variation</span>
        </summary>
        <div class="ans-content">
          <p><strong>Problem Statement:</strong> Puneeth's father went from Lucknow to Kanpur in 3 hours by motorcycle at 30 km/h. If he takes a car at 60 km/h, how long will it take? Can we represent this as <code>30 : 60 :: 3 : x</code>? Explain the speed-time table.</p>
          <div class="ans-step">
            <div class="ans-step-title">Step 1: Identifying Given Data &amp; Variables</div>
            <p>• Motorcycle: <code>Speed s₁ = 30 km/h</code>, <code>Time t₁ = 3 hours</code>.<br>
            • Car: <code>Speed s₂ = 60 km/h</code>, <code>Time t₂ = x hours</code>.<br>
            • Distance between cities is fixed (<code>d = 30 × 3 = 90 km</code>).</p>
          </div>
          <div class="ans-step">
            <div class="ans-step-title">Step 2: Determining Nature of Variation &amp; Conceptual Trap</div>
            <p><strong>CRITICAL TRAP:</strong> We <em>CANNOT</em> write <code>30 : 60 :: 3 : x</code>! That direct proportion would imply <code>x = 6 hours</code> (faster car taking MORE time!).<br>
            Because higher speed decreases travel time, Speed and Time vary <strong>inversely</strong>: <code>s₁ · t₁ = s₂ · t₂</code>.</p>
          </div>
          <div class="ans-step">
            <div class="ans-step-title">Step 3: Setting Up Inverse Proportion Equation</div>
            <p><code>30 × 3 = 60 × x</code><br>
            <code>90 = 60x ⇒ x = 90 ÷ 60</code>.</p>
          </div>
          <div class="ans-step">
            <div class="ans-step-title">Step 4: Step-by-Step Calculation</div>
            <p>• <code>x = 90 / 60 = 3 / 2 = 1.5 hours</code> (1 hour 30 minutes).<br>
            • Factor check: Speed doubled (30 → 60, ×2), so time halved (3 → 1.5, ×0.5)!</p>
          </div>
          <div class="ans-step">
            <div class="ans-step-title">Step 5: Final Statement &amp; Real-World Sense Check</div>
            <p><strong>Conclusion:</strong> It will take <strong>1.5 hours (1 hour 30 minutes)</strong> to reach Kanpur by car. Inverse proportion correctly models that doubling speed halves travel time.</p>
          </div>
        </div>
      </details>

      <!-- 22. Figure It Out Page 65 Q1: Check inverse proportion tables -->
      <details class="ans-box">
        <summary>
          <span><span class="step-pill">Fig It Out Pg 65 Q1</span> Testing Inverse Proportion in Three Data Tables (Product Invariance Test)</span>
        </summary>
        <div class="ans-content">
          <p><strong>Problem Statement:</strong> Which of the following data tables represent inverse proportion?<br>
          (i) x: 40, 80, 25, 16; y: 20, 10, 32, 50<br>
          (ii) x: 40, 80, 25, 16; y: 20, 10, 12.5, 8<br>
          (iii) x: 30, 90, 150, 10; y: 15, 5, 3, 45</p>
          <div class="ans-step">
            <div class="ans-step-title">Step 1: Identifying Governing Law</div>
            <p>Two quantities <em>x</em> and <em>y</em> are in inverse proportion if and only if their product <code>x · y = k</code> remains identical for all data pairs in the table.</p>
          </div>
          <div class="ans-step">
            <div class="ans-step-title">Step 2: Testing Table (i)</div>
            <p>• <code>40 × 20 = 800</code><br>
            • <code>80 × 10 = 800</code><br>
            • <code>25 × 32 = 800</code><br>
            • <code>16 × 50 = 800</code><br>
            All products equal <strong>800</strong>. Hence, Table (i) <strong>IS in inverse proportion</strong>.</p>
          </div>
          <div class="ans-step">
            <div class="ans-step-title">Step 3: Testing Table (ii)</div>
            <p>• <code>40 × 20 = 800</code><br>
            • <code>80 × 10 = 800</code><br>
            • <code>25 × 12.5 = 312.5 ≠ 800</code><br>
            • <code>16 × 8 = 128 ≠ 800</code><br>
            The products are not constant. Hence, Table (ii) <strong>is NOT in inverse proportion</strong>.</p>
          </div>
          <div class="ans-step">
            <div class="ans-step-title">Step 4: Testing Table (iii)</div>
            <p>• <code>30 × 15 = 450</code><br>
            • <code>90 × 5 = 450</code><br>
            • <code>150 × 3 = 450</code><br>
            • <code>10 × 45 = 450</code><br>
            All products equal <strong>450</strong>. Hence, Table (iii) <strong>IS in inverse proportion</strong>.</p>
          </div>
          <div class="ans-step">
            <div class="ans-step-title">Step 5: Final Statement &amp; Real-World Sense Check</div>
            <p><strong>Conclusion:</strong> <strong>Tables (i) and (iii)</strong> are in inverse proportion (with constants k = 800 and k = 450 respectively), while Table (ii) is not.</p>
          </div>
        </div>
      </details>

      <!-- 23. Figure It Out Page 65 Q2: Fill empty cells in table -->
      <details class="ans-box">
        <summary>
          <span><span class="step-pill">Fig It Out Pg 65 Q2</span> Completing Missing Cells in Inverse Proportion Table (k = 144)</span>
        </summary>
        <div class="ans-content">
          <p><strong>Problem Statement:</strong> Fill in the empty cells if <em>x</em> and <em>y</em> are in inverse proportion:<br>
          Col 1: (x = 16, y = 9) &nbsp;|&nbsp; Col 2: (x = 12, y = ?) &nbsp;|&nbsp; Col 3: (x = ?, y = 48) &nbsp;|&nbsp; Col 4: (x = 36, y = ?)</p>
          <div class="ans-step">
            <div class="ans-step-title">Step 1: Identifying Constant of Variation (k)</div>
            <p>From the complete first column: <code>x₁ = 16</code> and <code>y₁ = 9</code>.<br>
            Since <em>x</em> and <em>y</em> vary inversely: <code>k = x · y = 16 × 9 = 144</code>.</p>
          </div>
          <div class="ans-step">
            <div class="ans-step-title">Step 2: Formula Setup for Unknown Cells</div>
            <p>Every column must satisfy <code>x · y = 144</code>:<br>
            • To find <em>y</em>: <code>y = 144 ÷ x</code><br>
            • To find <em>x</em>: <code>x = 144 ÷ y</code>.</p>
          </div>
          <div class="ans-step">
            <div class="ans-step-title">Step 3: Calculating Column 2 (x = 12)</div>
            <p>• <code>y₂ = 144 ÷ 12 = 12</code>.</p>
          </div>
          <div class="ans-step">
            <div class="ans-step-title">Step 4: Calculating Column 3 (y = 48) &amp; Column 4 (x = 36)</div>
            <p>• Col 3: <code>x₃ = 144 ÷ 48 = 3</code>.<br>
            • Col 4: <code>y₄ = 144 ÷ 36 = 4</code>.</p>
          </div>
          <div class="ans-step">
            <div class="ans-step-title">Step 5: Final Statement &amp; Completed Table</div>
            <p><strong>Completed Table:</strong></p>
            <table class="data-table" style="max-width: 450px;">
              <tr><th>x</th><td>16</td><td><strong>12</strong></td><td><strong>3</strong></td><td>36</td></tr>
              <tr><th>y</th><td>9</td><td><strong>12</strong></td><td>48</td><td><strong>4</strong></td></tr>
            </table>
          </div>
        </div>
      </details>

      <!-- 24. Example 3 Page 65: 20 workers take 4 days road -->
      <details class="ans-box">
        <summary>
          <span><span class="step-pill">Example 3 Pg 65</span> Road Construction Worker-Days (20 Workers in 4 Days vs. 10 Workers)</span>
        </summary>
        <div class="ans-content">
          <p><strong>Problem Statement:</strong> 20 workers take 4 days to complete laying a road. How many days will 10 workers take to complete laying the same length of road?</p>
          <div class="ans-step">
            <div class="ans-step-title">Step 1: Identifying Given Data &amp; Variables</div>
            <p>• <code>w₁ = 20 workers</code>, <code>d₁ = 4 days</code>.<br>
            • <code>w₂ = 10 workers</code>, <code>d₂ = y₂ days</code>.<br>
            • Road length and work efficiency remain constant.</p>
          </div>
          <div class="ans-step">
            <div class="ans-step-title">Step 2: Determining Nature of Variation</div>
            <p>Inverse proportion. Fewer workers take more days to complete the exact same quantum of physical work: <code>w₁ · d₁ = w₂ · d₂</code>.</p>
          </div>
          <div class="ans-step">
            <div class="ans-step-title">Step 3: Setting Up Equation</div>
            <p><code>20 × 4 = 10 × d₂</code><br>
            <code>80 = 10d₂ ⇒ d₂ = 80 ÷ 10</code>.</p>
          </div>
          <div class="ans-step">
            <div class="ans-step-title">Step 4: Step-by-Step Calculation</div>
            <p>• <code>d₂ = 8 days</code>.<br>
            • Notice: Number of workers halved (20 ÷ 2 = 10), so the required days doubled (4 × 2 = 8)!</p>
          </div>
          <div class="ans-step">
            <div class="ans-step-title">Step 5: Final Statement &amp; Real-World Sense Check</div>
            <p><strong>Conclusion:</strong> It will take <strong>8 days</strong> for 10 workers to complete laying the road.</p>
          </div>
        </div>
      </details>

      <!-- 25. Example 4 Page 66: 2 pumps fill tank in 18 hours -->
      <details class="ans-box">
        <summary>
          <span><span class="step-pill">Example 4 Pg 66</span> Adding 2 More Pumps: Water Tank Inflow Capacity</span>
        </summary>
        <div class="ans-content">
          <p><strong>Problem Statement:</strong> 2 pumps can fill a tank in 18 hours. How much time will it take to fill the tank if we add 2 more pumps of the same kind?</p>
          <div class="ans-step">
            <div class="ans-step-title">Step 1: Identifying Given Data &amp; Variables</div>
            <p>• Initial pumps: <code>p₁ = 2 pumps</code>, <code>t₁ = 18 hours</code>.<br>
            • Additional pumps added = 2.<br>
            • New total pumps: <code>p₂ = 2 + 2 = 4 pumps</code>.<br>
            • Unknown: Time <code>t₂ = x hours</code>.</p>
          </div>
          <div class="ans-step">
            <div class="ans-step-title">Step 2: Determining Nature of Variation</div>
            <p>Inverse proportion. More pumps pumping simultaneously will fill the identical tank capacity in fewer hours: <code>p₁ · t₁ = p₂ · t₂</code>.</p>
          </div>
          <div class="ans-step">
            <div class="ans-step-title">Step 3: Setting Up Equation</div>
            <p><code>2 × 18 = 4 × x</code><br>
            <code>36 = 4x ⇒ x = 36 ÷ 4</code>.</p>
          </div>
          <div class="ans-step">
            <div class="ans-step-title">Step 4: Step-by-Step Calculation</div>
            <p>• <code>x = 9 hours</code>.<br>
            • Pump count doubled (2 → 4), so filling time halved (18 → 9)!</p>
          </div>
          <div class="ans-step">
            <div class="ans-step-title">Step 5: Final Statement &amp; Real-World Sense Check</div>
            <p><strong>Conclusion:</strong> It will take <strong>9 hours</strong> to fill the tank with 4 pumps.</p>
          </div>
        </div>
      </details>

      <!-- 26. Example 5 Page 66: 80 students food for 15 days -->
      <details class="ans-box">
        <summary>
          <span><span class="step-pill">Example 5 Pg 66</span> Hostel Ration Consumption (80 Students for 15 Days + 20 New Students)</span>
        </summary>
        <div class="ans-content">
          <p><strong>Problem Statement:</strong> A school has food provisions to feed 80 students for 15 days. If 20 more students join the school, for how many days will the provisions last?</p>
          <div class="ans-step">
            <div class="ans-step-title">Step 1: Identifying Given Data &amp; Variables</div>
            <p>• Initial students: <code>s₁ = 80</code>, <code>d₁ = 15 days</code>.<br>
            • New students joining = <code>20</code>.<br>
            • Total new student count: <code>s₂ = 80 + 20 = 100 students</code>.<br>
            • Unknown: New duration <code>d₂ = x days</code>.</p>
          </div>
          <div class="ans-step">
            <div class="ans-step-title">Step 2: Determining Nature of Variation</div>
            <p>Inverse proportion. More students eating from a fixed stock of grain causes provisions to be exhausted in fewer days: <code>s₁ · d₁ = s₂ · d₂</code>.</p>
          </div>
          <div class="ans-step">
            <div class="ans-step-title">Step 3: Setting Up Equation</div>
            <p><code>80 × 15 = 100 × x</code><br>
            <code>1200 = 100x ⇒ x = 1200 ÷ 100</code>.</p>
          </div>
          <div class="ans-step">
            <div class="ans-step-title">Step 4: Step-by-Step Calculation</div>
            <p>• <code>x = 12 days</code>.</p>
          </div>
          <div class="ans-step">
            <div class="ans-step-title">Step 5: Final Statement &amp; Real-World Sense Check</div>
            <p><strong>Conclusion:</strong> The food provisions will last for <strong>12 days</strong>.<br>
            <em>Assumption:</em> Every student consumes food at the identical daily rate.</p>
          </div>
        </div>
      </details>

      <!-- 27. Example 6 Page 66-67: Ram & Shyam cutting vegetables -->
      <details class="ans-box">
        <summary>
          <span><span class="step-pill">Example 6 Pg 66-67</span> Combined Collaborative Work: Ram &amp; Shyam Cutting Vegetables</span>
        </summary>
        <div class="ans-content">
          <p><strong>Problem Statement:</strong> If Ram takes 1 hour to cut a given quantity of vegetables and Shyam takes 1.5 hours to cut the same quantity of vegetables, how much time will they take to cut the vegetables if they do it together?</p>
          <div class="ans-step">
            <div class="ans-step-title">Step 1: Identifying Given Data &amp; Work Concept</div>
            <p>• Total task = <code>1 unit of work</code>.<br>
            • Ram's solo time = <code>1 hour</code>.<br>
            • Shyam's solo time = <code>1.5 hours = 3/2 hours</code>.<br>
            • Time cannot be averaged! Rates must be added.</p>
          </div>
          <div class="ans-step">
            <div class="ans-step-title">Step 2: Determining 1-Hour Work Rate for Each</div>
            <p>• Ram's 1-hour work = <code>1 ÷ 1 = 1 unit</code>.<br>
            • Shyam's 1-hour work = <code>1 ÷ (3/2) = 2/3 unit</code>.</p>
          </div>
          <div class="ans-step">
            <div class="ans-step-title">Step 3: Calculating Combined 1-Hour Work Rate</div>
            <p><code>Combined 1-Hour Rate = 1 + 2/3 = 5/3 units of work</code>.</p>
          </div>
          <div class="ans-step">
            <div class="ans-step-title">Step 4: Applying Direct Proportion for 1 Unit</div>
            <p>To do <code>5/3 units</code> takes 1 hour.<br>
            Therefore, to do <code>1 unit</code> takes: <code>1 ÷ (5/3) = 3/5 hour</code>.<br>
            Convert to minutes: <code>(3/5) × 60 = 36 minutes</code>.</p>
          </div>
          <div class="ans-step">
            <div class="ans-step-title">Step 5: Final Statement &amp; Real-World Sense Check</div>
            <p><strong>Conclusion:</strong> Working together, Ram and Shyam will finish cutting the vegetables in <strong>3/5 of an hour (36 minutes)</strong>.<br>
            <em>Sense check:</em> Since Ram alone takes 60 min, having Shyam help must make it finish in less than 60 min. 36 min is completely reasonable!</p>
          </div>
        </div>
      </details>

      <!-- 28. Figure It Out Page 67-68 Q1: Direct vs Inverse Classification -->
      <details class="ans-box">
        <summary>
          <span><span class="step-pill">Fig It Out Pg 67 Q1</span> Direct vs. Inverse Proportion Classification (6 Physical Scenarios)</span>
        </summary>
        <div class="ans-content">
          <p><strong>Problem Statement:</strong> Which of the following pairs of quantities are in inverse proportion?<br>
          (i) The number of taps filling a water tank and the time taken to fill it.<br>
          (ii) The number of painters hired and the days needed to paint a wall of fixed size.<br>
          (iii) The distance a car can travel and the amount of petrol in the tank.<br>
          (iv) The speed of a cyclist and the time taken to cover a fixed route.<br>
          (v) The length of cloth bought and the price paid at a fixed rate per metre.<br>
          (vi) The number of pages in a book and the time required to read it at a fixed reading speed.</p>
          <div class="ans-step">
            <div class="ans-step-title">Step 1: Classification Criteria</div>
            <p>• If Quantity A ↑ causes Quantity B ↓ proportionally ⇒ <strong>Inverse Proportion</strong>.<br>
            • If Quantity A ↑ causes Quantity B ↑ proportionally ⇒ <strong>Direct Proportion</strong>.</p>
          </div>
          <div class="ans-step">
            <div class="ans-step-title">Step 2: Evaluating Scenarios (i) &amp; (ii)</div>
            <p>• (i) <strong>Inverse Proportion:</strong> More taps running simultaneously deliver water faster, reducing the time needed.<br>
            • (ii) <strong>Inverse Proportion:</strong> More painters working simultaneously complete the fixed surface in fewer days.</p>
          </div>
          <div class="ans-step">
            <div class="ans-step-title">Step 3: Evaluating Scenarios (iii) &amp; (iv)</div>
            <p>• (iii) <strong>Direct Proportion (NOT inverse):</strong> More petrol in the fuel tank enables the car to travel a greater distance.<br>
            • (iv) <strong>Inverse Proportion:</strong> A cyclist travelling at higher speed covers the fixed route in less time.</p>
          </div>
          <div class="ans-step">
            <div class="ans-step-title">Step 4: Evaluating Scenarios (v) &amp; (vi)</div>
            <p>• (v) <strong>Direct Proportion (NOT inverse):</strong> Buying more metres of cloth costs more money.<br>
            • (vi) <strong>Direct Proportion (NOT inverse):</strong> Reading a thicker book with more pages requires more reading time.</p>
          </div>
          <div class="ans-step">
            <div class="ans-step-title">Step 5: Final Summary Statement</div>
            <p><strong>Conclusion:</strong> The pairs in <strong>Inverse Proportion</strong> are <strong>(i), (ii), and (iv)</strong>.<br>
            The pairs in Direct Proportion are (iii), (v), and (vi).</p>
          </div>
        </div>
      </details>

      <!-- 29. Figure It Out Page 67-68 Q2: 24 pencils cost 120 -->
      <details class="ans-box">
        <summary>
          <span><span class="step-pill">Fig It Out Pg 67 Q2</span> Commercial Direct Variation: 24 Pencils Cost ₹120</span>
        </summary>
        <div class="ans-content">
          <p><strong>Problem Statement:</strong> If 24 pencils cost ₹120, how much will 20 such pencils cost?</p>
          <div class="ans-step">
            <div class="ans-step-title">Step 1: Identifying Given Data &amp; Variables</div>
            <p>• <code>p₁ = 24 pencils</code>, <code>c₁ = ₹120</code>.<br>
            • <code>p₂ = 20 pencils</code>, <code>c₂ = x</code>.</p>
          </div>
          <div class="ans-step">
            <div class="ans-step-title">Step 2: Determining Nature of Variation</div>
            <p>Direct proportion. Fewer pencils purchased cost less money at a fixed unit rate: <code>c₁ / p₁ = c₂ / p₂</code>.</p>
          </div>
          <div class="ans-step">
            <div class="ans-step-title">Step 3: Unitary Method Setup</div>
            <p>• Cost of 1 pencil = <code>Total Cost ÷ Total Pencils = 120 ÷ 24 = ₹5 per pencil</code>.</p>
          </div>
          <div class="ans-step">
            <div class="ans-step-title">Step 4: Step-by-Step Calculation</div>
            <p>• Cost of 20 pencils = <code>20 × ₹5 = ₹100</code>.</p>
          </div>
          <div class="ans-step">
            <div class="ans-step-title">Step 5: Final Statement &amp; Real-World Sense Check</div>
            <p><strong>Conclusion:</strong> 20 pencils will cost <strong>₹100</strong>.</p>
          </div>
        </div>
      </details>

      <!-- 30. Figure It Out Page 67-68 Q3: Water tank 20 families 6 days -->
      <details class="ans-box">
        <summary>
          <span><span class="step-pill">Fig It Out Pg 67 Q3</span> Water Tank Supply (20 Families for 6 Days + 10 Families) &amp; Assumptions</span>
        </summary>
        <div class="ans-content">
          <p><strong>Problem Statement:</strong> A tank on a building has enough water to supply 20 families living there for 6 days. If 10 more families move in there, how long will the water last? What assumptions do you need to make to work out this problem?</p>
          <div class="ans-step">
            <div class="ans-step-title">Step 1: Identifying Given Data &amp; Variables</div>
            <p>• Initial families: <code>f₁ = 20</code>, <code>d₁ = 6 days</code>.<br>
            • Additional families = 10.<br>
            • New family count: <code>f₂ = 20 + 10 = 30 families</code>.<br>
            • Unknown: Duration <code>d₂ = x days</code>.</p>
          </div>
          <div class="ans-step">
            <div class="ans-step-title">Step 2: Determining Nature of Variation</div>
            <p>Inverse proportion. More families drawing from a fixed storage reservoir causes water to run out in fewer days: <code>f₁ · d₁ = f₂ · d₂</code>.</p>
          </div>
          <div class="ans-step">
            <div class="ans-step-title">Step 3: Setting Up Equation</div>
            <p><code>20 × 6 = 30 × x</code><br>
            <code>120 = 30x ⇒ x = 120 ÷ 30</code>.</p>
          </div>
          <div class="ans-step">
            <div class="ans-step-title">Step 4: Step-by-Step Calculation</div>
            <p>• <code>x = 4 days</code>.</p>
          </div>
          <div class="ans-step">
            <div class="ans-step-title">Step 5: Final Statement &amp; Mandatory Assumptions</div>
            <p><strong>Conclusion:</strong> The water will last for <strong>4 days</strong>.<br>
            <strong>Mandatory Real-World Assumptions:</strong><br>
            1. Every family consumes the exact same volume of water per day.<br>
            2. No additional water is pumped into the tank during these 4 days.<br>
            3. There are zero leaks, spills, or evaporation losses from the storage tank.</p>
          </div>
        </div>
      </details>

      <!-- 31. Figure It Out Page 67-68 Q4: Sleep hours of 8 living beings -->
      <details class="ans-box">
        <summary>
          <span><span class="step-pill">Fig It Out Pg 67 Q4</span> Decoding 24-Hour Sleep Clocks for 8 Living Beings</span>
        </summary>
        <div class="ans-content">
          <p><strong>Problem Statement:</strong> Fill in the average number of hours each living being sleeps in a day by looking at the charts on page 67. Select the appropriate hours from this list: <code>15, 2.5, 20, 8, 3.5, 13, 10.5, 18</code>.</p>
          <div class="ans-step">
            <div class="ans-step-title">Step 1: Identifying Governing Mathematical Relationship</div>
            <p>A full circular clock represents <strong>24 hours</strong> (= 360°).<br>
            • Each 1 hour of sleep = <code>360° ÷ 24 = 15° of central sector angle</code>.<br>
            • <strong>Blue sector = Sleep hours</strong>; <strong>Yellow sector = Awake hours</strong>.<br>
            • We sort both the 8 given numbers and the 8 visual sleep sectors in ascending order.</p>
          </div>
          <div class="ans-step">
            <div class="ans-step-title">Step 2: Ascending Mathematical List of Sleep Hours</div>
            <p><code>2.5 &lt; 3.5 &lt; 8.0 &lt; 10.5 &lt; 13.0 &lt; 15.0 &lt; 18.0 &lt; 20.0</code></p>
          </div>
          <div class="ans-step">
            <div class="ans-step-title">Step 3: Matching Top Row (Animals 1 to 4)</div>
            <p>1. <strong>Giraffe:</strong> Smallest sliver of blue (approx 37.5°) ⇒ <strong>2.5 hours</strong>.<br>
            2. <strong>Elephant:</strong> Slightly larger blue sector (approx 52.5°) ⇒ <strong>3.5 hours</strong>.<br>
            3. <strong>Human Child:</strong> Exactly 1/3 of the circle (120° angle) ⇒ <code>24 × (1/3) =</code> <strong>8 hours</strong>.<br>
            4. <strong>Dog:</strong> Blue sector nearly half the circle (approx 157.5°) ⇒ <strong>10.5 hours</strong>.</p>
          </div>
          <div class="ans-step">
            <div class="ans-step-title">Step 4: Matching Bottom Row (Animals 5 to 8)</div>
            <p>5. <strong>Cat:</strong> Blue sector slightly over half (195° angle) ⇒ <strong>13 hours</strong>.<br>
            6. <strong>Squirrel:</strong> Blue sector is 5/8 of circle (225° angle) ⇒ <strong>15 hours</strong>.<br>
            7. <strong>Python (Snake):</strong> Exactly 3/4 of circle (270° angle) ⇒ <code>24 × (3/4) =</code> <strong>18 hours</strong>.<br>
            8. <strong>Bat:</strong> Dominant blue sector, 5/6 of circle (300° angle) ⇒ <code>24 × (5/6) =</code> <strong>20 hours</strong>.</p>
          </div>
          <div class="ans-step">
            <div class="ans-step-title">Step 5: Final Statement Summary Table</div>
            <p><strong>Final Solution:</strong> Giraffe = 2.5 h | Elephant = 3.5 h | Human = 8 h | Dog = 10.5 h | Cat = 13 h | Squirrel = 15 h | Python = 18 h | Bat = 20 h.</p>
          </div>
        </div>
      </details>

      <!-- 32. Figure It Out Page 67-68 Q5: School transport pie chart -->
      <details class="ans-box">
        <summary>
          <span><span class="step-pill">Fig It Out Pg 68 Q5</span> School Transport Survey Pie Chart Analysis (All 4 Sub-Questions)</span>
        </summary>
        <div class="ans-content">
          <p><strong>Problem Statement:</strong> The pie chart shows the modes of transport used by children: Walk = 90°, Cycle = 60°, Bus = 120°, Two-wheeler = 60°, Car = (remaining angle).<br>
          (i) What is the most common mode of transport?<br>
          (ii) What fraction of children travel by car?<br>
          (iii) If 18 children travel by car, how many children took part in the survey? How many children use taxis to travel to school?<br>
          (iv) By which two modes of transport are equal numbers of children travelling?</p>
          <div class="ans-step">
            <div class="ans-step-title">Step 1: Calculating the Car Central Angle</div>
            <p>• Total circle = <code>360°</code>.<br>
            • Sum of given sectors = <code>Walk (90°) + Bus (120°) + Two-wheeler (60°) + Cycle (60°) = 330°</code>.<br>
            • <code>Car Sector Angle = 360° - 330° = 30°</code>.</p>
          </div>
          <div class="ans-step">
            <div class="ans-step-title">Step 2: Sub-question (i) - Most Common Mode</div>
            <p>The largest sector angle corresponds to the most common mode: <strong>Bus (120°)</strong> subtends the greatest angle (1/3 of all students).</p>
          </div>
          <div class="ans-step">
            <div class="ans-step-title">Step 3: Sub-question (ii) - Fraction by Car</div>
            <p><code>Fraction by Car = Car Angle / 360° = 30° / 360° = 1 / 12</code>.</p>
          </div>
          <div class="ans-step">
            <div class="ans-step-title">Step 4: Sub-question (iii) - Total Students &amp; Taxis</div>
            <p>• If <code>1/12 of Total = 18 students</code>:<br>
            <code>Total Students = 18 × 12 = 216 students</code>.<br>
            • <strong>Taxis:</strong> Taxis are not present on the survey pie chart (Angle = 0°). Therefore, <strong>0 children</strong> use taxis.</p>
          </div>
          <div class="ans-step">
            <div class="ans-step-title">Step 5: Sub-question (iv) - Equal Modes &amp; Final Statement</div>
            <p><strong>Conclusion:</strong><br>
            (i) <strong>Bus</strong> is the most common mode of transport.<br>
            (ii) <strong>1/12</strong> of the children travel by car.<br>
            (iii) Total children surveyed = <strong>216 children</strong>; Children using taxis = <strong>0</strong>.<br>
            (iv) <strong>Cycle and Two-wheeler</strong> have equal numbers of children (both subtend exactly <strong>60°</strong>, representing <code>216 × (60/360) = 36 students</code> each).</p>
          </div>
        </div>
      </details>

      <!-- 33. Figure It Out Page 67-68 Q6: 3 workers paint fence in 4 days -->
      <details class="ans-box">
        <summary>
          <span><span class="step-pill">Fig It Out Pg 68 Q6</span> Fence Painting Rate (3 Workers in 4 Days + 1 Worker) &amp; Assumptions</span>
        </summary>
        <div class="ans-content">
          <p><strong>Problem Statement:</strong> Three workers can paint a fence in 4 days. If one more worker joins the team, how many days will it take them to finish the work? What are the assumptions you need to make?</p>
          <div class="ans-step">
            <div class="ans-step-title">Step 1: Identifying Given Data &amp; Variables</div>
            <p>• Initial team: <code>w₁ = 3 workers</code>, <code>d₁ = 4 days</code>.<br>
            • Additional worker joining = 1.<br>
            • New team size: <code>w₂ = 3 + 1 = 4 workers</code>.<br>
            • Unknown: New duration <code>d₂ = x days</code>.</p>
          </div>
          <div class="ans-step">
            <div class="ans-step-title">Step 2: Determining Nature of Variation</div>
            <p>Inverse proportion. More workers painting a fixed fence length reduce the required painting days: <code>w₁ · d₁ = w₂ · d₂</code>.</p>
          </div>
          <div class="ans-step">
            <div class="ans-step-title">Step 3: Setting Up Equation</div>
            <p><code>3 × 4 = 4 × x</code><br>
            <code>12 = 4x ⇒ x = 12 ÷ 4</code>.</p>
          </div>
          <div class="ans-step">
            <div class="ans-step-title">Step 4: Step-by-Step Calculation</div>
            <p>• <code>x = 3 days</code>.</p>
          </div>
          <div class="ans-step">
            <div class="ans-step-title">Step 5: Final Statement &amp; Assumptions</div>
            <p><strong>Conclusion:</strong> It will take <strong>3 days</strong> for the 4 workers to finish painting the fence.<br>
            <strong>Assumptions:</strong> All workers work at the identical daily rate and efficiency, and working together does not create spatial hindrance.</p>
          </div>
        </div>
      </details>

      <!-- 34. Figure It Out Page 67-68 Q7: 6 hours to fill 2 tanks with pump -->
      <details class="ans-box">
        <summary>
          <span><span class="step-pill">Fig It Out Pg 68 Q7</span> Pump Capacity: Filling Multiple Water Tanks (Direct Proportion)</span>
        </summary>
        <div class="ans-content">
          <p><strong>Problem Statement:</strong> It takes 6 hours to fill 2 tanks of the same size with a pump. How long will it take to fill 5 such tanks with the same pump?</p>
          <div class="ans-step">
            <div class="ans-step-title">Step 1: Identifying Given Data &amp; Variables</div>
            <p>• <code>Tanks n₁ = 2</code>, <code>Time t₁ = 6 hours</code>.<br>
            • <code>Tanks n₂ = 5</code>, <code>Time t₂ = x hours</code>.<br>
            • Single pump of uniform pumping rate.</p>
          </div>
          <div class="ans-step">
            <div class="ans-step-title">Step 2: Determining Nature of Variation (CRITICAL TRAP!)</div>
            <p><strong>Caution:</strong> Unlike previous pump problems, here the <em>number of pumps is constant (1 pump)</em> while the <em>volume of water / number of tanks increases</em>!<br>
            More tanks require MORE time. This is <strong>DIRECT PROPORTION</strong>: <code>t₁ / n₁ = t₂ / n₂</code>.</p>
          </div>
          <div class="ans-step">
            <div class="ans-step-title">Step 3: Unitary Method Setup</div>
            <p>• Time to fill 1 tank = <code>6 hours ÷ 2 tanks = 3 hours per tank</code>.</p>
          </div>
          <div class="ans-step">
            <div class="ans-step-title">Step 4: Step-by-Step Calculation</div>
            <p>• Time to fill 5 tanks = <code>5 tanks × 3 hours/tank = 15 hours</code>.</p>
          </div>
          <div class="ans-step">
            <div class="ans-step-title">Step 5: Final Statement &amp; Real-World Sense Check</div>
            <p><strong>Conclusion:</strong> It will take <strong>15 hours</strong> to fill 5 such tanks with the same pump.</p>
          </div>
        </div>
      </details>

      <!-- 35. Figure It Out Page 67-68 Q8: Chairs arranged in 25 rows with 12 chairs -->
      <details class="ans-box">
        <summary>
          <span><span class="step-pill">Fig It Out Pg 68 Q8</span> Seating Arrangement: Rows vs. Chairs Per Row (Constant Total Chairs)</span>
        </summary>
        <div class="ans-content">
          <p><strong>Problem Statement:</strong> A given set of chairs are arranged in 25 rows, with 12 chairs in each row. If the chairs are rearranged with 20 chairs in each row, how many rows does this new arrangement have?</p>
          <div class="ans-step">
            <div class="ans-step-title">Step 1: Identifying Given Data &amp; Variables</div>
            <p>• Arrangement 1: <code>r₁ = 25 rows</code>, <code>c₁ = 12 chairs/row</code>.<br>
            • Arrangement 2: <code>c₂ = 20 chairs/row</code>, <code>r₂ = x rows</code>.<br>
            • Total number of chairs is constant.</p>
          </div>
          <div class="ans-step">
            <div class="ans-step-title">Step 2: Determining Nature of Variation</div>
            <p>Inverse proportion. Fitting more chairs into each row decreases the total number of rows needed: <code>r₁ · c₁ = r₂ · c₂</code>.</p>
          </div>
          <div class="ans-step">
            <div class="ans-step-title">Step 3: Calculating Constant Total Chairs</div>
            <p><code>Total Chairs = 25 × 12 = 300 chairs</code>.</p>
          </div>
          <div class="ans-step">
            <div class="ans-step-title">Step 4: Step-by-Step Calculation</div>
            <p><code>20 × x = 300 ⇒ x = 300 ÷ 20 = 15 rows</code>.</p>
          </div>
          <div class="ans-step">
            <div class="ans-step-title">Step 5: Final Statement &amp; Real-World Sense Check</div>
            <p><strong>Conclusion:</strong> The new seating arrangement will have <strong>15 rows</strong>.</p>
          </div>
        </div>
      </details>

      <!-- 36. Figure It Out Page 67-68 Q9: School periods 8 of 45 min to 9 periods -->
      <details class="ans-box">
        <summary>
          <span><span class="step-pill">Fig It Out Pg 68 Q9</span> School Timetable Revision: 8 Periods of 45 min vs. 9 Periods</span>
        </summary>
        <div class="ans-content">
          <p><strong>Problem Statement:</strong> A school has 8 periods a day, each of 45 minutes duration. How long is each period if the school has 9 periods a day, assuming that the total number of school hours per day stays the same?</p>
          <div class="ans-step">
            <div class="ans-step-title">Step 1: Identifying Given Data &amp; Variables</div>
            <p>• Initial timetable: <code>p₁ = 8 periods</code>, <code>t₁ = 45 minutes</code>.<br>
            • Proposed timetable: <code>p₂ = 9 periods</code>, <code>t₂ = x minutes</code>.<br>
            • Total instructional time remains strictly constant.</p>
          </div>
          <div class="ans-step">
            <div class="ans-step-title">Step 2: Determining Nature of Variation</div>
            <p>Inverse proportion. Adding more periods within the exact same daily school hours forces each period to be shorter: <code>p₁ · t₁ = p₂ · t₂</code>.</p>
          </div>
          <div class="ans-step">
            <div class="ans-step-title">Step 3: Calculating Total Daily Instructional Time</div>
            <p><code>Total Minutes = 8 periods × 45 min/period = 360 minutes (6 hours)</code>.</p>
          </div>
          <div class="ans-step">
            <div class="ans-step-title">Step 4: Step-by-Step Calculation</div>
            <p><code>9 × x = 360 ⇒ x = 360 ÷ 9 = 40 minutes</code>.</p>
          </div>
          <div class="ans-step">
            <div class="ans-step-title">Step 5: Final Statement &amp; Real-World Sense Check</div>
            <p><strong>Conclusion:</strong> Each period will be <strong>40 minutes long</strong> (a reduction of 5 minutes per period).</p>
          </div>
        </div>
      </details>

      <!-- 37. Figure It Out Page 67-68 Q10: Small pump (3 h) and large pump (2 h) -->
      <details class="ans-box">
        <summary>
          <span><span class="step-pill">Fig It Out Pg 68 Q10</span> Collaborative Inflow: Small Pump (3 h) &amp; Large Pump (2 h) Filling Together</span>
        </summary>
        <div class="ans-content">
          <p><strong>Problem Statement:</strong> A small pump can fill a tank in 3 hours, while a large pump can fill the same tank in 2 hours. If both pumps are used together, how long will the tank take to fill?</p>
          <div class="ans-step">
            <div class="ans-step-title">Step 1: Identifying Given Data &amp; Concepts</div>
            <p>• Small pump solo time = <code>3 hours</code>.<br>
            • Large pump solo time = <code>2 hours</code>.<br>
            • Both pumps operate simultaneously into the same tank.</p>
          </div>
          <div class="ans-step">
            <div class="ans-step-title">Step 2: Determining Hourly Inflow Rates</div>
            <p>• In 1 hour, small pump fills <code>1/3 of the tank</code>.<br>
            • In 1 hour, large pump fills <code>1/2 of the tank</code>.</p>
          </div>
          <div class="ans-step">
            <div class="ans-step-title">Step 3: Combining Inflow Rates</div>
            <p><code>Combined 1-Hour Inflow = 1/3 + 1/2 = 2/6 + 3/6 = 5/6 of the tank</code>.</p>
          </div>
          <div class="ans-step">
            <div class="ans-step-title">Step 4: Inverting Rate to Obtain Total Time</div>
            <p>• Time to fill 1 complete tank = <code>1 ÷ (5/6) = 6/5 hours</code>.<br>
            • Converting to hours and minutes: <code>6/5 hours = 1.2 hours = 1 hour + (0.2 × 60 min) = 1 hour 12 minutes</code>.</p>
          </div>
          <div class="ans-step">
            <div class="ans-step-title">Step 5: Final Statement &amp; Real-World Sense Check</div>
            <p><strong>Conclusion:</strong> Both pumps working together will fill the tank in <strong>6/5 hours (1 hour 12 minutes)</strong>.<br>
            <em>Sense check:</em> The large pump alone takes 2 hours; with the small pump helping, filling must take less than 2 hours. 1 hr 12 min is completely logical.</p>
          </div>
        </div>
      </details>

      <!-- 38. Figure It Out Page 67-68 Q11: 42 machines 63 days to 54 days -->
      <details class="ans-box">
        <summary>
          <span><span class="step-pill">Fig It Out Pg 68 Q11</span> Industrial Output: 42 Machines in 63 Days vs. Target of 54 Days</span>
        </summary>
        <div class="ans-content">
          <p><strong>Problem Statement:</strong> A factory requires 42 machines to produce a given number of toys in 63 days. How many machines are required to produce the same number of toys in 54 days?</p>
          <div class="ans-step">
            <div class="ans-step-title">Step 1: Identifying Given Data &amp; Variables</div>
            <p>• Initial state: <code>m₁ = 42 machines</code>, <code>d₁ = 63 days</code>.<br>
            • Target state: <code>d₂ = 54 days</code>, <code>m₂ = x machines</code>.<br>
            • Total toy production target is constant.</p>
          </div>
          <div class="ans-step">
            <div class="ans-step-title">Step 2: Determining Nature of Variation</div>
            <p>Inverse proportion. Producing the same volume of goods in fewer days requires more active machines: <code>m₁ · d₁ = m₂ · d₂</code>.</p>
          </div>
          <div class="ans-step">
            <div class="ans-step-title">Step 3: Setting Up Equation</div>
            <p><code>42 × 63 = x × 54</code><br>
            <code>x = (42 × 63) ÷ 54</code>.</p>
          </div>
          <div class="ans-step">
            <div class="ans-step-title">Step 4: Step-by-Step Simplification</div>
            <p>• Divide 63 and 54 by common factor 9: <code>63 ÷ 9 = 7</code>, <code>54 ÷ 9 = 6</code>.<br>
            • <code>x = (42 × 7) ÷ 6</code>.<br>
            • Divide 42 by 6: <code>42 ÷ 6 = 7</code>.<br>
            • <code>x = 7 × 7 = 49 machines</code>.</p>
          </div>
          <div class="ans-step">
            <div class="ans-step-title">Step 5: Final Statement &amp; Real-World Sense Check</div>
            <p><strong>Conclusion:</strong> Exactly <strong>49 machines</strong> are required to produce the toys in 54 days (an addition of 7 machines).</p>
          </div>
        </div>
      </details>

      <!-- 39. Figure It Out Page 67-68 Q12: Car at 60 km/h takes 2 hours to 80 km/h -->
      <details class="ans-box">
        <summary>
          <span><span class="step-pill">Fig It Out Pg 68 Q12</span> High-Speed Transit: Car at 60 km/h in 2 Hours Accelerated to 80 km/h</span>
        </summary>
        <div class="ans-content">
          <p><strong>Problem Statement:</strong> A car takes 2 hours to reach a destination travelling at a speed of 60 km/h. How long will the car take if it travels at a speed of 80 km/h?</p>
          <div class="ans-step">
            <div class="ans-step-title">Step 1: Identifying Given Data &amp; Variables</div>
            <p>• Initial trip: <code>s₁ = 60 km/h</code>, <code>t₁ = 2 hours</code>.<br>
            • Accelerated trip: <code>s₂ = 80 km/h</code>, <code>t₂ = x hours</code>.<br>
            • Destination distance is fixed.</p>
          </div>
          <div class="ans-step">
            <div class="ans-step-title">Step 2: Determining Nature of Variation</div>
            <p>Inverse proportion. As cruising speed increases, transit duration decreases: <code>s₁ · t₁ = s₂ · t₂</code>.</p>
          </div>
          <div class="ans-step">
            <div class="ans-step-title">Step 3: Calculating Constant Total Distance</div>
            <p><code>Distance = Speed × Time = 60 km/h × 2 hours = 120 km</code>.</p>
          </div>
          <div class="ans-step">
            <div class="ans-step-title">Step 4: Step-by-Step Calculation</div>
            <p><code>80 × x = 120 ⇒ x = 120 ÷ 80 = 12 / 8 = 3 / 2 = 1.5 hours</code>.<br>
            Convert to hours and minutes: <code>1.5 hours = 1 hour 30 minutes</code>.</p>
          </div>
          <div class="ans-step">
            <div class="ans-step-title">Step 5: Final Statement &amp; Real-World Sense Check</div>
            <p><strong>Conclusion:</strong> The car will take <strong>1.5 hours (1 hour 30 minutes)</strong> to reach the destination travelling at 80 km/h (saving 30 minutes of travel time).</p>
          </div>
        </div>
      </details>
    </section>
"""
