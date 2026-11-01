# -*- coding: utf-8 -*-
"""Part 6: Section 4 Part A - 100% Solved NCERT Questions (Questions 1 to 20: In-text, Activities, Figure it Out)."""

SECTION4A_CONTENT = """
    <!-- SECTION 4: 100% SOLVED NCERT QUESTIONS (PART A) -->
    <section id="ncert-solutions" class="section-card">
      <div class="section-header">
        <div class="section-icon-box">
          <i class="fa-solid fa-pencil"></i>
        </div>
        <div>
          <h2 class="section-title">Section 4: 100% Solved NCERT Questions &amp; Activities</h2>
          <p class="section-tagline">Every in-text prompt, classroom activity, Try These, and exercise in Ganita Prakash Chapter 5 solved with 5-step methodology</p>
        </div>
      </div>

      <!-- QUESTION 1: IN-TEXT PROMPT PAGE 107 -->
      <details class="ans-box" open>
        <summary class="ans-header">
          <div class="summary-left">
            <i class="fa-solid fa-chevron-right summary-icon"></i>
            <span>NCERT In-Text Prompt (Page 107): Can Two Straight Lines Intersect at More Than One Point?</span>
          </div>
          <span class="question-badge badge-intext">In-Text Exploration</span>
        </summary>
        <div class="ans-content">
          <div class="step-box step-1">
            <div class="step-header"><i class="fa-solid fa-bullseye"></i> Step 1: What is Given &amp; What to Find</div>
            <p><strong>Given:</strong> Two straight lines lying on the same flat plane.</p>
            <p><strong>To Determine:</strong> Whether it is geometrically possible for these two straight lines to intersect each other at more than one point.</p>
          </div>
          <div class="step-box step-2">
            <div class="step-header"><i class="fa-solid fa-lightbulb"></i> Step 2: Key Concept &amp; Euclidean Axiom</div>
            <p><strong>Euclid's First Axiom of Straight Lines:</strong> A straight line has a constant, unwavering direction throughout its entire length. It never curves, bends, or loops back. Through any two distinct points in a plane, there is one and only one unique straight line.</p>
          </div>
          <div class="step-box step-3">
            <div class="step-header"><i class="fa-solid fa-pen-to-square"></i> Step 3: Step-by-Step Logical Proof</div>
            <p>1. Suppose two straight lines <span class="math-inline">l</span> and <span class="math-inline">m</span> intersect at a point <span class="math-inline">P</span>.</p>
            <p>2. Once they pass point <span class="math-inline">P</span>, they diverge (move further apart) indefinitely because neither line can change its direction.</p>
            <p>3. If they were to meet again at a second distinct point <span class="math-inline">Q</span>, both point <span class="math-inline">P</span> and point <span class="math-inline">Q</span> would lie on line <span class="math-inline">l</span> and line <span class="math-inline">m</span>.</p>
            <p>4. But Euclid's axiom states that only one straight line can pass through two distinct points. Therefore, line <span class="math-inline">l</span> and line <span class="math-inline">m</span> must be the exact same coincident line!</p>
          </div>
          <div class="step-box step-4">
            <div class="step-header"><i class="fa-solid fa-magnifying-glass"></i> Step 4: Verification &amp; Cross-Check</div>
            <p>Try drawing two straight lines on a sheet of paper. As long as your ruler is straight, you cannot make them touch a second time without deliberately bending the pencil line.</p>
          </div>
          <div class="step-box step-5">
            <div class="step-header"><i class="fa-solid fa-flag-checkered"></i> Step 5: Final Answer Statement</div>
            <p><strong>Conclusion:</strong> <strong>No</strong>, two distinct straight lines cannot intersect at more than one point. They intersect at <strong>at most one point</strong>.</p>
          </div>
        </div>
      </details>

      <!-- QUESTION 2: ACTIVITY 1 PAGE 107 -->
      <details class="ans-box">
        <summary class="ans-header">
          <div class="summary-left">
            <i class="fa-solid fa-chevron-right summary-icon"></i>
            <span>Activity 1 (Page 107): Measuring Angles of Intersecting Lines &amp; Spotting Patterns</span>
          </div>
          <span class="question-badge badge-try">Classroom Activity</span>
        </summary>
        <div class="ans-content">
          <div class="step-box step-1">
            <div class="step-header"><i class="fa-solid fa-bullseye"></i> Step 1: What is Given &amp; What to Find</div>
            <p><strong>Task:</strong> Draw four pairs of intersecting lines on paper. Measure the four angles formed at each intersection point using a protractor, and identify all recurring patterns.</p>
          </div>
          <div class="step-box step-2">
            <div class="step-header"><i class="fa-solid fa-lightbulb"></i> Step 2: Key Concept &amp; Formula</div>
            <p>Around an intersection point <span class="math-inline">O</span>, four angles are formed: <span class="math-inline">∠a, ∠b, ∠c, ∠d</span>. Adjacent angles along a straight line form a linear pair (<span class="math-inline">Sum = 180°</span>), and vertically opposite angles face each other.</p>
          </div>
          <div class="step-box step-3">
            <div class="step-header"><i class="fa-solid fa-pen-to-square"></i> Step 3: Tabulation of Measured Angles Across 4 Trials</div>
            <p>Sample measurements from 4 distinct pairs of intersecting lines:</p>
            <div class="table-responsive">
              <table>
                <thead>
                  <tr>
                    <th>Trial</th>
                    <th>Angle ∠a</th>
                    <th>Angle ∠b</th>
                    <th>Angle ∠c</th>
                    <th>Angle ∠d</th>
                    <th>Linear Pairs (a+b, b+c)</th>
                    <th>Opposite Pairs (a vs c, b vs d)</th>
                  </tr>
                </thead>
                <tbody>
                  <tr>
                    <td><strong>Pair 1</strong></td>
                    <td>120°</td>
                    <td>60°</td>
                    <td>120°</td>
                    <td>60°</td>
                    <td>120° + 60° = 180°</td>
                    <td>∠a = ∠c = 120°, ∠b = ∠d = 60°</td>
                  </tr>
                  <tr>
                    <td><strong>Pair 2</strong></td>
                    <td>45°</td>
                    <td>135°</td>
                    <td>45°</td>
                    <td>135°</td>
                    <td>45° + 135° = 180°</td>
                    <td>∠a = ∠c = 45°, ∠b = ∠d = 135°</td>
                  </tr>
                  <tr>
                    <td><strong>Pair 3</strong></td>
                    <td>70°</td>
                    <td>110°</td>
                    <td>70°</td>
                    <td>110°</td>
                    <td>70° + 110° = 180°</td>
                    <td>∠a = ∠c = 70°, ∠b = ∠d = 110°</td>
                  </tr>
                  <tr>
                    <td><strong>Pair 4</strong></td>
                    <td>90°</td>
                    <td>90°</td>
                    <td>90°</td>
                    <td>90°</td>
                    <td>90° + 90° = 180°</td>
                    <td>∠a = ∠c = 90°, ∠b = ∠d = 90°</td>
                  </tr>
                </tbody>
              </table>
            </div>
          </div>
          <div class="step-box step-4">
            <div class="step-header"><i class="fa-solid fa-magnifying-glass"></i> Step 4: Verification of Observed Patterns</div>
            <p>1. In every trial, angles lying opposite to each other across the vertex are exactly equal (<span class="math-inline">∠a = ∠c</span> and <span class="math-inline">∠b = ∠d</span>).</p>
            <p>2. In every trial, any two adjacent angles form a straight line and sum to <span class="math-inline">180°</span>.</p>
          </div>
          <div class="step-box step-5">
            <div class="step-header"><i class="fa-solid fa-flag-checkered"></i> Step 5: Final Answer Statement</div>
            <p><strong>Observed Patterns:</strong> Vertically opposite angles are always equal to each other, and adjacent angles formed along a straight line always sum to 180°.</p>
          </div>
        </div>
      </details>

      <!-- QUESTION 3: DEDUCTIVE REASONING PAGE 107 -->
      <details class="ans-box">
        <summary class="ans-header">
          <div class="summary-left">
            <i class="fa-solid fa-chevron-right summary-icon"></i>
            <span>NCERT In-Text Problem (Page 107): Finding ∠b, ∠c, ∠d When ∠a = 120°</span>
          </div>
          <span class="question-badge badge-intext">Deductive Problem</span>
        </summary>
        <div class="ans-content">
          <div class="step-box step-1">
            <div class="step-header"><i class="fa-solid fa-bullseye"></i> Step 1: What is Given &amp; What to Find</div>
            <p><strong>Given:</strong> In Fig. 5.2, two lines <span class="math-inline">l</span> and <span class="math-inline">m</span> intersect, forming angles <span class="math-inline">∠a, ∠b, ∠c, ∠d</span>. Given that <span class="math-inline">∠a = 120°</span>.</p>
            <p><strong>To Find:</strong> The exact measures of <span class="math-inline">∠b</span>, <span class="math-inline">∠c</span>, and <span class="math-inline">∠d</span> without drawing or measuring them.</p>
          </div>
          <div class="step-box step-2">
            <div class="step-header"><i class="fa-solid fa-lightbulb"></i> Step 2: Key Concept &amp; Formula</div>
            <p>The angle on a straight line is <span class="math-inline">180°</span>. Therefore, any linear pair of adjacent angles sums to <span class="math-inline">180°</span>.</p>
          </div>
          <div class="step-box step-3">
            <div class="step-header"><i class="fa-solid fa-pen-to-square"></i> Step 3: Mathematical Calculations</div>
            <p>1. <span class="math-inline">∠a</span> and <span class="math-inline">∠b</span> form a straight angle on line <span class="math-inline">l</span>:</p>
            <div class="math-display">∠a + ∠b = 180° ⇒ 120° + ∠b = 180° ⇒ ∠b = 180° - 120° = 60°</div>
            <p>2. <span class="math-inline">∠b</span> and <span class="math-inline">∠c</span> form a straight angle on line <span class="math-inline">m</span>:</p>
            <div class="math-display">∠b + ∠c = 180° ⇒ 60° + ∠c = 180° ⇒ ∠c = 180° - 60° = 120°</div>
            <p>3. <span class="math-inline">∠c</span> and <span class="math-inline">∠d</span> form a straight angle on line <span class="math-inline">l</span>:</p>
            <div class="math-display">∠c + ∠d = 180° ⇒ 120° + ∠d = 180° ⇒ ∠d = 180° - 120° = 60°</div>
          </div>
          <div class="step-box step-4">
            <div class="step-header"><i class="fa-solid fa-magnifying-glass"></i> Step 4: Verification &amp; Total Sum Check</div>
            <p>Check the sum of all four angles around the intersection point:</p>
            <div class="math-display">∠a + ∠b + ∠c + ∠d = 120° + 60° + 120° + 60° = 360° (Full circle confirmed!)</div>
          </div>
          <div class="step-box step-5">
            <div class="step-header"><i class="fa-solid fa-flag-checkered"></i> Step 5: Final Answer Statement</div>
            <p><strong>Values:</strong> <strong>∠b = 60°</strong>, <strong>∠c = 120°</strong>, and <strong>∠d = 60°</strong>.</p>
          </div>
        </div>
      </details>

      <!-- QUESTION 4: FORMAL PROOF OF VERTICALLY OPPOSITE ANGLES PAGE 107-108 -->
      <details class="ans-box">
        <summary class="ans-header">
          <div class="summary-left">
            <i class="fa-solid fa-chevron-right summary-icon"></i>
            <span>Textbook Formal Proof (Page 107-108): General Proof that Vertically Opposite Angles are Equal</span>
          </div>
          <span class="question-badge badge-try">Mathematical Proof</span>
        </summary>
        <div class="ans-content">
          <div class="step-box step-1">
            <div class="step-header"><i class="fa-solid fa-bullseye"></i> Step 1: What is Given &amp; What to Prove</div>
            <p><strong>Given:</strong> Two straight lines <span class="math-inline">l</span> and <span class="math-inline">m</span> intersect at a point, forming angles <span class="math-inline">∠a, ∠b, ∠c, ∠d</span>.</p>
            <p><strong>To Prove:</strong> Vertically opposite angles are equal, i.e., <span class="math-inline">∠a = ∠c</span> and <span class="math-inline">∠b = ∠d</span>, for any arbitrary angle measure.</p>
          </div>
          <div class="step-box step-2">
            <div class="step-header"><i class="fa-solid fa-lightbulb"></i> Step 2: Axiom / Theorem Used</div>
            <p><strong>Linear Pair Axiom:</strong> If a ray stands on a straight line, the sum of two adjacent angles formed is equal to <span class="math-inline">180°</span>.</p>
          </div>
          <div class="step-box step-3">
            <div class="step-header"><i class="fa-solid fa-pen-to-square"></i> Step 3: Deductive Derivation</div>
            <p>1. Since straight line <span class="math-inline">l</span> has adjacent angles <span class="math-inline">∠a</span> and <span class="math-inline">∠b</span>:</p>
            <div class="math-display">∠a + ∠b = 180° &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;--- (Equation 1)</div>
            <p>2. Since straight line <span class="math-inline">m</span> has adjacent angles <span class="math-inline">∠b</span> and <span class="math-inline">∠c</span>:</p>
            <div class="math-display">∠b + ∠c = 180° &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;--- (Equation 2)</div>
            <p>3. From (1) and (2), both expressions equal 180°. Therefore, by Euclid's First Common Notion:</p>
            <div class="math-display">∠a + ∠b = ∠b + ∠c</div>
            <p>4. Subtracting <span class="math-inline">∠b</span> from both sides:</p>
            <div class="math-display">∠a + ∠b - ∠b = ∠b + ∠c - ∠b ⇒ <strong>∠a = ∠c</strong></div>
            <p>5. Similarly, along line <span class="math-inline">l</span>, <span class="math-inline">∠c + ∠d = 180°</span>. Since <span class="math-inline">∠b + ∠c = 180°</span>:</p>
            <div class="math-display">∠b + ∠c = ∠c + ∠d ⇒ <strong>∠b = ∠d</strong></div>
          </div>
          <div class="step-box step-4">
            <div class="step-header"><i class="fa-solid fa-magnifying-glass"></i> Step 4: Verification</div>
            <p>This proof does not use any specific numbers like 120° or 60°. It holds true for any real angle measure <span class="math-inline">0° &lt; θ &lt; 180°</span>.</p>
          </div>
          <div class="step-box step-5">
            <div class="step-header"><i class="fa-solid fa-flag-checkered"></i> Step 5: Final Answer Statement</div>
            <p><strong>Conclusion:</strong> Hence proved that whenever two straight lines intersect, vertically opposite angles are strictly equal.</p>
          </div>
        </div>
      </details>

      <!-- QUESTION 5: FIGURE IT OUT PAGE 108 -->
      <details class="ans-box">
        <summary class="ans-header">
          <div class="summary-left">
            <i class="fa-solid fa-chevron-right summary-icon"></i>
            <span>Figure it Out (Page 108): Listing All Linear Pairs &amp; Vertically Opposite Pairs in Fig. 5.3</span>
          </div>
          <span class="question-badge badge-exercise">Figure it Out</span>
        </summary>
        <div class="ans-content">
          <div class="step-box step-1">
            <div class="step-header"><i class="fa-solid fa-bullseye"></i> Step 1: What is Given &amp; What to Find</div>
            <p><strong>Given:</strong> Figure 5.3 showing two straight lines <span class="math-inline">l</span> and <span class="math-inline">m</span> intersecting, with four angles labelled <span class="math-inline">a, b, c, d</span>.</p>
            <p><strong>To Find:</strong> Complete exhaustive list of (a) all linear pairs, and (b) all pairs of vertically opposite angles.</p>
          </div>
          <div class="step-box step-2">
            <div class="step-header"><i class="fa-solid fa-lightbulb"></i> Step 2: Definitions</div>
            <p>• <strong>Linear Pair:</strong> Two adjacent angles on a straight line that add up to 180°.<br>• <strong>Vertically Opposite Angles:</strong> Non-adjacent angles facing each other across the intersection vertex.</p>
          </div>
          <div class="step-box step-3">
            <div class="step-header"><i class="fa-solid fa-pen-to-square"></i> Step 3: Complete Listing</div>
            <p><strong>(a) Linear Pairs (4 total pairs):</strong></p>
            <ol style="margin-left: 2rem;">
              <li><span class="math-inline">∠a</span> and <span class="math-inline">∠b</span> (along line l)</li>
              <li><span class="math-inline">∠b</span> and <span class="math-inline">∠c</span> (along line m)</li>
              <li><span class="math-inline">∠c</span> and <span class="math-inline">∠d</span> (along line l)</li>
              <li><span class="math-inline">∠d</span> and <span class="math-inline">∠a</span> (along line m)</li>
            </ol>
            <p style="margin-top: 1rem;"><strong>(b) Pairs of Vertically Opposite Angles (2 total pairs):</strong></p>
            <ol style="margin-left: 2rem;">
              <li><span class="math-inline">∠a</span> and <span class="math-inline">∠c</span></li>
              <li><span class="math-inline">∠b</span> and <span class="math-inline">∠d</span></li>
            </ol>
          </div>
          <div class="step-box step-4">
            <div class="step-header"><i class="fa-solid fa-magnifying-glass"></i> Step 4: Verification</div>
            <p>Linear pairs: 4 pairs of adjacent angles along the 2 straight lines. Vertically opposite: 2 pairs of non-adjacent opposite angles. Total angle relationships accounted for.</p>
          </div>
          <div class="step-box step-5">
            <div class="step-header"><i class="fa-solid fa-flag-checkered"></i> Step 5: Final Answer Statement</div>
            <p><strong>Linear Pairs:</strong> (∠a, ∠b), (∠b, ∠c), (∠c, ∠d), (∠d, ∠a).<br><strong>Vertically Opposite:</strong> (∠a, ∠c) and (∠b, ∠d).</p>
          </div>
        </div>
      </details>

      <!-- QUESTION 6: MEASUREMENTS & GEOMETRY IN-TEXT BOX PAGE 108 -->
      <details class="ans-box">
        <summary class="ans-header">
          <div class="summary-left">
            <i class="fa-solid fa-chevron-right summary-icon"></i>
            <span>Measurements and Geometry (Page 108): Why Linear Pairs May Not Add Up to Exactly 180° When Measured</span>
          </div>
          <span class="question-badge badge-intext">Conceptual Inquiry</span>
        </summary>
        <div class="ans-content">
          <div class="step-box step-1">
            <div class="step-header"><i class="fa-solid fa-bullseye"></i> Step 1: What is Given &amp; What to Find</div>
            <p><strong>Question:</strong> When you measure linear pairs with a protractor, why might they sometimes add up to 179° or 181°? Why might vertically opposite angles sometimes appear unequal when measured?</p>
          </div>
          <div class="step-box step-2">
            <div class="step-header"><i class="fa-solid fa-lightbulb"></i> Step 2: Key Concepts</div>
            <p>Difference between pure theoretical mathematical geometry (ideal concepts) and empirical physical measurements (real-world tool limitations).</p>
          </div>
          <div class="step-box step-3">
            <div class="step-header"><i class="fa-solid fa-pen-to-square"></i> Step 3: Step-by-Step Reasons</div>
            <p>1. <strong>Instrument Calibration &amp; Parallax Error:</strong> The human eye may not align the protractor center point or baseline precisely with the vertex and ray, leading to a ±1° reading error.</p>
            <p>2. <strong>Line Thickness:</strong> An ideal geometric line has zero width. But pencil graphite has a physical thickness of 0.5 mm to 1 mm, creating slight angle distortions.</p>
            <p>3. <strong>Mathematical Reasoning vs Physical Drawing:</strong> In geometry, we prove relationships through undeniable logic (deduction). We know a straight angle is 180°, so any two angles forming it must add up to 180° in pure geometry.</p>
          </div>
          <div class="step-box step-4">
            <div class="step-header"><i class="fa-solid fa-magnifying-glass"></i> Step 4: Verification &amp; Application</div>
            <p>Despite minor drawing errors, geometric predictions are so remarkably close to reality that they are successfully used in architecture, bridge engineering, and aeronautics.</p>
          </div>
          <div class="step-box step-5">
            <div class="step-header"><i class="fa-solid fa-flag-checkered"></i> Step 5: Final Answer Statement</div>
            <p><strong>Conclusion:</strong> Discrepancies are due to physical measurement errors and line thickness; purely reasoned geometric laws remain exact and unwavering.</p>
          </div>
        </div>
      </details>

      <!-- QUESTION 7: SECTION 5.2 IN-TEXT PROMPT PAGE 108 -->
      <details class="ans-box">
        <summary class="ans-header">
          <div class="summary-left">
            <i class="fa-solid fa-chevron-right summary-icon"></i>
            <span>NCERT In-Text Prompt (Page 108): Can Two Lines Intersect Such That All Four Angles Are Equal?</span>
          </div>
          <span class="question-badge badge-intext">Perpendicular Inquiry</span>
        </summary>
        <div class="ans-content">
          <div class="step-box step-1">
            <div class="step-header"><i class="fa-solid fa-bullseye"></i> Step 1: What is Given &amp; What to Find</div>
            <p><strong>Question:</strong> Can you draw a pair of intersecting lines such that all four angles are equal? What will be the measure of each angle?</p>
          </div>
          <div class="step-box step-2">
            <div class="step-header"><i class="fa-solid fa-lightbulb"></i> Step 2: Key Formula</div>
            <p>The total sum of angles around a single point of intersection is <span class="math-inline">360°</span> (a complete circular rotation).</p>
          </div>
          <div class="step-box step-3">
            <div class="step-header"><i class="fa-solid fa-pen-to-square"></i> Step 3: Mathematical Calculation</div>
            <p>Let each of the four equal angles be <span class="math-inline">x</span>.</p>
            <div class="math-display">
              x + x + x + x = 360°<br>
              4x = 360°<br>
              x = 360° ÷ 4 = 90°
            </div>
          </div>
          <div class="step-box step-4">
            <div class="step-header"><i class="fa-solid fa-magnifying-glass"></i> Step 4: Verification via Linear Pairs</div>
            <p>Any two adjacent angles sum to: <span class="math-inline">90° + 90° = 180°</span> (A true linear pair!).</p>
          </div>
          <div class="step-box step-5">
            <div class="step-header"><i class="fa-solid fa-flag-checkered"></i> Step 5: Final Answer Statement</div>
            <p><strong>Conclusion:</strong> <strong>Yes</strong>, two lines can intersect such that all four angles are equal. The measure of each angle must be exactly <strong>90° (a right angle)</strong>. The lines are called <strong>perpendicular lines</strong>.</p>
          </div>
        </div>
      </details>

      <!-- QUESTION 8: SECTION 5.3 IN-TEXT ANALYSIS PAGE 109 -->
      <details class="ans-box">
        <summary class="ans-header">
          <div class="summary-left">
            <i class="fa-solid fa-chevron-right summary-icon"></i>
            <span>Section 5.3 In-Text Analysis (Page 109, Fig. 5.5): Describing How Line Segments Meet or Cross</span>
          </div>
          <span class="question-badge badge-intext">Geometric Description</span>
        </summary>
        <div class="ans-content">
          <div class="step-box step-1">
            <div class="step-header"><i class="fa-solid fa-bullseye"></i> Step 1: What is Given &amp; What to Describe</div>
            <p><strong>Given:</strong> Figure 5.5 with multiple pairs of line segments (<span class="math-inline">FG, FH, ST, UV, OP, QR</span>, etc.).</p>
            <p><strong>Task:</strong> Describe how the line segments meet or cross using precise mathematical terms (endpoint, point, intersect, extend, angle measure).</p>
          </div>
          <div class="step-box step-2">
            <div class="step-header"><i class="fa-solid fa-lightbulb"></i> Step 2: Precise Terminology</div>
            <p>• Segments can meet at an <strong>endpoint</strong>.<br>• Segments can intersect at an internal <strong>point of intersection</strong>.<br>• Segments can be <strong>converging</strong> (will meet if extended) or <strong>parallel</strong> (never meet when extended).</p>
          </div>
          <div class="step-box step-3">
            <div class="step-header"><i class="fa-solid fa-pen-to-square"></i> Step 3: Detailed Case-by-Case Breakdown</div>
            <p>1. <strong>Segments FG and FH:</strong> Meet at the common endpoint <span class="math-inline">F</span> at an angle of <span class="math-inline">115.3°</span>.</p>
            <p>2. <strong>Segments ST and UV:</strong> They do not currently touch, but they are inclined toward each other. <em>If extended, line segments ST and UV are likely to meet at an intersection point.</em></p>
            <p>3. <strong>Segments OP and QR:</strong> They are straight segments lying at a constant distance apart. <em>If extended, line segments OP and QR will never meet. They are parallel line segments.</em></p>
          </div>
          <div class="step-box step-4">
            <div class="step-header"><i class="fa-solid fa-magnifying-glass"></i> Step 4: Verification</div>
            <p>Using a straight ruler to trace the paths verifies that ST and UV converge to an intersection point, whereas OP and QR remain equidistant.</p>
          </div>
          <div class="step-box step-5">
            <div class="step-header"><i class="fa-solid fa-flag-checkered"></i> Step 5: Final Answer Statement</div>
            <p><strong>Summary:</strong> FG and FH meet at endpoint F (115.3°); ST and UV will intersect when extended; OP and QR will never intersect when extended as they are parallel.</p>
          </div>
        </div>
      </details>

      <!-- QUESTION 9: SECTION 5.4 IN-TEXT & FIG 5.6 PAGE 110 -->
      <details class="ans-box">
        <summary class="ans-header">
          <div class="summary-left">
            <i class="fa-solid fa-chevron-right summary-icon"></i>
            <span>Section 5.4 In-Text &amp; Fig. 5.6 (Page 110): Spotting Classroom Parallel Lines &amp; Identifying Parallel Sets</span>
          </div>
          <span class="question-badge badge-try">Visual Identification</span>
        </summary>
        <div class="ans-content">
          <div class="step-box step-1">
            <div class="step-header"><i class="fa-solid fa-bullseye"></i> Step 1: What is Given &amp; What to Find</div>
            <p><strong>Questions:</strong> (a) Name some parallel lines you can spot in your classroom. (b) In Fig. 5.6, which pairs of lines appear to be parallel?</p>
          </div>
          <div class="step-box step-2">
            <div class="step-header"><i class="fa-solid fa-lightbulb"></i> Step 2: Key Geometric Criteria</div>
            <p>Lines must lie on the same plane and maintain a constant perpendicular distance apart (equidistant).</p>
          </div>
          <div class="step-box step-3">
            <div class="step-header"><i class="fa-solid fa-pen-to-square"></i> Step 3: Analysis &amp; Identification</div>
            <p><strong>(a) Classroom Parallel Lines Examples:</strong></p>
            <ul style="margin-left: 1.5rem;">
              <li>Opposite edges of the classroom blackboard/whiteboard.</li>
              <li>Ruled horizontal lines on a student's notebook page.</li>
              <li>Opposite horizontal edges of the classroom door and window frames.</li>
              <li>Opposite edges of a student desk tabletop.</li>
              <li>Parallel fluorescent tube-light fixtures mounted on the ceiling.</li>
            </ul>
            <p style="margin-top: 1rem;"><strong>(b) Parallel Sets in Fig. 5.6 (Official Textbook Classification):</strong></p>
            <ul style="margin-left: 1.5rem;">
              <li>Lines <span class="math-inline">a</span>, <span class="math-inline">i</span>, and <span class="math-inline">h</span> are parallel to each other (<span class="math-inline">a ∥ i ∥ h</span>).</li>
              <li>Lines <span class="math-inline">c</span> and <span class="math-inline">g</span> are parallel to each other (<span class="math-inline">c ∥ g</span>).</li>
              <li>Lines <span class="math-inline">d</span> and <span class="math-inline">f</span> are parallel to each other (<span class="math-inline">d ∥ f</span>).</li>
              <li>Lines <span class="math-inline">e</span> and <span class="math-inline">b</span> are parallel to each other (<span class="math-inline">e ∥ b</span>).</li>
            </ul>
          </div>
          <div class="step-box step-4">
            <div class="step-header"><i class="fa-solid fa-magnifying-glass"></i> Step 4: Verification</div>
            <p>Measuring perpendicular distance between line pairs at multiple points confirms that their separation remains identical throughout.</p>
          </div>
          <div class="step-box step-5">
            <div class="step-header"><i class="fa-solid fa-flag-checkered"></i> Step 5: Final Answer Statement</div>
            <p><strong>Answer:</strong> In Fig. 5.6, the parallel sets are: <strong>(a, i, h)</strong>, <strong>(c, g)</strong>, <strong>(d, f)</strong>, and <strong>(e, b)</strong>.</p>
          </div>
        </div>
      </details>

      <!-- QUESTION 10: ACTIVITY 2 PAGE 111-112 -->
      <details class="ans-box">
        <summary class="ans-header">
          <div class="summary-left">
            <i class="fa-solid fa-chevron-right summary-icon"></i>
            <span>Activity 2 (Page 111-112): Paper-Folding Sequences, Edges, &amp; The 2ⁿ + 1 Pattern</span>
          </div>
          <span class="question-badge badge-try">Origami Activity</span>
        </summary>
        <div class="ans-content">
          <div class="step-box step-1">
            <div class="step-header"><i class="fa-solid fa-bullseye"></i> Step 1: What is Given &amp; All In-Text Prompts</div>
            <p>Take a plain square sheet of paper and perform sequential folds:</p>
            <ol style="margin-left: 1.5rem;">
              <li>Opposite edges description.</li>
              <li>Adjacent edges description.</li>
              <li>First horizontal half-fold: parallel lines count and relation to vertical sides.</li>
              <li>Second horizontal fold: parallel lines count.</li>
              <li>Third horizontal fold: parallel lines count and general pattern formula.</li>
              <li>Vertical fold relation to horizontal creases.</li>
              <li>Diagonal fold and creating parallel lines to the diagonal.</li>
            </ol>
          </div>
          <div class="step-box step-2">
            <div class="step-header"><i class="fa-solid fa-lightbulb"></i> Step 2: Geometric Principles of Paper Folding</div>
            <p>Folding a flat sheet aligns edges and divides planar regions symmetrically. A crease forms a straight line segment. Folding an edge onto its opposite edge bisects the region perpendicularly.</p>
          </div>
          <div class="step-box step-3">
            <div class="step-header"><i class="fa-solid fa-pen-to-square"></i> Step 3: Complete Answers to Prompts</div>
            <p>1. <strong>Opposite Edges:</strong> The opposite edges of the sheet are <strong>parallel</strong> to each other.</p>
            <p>2. <strong>Adjacent Edges:</strong> The adjacent edges are <strong>perpendicular</strong> to each other (they meet at 90° right angles).</p>
            <p>3. <strong>First Horizontal Fold:</strong> We see <strong>3 parallel lines</strong> (2 original outer edges + 1 middle crease). The new crease is <strong>perpendicular</strong> to the vertical side edges.</p>
            <p>4. <strong>Second Horizontal Fold:</strong> We see <strong>5 parallel lines</strong> (2 original edges + 3 creases).</p>
            <p>5. <strong>Third Horizontal Fold:</strong> We see <strong>9 parallel lines</strong> (2 original edges + 7 creases).</p>
            <p>6. <strong>General Pattern:</strong> The number of parallel lines follows the formula <span class="math-inline">2ⁿ + 1</span>, where <span class="math-inline">n</span> is the number of successive folds.</p>
            <p>7. <strong>Vertical Fold:</strong> This new vertical line is <strong>perpendicular</strong> to all the previous horizontal lines.</p>
            <p>8. <strong>Diagonal Fold:</strong> Yes, by folding a corner onto the diagonal crease, we create a crease strictly <strong>parallel to the diagonal line</strong>.</p>
          </div>
          <div class="step-box step-4">
            <div class="step-header"><i class="fa-solid fa-magnifying-glass"></i> Step 4: Verification of 2ⁿ + 1 Formula</div>
            <div class="math-display">
              For n = 1: 2¹ + 1 = 3 lines.<br>
              For n = 2: 2² + 1 = 5 lines.<br>
              For n = 3: 2³ + 1 = 9 lines.<br>
              For n = 4: 2⁴ + 1 = 17 lines. Formula holds perfectly!
            </div>
          </div>
          <div class="step-box step-5">
            <div class="step-header"><i class="fa-solid fa-flag-checkered"></i> Step 5: Final Answer Statement</div>
            <p><strong>Summary:</strong> Opposite edges are parallel; adjacent edges are perpendicular; horizontal folds generate 3, 5, 9 parallel lines according to the general formula <span class="math-inline">2ⁿ + 1</span>.</p>
          </div>
        </div>
      </details>

      <!-- QUESTION 11: CORNER FOLDING ACTIVITY PAGE 112 -->
      <details class="ans-box">
        <summary class="ans-header">
          <div class="summary-left">
            <i class="fa-solid fa-chevron-right summary-icon"></i>
            <span>Activity (Page 112, Fig. 5.8): Corner Folding to Center Line — Are a, b, c Parallel to p, q, r?</span>
          </div>
          <span class="question-badge badge-try">Origami Proof</span>
        </summary>
        <div class="ans-content">
          <div class="step-box step-1">
            <div class="step-header"><i class="fa-solid fa-bullseye"></i> Step 1: What is Given &amp; What to Find</div>
            <p><strong>Given:</strong> A square sheet folded in the middle, edges folded to the center crease, top-right and bottom-left corners folded onto the crease line creating triangles (Fig. 5.8).</p>
            <p><strong>Question:</strong> Are segments <span class="math-inline">a, b, c</span> parallel to <span class="math-inline">p, q, r</span> respectively? Why or why not?</p>
          </div>
          <div class="step-box step-2">
            <div class="step-header"><i class="fa-solid fa-lightbulb"></i> Step 2: Geometric Symmetry &amp; Perpendicularity</div>
            <p>Lines perpendicular to the same line are parallel. Symmetric corner folds along identical angular orientations create parallel segments.</p>
          </div>
          <div class="step-box step-3">
            <div class="step-header"><i class="fa-solid fa-pen-to-square"></i> Step 3: Step-by-Step Justification</div>
            <p><strong>Yes, line segments a, b, and c are strictly parallel to p, q, and r respectively:</strong></p>
            <p>1. <strong>a ∥ p:</strong> Segments <span class="math-inline">a</span> and <span class="math-inline">p</span> lie on the outer edge and the central crease of the paper, which were formed by folding the sheet in half. Therefore, <span class="math-inline">a ∥ p</span>.</p>
            <p>2. <strong>b ∥ q:</strong> Segments <span class="math-inline">b</span> and <span class="math-inline">q</span> are both perpendicular to the horizontal crease lines. Since two lines perpendicular to the same line are parallel, <span class="math-inline">b ∥ q</span>.</p>
            <p>3. <strong>c ∥ r:</strong> Segments <span class="math-inline">c</span> and <span class="math-inline">r</span> are the hypotenuses of identical corner fold triangles folded along the same diagonal direction at 45°. Because they share identical orientation and corresponding angles, <span class="math-inline">c ∥ r</span>.</p>
          </div>
          <div class="step-box step-4">
            <div class="step-header"><i class="fa-solid fa-magnifying-glass"></i> Step 4: Verification</div>
            <p>Placing a set square or protractor shows that segments c and r make the identical 45° angle with the base, verifying parallelism via equal corresponding angles.</p>
          </div>
          <div class="step-box step-5">
            <div class="step-header"><i class="fa-solid fa-flag-checkered"></i> Step 5: Final Answer Statement</div>
            <p><strong>Answer:</strong> <strong>Yes</strong>, <span class="math-inline">a ∥ p</span>, <span class="math-inline">b ∥ q</span>, and <span class="math-inline">c ∥ r</span> due to shared perpendicularity to creases and identical 45° angular orientation.</p>
          </div>
        </div>
      </details>

      <!-- QUESTION 12: FIGURE IT OUT Q1 PAGE 113 -->
      <details class="ans-box">
        <summary class="ans-header">
          <div class="summary-left">
            <i class="fa-solid fa-chevron-right summary-icon"></i>
            <span>Figure it Out Q1 (Page 113, Fig. 5.10): Drawing Perpendicular Lines on Dot Paper</span>
          </div>
          <span class="question-badge badge-exercise">Figure it Out</span>
        </summary>
        <div class="ans-content">
          <div class="step-box step-1">
            <div class="step-header"><i class="fa-solid fa-bullseye"></i> Step 1: What is Given &amp; Task</div>
            <p><strong>Given:</strong> A square grid dot paper containing various pre-drawn line segments (horizontal, vertical, and diagonal at 45°).</p>
            <p><strong>Task:</strong> Draw lines strictly perpendicular to the given lines using the grid dots as guide points.</p>
          </div>
          <div class="step-box step-2">
            <div class="step-header"><i class="fa-solid fa-lightbulb"></i> Step 2: Dot Paper Geometry</div>
            <p>On square dot paper, rows run horizontally and columns run vertically at an exact 90° angle. A line with a slope of 1 (45° diagonal) has a perpendicular line with a slope of -1 (the opposite diagonal).</p>
          </div>
          <div class="step-box step-3">
            <div class="step-header"><i class="fa-solid fa-pen-to-square"></i> Step 3: Construction Technique</div>
            <p>1. <strong>For Horizontal Segments:</strong> Connect dots along the vertical column crossing the segment. The vertical line makes an exact 90° angle with the horizontal segment.</p>
            <p>2. <strong>For Vertical Segments:</strong> Connect dots along the horizontal row crossing the segment. The horizontal line makes an exact 90° angle.</p>
            <p>3. <strong>For 45° Diagonal Segments (sloping up-right):</strong> Connect dots diagonally in the opposite direction (sloping down-right). The two diagonals of a square grid always intersect perpendicularly at 90°.</p>
          </div>
          <div class="step-box step-4">
            <div class="step-header"><i class="fa-solid fa-magnifying-glass"></i> Step 4: Verification</div>
            <p>Place the corner of a set square or protractor at the intersection of the drawn lines. The angle measures exactly 90°.</p>
          </div>
          <div class="step-box step-5">
            <div class="step-header"><i class="fa-solid fa-flag-checkered"></i> Step 5: Final Answer Statement</div>
            <p><strong>Result:</strong> Perpendicular lines are constructed by drawing vertical lines across horizontal segments, horizontal lines across vertical segments, and opposite diagonal lines across 45° segments.</p>
          </div>
        </div>
      </details>

      <!-- QUESTION 13: FIGURE IT OUT Q2 PAGE 113 -->
      <details class="ans-box">
        <summary class="ans-header">
          <div class="summary-left">
            <i class="fa-solid fa-chevron-right summary-icon"></i>
            <span>Figure it Out Q2 (Page 113, Fig. 5.11): Marking Parallel Lines &amp; Spotting Perpendiculars</span>
          </div>
          <span class="question-badge badge-exercise">Figure it Out</span>
        </summary>
        <div class="ans-content">
          <div class="step-box step-1">
            <div class="step-header"><i class="fa-solid fa-bullseye"></i> Step 1: What is Given &amp; Questions</div>
            <p><strong>Given:</strong> Figure 5.11 showing an intricate grid figure with multiple line segments.</p>
            <p><strong>Tasks:</strong><br>(a) Mark parallel lines with arrow symbols (&gt;, &gt;&gt;) and mark perpendicular angles with square symbols (⊾).<br>(b) How did you spot the perpendicular lines?<br>(c) How did you spot the parallel lines?</p>
          </div>
          <div class="step-box step-2">
            <div class="step-header"><i class="fa-solid fa-lightbulb"></i> Step 2: Geometric Definitions</div>
            <p>• Perpendicular lines meet at right angles (90°).<br>• Parallel lines maintain constant separation throughout their length and have identical slope/direction.</p>
          </div>
          <div class="step-box step-3">
            <div class="step-header"><i class="fa-solid fa-pen-to-square"></i> Step 3: Detailed Answers</div>
            <p><strong>(a) Marking Notations:</strong> Single arrow (&gt;) is marked on the first set of parallel horizontal lines; double arrow (&gt;&gt;) is marked on the set of parallel inclined lines. Square symbols (⊾) are marked at all vertices where horizontal and vertical segments meet.</p>
            <p><strong>(b) How Perpendicular Lines Were Spotted:</strong> The vertical and horizontal lines on the grid paper meet at an exact <strong>90-degree right angle</strong>. We spot them by finding lines that follow the vertical and horizontal grid axes or by using the corner of a set square.</p>
            <p><strong>(c) How Parallel Lines Were Spotted:</strong> By identifying lines that <strong>always remain the exact same perpendicular distance apart</strong> from one end to the other and have matching slopes across the grid.</p>
          </div>
          <div class="step-box step-4">
            <div class="step-header"><i class="fa-solid fa-magnifying-glass"></i> Step 4: Verification</div>
            <p>Measuring perpendicular distance with a ruler at three separate locations along the segments confirms they are equidistant.</p>
          </div>
          <div class="step-box step-5">
            <div class="step-header"><i class="fa-solid fa-flag-checkered"></i> Step 5: Final Answer Statement</div>
            <p><strong>Summary:</strong> Perpendicular lines were spotted by 90° intersections along grid axes; parallel lines were spotted by constant perpendicular separation.</p>
          </div>
        </div>
      </details>

      <!-- QUESTION 14: FIGURE IT OUT Q3 PAGE 113 -->
      <details class="ans-box">
        <summary class="ans-header">
          <div class="summary-left">
            <i class="fa-solid fa-chevron-right summary-icon"></i>
            <span>Figure it Out Q3 (Page 113): Drawing Different Sets of Parallel Lines on Dot Paper</span>
          </div>
          <span class="question-badge badge-exercise">Figure it Out</span>
        </summary>
        <div class="ans-content">
          <div class="step-box step-1">
            <div class="step-header"><i class="fa-solid fa-bullseye"></i> Step 1: What is Given &amp; Task</div>
            <p><strong>Task:</strong> In dot paper, draw different sets of parallel lines. The line segments can be of different lengths, but their endpoints must be dots on the paper.</p>
          </div>
          <div class="step-box step-2">
            <div class="step-header"><i class="fa-solid fa-lightbulb"></i> Step 2: Slope Rule on Dot Grids</div>
            <p>On dot paper, two segments are parallel if they have the exact same "rise over run" (vertical step ÷ horizontal step). For example, 1 unit up and 2 units right.</p>
          </div>
          <div class="step-box step-3">
            <div class="step-header"><i class="fa-solid fa-pen-to-square"></i> Step 3: Step-by-Step Construction of 3 Distinct Sets</div>
            <p>1. <strong>Set 1 (Horizontal Parallel Lines):</strong> Draw segment <span class="math-inline">AB</span> of length 4 dots horizontally along Row 2. Draw segment <span class="math-inline">CD</span> of length 6 dots horizontally along Row 4. Since both have slope 0, <span class="math-inline">AB ∥ CD</span>.</p>
            <p>2. <strong>Set 2 (Vertical Parallel Lines):</strong> Draw segment <span class="math-inline">EF</span> of length 3 dots along Column 3. Draw segment <span class="math-inline">GH</span> of length 5 dots along Column 6. Both are vertical, so <span class="math-inline">EF ∥ GH</span>.</p>
            <p>3. <strong>Set 3 (Slanted Parallel Lines):</strong> Draw a segment connecting dot (1,1) to (3,3) (slope 1). Draw another segment connecting dot (1,3) to (4,6) (slope 1). Since both climb 1 dot vertically for every 1 dot horizontally, they are strictly parallel!</p>
          </div>
          <div class="step-box step-4">
            <div class="step-header"><i class="fa-solid fa-magnifying-glass"></i> Step 4: Verification</div>
            <p>Sliding a set square confirms that the angle between each pair of drawn lines and a common transversal is identical.</p>
          </div>
          <div class="step-box step-5">
            <div class="step-header"><i class="fa-solid fa-flag-checkered"></i> Step 5: Final Answer Statement</div>
            <p><strong>Result:</strong> Successfully drawn sets of horizontal, vertical, and slanted parallel segments having dots as endpoints.</p>
          </div>
        </div>
      </details>

      <!-- QUESTION 15: FIGURE IT OUT Q4 PAGE 114 -->
      <details class="ans-box">
        <summary class="ans-header">
          <div class="summary-left">
            <i class="fa-solid fa-chevron-right summary-icon"></i>
            <span>Figure it Out Q4 (Page 114, Fig. 5.12): Drawing Parallel Lines to Given Segments a to h</span>
          </div>
          <span class="question-badge badge-exercise">Figure it Out</span>
        </summary>
        <div class="ans-content">
          <div class="step-box step-1">
            <div class="step-header"><i class="fa-solid fa-bullseye"></i> Step 1: What is Given &amp; Prompts</div>
            <p><strong>Given:</strong> Line segments <span class="math-inline">a, b, c, d, e, f, g, h</span> drawn on dot paper in various orientations.</p>
            <p><strong>Questions:</strong><br>(a) Did you find it challenging to draw some of them?<br>(b) Which ones were challenging?<br>(c) How did you do it?</p>
          </div>
          <div class="step-box step-2">
            <div class="step-header"><i class="fa-solid fa-lightbulb"></i> Step 2: Pedagogical Insight</div>
            <p>Horizontal and vertical segments follow the rectangular grid directly, making them effortless. But segments inclined at odd angles require counting grid steps (slope) to maintain equidistance.</p>
          </div>
          <div class="step-box step-3">
            <div class="step-header"><i class="fa-solid fa-pen-to-square"></i> Step 3: Complete Step-by-Step Answers</div>
            <p><strong>(a) Challenge:</strong> <strong>Yes</strong>, drawing parallel lines to some segments was notably harder than others.</p>
            <p><strong>(b) Which Ones Were Challenging:</strong> Line segments <strong>e, f, g, and h</strong> were challenging. Segments <span class="math-inline">a, b, c, d</span> were simple because they were strictly horizontal, vertical, or at 45°. But <span class="math-inline">e, f, g, h</span> had unusual slopes (like 1 dot up for every 2 or 3 dots across).</p>
            <p><strong>(c) How It Was Done:</strong> By counting the exact number of horizontal and vertical dot spaces between the segment's endpoints (its slope) and replicating that exact step from a new starting dot. This ensures that the new line segment remains <strong>equidistant</strong> from the original segment at every point.</p>
          </div>
          <div class="step-box step-4">
            <div class="step-header"><i class="fa-solid fa-magnifying-glass"></i> Step 4: Verification</div>
            <p>Using a transparent set square confirms that the angle of inclination of the newly drawn line matches the original line segment perfectly.</p>
          </div>
          <div class="step-box step-5">
            <div class="step-header"><i class="fa-solid fa-flag-checkered"></i> Step 5: Final Answer Statement</div>
            <p><strong>Answers:</strong> (a) Yes; (b) Segments e, f, g, and h; (c) By maintaining constant perpendicular distance and replicating the grid-step slope.</p>
          </div>
        </div>
      </details>

      <!-- QUESTION 16: FIGURE IT OUT Q5 PAGE 114 -->
      <details class="ans-box">
        <summary class="ans-header">
          <div class="summary-left">
            <i class="fa-solid fa-chevron-right summary-icon"></i>
            <span>Figure it Out Q5 (Page 114, Fig. 5.13): Which Line is Parallel to Line a — Line b or Line c?</span>
          </div>
          <span class="question-badge badge-exercise">Figure it Out</span>
        </summary>
        <div class="ans-content">
          <div class="step-box step-1">
            <div class="step-header"><i class="fa-solid fa-bullseye"></i> Step 1: What is Given &amp; Question</div>
            <p><strong>Given:</strong> Figure 5.13 showing line <span class="math-inline">a</span>, line <span class="math-inline">b</span>, and line <span class="math-inline">c</span>.</p>
            <p><strong>Question:</strong> Which line is parallel to line <span class="math-inline">a</span> — line <span class="math-inline">b</span> or line <span class="math-inline">c</span>? How do you decide this?</p>
          </div>
          <div class="step-box step-2">
            <div class="step-header"><i class="fa-solid fa-lightbulb"></i> Step 2: Criteria for Parallelism</div>
            <p>Two lines are parallel if and only if the perpendicular distance between them remains constant at all points, or if they never intersect when extended indefinitely.</p>
          </div>
          <div class="step-box step-3">
            <div class="step-header"><i class="fa-solid fa-pen-to-square"></i> Step 3: Analysis of Lines b and c Against Line a</div>
            <p>1. <strong>Examining Line b:</strong> Look at the gap between line <span class="math-inline">a</span> and line <span class="math-inline">b</span>. As you move from left to right, the distance between them narrows. If both lines are extended to the right, they will visibly intersect. Therefore, line <span class="math-inline">b</span> is <strong>not parallel</strong> to line <span class="math-inline">a</span>.</p>
            <p>2. <strong>Examining Line c:</strong> Measure the perpendicular distance between line <span class="math-inline">a</span> and line <span class="math-inline">c</span> at the left end, middle, and right end. The distance remains exactly identical everywhere. They will never meet, however far extended.</p>
          </div>
          <div class="step-box step-4">
            <div class="step-header"><i class="fa-solid fa-magnifying-glass"></i> Step 4: Verification via Transversal</div>
            <p>Drawing a vertical transversal across line <span class="math-inline">a</span> and line <span class="math-inline">c</span> shows that their corresponding angles are identical, whereas the angles with line <span class="math-inline">b</span> are unequal.</p>
          </div>
          <div class="step-box step-5">
            <div class="step-header"><i class="fa-solid fa-flag-checkered"></i> Step 5: Final Answer Statement</div>
            <p><strong>Answer:</strong> <strong>Line c</strong> is parallel to line <span class="math-inline">a</span> because the perpendicular distance between line <span class="math-inline">a</span> and line <span class="math-inline">c</span> remains constant everywhere.</p>
          </div>
        </div>
      </details>

      <!-- QUESTION 17: SECTION 5.5 IN-TEXT INQUIRY PAGE 115 -->
      <details class="ans-box">
        <summary class="ans-header">
          <div class="summary-left">
            <i class="fa-solid fa-chevron-right summary-icon"></i>
            <span>Section 5.5 In-Text Inquiry (Page 115): Can a Transversal Form 8 or 5 Distinct Angle Measures?</span>
          </div>
          <span class="question-badge badge-intext">Transversal Inquiry</span>
        </summary>
        <div class="ans-content">
          <div class="step-box step-1">
            <div class="step-header"><i class="fa-solid fa-bullseye"></i> Step 1: What is Given &amp; Questions</div>
            <p>In Fig. 5.14, transversal <span class="math-inline">t</span> intersects lines <span class="math-inline">l</span> and <span class="math-inline">m</span>, forming 8 angles.</p>
            <p><strong>Questions:</strong><br>(a) Is it possible for all the eight angles to have different measurements? Why or why not?<br>(b) What about 5 different angles (or 6, 7)?</p>
          </div>
          <div class="step-box step-2">
            <div class="step-header"><i class="fa-solid fa-lightbulb"></i> Step 2: Theorem of Vertically Opposite Angles</div>
            <p>At any straight line intersection, vertically opposite angles are equal. At intersection 1: <span class="math-inline">∠1 = ∠3</span> and <span class="math-inline">∠2 = ∠4</span>. At intersection 2: <span class="math-inline">∠5 = ∠7</span> and <span class="math-inline">∠6 = ∠8</span>.</p>
          </div>
          <div class="step-box step-3">
            <div class="step-header"><i class="fa-solid fa-pen-to-square"></i> Step 3: Mathematical Deduction</div>
            <p><strong>(a) Can all 8 angles be different?</strong></p>
            <p><strong>NO!</strong> Because around vertex 1, <span class="math-inline">∠1 = ∠3</span> and <span class="math-inline">∠2 = ∠4</span> (at most 2 distinct measures). Around vertex 2, <span class="math-inline">∠5 = ∠7</span> and <span class="math-inline">∠6 = ∠8</span> (at most 2 distinct measures). Thus, in total, there can be at most <span class="math-inline">2 + 2 = 4</span> distinct angle measures. Having 8 different measures is mathematically impossible!</p>
            <p><strong>(b) What about 5, 6, or 7 different angles?</strong></p>
            <p><strong>NO!</strong> For the exact same reason: because vertically opposite angles force angles to exist in equal pairs, the number of distinct angle measures can NEVER exceed 4.</p>
          </div>
          <div class="step-box step-4">
            <div class="step-header"><i class="fa-solid fa-magnifying-glass"></i> Step 4: Verification</div>
            <p>Even if lines <span class="math-inline">l</span> and <span class="math-inline">m</span> are wildly non-parallel, vertex 1 has 2 values (e.g. 50° and 130°) and vertex 2 has 2 values (e.g. 70° and 110°). Total distinct measures = 4. When lines are parallel, total distinct measures drop to 2!</p>
          </div>
          <div class="step-box step-5">
            <div class="step-header"><i class="fa-solid fa-flag-checkered"></i> Step 5: Final Answer Statement</div>
            <p><strong>Conclusion:</strong> <strong>No</strong>, it is impossible to have 8, 7, 6, or 5 distinct angle measures. The maximum possible number of distinct angle measures formed by a transversal cutting two lines is <strong>4</strong>.</p>
          </div>
        </div>
      </details>

      <!-- QUESTION 18: SECTION 5.6 ACTIVITY 3 PAGE 115-116 -->
      <details class="ans-box">
        <summary class="ans-header">
          <div class="summary-left">
            <i class="fa-solid fa-chevron-right summary-icon"></i>
            <span>Section 5.6 Activity 3 (Page 115-116): Constructing Parallel Lines by Setting Corresponding Angles to 60°</span>
          </div>
          <span class="question-badge badge-try">Geometric Construction</span>
        </summary>
        <div class="ans-content">
          <div class="step-box step-1">
            <div class="step-header"><i class="fa-solid fa-bullseye"></i> Step 1: What is Given &amp; Objective</div>
            <p><strong>Task:</strong> Draw a pair of lines and a transversal such that they form only two distinct angle measures (60° and 120°).</p>
          </div>
          <div class="step-box step-2">
            <div class="step-header"><i class="fa-solid fa-lightbulb"></i> Step 2: Corresponding Angles Postulate</div>
            <p>If two coplanar lines cut by a transversal have equal corresponding angles, the two lines are parallel.</p>
          </div>
          <div class="step-box step-3">
            <div class="step-header"><i class="fa-solid fa-pen-to-square"></i> Step 3: Four Construction Steps</div>
            <p>1. <strong>Step 1:</strong> Draw a straight line <span class="math-inline">l</span> and draw a transversal <span class="math-inline">t</span> intersecting it at point <span class="math-inline">X</span>.</p>
            <p>2. <strong>Step 2:</strong> With a protractor, measure <span class="math-inline">∠a = 60°</span>. Its linear pair is naturally <span class="math-inline">180° - 60° = 120°</span>.</p>
            <p>3. <strong>Step 3:</strong> Mark a second point <span class="math-inline">Y</span> further along transversal <span class="math-inline">t</span>.</p>
            <p>4. <strong>Step 4:</strong> Through point <span class="math-inline">Y</span>, use your protractor (or tracing paper) to draw line <span class="math-inline">m</span> forming a corresponding angle <span class="math-inline">∠b = 60°</span> in the matching relative corner.</p>
          </div>
          <div class="step-box step-4">
            <div class="step-header"><i class="fa-solid fa-magnifying-glass"></i> Step 4: Verification</div>
            <p>Observing line <span class="math-inline">l</span> and line <span class="math-inline">m</span> reveals that they never meet. Measuring distance between them confirms they are perfectly parallel!</p>
          </div>
          <div class="step-box step-5">
            <div class="step-header"><i class="fa-solid fa-flag-checkered"></i> Step 5: Final Answer Statement</div>
            <p><strong>Conclusion:</strong> Lines <span class="math-inline">l</span> and <span class="math-inline">m</span> are parallel because their corresponding angles with transversal <span class="math-inline">t</span> were constructed to be strictly equal (<span class="math-inline">∠a = ∠b = 60°</span>).</p>
          </div>
        </div>
      </details>

      <!-- QUESTION 19: ACTIVITY 4 & 5 PAGE 117 -->
      <details class="ans-box">
        <summary class="ans-header">
          <div class="summary-left">
            <i class="fa-solid fa-chevron-right summary-icon"></i>
            <span>Activities 4 &amp; 5 (Page 117): Tracing Paper Test &amp; The Non-Parallel Lines Counter-Proof</span>
          </div>
          <span class="question-badge badge-try">Verification Activities</span>
        </summary>
        <div class="ans-content">
          <div class="step-box step-1">
            <div class="step-header"><i class="fa-solid fa-bullseye"></i> Step 1: What is Given &amp; Inquiries</div>
            <p>• <strong>Activity 4:</strong> Fig. 5.19 has parallel lines <span class="math-inline">l ∥ m</span> cut by transversal <span class="math-inline">t</span>. Trace <span class="math-inline">∠a</span> and superimpose over corresponding angle <span class="math-inline">∠b</span>.<br>• <strong>Activity 5:</strong> In Fig. 5.20, lines <span class="math-inline">l</span> and <span class="math-inline">m</span> are non-parallel. Can you draw a transversal <span class="math-inline">t</span> such that a pair of corresponding angles is equal?</p>
          </div>
          <div class="step-box step-2">
            <div class="step-header"><i class="fa-solid fa-lightbulb"></i> Step 2: Equivalence Theorem</div>
            <p>Parallelism of lines is logically equivalent to the equality of corresponding angles: <span class="math-inline">l ∥ m ⇔ Corresponding Angles are Equal</span>.</p>
          </div>
          <div class="step-box step-3">
            <div class="step-header"><i class="fa-solid fa-pen-to-square"></i> Step 3: Observations</div>
            <p>1. <strong>Activity 4 Result:</strong> When the tracing of <span class="math-inline">∠a</span> is placed over <span class="math-inline">∠b</span>, the arms and vertex align <strong>exactly</strong>. All four corresponding angle pairs match identically. <em>Corresponding angles formed by a transversal intersecting parallel lines are always equal.</em></p>
            <p>2. <strong>Activity 5 Result:</strong> You find it <strong>completely impossible</strong> to draw a transversal on non-parallel lines where corresponding angles match! No matter how you tilt the transversal ruler, one angle is always larger than the other. <em>When lines are not parallel, corresponding angles can NEVER be equal.</em></p>
          </div>
          <div class="step-box step-4">
            <div class="step-header"><i class="fa-solid fa-magnifying-glass"></i> Step 4: Verification</div>
            <p>Proved both ways: Parallel implies equal corresponding angles; Non-parallel implies unequal corresponding angles.</p>
          </div>
          <div class="step-box step-5">
            <div class="step-header"><i class="fa-solid fa-flag-checkered"></i> Step 5: Final Answer Statement</div>
            <p><strong>Conclusion:</strong> Equality of corresponding angles occurs <strong>if and only if</strong> the intersected lines are parallel.</p>
          </div>
        </div>
      </details>

      <!-- QUESTION 20: FIGURE IT OUT PAGE 119 -->
      <details class="ans-box">
        <summary class="ans-header">
          <div class="summary-left">
            <i class="fa-solid fa-chevron-right summary-icon"></i>
            <span>Section 5.7 Figure it Out (Page 119, Fig. 5.23): Drawing a Line Parallel to l Through External Point A</span>
          </div>
          <span class="question-badge badge-exercise">Geometry Box Construction</span>
        </summary>
        <div class="ans-content">
          <div class="step-box step-1">
            <div class="step-header"><i class="fa-solid fa-bullseye"></i> Step 1: What is Given &amp; Objective</div>
            <p><strong>Given:</strong> A straight line <span class="math-inline">l</span> and a point <span class="math-inline">A</span> lying outside line <span class="math-inline">l</span> (Fig. 5.23).</p>
            <p><strong>Task:</strong> Describe step-by-step how to construct a line parallel to <span class="math-inline">l</span> passing through point <span class="math-inline">A</span> using tools from your geometry box.</p>
          </div>
          <div class="step-box step-2">
            <div class="step-header"><i class="fa-solid fa-lightbulb"></i> Step 2: Tools Required &amp; Geometric Principle</div>
            <p><strong>Tools:</strong> Straightedge ruler, Set square (right-angled triangle), sharp pencil.<br><strong>Principle:</strong> Sliding a set square along a stationary ruler preserves equal 90° corresponding angles.</p>
          </div>
          <div class="step-box step-3">
            <div class="step-header"><i class="fa-solid fa-pen-to-square"></i> Step 3: Official 5-Step Drafting Method</div>
            <p>1. Place one edge of your set square so that it lies exactly along the given line <span class="math-inline">l</span>.</p>
            <p>2. Place the straightedge ruler firmly against the adjacent edge of the set square so that the ruler cannot slip or move.</p>
            <p>3. Hold the ruler firmly in place with your left hand, and carefully <strong>slide the set square along the ruler</strong> until its top edge reaches external point <span class="math-inline">A</span>.</p>
            <p>4. Using a sharp pencil, draw a straight line along the edge of the set square passing through point <span class="math-inline">A</span>.</p>
            <p>5. Remove the tools and extend the line in both directions with your ruler.</p>
          </div>
          <div class="step-box step-4">
            <div class="step-header"><i class="fa-solid fa-magnifying-glass"></i> Step 4: Verification</div>
            <p>The ruler acted as a transversal line. The set square maintained an angle of 90° with the ruler at both positions. Because corresponding angles are equal, the new line passing through point A is strictly parallel to line <span class="math-inline">l</span>.</p>
          </div>
          <div class="step-box step-5">
            <div class="step-header"><i class="fa-solid fa-flag-checkered"></i> Step 5: Final Answer Statement</div>
            <p><strong>Result:</strong> Successfully constructed a unique line parallel to <span class="math-inline">l</span> through point <span class="math-inline">A</span> using a ruler and set square.</p>
          </div>
        </div>
      </details>
"""
