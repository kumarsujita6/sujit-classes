# -*- coding: utf-8 -*-
"""
Module: ch4_section5.py
Contains Section 5: Complete Exam Question Bank (27 CBE Models).
Features:
- Interactive Quiz Engine with real-time score counter
- 5 Conceptual MCQs with trap explanations & dynamic feedback
- 5 Assertion & Reasoning questions with evaluation
- 6 Short Answer Questions (2M/3M)
- 4 Long Answer Questions (5M) with detailed marking schemes
- 2 Competency-Based Real-World Case Studies
- 5 Previous Years Questions (PYQs) with full model solutions
"""

def get_section_5():
    return """
    <!-- SECTION 5: COMPLETE EXAM QUESTION BANK -->
    <section id="section-5">
      <div class="section-header">
        <div class="section-tag"><i class="fa-solid fa-clipboard-question"></i> CBSE &amp; BSE Odisha Exam Bank</div>
        <h2 class="section-title">Section 5: Complete Exam Question Bank (27 CBE Models)</h2>
        <p class="section-desc">
          An exhaustive repository of 27 high-yield examination questions designed according to the latest CBSE Competency-Based Education (CBE) and NEP guidelines, complete with an interactive quiz engine.
        </p>
      </div>

      <!-- PART A: INTERACTIVE MCQS -->
      <div class="quiz-score-header">
        <div>
          <h3><i class="fa-solid fa-brain"></i> Interactive MCQ Quiz Engine</h3>
          <p style="font-size: 0.85rem; margin: 0.2rem 0 0 0; opacity: 0.9;">Test your conceptual sharpness! Click an option to see instant verification and trap analysis.</p>
        </div>
        <div class="score-badge" id="quizScoreDisplay">Score: 0 / 5</div>
      </div>

      <!-- MCQ 1 -->
      <div class="mcq-card" id="mcq-card-1">
        <div class="mcq-question">
          <strong>Q1.</strong> The diagonals of a quadrilateral are equal in length and bisect each other. The quadrilateral MUST necessarily be a:
        </div>
        <div class="mcq-options-grid">
          <button class="option-btn" onclick="handleMcqChoice(1, 'A', false, 'mcq-card-1')">A) Square</button>
          <button class="option-btn" onclick="handleMcqChoice(1, 'B', true, 'mcq-card-1')">B) Rectangle</button>
          <button class="option-btn" onclick="handleMcqChoice(1, 'C', false, 'mcq-card-1')">C) Rhombus</button>
          <button class="option-btn" onclick="handleMcqChoice(1, 'D', false, 'mcq-card-1')">D) General Parallelogram</button>
        </div>
        <div class="feedback-box" id="feedback-1">
          <strong>Correct Answer: B) Rectangle</strong><br>
          <em>Exam Trap Alert:</em> Many students hastily choose <strong>Square</strong>! Remember Deduction 3: if diagonals are equal and bisect each other, the corner angles are guaranteed to be 90°, making it a <strong>Rectangle</strong>. It only becomes a square if the diagonals are ALSO perpendicular (90°) or if all four sides are equal.
        </div>
      </div>

      <!-- MCQ 2 -->
      <div class="mcq-card" id="mcq-card-2">
        <div class="mcq-question">
          <strong>Q2.</strong> Two adjacent angles of a parallelogram are in the ratio 2 : 3. What is the measure of the smaller angle?
        </div>
        <div class="mcq-options-grid">
          <button class="option-btn" onclick="handleMcqChoice(2, 'A', false, 'mcq-card-2')">A) 36°</button>
          <button class="option-btn" onclick="handleMcqChoice(2, 'B', false, 'mcq-card-2')">B) 54°</button>
          <button class="option-btn" onclick="handleMcqChoice(2, 'C', true, 'mcq-card-2')">C) 72°</button>
          <button class="option-btn" onclick="handleMcqChoice(2, 'D', false, 'mcq-card-2')">D) 108°</button>
        </div>
        <div class="feedback-box" id="feedback-2">
          <strong>Correct Answer: C) 72°</strong><br>
          <em>Step-by-Step Solution:</em> In any parallelogram, consecutive adjacent angles are supplementary: 2x + 3x = 180° ⇒ 5x = 180° ⇒ x = 36°. Smaller angle = 2x = 2 × 36° = <strong>72°</strong>. (The larger angle is 3 × 36° = 108°).<br>
          <em>Trap:</em> Students who divide 360° by 5 get 72° for x and then calculate 2x = 144°, forgetting that adjacent angles sum to 180°, not 360°!
        </div>
      </div>

      <!-- MCQ 3 -->
      <div class="mcq-card" id="mcq-card-3">
        <div class="mcq-question">
          <strong>Q3.</strong> The diagonals of a rhombus ABCD intersect at O. If AC = 16 cm and BD = 12 cm, what is the perimeter of the rhombus?
        </div>
        <div class="mcq-options-grid">
          <button class="option-btn" onclick="handleMcqChoice(3, 'A', false, 'mcq-card-3')">A) 20 cm</button>
          <button class="option-btn" onclick="handleMcqChoice(3, 'B', true, 'mcq-card-3')">B) 40 cm</button>
          <button class="option-btn" onclick="handleMcqChoice(3, 'C', false, 'mcq-card-3')">C) 28 cm</button>
          <button class="option-btn" onclick="handleMcqChoice(3, 'D', false, 'mcq-card-3')">D) 56 cm</button>
        </div>
        <div class="feedback-box" id="feedback-3">
          <strong>Correct Answer: B) 40 cm</strong><br>
          <em>Step-by-Step Solution:</em> The diagonals of a rhombus bisect each other at right angles: OA = 16/2 = 8 cm and OB = 12/2 = 6 cm. In right △AOB: Side AB = √(OA² + OB²) = √(8² + 6²) = √(64 + 36) = √100 = 10 cm. Perimeter = 4 × Side = 4 × 10 cm = <strong>40 cm</strong>.<br>
          <em>Trap:</em> Option A (10 cm) is just the side length, not the perimeter!
        </div>
      </div>

      <!-- MCQ 4 -->
      <div class="mcq-card" id="mcq-card-4">
        <div class="mcq-question">
          <strong>Q4.</strong> Which of the following statements is mathematically ALWAYS TRUE?
        </div>
        <div class="mcq-options-grid">
          <button class="option-btn" onclick="handleMcqChoice(4, 'A', false, 'mcq-card-4')">A) A quadrilateral whose diagonals are perpendicular is a rhombus.</button>
          <button class="option-btn" onclick="handleMcqChoice(4, 'B', true, 'mcq-card-4')">B) Every rhombus is a kite.</button>
          <button class="option-btn" onclick="handleMcqChoice(4, 'C', false, 'mcq-card-4')">C) Diagonals of every parallelogram are equal.</button>
          <button class="option-btn" onclick="handleMcqChoice(4, 'D', false, 'mcq-card-4')">D) An isosceles trapezium is a parallelogram.</button>
        </div>
        <div class="feedback-box" id="feedback-4">
          <strong>Correct Answer: B) Every rhombus is a kite.</strong><br>
          <em>Analysis:</em> A kite is defined as having two pairs of adjacent equal sides. In a rhombus, all four sides are equal, so adjacent sides are automatically equal in pairs! Thus, every rhombus satisfies the definition of a kite. Statement A is false because kites also have perpendicular diagonals. Statement C is false (only rectangles/squares have equal diagonals). Statement D is false because non-parallel legs intersect.
        </div>
      </div>

      <!-- MCQ 5 -->
      <div class="mcq-card" id="mcq-card-5">
        <div class="mcq-question">
          <strong>Q5.</strong> In an isosceles trapezium ABCD with AB ∥ CD and AD = BC, if ∠C = 115°, what is the measure of base angle ∠A?
        </div>
        <div class="mcq-options-grid">
          <button class="option-btn" onclick="handleMcqChoice(5, 'A', false, 'mcq-card-5')">A) 115°</button>
          <button class="option-btn" onclick="handleMcqChoice(5, 'B', false, 'mcq-card-5')">B) 75°</button>
          <button class="option-btn" onclick="handleMcqChoice(5, 'C', true, 'mcq-card-5')">C) 65°</button>
          <button class="option-btn" onclick="handleMcqChoice(5, 'D', false, 'mcq-card-5')">D) 55°</button>
        </div>
        <div class="feedback-box" id="feedback-5">
          <strong>Correct Answer: C) 65°</strong><br>
          <em>Step-by-Step Solution:</em> In an isosceles trapezium, the top base angles are equal: ∠D = ∠C = 115°. Along non-parallel leg AD, consecutive interior angles between parallel lines AB and CD add to 180°: ∠A + ∠D = 180° ⇒ ∠A = 180° − 115° = <strong>65°</strong>.
        </div>
      </div>

      <!-- PART B: ASSERTION & REASONING -->
      <h3 class="subheading"><i class="fa-solid fa-scale-balanced"></i> 5.2 Assertion &amp; Reasoning Questions (5 Items)</h3>
      <p style="font-size: 0.95rem; color: var(--text-muted);">
        <strong>Directions:</strong> In each question below, choose:
        <br>(A) Both Assertion (A) and Reason (R) are true and Reason (R) is the correct explanation of Assertion (A).
        <br>(B) Both Assertion (A) and Reason (R) are true but Reason (R) is NOT the correct explanation of Assertion (A).
        <br>(C) Assertion (A) is true but Reason (R) is false.
        <br>(D) Assertion (A) is false but Reason (R) is true.
      </p>

      <details class="ans-box">
        <summary>
          <span><i class="fa-solid fa-question" style="color: var(--primary); margin-right: 0.5rem;"></i> AR Question 1: Diagonal Equality vs. Rectangle Classification</span>
        </summary>
        <div class="ans-content">
          <p><strong>Assertion (A):</strong> A quadrilateral having diagonals of equal length is not necessarily a rectangle.</p>
          <p><strong>Reason (R):</strong> In an isosceles trapezium, the diagonals are equal in length, but it is not a rectangle.</p>
          <div class="step-container">
            <div class="step-box step-1">
              <span class="step-badge">Step 1: Evaluation of Assertion (A)</span>
              <p>Assertion (A) is TRUE. Simply having equal diagonals does not make a quadrilateral a rectangle. The diagonals must also bisect each other.</p>
            </div>
            <div class="step-box step-2">
              <span class="step-badge">Step 2: Evaluation of Reason (R)</span>
              <p>Reason (R) is TRUE. In an isosceles trapezium, the diagonals are congruent (UW = VX), but only one pair of sides is parallel, so it is not a rectangle.</p>
            </div>
            <div class="step-box step-3">
              <span class="step-badge">Step 3: Logical Connection</span>
              <p>Reason (R) provides the exact geometric counterexample that proves Assertion (A).</p>
            </div>
            <div class="step-box step-4">
              <span class="step-badge">Step 4: Final Option</span>
              <p><strong>Correct Option: (A)</strong> Both Assertion and Reason are true, and Reason is the correct explanation of Assertion.</p>
            </div>
          </div>
        </div>
      </details>

      <details class="ans-box">
        <summary>
          <span><i class="fa-solid fa-question" style="color: var(--primary); margin-right: 0.5rem;"></i> AR Question 2: Diagonals of a Square</span>
        </summary>
        <div class="ans-content">
          <p><strong>Assertion (A):</strong> The diagonals of a square are equal in length and bisect each other at right angles.</p>
          <p><strong>Reason (R):</strong> A square is both a rectangle (inheriting equal bisecting diagonals) and a rhombus (inheriting perpendicular bisecting diagonals).</p>
          <div class="step-container">
            <div class="step-box step-1">
              <span class="step-badge">Step 1: Evaluation of Assertion (A)</span>
              <p>Assertion (A) is TRUE by Property 4 of squares.</p>
            </div>
            <div class="step-box step-2">
              <span class="step-badge">Step 2: Evaluation of Reason (R)</span>
              <p>Reason (R) is TRUE. A square is the unique intersection of the set of Rectangles and Rhombuses in the Euler-Venn taxonomy.</p>
            </div>
            <div class="step-box step-3">
              <span class="step-badge">Step 3: Logical Connection</span>
              <p>Because the square belongs to both families, it inherits both sets of diagonal properties simultaneously. Reason correctly explains Assertion.</p>
            </div>
            <div class="step-box step-4">
              <span class="step-badge">Step 4: Final Option</span>
              <p><strong>Correct Option: (A)</strong></p>
            </div>
          </div>
        </div>
      </details>

      <details class="ans-box">
        <summary>
          <span><i class="fa-solid fa-question" style="color: var(--primary); margin-right: 0.5rem;"></i> AR Question 3: Parallelogram Angle Distribution</span>
        </summary>
        <div class="ans-content">
          <p><strong>Assertion (A):</strong> If the interior angles of a quadrilateral are 120°, 60°, 120°, and 60° taken in sequential order, it is guaranteed to be a parallelogram.</p>
          <p><strong>Reason (R):</strong> If both pairs of opposite angles of a quadrilateral are equal, consecutive angles must add to 180°, which makes both pairs of opposite sides parallel.</p>
          <div class="step-container">
            <div class="step-box step-1">
              <span class="step-badge">Step 1: Evaluation of Assertion (A)</span>
              <p>Assertion (A) is TRUE. Opposite angles are 120° = 120° and 60° = 60°.</p>
            </div>
            <div class="step-box step-2">
              <span class="step-badge">Step 2: Evaluation of Reason (R)</span>
              <p>Reason (R) is TRUE. In quadrilateral ABCD with ∠A = ∠C = 120° and ∠B = ∠D = 60°, consecutive angles sum to 120° + 60° = 180°. By the transversal converse, AB ∥ CD and AD ∥ BC.</p>
            </div>
            <div class="step-box step-3">
              <span class="step-badge">Step 3: Logical Connection</span>
              <p>Reason provides the exact geometric proof for Assertion.</p>
            </div>
            <div class="step-box step-4">
              <span class="step-badge">Step 4: Final Option</span>
              <p><strong>Correct Option: (A)</strong></p>
            </div>
          </div>
        </div>
      </details>

      <details class="ans-box">
        <summary>
          <span><i class="fa-solid fa-question" style="color: var(--primary); margin-right: 0.5rem;"></i> AR Question 4: Reflection Symmetry of a Kite</span>
        </summary>
        <div class="ans-content">
          <p><strong>Assertion (A):</strong> A general kite has two lines of reflection symmetry.</p>
          <p><strong>Reason (R):</strong> The diagonals of a kite intersect each other at right angles (90°).</p>
          <div class="step-container">
            <div class="step-box step-1">
              <span class="step-badge">Step 1: Evaluation of Assertion (A)</span>
              <p>Assertion (A) is <strong>FALSE</strong>. A general kite has only <strong>ONE</strong> line of reflection symmetry (the main diagonal joining the vertices where unequal sides meet). It would only have two lines of symmetry if all four sides were equal (which is a rhombus).</p>
            </div>
            <div class="step-box step-2">
              <span class="step-badge">Step 2: Evaluation of Reason (R)</span>
              <p>Reason (R) is <strong>TRUE</strong>. The diagonals of any kite do intersect perpendicularly at 90°.</p>
            </div>
            <div class="step-box step-3">
              <span class="step-badge">Step 3: Final Option</span>
              <p><strong>Correct Option: (D)</strong> Assertion (A) is false, but Reason (R) is true.</p>
            </div>
          </div>
        </div>
      </details>

      <details class="ans-box">
        <summary>
          <span><i class="fa-solid fa-question" style="color: var(--primary); margin-right: 0.5rem;"></i> AR Question 5: Geometric Impossibility of Three 90° Angles with an 85° Angle</span>
        </summary>
        <div class="ans-content">
          <p><strong>Assertion (A):</strong> It is impossible to construct a planar quadrilateral with angles measuring 90°, 90°, 90°, and 85°.</p>
          <p><strong>Reason (R):</strong> The sum of the interior angle measures of any planar quadrilateral must equal exactly 360°.</p>
          <div class="step-container">
            <div class="step-box step-1">
              <span class="step-badge">Step 1: Evaluation of Assertion (A)</span>
              <p>Assertion (A) is TRUE. 90° + 90° + 90° + 85° = 355° ≠ 360°. Such a figure cannot close.</p>
            </div>
            <div class="step-box step-2">
              <span class="step-badge">Step 2: Evaluation of Reason (R)</span>
              <p>Reason (R) is TRUE by the Angle Sum Property of a quadrilateral.</p>
            </div>
            <div class="step-box step-3">
              <span class="step-badge">Step 3: Logical Connection</span>
              <p>Reason is the foundational axiom that proves Assertion.</p>
            </div>
            <div class="step-box step-4">
              <span class="step-badge">Step 4: Final Option</span>
              <p><strong>Correct Option: (A)</strong></p>
            </div>
          </div>
        </div>
      </details>

      <!-- PART C: SHORT ANSWER QUESTIONS -->
      <h3 class="subheading"><i class="fa-solid fa-pencil"></i> 5.3 Short Answer Questions (2M &amp; 3M - 6 Items)</h3>

      <!-- SAQ 1 -->
      <details class="ans-box">
        <summary>
          <span><i class="fa-solid fa-pen-clip" style="color: var(--primary); margin-right: 0.5rem;"></i> SAQ 1 (2 Marks): Angles of Parallelogram in Ratio 4 : 5</span>
        </summary>
        <div class="ans-content">
          <p><strong>Question:</strong> Two adjacent angles of a parallelogram are in the ratio 4 : 5. Find the measure of all four angles of the parallelogram.</p>
          <div class="step-container">
            <div class="step-box step-1">
              <span class="step-badge">Step 1: Given Data</span>
              <p>Let the two adjacent angles be 4x and 5x.</p>
            </div>
            <div class="step-box step-2">
              <span class="step-badge">Step 2: Property Applied</span>
              <p>Consecutive adjacent angles in a parallelogram are supplementary (sum = 180°).</p>
            </div>
            <div class="step-box step-3">
              <span class="step-badge">Step 3: Algebraic Working</span>
              <p>4x + 5x = 180° ⇒ 9x = 180° ⇒ x = 20°.<br>
              First angle = 4 × 20° = <strong>80°</strong>.<br>
              Second angle = 5 × 20° = <strong>100°</strong>.</p>
            </div>
            <div class="step-box step-4">
              <span class="step-badge">Step 4: Opposite Angles Law</span>
              <p>Opposite angles are equal. Therefore, the four angles are <strong>80°, 100°, 80°, 100°</strong>.</p>
            </div>
          </div>
        </div>
      </details>

      <!-- SAQ 2 -->
      <details class="ans-box">
        <summary>
          <span><i class="fa-solid fa-pen-clip" style="color: var(--primary); margin-right: 0.5rem;"></i> SAQ 2 (2 Marks): Rhombus with Perimeter 52 cm and Diagonal 10 cm</span>
        </summary>
        <div class="ans-content">
          <p><strong>Question:</strong> The perimeter of a rhombus is 52 cm, and one of its diagonals is 10 cm. Find the length of the second diagonal.</p>
          <div class="step-container">
            <div class="step-box step-1">
              <span class="step-badge">Step 1: Side Length Calculation</span>
              <p>Perimeter = 4a = 52 cm ⇒ Side a = 52 ÷ 4 = <strong>13 cm</strong>.</p>
            </div>
            <div class="step-box step-2">
              <span class="step-badge">Step 2: Half Diagonal Calculation</span>
              <p>Given d₁ = 10 cm ⇒ Half diagonal = d₁ / 2 = 10 ÷ 2 = <strong>5 cm</strong>.</p>
            </div>
            <div class="step-box step-3">
              <span class="step-badge">Step 3: Pythagoras Theorem at 90° Intersection</span>
              <p>Diagonals intersect perpendicularly. In right △AOB:<br>
              (d₂ / 2)² = a² − (d₁ / 2)² = 13² − 5² = 169 − 25 = 144.<br>
              d₂ / 2 = √144 = <strong>12 cm</strong>.</p>
            </div>
            <div class="step-box step-4">
              <span class="step-badge">Step 4: Final Result</span>
              <p>Total length of second diagonal d₂ = 2 × 12 cm = <strong>24 cm</strong>.</p>
            </div>
          </div>
        </div>
      </details>

      <!-- SAQ 3 -->
      <details class="ans-box">
        <summary>
          <span><i class="fa-solid fa-pen-clip" style="color: var(--primary); margin-right: 0.5rem;"></i> SAQ 3 (3 Marks): Quadrilateral Angles in Ratio 3 : 5 : 9 : 13</span>
        </summary>
        <div class="ans-content">
          <p><strong>Question:</strong> The four angles of a quadrilateral are in the ratio 3 : 5 : 9 : 13. Find the measure of each angle. Is this quadrilateral convex or concave?</p>
          <div class="step-container">
            <div class="step-box step-1">
              <span class="step-badge">Step 1: Algebraic Setup</span>
              <p>Let the angles be 3x, 5x, 9x, and 13x.</p>
            </div>
            <div class="step-box step-2">
              <span class="step-badge">Step 2: Angle Sum Property</span>
              <p>3x + 5x + 9x + 13x = 360° ⇒ 30x = 360° ⇒ x = 12°.</p>
            </div>
            <div class="step-box step-3">
              <span class="step-badge">Step 3: Angle Values</span>
              <p>• ∠1 = 3 × 12° = <strong>36°</strong><br>
              • ∠2 = 5 × 12° = <strong>60°</strong><br>
              • ∠3 = 9 × 12° = <strong>108°</strong><br>
              • ∠4 = 13 × 12° = <strong>156°</strong></p>
            </div>
            <div class="step-box step-4">
              <span class="step-badge">Step 4: Convexity Verification</span>
              <p>Since every interior angle is strictly less than 180° (none is reflex), the quadrilateral is strictly <strong>Convex</strong>.</p>
            </div>
          </div>
        </div>
      </details>

      <!-- SAQ 4 -->
      <details class="ans-box">
        <summary>
          <span><i class="fa-solid fa-pen-clip" style="color: var(--primary); margin-right: 0.5rem;"></i> SAQ 4 (3 Marks): Angle Bisectors of Adjacent Angles in a Parallelogram</span>
        </summary>
        <div class="ans-content">
          <p><strong>Question:</strong> In a parallelogram ABCD, the bisectors of consecutive angles ∠A and ∠B intersect at point P. Prove that ∠APB = 90°.</p>
          <div class="step-container">
            <div class="step-box step-1">
              <span class="step-badge">Step 1: Given Data</span>
              <p>Parallelogram ABCD with AP bisecting ∠A and BP bisecting ∠B.</p>
            </div>
            <div class="step-box step-2">
              <span class="step-badge">Step 2: Adjacent Angle Property</span>
              <p>In a parallelogram, consecutive adjacent angles sum to 180°: <strong>∠A + ∠B = 180°</strong>.</p>
            </div>
            <div class="step-box step-3">
              <span class="step-badge">Step 3: Halving the Equation</span>
              <p>Dividing the equation by 2:<br>
              ½(∠A) + ½(∠B) = 180° ÷ 2 = 90°.<br>
              Since AP and BP are angle bisectors: ∠PAB = ½(∠A) and ∠PBA = ½(∠B).<br>
              Therefore, <strong>∠PAB + ∠PBA = 90°</strong>.</p>
            </div>
            <div class="step-box step-4">
              <span class="step-badge">Step 4: Triangle Angle Sum</span>
              <p>In △APB: ∠PAB + ∠PBA + ∠APB = 180° ⇒ 90° + ∠APB = 180° ⇒ <strong>∠APB = 90°</strong>. (Hence proved!)</p>
            </div>
          </div>
        </div>
      </details>

      <!-- SAQ 5 -->
      <details class="ans-box">
        <summary>
          <span><i class="fa-solid fa-pen-clip" style="color: var(--primary); margin-right: 0.5rem;"></i> SAQ 5 (3 Marks): Kite Diagonals with Sides 5 cm and 12 cm</span>
        </summary>
        <div class="ans-content">
          <p><strong>Question:</strong> In kite ABCD, adjacent sides AB = AD = 5 cm and BC = CD = 12 cm. If the cross diagonal BD = 6 cm, find the length of the main diagonal AC.</p>
          <div class="step-container">
            <div class="step-box step-1">
              <span class="step-badge">Step 1: Intersection Geometry</span>
              <p>The main diagonal AC is the perpendicular bisector of cross diagonal BD at O. Thus, OB = OD = 6 ÷ 2 = <strong>3 cm</strong>, and ∠AOB = ∠COB = 90°.</p>
            </div>
            <div class="step-box step-2">
              <span class="step-badge">Step 2: Calculate OA</span>
              <p>In right △AOB: OA² = AB² − OB² = 5² − 3² = 25 − 9 = 16 ⇒ OA = <strong>4 cm</strong>.</p>
            </div>
            <div class="step-box step-3">
              <span class="step-badge">Step 3: Calculate OC</span>
              <p>In right △COB: OC² = BC² − OB² = 12² − 3² = 144 − 9 = 135 ⇒ OC = √135 = 3√15 ≈ <strong>11.62 cm</strong>.</p>
            </div>
            <div class="step-box step-4">
              <span class="step-badge">Step 4: Total Diagonal Length</span>
              <p>Total AC = OA + OC = 4 + 3√15 ≈ <strong>15.62 cm</strong>.</p>
            </div>
          </div>
        </div>
      </details>

      <!-- SAQ 6 -->
      <details class="ans-box">
        <summary>
          <span><i class="fa-solid fa-pen-clip" style="color: var(--primary); margin-right: 0.5rem;"></i> SAQ 6 (3 Marks): Height &amp; Area of Isosceles Trapezium</span>
        </summary>
        <div class="ans-content">
          <p><strong>Question:</strong> An isosceles trapezium has parallel sides of lengths 10 cm and 22 cm, and non-parallel legs of 10 cm each. Find its height and area.</p>
          <div class="step-container">
            <div class="step-box step-1">
              <span class="step-badge">Step 1: Partitioning the Base</span>
              <p>Let parallel bases be a = 10 cm and b = 22 cm. Drop altitudes from top vertices to bottom base. The horizontal projection of each leg is: x = (22 − 10) ÷ 2 = 12 ÷ 2 = <strong>6 cm</strong>.</p>
            </div>
            <div class="step-box step-2">
              <span class="step-badge">Step 2: Calculate Height using Pythagoras</span>
              <p>In the outer right triangle: h² = Leg² − x² = 10² − 6² = 100 − 36 = 64 ⇒ Height h = √64 = <strong>8 cm</strong>.</p>
            </div>
            <div class="step-box step-3">
              <span class="step-badge">Step 3: Area Computation</span>
              <p>Area = ½ × (Sum of Parallel Bases) × Height = ½ × (10 + 22) × 8 = ½ × 32 × 8 = <strong>128 cm²</strong>.</p>
            </div>
          </div>
        </div>
      </details>

      <!-- PART D: LONG ANSWER QUESTIONS (5 MARKS) -->
      <h3 class="subheading"><i class="fa-solid fa-award"></i> 5.4 Long Answer Questions with Step-by-Step Marking Schemes (5M - 4 Items)</h3>

      <!-- LAQ 1 -->
      <details class="ans-box">
        <summary>
          <span><i class="fa-solid fa-file-pen" style="color: var(--primary); margin-right: 0.5rem;"></i> LAQ 1 (5 Marks): Angle Sum Theorem Proof &amp; Concave Extension</span>
        </summary>
        <div class="ans-content">
          <p><strong>Question:</strong> State and prove the Angle Sum Property of a quadrilateral. Does this theorem hold true for a concave (dart-shaped) quadrilateral? Justify with a diagram and rigorous mathematical proof.</p>
          <div class="step-container">
            <div class="step-box step-1">
              <span class="step-badge">Marking Scheme Breakdown [Total: 5 Marks]</span>
              <p>• Statement of Theorem: 1 Mark<br>
              • Construction &amp; Convex Proof: 2 Marks<br>
              • Concave Quadrilateral Identification &amp; Proof: 2 Marks</p>
            </div>
            <div class="step-box step-2">
              <span class="step-badge">Part 1: Statement &amp; Convex Proof</span>
              <p><strong>Statement:</strong> The sum of the interior angle measures of any planar quadrilateral is 360°.<br>
              <strong>Proof:</strong> Let ABCD be a convex quadrilateral. Draw diagonal AC. This divides ABCD into △ABC and △CDA.<br>
              In △ABC: ∠CAB + ∠B + ∠BCA = 180° ...(1)<br>
              In △CDA: ∠CAD + ∠D + ∠DCA = 180° ...(2)<br>
              Adding (1) and (2):<br>
              (∠CAB + ∠CAD) + ∠B + (∠BCA + ∠DCA) + ∠D = 180° + 180° = 360°<br>
              ⇒ ∠A + ∠B + ∠C + ∠D = 360°.</p>
            </div>
            <div class="step-box step-3">
              <span class="step-badge">Part 2: Concave Quadrilateral Proof</span>
              <p>Let ADCB be a concave quadrilateral where vertex C forms an interior reflex angle (> 180°).<br>
              Draw internal diagonal BD connecting vertices B and D. This diagonal lies entirely inside the figure and partitions the concave quadrilateral into two triangles: △ADB and △BDC.<br>
              In △ADB: ∠DAB + ∠ABD + ∠ADB = 180°<br>
              In △BDC: ∠CBD + ∠BDC + ∠BCD = 180°<br>
              Adding both equations:<br>
              ∠DAB + (∠ABD + ∠CBD) + (∠ADB + ∠BDC) + ∠BCD = 180° + 180° = 360°<br>
              ⇒ ∠A + ∠B + ∠D + ∠C = 360°.<br>
              <strong>Conclusion:</strong> The theorem holds universally for ALL quadrilaterals, convex or concave!</p>
            </div>
          </div>
        </div>
      </details>

      <!-- LAQ 2 -->
      <details class="ans-box">
        <summary>
          <span><i class="fa-solid fa-file-pen" style="color: var(--primary); margin-right: 0.5rem;"></i> LAQ 2 (5 Marks): Necessary and Sufficient Diagonal Bisection Theorem</span>
        </summary>
        <div class="ans-content">
          <p><strong>Question:</strong> Prove that a quadrilateral is a parallelogram if and only if its diagonals bisect each other.</p>
          <div class="step-container">
            <div class="step-box step-1">
              <span class="step-badge">Marking Scheme Breakdown [Total: 5 Marks]</span>
              <p>• Part 1: Proving Parallelogram ⇒ Diagonals Bisect: 2.5 Marks<br>
              • Part 2: Proving Diagonals Bisect ⇒ Parallelogram (Converse): 2.5 Marks</p>
            </div>
            <div class="step-box step-2">
              <span class="step-badge">Part 1: Given Parallelogram ABCD, Prove OA = OC and OB = OD</span>
              <p>In parallelogram ABCD, AB ∥ CD and AB = CD (opposite sides). Diagonals AC and BD intersect at O.<br>
              In △AOB and △COD:<br>
              • AB = CD (Opposite sides of parallelogram are equal)<br>
              • ∠OAB = ∠OCD (Alternate interior angles, AB ∥ CD with transversal AC)<br>
              • ∠OBA = ∠ODC (Alternate interior angles, AB ∥ CD with transversal BD)<br>
              By ASA Congruence: <strong>△AOB ≅ △COD</strong>.<br>
              By CPCTC: <strong>OA = OC</strong> and <strong>OB = OD</strong>. (Diagonals bisect each other).</p>
            </div>
            <div class="step-box step-3">
              <span class="step-badge">Part 2: Converse — Given OA = OC and OB = OD, Prove ABCD is Parallelogram</span>
              <p>In △AOB and △COD:<br>
              • OA = OC (Given)<br>
              • OB = OD (Given)<br>
              • ∠AOB = ∠COD (Vertically opposite angles)<br>
              By SAS Congruence: <strong>△AOB ≅ △COD</strong>.<br>
              By CPCTC: AB = CD and ∠OAB = ∠OCD.<br>
              Since alternate interior angles ∠OAB and ∠OCD are equal, <strong>AB ∥ CD</strong>.<br>
              Since one pair of opposite sides (AB and CD) is <strong>BOTH equal and parallel</strong>, quadrilateral ABCD is guaranteed to be a <strong>Parallelogram</strong>!</p>
            </div>
          </div>
        </div>
      </details>

      <!-- LAQ 3 -->
      <details class="ans-box">
        <summary>
          <span><i class="fa-solid fa-file-pen" style="color: var(--primary); margin-right: 0.5rem;"></i> LAQ 3 (5 Marks): Midpoint Quadrilateral of a Rhombus is a Rectangle</span>
        </summary>
        <div class="ans-content">
          <p><strong>Question:</strong> ABCD is a rhombus. P, Q, R, and S are the midpoints of sides AB, BC, CD, and DA respectively. Prove that the quadrilateral PQRS is a rectangle.</p>
          <div class="step-container">
            <div class="step-box step-1">
              <span class="step-badge">Marking Scheme Breakdown [Total: 5 Marks]</span>
              <p>• Midpoint Theorem application to show PQRS is a parallelogram: 2 Marks<br>
              • Using Rhombus Diagonals at 90°: 1.5 Marks<br>
              • Proving Corner Angle of PQRS = 90°: 1.5 Marks</p>
            </div>
            <div class="step-box step-2">
              <span class="step-badge">Step 1: Apply Midpoint Theorem</span>
              <p>Draw diagonal AC of rhombus ABCD.<br>
              In △ABC, P is midpoint of AB and Q is midpoint of BC. By Midpoint Theorem: <strong>PQ ∥ AC and PQ = ½ AC</strong>.<br>
              In △ADC, S is midpoint of AD and R is midpoint of CD. By Midpoint Theorem: <strong>SR ∥ AC and SR = ½ AC</strong>.<br>
              Therefore, PQ ∥ SR and PQ = SR. Since one pair of opposite sides is equal and parallel, <strong>PQRS is a parallelogram</strong>.</p>
            </div>
            <div class="step-box step-3">
              <span class="step-badge">Step 2: Prove One Angle of PQRS is 90°</span>
              <p>Draw diagonal BD of rhombus ABCD. By the properties of a rhombus, diagonals are perpendicular: <strong>AC ⊥ BD</strong>.<br>
              Let AC and BD intersect at O. Let PQ intersect BD at M, and QR intersect AC at N.<br>
              • In quadrilateral OMQN:<br>
              MQ ∥ ON (since BD ∥ QR by Midpoint theorem in △BCD)<br>
              NQ ∥ OM (since AC ∥ PQ)<br>
              Therefore, OMQN is a parallelogram!<br>
              • In parallelogram OMQN, opposite angles are equal: ∠MQN = ∠MON.<br>
              Since AC ⊥ BD, ∠MON = 90°. Therefore, <strong>∠MQN = ∠PQR = 90°</strong>.</p>
            </div>
            <div class="step-box step-4">
              <span class="step-badge">Step 3: Final Conclusion</span>
              <p>A parallelogram with one right angle is a <strong>Rectangle</strong>. Hence, PQRS is strictly a rectangle!</p>
            </div>
          </div>
        </div>
      </details>

      <!-- LAQ 4 -->
      <details class="ans-box">
        <summary>
          <span><i class="fa-solid fa-file-pen" style="color: var(--primary); margin-right: 0.5rem;"></i> LAQ 4 (5 Marks): The Carpenter's Practical Geometry Proof</span>
        </summary>
        <div class="ans-content">
          <p><strong>Question:</strong> A furniture maker wants to construct a perfectly square window frame of diagonal 10 cm using two wooden strips. Explain using Deductions 1, 2, 3, and 5 how the carpenter can guarantee that the completed frame is an exact square without measuring a single corner angle with a protractor.</p>
          <div class="step-container">
            <div class="step-box step-1">
              <span class="step-badge">Marking Scheme Breakdown [Total: 5 Marks]</span>
              <p>• Strip length &amp; bisection deduction: 1.5 Marks<br>
              • Perpendicularity condition (Deduction 5): 1.5 Marks<br>
              • Proof of corner angles = 90° (Deduction 3): 1 Mark<br>
              • Proof of equal side lengths (SSS / Pythagoras): 1 Mark</p>
            </div>
            <div class="step-box step-2">
              <span class="step-badge">Step-by-Step Practical Procedure</span>
              <p>1. <strong>Cut Two Equal Strips (Deduction 1):</strong> Cut two rigid wooden strips of exactly 10 cm each.<br>
              2. <strong>Locate Midpoints (Deduction 2):</strong> Measure 5 cm from either end of both strips and drill a pivot hole at the exact midpoint O. Pin the strips together so that OA = OB = OC = OD = 5 cm.<br>
              3. <strong>Set Perpendicular Orientation at 90° (Deduction 5):</strong> Adjust the opening angle until the strips cross at exactly 90°. (This can be verified by checking that the four corner thread lengths are identical, or using a carpenter's 3-4-5 framing square).<br>
              4. <strong>Connect Endpoints:</strong> Fasten the four outer frame battens to endpoints A, B, C, D.<br>
              5. <strong>Mathematical Guarantee:</strong><br>
              • By Deduction 3: Since OA = OB = OC = OD, each vertex angle is (90° − 90°/2) + 90°/2 = 90°.<br>
              • By Deduction 10 &amp; Pythagoras: Each side = √(5² + 5²) = √50 ≈ 7.07 cm. All four sides are equal.<br>
              The resulting frame is mathematically guaranteed to be a <strong>Square</strong>!</p>
            </div>
          </div>
        </div>
      </details>

      <!-- PART E: CASE STUDIES -->
      <h3 class="subheading"><i class="fa-solid fa-city"></i> 5.5 Competency-Based Real-World Case Studies (2 Items)</h3>

      <!-- CASE STUDY 1 -->
      <details class="ans-box">
        <summary>
          <span><i class="fa-solid fa-building-columns" style="color: var(--primary); margin-right: 0.5rem;"></i> Case Study 1: The Modern Architectural Kite Canopy (Aerodynamics &amp; Tiling)</span>
        </summary>
        <div class="ans-content">
          <p><strong>Context &amp; Background:</strong> An architectural engineering firm designs a futuristic fabric tensile canopy for an amphitheater in Bhubaneswar. The roof is modeled as a symmetrical kite ABCD with main vertical spine AC and horizontal cross-stay BD. The shorter upper struts AB and AD measure 10 m each, while the longer lower struts BC and CD measure 17 m each. The horizontal cross-stay BD measures 16 m.</p>
          <div class="step-container">
            <div class="step-box step-1">
              <span class="step-badge">Question 1: Find the length of the main vertical spine AC</span>
              <p>• The cross-stay BD is bisected perpendicularly at O: OB = OD = 16 ÷ 2 = <strong>8 m</strong>.<br>
              • In top right △AOB: OA = √(AB² − OB²) = √(10² − 8²) = √(100 − 64) = √36 = <strong>6 m</strong>.<br>
              • In bottom right △COB: OC = √(BC² − OB²) = √(17² − 8²) = √(289 − 64) = √225 = <strong>15 m</strong>.<br>
              • Total length of main spine AC = OA + OC = 6 m + 15 m = <strong>21 m</strong>.</p>
            </div>
            <div class="step-box step-2">
              <span class="step-badge">Question 2: Calculate the total surface area of canopy fabric needed</span>
              <p>Area of Kite = ½ × d₁ × d₂ = ½ × AC × BD = ½ × 21 m × 16 m = <strong>168 m²</strong>.</p>
            </div>
            <div class="step-box step-3">
              <span class="step-badge">Question 3: Determine the perimeter and boundary piping length</span>
              <p>Perimeter = AB + BC + CD + DA = 10 + 17 + 17 + 10 = <strong>54 m</strong>.</p>
            </div>
            <div class="step-box step-4">
              <span class="step-badge">Question 4: Which diagonal acts as the structural line of symmetry?</span>
              <p>Spine <strong>AC</strong> acts as the line of symmetry because it bisects the canopy into two congruent mirror halves (△ABC ≅ △ADC).</p>
            </div>
          </div>
        </div>
      </details>

      <!-- CASE STUDY 2 -->
      <details class="ans-box">
        <summary>
          <span><i class="fa-solid fa-tree" style="color: var(--primary); margin-right: 0.5rem;"></i> Case Study 2: Smart Eco-Park Land Zoning (Parallelograms &amp; Trapeziums)</span>
        </summary>
        <div class="ans-content">
          <p><strong>Context &amp; Background:</strong> Cuttack Municipal Corporation plans a green community park. The land is surveyed as a large parallelogram PQRS with sides PQ = 50 m and QR = 30 m. The acute angle ∠P is measured to be 60°. A pathway is constructed along the diagonal PR. Inside the park, a section is demarcated as an isosceles trapezium children's play area with parallel sides of 12 m and 20 m and non-parallel legs of 5 m each.</p>
          <div class="step-container">
            <div class="step-box step-1">
              <span class="step-badge">Question 1: Find all four interior corner angles of park PQRS</span>
              <p>Since PQRS is a parallelogram: Opposite angles are equal: ∠R = ∠P = <strong>60°</strong>.<br>
              Consecutive angles are supplementary: ∠Q = 180° − 60° = <strong>120°</strong>, and ∠S = <strong>120°</strong>.</p>
            </div>
            <div class="step-box step-2">
              <span class="step-badge">Question 2: Calculate the total fencing cost of the outer park at ₹120 per meter</span>
              <p>Perimeter = 2(PQ + QR) = 2(50 + 30) = 2 × 80 = <strong>160 m</strong>.<br>
              Total Cost = 160 m × ₹120 = <strong>₹19,200</strong>.</p>
            </div>
            <div class="step-box step-3">
              <span class="step-badge">Question 3: Find the height and area of the children's play area</span>
              <p>In the isosceles trapezium: parallel bases = 12 m and 20 m, legs = 5 m.<br>
              Offset per side = (20 − 12) ÷ 2 = 4 m.<br>
              Height h = √(5² − 4²) = √(25 − 16) = √9 = <strong>3 m</strong>.<br>
              Area = ½ × (12 + 20) × 3 = ½ × 32 × 3 = <strong>48 m²</strong>.</p>
            </div>
          </div>
        </div>
      </details>

      <!-- PART F: PYQS & PROBABLE QUESTIONS -->
      <h3 class="subheading"><i class="fa-solid fa-clock-rotate-left"></i> 5.6 Previous Years &amp; Most Probable Exam Questions (5 Items)</h3>

      <!-- PYQ 1 -->
      <details class="ans-box">
        <summary>
          <span><i class="fa-solid fa-scroll" style="color: var(--primary); margin-right: 0.5rem;"></i> PYQ 1 (CBSE 2023): Algebraic Opposite Angles in Parallelogram</span>
        </summary>
        <div class="ans-content">
          <p><strong>Question:</strong> In a parallelogram PQRS, ∠P = (3x − 10)° and ∠R = (x + 30)°. Find the value of x and the measure of all four interior angles.</p>
          <div class="step-container">
            <div class="step-box step-1">
              <span class="step-badge">Step 1: Opposite Angles Theorem</span>
              <p>In a parallelogram, opposite angles are equal: ∠P = ∠R.</p>
            </div>
            <div class="step-box step-2">
              <span class="step-badge">Step 2: Solve for x</span>
              <p>3x − 10 = x + 30 ⇒ 3x − x = 30 + 10 ⇒ 2x = 40 ⇒ <strong>x = 20</strong>.</p>
            </div>
            <div class="step-box step-3">
              <span class="step-badge">Step 3: Calculate Angles</span>
              <p>• ∠P = 3(20) − 10 = 60 − 10 = <strong>50°</strong>.<br>
              • ∠R = 20 + 30 = <strong>50°</strong>.<br>
              • Adjacent angle ∠Q = 180° − 50° = <strong>130°</strong>.<br>
              • Opposite angle ∠S = ∠Q = <strong>130°</strong>.</p>
            </div>
            <div class="step-box step-4">
              <span class="step-badge">Step 4: Final Result</span>
              <p>The four angles are <strong>50°, 130°, 50°, 130°</strong>.</p>
            </div>
          </div>
        </div>
      </details>

      <!-- PYQ 2 -->
      <details class="ans-box">
        <summary>
          <span><i class="fa-solid fa-scroll" style="color: var(--primary); margin-right: 0.5rem;"></i> PYQ 2 (CBSE 2022): Rectangle Diagonals Center Angle</span>
        </summary>
        <div class="ans-content">
          <p><strong>Question:</strong> The diagonals of a rectangle ABCD intersect at O. If ∠BOC = 68°, find the measure of ∠OAD.</p>
          <div class="step-container">
            <div class="step-box step-1">
              <span class="step-badge">Step 1: Vertically Opposite Angles</span>
              <p>In rectangle ABCD, ∠AOD and ∠BOC are vertically opposite angles: <strong>∠AOD = ∠BOC = 68°</strong>.</p>
            </div>
            <div class="step-box step-2">
              <span class="step-badge">Step 2: Isosceles Triangle Property</span>
              <p>Diagonals of a rectangle are equal and bisect each other: OA = OD. Therefore, △AOD is an isosceles triangle with base angles ∠OAD = ∠ODA.</p>
            </div>
            <div class="step-box step-3">
              <span class="step-badge">Step 3: Compute Base Angle</span>
              <p>In △AOD: ∠OAD + ∠ODA + ∠AOD = 180°<br>
              2(∠OAD) + 68° = 180° ⇒ 2(∠OAD) = 112° ⇒ <strong>∠OAD = 56°</strong>.</p>
            </div>
          </div>
        </div>
      </details>

      <!-- PYQ 3 -->
      <details class="ans-box">
        <summary>
          <span><i class="fa-solid fa-scroll" style="color: var(--primary); margin-right: 0.5rem;"></i> PYQ 3 (BSE Odisha 2024 Model): Perimeter Equivalence Between Square &amp; Rhombus</span>
        </summary>
        <div class="ans-content">
          <p><strong>Question:</strong> The perimeter of a square is equal to the perimeter of a rhombus with diagonals 12 cm and 16 cm. Find the side of the square and compare the areas of both figures.</p>
          <div class="step-container">
            <div class="step-box step-1">
              <span class="step-badge">Step 1: Rhombus Side &amp; Perimeter</span>
              <p>Half diagonals = 6 cm and 8 cm. Rhombus side = √(6² + 8²) = √(36 + 64) = √100 = <strong>10 cm</strong>.<br>
              Perimeter = 4 × 10 cm = <strong>40 cm</strong>.</p>
            </div>
            <div class="step-box step-2">
              <span class="step-badge">Step 2: Square Side &amp; Area</span>
              <p>Perimeter of square = 40 cm ⇒ Side of square a = 40 ÷ 4 = <strong>10 cm</strong>.<br>
              Area of Square = a² = 10² = <strong>100 cm²</strong>.</p>
            </div>
            <div class="step-box step-3">
              <span class="step-badge">Step 3: Rhombus Area</span>
              <p>Area of Rhombus = ½ × d₁ × d₂ = ½ × 12 × 16 = <strong>96 cm²</strong>.</p>
            </div>
            <div class="step-box step-4">
              <span class="step-badge">Step 4: Comparison</span>
              <p>Although both figures have the identical perimeter (40 cm), the <strong>Square has a larger area (100 cm²)</strong> than the Rhombus (96 cm²) by 4 cm²! (A square maximizes area for a given perimeter).</p>
            </div>
          </div>
        </div>
      </details>

      <!-- PYQ 4 -->
      <details class="ans-box">
        <summary>
          <span><i class="fa-solid fa-scroll" style="color: var(--primary); margin-right: 0.5rem;"></i> PYQ 4 (CBSE 2021): Metrics of Square with Diagonal 10 cm</span>
        </summary>
        <div class="ans-content">
          <p><strong>Question:</strong> If the diagonal of a square is 10 cm, find its exact area and perimeter.</p>
          <div class="step-container">
            <div class="step-box step-1">
              <span class="step-badge">Step 1: Area from Diagonal</span>
              <p>For any square: Area = ½ × d² = ½ × 10² = ½ × 100 = <strong>50 cm²</strong>.</p>
            </div>
            <div class="step-box step-2">
              <span class="step-badge">Step 2: Side Length Calculation</span>
              <p>d = a√2 ⇒ a = d / √2 = 10 / √2 = 5√2 cm ≈ <strong>7.07 cm</strong>.</p>
            </div>
            <div class="step-box step-3">
              <span class="step-badge">Step 3: Perimeter Calculation</span>
              <p>Perimeter = 4a = 4 × (5√2) = <strong>20√2 cm</strong> ≈ <strong>28.28 cm</strong>.</p>
            </div>
          </div>
        </div>
      </details>

      <!-- PYQ 5 -->
      <details class="ans-box">
        <summary>
          <span><i class="fa-solid fa-scroll" style="color: var(--primary); margin-right: 0.5rem;"></i> PYQ 5 (Exemplar Challenge): Proving Square from Diagonals</span>
        </summary>
        <div class="ans-content">
          <p><strong>Question:</strong> Prove that if the diagonals of a quadrilateral are equal in length and bisect each other at right angles, then the quadrilateral is a square.</p>
          <div class="step-container">
            <div class="step-box step-1">
              <span class="step-badge">Step 1: Given Conditions</span>
              <p>Quadrilateral ABCD has: (1) AC = BD, (2) OA = OC and OB = OD, (3) AC ⊥ BD (∠AOB = 90°).</p>
            </div>
            <div class="step-box step-2">
              <span class="step-badge">Step 2: Prove Parallelogram</span>
              <p>Since diagonals bisect each other (OA = OC, OB = OD), ABCD is a <strong>Parallelogram</strong>.</p>
            </div>
            <div class="step-box step-3">
              <span class="step-badge">Step 3: Prove Rhombus</span>
              <p>In △AOB and △COB: OA = OC, OB = OB, ∠AOB = ∠COB = 90°. By SAS Congruence: △AOB ≅ △COB ⇒ AB = BC. A parallelogram with equal adjacent sides is a <strong>Rhombus</strong>.</p>
            </div>
            <div class="step-box step-4">
              <span class="step-badge">Step 4: Prove Rectangle &amp; Square</span>
              <p>In △ABC and △BAD: AB = AB, BC = AD, AC = BD (given). By SSS Congruence: △ABC ≅ △BAD ⇒ ∠ABC = ∠BAD. Since adjacent angles in a parallelogram sum to 180°: ∠ABC + ∠BAD = 180° ⇒ 2(∠ABC) = 180° ⇒ ∠ABC = 90°.<br>
              Since ABCD is a rhombus with a 90° angle, it is strictly a <strong>Square</strong>!</p>
            </div>
          </div>
        </div>
      </details>
    </section>
"""
