# -*- coding: utf-8 -*-
"""Part 8: Section 5 - Complete Exam Question Bank (27 Exhaustive Questions)."""

SECTION5_CONTENT = """
    <!-- SECTION 5: COMPLETE EXAM QUESTION BANK (27 QUESTIONS) -->
    <section id="exam-bank" class="section-card">
      <div class="section-header">
        <div class="section-icon-box">
          <i class="fa-solid fa-file-pen"></i>
        </div>
        <div>
          <h2 class="section-title">Section 5: Complete Exam Question Bank</h2>
          <p class="section-tagline">27 high-yield exam questions: Interactive MCQs, Assertion-Reasoning, SAQs, LAQs with marking schemes, Case Studies, and PYQs</p>
        </div>
      </div>

      <!-- PART A: 5 CONCEPTUAL MCQS WITH INTERACTIVE ENGINE -->
      <h3 class="subheading"><i class="fa-solid fa-circle-question"></i> Part A: Conceptual MCQs (Interactive Quiz Engine)</h3>
      <p>
        Click on your chosen option to instantly test your conceptual understanding. The quiz engine immediately highlights correct answers in green, traps in red, and provides detailed pedagogical explanations.
      </p>

      <!-- MCQ 1 -->
      <div class="quiz-card" id="quiz-mcq1">
        <div class="quiz-question">
          <strong>Question 1:</strong> A straight transversal line cuts across two distinct non-parallel straight lines on a plane. What is the <em>maximum</em> possible number of distinct angle measures that can be formed?
        </div>
        <div class="quiz-options">
          <button class="option-btn" onclick="checkQuiz('mcq1', 0, false)"><i class="fa-regular fa-circle"></i> A) 8 distinct angle measures</button>
          <button class="option-btn" onclick="checkQuiz('mcq1', 1, false)"><i class="fa-regular fa-circle"></i> B) 6 distinct angle measures</button>
          <button class="option-btn" onclick="checkQuiz('mcq1', 2, true)"><i class="fa-regular fa-circle"></i> C) 4 distinct angle measures</button>
          <button class="option-btn" onclick="checkQuiz('mcq1', 3, false)"><i class="fa-regular fa-circle"></i> D) 2 distinct angle measures</button>
        </div>
        <div class="quiz-feedback" id="feedback-mcq1">
          <strong>Correct Answer: C (4 distinct angle measures).</strong><br>
          <span style="color: #64748b;">Trap Explanation:</span> Many students jump to Option A because 8 total angles are drawn. However, around every intersection vertex, vertically opposite angles are strictly equal (<span class="math-inline">∠1 = ∠3</span>, <span class="math-inline">∠2 = ∠4</span>, etc.). Therefore, each intersection can produce at most 2 distinct measures. For 2 intersections, the maximum possible distinct measures is <span class="math-inline">2 + 2 = 4</span>!
        </div>
      </div>

      <!-- MCQ 2 -->
      <div class="quiz-card" id="quiz-mcq2">
        <div class="quiz-question">
          <strong>Question 2:</strong> If two parallel lines are intersected by a transversal, each pair of interior angles on the same side of the transversal is:
        </div>
        <div class="quiz-options">
          <button class="option-btn" onclick="checkQuiz('mcq2', 0, false)"><i class="fa-regular fa-circle"></i> A) Equal in measure</button>
          <button class="option-btn" onclick="checkQuiz('mcq2', 1, false)"><i class="fa-regular fa-circle"></i> B) Complementary (Sum = 90°)</button>
          <button class="option-btn" onclick="checkQuiz('mcq2', 2, true)"><i class="fa-regular fa-circle"></i> C) Supplementary (Sum = 180°)</button>
          <button class="option-btn" onclick="checkQuiz('mcq2', 3, false)"><i class="fa-regular fa-circle"></i> D) Always obtuse</button>
        </div>
        <div class="quiz-feedback" id="feedback-mcq2">
          <strong>Correct Answer: C (Supplementary).</strong><br>
          <span style="color: #64748b;">Trap Explanation:</span> Students frequently confuse "Equal" (which applies to alternate interior angles and corresponding angles) with "Supplementary" (which applies to consecutive interior angles). Consecutive interior angles are only equal if both are 90°! Their sum is always 180°.
        </div>
      </div>

      <!-- MCQ 3 -->
      <div class="quiz-card" id="quiz-mcq3">
        <div class="quiz-question">
          <strong>Question 3:</strong> Two straight lines intersect at point O. The angle formed between the bisectors of any two adjacent angles forming a linear pair is always:
        </div>
        <div class="quiz-options">
          <button class="option-btn" onclick="checkQuiz('mcq3', 0, false)"><i class="fa-regular fa-circle"></i> A) 45° (Acute)</button>
          <button class="option-btn" onclick="checkQuiz('mcq3', 1, false)"><i class="fa-regular fa-circle"></i> B) 60° (Equilateral component)</button>
          <button class="option-btn" onclick="checkQuiz('mcq3', 2, true)"><i class="fa-regular fa-circle"></i> C) 90° (A right angle)</button>
          <button class="option-btn" onclick="checkQuiz('mcq3', 3, false)"><i class="fa-regular fa-circle"></i> D) 180° (A straight angle)</button>
        </div>
        <div class="quiz-feedback" id="feedback-mcq3">
          <strong>Correct Answer: C (90° - A right angle).</strong><br>
          <span style="color: #64748b;">Mathematical Proof:</span> Let the linear pair angles be <span class="math-inline">2x</span> and <span class="math-inline">2y</span>. Since they form a linear pair: <span class="math-inline">2x + 2y = 180°</span>. Dividing the entire equation by 2 gives: <span class="math-inline">x + y = 90°</span>. Since the angle between the bisectors is <span class="math-inline">x + y</span>, it is always an exact right angle of 90°!
        </div>
      </div>

      <!-- MCQ 4 -->
      <div class="quiz-card" id="quiz-mcq4">
        <div class="quiz-question">
          <strong>Question 4:</strong> A transversal line intersects two coplanar lines l and m. Which of the following conditions is <strong>NOT sufficient</strong> to prove that line l is parallel to line m?
        </div>
        <div class="quiz-options">
          <button class="option-btn" onclick="checkQuiz('mcq4', 0, false)"><i class="fa-regular fa-circle"></i> A) One pair of alternate interior angles is equal</button>
          <button class="option-btn" onclick="checkQuiz('mcq4', 1, false)"><i class="fa-regular fa-circle"></i> B) One pair of corresponding angles is equal</button>
          <button class="option-btn" onclick="checkQuiz('mcq4', 2, true)"><i class="fa-regular fa-circle"></i> C) One pair of vertically opposite angles is equal</button>
          <button class="option-btn" onclick="checkQuiz('mcq4', 3, false)"><i class="fa-regular fa-circle"></i> D) Interior angles on the same side sum to 180°</button>
        </div>
        <div class="quiz-feedback" id="feedback-mcq4">
          <strong>Correct Answer: C (One pair of vertically opposite angles is equal).</strong><br>
          <span style="color: #64748b;">Trap Explanation:</span> Vertically opposite angles are <em>always equal</em> whenever ANY two lines cross, whether the other line is parallel, perpendicular, or tilted at 1 degree! It gives zero information about whether line l is parallel to line m.
        </div>
      </div>

      <!-- MCQ 5 -->
      <div class="quiz-card" id="quiz-mcq5">
        <div class="quiz-question">
          <strong>Question 5:</strong> An angle measures 24° more than its complement. What is the measure of the <strong>supplement</strong> of this angle?
        </div>
        <div class="quiz-options">
          <button class="option-btn" onclick="checkQuiz('mcq5', 0, false)"><i class="fa-regular fa-circle"></i> A) 33°</button>
          <button class="option-btn" onclick="checkQuiz('mcq5', 1, false)"><i class="fa-regular fa-circle"></i> B) 57°</button>
          <button class="option-btn" onclick="checkQuiz('mcq5', 2, true)"><i class="fa-regular fa-circle"></i> C) 123°</button>
          <button class="option-btn" onclick="checkQuiz('mcq5', 3, false)"><i class="fa-regular fa-circle"></i> D) 147°</button>
        </div>
        <div class="quiz-feedback" id="feedback-mcq5">
          <strong>Correct Answer: C (123°).</strong><br>
          <span style="color: #64748b;">Step-by-Step Calculation:</span> Let the angle be <span class="math-inline">x</span>. Its complement is <span class="math-inline">90° - x</span>.<br>
          According to the question: <span class="math-inline">x = (90° - x) + 24° ⇒ 2x = 114° ⇒ x = 57°</span>.<br>
          <em>The Trap:</em> 57° is option B! But the question asked for its <strong>supplement</strong>:<br>
          <span class="math-inline">Supplement = 180° - 57° = 123°</span>. Always read the final question word carefully!
        </div>
      </div>

      <!-- PART B: 5 ASSERTION & REASONING QUESTIONS -->
      <h3 class="subheading"><i class="fa-solid fa-scale-balanced"></i> Part B: Assertion &amp; Reasoning Questions</h3>
      <p>
        <strong>Directions:</strong> In the following questions, a statement of Assertion (A) is followed by a statement of Reason (R). Choose the correct option from:<br>
        <strong>(A)</strong> Both (A) and (R) are true, and (R) is the correct explanation of (A).<br>
        <strong>(B)</strong> Both (A) and (R) are true, but (R) is NOT the correct explanation of (A).<br>
        <strong>(C)</strong> (A) is true, but (R) is false.<br>
        <strong>(D)</strong> (A) is false, but (R) is true.
      </p>

      <!-- A&R 1 -->
      <div class="callout callout-def">
        <p><strong>A&amp;R Question 1:</strong></p>
        <p><strong>Assertion (A):</strong> When two straight lines intersect, vertically opposite angles are always equal.</p>
        <p><strong>Reason (R):</strong> The sum of two adjacent angles forming a linear pair along a straight line is always 180°.</p>
        <p><strong>Correct Option: (A)</strong></p>
        <p><em>Deep Explanation:</em> Both statements are mathematically true. Furthermore, Reason (R) is the exact mathematical foundation used to prove Assertion (A): because <span class="math-inline">∠a + ∠b = 180°</span> and <span class="math-inline">∠b + ∠c = 180°</span>, subtracting <span class="math-inline">∠b</span> proves <span class="math-inline">∠a = ∠c</span>. Thus, (R) correctly explains (A).</p>
      </div>

      <!-- A&R 2 -->
      <div class="callout callout-def">
        <p><strong>A&amp;R Question 2:</strong></p>
        <p><strong>Assertion (A):</strong> Two straight lines in a plane that are both perpendicular to the same transversal line are parallel to each other.</p>
        <p><strong>Reason (R):</strong> If a transversal cuts two lines such that corresponding angles are equal, the lines are guaranteed to be parallel.</p>
        <p><strong>Correct Option: (A)</strong></p>
        <p><em>Deep Explanation:</em> If line <span class="math-inline">l ⊥ t</span> and line <span class="math-inline">m ⊥ t</span>, both lines make an angle of 90° with transversal <span class="math-inline">t</span>. These angles are in corresponding positions. Since both equal 90°, corresponding angles are equal, which proves <span class="math-inline">l ∥ m</span> by Reason (R).</p>
      </div>

      <!-- A&R 3 -->
      <div class="callout callout-def">
        <p><strong>A&amp;R Question 3:</strong></p>
        <p><strong>Assertion (A):</strong> If two straight lines in three-dimensional space never meet, they are always parallel.</p>
        <p><strong>Reason (R):</strong> Parallel lines are defined as straight lines lying on the same flat plane that never intersect however far extended.</p>
        <p><strong>Correct Option: (D) — (A) is false, but (R) is true!</strong></p>
        <p><em>Deep Explanation:</em> Assertion (A) is completely false because in 3D space, lines can be <strong>skew</strong> (non-coplanar lines that never meet and are not parallel). Reason (R) is true because it correctly includes the mandatory condition of being <em>coplanar</em>.</p>
      </div>

      <!-- A&R 4 -->
      <div class="callout callout-def">
        <p><strong>A&amp;R Question 4:</strong></p>
        <p><strong>Assertion (A):</strong> When two parallel lines are intersected by a transversal, the interior angles on the same side of the transversal are supplementary.</p>
        <p><strong>Reason (R):</strong> Alternate interior angles formed by a transversal intersecting parallel lines are equal.</p>
        <p><strong>Correct Option: (B)</strong></p>
        <p><em>Deep Explanation:</em> Both statements are mathematically true theorems. However, Reason (R) (equality of alternate interior angles) is not the direct explanation for Assertion (A); Assertion (A) is directly explained by combining linear pairs with corresponding angles (<span class="math-inline">∠2 + ∠3 = 180°</span> and <span class="math-inline">∠2 = ∠6</span>).</p>
      </div>

      <!-- A&R 5 -->
      <div class="callout callout-def">
        <p><strong>A&amp;R Question 5:</strong></p>
        <p><strong>Assertion (A):</strong> Folding a square sheet of paper horizontally 3 times creates a total of 9 parallel lines.</p>
        <p><strong>Reason (R):</strong> The general mathematical formula for the number of parallel lines formed by <span class="math-inline">n</span> successive folds is <span class="math-inline">2ⁿ + 1</span>.</p>
        <p><strong>Correct Option: (A)</strong></p>
        <p><em>Deep Explanation:</em> Substituting <span class="math-inline">n = 3</span> into the formula gives <span class="math-inline">2³ + 1 = 8 + 1 = 9</span> parallel lines. Both statements are true and Reason (R) provides the exact mathematical formula that explains Assertion (A).</p>
      </div>

      <!-- PART C: 6 SHORT ANSWER QUESTIONS (2M & 3M) -->
      <h3 class="subheading"><i class="fa-solid fa-pen-clip"></i> Part C: Short Answer Questions (2M / 3M)</h3>

      <!-- SAQ 1 -->
      <div class="callout callout-pyq">
        <p><strong>SAQ 1 (2 Marks):</strong> Two supplementary angles are in the ratio <span class="math-inline">4 : 5</span>. Find the exact degree measure of both angles.</p>
        <div class="mark-scheme">
          <div class="mark-scheme-title">Marking Scheme</div>
          <div class="mark-item"><span>Let angles be 4x and 5x; state 4x + 5x = 180°</span><span class="mark-val">1 Mark</span></div>
          <div class="mark-item"><span>Solve 9x = 180° ⇒ x = 20°; calculate 80° and 100°</span><span class="mark-val">1 Mark</span></div>
        </div>
        <p><strong>Model Answer:</strong><br>
          Let the two angles be <span class="math-inline">4x</span> and <span class="math-inline">5x</span>.<br>
          Since supplementary angles add up to 180°:<br>
          <span class="math-inline">4x + 5x = 180° ⇒ 9x = 180° ⇒ x = 180° ÷ 9 = 20°</span>.<br>
          First angle = <span class="math-inline">4 × 20° = 80°</span>.<br>
          Second angle = <span class="math-inline">5 × 20° = 100°</span>.<br>
          <strong>Final Answer: The angles are 80° and 100°.</strong>
        </p>
      </div>

      <!-- SAQ 2 -->
      <div class="callout callout-pyq">
        <p><strong>SAQ 2 (2 Marks):</strong> Prove that the angle bisectors of two vertically opposite angles lie along the exact same straight line (are collinear).</p>
        <div class="mark-scheme">
          <div class="mark-scheme-title">Marking Scheme</div>
          <div class="mark-item"><span>Establish angle bisector relations around vertex</span><span class="mark-val">1 Mark</span></div>
          <div class="mark-item"><span>Sum angles to show total measure = 180° (straight line)</span><span class="mark-val">1 Mark</span></div>
        </div>
        <p><strong>Model Answer:</strong><br>
          Let lines <span class="math-inline">AB</span> and <span class="math-inline">CD</span> intersect at <span class="math-inline">O</span>. Vertically opposite angles are <span class="math-inline">∠AOD</span> and <span class="math-inline">∠BOC</span>.<br>
          Let ray <span class="math-inline">OE</span> bisect <span class="math-inline">∠AOD</span>, so <span class="math-inline">∠AOE = ∠EOD = x</span>. Therefore, <span class="math-inline">∠AOD = 2x</span>.<br>
          Since vertically opposite angles are equal, <span class="math-inline">∠BOC = 2x</span>. Let ray <span class="math-inline">OF</span> bisect <span class="math-inline">∠BOC</span>, so <span class="math-inline">∠BOF = ∠FOC = x</span>.<br>
          Now, <span class="math-inline">∠AOD</span> and <span class="math-inline">∠AOC</span> form a linear pair on line <span class="math-inline">CD</span>, so <span class="math-inline">2x + ∠AOC = 180°</span>.<br>
          Consider the total angle along rays <span class="math-inline">OE</span> and <span class="math-inline">OF</span>:<br>
          <span class="math-inline">∠EOF = ∠AOE + ∠AOC + ∠COF = x + ∠AOC + x = 2x + ∠AOC = 180°</span>.<br>
          Since <span class="math-inline">∠EOF = 180°</span>, rays <span class="math-inline">OE</span> and <span class="math-inline">OF</span> form opposite rays along a single straight line. <strong>Hence proved.</strong>
        </p>
      </div>

      <!-- SAQ 3 -->
      <div class="callout callout-pyq">
        <p><strong>SAQ 3 (3 Marks):</strong> In a figure, line <span class="math-inline">l ∥ m</span> and line <span class="math-inline">m ∥ n</span>. A transversal <span class="math-inline">t</span> intersects them. If the ratio of interior angles <span class="math-inline">x : y = 2 : 3</span>, where <span class="math-inline">x</span> and <span class="math-inline">y</span> are interior angles on the same side between lines <span class="math-inline">l</span> and <span class="math-inline">m</span>, and <span class="math-inline">z</span> is alternate to <span class="math-inline">y</span> on line <span class="math-inline">n</span>, find <span class="math-inline">x, y,</span> and <span class="math-inline">z</span>.</p>
        <div class="mark-scheme">
          <div class="mark-scheme-title">Marking Scheme</div>
          <div class="mark-item"><span>Apply co-interior rule: x + y = 180° and solve for x and y</span><span class="mark-val">1.5 Marks</span></div>
          <div class="mark-item"><span>Apply alternate interior rule between m and n to find z</span><span class="mark-val">1.5 Marks</span></div>
        </div>
        <p><strong>Model Answer:</strong><br>
          1. Since <span class="math-inline">l ∥ m</span> and <span class="math-inline">x, y</span> are interior angles on the same side of transversal <span class="math-inline">t</span>:<br>
          <span class="math-inline">x + y = 180°</span>.<br>
          Given <span class="math-inline">x : y = 2 : 3</span>, let <span class="math-inline">x = 2k</span> and <span class="math-inline">y = 3k</span>.<br>
          <span class="math-inline">2k + 3k = 180° ⇒ 5k = 180° ⇒ k = 36°</span>.<br>
          <span class="math-inline">x = 2 × 36° = 72°</span>.<br>
          <span class="math-inline">y = 3 × 36° = 108°</span>.<br>
          2. Since <span class="math-inline">m ∥ n</span> and <span class="math-inline">z</span> is alternate interior to <span class="math-inline">y</span>:<br>
          <span class="math-inline">z = y = 108°</span>.<br>
          <strong>Final Answer: x = 72°, y = 108°, and z = 108°.</strong>
        </p>
      </div>

      <!-- SAQ 4 -->
      <div class="callout callout-pyq">
        <p><strong>SAQ 4 (3 Marks):</strong> If a transversal intersects two parallel lines, prove that the bisectors of any pair of alternate interior angles are parallel to each other.</p>
        <div class="mark-scheme">
          <div class="mark-scheme-title">Marking Scheme</div>
          <div class="mark-item"><span>State alternate interior angles equal: ∠ABC = ∠BCD</span><span class="mark-val">1 Mark</span></div>
          <div class="mark-item"><span>Halve both sides to show ∠1 = ∠2</span><span class="mark-val">1 Mark</span></div>
          <div class="mark-item"><span>Conclude bisectors are parallel via converse alternate angles test</span><span class="mark-val">1 Mark</span></div>
        </div>
        <p><strong>Model Answer:</strong><br>
          1. Let parallel lines <span class="math-inline">AB ∥ CD</span> be intersected by transversal <span class="math-inline">BC</span>.<br>
          2. Alternate interior angles are equal: <span class="math-inline">∠ABC = ∠BCD</span>.<br>
          3. Let ray <span class="math-inline">BM</span> bisect <span class="math-inline">∠ABC</span>, and ray <span class="math-inline">CN</span> bisect <span class="math-inline">∠BCD</span>.<br>
          4. Then <span class="math-inline">∠MBC = ½ ∠ABC</span> and <span class="math-inline">∠NCB = ½ ∠BCD</span>.<br>
          5. Since <span class="math-inline">∠ABC = ∠BCD</span>, dividing by 2 gives: <span class="math-inline">∠MBC = ∠NCB</span>.<br>
          6. But <span class="math-inline">∠MBC</span> and <span class="math-inline">∠NCB</span> are alternate interior angles for lines <span class="math-inline">BM</span> and <span class="math-inline">CN</span> with transversal <span class="math-inline">BC</span>.<br>
          7. By the Converse of the Alternate Interior Angles Test, line <span class="math-inline">BM ∥ CN</span>. <strong>Hence proved!</strong>
        </p>
      </div>

      <!-- SAQ 5 -->
      <div class="callout callout-pyq">
        <p><strong>SAQ 5 (3 Marks):</strong> An angle is equal to one-third of its supplement. Find the measure of the angle and the measure of its complement.</p>
        <div class="mark-scheme">
          <div class="mark-scheme-title">Marking Scheme</div>
          <div class="mark-item"><span>Formulate equation x = (180 - x) / 3 and solve for x</span><span class="mark-val">1.5 Marks</span></div>
          <div class="mark-item"><span>Calculate complement 90° - x</span><span class="mark-val">1.5 Marks</span></div>
        </div>
        <p><strong>Model Answer:</strong><br>
          1. Let the angle be <span class="math-inline">x</span>. Its supplement is <span class="math-inline">180° - x</span>.<br>
          2. Given condition: <span class="math-inline">x = ⅓(180° - x)</span>.<br>
          Multiplying both sides by 3:<br>
          <span class="math-inline">3x = 180° - x ⇒ 4x = 180° ⇒ x = 180° ÷ 4 = 45°</span>.<br>
          3. The measure of the angle is <strong>45°</strong>.<br>
          4. Its complement is: <span class="math-inline">90° - 45° = 45°</span>.<br>
          <strong>Final Answer: The angle is 45°, and its complement is 45°.</strong>
        </p>
      </div>

      <!-- SAQ 6 -->
      <div class="callout callout-pyq">
        <p><strong>SAQ 6 (3 Marks):</strong> In △ABC, line segment DE is drawn parallel to base BC, intersecting side AB at D and AC at E. If <span class="math-inline">∠ADE = 50°</span> and <span class="math-inline">∠AED = 70°</span>, find the measures of <span class="math-inline">∠B, ∠C,</span> and <span class="math-inline">∠A</span> of △ABC.</p>
        <div class="mark-scheme">
          <div class="mark-scheme-title">Marking Scheme</div>
          <div class="mark-item"><span>Use corresponding angles to find ∠B = 50° and ∠C = 70°</span><span class="mark-val">1.5 Marks</span></div>
          <div class="mark-item"><span>Use angle sum property of triangle to find ∠A = 60°</span><span class="mark-val">1.5 Marks</span></div>
        </div>
        <p><strong>Model Answer:</strong><br>
          1. Since <span class="math-inline">DE ∥ BC</span> and <span class="math-inline">AB</span> is a transversal:<br>
          <span class="math-inline">∠B = ∠ADE = 50°</span> (Corresponding angles).<br>
          2. Since <span class="math-inline">DE ∥ BC</span> and <span class="math-inline">AC</span> is a transversal:<br>
          <span class="math-inline">∠C = ∠AED = 70°</span> (Corresponding angles).<br>
          3. In △ABC, the sum of all three interior angles is 180°:<br>
          <span class="math-inline">∠A + ∠B + ∠C = 180° ⇒ ∠A + 50° + 70° = 180° ⇒ ∠A + 120° = 180° ⇒ ∠A = 60°</span>.<br>
          <strong>Final Answer: ∠B = 50°, ∠C = 70°, and ∠A = 60°.</strong>
        </p>
      </div>

      <!-- PART D: 4 LONG ANSWER QUESTIONS (5M) WITH STEP-BY-STEP MARKING SCHEMES -->
      <h3 class="subheading"><i class="fa-solid fa-award"></i> Part D: Long Answer Questions (5 Marks Each)</h3>

      <!-- LAQ 1 -->
      <div class="callout callout-def">
        <p><strong>LAQ 1 (5 Marks):</strong> Prove that if two parallel lines are intersected by a transversal, the bisectors of the four interior angles enclose a rectangle.</p>
        <div class="mark-scheme">
          <div class="mark-scheme-title">CBSE Topper Marking Scheme (5 Marks Total)</div>
          <div class="mark-item"><span>Given, To Prove, and neat labelled diagram</span><span class="mark-val">1 Mark</span></div>
          <div class="mark-item"><span>Prove opposite sides of quadrilateral are parallel (parallelogram)</span><span class="mark-val">2 Marks</span></div>
          <div class="mark-item"><span>Prove one interior corner angle is 90° using linear/co-interior pair</span><span class="mark-val">1.5 Marks</span></div>
          <div class="mark-item"><span>Conclude that a parallelogram with a 90° angle is a rectangle</span><span class="mark-val">0.5 Mark</span></div>
        </div>
        <p><strong>Model Answer:</strong><br>
          <strong>Given:</strong> Parallel lines <span class="math-inline">AB ∥ CD</span> cut by transversal <span class="math-inline">EF</span> at points <span class="math-inline">G</span> and <span class="math-inline">H</span>. Rays <span class="math-inline">GM, GN, HM, HN</span> bisect interior angles <span class="math-inline">∠BGH, ∠AGH, ∠CHG, ∠DHG</span> respectively, meeting to form quadrilateral <span class="math-inline">GMHN</span>.<br>
          <strong>To Prove:</strong> Quadrilateral <span class="math-inline">GMHN</span> is a rectangle.<br><br>
          <strong>Proof:</strong><br>
          1. <em>Proving GMHN is a parallelogram:</em><br>
          Since <span class="math-inline">AB ∥ CD</span>, alternate interior angles are equal: <span class="math-inline">∠AGH = ∠DHG</span>.<br>
          Halving both sides: <span class="math-inline">½ ∠AGH = ½ ∠DHG ⇒ ∠NGH = ∠MHG</span>.<br>
          Since these are alternate interior angles for lines <span class="math-inline">GN</span> and <span class="math-inline">HM</span> with transversal <span class="math-inline">GH</span>, it follows that <span class="math-inline">GN ∥ HM</span>.<br>
          Similarly, <span class="math-inline">∠BGH = ∠CHG ⇒ ½ ∠BGH = ½ ∠CHG ⇒ ∠MGH = ∠NHG ⇒ GM ∥ HN</span>.<br>
          Since both pairs of opposite sides are parallel (<span class="math-inline">GN ∥ HM</span> and <span class="math-inline">GM ∥ HN</span>), <span class="math-inline">GMHN</span> is a <strong>parallelogram</strong>.<br><br>
          2. <em>Proving one corner angle is 90°:</em><br>
          Angles <span class="math-inline">∠AGH</span> and <span class="math-inline">∠BGH</span> form a linear pair on straight line <span class="math-inline">AB</span>:<br>
          <span class="math-inline">∠AGH + ∠BGH = 180°</span>.<br>
          Dividing the entire equation by 2:<br>
          <span class="math-inline">½ ∠AGH + ½ ∠BGH = 90°</span>.<br>
          <span class="math-inline">∠NGH + ∠MGH = 90° ⇒ ∠MGN = 90°</span>.<br><br>
          3. <em>Conclusion:</em> A parallelogram with at least one right angle is a <strong>rectangle</strong>.<br>
          Therefore, quadrilateral <span class="math-inline">GMHN</span> is a rectangle. <strong>Q.E.D. Hence Proved!</strong>
        </p>
      </div>

      <!-- LAQ 2 -->
      <div class="callout callout-def">
        <p><strong>LAQ 2 (5 Marks):</strong> In a geometric system, line <span class="math-inline">AB ∥ CD</span>. Transversals <span class="math-inline">PQ</span> and <span class="math-inline">RS</span> intersect at point <span class="math-inline">O</span> between the parallel lines. If <span class="math-inline">∠POB = (3x + 10)°</span>, <span class="math-inline">∠QOD = (2y - 5)°</span>, <span class="math-inline">∠AOR = (x + 2y)°</span>, and <span class="math-inline">∠ROB = 75°</span>, set up linear algebraic equations and find the values of <span class="math-inline">x, y</span>, and all four angles.</p>
        <div class="mark-scheme">
          <div class="mark-scheme-title">Marking Scheme (5 Marks Total)</div>
          <div class="mark-item"><span>State linear pair relation: (x + 2y) + 75° = 180° ⇒ x + 2y = 105°</span><span class="mark-val">1.5 Marks</span></div>
          <div class="mark-item"><span>State vertically opposite relation: 3x + 10 = 2y - 5 (or equivalent)</span><span class="mark-val">1.5 Marks</span></div>
          <div class="mark-item"><span>Solve linear system for x and y</span><span class="mark-val">1 Mark</span></div>
          <div class="mark-item"><span>Compute degree values of all four angles with units</span><span class="mark-val">1 Mark</span></div>
        </div>
        <p><strong>Model Answer:</strong><br>
          1. Angles <span class="math-inline">∠AOR</span> and <span class="math-inline">∠ROB</span> form a linear pair along line <span class="math-inline">AB</span>:<br>
          <span class="math-inline">(x + 2y) + 75° = 180° ⇒ x + 2y = 105° &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;--- (Equation 1)</span><br><br>
          2. When lines <span class="math-inline">AB</span> and transversal <span class="math-inline">PQ</span> intersect, vertically opposite angles across <span class="math-inline">O</span> give:<br>
          Suppose <span class="math-inline">3x + 10 = 85°</span> (since linear pair with <span class="math-inline">∠POA = 95°</span>):<br>
          <span class="math-inline">3x = 75° ⇒ x = 25°</span>.<br><br>
          3. Substitute <span class="math-inline">x = 25°</span> into Equation (1):<br>
          <span class="math-inline">25° + 2y = 105° ⇒ 2y = 80° ⇒ y = 40°</span>.<br><br>
          4. <strong>Angle Values:</strong><br>
          <span class="math-inline">∠POB = 3(25) + 10 = 85°</span>.<br>
          <span class="math-inline">∠QOD = 2(40) - 5 = 80° - 5 = 75°</span>.<br>
          <span class="math-inline">∠AOR = 25 + 2(40) = 105°</span>.<br>
          <span class="math-inline">∠ROB = 75°</span>.<br>
          <strong>Final Answer: x = 25°, y = 40°.</strong>
        </p>
      </div>

      <!-- LAQ 3 -->
      <div class="callout callout-def">
        <p><strong>LAQ 3 (5 Marks):</strong> Comprehensive Axiomatic Proof: Starting strictly from the Corresponding Angles Postulate, prove both of the following fundamental theorems:<br>
        (a) Alternate Interior Angles are equal.<br>
        (b) Consecutive Interior Angles on the same side of the transversal are supplementary.</p>
        <div class="mark-scheme">
          <div class="mark-scheme-title">Marking Scheme (5 Marks Total)</div>
          <div class="mark-item"><span>Clear statement of Corresponding Angles Postulate</span><span class="mark-val">1 Mark</span></div>
          <div class="mark-item"><span>Part (a): Rigorous derivation using vertically opposite angles</span><span class="mark-val">2 Marks</span></div>
          <div class="mark-item"><span>Part (b): Rigorous derivation using linear pair substitution</span><span class="mark-val">2 Marks</span></div>
        </div>
        <p><strong>Model Answer:</strong><br>
          <strong>Corresponding Angles Postulate:</strong> If two parallel lines <span class="math-inline">l ∥ m</span> are cut by transversal <span class="math-inline">t</span>, then corresponding angles in identical relative positions are equal: <span class="math-inline">∠2 = ∠6</span> and <span class="math-inline">∠1 = ∠5</span>.<br><br>
          <strong>(a) Proof that Alternate Interior Angles are Equal:</strong><br>
          Consider alternate interior angles <span class="math-inline">∠4</span> and <span class="math-inline">∠6</span>.<br>
          1. By Corresponding Angles Postulate: <span class="math-inline">∠2 = ∠6</span> (Equation 1).<br>
          2. Angles <span class="math-inline">∠2</span> and <span class="math-inline">∠4</span> are vertically opposite angles at the top vertex, so: <span class="math-inline">∠2 = ∠4</span> (Equation 2).<br>
          3. Equating both equations: <span class="math-inline">∠4 = ∠6</span>.<br>
          Similarly, <span class="math-inline">∠1 = ∠5</span> and <span class="math-inline">∠1 = ∠3 ⇒ ∠3 = ∠5</span>. <strong>Hence Part (a) is proved!</strong><br><br>
          <strong>(b) Proof that Consecutive Interior Angles are Supplementary:</strong><br>
          Consider consecutive interior angles <span class="math-inline">∠3</span> and <span class="math-inline">∠6</span> on the right side of transversal <span class="math-inline">t</span>.<br>
          1. Angles <span class="math-inline">∠2</span> and <span class="math-inline">∠3</span> lie along straight line <span class="math-inline">l</span>, forming a linear pair:<br>
          <span class="math-inline">∠2 + ∠3 = 180°</span> (Equation 3).<br>
          2. But by the Corresponding Angles Postulate, <span class="math-inline">∠2 = ∠6</span>.<br>
          3. Substitute <span class="math-inline">∠6</span> in place of <span class="math-inline">∠2</span> in Equation (3):<br>
          <span class="math-inline">∠6 + ∠3 = 180°</span>.<br>
          Similarly, for the left side: <span class="math-inline">∠1 + ∠4 = 180°</span> and <span class="math-inline">∠1 = ∠5 ⇒ ∠5 + ∠4 = 180°</span>.<br>
          <strong>Hence Part (b) is proved! Both fundamental theorems derived successfully.</strong>
        </p>
      </div>

      <!-- LAQ 4 -->
      <div class="callout callout-def">
        <p><strong>LAQ 4 (5 Marks):</strong> Optical Physics &amp; Parallel Mirrors: Two plane mirrors AB and CD are placed strictly parallel to each other (<span class="math-inline">AB ∥ CD</span>). An incident light ray PQ strikes mirror AB at point Q, reflects along path QR, and strikes mirror CD at point R, reflecting outward along path RS. Using the Law of Reflection (angle of incidence = angle of reflection), prove that the incident ray PQ is strictly parallel to the reflected ray RS (<span class="math-inline">PQ ∥ RS</span>).</p>
        <div class="mark-scheme">
          <div class="mark-scheme-title">Marking Scheme (5 Marks Total)</div>
          <div class="mark-item"><span>Construct normals QM ⊥ AB and RN ⊥ CD; prove QM ∥ RN</span><span class="mark-val">1.5 Marks</span></div>
          <div class="mark-item"><span>Use alternate interior angles between normals to show ∠r₁ = ∠i₂</span><span class="mark-val">1.5 Marks</span></div>
          <div class="mark-item"><span>Apply Law of Reflection to double angles: ∠PQR = ∠QRS</span><span class="mark-val">1 Mark</span></div>
          <div class="mark-item"><span>Apply converse of alternate interior angles to conclude PQ ∥ RS</span><span class="mark-val">1 Mark</span></div>
        </div>
        <p><strong>Model Answer:</strong><br>
          <strong>Construction:</strong> Draw normal <span class="math-inline">QM ⊥ AB</span> at point <span class="math-inline">Q</span>, and draw normal <span class="math-inline">RN ⊥ CD</span> at point <span class="math-inline">R</span>.<br><br>
          <strong>Proof:</strong><br>
          1. Since mirror <span class="math-inline">AB ∥ CD</span> and normals are perpendicular to the mirrors (<span class="math-inline">QM ⊥ AB</span> and <span class="math-inline">RN ⊥ CD</span>), the two normals are parallel to each other: <span class="math-inline">QM ∥ RN</span>.<br>
          2. Ray <span class="math-inline">QR</span> acts as a transversal intersecting the two parallel normals <span class="math-inline">QM</span> and <span class="math-inline">RN</span>. Therefore, alternate interior angles between the normals are equal:<br>
          <span class="math-inline">∠MQR = ∠NRQ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;--- (Equation 1)</span><br>
          Let <span class="math-inline">∠MQR = ∠2</span> (angle of reflection at mirror AB) and <span class="math-inline">∠NRQ = ∠3</span> (angle of incidence at mirror CD). So <span class="math-inline">∠2 = ∠3</span>.<br><br>
          3. By the Law of Reflection of Light:<br>
          At mirror AB: <span class="math-inline">∠PQM = ∠MQR ⇒ ∠1 = ∠2</span>.<br>
          Therefore, total <span class="math-inline">∠PQR = ∠1 + ∠2 = 2∠2</span>.<br>
          At mirror CD: <span class="math-inline">∠NRQ = ∠NRS ⇒ ∠3 = ∠4</span>.<br>
          Therefore, total <span class="math-inline">∠QRS = ∠3 + ∠4 = 2∠3</span>.<br><br>
          4. Since <span class="math-inline">∠2 = ∠3</span> from Equation (1), multiplying both sides by 2 gives:<br>
          <span class="math-inline">2∠2 = 2∠3 ⇒ ∠PQR = ∠QRS</span>.<br><br>
          5. Notice that <span class="math-inline">∠PQR</span> and <span class="math-inline">∠QRS</span> form a pair of alternate interior angles for lines <span class="math-inline">PQ</span> and <span class="math-inline">RS</span> with transversal <span class="math-inline">QR</span>.<br>
          6. By the Converse of the Alternate Interior Angles Test, since alternate interior angles are equal, the rays must be parallel:<br>
          <strong>PQ ∥ RS</strong>. <strong>Q.E.D. Hence Proved!</strong>
        </p>
      </div>

      <!-- PART E: 2 COMPETENCY-BASED CASE STUDIES -->
      <h3 class="subheading"><i class="fa-solid fa-briefcase"></i> Part E: Competency-Based Real-World Case Studies</h3>

      <!-- CASE STUDY 1 -->
      <div class="callout callout-act">
        <p><strong>Case Study 1: High-Speed Vande Bharat Railway Track Engineering</strong></p>
        <p>
          Indian Railways engineers are laying a new electrified high-speed railway corridor outside Bhubaneswar. The two steel rails of the track must remain strictly parallel at a standardized broad gauge distance of <span class="math-inline">1676  mm</span>. At a switching junction, a diagonal crossover track (acting as a transversal <span class="math-inline">t</span>) cuts across both main lines <span class="math-inline">l</span> and <span class="math-inline">m</span>. The acute angle of the track switch with the outer rail is measured by laser sensors to be <span class="math-inline">32°</span>.
        </p>
        <ol style="margin-left: 2rem; line-height: 1.8;">
          <li>What must be the measure of the corresponding angle formed at the inner rail to ensure zero derailment risk?</li>
          <li>What is the measure of the obtuse angle formed by the train wheels as they enter the crossover track?</li>
          <li>If ground subsidence causes the inner rail angle to drift to <span class="math-inline">34°</span>, explain mathematically why train operations must be halted immediately.</li>
        </ol>
        <p><strong>Model Answers:</strong></p>
        <p>1. Since the rails must remain strictly parallel (<span class="math-inline">l ∥ m</span>), the corresponding angle must be <strong>strictly equal to 32°</strong>.</p>
        <p>2. The obtuse angle forms a linear pair along the rail with the acute switch angle: <span class="math-inline">180° - 32° = 148°</span>.</p>
        <p>3. If the inner rail angle becomes <span class="math-inline">34°</span>, then corresponding angles are unequal (<span class="math-inline">32° ≠ 34°</span>). By the Parallel Line Postulate, the rails are no longer parallel! They will either converge (pinching train wheel flanges) or diverge (allowing wheels to drop off the track), causing catastrophic high-speed derailment.</p>
      </div>

      <!-- CASE STUDY 2 -->
      <div class="callout callout-act">
        <p><strong>Case Study 2: Hydraulic Scissor Lift &amp; Roof Truss Linkage</strong></p>
        <p>
          An industrial maintenance scissor lift uses interlocking steel beams to raise a work platform. The platform at the top must remain perfectly horizontal and parallel to the wheeled ground chassis at all heights. The crossing steel beams form repeating "X" linkages where each pair of beams intersects at a central pivot pin.
        </p>
        <ol style="margin-left: 2rem; line-height: 1.8;">
          <li>At a certain height, the angle between the two crossed scissor beams is measured to be <span class="math-inline">74°</span>. What is the measure of the vertically opposite angle?</li>
          <li>What is the measure of the adjacent angle in the scissor pivot?</li>
          <li>Explain how the equality of alternate interior angles across the scissor beams guarantees that the technician's platform never tilts as the lift moves up or down.</li>
        </ol>
        <p><strong>Model Answers:</strong></p>
        <p>1. Vertically opposite angles across the pivot pin are always equal, so the opposite angle is exactly <strong>74°</strong>.</p>
        <p>2. The adjacent angle forms a linear pair on the straight steel beam: <span class="math-inline">180° - 74° = 106°</span>.</p>
        <p>3. Each crossed beam serves as a transversal connecting the bottom chassis and top platform. Because the scissor linkages are built with equal beam lengths forming symmetric alternate interior angles at top and bottom (<span class="math-inline">∠top = ∠bottom</span>), the Converse Alternate Interior Angles Test ensures that the top platform remains strictly parallel to the floor at every extension stage!</p>
      </div>

      <!-- PART F: 5 PREVIOUS YEARS QUESTIONS (PYQS) & MOST PROBABLE EXAM QUESTIONS -->
      <h3 class="subheading"><i class="fa-solid fa-clock-rotate-left"></i> Part F: Previous Years Questions (PYQs) &amp; Most Probable Questions</h3>

      <!-- PYQ 1 -->
      <div class="callout callout-pyq">
        <p><strong>PYQ 1 (CBSE Class 7 Standard):</strong> In the given figure, two straight lines <span class="math-inline">AB</span> and <span class="math-inline">CD</span> intersect at point <span class="math-inline">O</span>. If <span class="math-inline">∠AOC = (3x - 15)°</span> and <span class="math-inline">∠BOD = (2x + 25)°</span>, find the value of <span class="math-inline">x</span> and the measure of all four angles around point <span class="math-inline">O</span>.</p>
        <p><strong>Model Solution:</strong><br>
          1. Angles <span class="math-inline">∠AOC</span> and <span class="math-inline">∠BOD</span> are vertically opposite angles. Since vertically opposite angles are equal:<br>
          <span class="math-inline">3x - 15 = 2x + 25 ⇒ 3x - 2x = 25 + 15 ⇒ x = 40</span>.<br>
          2. <span class="math-inline">∠AOC = 3(40) - 15 = 120 - 15 = 105°</span>.<br>
          3. <span class="math-inline">∠BOD = 2(40) + 25 = 80 + 25 = 105°</span>.<br>
          4. Angles <span class="math-inline">∠AOC</span> and <span class="math-inline">∠AOD</span> form a linear pair along line <span class="math-inline">CD</span>:<br>
          <span class="math-inline">∠AOD = 180° - 105° = 75°</span>.<br>
          5. Vertically opposite angle <span class="math-inline">∠BOC = ∠AOD = 75°</span>.<br>
          <strong>Final Answer: x = 40; ∠AOC = 105°, ∠BOD = 105°, ∠AOD = 75°, ∠BOC = 75°.</strong>
        </p>
      </div>

      <!-- PYQ 2 -->
      <div class="callout callout-pyq">
        <p><strong>PYQ 2 (BSE Odisha / State Board Standard):</strong> In a figure, <span class="math-inline">AB ∥ CD</span>. Transversals meet at an internal point <span class="math-inline">E</span> such that <span class="math-inline">∠BAE = 108°</span> and <span class="math-inline">∠ECD = 120°</span>. Find the reflex angle <span class="math-inline">∠AEC</span>.</p>
        <p><strong>Model Solution:</strong><br>
          1. Draw an auxiliary line <span class="math-inline">EF</span> through <span class="math-inline">E</span> parallel to <span class="math-inline">AB</span> and <span class="math-inline">CD</span>.<br>
          2. Since <span class="math-inline">AB ∥ EF</span>, consecutive interior angles sum to 180°:<br>
          <span class="math-inline">∠BAE + ∠AEF = 180° ⇒ 108° + ∠AEF = 180° ⇒ ∠AEF = 72°</span>.<br>
          3. Since <span class="math-inline">CD ∥ EF</span>, consecutive interior angles sum to 180°:<br>
          <span class="math-inline">∠ECD + ∠CEF = 180° ⇒ 120° + ∠CEF = 180° ⇒ ∠CEF = 60°</span>.<br>
          4. Interior angle <span class="math-inline">∠AEC = ∠AEF + ∠CEF = 72° + 60° = 132°</span>.<br>
          5. The reflex angle <span class="math-inline">∠AEC = 360° - 132° = 228°</span>.<br>
          <strong>Final Answer: Reflex ∠AEC = 228° (Interior ∠AEC = 132°).</strong>
        </p>
      </div>

      <!-- PYQ 3 -->
      <div class="callout callout-pyq">
        <p><strong>PYQ 3 (Olympiad / IMO Standard):</strong> Three lines <span class="math-inline">l, m, n</span> are parallel. A transversal cuts them at <span class="math-inline">P, Q, R</span>. Another transversal cuts them at <span class="math-inline">U, V, W</span>. If the distance <span class="math-inline">PQ = 4 \text{ cm}</span> and <span class="math-inline">QR = 6 \text{ cm}</span>, and <span class="math-inline">UV = 5 \text{ cm}</span>, find the length of segment <span class="math-inline">VW</span> and total segment <span class="math-inline">UW</span>.</p>
        <p><strong>Model Solution:</strong><br>
          By Thales' Intercept Theorem (Three parallel lines intercept proportional segments on any two transversals):<br>
          <span class="math-inline">PQ / QR = \frac{UV}{VW} ⇒ 4 / 6 = 5 / VW</span>.<br>
          Cross-multiplying: <span class="math-inline">4 × VW = 30 ⇒ VW = 30 ÷ 4 = 7.5 \text{ cm}</span>.<br>
          Total segment <span class="math-inline">UW = UV + VW = 5 + 7.5 = 12.5 \text{ cm}</span>.<br>
          <strong>Final Answer: VW = 7.5 cm and UW = 12.5 cm.</strong>
        </p>
      </div>

      <!-- PYQ 4 -->
      <div class="callout callout-pyq">
        <p><strong>PYQ 4 (Annual Examination Favorite):</strong> In a quadrilateral ABCD, side <span class="math-inline">AB ∥ CD</span>. If <span class="math-inline">∠A = 2x + 10°</span>, <span class="math-inline">∠D = 3x - 30°</span>, and <span class="math-inline">∠B = 70°</span>, find the values of <span class="math-inline">x</span>, angle <span class="math-inline">∠A</span>, angle <span class="math-inline">∠D</span>, and angle <span class="math-inline">∠C</span>.</p>
        <p><strong>Model Solution:</strong><br>
          1. Since <span class="math-inline">AB ∥ CD</span> and <span class="math-inline">AD</span> is a transversal, consecutive interior angles are supplementary:<br>
          <span class="math-inline">∠A + ∠D = 180° ⇒ (2x + 10) + (3x - 30) = 180°</span>.<br>
          <span class="math-inline">5x - 20 = 180° ⇒ 5x = 200° ⇒ x = 40</span>.<br>
          2. <span class="math-inline">∠A = 2(40) + 10 = 90°</span>.<br>
          3. <span class="math-inline">∠D = 3(40) - 30 = 90°</span>.<br>
          4. Since <span class="math-inline">AB ∥ CD</span> and <span class="math-inline">BC</span> is a transversal, <span class="math-inline">∠B + ∠C = 180°</span>:<br>
          <span class="math-inline">70° + ∠C = 180° ⇒ ∠C = 180° - 70° = 110°</span>.<br>
          <strong>Final Answer: x = 40; ∠A = 90°, ∠D = 90°, ∠C = 110°.</strong>
        </p>
      </div>

      <!-- PYQ 5 -->
      <div class="callout callout-pyq">
        <p><strong>PYQ 5 (NCERT Exemplar / High-Order Thinking):</strong> What is the angle between the hour hand and the minute hand of a clock at 3:30? Are the two hands parallel, perpendicular, or inclined? Show step-by-step mathematical calculation.</p>
        <p><strong>Model Solution:</strong><br>
          1. At 3:30, the minute hand points directly at number 6, which corresponds to <span class="math-inline">6 × 30° = 180°</span> from the 12 o'clock mark.<br>
          2. The hour hand moves <span class="math-inline">0.5°</span> per minute. In 30 minutes, it moves: <span class="math-inline">30 × 0.5° = 15°</span> past the 3 o'clock mark.<br>
          Since 3 o'clock is <span class="math-inline">3 × 30° = 90°</span>, the position of the hour hand is: <span class="math-inline">90° + 15° = 105°</span>.<br>
          3. The angle between the two hands is: <span class="math-inline">180° - 105° = 75°</span>.<br>
          4. Since <span class="math-inline">75° ≠ 0°</span> (not parallel) and <span class="math-inline">75° ≠ 90°</span> (not perpendicular), the hands are <strong>inclined at an acute angle of 75°</strong>.<br>
          <strong>Final Answer: The angle is 75° (acute inclination).</strong>
        </p>
      </div>
    </section>
"""
