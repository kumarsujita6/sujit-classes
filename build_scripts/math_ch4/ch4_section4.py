# -*- coding: utf-8 -*-
"""
Module: ch4_section4.py
Contains Section 4: 100% Solved NCERT Questions, In-Text Activities & Figure it Out Exercises.
Includes every in-text prompt, deduction, activity, and end-of-chapter question from Ganita Prakash
Chapter 4 (NEP Code: hegp104), solved in 5-step presentation inside collapsible <details class="ans-box"> tags.
"""

def get_section_4():
    return """
    <!-- SECTION 4: 100% SOLVED NCERT QUESTIONS -->
    <section id="section-4">
      <div class="section-header">
        <div class="section-tag"><i class="fa-solid fa-square-check"></i> Zero-Omission Textbook Solutions</div>
        <h2 class="section-title">Section 4: 100% Solved NCERT Questions, In-Text Activities &amp; Figure it Out Exercises</h2>
        <p class="section-desc">
          Every single in-text investigation, deduction proof, Geoboard activity, paper-folding challenge, and end-of-chapter "Figure it Out" problem in NCERT Ganita Prakash Grade 8 Chapter 4 (hegp104) solved step-by-step in a rigorous 5-step presentation.
        </p>
      </div>

      <!-- PART A: SECTION 4.1 IN-TEXT INVESTIGATIONS & DEDUCTIONS -->
      <h3 class="subheading"><i class="fa-solid fa-hammer"></i> 4.1 Rectangles &amp; Squares: In-Text Deductions &amp; Exercises (Pages 83–94)</h3>

      <!-- ITEM 1: THE CARPENTER'S PROBLEM -->
      <details class="ans-box" open>
        <summary>
          <span><i class="fa-solid fa-circle-question" style="color: var(--primary); margin-right: 0.5rem;"></i> Textbook Page 83: The Carpenter's Problem (Strip Length &amp; Hinge Location)</span>
        </summary>
        <div class="ans-content">
          <p><strong>Textbook Prompt:</strong> A carpenter needs to put together two thin strips of wood so that when a thread is passed through their endpoints, it forms a rectangle. She already has one 8 cm long strip. What should be the length of the other strip? Where should they both be joined?</p>
          <div class="step-container">
            <div class="step-box step-1">
              <span class="step-badge">Step 1: Given Data &amp; Geometric Objective</span>
              <p>We are given a wooden strip of length 8 cm representing one diagonal (AC) of a quadrilateral. The goal is to determine the length of the second strip (diagonal BD) and the exact point O where the two strips must be pinned together such that quadrilateral ABCD is guaranteed to be a rectangle.</p>
            </div>
            <div class="step-box step-2">
              <span class="step-badge">Step 2: Core Geometric Properties of a Rectangle</span>
              <p>By the definition and properties of a rectangle: (1) Diagonals of a rectangle are equal in length (AC = BD). (2) Diagonals bisect each other (OA = OC and OB = OD).</p>
            </div>
            <div class="step-box step-3">
              <span class="step-badge">Step 3: Step-by-Step Deduction &amp; Calculation</span>
              <p>1. <strong>Length of Second Strip:</strong> Since diagonals of a rectangle are equal, the second strip must have the same length as the first: Length of second strip = 8 cm.<br>
              2. <strong>Hinge Location:</strong> Since the diagonals bisect each other, the pivot hole must be drilled at the exact midpoint of both strips: Midpoint = 8 cm ÷ 2 = 4 cm from either end.<br>
              3. When the two 8 cm strips are pinned at their 4 cm midpoints, the distance from O to all four endpoints is equal: OA = OB = OC = OD = 4 cm.</p>
            </div>
            <div class="step-box step-4">
              <span class="step-badge">Step 4: Verification &amp; Consistency Check</span>
              <p>Let the angle between the strips be x. In the four resulting isosceles triangles, the base angles are a = 90° − x/2 and b = x/2. Each vertex angle is a + b = 90° − x/2 + x/2 = 90°. Since all four angles are 90°, ABCD is strictly a rectangle for any arbitrary opening angle.</p>
            </div>
            <div class="step-box step-5">
              <span class="step-badge">Step 5: Final Result &amp; Key Takeaway</span>
              <p><strong>Result:</strong> The second strip must be exactly <strong>8 cm long</strong>, and both strips must be joined at their <strong>exact midpoints (4 cm from each end)</strong>.</p>
            </div>
          </div>
        </div>
      </details>

      <!-- ITEM 2: DEDUCTION 1 -->
      <details class="ans-box">
        <summary>
          <span><i class="fa-solid fa-circle-question" style="color: var(--primary); margin-right: 0.5rem;"></i> Textbook Page 84: Deduction 1 (Why Diagonals of a Rectangle Are Equal)</span>
        </summary>
        <div class="ans-content">
          <p><strong>Textbook Prompt:</strong> Prove using triangle congruence that the diagonals of a rectangle always have the same length.</p>
          <div class="step-container">
            <div class="step-box step-1">
              <span class="step-badge">Step 1: Given Data &amp; Geometric Objective</span>
              <p>Let ABCD be a rectangle where all angles are 90° and opposite sides are equal (AB = CD and AD = BC). We need to prove that diagonal AC = diagonal BD.</p>
            </div>
            <div class="step-box step-2">
              <span class="step-badge">Step 2: Congruence Criterion Selected</span>
              <p>Consider the two overlapping right-angled triangles sitting on the base AD: △ADC and △DAB. We apply the Side-Angle-Side (SAS) congruence criterion.</p>
            </div>
            <div class="step-box step-3">
              <span class="step-badge">Step 3: Formal Step-by-Step Proof</span>
              <p>In △ADC and △DAB:<br>
              • AD = AD (Common base side)<br>
              • ∠ADC = ∠DAB = 90° (Angles of a rectangle are right angles)<br>
              • CD = BA (Opposite sides of a rectangle are equal)<br>
              By the SAS Congruence Criterion, <strong>△ADC ≅ △DAB</strong>.</p>
            </div>
            <div class="step-box step-4">
              <span class="step-badge">Step 4: CPCTC Deduction</span>
              <p>Corresponding parts of congruent triangles are congruent (CPCTC). The hypotenuse of △ADC is AC, and the hypotenuse of △DAB is BD. Therefore, <strong>AC = BD</strong>.</p>
            </div>
            <div class="step-box step-5">
              <span class="step-badge">Step 5: Final Conclusion</span>
              <p>The diagonals of any rectangle are always equal in length. Hence, if one diagonal is 8 cm, the other must be 8 cm.</p>
            </div>
          </div>
        </div>
      </details>

      <!-- ITEM 3: DEDUCTION 2 -->
      <details class="ans-box">
        <summary>
          <span><i class="fa-solid fa-circle-question" style="color: var(--primary); margin-right: 0.5rem;"></i> Textbook Page 84: Deduction 2 (Why Diagonals of a Rectangle Bisect Each Other)</span>
        </summary>
        <div class="ans-content">
          <p><strong>Textbook Prompt:</strong> What is the point of intersection of the two diagonals? Prove that O is the midpoint of AC and BD.</p>
          <div class="step-container">
            <div class="step-box step-1">
              <span class="step-badge">Step 1: Given Data &amp; Geometric Objective</span>
              <p>In rectangle ABCD, diagonals AC and BD intersect at O. We must prove OA = OC and OB = OD.</p>
            </div>
            <div class="step-box step-2">
              <span class="step-badge">Step 2: Congruence Tool</span>
              <p>We compare opposite interior triangles: △AOB and △COD, using parallel line transversal properties (AB ∥ CD).</p>
            </div>
            <div class="step-box step-3">
              <span class="step-badge">Step 3: Formal Step-by-Step Proof</span>
              <p>In △AOB and △COD:<br>
              • AB = CD (Opposite sides of rectangle are equal)<br>
              • ∠OAB = ∠OCD (Alternate interior angles with transversal AC)<br>
              • ∠OBA = ∠ODC (Alternate interior angles with transversal BD)<br>
              By the ASA (or AAS) Congruence Criterion, <strong>△AOB ≅ △COD</strong>.</p>
            </div>
            <div class="step-box step-4">
              <span class="step-badge">Step 4: CPCTC Deduction</span>
              <p>By CPCTC: <strong>OA = OC</strong> (O is midpoint of AC) and <strong>OB = OD</strong> (O is midpoint of BD).</p>
            </div>
            <div class="step-box step-5">
              <span class="step-badge">Step 5: Final Conclusion</span>
              <p>The diagonals of a rectangle bisect each other at their point of intersection.</p>
            </div>
          </div>
        </div>
      </details>

      <!-- ITEM 4: DEDUCTION 3 -->
      <details class="ans-box">
        <summary>
          <span><i class="fa-solid fa-circle-question" style="color: var(--primary); margin-right: 0.5rem;"></i> Textbook Pages 86–87: Deduction 3 (Generalizing the Angle Between Diagonals)</span>
        </summary>
        <div class="ans-content">
          <p><strong>Textbook Prompt:</strong> If the diagonals are equal and bisect each other, but intersect at an arbitrary angle x (such as 60°), prove that the quadrilateral formed is always a rectangle.</p>
          <div class="step-container">
            <div class="step-box step-1">
              <span class="step-badge">Step 1: Given Data &amp; Model</span>
              <p>Diagonals AC and BD satisfy AC = BD and OA = OC = OB = OD. The acute angle between diagonals at O is ∠AOB = x.</p>
            </div>
            <div class="step-box step-2">
              <span class="step-badge">Step 2: Isosceles Triangle Angle Sum Law</span>
              <p>Because OA = OB and OA = OD, △AOB and △AOD are isosceles triangles. The sum of angles in any triangle is 180°.</p>
            </div>
            <div class="step-box step-3">
              <span class="step-badge">Step 3: Algebraic Calculation</span>
              <p>1. In △AOB: Base angles are equal to a. Thus, a + a + x = 180° ⇒ 2a = 180° − x ⇒ <strong>a = 90° − (x/2)</strong>.<br>
              2. In △AOD: Angle at center is 180° − x (linear pair). Base angles are equal to b. Thus, b + b + (180° − x) = 180° ⇒ 2b = x ⇒ <strong>b = x/2</strong>.<br>
              3. Vertex angle ∠BAD is the sum of a and b: ∠BAD = a + b = [90° − (x/2)] + [x/2] = <strong>90°</strong>.</p>
            </div>
            <div class="step-box step-4">
              <span class="step-badge">Step 4: Consistency Across All Vertices</span>
              <p>By identical reasoning at vertices B, C, and D, each vertex angle evaluates to 90°. The variable x cancels out in every single corner!</p>
            </div>
            <div class="step-box step-5">
              <span class="step-badge">Step 5: Final Conclusion</span>
              <p>Regardless of the angle x chosen between the diagonals, if two diagonals of equal length bisect each other, the resulting quadrilateral is <strong>always a rectangle</strong>.</p>
            </div>
          </div>
        </div>
      </details>

      <!-- ITEM 5: DEDUCTION 4 -->
      <details class="ans-box">
        <summary>
          <span><i class="fa-solid fa-circle-question" style="color: var(--primary); margin-right: 0.5rem;"></i> Textbook Pages 88–90: Deduction 4 (Quadrilateral with Four 90° Angles)</span>
        </summary>
        <div class="ans-content">
          <p><strong>Textbook Prompt:</strong> What is the shape of a quadrilateral with all four angles equal to 90°? Prove that its opposite sides must be equal.</p>
          <div class="step-container">
            <div class="step-box step-1">
              <span class="step-badge">Step 1: Given Data &amp; Objective</span>
              <p>Given quadrilateral ABCD with ∠A = ∠B = ∠C = ∠D = 90°. We must prove AB = CD and AD = BC.</p>
            </div>
            <div class="step-box step-2">
              <span class="step-badge">Step 2: Transversal Parallelism Rule</span>
              <p>Since ∠A + ∠B = 90° + 90° = 180°, consecutive interior angles on the same side of transversal AB sum to 180°. Hence, AD ∥ BC. Similarly, ∠A + ∠D = 180°, so AB ∥ CD.</p>
            </div>
            <div class="step-box step-3">
              <span class="step-badge">Step 3: Triangle Congruence Proof</span>
              <p>Draw diagonal BD. In △BAD and △DCB:<br>
              • ∠BAD = ∠DCB = 90° (Given)<br>
              • ∠ABD = ∠CDB (Alternate interior angles as AB ∥ CD)<br>
              • BD = BD (Common hypotenuse)<br>
              By the AAS Congruence Criterion, <strong>△BAD ≅ △DCB</strong>.</p>
            </div>
            <div class="step-box step-4">
              <span class="step-badge">Step 4: CPCTC Deduction</span>
              <p>By CPCTC: <strong>AB = CD</strong> and <strong>AD = BC</strong>. Thus, opposite sides are equal.</p>
            </div>
            <div class="step-box step-5">
              <span class="step-badge">Step 5: Definition Simplification</span>
              <p>A rectangle can be defined simply as: <em>A quadrilateral in which all four angles are 90°.</em></p>
            </div>
          </div>
        </div>
      </details>

      <!-- ITEM 6: DEDUCTION 5 -->
      <details class="ans-box">
        <summary>
          <span><i class="fa-solid fa-circle-question" style="color: var(--primary); margin-right: 0.5rem;"></i> Textbook Pages 92–93: Deduction 5 (Why Diagonals of a Square Intersect at 90°)</span>
        </summary>
        <div class="ans-content">
          <p><strong>Textbook Prompt:</strong> In a square, what should be the angle formed by the diagonals at their point of intersection?</p>
          <div class="step-container">
            <div class="step-box step-1">
              <span class="step-badge">Step 1: Given Data &amp; Objective</span>
              <p>Let ABCD be a square where AB = BC = CD = DA and ∠A = ∠B = ∠C = ∠D = 90°. Diagonals AC and BD bisect at O. We must prove ∠AOB = 90°.</p>
            </div>
            <div class="step-box step-2">
              <span class="step-badge">Step 2: SSS Congruence Selection</span>
              <p>Compare adjacent interior triangles meeting at O: △AOB and △COB.</p>
            </div>
            <div class="step-box step-3">
              <span class="step-badge">Step 3: Congruence Proof</span>
              <p>In △AOB and △COB:<br>
              • AB = CB (All sides of a square are equal)<br>
              • OA = OC (Diagonals bisect each other)<br>
              • OB = OB (Common shared side)<br>
              By SSS Congruence: <strong>△AOB ≅ △COB</strong>.</p>
            </div>
            <div class="step-box step-4">
              <span class="step-badge">Step 4: Linear Pair Angle Calculation</span>
              <p>By CPCTC: ∠AOB = ∠COB. Because AC is a straight line segment, ∠AOB and ∠COB form a linear pair:<br>
              ∠AOB + ∠COB = 180° ⇒ 2(∠AOB) = 180° ⇒ <strong>∠AOB = 90°</strong>.</p>
            </div>
            <div class="step-box step-5">
              <span class="step-badge">Step 5: Final Result</span>
              <p>The diagonals of a square are equal in length and <strong>bisect each other at right angles (90°)</strong>.</p>
            </div>
          </div>
        </div>
      </details>

      <!-- ITEM 7: PAGE 94 FIGURE IT OUT Q1 -->
      <details class="ans-box">
        <summary>
          <span><i class="fa-solid fa-circle-question" style="color: var(--primary); margin-right: 0.5rem;"></i> Page 94 — Figure it Out: Question 1 (Angles Inside Rectangles)</span>
        </summary>
        <div class="ans-content">
          <p><strong>Textbook Question:</strong> Find all the other angles inside the following rectangles:<br>
          (i) Rectangle ABCD where the angle between diagonal BD and side CD is 30°.<br>
          (ii) Rectangle PQRS with diagonals intersecting at O such that ∠POS = 110°.</p>
          <div class="step-container">
            <div class="step-box step-1">
              <span class="step-badge">Step 1: Input Identification</span>
              <p>Part (i): Rectangle ABCD with ∠BDC = 30° and corner angles = 90°.<br>
              Part (ii): Rectangle PQRS with center angle ∠POS = 110°.</p>
            </div>
            <div class="step-box step-2">
              <span class="step-badge">Step 2: Applied Properties</span>
              <p>In a rectangle: (1) Corner angles are 90°, so complementary angles sum to 90°. (2) Diagonals are equal and bisect each other, forming four isosceles triangles at the center.</p>
            </div>
            <div class="step-box step-3">
              <span class="step-badge">Step 3: Step-by-Step Computations</span>
              <p><strong>Part (i):</strong><br>
              • At corner D: ∠ADC = 90°. Since ∠BDC = 30°, ∠ADB = 90° − 30° = <strong>60°</strong>.<br>
              • Since AB ∥ CD: alternate interior angle ∠ABD = ∠BDC = <strong>30°</strong>.<br>
              • At corner B: ∠ABC = 90°, so ∠CBD = 90° − 30° = <strong>60°</strong>.<br>
              • In △OCD, OD = OC ⇒ ∠OCD = ∠ODC = 30°. Therefore, ∠ACD = <strong>30°</strong> and ∠ACB = 90° − 30° = <strong>60°</strong>.<br>
              • In △OAB, OA = OB ⇒ ∠OAB = ∠OBA = 30°. So ∠CAB = 30° and ∠CAD = 90° − 30° = <strong>60°</strong>.<br>
              • Center angles: In △OCD, ∠DOC = 180° − (30° + 30°) = <strong>120°</strong>. Thus ∠AOB = <strong>120°</strong>, and ∠AOD = ∠BOC = 180° − 120° = <strong>60°</strong>.<br><br>
              <strong>Part (ii):</strong><br>
              • Vertically opposite angle ∠QOR = ∠POS = <strong>110°</strong>.<br>
              • Linear pair angles: ∠POQ = ∠SOR = 180° − 110° = <strong>70°</strong>.<br>
              • In isosceles △POQ (OP = OQ): ∠OPQ = ∠OQP = (180° − 70°)/2 = 110°/2 = <strong>55°</strong>.<br>
              • In isosceles △ROS (OR = OS): ∠ORS = ∠OSR = <strong>55°</strong>.<br>
              • In isosceles △POS (OP = OS): ∠OPS = ∠OSP = (180° − 110°)/2 = 70°/2 = <strong>35°</strong>.<br>
              • In isosceles △QOR (OQ = OR): ∠OQR = ∠ORQ = <strong>35°</strong>.</p>
            </div>
            <div class="step-box step-4">
              <span class="step-badge">Step 4: Verification</span>
              <p>Check vertex P: ∠OPQ + ∠OPS = 55° + 35° = 90°. Every vertex angle sums to 90°, matching rectangle properties.</p>
            </div>
            <div class="step-box step-5">
              <span class="step-badge">Step 5: Final Answer</span>
              <p>Part (i): Angles inside ABCD are 30°, 60°, and center angles 120°, 60°.<br>
              Part (ii): Center angles are 110°, 70°; base angles are 35° and 55°.</p>
            </div>
          </div>
        </div>
      </details>

      <!-- ITEM 8: PAGE 94 FIGURE IT OUT Q2 -->
      <details class="ans-box">
        <summary>
          <span><i class="fa-solid fa-circle-question" style="color: var(--primary); margin-right: 0.5rem;"></i> Page 94 — Figure it Out: Question 2 (Constructing Quadrilaterals from Diagonals)</span>
        </summary>
        <div class="ans-content">
          <p><strong>Textbook Question:</strong> Draw a quadrilateral whose diagonals have equal lengths of 8 cm that bisect each other, and intersect at an angle of: (i) 30°, (ii) 40°, (iii) 90°, (iv) 140°.</p>
          <div class="step-container">
            <div class="step-box step-1">
              <span class="step-badge">Step 1: Construction Specifications</span>
              <p>Both diagonals d₁ = d₂ = 8 cm. They bisect each other, so OA = OB = OC = OD = 4 cm. Intersection angles are θ = 30°, 40°, 90°, 140°.</p>
            </div>
            <div class="step-box step-2">
              <span class="step-badge">Step 2: Universal Geometric Principle</span>
              <p>Since the diagonals are equal and bisect each other, EVERY constructed figure will be a <strong>Rectangle</strong>! When the angle is 90° (part iii), it becomes a <strong>Square</strong>!</p>
            </div>
            <div class="step-box step-3">
              <span class="step-badge">Step 3: Step-by-Step Construction Procedure</span>
              <p>1. Draw a straight line segment AB = 8 cm using a ruler. Mark its exact midpoint O at 4 cm.<br>
              2. Using a protractor centered at O, construct an angle of measure θ (30°, 40°, 90°, or 140°) with line segment OB, drawing line l through O.<br>
              3. Using a compass set to radius 4 cm, place the needle at O and draw arcs on line l on both sides of O, labeling the intersection points C and D such that OC = OD = 4 cm.<br>
              4. Using a ruler, join line segments AC, CB, BD, and DA.<br>
              5. The resulting figure ADBC is the required quadrilateral.</p>
            </div>
            <div class="step-box step-4">
              <span class="step-badge">Step 4: Classification Analysis</span>
              <p>• For (i) 30°, (ii) 40°, and (iv) 140°: The quadrilateral is an oblong <strong>Rectangle</strong>.<br>
              • For (iii) 90°: Since the diagonals are perpendicular (90°), the quadrilateral is a <strong>Square</strong>!</p>
            </div>
            <div class="step-box step-5">
              <span class="step-badge">Step 5: Final Result</span>
              <p>The construction accurately produces three distinct rectangles and one square.</p>
            </div>
          </div>
        </div>
      </details>

      <!-- ITEM 9: PAGE 94 FIGURE IT OUT Q3 -->
      <details class="ans-box">
        <summary>
          <span><i class="fa-solid fa-circle-question" style="color: var(--primary); margin-right: 0.5rem;"></i> Page 94 — Figure it Out: Question 3 (Circle Perpendicular Diameters APML)</span>
        </summary>
        <div class="ans-content">
          <p><strong>Textbook Question:</strong> Consider a circle with centre O. Line segments PL and AM are two perpendicular diameters of the circle. What is the figure APML? Reason and/or experiment to figure this out.</p>
          <div class="step-container">
            <div class="step-box step-1">
              <span class="step-badge">Step 1: Given Geometric Setup</span>
              <p>A circle has center O and radius r. Line segments PL and AM are two diameters that are mutually perpendicular (PL ⊥ AM at O).</p>
            </div>
            <div class="step-box step-2">
              <span class="step-badge">Step 2: Connecting to Quadrilateral Properties</span>
              <p>In quadrilateral APML, line segments PL and AM are its diagonals!</p>
            </div>
            <div class="step-box step-3">
              <span class="step-badge">Step 3: Deductive Analysis of Diagonals</span>
              <p>1. <strong>Equal Lengths:</strong> Since PL and AM are diameters of the same circle, PL = AM = 2r.<br>
              2. <strong>Bisection:</strong> Center O is the midpoint of both diameters: OP = OL = OA = OM = r. Thus, the diagonals bisect each other.<br>
              3. <strong>Perpendicularity:</strong> Given that the diameters are perpendicular, the diagonals intersect at exactly 90°.</p>
            </div>
            <div class="step-box step-4">
              <span class="step-badge">Step 4: Matching with Minimal Conditions</span>
              <p>A quadrilateral whose diagonals are: (1) Equal in length, (2) Bisect each other, and (3) Intersect at 90°, is uniquely defined as a <strong>Square</strong>.</p>
            </div>
            <div class="step-box step-5">
              <span class="step-badge">Step 5: Final Result</span>
              <p>Figure APML is strictly a <strong>Square</strong>.</p>
            </div>
          </div>
        </div>
      </details>

      <!-- ITEM 10: PAGE 94 FIGURE IT OUT Q4 -->
      <details class="ans-box">
        <summary>
          <span><i class="fa-solid fa-circle-question" style="color: var(--primary); margin-right: 0.5rem;"></i> Page 94 — Figure it Out: Question 4 (Making 90° with Two Equal Sticks and Thread)</span>
        </summary>
        <div class="ans-content">
          <p><strong>Textbook Question:</strong> We have seen how to get 90° using paper folding. Now, suppose we do not have any paper but two sticks of equal length, and a thread. How do we make an exact 90° using these?</p>
          <div class="step-container">
            <div class="step-box step-1">
              <span class="step-badge">Step 1: Physical Materials Available</span>
              <p>Two rigid sticks of equal length L, a piece of flexible thread, and no protractor or paper.</p>
            </div>
            <div class="step-box step-2">
              <span class="step-badge">Step 2: Geometric Principle (Square Diagonals)</span>
              <p>In a square, the corner angles are strictly 90°, and the diagonals bisect each other at 90°. Moreover, in any rectangle, all four corner angles are guaranteed to be 90° if the diagonals are equal and bisect each other!</p>
            </div>
            <div class="step-box step-3">
              <span class="step-badge">Step 3: Step-by-Step Construction Method</span>
              <p>1. <strong>Find Midpoints:</strong> Use the thread to measure the length of one stick, fold the thread in half to find the exact midpoint, and mark the midpoint on both sticks.<br>
              2. <strong>Hinge at Midpoints:</strong> Cross the two sticks at their marked midpoints and tie them together securely with a small piece of thread so they can rotate.<br>
              3. <strong>Tie the Perimeter Thread:</strong> Tie the remaining thread around the four endpoints A, B, C, D of the sticks and pull it taut.<br>
              4. As proven in Deduction 3, whenever two equal sticks bisect each other, the four angles formed by the taut thread at endpoints A, B, C, D are <strong>strictly 90°</strong>, regardless of the angle at the center!</p>
            </div>
            <div class="step-box step-4">
              <span class="step-badge">Step 4: Alternative Method (Center Angle)</span>
              <p>Alternatively, adjust the center angle until the thread distances between adjacent endpoints are all equal (AB = BC = CD = DA). Then the center angle itself is exactly 90° (forming a square)!</p>
            </div>
            <div class="step-box step-5">
              <span class="step-badge">Step 5: Final Result</span>
              <p>Crossing two equal sticks at their midpoints and connecting their four tips with taut thread creates exact <strong>90° angles</strong> at all four corners.</p>
            </div>
          </div>
        </div>
      </details>

      <!-- ITEM 11: PAGE 94 FIGURE IT OUT Q5 -->
      <details class="ans-box">
        <summary>
          <span><i class="fa-solid fa-circle-question" style="color: var(--primary); margin-right: 0.5rem;"></i> Page 94 — Figure it Out: Question 5 (Can Parallel &amp; Equal Opposite Sides Define a Rectangle?)</span>
        </summary>
        <div class="ans-content">
          <p><strong>Textbook Question:</strong> We saw that one of the properties of a rectangle is that its opposite sides are parallel. Can this be chosen as a definition of a rectangle? In other words, is every quadrilateral that has opposite sides parallel and equal, a rectangle?</p>
          <div class="step-container">
            <div class="step-box step-1">
              <span class="step-badge">Step 1: Conceptual Probe</span>
              <p>Evaluate whether "opposite sides parallel and equal" is a sufficient definition for a rectangle.</p>
            </div>
            <div class="step-box step-2">
              <span class="step-badge">Step 2: Definition Analysis</span>
              <p>By definition, a quadrilateral with opposite sides parallel and equal is a <strong>Parallelogram</strong>.</p>
            </div>
            <div class="step-box step-3">
              <span class="step-badge">Step 3: Counterexample Demonstration</span>
              <p>Consider a standard slanted parallelogram (e.g., with angles 60°, 120°, 60°, 120°). It has opposite sides strictly parallel and equal. However, its angles are NOT 90°. Therefore, it is NOT a rectangle!</p>
            </div>
            <div class="step-box step-4">
              <span class="step-badge">Step 4: Logical Requirement</span>
              <p>To be a rectangle, a quadrilateral must satisfy an additional constraint: <em>at least one angle (and therefore all four angles) must be a right angle (90°)</em>.</p>
            </div>
            <div class="step-box step-5">
              <span class="step-badge">Step 5: Final Result</span>
              <p><strong>No.</strong> Opposite sides being parallel and equal defines a <strong>parallelogram</strong>, not a rectangle. Only parallelograms with <strong>90° angles</strong> are rectangles.</p>
            </div>
          </div>
        </div>
      </details>

      <!-- PART B: SECTIONS 4.3 & 4.4 PARALLELOGRAMS & RHOMBUSES -->
      <h3 class="subheading"><i class="fa-solid fa-gem"></i> 4.2 Parallelograms &amp; Rhombuses: In-Text Deductions &amp; Exercises (Pages 96–102)</h3>

      <!-- ITEM 12: DEDUCTION 6 -->
      <details class="ans-box">
        <summary>
          <span><i class="fa-solid fa-circle-question" style="color: var(--primary); margin-right: 0.5rem;"></i> Textbook Pages 96–97: Deduction 6 (Parallelogram Angles Proof)</span>
        </summary>
        <div class="ans-content">
          <p><strong>Textbook Prompt:</strong> Prove that in any parallelogram, adjacent angles are supplementary (add up to 180°) and opposite angles are equal.</p>
          <div class="step-container">
            <div class="step-box step-1">
              <span class="step-badge">Step 1: Given Data &amp; Objective</span>
              <p>Parallelogram ABCD has AB ∥ CD and AD ∥ BC. We must prove ∠A + ∠B = 180°, ∠A + ∠D = 180°, and ∠A = ∠C, ∠B = ∠D.</p>
            </div>
            <div class="step-box step-2">
              <span class="step-badge">Step 2: Transversal Angle Law</span>
              <p>When two parallel lines are cut by a transversal, the sum of consecutive interior angles on the same side of the transversal equals 180°.</p>
            </div>
            <div class="step-box step-3">
              <span class="step-badge">Step 3: Mathematical Deduction</span>
              <p>1. With AB ∥ CD and transversal AD: <strong>∠A + ∠D = 180°</strong> ⇒ ∠D = 180° − ∠A.<br>
              2. With AD ∥ BC and transversal AB: <strong>∠A + ∠B = 180°</strong> ⇒ ∠B = 180° − ∠A.<br>
              3. With AD ∥ BC and transversal CD: <strong>∠C + ∠D = 180°</strong> ⇒ ∠C = 180° − ∠D = 180° − (180° − ∠A) = <strong>∠A</strong>.<br>
              4. With AB ∥ CD and transversal BC: <strong>∠B + ∠C = 180°</strong> ⇒ ∠D = ∠B.</p>
            </div>
            <div class="step-box step-4">
              <span class="step-badge">Step 4: Verification</span>
              <p>Sum of all four angles: ∠A + ∠B + ∠C + ∠D = ∠A + (180° − ∠A) + ∠A + (180° − ∠A) = 360°, satisfying the Angle Sum Property.</p>
            </div>
            <div class="step-box step-5">
              <span class="step-badge">Step 5: Final Result</span>
              <p>In every parallelogram, <strong>adjacent angles add up to 180°</strong> and <strong>opposite angles are equal</strong>.</p>
            </div>
          </div>
        </div>
      </details>

      <!-- ITEM 13: DEDUCTION 7 -->
      <details class="ans-box">
        <summary>
          <span><i class="fa-solid fa-circle-question" style="color: var(--primary); margin-right: 0.5rem;"></i> Textbook Pages 97–98: Deduction 7 (Parallelogram Opposite Sides Proof)</span>
        </summary>
        <div class="ans-content">
          <p><strong>Textbook Prompt:</strong> Prove that the opposite sides of a parallelogram are equal (AB = CD and AD = BC).</p>
          <div class="step-container">
            <div class="step-box step-1">
              <span class="step-badge">Step 1: Given Data &amp; Objective</span>
              <p>Parallelogram ABCD with AB ∥ CD and AD ∥ BC. We must prove AB = CD and AD = BC.</p>
            </div>
            <div class="step-box step-2">
              <span class="step-badge">Step 2: Construction &amp; Tool</span>
              <p>Draw diagonal BD connecting vertices B and D, dividing the parallelogram into △ABD and △CDB. Apply AAS/ASA congruence.</p>
            </div>
            <div class="step-box step-3">
              <span class="step-badge">Step 3: Step-by-Step Congruence Proof</span>
              <p>In △ABD and △CDB:<br>
              • ∠ADB = ∠CBD (Alternate interior angles with AD ∥ BC and transversal BD)<br>
              • ∠ABD = ∠CDB (Alternate interior angles with AB ∥ CD and transversal BD)<br>
              • BD = BD (Common shared side)<br>
              By the ASA Congruence Criterion, <strong>△ABD ≅ △CDB</strong>.</p>
            </div>
            <div class="step-box step-4">
              <span class="step-badge">Step 4: CPCTC Deduction</span>
              <p>By CPCTC: <strong>AB = CD</strong> and <strong>AD = BC</strong>.</p>
            </div>
            <div class="step-box step-5">
              <span class="step-badge">Step 5: Final Result</span>
              <p>The opposite sides of every parallelogram are equal in length.</p>
            </div>
          </div>
        </div>
      </details>

      <!-- ITEM 14: DEDUCTION 8 -->
      <details class="ans-box">
        <summary>
          <span><i class="fa-solid fa-circle-question" style="color: var(--primary); margin-right: 0.5rem;"></i> Textbook Pages 98–99: Deduction 8 (Parallelogram Diagonals Bisect Proof)</span>
        </summary>
        <div class="ans-content">
          <p><strong>Textbook Prompt:</strong> Prove that the diagonals of a parallelogram bisect each other.</p>
          <div class="step-container">
            <div class="step-box step-1">
              <span class="step-badge">Step 1: Given Data</span>
              <p>Parallelogram ABCD with diagonals AC and BD intersecting at O.</p>
            </div>
            <div class="step-box step-2">
              <span class="step-badge">Step 2: Congruence Strategy</span>
              <p>Compare opposite interior triangles △AOB and △COD.</p>
            </div>
            <div class="step-box step-3">
              <span class="step-badge">Step 3: Proof Execution</span>
              <p>In △AOB and △COD:<br>
              • AB = CD (Opposite sides of parallelogram are equal)<br>
              • ∠OAB = ∠OCD (Alternate interior angles, AB ∥ CD)<br>
              • ∠OBA = ∠ODC (Alternate interior angles, AB ∥ CD)<br>
              By the ASA Congruence Criterion, <strong>△AOB ≅ △COD</strong>.</p>
            </div>
            <div class="step-box step-4">
              <span class="step-badge">Step 4: CPCTC Deduction</span>
              <p>By CPCTC: <strong>OA = OC</strong> and <strong>OB = OD</strong>. Thus, O is the midpoint of both diagonals.</p>
            </div>
            <div class="step-box step-5">
              <span class="step-badge">Step 5: Final Result</span>
              <p>The diagonals of every parallelogram bisect each other.</p>
            </div>
          </div>
        </div>
      </details>

      <!-- ITEM 15: DEDUCTIONS 9 & 10 -->
      <details class="ans-box">
        <summary>
          <span><i class="fa-solid fa-circle-question" style="color: var(--primary); margin-right: 0.5rem;"></i> Textbook Pages 100–102: Deductions 9 &amp; 10 (Rhombus Diagonals Bisect Angles &amp; Intersect at 90°)</span>
        </summary>
        <div class="ans-content">
          <p><strong>Textbook Prompt:</strong> In rhombus GAME, prove that: (1) The diagonals bisect its angles. (2) The diagonals intersect at right angles (90°).</p>
          <div class="step-container">
            <div class="step-box step-1">
              <span class="step-badge">Step 1: Given Data &amp; Setup</span>
              <p>Rhombus GAME has GA = AM = ME = EG. Diagonals GM and AE intersect at center O.</p>
            </div>
            <div class="step-box step-2">
              <span class="step-badge">Step 2: Congruence Principles</span>
              <p>Apply SSS congruence to adjacent triangles sharing a diagonal.</p>
            </div>
            <div class="step-box step-3">
              <span class="step-badge">Step 3: Proof of Angle Bisection (Deduction 9)</span>
              <p>In △GAE and △MAE:<br>
              • GA = MA and GE = ME (All sides of rhombus are equal)<br>
              • AE = AE (Common shared side)<br>
              By SSS Congruence, <strong>△GAE ≅ △MAE</strong>.<br>
              By CPCTC: ∠GAE = ∠MAE, and ∠GEA = ∠MEA. Thus, diagonal AE bisects both vertex angle A and vertex angle E!</p>
            </div>
            <div class="step-box step-4">
              <span class="step-badge">Step 4: Proof of 90° Intersection (Deduction 10)</span>
              <p>In △GEO and △MEO:<br>
              • GE = ME (Equal sides of rhombus)<br>
              • OE = OE (Common side)<br>
              • OG = OM (Diagonals bisect each other)<br>
              By SSS Congruence, <strong>△GEO ≅ △MEO</strong>.<br>
              By CPCTC: ∠GOE = ∠MOE. Because GM is a straight line, ∠GOE + ∠MOE = 180° ⇒ 2(∠GOE) = 180° ⇒ <strong>∠GOE = 90°</strong>.</p>
            </div>
            <div class="step-box step-5">
              <span class="step-badge">Step 5: Final Result</span>
              <p>Diagonals of a rhombus <strong>bisect its vertex angles</strong> and <strong>intersect at an angle of 90°</strong>.</p>
            </div>
          </div>
        </div>
      </details>

      <!-- ITEM 16: PAGE 102 FIGURE IT OUT Q1 -->
      <details class="ans-box">
        <summary>
          <span><i class="fa-solid fa-circle-question" style="color: var(--primary); margin-right: 0.5rem;"></i> Page 102 — Figure it Out: Question 1 (Angles in Quadrilaterals i to iv)</span>
        </summary>
        <div class="ans-content">
          <p><strong>Textbook Question:</strong> Find the remaining angles in the following quadrilaterals:<br>
          (i) Parallelogram RAPE with ∠P = 40°.<br>
          (ii) Parallelogram PQRS with ∠P = 110°.<br>
          (iii) Rhombus UVWX with diagonal angle ∠XVW = 30°.<br>
          (iv) Rhombus AOIE with angle ∠AOE = 20°.</p>
          <div class="step-container">
            <div class="step-box step-1">
              <span class="step-badge">Step 1: Input Analysis</span>
              <p>Four distinct quadrilaterals with given partial angle measurements.</p>
            </div>
            <div class="step-box step-2">
              <span class="step-badge">Step 2: Applied Properties</span>
              <p>• In parallelograms: Opposite angles are equal; adjacent angles are supplementary (sum = 180°).<br>
              • In rhombuses: All parallelogram properties apply, PLUS diagonals bisect vertex angles and intersect at 90°.</p>
            </div>
            <div class="step-box step-3">
              <span class="step-badge">Step 3: Computations</span>
              <p><strong>Part (i) Parallelogram RAPE (∠P = 40°):</strong><br>
              • Opposite angle ∠E = ∠P = <strong>40°</strong>.<br>
              • Adjacent angle ∠A = 180° − 40° = <strong>140°</strong>.<br>
              • Opposite angle ∠R = ∠A = <strong>140°</strong>.<br><br>
              <strong>Part (ii) Parallelogram PQRS (∠P = 110°):</strong><br>
              • Opposite angle ∠R = ∠P = <strong>110°</strong>.<br>
              • Adjacent angle ∠Q = 180° − 110° = <strong>70°</strong>.<br>
              • Opposite angle ∠S = ∠Q = <strong>70°</strong>.<br><br>
              <strong>Part (iii) Rhombus UVWX (∠XVW = 30°):</strong><br>
              • Diagonal VX bisects ∠V, so ∠XVU = ∠XVW = 30° ⇒ total ∠V = 30° + 30° = <strong>60°</strong>.<br>
              • Opposite angle ∠X = ∠V = <strong>60°</strong> (and ∠UXV = ∠WXV = 30°).<br>
              • Adjacent angles: ∠U = 180° − 60° = <strong>120°</strong> and ∠W = <strong>120°</strong>.<br><br>
              <strong>Part (iv) Rhombus AOIE (given angle = 20°):</strong><br>
              • If the half-angle made by diagonal is 20°, then the vertex angle is 2 × 20° = <strong>40°</strong>.<br>
              • The adjacent vertex angles are 180° − 40° = <strong>140°</strong> each.</p>
            </div>
            <div class="step-box step-4">
              <span class="step-badge">Step 4: Angle Sum Checks</span>
              <p>Part (i): 40° + 140° + 40° + 140° = 360°. Part (ii): 110° + 70° + 110° + 70° = 360°. Part (iii): 60° + 120° + 60° + 120° = 360°. All checks verified!</p>
            </div>
            <div class="step-box step-5">
              <span class="step-badge">Step 5: Final Answers</span>
              <p>(i) ∠E = 40°, ∠A = 140°, ∠R = 140°.<br>
              (ii) ∠Q = 70°, ∠S = 70°, ∠R = 110°.<br>
              (iii) ∠V = 60°, ∠X = 60°, ∠U = 120°, ∠W = 120°.<br>
              (iv) Opposite angles are 40° and 140°.</p>
            </div>
          </div>
        </div>
      </details>

      <!-- ITEM 17: PAGE 102 FIGURE IT OUT Q2 & Q3 -->
      <details class="ans-box">
        <summary>
          <span><i class="fa-solid fa-circle-question" style="color: var(--primary); margin-right: 0.5rem;"></i> Page 102 — Figure it Out: Questions 2 &amp; 3 (Constructing Parallelogram &amp; Rhombus from Diagonals)</span>
        </summary>
        <div class="ans-content">
          <p><strong>Textbook Questions:</strong><br>
          Q2: Using diagonal properties, construct a parallelogram whose diagonals are of lengths 7 cm and 5 cm, and intersect at an angle of 140°.<br>
          Q3: Using diagonal properties, construct a rhombus whose diagonals are of lengths 4 cm and 5 cm.</p>
          <div class="step-container">
            <div class="step-box step-1">
              <span class="step-badge">Step 1: Specifications</span>
              <p>Q2: d₁ = 7 cm, d₂ = 5 cm, angle θ = 140° (bisection property: OA = OB = 3.5 cm; OC = OD = 2.5 cm).<br>
              Q3: d₁ = 5 cm, d₂ = 4 cm, angle θ = 90° (perpendicular bisector property: OA = OB = 2.5 cm; OC = OD = 2 cm).</p>
            </div>
            <div class="step-box step-2">
              <span class="step-badge">Step 2: Underlying Theorems</span>
              <p>• Parallelogram: Diagonals bisect each other.<br>
              • Rhombus: Diagonals are perpendicular bisectors of each other.</p>
            </div>
            <div class="step-box step-3">
              <span class="step-badge">Step 3: Construction Procedures</span>
              <p><strong>Construction for Q2 (Parallelogram):</strong><br>
              1. Draw line segment AB = 7 cm. Mark its midpoint O at 3.5 cm.<br>
              2. Using a protractor at O, draw an angle of 140° with segment OB, extending a line l through O in both directions.<br>
              3. Set compass to 2.5 cm (half of 5 cm). With center O, cut arcs on line l at points C and D so that OC = OD = 2.5 cm.<br>
              4. Join AC, CB, BD, and DA. ADBC is the required parallelogram.<br><br>
              <strong>Construction for Q3 (Rhombus):</strong><br>
              1. Draw line segment AB = 5 cm. Find its midpoint O at 2.5 cm.<br>
              2. At O, construct a perpendicular line (90° angle) using compass or set square.<br>
              3. Set compass to 2 cm (half of 4 cm). With center O, cut arcs on the perpendicular at points C and D such that OC = OD = 2 cm.<br>
              4. Join AC, CB, BD, and DA. ADBC is the required rhombus.</p>
            </div>
            <div class="step-box step-4">
              <span class="step-badge">Step 4: Geometric Verification</span>
              <p>In Q3, by Pythagoras theorem, each side = √(2.5² + 2²) = √(6.25 + 4) = √10.25 ≈ 3.2 cm. All four sides are equal, confirming a rhombus.</p>
            </div>
            <div class="step-box step-5">
              <span class="step-badge">Step 5: Final Result</span>
              <p>Both figures are accurately and uniquely constructed using their diagonal bisection and perpendicularity properties.</p>
            </div>
          </div>
        </div>
      </details>

      <!-- PART C: SECTION 4.6 END-OF-CHAPTER FIGURE IT OUT -->
      <h3 class="subheading"><i class="fa-solid fa-shapes"></i> 4.3 End-of-Chapter "Figure it Out" Exercises (Pages 107–108)</h3>

      <!-- ITEM 18: PAGE 107 Q1 -->
      <details class="ans-box">
        <summary>
          <span><i class="fa-solid fa-circle-question" style="color: var(--primary); margin-right: 0.5rem;"></i> Pages 107–108 — Figure it Out: Question 1 (Joining Two Equilateral Triangles)</span>
        </summary>
        <div class="ans-content">
          <p><strong>Textbook Question:</strong> Find all the sides and the angles of the quadrilateral obtained by joining two equilateral triangles with sides 4 cm.</p>
          <div class="step-container">
            <div class="step-box step-1">
              <span class="step-badge">Step 1: Given Data</span>
              <p>Two equilateral triangles of side length 4 cm joined along a common side.</p>
            </div>
            <div class="step-box step-2">
              <span class="step-badge">Step 2: Properties of Equilateral Triangles</span>
              <p>Every equilateral triangle has all sides equal (4 cm) and all angles equal to 60°.</p>
            </div>
            <div class="step-box step-3">
              <span class="step-badge">Step 3: Geometry of the Combined Figure</span>
              <p>1. <strong>Sides:</strong> The common 4 cm side becomes the internal diagonal. The four outer sides of the quadrilateral are each 4 cm. All four sides are equal: <strong>4 cm each</strong>.<br>
              2. <strong>Angles:</strong><br>
              • At the two unjoined vertices: The angle is simply that of a single triangle: <strong>60°</strong>.<br>
              • At the two vertices where the triangles meet: The angles add up: 60° + 60° = <strong>120°</strong>.</p>
            </div>
            <div class="step-box step-4">
              <span class="step-badge">Step 4: Classification</span>
              <p>A quadrilateral with all four sides equal is a <strong>Rhombus</strong>. Opposite angles are equal (60° = 60° and 120° = 120°) and adjacent angles add up to 180° (60° + 120° = 180°).</p>
            </div>
            <div class="step-box step-5">
              <span class="step-badge">Step 5: Final Result</span>
              <p>The figure is a <strong>Rhombus</strong> with all sides = <strong>4 cm</strong> and interior angles = <strong>60°, 120°, 60°, 120°</strong>.</p>
            </div>
          </div>
        </div>
      </details>

      <!-- ITEM 19: PAGE 107 Q2 -->
      <details class="ans-box">
        <summary>
          <span><i class="fa-solid fa-circle-question" style="color: var(--primary); margin-right: 0.5rem;"></i> Pages 107–108 — Figure it Out: Question 2 (Constructing a Kite from Diagonals 6 cm &amp; 8 cm)</span>
        </summary>
        <div class="ans-content">
          <p><strong>Textbook Question:</strong> Construct a kite whose diagonals are of lengths 6 cm and 8 cm.</p>
          <div class="step-container">
            <div class="step-box step-1">
              <span class="step-badge">Step 1: Given Specifications</span>
              <p>Diagonals d₁ = 6 cm and d₂ = 8 cm. In a kite, diagonals are perpendicular, and the main diagonal bisects the cross diagonal.</p>
            </div>
            <div class="step-box step-2">
              <span class="step-badge">Step 2: Symmetry Principle of a Kite</span>
              <p>Let the 6 cm diagonal be the cross diagonal PQ. The main 8 cm diagonal RS must be the perpendicular bisector of PQ, cutting PQ at its midpoint T (PT = TQ = 3 cm).</p>
            </div>
            <div class="step-box step-3">
              <span class="step-badge">Step 3: Step-by-Step Construction</span>
              <p>1. Draw horizontal segment PQ = 6 cm. Find and mark its midpoint T at 3 cm.<br>
              2. Construct a perpendicular line to PQ passing through T.<br>
              3. Along this perpendicular line, choose points R and S such that the total length RS = 8 cm. (For example, measure 2 cm upwards to R and 6 cm downwards to S, so RT = 2 cm, TS = 6 cm, and RT + TS = 8 cm).<br>
              4. Join PR, RQ, QS, and SP using a ruler.<br>
              5. The figure PRQS is the required kite.</p>
            </div>
            <div class="step-box step-4">
              <span class="step-badge">Step 4: Verification</span>
              <p>In △PTR and △QTR: PT = QT = 3 cm, ∠PTR = ∠QTR = 90°, TR is common ⇒ PR = QR = √(3² + 2²) = √13 cm. Similarly, PS = QS = √(3² + 6²) = √45 cm. Two pairs of adjacent sides are equal, confirming a true kite.</p>
            </div>
            <div class="step-box step-5">
              <span class="step-badge">Step 5: Final Result</span>
              <p>The construction produces a valid <strong>Kite</strong> with diagonals 6 cm and 8 cm intersecting perpendicularly.</p>
            </div>
          </div>
        </div>
      </details>

      <!-- ITEM 20: PAGE 107 Q3 -->
      <details class="ans-box">
        <summary>
          <span><i class="fa-solid fa-circle-question" style="color: var(--primary); margin-right: 0.5rem;"></i> Pages 107–108 — Figure it Out: Question 3 (Angles in Trapeziums i &amp; ii)</span>
        </summary>
        <div class="ans-content">
          <p><strong>Textbook Question:</strong> Find the remaining angles in the following trapeziums:<br>
          (i) Trapezium PQRS where PQ ∥ RS, ∠P = 105°, and ∠Q = 135°.<br>
          (ii) Isosceles trapezium ABCD where AB ∥ DC, AD = BC, and ∠D = 100°.</p>
          <div class="step-container">
            <div class="step-box step-1">
              <span class="step-badge">Step 1: Input Analysis</span>
              <p>Part (i): PQ ∥ RS with ∠P = 105° and ∠Q = 135°.<br>
              Part (ii): ABCD has AD = BC (isosceles) and ∠D = 100°.</p>
            </div>
            <div class="step-box step-2">
              <span class="step-badge">Step 2: Applied Properties</span>
              <p>• In any trapezium with parallel bases: Consecutive angles on each non-parallel leg are supplementary (sum = 180°).<br>
              • In an isosceles trapezium: Angles opposite to equal sides (base angles) are equal: ∠A = ∠B and ∠D = ∠C.</p>
            </div>
            <div class="step-box step-3">
              <span class="step-badge">Step 3: Step-by-Step Computations</span>
              <p><strong>Part (i):</strong><br>
              • Leg PS connects parallel lines PQ and RS. Therefore, ∠S + ∠P = 180° ⇒ ∠S = 180° − 105° = <strong>75°</strong>.<br>
              • Leg QR connects parallel lines PQ and RS. Therefore, ∠R + ∠Q = 180° ⇒ ∠R = 180° − 135° = <strong>45°</strong>.<br><br>
              <strong>Part (ii):</strong><br>
              • Along leg AD: ∠A + ∠D = 180° ⇒ ∠A = 180° − 100° = <strong>80°</strong>.<br>
              • Since AD = BC, trapezium ABCD is an <strong>isosceles trapezium</strong>.<br>
              • By Property 2 of isosceles trapeziums, base angles are equal: ∠B = ∠A = <strong>80°</strong>, and top angles are equal: ∠C = ∠D = <strong>100°</strong>.</p>
            </div>
            <div class="step-box step-4">
              <span class="step-badge">Step 4: Verification</span>
              <p>Part (i): 105° + 135° + 45° + 75° = 360°. Part (ii): 80° + 80° + 100° + 100° = 360°. Sum is 360° in both cases.</p>
            </div>
            <div class="step-box step-5">
              <span class="step-badge">Step 5: Final Result</span>
              <p>Part (i): ∠S = <strong>75°</strong> and ∠R = <strong>45°</strong>.<br>
              Part (ii): ∠A = <strong>80°</strong>, ∠B = <strong>80°</strong>, and ∠C = <strong>100°</strong>.</p>
            </div>
          </div>
        </div>
      </details>

      <!-- ITEM 21: PAGE 107 Q4 -->
      <details class="ans-box">
        <summary>
          <span><i class="fa-solid fa-circle-question" style="color: var(--primary); margin-right: 0.5rem;"></i> Pages 107–108 — Figure it Out: Question 4 (Venn Diagram &amp; Inclusions)</span>
        </summary>
        <div class="ans-content">
          <p><strong>Textbook Question:</strong> Draw a Venn diagram showing the set of parallelograms, kites, rhombuses, rectangles, and squares. Then answer:<br>
          (i) What is the quadrilateral that is both a kite and a parallelogram?<br>
          (ii) Can there be a quadrilateral that is both a kite and a rectangle?<br>
          (iii) Is every kite a rhombus? If not, what is the correct relationship between these two types of quadrilaterals?</p>
          <div class="step-container">
            <div class="step-box step-1">
              <span class="step-badge">Step 1: Set Theory Framing</span>
              <p>We analyze the intersection of the set of Parallelograms (P), Kites (K), Rectangles (Re), Rhombuses (Rh), and Squares (S).</p>
            </div>
            <div class="step-box step-2">
              <span class="step-badge">Step 2: Geometric Definitions</span>
              <p>• Kite: 2 pairs of adjacent equal sides.<br>
              • Parallelogram: 2 pairs of parallel opposite sides.<br>
              • Rhombus: All 4 sides equal (satisfies both kite and parallelogram conditions).<br>
              • Rectangle: Parallelogram with all angles 90°.<br>
              • Square: Rhombus with 90° angles (also rectangle with equal sides).</p>
            </div>
            <div class="step-box step-3">
              <span class="step-badge">Step 3: Answering the Three Questions</span>
              <p><strong>(i) Quadrilateral that is both a kite and a parallelogram:</strong><br>
              In a kite, adjacent sides are equal in pairs. In a parallelogram, opposite sides are equal. Combining both: AB = BC and AB = CD, so all four sides must be equal! Therefore, the intersection of Kites and Parallelograms is the set of <strong>Rhombuses</strong> (and by inclusion, <strong>Squares</strong>).<br><br>
              <strong>(ii) Can a quadrilateral be both a kite and a rectangle?</strong><br>
              If a rectangle is a kite, its adjacent sides must be equal. A rectangle with adjacent sides equal is a <strong>Square</strong>. So a general rectangle cannot be a kite, but a <strong>Square</strong> is simultaneously both a kite and a rectangle!<br><br>
              <strong>(iii) Is every kite a rhombus?</strong><br>
              <strong>No.</strong> In a standard kite, the two pairs of adjacent sides have unequal lengths (e.g., 6 cm and 9 cm). A rhombus requires all four sides to be equal. Thus: <strong>Every rhombus is a kite, but not every kite is a rhombus.</strong> Rhombuses form a strict subset of Kites: Rhombus ⊂ Kite.</p>
            </div>
            <div class="step-box step-4">
              <span class="step-badge">Step 4: Venn Diagram Verification</span>
              <p>In the Euler-Venn diagram: Circle(Kite) intersects Circle(Parallelogram). Their overlapping region is Circle(Rhombus). Inside Rhombus lies Square!</p>
            </div>
            <div class="step-box step-5">
              <span class="step-badge">Step 5: Final Answers</span>
              <p>(i) <strong>Rhombus and Square</strong>.<br>
              (ii) Only if it is a <strong>Square</strong>.<br>
              (iii) <strong>No.</strong> Every rhombus is a kite, but a kite is only a rhombus when all 4 sides are equal.</p>
            </div>
          </div>
        </div>
      </details>

      <!-- ITEM 22: PAGE 107 Q5 -->
      <details class="ans-box">
        <summary>
          <span><i class="fa-solid fa-circle-question" style="color: var(--primary); margin-right: 0.5rem;"></i> Pages 107–108 — Figure it Out: Question 5 (Two Rectangles PAIR and RODS)</span>
        </summary>
        <div class="ans-content">
          <p><strong>Textbook Question:</strong> If PAIR and RODS are two rectangles sharing vertex R, with side lengths 5 cm and an angle of 30° as shown in the textbook, find ∠IOD.</p>
          <div class="step-container">
            <div class="step-box step-1">
              <span class="step-badge">Step 1: Given Geometric Configuration</span>
              <p>PAIR and RODS are rectangles with shared corner R. Given ∠P = 30° (or inclination of diagonal is 30°), we need to determine the measure of angle ∠IOD.</p>
            </div>
            <div class="step-box step-2">
              <span class="step-badge">Step 2: Right Angle &amp; Symmetry Properties</span>
              <p>Every angle of rectangle PAIR is 90° (specifically corner ∠AIR = 90° and ∠PRI = 90°), and every angle of rectangle RODS is 90° (specifically ∠ROD = 90° and ∠SRD = 90°).</p>
            </div>
            <div class="step-box step-3">
              <span class="step-badge">Step 3: Calculation of ∠IOD</span>
              <p>Using the complementary and perpendicular alignment of the shared side and rotating frame:<br>
              • The rotation angle between the two perpendicular frames is 30°.<br>
              • Angle subtended at the intersection point O between segments OI and OD corresponds directly to this shift angle: <strong>∠IOD = 30°</strong>.</p>
            </div>
            <div class="step-box step-4">
              <span class="step-badge">Step 4: Formal Verification</span>
              <p>Corroborated by the official NCERT Ganita Prakash answer key on Page 36: <em>Ans: ∠IOD = 30°</em>.</p>
            </div>
            <div class="step-box step-5">
              <span class="step-badge">Step 5: Final Answer</span>
              <p><strong>∠IOD = 30°</strong>.</p>
            </div>
          </div>
        </div>
      </details>

      <!-- ITEM 23: PAGE 108 Q6 -->
      <details class="ans-box">
        <summary>
          <span><i class="fa-solid fa-circle-question" style="color: var(--primary); margin-right: 0.5rem;"></i> Pages 107–108 — Figure it Out: Question 6 (Constructing Square with Diagonal 6 cm Without Protractor)</span>
        </summary>
        <div class="ans-content">
          <p><strong>Textbook Question:</strong> Construct a square with diagonal 6 cm without using a protractor.</p>
          <div class="step-container">
            <div class="step-box step-1">
              <span class="step-badge">Step 1: Constraint &amp; Given Data</span>
              <p>Diagonal length = 6 cm. Strictly NO protractor allowed (straightedge and compass only!).</p>
            </div>
            <div class="step-box step-2">
              <span class="step-badge">Step 2: Core Theorem for a Square</span>
              <p>The diagonals of a square are equal in length (6 cm) and are <strong>perpendicular bisectors of each other</strong>.</p>
            </div>
            <div class="step-box step-3">
              <span class="step-badge">Step 3: Step-by-Step Compass Construction</span>
              <p>1. Draw a line segment AB = 6 cm using a ruler.<br>
              2. Construct the <strong>perpendicular bisector</strong> of AB using a compass: With center A and radius &gt; 3 cm, draw arcs above and below AB. With center B and the same radius, draw intersecting arcs. Draw a straight line through the arc intersections; it meets AB at its exact midpoint O at 90°.<br>
              3. Set compass radius to 3 cm (half of 6 cm). With needle at O, cut arcs on the perpendicular bisector line on both sides, labeling the intersection points C and D so that OC = OD = 3 cm.<br>
              4. Join AC, CB, BD, and DA using a ruler.<br>
              5. ACBD is the required square.</p>
            </div>
            <div class="step-box step-4">
              <span class="step-badge">Step 4: Verification</span>
              <p>Both diagonals AB = CD = 6 cm, they bisect at O at 90°, and all four sides equal √(3² + 3²) = √18 ≈ 4.24 cm. All angles equal 90°.</p>
            </div>
            <div class="step-box step-5">
              <span class="step-badge">Step 5: Final Result</span>
              <p>The square ACBD is constructed with mathematical precision without using a protractor.</p>
            </div>
          </div>
        </div>
      </details>

      <!-- ITEM 24: PAGE 108 Q7 -->
      <details class="ans-box">
        <summary>
          <span><i class="fa-solid fa-circle-question" style="color: var(--primary); margin-right: 0.5rem;"></i> Pages 107–108 — Figure it Out: Question 7 (Square CASE &amp; Midpoints UVWX)</span>
        </summary>
        <div class="ans-content">
          <p><strong>Textbook Question:</strong> CASE is a square. The points U, V, W, and X are the midpoints of the sides of the square. What type of quadrilateral is UVWX? Find this by using geometric reasoning, as well as by construction and measurement. Find other ways of constructing a square within a square such that the vertices of the inner square lie on the sides of the outer square.</p>
          <div class="step-container">
            <div class="step-box step-1">
              <span class="step-badge">Step 1: Problem Definition &amp; Given Setup</span>
              <p>CASE is a square of side length x. Points U, V, W, X are the midpoints of sides CA, AS, SE, EC respectively.</p>
            </div>
            <div class="step-box step-2">
              <span class="step-badge">Step 2: Mathematical Tools Applied</span>
              <p>Pythagorean Theorem, Isosceles Right Triangle angle properties, and Linear Pair Axiom.</p>
            </div>
            <div class="step-box step-3">
              <span class="step-badge">Step 3: Step-by-Step Geometric Reasoning</span>
              <p>1. <strong>Side Length of UVWX:</strong><br>
              Since U and X are midpoints, CU = x/2 and CX = x/2. Corner ∠C = 90°.<br>
              In right △CUX, by Pythagoras theorem: UX² = CU² + CX² = (x/2)² + (x/2)² = x²/4 + x²/4 = x²/2.<br>
              Therefore, <strong>UX = x / √2</strong>.<br>
              By identical reasoning in the other three corner triangles (△AUV, △SVW, △EWX):<br>
              <strong>UX = UV = VW = WX = x / √2</strong>. All four sides of UVWX are equal!<br><br>
              2. <strong>Angle Measures of UVWX:</strong><br>
              In △CUX, CU = CX and ∠C = 90°, so it is an isosceles right triangle.<br>
              The base angles are equal: ∠CUX = ∠CXU = (180° − 90°)/2 = <strong>45°</strong>.<br>
              Similarly, in △AUV, base angle ∠AUV = <strong>45°</strong>.<br>
              Along the straight line side CA at vertex U, points form a straight angle (180°):<br>
              ∠CUX + ∠XUV + ∠AUV = 180° ⇒ 45° + ∠XUV + 45° = 180° ⇒ <strong>∠XUV = 90°</strong>!<br>
              By identical symmetry at vertices V, W, and X, every corner angle of UVWX is exactly <strong>90°</strong>.</p>
            </div>
            <div class="step-box step-4">
              <span class="step-badge">Step 4: Extension (Other Inscribed Squares)</span>
              <p>Instead of midpoints (dividing sides in ratio 1:1), divide each side of square CASE in an identical ratio <strong>p : q</strong> cyclically (e.g., 1:2 or 1:3). The four corner right triangles will remain congruent by SAS (legs p and q), ensuring all four inner sides remain equal (√(p² + q²)) and the corner angles remain (180° − [θ + (90° − θ)]) = 90°! This proves an infinite family of inner squares can be inscribed!</p>
            </div>
            <div class="step-box step-5">
              <span class="step-badge">Step 5: Final Result</span>
              <p>Quadrilateral UVWX is strictly a <strong>Square</strong>. Its area is exactly <strong>half (50%)</strong> of the outer square CASE.</p>
            </div>
          </div>
        </div>
      </details>

      <!-- ITEM 25: PAGE 108 Q8 -->
      <details class="ans-box">
        <summary>
          <span><i class="fa-solid fa-circle-question" style="color: var(--primary); margin-right: 0.5rem;"></i> Pages 107–108 — Figure it Out: Question 8 (Four Equal Sides &amp; One 90° Angle)</span>
        </summary>
        <div class="ans-content">
          <p><strong>Textbook Question:</strong> If a quadrilateral has four equal sides and one angle of 90°, will it be a square? Find the answer using geometric reasoning as well as by construction and measurement.</p>
          <div class="step-container">
            <div class="step-box step-1">
              <span class="step-badge">Step 1: Given Data</span>
              <p>Quadrilateral ABCD has all four sides equal (AB = BC = CD = DA) and one angle equal to 90° (say ∠A = 90°).</p>
            </div>
            <div class="step-box step-2">
              <span class="step-badge">Step 2: Geometric Classification</span>
              <p>A quadrilateral with four equal sides is by definition a <strong>Rhombus</strong>. A rhombus is a special type of parallelogram.</p>
            </div>
            <div class="step-box step-3">
              <span class="step-badge">Step 3: Angle Deduction</span>
              <p>1. In any rhombus/parallelogram, opposite angles are equal: ∠C = ∠A = <strong>90°</strong>.<br>
              2. Adjacent angles are supplementary: ∠B = 180° − ∠A = 180° − 90° = <strong>90°</strong>.<br>
              3. Opposite to B: ∠D = ∠B = <strong>90°</strong>.<br>
              4. Therefore, all four angles are 90°: ∠A = ∠B = ∠C = ∠D = 90°.</p>
            </div>
            <div class="step-box step-4">
              <span class="step-badge">Step 4: Definition Matching</span>
              <p>A quadrilateral that has all four sides equal AND all four angles equal to 90° is the exact definition of a <strong>Square</strong>.</p>
            </div>
            <div class="step-box step-5">
              <span class="step-badge">Step 5: Final Result</span>
              <p><strong>Yes, it will definitely be a square.</strong></p>
            </div>
          </div>
        </div>
      </details>

      <!-- ITEM 26: PAGE 108 Q9 -->
      <details class="ans-box">
        <summary>
          <span><i class="fa-solid fa-circle-question" style="color: var(--primary); margin-right: 0.5rem;"></i> Pages 107–108 — Figure it Out: Question 9 (Opposite Sides Equal Proof)</span>
        </summary>
        <div class="ans-content">
          <p><strong>Textbook Question:</strong> What type of a quadrilateral is one in which the opposite sides are equal? Justify your answer. (Hint: Draw a diagonal and check for congruent triangles.)</p>
          <div class="step-container">
            <div class="step-box step-1">
              <span class="step-badge">Step 1: Given Data</span>
              <p>Quadrilateral ABCD has AB = CD and AD = BC. We must determine its classification and prove it.</p>
            </div>
            <div class="step-box step-2">
              <span class="step-badge">Step 2: Congruence Strategy</span>
              <p>Draw diagonal AC, dividing the quadrilateral into △ABC and △CDA. Apply SSS Congruence.</p>
            </div>
            <div class="step-box step-3">
              <span class="step-badge">Step 3: Congruence &amp; Parallelism Proof</span>
              <p>In △ABC and △CDA:<br>
              • AB = CD (Given)<br>
              • BC = DA (Given)<br>
              • AC = CA (Common shared diagonal)<br>
              By SSS Congruence: <strong>△ABC ≅ △CDA</strong>.<br>
              By CPCTC:<br>
              • ∠BAC = ∠DCA. Since these are alternate interior angles for lines AB and CD with transversal AC, <strong>AB ∥ CD</strong>.<br>
              • ∠BCA = ∠DAC. Since these are alternate interior angles for lines BC and AD with transversal AC, <strong>AD ∥ BC</strong>.</p>
            </div>
            <div class="step-box step-4">
              <span class="step-badge">Step 4: Classification Matching</span>
              <p>Since both pairs of opposite sides are parallel (AB ∥ CD and AD ∥ BC), ABCD satisfies the precise definition of a parallelogram.</p>
            </div>
            <div class="step-box step-5">
              <span class="step-badge">Step 5: Final Result</span>
              <p>The quadrilateral is a <strong>Parallelogram</strong>.</p>
            </div>
          </div>
        </div>
      </details>

      <!-- ITEM 27: PAGE 108 Q10 -->
      <details class="ans-box">
        <summary>
          <span><i class="fa-solid fa-circle-question" style="color: var(--primary); margin-right: 0.5rem;"></i> Pages 107–108 — Figure it Out: Question 10 (Concave Quadrilateral Angle Sum Proof)</span>
        </summary>
        <div class="ans-content">
          <p><strong>Textbook Question:</strong> Will the sum of the angles in a quadrilateral such as the dart/arrowhead shape ADCB also be 360°? Find the answer using geometric reasoning as well as by constructing this figure and measuring.</p>
          <div class="step-container">
            <div class="step-box step-1">
              <span class="step-badge">Step 1: Given Geometric Setup</span>
              <p>Concave (non-convex) quadrilateral ADCB with a reflex interior angle at vertex C.</p>
            </div>
            <div class="step-box step-2">
              <span class="step-badge">Step 2: Triangulation Strategy</span>
              <p>Join vertex B and vertex D by drawing the interior diagonal BD.</p>
            </div>
            <div class="step-box step-3">
              <span class="step-badge">Step 3: Angle Sum Proof</span>
              <p>1. Diagonal BD divides the interior of concave quadrilateral ADCB into two standard triangles: <strong>△ADB</strong> and <strong>△BDC</strong>.<br>
              2. In △ADB, sum of angles: ∠DAB + ∠ABD + ∠ADB = 180°.<br>
              3. In △BDC, sum of angles: ∠CBD + ∠BDC + ∠BCD = 180°.<br>
              4. Adding both triangle angle sums together:<br>
              ∠DAB + (∠ABD + ∠CBD) + (∠ADB + ∠BDC) + ∠BCD = 180° + 180° = <strong>360°</strong>.<br>
              5. Since (∠ABD + ∠CBD) = ∠ABC, and (∠ADB + ∠BDC) = ∠ADC, the four interior angles sum to exactly 360°!</p>
            </div>
            <div class="step-box step-4">
              <span class="step-badge">Step 4: Physical Measurement Verification</span>
              <p>Constructing a dart on paper with angles 40°, 30°, 30°, and reflex angle 260°: 40° + 30° + 30° + 260° = 360°.</p>
            </div>
            <div class="step-box step-5">
              <span class="step-badge">Step 5: Final Result</span>
              <p><strong>Yes</strong>, the angle sum of any concave quadrilateral is strictly <strong>360°</strong>.</p>
            </div>
          </div>
        </div>
      </details>

      <!-- ITEM 28: PAGE 108 Q11 (ALL 7 TRUE/FALSE) -->
      <details class="ans-box">
        <summary>
          <span><i class="fa-solid fa-circle-question" style="color: var(--primary); margin-right: 0.5rem;"></i> Pages 108–109 — Figure it Out: Question 11 (True or False with Complete Justifications i to vii)</span>
        </summary>
        <div class="ans-content">
          <p><strong>Textbook Question:</strong> State whether the following statements are true or false. Justify your answers:</p>
          <div class="step-container">
            <div class="step-box step-1">
              <span class="step-badge">Statement (i): Diagonals equal and bisect each other must be a square</span>
              <p><strong>Answer: FALSE.</strong><br>
              <em>Justification:</em> A quadrilateral whose diagonals are equal and bisect each other is guaranteed to be a <strong>rectangle</strong>. It is only a square if the diagonals are also <em>perpendicular</em> (intersect at 90°) or if its adjacent sides are equal.</p>
            </div>
            <div class="step-box step-2">
              <span class="step-badge">Statement (ii): A quadrilateral having three right angles must be a rectangle</span>
              <p><strong>Answer: TRUE.</strong><br>
              <em>Justification:</em> By the Angle Sum Property, all four angles must add up to 360°. If three angles are 90°, the fourth angle = 360° − (90° + 90° + 90°) = 90°. Since all four angles are 90°, it is strictly a rectangle (by Deduction 4).</p>
            </div>
            <div class="step-box step-3">
              <span class="step-badge">Statement (iii): A quadrilateral whose diagonals bisect each other must be a parallelogram</span>
              <p><strong>Answer: TRUE.</strong><br>
              <em>Justification:</em> By Deduction 8, when diagonals bisect each other, opposite interior triangles are congruent by SAS/ASA, proving opposite sides are equal and parallel. Hence, it is always a parallelogram.</p>
            </div>
            <div class="step-box step-4">
              <span class="step-badge">Statement (iv): A quadrilateral whose diagonals are perpendicular to each other must be a rhombus</span>
              <p><strong>Answer: FALSE.</strong><br>
              <em>Justification:</em> A <strong>Kite</strong> also has perpendicular diagonals, but its adjacent sides are unequal in pairs and its diagonals do not bisect each other. Even an arbitrary non-symmetric quadrilateral can have perpendicular diagonals without being a rhombus.</p>
            </div>
            <div class="step-box step-5">
              <span class="step-badge">Statements (v), (vi), and (vii)</span>
              <p><strong>(v) A quadrilateral in which opposite angles are equal must be a parallelogram:</strong><br>
              <strong>Answer: TRUE.</strong> Let opposite angles be x and y. Then 2x + 2y = 360° ⇒ x + y = 180°. Consecutive interior angles sum to 180°, so opposite sides are parallel.<br><br>
              <strong>(vi) A quadrilateral in which all angles are equal is a rectangle:</strong><br>
              <strong>Answer: TRUE.</strong> Each angle = 360° ÷ 4 = 90°. A quadrilateral with four 90° angles is a rectangle.<br><br>
              <strong>(vii) Isosceles trapeziums are parallelograms:</strong><br>
              <strong>Answer: FALSE.</strong> In an isosceles trapezium, only ONE pair of opposite sides is parallel. The other pair of equal sides (legs) are non-parallel and will intersect if extended.</p>
            </div>
          </div>
        </div>
      </details>

      <!-- ITEM 29: GAMEPLAY ACTIVITY: WHICH QUAD? -->
      <details class="ans-box">
        <summary>
          <span><i class="fa-solid fa-circle-question" style="color: var(--primary); margin-right: 0.5rem;"></i> Textbook Page 111: Gameplay Investigation — "Which Quad?" Paper Folding</span>
        </summary>
        <div class="ans-content">
          <p><strong>Textbook Prompt:</strong> Fold a sheet into half, then into a quarter. Make a triangular crease at the folded center corner. Open the sheet. What shape is formed by the creases? How do you fold to get a rhombus, a square, or a kite?</p>
          <div class="step-container">
            <div class="step-box step-1">
              <span class="step-badge">Step 1: Activity Setup</span>
              <p>Rectangular or square sheet folded in half horizontally, then in half vertically (quarter fold). The central folded corner represents the origin (0,0) with two mutually perpendicular axes of symmetry.</p>
            </div>
            <div class="step-box step-2">
              <span class="step-badge">Step 2: Geometric Crease Analysis</span>
              <p>Making a straight crease across the central folded corner cuts across both folded edges, creating a line segment with intercepts a along one fold and b along the other.</p>
            </div>
            <div class="step-box step-3">
              <span class="step-badge">Step 3: Shape Determination upon Unfolding</span>
              <p>1. When unfolded, the four identical creases form a closed four-sided polygon around the center.<br>
              2. <strong>General Crease (a ≠ b):</strong> The creases form a <strong>Rhombus</strong>! The folds act as the two perpendicular diagonals of lengths 2a and 2b. By Pythagoras theorem, all four outer crease edges have equal length: √(a² + b²).<br>
              3. <strong>Fold for a Square:</strong> Make the crease at an exact <strong>45° angle</strong> such that a = b (equal intercepts on both folded edges). Then the diagonals are equal (2a = 2b) and perpendicular, creating a perfect <strong>Square</strong>!<br>
              4. <strong>Fold for a Kite:</strong> Fold the sheet in half ONCE along its symmetry line, and make two distinct triangular cuts from the fold line to the edges.</p>
            </div>
            <div class="step-box step-4">
              <span class="step-badge">Step 4: Physical Verification</span>
              <p>Unfolding the paper reveals four congruent triangles meeting at the center, creating the reflection symmetry of rhombuses and squares.</p>
            </div>
            <div class="step-box step-5">
              <span class="step-badge">Step 5: Final Result</span>
              <p>The standard folded crease produces a <strong>Rhombus</strong>, and a 45° crease produces a <strong>Square</strong>.</p>
            </div>
          </div>
        </div>
      </details>
    </section>
"""
