# -*- coding: utf-8 -*-
"""
Module: ch3_section5.py
Contains Section 5: Complete Exam Question Bank (27 Questions Total).
- 5 Interactive MCQs with Quiz Engine (instant feedback & trap analysis)
- 5 Assertion & Reasoning Questions (CBSE Pattern)
- 6 Short Answer Questions (2M / 3M)
- 4 Long Answer Questions (5M with explicit marking schemes)
- 2 Competency-Based Case Studies
- 5 Previous Years Questions (PYQs) & Most Probable Exam Questions
"""

def get_section_5():
    return """
    <!-- ======================================================== -->
    <!-- SECTION 5: COMPLETE EXAM QUESTION BANK (27 CBE QUESTIONS) -->
    <!-- ======================================================== -->
    <section id="section-5">
      <div class="section-header">
        <span class="section-badge"><i class="fa-solid fa-clipboard-question"></i> Board Exam Architecture</span>
        <h2 class="section-title">Section 5: Complete Exam Question Bank (27 CBE Models)</h2>
        <p class="section-desc">
          Rigorous, multi-tier examination bank designed strictly on CBSE Competency-Based Education (CBE) and NEP 2020 guidelines — featuring interactive MCQs, Assertion-Reasoning, Short/Long models with marking schemes, and case studies.
        </p>
      </div>

      <!-- ======================================================== -->
      <!-- PART 1: 5 CONCEPTUAL MCQS (INTERACTIVE ENGINE)           -->
      <!-- ======================================================== -->
      <h3><i class="fa-solid fa-circle-check" style="color: var(--primary);"></i> 1. Conceptual Multiple Choice Questions (Interactive Quiz)</h3>
      <p>Test your conceptual reflexes! Click an option to evaluate instantly with detailed trap explanations.</p>

      <!-- LIVE SCORE COUNTER -->
      <div class="score-badge-container">
        <div class="score-text"><i class="fa-solid fa-award" style="color: var(--accent);"></i> Real-Time Quiz Score:</div>
        <div class="score-number" id="quizScoreDisplay">0 / 5</div>
      </div>

      <!-- MCQ 1 -->
      <div class="quiz-card" id="mcq-card-1">
        <div class="quiz-q-num">Question 1 (Recall & Analysis)</div>
        <div class="quiz-question">
          Which of the following is the PRIMARY reason why ancient Egyptians had to invent new hieroglyphic symbols for higher numbers like 100, 1000, and 10,000, while the modern Hindu system needs NO new symbols?
        </div>
        <div class="quiz-options">
          <button class="option-btn" onclick="handleMcqChoice(1, 'A', false, 'mcq-card-1')">
            A) The Egyptians used base 12 while the Hindu system uses base 10.
          </button>
          <button class="option-btn" onclick="handleMcqChoice(1, 'B', true, 'mcq-card-1')">
            B) The Egyptian system was additive, whereas the Hindu system uses positional place value with zero.
          </button>
          <button class="option-btn" onclick="handleMcqChoice(1, 'C', false, 'mcq-card-1')">
            C) Egyptian scribes did not know how to multiply numbers.
          </button>
          <button class="option-btn" onclick="handleMcqChoice(1, 'D', false, 'mcq-card-1')">
            D) Egyptian papyrus was too fragile to draw repetitive tally marks.
          </button>
        </div>
        <div class="quiz-feedback" id="feedback-1">
          <strong>Correct Answer: B!</strong><br>
          <em>Conceptual Explanation:</em> In an additive system, each power of 10 must have its own distinct pictorial symbol (stroke, heel bone, coil, lotus). In contrast, the Hindu system uses <strong>positional place value</strong>: the location of the digit automatically denotes the power of 10, and <strong>zero (0)</strong> holds empty columns, eliminating the need to ever invent new symbols!
          <br><span style="color: var(--danger-dark); font-weight: 600;">Student Trap:</span> Option A is false because both Egyptian and Hindu systems are decimal (base 10). The critical difference is positional vs additive!
        </div>
      </div>

      <!-- MCQ 2 -->
      <div class="quiz-card" id="mcq-card-2">
        <div class="quiz-q-num">Question 2 (Mathematical Properties of Base-n)</div>
        <div class="quiz-question">
          In any base-n number system, what is the product of any two landmark numbers, say nᵃ and nᵇ?
        </div>
        <div class="quiz-options">
          <button class="option-btn" onclick="handleMcqChoice(2, 'A', false, 'mcq-card-2')">
            A) It is always a composite number that cannot be represented as a landmark.
          </button>
          <button class="option-btn" onclick="handleMcqChoice(2, 'B', false, 'mcq-card-2')">
            B) It depends on whether the base n is an even or odd integer.
          </button>
          <button class="option-btn" onclick="handleMcqChoice(2, 'C', true, 'mcq-card-2')">
            C) It is always guaranteed to be another landmark number in that system: nᵃ⁺ᵇ.
          </button>
          <button class="option-btn" onclick="handleMcqChoice(2, 'D', false, 'mcq-card-2')">
            D) It is always equal to n × (a + b).
          </button>
        </div>
        <div class="quiz-feedback" id="feedback-2">
          <strong>Correct Answer: C!</strong><br>
          <em>Conceptual Explanation:</em> By the fundamental law of exponents, nᵃ × nᵇ = nᵃ⁺ᵇ. Since the landmark numbers of a base-n system are precisely the powers of n starting from n⁰, any power added to another power yields an integer power of n, which is directly another landmark! This closure property makes base-n multiplication extraordinarily streamlined compared to Roman numerals.
          <br><span style="color: var(--danger-dark); font-weight: 600;">Student Trap:</span> Don't confuse the exponent law nᵃ × nᵇ = nᵃ⁺ᵇ with multiplying the base by the sum of exponents (Option D).
        </div>
      </div>

      <!-- MCQ 3 -->
      <div class="quiz-card" id="mcq-card-3">
        <div class="quiz-q-num">Question 3 (Archaeology & Historical Numeration)</div>
        <div class="quiz-question">
          What is the unique mathematical peculiarity of the Mayan number system's third positional tier?
        </div>
        <div class="quiz-options">
          <button class="option-btn" onclick="handleMcqChoice(3, 'A', false, 'mcq-card-3')">
            A) It has a multiplier of 20² = 400.
          </button>
          <button class="option-btn" onclick="handleMcqChoice(3, 'B', true, 'mcq-card-3')">
            B) It has a multiplier of 18 × 20 = 360, tuned to match their solar calendar.
          </button>
          <button class="option-btn" onclick="handleMcqChoice(3, 'C', false, 'mcq-card-3')">
            C) It can only hold odd numbers.
          </button>
          <button class="option-btn" onclick="handleMcqChoice(3, 'D', false, 'mcq-card-3')">
            D) It uses horizontal dots instead of vertical dots.
          </button>
        </div>
        <div class="quiz-feedback" id="feedback-3">
          <strong>Correct Answer: B!</strong><br>
          <em>Conceptual Explanation:</em> In a strict base-20 vigesimal system, the third tier would be 20² = 400. However, the Mayan astronomers deliberately altered this position to 18 × 20 = <strong>360</strong> so that their numerical tiers directly synchronized with the 360-day solar Haab calendar!
          <br><span style="color: var(--danger-dark); font-weight: 600;">Student Trap:</span> Many students reflexively compute 20² = 400 and forget the Maya's calendar modification!
        </div>
      </div>

      <!-- MCQ 4 -->
      <div class="quiz-card" id="mcq-card-4">
        <div class="quiz-q-num">Question 4 (Base Conversion & Binary Logic)</div>
        <div class="quiz-question">
          How is the decimal number 25 represented in Base-8 (Octal) and Base-5 respectively?
        </div>
        <div class="quiz-options">
          <button class="option-btn" onclick="handleMcqChoice(4, 'A', false, 'mcq-card-4')">
            A) Base-8: 25₈ &nbsp;|&nbsp; Base-5: 50₅
          </button>
          <button class="option-btn" onclick="handleMcqChoice(4, 'B', true, 'mcq-card-4')">
            B) Base-8: 31₈ &nbsp;|&nbsp; Base-5: 100₅
          </button>
          <button class="option-btn" onclick="handleMcqChoice(4, 'C', false, 'mcq-card-4')">
            C) Base-8: 31₈ &nbsp;|&nbsp; Base-5: 55₅
          </button>
          <button class="option-btn" onclick="handleMcqChoice(4, 'D', false, 'mcq-card-4')">
            D) Base-8: 17₈ &nbsp;|&nbsp; Base-5: 125₅
          </button>
        </div>
        <div class="quiz-feedback" id="feedback-4">
          <strong>Correct Answer: B!</strong><br>
          <em>Conceptual Explanation:</em> <br>
          • In Base-8: 25 = (3 × 8¹) + (1 × 8⁰) = <strong>31₈</strong>.<br>
          • In Base-5: 25 = (1 × 5²) + (0 × 5¹) + (0 × 5⁰) = <strong>100₅</strong>.<br>
          <span style="color: var(--danger-dark); font-weight: 600;">Student Trap:</span> The symbol '5' cannot exist as a digit in Base-5 (digits can only be 0, 1, 2, 3, 4). Therefore, options A and C are instantly disqualified!
        </div>
      </div>

      <!-- MCQ 5 -->
      <div class="quiz-card" id="mcq-card-5">
        <div class="quiz-q-num">Question 5 (Chinese Rod Numerals)</div>
        <div class="quiz-question">
          Why did Chinese mathematicians strictly alternate between Zong (vertical) and Heng (horizontal) forms in rod numerals?
        </div>
        <div class="quiz-options">
          <button class="option-btn" onclick="handleMcqChoice(5, 'A', false, 'mcq-card-5')">
            A) To differentiate positive numbers from negative debts.
          </button>
          <button class="option-btn" onclick="handleMcqChoice(5, 'B', false, 'mcq-card-5')">
            B) Because bamboo rods break if placed in the same direction.
          </button>
          <button class="option-btn" onclick="handleMcqChoice(5, 'C', true, 'mcq-card-5')">
            C) To distinguish adjacent columns and prevent parallel rods from merging into a single digit.
          </button>
          <button class="option-btn" onclick="handleMcqChoice(5, 'D', false, 'mcq-card-5')">
            D) To indicate odd and even calendar years.
          </button>
        </div>
        <div class="quiz-feedback" id="feedback-5">
          <strong>Correct Answer: C!</strong><br>
          <em>Conceptual Explanation:</em> Without alternating directions, four vertical rods followed by one vertical rod (representing 41) would appear as five consecutive vertical rods: |||||, which represents the number 5! Alternating vertical rods (units, hundreds) with horizontal rods (tens, thousands) created instant visual boundaries between adjacent place-value columns.
        </div>
      </div>

      <!-- ======================================================== -->
      <!-- PART 2: 5 ASSERTION & REASONING QUESTIONS (CBSE)         -->
      <!-- ======================================================== -->
      <h3><i class="fa-solid fa-arrows-split-up-and-left" style="color: var(--secondary);"></i> 2. Assertion & Reasoning Questions (CBSE Pattern)</h3>
      <p style="font-size: 0.95rem; margin-bottom: 1.5rem;">
        <strong>Instructions for Questions 6 to 10:</strong> Choose the correct option from:<br>
        (A) Both Assertion (A) and Reason (R) are true and Reason (R) is the correct explanation of Assertion (A).<br>
        (B) Both Assertion (A) and Reason (R) are true but Reason (R) is NOT the correct explanation of Assertion (A).<br>
        (C) Assertion (A) is true but Reason (R) is false.<br>
        (D) Assertion (A) is false but Reason (R) is true.
      </p>

      <!-- AR 1 -->
      <details class="ans-box">
        <summary>
          <span><i class="fa-solid fa-scale-balanced" style="color: var(--secondary); margin-right: 0.5rem;"></i> Question 6 — Assertion & Reasoning: The Subitizing Grouping Threshold</span>
        </summary>
        <div class="ans-content">
          <p><strong>Assertion (A):</strong> Most human beings across early civilizations grouped counts into sets of 5, 10, or 20 rather than counting continuously by single tallies.<br>
          <strong>Reason (R):</strong> The human brain possesses an innate perceptual mechanism called subitizing, which allows immediate quantity recognition only up to 4 items without sequential counting.</p>
          <div class="step-container">
            <div class="step-box step-1">
              <span class="step-badge">Step 1: Evaluation of Assertion (A)</span>
              <p>Assertion (A) is <strong>TRUE</strong>. Historical archaeology proves that early tally marks on cave walls and bones were grouped by notches of 5 (matching hands), 10 (fingers), or 20 (fingers and toes).</p>
            </div>
            <div class="step-box step-2">
              <span class="step-badge">Step 2: Evaluation of Reason (R)</span>
              <p>Reason (R) is <strong>TRUE</strong>. Cognitive science confirms that subitizing allows immediate apprehension of quantities 1 to 4; beyond 4, humans must count sequentially or group.</p>
            </div>
            <div class="step-box step-3">
              <span class="step-badge">Step 3: Causal Linkage</span>
              <p>Because humans cannot instantly perceive groups of 5 or more at a single glance, they were forced to invent new landmark symbols or group marks at or above 5. Thus, Reason (R) is the direct cognitive cause of Assertion (A).</p>
            </div>
            <div class="step-box step-5">
              <span class="step-badge">Step 5: Final Conclusion</span>
              <p><strong>Correct Option: (A)</strong> — Both (A) and (R) are true, and (R) correctly explains (A).</p>
            </div>
          </div>
        </div>
      </details>

      <!-- AR 2 -->
      <details class="ans-box">
        <summary>
          <span><i class="fa-solid fa-scale-balanced" style="color: var(--secondary); margin-right: 0.5rem;"></i> Question 7 — Assertion & Reasoning: Babylonian Ambiguity Without Zero</span>
        </summary>
        <div class="ans-content">
          <p><strong>Assertion (A):</strong> In the early Mesopotamian number system, the numeral containing one wedge in the sixties column and two wedges in the units column could be interpreted as 62, 3602, or 216,002.<br>
          <strong>Reason (R):</strong> The early Mesopotamians lacked a dedicated symbol for zero and relied merely on leaving blank spaces between place-value columns.</p>
          <div class="step-container">
            <div class="step-box step-1">
              <span class="step-badge">Step 1: Evaluation of Assertion (A)</span>
              <p>Assertion (A) is <strong>TRUE</strong>. A scribe writing ▼ followed by ▼▼ with unclear spacing could mean 1(60) + 2(1) = 62, or 1(3600) + 0(60) + 2(1) = 3602, or even higher powers.</p>
            </div>
            <div class="step-box step-2">
              <span class="step-badge">Step 2: Evaluation of Reason (R)</span>
              <p>Reason (R) is <strong>TRUE</strong>. In early cuneiform tablets, blank spaces indicated empty powers of 60. Without uniform spacing or a placeholder, reader ambiguity was pervasive.</p>
            </div>
            <div class="step-box step-3">
              <span class="step-badge">Step 3: Causal Linkage</span>
              <p>The ambiguity described in (A) exists precisely because of the absence of a visible zero placeholder stated in (R). Hence, (R) is the exact explanation.</p>
            </div>
            <div class="step-box step-5">
              <span class="step-badge">Step 5: Final Conclusion</span>
              <p><strong>Correct Option: (A)</strong> — Both (A) and (R) are true, and (R) is the correct explanation of (A).</p>
            </div>
          </div>
        </div>
      </details>

      <!-- AR 3 -->
      <details class="ans-box">
        <summary>
          <span><i class="fa-solid fa-scale-balanced" style="color: var(--secondary); margin-right: 0.5rem;"></i> Question 8 — Assertion & Reasoning: Repetition in Base-n Systems</span>
        </summary>
        <div class="ans-content">
          <p><strong>Assertion (A):</strong> In an additive base-5 number system, the landmark symbol representing 1 can appear up to 5 times in a standard numeral.<br>
          <strong>Reason (R):</strong> In any base-n system, exactly n units of any landmark number combine to form 1 unit of the next higher landmark number.</p>
          <div class="step-container">
            <div class="step-box step-1">
              <span class="step-badge">Step 1: Evaluation of Assertion (A)</span>
              <p>Assertion (A) is <strong>FALSE</strong>. In a base-5 system, once 5 units accumulate, they must be regrouped into 1 unit of the next landmark (5). Therefore, the unit symbol can appear at most <strong>4 times</strong> (never 5 times in canonical form)!</p>
            </div>
            <div class="step-box step-2">
              <span class="step-badge">Step 2: Evaluation of Reason (R)</span>
              <p>Reason (R) is <strong>TRUE</strong>. By definition of base-n, n units of nᵏ equal 1 unit of nᵏ⁺¹.</p>
            </div>
            <div class="step-box step-5">
              <span class="step-badge">Step 5: Final Conclusion</span>
              <p><strong>Correct Option: (D)</strong> — Assertion (A) is false, but Reason (R) is true.</p>
            </div>
          </div>
        </div>
      </details>

      <!-- AR 4 -->
      <details class="ans-box">
        <summary>
          <span><i class="fa-solid fa-scale-balanced" style="color: var(--secondary); margin-right: 0.5rem;"></i> Question 9 — Assertion & Reasoning: Brahmagupta's Ring Formulation</span>
        </summary>
        <div class="ans-content">
          <p><strong>Assertion (A):</strong> Brahmagupta's treatment of zero in the <em>Brāhmasphuṭasiddhānta</em> (628 CE) transformed zero from a mere placeholder into a fully functioning algebraic number.<br>
          <strong>Reason (R):</strong> Brahmagupta established arithmetic operational laws for positive quantities (fortunes), negative quantities (debts), and zero (śūnya) that are closed under addition, subtraction, and multiplication.</p>
          <div class="step-container">
            <div class="step-box step-1">
              <span class="step-badge">Step 1: Evaluation of Assertion (A)</span>
              <p>Assertion (A) is <strong>TRUE</strong>. Prior to Brahmagupta, cultures like the Babylonians and Mayans used zero only as a blank placeholder. Brahmagupta was the first to treat zero as an independent number subject to arithmetic operations.</p>
            </div>
            <div class="step-box step-2">
              <span class="step-badge">Step 2: Evaluation of Reason (R)</span>
              <p>Reason (R) is <strong>TRUE</strong>. He defined formal rules: <code>a + 0 = a</code>, <code>a - 0 = a</code>, <code>0 - a = -a</code>, <code>a × 0 = 0</code>, establishing the algebraic ring of integers (ℤ).</p>
            </div>
            <div class="step-box step-3">
              <span class="step-badge">Step 3: Causal Linkage</span>
              <p>Defining these operational rules is precisely what conferred algebraic number status upon zero. Thus (R) directly explains (A).</p>
            </div>
            <div class="step-box step-5">
              <span class="step-badge">Step 5: Final Conclusion</span>
              <p><strong>Correct Option: (A)</strong> — Both (A) and (R) are true, and (R) is the correct explanation of (A).</p>
            </div>
          </div>
        </div>
      </details>

      <!-- AR 5 -->
      <details class="ans-box">
        <summary>
          <span><i class="fa-solid fa-scale-balanced" style="color: var(--secondary); margin-right: 0.5rem;"></i> Question 10 — Assertion & Reasoning: Roman Multiplication Complexity</span>
        </summary>
        <div class="ans-content">
          <p><strong>Assertion (A):</strong> Roman numerals did not allow easy paper-and-pencil multiplication algorithms.<br>
          <strong>Reason (R):</strong> Roman numerals are constructed using Latin letters rather than Sanskrit characters.</p>
          <div class="step-container">
            <div class="step-box step-1">
              <span class="step-badge">Step 1: Evaluation of Assertion (A)</span>
              <p>Assertion (A) is <strong>TRUE</strong>. Multiplying in Roman numerals (e.g. <code>LXXVIII × XLIX</code>) requires extensive cross-expansion and is extremely cumbersome on paper.</p>
            </div>
            <div class="step-box step-2">
              <span class="step-badge">Step 2: Evaluation of Reason (R)</span>
              <p>Reason (R) is <strong>FALSE</strong> (as an explanation). The visual script (Latin vs Sanskrit) is completely irrelevant! Roman multiplication is difficult because the system lacks <strong>positional place value</strong> and has <strong>no zero</strong>, not because of Latin letters!</p>
            </div>
            <div class="step-box step-5">
              <span class="step-badge">Step 5: Final Conclusion</span>
              <p><strong>Correct Option: (C)</strong> — Assertion (A) is true, but Reason (R) is false.</p>
            </div>
          </div>
        </div>
      </details>

      <!-- ======================================================== -->
      <!-- PART 3: 6 SHORT ANSWER QUESTIONS (2M / 3M)               -->
      <!-- ======================================================== -->
      <h3><i class="fa-solid fa-file-lines" style="color: var(--purple);"></i> 3. Short Answer Questions (2-Mark & 3-Mark Models)</h3>

      <!-- SA 1 -->
      <details class="ans-box">
        <summary>
          <span><i class="fa-solid fa-pen-fancy" style="color: var(--purple); margin-right: 0.5rem;"></i> Question 11 (2 Marks): Mathematical Definition of a Base-n System</span>
        </summary>
        <div class="ans-content">
          <p><strong>Question:</strong> State the two fundamental conditions that define a base-n number system. What are the landmark numbers of a base-6 system?</p>
          <div class="step-container">
            <div class="step-box step-1">
              <span class="step-badge">Step 1: Marking Scheme Analysis (2 Marks Total)</span>
              <p>• 1 Mark for stating the two defining conditions of a base-n system.<br>• 1 Mark for calculating the first four landmark numbers of Base-6.</p>
            </div>
            <div class="step-box step-2">
              <span class="step-badge">Step 2: Two Defining Conditions</span>
              <ol style="margin-left: 1.5rem; line-height: 1.8;">
                <li>The first landmark number must be <strong>1 (i.e., n⁰ = 1)</strong>.</li>
                <li>Every subsequent landmark number is obtained by multiplying the previous landmark number by a fixed integer constant <strong>n</strong>.</li>
              </ol>
            </div>
            <div class="step-box step-3">
              <span class="step-badge">Step 3: Landmark Numbers of Base-6</span>
              <p>
                <code>6⁰ = 1</code> <br>
                <code>6¹ = 6</code> <br>
                <code>6² = 36</code> <br>
                <code>6³ = 216</code> <br>
                <code>6⁴ = 1,296</code>
              </p>
            </div>
            <div class="step-box step-5">
              <span class="step-badge">Step 5: Final Topper-Level Answer</span>
              <p>The defining conditions are: (1) n⁰ = 1 is the 1st landmark, and (2) each next landmark is n times the prior one. For Base-6, the landmark numbers are <strong>1, 6, 36, 216, 1296...</strong></p>
            </div>
          </div>
        </div>
      </details>

      <!-- SA 2 -->
      <details class="ans-box">
        <summary>
          <span><i class="fa-solid fa-pen-fancy" style="color: var(--purple); margin-right: 0.5rem;"></i> Question 12 (2 Marks): Subtractive Principle in Roman Numerals</span>
        </summary>
        <div class="ans-content">
          <p><strong>Question:</strong> Explain the subtractive rule in Roman numerals. Why is the number 49 written as <code>XLIX</code> and NOT as <code>IL</code>?</p>
          <div class="step-container">
            <div class="step-box step-1">
              <span class="step-badge">Step 1: Marking Scheme Breakdown (2 Marks)</span>
              <p>• 1 Mark for stating the subtractive principle and eligible subtractive pairs.<br>• 1 Mark for explaining why IL violates the decimal place-order convention.</p>
            </div>
            <div class="step-box step-2">
              <span class="step-badge">Step 2: The Subtractive Rule & Strict Pairing Constraints</span>
              <p>When a smaller landmark symbol is placed immediately before a larger landmark symbol, its value is subtracted. However, Roman convention strictly dictates that a symbol can only be subtracted from the next two higher landmarks of its own decimal scale: <br>
              • <code>I</code> can only be subtracted from <code>V</code> and <code>X</code> (producing IV = 4, IX = 9). <br>
              • <code>X</code> can only be subtracted from <code>L</code> and <code>C</code> (producing XL = 40, XC = 90). <br>
              • <code>C</code> can only be subtracted from <code>D</code> and <code>M</code> (producing CD = 400, CM = 900).</p>
            </div>
            <div class="step-box step-3">
              <span class="step-badge">Step 3: Explaining 49</span>
              <p>The number 49 is composed of 40 (forty) + 9 (nine). Forty is written as <code>XL</code> (50 - 10). Nine is written as <code>IX</code> (10 - 1). Combining them yields <strong>XLIX</strong>. Writing <code>IL</code> violates the decimal pairing rule because <code>I</code> (1) cannot be directly subtracted from <code>L</code> (50)!</p>
            </div>
            <div class="step-box step-5">
              <span class="step-badge">Step 5: Final Model Answer</span>
              <p><code>I</code> can only be subtracted from <code>V</code> and <code>X</code>. Therefore, 49 must be decomposed into 40 (XL) + 9 (IX) = <strong>XLIX</strong>. <code>IL</code> is an invalid numeral.</p>
            </div>
          </div>
        </div>
      </details>

      <!-- SA 3 -->
      <details class="ans-box">
        <summary>
          <span><i class="fa-solid fa-pen-fancy" style="color: var(--purple); margin-right: 0.5rem;"></i> Question 13 (3 Marks): Archaeological Tally Sticks Comparison</span>
        </summary>
        <div class="ans-content">
          <p><strong>Question:</strong> Name the two oldest mathematical bone artifacts discovered by archaeologists. Compare their geographical origins, approximate ages, and mathematical significance.</p>
          <div class="step-container">
            <div class="step-box step-1">
              <span class="step-badge">Step 1: Marking Scheme Breakdown (3 Marks)</span>
              <p>• 1.5 Marks for Lebombo Bone (location, age, lunar significance).<br>• 1.5 Marks for Ishango Bone (location, age, prime/doubling columns).</p>
            </div>
            <div class="step-box step-2">
              <span class="step-badge">Step 2: Structured Comparative Response</span>
              <div class="table-wrapper">
                <table>
                  <thead><tr><th>Feature</th><th>The Lebombo Bone</th><th>The Ishango Bone</th></tr></thead>
                  <tbody>
                    <tr><td><strong>Discovery Location</strong></td><td>Border Cave, Lebombo Mountains, South Africa</td><td>Ishango region near Lake Edward, DR Congo</td></tr>
                    <tr><td><strong>Estimated Age</strong></td><td>Approx. <strong>44,000 years old</strong> (Oldest mathematical artifact)</td><td>Approx. <strong>20,000 to 35,000 years old</strong></td></tr>
                    <tr><td><strong>Physical Specimen</strong></td><td>Baboon fibula with <strong>29 distinct carved notches</strong></td><td>Dark baboon fibula with carved columns & quartz tool</td></tr>
                    <tr><td><strong>Mathematical Role</strong></td><td>Likely a <strong>lunar calendar</strong> tracking the 29.5-day cycle</td><td>Notches grouped into primes (11, 13, 17, 19) and doubling patterns</td></tr>
                  </tbody>
                </table>
              </div>
            </div>
            <div class="step-box step-5">
              <span class="step-badge">Step 5: Final Conclusion</span>
              <p>The Lebombo and Ishango bones demonstrate that systematic tallying, calendar arithmetic, and number grouping originated in Africa tens of thousands of years before the rise of urban civilizations.</p>
            </div>
          </div>
        </div>
      </details>

      <!-- SA 4 -->
      <details class="ans-box">
        <summary>
          <span><i class="fa-solid fa-pen-fancy" style="color: var(--purple); margin-right: 0.5rem;"></i> Question 14 (3 Marks): Distributive Law in Egyptian Multiplication</span>
        </summary>
        <div class="ans-content">
          <p><strong>Question:</strong> How did Egyptian scribes use the distributive property to multiply numbers? Demonstrate how the product <code>21 × 10</code> was computed in hieroglyphic arithmetic.</p>
          <div class="step-container">
            <div class="step-box step-1">
              <span class="step-badge">Step 1: Marking Scheme Breakdown (3 Marks)</span>
              <p>• 1 Mark for stating the algebraic distributive identity: (a + b) × n = an + bn.<br>• 1 Mark for decomposing 21 into Egyptian landmark components.<br>• 1 Mark for multiplying each component by 10 and regrouping.</p>
            </div>
            <div class="step-box step-2">
              <span class="step-badge">Step 2: Mathematical Principle</span>
              <p>The distributive property states that multiplying a sum by a number is equivalent to multiplying each addend individually: <code class="math-code">(a + b) × n = (a × n) + (b × n)</code>.</p>
            </div>
            <div class="step-box step-3">
              <span class="step-badge">Step 3: Step-by-Step Egyptian Execution</span>
              <ul style="margin-left: 1.5rem; line-height: 1.8;">
                <li>The number 21 in Egyptian numerals consists of <strong>2 Heel Bones (∩ ∩)</strong> and <strong>1 Stroke (|)</strong>.</li>
                <li>Multiplying by 10 (Heel Bone): <br>
                <code>21 × 10 = (20 + 1) × 10 = (20 × 10) + (1 × 10)</code>.</li>
                <li>Applying landmark power shifts: <br>
                Each Heel Bone (10) multiplied by 10 becomes <strong>1 Coil of Rope (100)</strong>. Thus, 2 Heel Bones become <strong>2 Coils of Rope (𓏲 𓏲)</strong> = 200. <br>
                The 1 Stroke (1) multiplied by 10 becomes <strong>1 Heel Bone (∩)</strong> = 10.</li>
                <li>Combining the shifted glyphs: <strong>2 Coils of Rope + 1 Heel Bone = 210</strong>.</li>
              </ul>
            </div>
            <div class="step-box step-5">
              <span class="step-badge">Step 5: Final Answer</span>
              <p>21 × 10 is evaluated by shifting each component to the next landmark: 2 Heel Bones become 2 Coils (200), and 1 Stroke becomes 1 Heel Bone (10), yielding <strong>210</strong>.</p>
            </div>
          </div>
        </div>
      </details>

      <!-- SA 5 -->
      <details class="ans-box">
        <summary>
          <span><i class="fa-solid fa-pen-fancy" style="color: var(--purple); margin-right: 0.5rem;"></i> Question 15 (3 Marks): Decimal Number 43 in Four Different Bases</span>
        </summary>
        <div class="ans-content">
          <p><strong>Question:</strong> Convert the decimal number <strong>43</strong> into: (i) Base-2 (Binary), (ii) Base-5, and (iii) Base-8 (Octal). Show all quotient and remainder calculations.</p>
          <div class="step-container">
            <div class="step-box step-1">
              <span class="step-badge">Step 1: Marking Scheme Breakdown (3 Marks)</span>
              <p>• 1 Mark for Base-2 conversion.<br>• 1 Mark for Base-5 conversion.<br>• 1 Mark for Base-8 conversion.</p>
            </div>
            <div class="step-box step-2">
              <span class="step-badge">Step 2: Base-2 (Binary) Conversion</span>
              <p>Successive division of 43 by 2: <br>
              43 ÷ 2 = 21, rem <strong>1</strong> <br>
              21 ÷ 2 = 10, rem <strong>1</strong> <br>
              10 ÷ 2 = 5, rem <strong>0</strong> <br>
              5 ÷ 2 = 2, rem <strong>1</strong> <br>
              2 ÷ 2 = 1, rem <strong>0</strong> <br>
              1 ÷ 2 = 0, rem <strong>1</strong> <br>
              Reading remainders bottom to top: <strong>43₁₀ = 101011₂</strong>. <br>
              Check: 32 + 8 + 2 + 1 = 43. Correct!</p>
            </div>
            <div class="step-box step-3">
              <span class="step-badge">Step 3: Base-5 Conversion</span>
              <p>Successive division of 43 by 5: <br>
              43 ÷ 5 = 8, rem <strong>3</strong> <br>
              8 ÷ 5 = 1, rem <strong>3</strong> <br>
              1 ÷ 5 = 0, rem <strong>1</strong> <br>
              Reading remainders bottom to top: <strong>43₁₀ = 133₅</strong>. <br>
              Check: (1 × 25) + (3 × 5) + (3 × 1) = 25 + 15 + 3 = 43. Correct!</p>
            </div>
            <div class="step-box step-4">
              <span class="step-badge">Step 4: Base-8 (Octal) Conversion</span>
              <p>Successive division of 43 by 8: <br>
              43 ÷ 8 = 5, rem <strong>3</strong> <br>
              5 ÷ 8 = 0, rem <strong>5</strong> <br>
              Reading remainders bottom to top: <strong>43₁₀ = 53₈</strong>. <br>
              Check: (5 × 8) + (3 × 1) = 40 + 3 = 43. Correct!</p>
            </div>
            <div class="step-box step-5">
              <span class="step-badge">Step 5: Final Model Answers</span>
              <p>
                <strong>(i) Base-2: 101011₂</strong> <br>
                <strong>(ii) Base-5: 133₅</strong> <br>
                <strong>(iii) Base-8: 53₈</strong>
              </p>
            </div>
          </div>
        </div>
      </details>

      <!-- SA 6 -->
      <details class="ans-box">
        <summary>
          <span><i class="fa-solid fa-pen-fancy" style="color: var(--purple); margin-right: 0.5rem;"></i> Question 16 (2 Marks): Dual Mathematical Identity of Zero</span>
        </summary>
        <div class="ans-content">
          <p><strong>Question:</strong> Distinguish between the two distinct roles of zero in the Hindu number system: (1) zero as a positional placeholder, and (2) zero as an algebraic number.</p>
          <div class="step-container">
            <div class="step-box step-1">
              <span class="step-badge">Step 1: Marking Scheme Breakdown (2 Marks)</span>
              <p>• 1 Mark for defining the placeholder function with an illustrative example.<br>• 1 Mark for defining the algebraic number function with operational laws.</p>
            </div>
            <div class="step-box step-2">
              <span class="step-badge">Step 2: Role 1 — Zero as a Positional Placeholder</span>
              <p>Zero acts as a positional spacer to indicate that a specific power of 10 has no count. Without zero, <code>35</code>, <code>305</code>, and <code>3500</code> would all be written as <code>35</code>, causing complete ambiguity. The placeholder preserves column values.</p>
            </div>
            <div class="step-box step-3">
              <span class="step-badge">Step 3: Role 2 — Zero as an Autonomous Algebraic Number</span>
              <p>Zero is not merely an empty space; it is a valid integer that participates in arithmetic: <br>
              • Additive Identity: <code>a + 0 = a</code> <br>
              • Additive Inverse: <code>a + (-a) = 0</code> <br>
              • Multiplicative Annihilator: <code>a × 0 = 0</code></p>
            </div>
            <div class="step-box step-5">
              <span class="step-badge">Step 5: Final Model Answer</span>
              <p>As a <strong>placeholder</strong>, zero maintains column positions (305 vs 35). As an <strong>algebraic number</strong>, zero possesses defined operational arithmetic laws codified by Brahmagupta.</p>
            </div>
          </div>
        </div>
      </details>

      <!-- ======================================================== -->
      <!-- PART 4: 4 LONG ANSWER QUESTIONS (5M WITH SCHEMES)        -->
      <!-- ======================================================== -->
      <h3><i class="fa-solid fa-medal" style="color: var(--accent-dark);"></i> 4. Long Answer Questions (5-Mark Models with Step-by-Step Marking Schemes)</h3>

      <!-- LA 1 -->
      <details class="ans-box">
        <summary>
          <span><i class="fa-solid fa-star" style="color: var(--accent); margin-right: 0.5rem;"></i> Question 17 (5 Marks): The 5 Evolutionary Stages of Number Representation</span>
        </summary>
        <div class="ans-content">
          <p><strong>Question:</strong> Trace the complete 5-stage intellectual evolution of number representation from Paleolithic tallies to the modern Hindu decimal system. Provide a historical example, mathematical mechanism, and core breakthrough for each stage.</p>
          <div class="step-container">
            <div class="step-box step-1">
              <span class="step-badge">Step 1: Marking Scheme Breakdown (5 Marks Total — 1 Mark Per Stage)</span>
              <p>• Stage 1 (1M): One-to-one tallies & counting in single group sizes.<br>
              • Stage 2 (1M): Grouping by arbitrary landmark numbers.<br>
              • Stage 3 (1M): The Base-n revolution (powers of n as landmarks).<br>
              • Stage 4 (1M): Positional place-value representation.<br>
              • Stage 5 (1M): Indian invention of True Zero and universal arithmetic algorithms.</p>
            </div>
            <div class="step-box step-2">
              <span class="step-badge">Step 2: Exhaustive Stage-by-Stage Narrative</span>
              <div class="table-wrapper">
                <table>
                  <thead><tr><th>Stage</th><th>Historical Culture / Artifact</th><th>Mathematical Mechanism</th><th>Conceptual Breakthrough</th></tr></thead>
                  <tbody>
                    <tr>
                      <td><strong>Stage 1: Grouping by Single Size</strong></td>
                      <td>Lebombo Bone (44,000 BCE) & Gumulgal Tribe</td>
                      <td>Counts tracked by notches or pairs (urapon = 1, ukasar = 2).</td>
                      <td>Replaced chaotic unorganized tallies with regular packet sizes.</td>
                    </tr>
                    <tr>
                      <td><strong>Stage 2: Arbitrary Landmark Numbers</strong></td>
                      <td>Roman Numerals (Rome, 8th c. BCE)</td>
                      <td>Specific letters assigned to fixed key milestones: I, V, X, L, C, D, M.</td>
                      <td>Allowed writing large numbers without thousands of repetitive strokes.</td>
                    </tr>
                    <tr>
                      <td><strong>Stage 3: The Base-n Power Principle</strong></td>
                      <td>Egyptian Hieroglyphs (3000 BCE)</td>
                      <td>Landmarks are powers of a fixed base n (1, 10, 100, 1000...).</td>
                      <td>Regrouping becomes predictable: n units always equal 1 next landmark!</td>
                    </tr>
                    <tr>
                      <td><strong>Stage 4: Positional Place-Value</strong></td>
                      <td>Mesopotamia (Base-60) & Maya (Base-20)</td>
                      <td>The physical position/column determines which power of the base applies.</td>
                      <td>Eliminated the need to invent infinite symbols for higher powers.</td>
                    </tr>
                    <tr>
                      <td><strong>Stage 5: Decimal System with True Zero</strong></td>
                      <td>Ancient India (Bakhshali, Aryabhata, Brahmagupta)</td>
                      <td>Ten universal digits (0–9) where 0 is both placeholder and algebraic number.</td>
                      <td>Created compact, unambiguous notation and rapid columnar arithmetic.</td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </div>
            <div class="step-box step-5">
              <span class="step-badge">Step 5: Synthesis</span>
              <p>This 45,000-year trajectory transformed numbers from physical tallies into the most powerful, abstract, and efficient calculating tool ever created by human intellect.</p>
            </div>
          </div>
        </div>
      </details>

      <!-- LA 2 -->
      <details class="ans-box">
        <summary>
          <span><i class="fa-solid fa-star" style="color: var(--accent); margin-right: 0.5rem;"></i> Question 18 (5 Marks): Comparative Analysis of Mesopotamian, Mayan, Chinese, and Hindu Systems</span>
        </summary>
        <div class="ans-content">
          <p><strong>Question:</strong> Compare the place-value systems of Mesopotamia, the Maya, China, and India across five specific parameters: (1) Base used, (2) Basic symbols, (3) Orientation of writing, (4) Treatment of empty columns (zero), and (5) Arithmetic versatility.</p>
          <div class="step-container">
            <div class="step-box step-1">
              <span class="step-badge">Step 1: Marking Scheme Breakdown (5 Marks — 1 Mark Per Parameter)</span>
              <p>• 1M for Base comparison across all 4 civilizations.<br>
              • 1M for Symbols & Glyphs comparison.<br>
              • 1M for Spatial Orientation (horizontal vs vertical).<br>
              • 1M for Zero and Placeholder mechanisms.<br>
              • 1M for Computational power and modern survivability.</p>
            </div>
            <div class="step-box step-2">
              <span class="step-badge">Step 2: Master Comparative Synthesis</span>
              <div class="table-wrapper">
                <table>
                  <thead>
                    <tr>
                      <th>Parameter</th>
                      <th>Mesopotamia (Babylon)</th>
                      <th>Maya Civilization</th>
                      <th>China (Rod Numerals)</th>
                      <th>India (Hindu System)</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr>
                      <td><strong>1. Base (n)</strong></td>
                      <td>Base 60 (Sexagesimal)</td>
                      <td>Modified Base 20 (3rd tier = 360)</td>
                      <td>Base 10 (Decimal)</td>
                      <td><strong>Base 10 (Decimal)</strong></td>
                    </tr>
                    <tr>
                      <td><strong>2. Basic Symbols</strong></td>
                      <td>Wedge (1) & Corner (10)</td>
                      <td>Dot (1), Bar (5), Shell (0)</td>
                      <td>Rods in 1–9 combinations</td>
                      <td><strong>Ten Digits: 0 through 9</strong></td>
                    </tr>
                    <tr>
                      <td><strong>3. Spatial Orientation</strong></td>
                      <td>Horizontal (Left to right)</td>
                      <td>Vertical (Bottom to top)</td>
                      <td>Horizontal (Alternating)</td>
                      <td><strong>Horizontal (Left to right)</strong></td>
                    </tr>
                    <tr>
                      <td><strong>4. Treatment of Zero</strong></td>
                      <td>Blank space / Slanted double-wedge (No terminal zero)</td>
                      <td>Seashell glyph (true placeholder, not algebraic)</td>
                      <td>Empty board square (later circle 〇)</td>
                      <td><strong>Full Circle / Dot (Śūnya): Placeholder AND Number!</strong></td>
                    </tr>
                    <tr>
                      <td><strong>5. Arithmetic Versatility</strong></td>
                      <td>Excellent for fractions; ambiguous for whole numbers</td>
                      <td>Astronomical calendar tracking; awkward for trade</td>
                      <td>Fast on counting board; rods easily disordered</td>
                      <td><strong>Supreme universality; fastest paper-and-pencil algorithms</strong></td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </div>
            <div class="step-box step-5">
              <span class="step-badge">Step 5: Concluding Verdict</span>
              <p>The Hindu system triumphed globally because it combined the decimal base, compact single-character digits, horizontal orientation, and the complete algebraic codification of zero.</p>
            </div>
          </div>
        </div>
      </details>

      <!-- LA 3 -->
      <details class="ans-box">
        <summary>
          <span><i class="fa-solid fa-star" style="color: var(--accent); margin-right: 0.5rem;"></i> Question 19 (5 Marks): Comprehensive Multi-Base Arithmetic Problem</span>
        </summary>
        <div class="ans-content">
          <p><strong>Question:</strong> <br>
          (a) Evaluate the sum in Base-5: <code>243₅ + 134₅</code> showing all column carry-over regroupings. <br>
          (b) Convert the addends and the result into decimal to verify correctness. <br>
          (c) Express the final sum in Base-2 (Binary).</p>
          <div class="step-container">
            <div class="step-box step-1">
              <span class="step-badge">Step 1: Marking Scheme Breakdown (5 Marks)</span>
              <p>• 2 Marks for column-by-column Base-5 addition with carry.<br>• 1.5 Marks for decimal conversion of addends and sum verification.<br>• 1.5 Marks for converting the sum to binary.</p>
            </div>
            <div class="step-box step-2">
              <span class="step-badge">Step 2: Base-5 Addition Execution</span>
              <p>Arrange in columns: <br>
              &nbsp;&nbsp;[Carry]: &nbsp; (1) &nbsp; (1) <br>
              &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 2 &nbsp;&nbsp; 4 &nbsp;&nbsp; 3 <br>
              &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; + &nbsp; 1 &nbsp;&nbsp; 3 &nbsp;&nbsp; 4 <br>
              &nbsp;&nbsp;-------------------</p>
              <ul style="margin-left: 1.5rem; line-height: 1.8;">
                <li><strong>Units Column:</strong> 3 + 4 = 7. In Base-5: 7 ÷ 5 = 1 with remainder 2. Write <strong>2</strong> in units, carry <strong>1</strong> to fives column!</li>
                <li><strong>Fives Column:</strong> 4 + 3 + 1 (carry) = 8. In Base-5: 8 ÷ 5 = 1 with remainder 3. Write <strong>3</strong> in fives, carry <strong>1</strong> to twenty-fives column!</li>
                <li><strong>Twenty-Fives Column:</strong> 2 + 1 + 1 (carry) = 4. Since 4 < 5, write <strong>4</strong>!</li>
                <li><strong>Base-5 Sum:</strong> <code>432₅</code>.</li>
              </ul>
            </div>
            <div class="step-box step-3">
              <span class="step-badge">Step 3: Decimal Verification</span>
              <ul style="margin-left: 1.5rem; line-height: 1.8;">
                <li><code>243₅ = (2 × 25) + (4 × 5) + (3 × 1) = 50 + 20 + 3 = 73₁₀</code>.</li>
                <li><code>134₅ = (1 × 25) + (3 × 5) + (4 × 1) = 25 + 15 + 4 = 44₁₀</code>.</li>
                <li>Decimal Sum: <code>73 + 44 = 117₁₀</code>.</li>
                <li>Verify 432₅ in decimal: <code>(4 × 25) + (3 × 5) + (2 × 1) = 100 + 15 + 2 = 117₁₀</code>. <strong>100% Verified!</strong></li>
              </ul>
            </div>
            <div class="step-box step-4">
              <span class="step-badge">Step 4: Conversion of 117 to Base-2 (Binary)</span>
              <p>Successive division of 117 by 2: <br>
              117 ÷ 2 = 58 rem <strong>1</strong>; 58 ÷ 2 = 29 rem <strong>0</strong>; 29 ÷ 2 = 14 rem <strong>1</strong>; 14 ÷ 2 = 7 rem <strong>0</strong>; 7 ÷ 2 = 3 rem <strong>1</strong>; 3 ÷ 2 = 1 rem <strong>1</strong>; 1 ÷ 2 = 0 rem <strong>1</strong>. <br>
              Reading remainders bottom to top: <code>117₁₀ = 1110101₂</code>. <br>
              Check: 64 + 32 + 16 + 4 + 1 = 117. Correct!</p>
            </div>
            <div class="step-box step-5">
              <span class="step-badge">Step 5: Final Answers</span>
              <p>
                <strong>(a) 243₅ + 134₅ = 432₅</strong> <br>
                <strong>(b) Decimal Verification: 73 + 44 = 117 (Matches 432₅ = 117)</strong> <br>
                <strong>(c) Binary Representation: 1110101₂</strong>
              </p>
            </div>
          </div>
        </div>
      </details>

      <!-- LA 4 -->
      <details class="ans-box">
        <summary>
          <span><i class="fa-solid fa-star" style="color: var(--accent); margin-right: 0.5rem;"></i> Question 20 (5 Marks): Global Transmission of Hindu Numerals</span>
        </summary>
        <div class="ans-content">
          <p><strong>Question:</strong> Describe the historical journey of the Hindu number system from ancient India to the Arab world, Europe, and the modern globe. Detail the key contributions of Al-Khwārizmī, Al-Kindī, Fibonacci, and Pierre-Simon Laplace.</p>
          <div class="step-container">
            <div class="step-box step-1">
              <span class="step-badge">Step 1: Marking Scheme Breakdown (5 Marks)</span>
              <p>• 1 Mark for Indian roots (Bakhshali, Aryabhata, Brahmagupta).<br>
              • 1.5 Marks for transmission to Baghdad & contributions of Al-Khwārizmī and Al-Kindī.<br>
              • 1.5 Marks for European transmission via Fibonacci's <em>Liber Abaci</em> and Renaissance adoption.<br>
              • 1 Mark for Laplace's philosophical evaluation.</p>
            </div>
            <div class="step-box step-2">
              <span class="step-badge">Step 2: Indian Genesis (c. 200 BCE – 628 CE)</span>
              <p>Ancient Vedic texts established oral decimal naming up to 10¹². The Bakhshali Manuscript (c. 3rd century CE) provided the earliest physical record of zero as a dot. Aryabhata (499 CE) formalized place value, and Brahmagupta (628 CE) codified algebraic rules for zero and negatives.</p>
            </div>
            <div class="step-box step-3">
              <span class="step-badge">Step 3: The Golden Age of Baghdad (c. 800–850 CE)</span>
              <p>Indian astronomical treatises (the <em>Brahmasphutasiddhanta</em>) were translated into Arabic in Baghdad. Persian mathematician <strong>Muḥammad ibn Mūsā al-Khwārizmī</strong> wrote <em>On the Calculation with Hindu Numerals</em> (c. 825 CE), transmitting the decimal algorithm (from whose Latinized name <em>Algoritmi</em> we derive the word <strong>algorithm</strong>!). Philosopher <strong>Al-Kindī</strong> wrote <em>On the Use of the Hindu Numerals</em> (c. 830 CE), popularizing them throughout the Islamic empire.</p>
            </div>
            <div class="step-box step-4">
              <span class="step-badge">Step 4: European Transmission via Fibonacci (1202 CE)</span>
              <p>Because European scholars encountered these numerals through Arab texts, they referred to them as "Arabic numerals", whereas Arab scholars explicitly recognized them as "Hindu numerals" (<em>al-arqām al-hindiyyah</em>). In 1202 CE, Italian merchant <strong>Leonardo Fibonacci</strong> published <em>Liber Abaci</em> (The Book of Calculation), championing the 9 Indian digits plus sign zero (zephirum). Despite fierce resistance from traditional Roman abacists, the European scientific Renaissance made adopting Hindu numerals unavoidable by the 17th century.</p>
            </div>
            <div class="step-box step-5">
              <span class="step-badge">Step 5: Laplace's Universal Assessment</span>
              <p>In 1814, French mathematician <strong>Pierre-Simon Laplace</strong> celebrated India's discovery as a masterpiece of economy and power, writing that its sheer simplicity facilitated computations and elevated arithmetic to the foremost ranks of human inventions.</p>
            </div>
          </div>
        </div>
      </details>

      <!-- ======================================================== -->
      <!-- PART 5: 2 COMPETENCY-BASED REAL-WORLD CASE STUDIES       -->
      <!-- ======================================================== -->
      <h3><i class="fa-solid fa-briefcase" style="color: var(--danger);"></i> 5. Competency-Based Real-World Case Studies</h3>

      <!-- CASE STUDY 1 -->
      <details class="ans-box">
        <summary>
          <span><i class="fa-solid fa-satellite" style="color: var(--danger); margin-right: 0.5rem;"></i> Case Study 1: Deep Space Telemetry & The Clash of Number Systems</span>
        </summary>
        <div class="ans-content">
          <div style="background: #fff1f2; border-left: 4px solid var(--danger); padding: 1.25rem; border-radius: var(--radius-sm); margin-bottom: 1.25rem;">
            <h5 style="color: #9f1239; margin-bottom: 0.5rem;"><i class="fa-solid fa-rocket"></i> Space Mission Flight Dynamics</h5>
            <p style="font-size: 0.95rem; line-height: 1.7; margin: 0;">
              ISRO's deep-space satellite tracking station receives raw telemetry data from an interplanetary probe orbiting Mars. The onboard computer encodes antenna angle telemetry in <strong>Base-2 (binary)</strong>, timestamps the mission elapsed time using the ancient Babylonian <strong>sexagesimal base-60</strong> standard (hours, minutes, seconds), and transmits battery voltage levels in <strong>Base-10 (decimal)</strong>. A ground engineer receives a data packet containing: <br>
              • Telemetry Status Flag: <code>11010₂</code> <br>
              • Mission Elapsed Angle: <code>2 hours, 15 minutes, 30 seconds</code> <br>
              • Sensor Battery Level: <code>43 Volts</code>
            </p>
          </div>
          <p><strong>Questions:</strong> <br>
          1. Convert the binary status flag <code>11010₂</code> into standard decimal. <br>
          2. Express the mission elapsed time (2 hr 15 min 30 sec) purely in seconds, and show how the Mesopotamians would write this number in base-60 cuneiform. <br>
          3. Convert the battery level (43 V) into Base-5.</p>

          <div class="step-container">
            <div class="step-box step-1">
              <span class="step-badge">Step 1: Solution to Question 1 (Binary to Decimal)</span>
              <p><code>11010₂ = (1 × 2⁴) + (1 × 2³) + (0 × 2²) + (1 × 2¹) + (0 × 2⁰)</code> <br>
              = 16 + 8 + 0 + 2 + 0 = <strong>26</strong>. <br>
              The telemetry status flag is <strong>26</strong>.</p>
            </div>
            <div class="step-box step-2">
              <span class="step-badge">Step 2: Solution to Question 2 (Sexagesimal Time Conversion)</span>
              <p>Convert 2 hr 15 min 30 sec to total seconds: <br>
              • 2 hours = 2 × 3,600 = 7,200 seconds. <br>
              • 15 minutes = 15 × 60 = 900 seconds. <br>
              • 30 seconds = 30 seconds. <br>
              Total Seconds = 7,200 + 900 + 30 = <strong>8,130 seconds</strong>. <br>
              In Mesopotamian Base-60: <br>
              <code>8130 = (2 × 3600) + (15 × 60) + (30 × 1)</code>. <br>
              • 3600s place: 2 wedges <code>[▼▼]</code> <br>
              • 60s place: 1 corner + 5 wedges <code>[◄ ▼▼▼▼▼]</code> <br>
              • 1s place: 3 corners <code>[◄◄◄]</code>.</p>
            </div>
            <div class="step-box step-3">
              <span class="step-badge">Step 3: Solution to Question 3 (Decimal 43 to Base-5)</span>
              <p>43 = (1 × 25) + (3 × 5) + (3 × 1) → <strong>133₅</strong>.</p>
            </div>
            <div class="step-box step-5">
              <span class="step-badge">Step 5: Final Case Study Summary</span>
              <p>Status Flag = <strong>26</strong>; Total Seconds = <strong>8,130 s</strong> (2, 15, 30 in base-60); Battery Level = <strong>133₅</strong>.</p>
            </div>
          </div>
        </div>
      </details>

      <!-- CASE STUDY 2 -->
      <details class="ans-box">
        <summary>
          <span><i class="fa-solid fa-archway" style="color: var(--danger); margin-right: 0.5rem;"></i> Case Study 2: Archaeological Decryption of an Ancient Trade Tablet</span>
        </summary>
        <div class="ans-content">
          <div style="background: #fff1f2; border-left: 4px solid var(--danger); padding: 1.25rem; border-radius: var(--radius-sm); margin-bottom: 1.25rem;">
            <h5 style="color: #9f1239; margin-bottom: 0.5rem;"><i class="fa-solid fa-magnifying-glass"></i> The Maritime Mediterranean Dig</h5>
            <p style="font-size: 0.95rem; line-height: 1.7; margin: 0;">
              Archaeologists excavating a Bronze Age trading port in the eastern Mediterranean discover an ancient cargo manifest recording an olive oil transaction between an Egyptian merchant and a Roman envoy. The document records two shipments: <br>
              • <strong>Shipment 1 (Egyptian hieroglyphic script):</strong> [1 Coil of Rope + 8 Heel Bones + 5 Single Strokes] jars of oil. <br>
              • <strong>Shipment 2 (Roman numerical script):</strong> <code>CCXLVII</code> jars of oil. <br>
              A debate arises among researchers regarding which shipment was larger and what total volume of olive oil was received.
            </p>
          </div>
          <p><strong>Questions:</strong> <br>
          1. Calculate the exact decimal count of olive oil jars in Shipment 1. <br>
          2. Calculate the exact decimal count of olive oil jars in Shipment 2. <br>
          3. Determine which shipment was larger and by how many jars. <br>
          4. Express the total combined jars of both shipments in Roman numerals.</p>

          <div class="step-container">
            <div class="step-box step-1">
              <span class="step-badge">Step 1: Decoding Shipment 1 (Egyptian Hieroglyphs)</span>
              <p>• 1 Coil of Rope = 1 × 100 = 100. <br>
              • 8 Heel Bones = 8 × 10 = 80. <br>
              • 5 Single Strokes = 5 × 1 = 5. <br>
              Total Shipment 1 = 100 + 80 + 5 = <strong>185 jars</strong>.</p>
            </div>
            <div class="step-box step-2">
              <span class="step-badge">Step 2: Decoding Shipment 2 (Roman CCXLVII)</span>
              <p>• CC = 100 + 100 = 200. <br>
              • XL = 50 - 10 = 40. <br>
              • VII = 5 + 1 + 1 = 7. <br>
              Total Shipment 2 = 200 + 40 + 7 = <strong>247 jars</strong>.</p>
            </div>
            <div class="step-box step-3">
              <span class="step-badge">Step 3: Comparison & Difference</span>
              <p>247 > 185. Therefore, <strong>Shipment 2 was larger</strong>. <br>
              Difference = 247 - 185 = <strong>62 jars</strong>.</p>
            </div>
            <div class="step-box step-4">
              <span class="step-badge">Step 4: Total Combined Volume in Roman Numerals</span>
              <p>Total Jars = 185 + 247 = <strong>432 jars</strong>. <br>
              Decomposing 432 into Roman landmarks: <br>
              400 (CD) + 30 (XXX) + 2 (II) = <strong>CDXXXII</strong>.</p>
            </div>
            <div class="step-box step-5">
              <span class="step-badge">Step 5: Final Answers</span>
              <p>
                <strong>1. Shipment 1 = 185 jars</strong> <br>
                <strong>2. Shipment 2 = 247 jars</strong> <br>
                <strong>3. Shipment 2 was larger by 62 jars</strong> <br>
                <strong>4. Combined Total = 432 jars (Roman: CDXXXII)</strong>
              </p>
            </div>
          </div>
        </div>
      </details>

      <!-- ======================================================== -->
      <!-- PART 6: 5 PYQS & MOST PROBABLE EXAM QUESTIONS            -->
      <!-- ======================================================== -->
      <h3><i class="fa-solid fa-graduation-cap" style="color: var(--primary);"></i> 6. Previous Years Questions (PYQs) & Most Probable Exam Models</h3>

      <!-- PYQ 1 -->
      <details class="ans-box">
        <summary>
          <span><i class="fa-solid fa-clock-rotate-left" style="color: var(--primary); margin-right: 0.5rem;"></i> Question 23 (PYQ): Landmark Multiples in Base-10 Systems</span>
        </summary>
        <div class="ans-content">
          <p><strong>Exam Question:</strong> If a number system is constructed with base 10, explain why multiplying any number by 10 shifts each symbol to the next higher landmark. Illustrate using both Egyptian hieroglyphs and modern Hindu numerals.</p>
          <div class="step-container">
            <div class="step-box step-1">
              <span class="step-badge">Step 1: Core Mathematical Law</span>
              <p>In any base-10 system, the landmark values are the ascending powers of 10: <code>10⁰, 10¹, 10², 10³, ...</code> Multiplying any term <code>k × 10ⁿ</code> by 10 yields <code class="math-code">(k × 10ⁿ) × 10¹ = k × 10ⁿ⁺¹</code>.</p>
            </div>
            <div class="step-box step-2">
              <span class="step-badge">Step 2: Egyptian Hieroglyphic Illustration</span>
              <p>Multiplying 3 heel bones (3 × 10) by 10 yields 30 × 10 = 300, which transforms the 3 heel bones directly into <strong>3 coils of rope</strong>! The physical glyph changes to the next higher picture on the ladder.</p>
            </div>
            <div class="step-box step-3">
              <span class="step-badge">Step 3: Hindu Positional Illustration</span>
              <p>In modern Hindu numerals, multiplying 35 by 10 shifts the digit 3 from the tens column (3 × 10) to the hundreds column (3 × 100) and the digit 5 from units (5 × 1) to tens (5 × 10), while the newly vacated units column is filled with <code>0</code>, resulting in <strong>350</strong>.</p>
            </div>
            <div class="step-box step-5">
              <span class="step-badge">Step 5: Final Conclusion</span>
              <p>In both systems, multiplication by the base increases the exponent by 1. In Egyptian it transforms the glyph; in Hindu numerals it shifts columns and appends zero.</p>
            </div>
          </div>
        </div>
      </details>

      <!-- PYQ 2 -->
      <details class="ans-box">
        <summary>
          <span><i class="fa-solid fa-clock-rotate-left" style="color: var(--primary); margin-right: 0.5rem;"></i> Question 24 (PYQ): Why Base-60 is Preserved in Modern Timekeeping</span>
        </summary>
        <div class="ans-content">
          <p><strong>Exam Question:</strong> Although modern civilization uses the base-10 Hindu decimal system for all science and commerce, two everyday measurements still strictly preserve the ancient Babylonian base-60 system. Identify these two measurements and explain why base 60 is exceptionally advantageous for them.</p>
          <div class="step-container">
            <div class="step-box step-1">
              <span class="step-badge">Step 1: Identification of the Two Measurements</span>
              <p>The two everyday measurements are: <br>
              1. <strong>Time Measurement:</strong> 1 hour = 60 minutes, and 1 minute = 60 seconds. <br>
              2. <strong>Angular & Circular Measurement (Geometry & Navigation):</strong> A complete circle = 360° (6 × 60°), 1 degree of arc = 60 arcminutes, and 1 arcminute = 60 arcseconds.</p>
            </div>
            <div class="step-box step-2">
              <span class="step-badge">Step 2: Mathematical Advantage of 60</span>
              <p>The number 60 is a <strong>superior highly composite number</strong>. It possesses <strong>12 distinct divisors</strong>: <code>1, 2, 3, 4, 5, 6, 10, 12, 15, 20, 30, and 60</code>. <br>
              Because 60 can be divided cleanly into halves (30 min), thirds (20 min), quarters (15 min), fifths (12 min), and sixths (10 min) without producing recurring decimals, it is the most practical base for dividing clocks and navigational compasses!</p>
            </div>
            <div class="step-box step-5">
              <span class="step-badge">Step 5: Final Answer</span>
              <p>Time (hours/minutes/seconds) and Geometry (degrees/minutes of arc) preserve base 60 because of 60's unmatched divisibility by 1, 2, 3, 4, 5, and 6.</p>
            </div>
          </div>
        </div>
      </details>

      <!-- PYQ 3 -->
      <details class="ans-box">
        <summary>
          <span><i class="fa-solid fa-clock-rotate-left" style="color: var(--primary); margin-right: 0.5rem;"></i> Question 25 (PYQ): The Role of the Bakhshali Manuscript</span>
        </summary>
        <div class="ans-content">
          <p><strong>Exam Question:</strong> What is the historical importance of the Bakhshali manuscript in the story of numbers? When and where was it discovered, and what did scientific radiocarbon dating reveal?</p>
          <div class="step-container">
            <div class="step-box step-1">
              <span class="step-badge">Step 1: Discovery Context</span>
              <p>The Bakhshali manuscript was discovered in <strong>1881</strong> by a farmer digging in a field in the village of Bakhshali, near Peshawar (ancient Gandhara, in undivided India). It consists of 70 fragile birch-bark leaves written in the ancient Śāradā script and Sanskrit language.</p>
            </div>
            <div class="step-box step-2">
              <span class="step-badge">Step 2: Scientific Radiocarbon Dating (Oxford University, 2017)</span>
              <p>In 2017, the Bodleian Libraries at the University of Oxford conducted carbon-14 dating on the manuscript. The tests astonished historians worldwide by dating the oldest birch bark to <strong>c. 224–383 CE (3rd to 4th century CE)</strong> — making it nearly 500 years older than scholars previously believed!</p>
            </div>
            <div class="step-box step-3">
              <span class="step-badge">Step 3: Mathematical Significance</span>
              <p>The Bakhshali manuscript contains the <strong>world's oldest recorded physical evidence of zero used as a dot (śūnya-bindu)</strong> within active algebraic and commercial calculations (calculating square roots, fractions, and profit-and-loss).</p>
            </div>
            <div class="step-box step-5">
              <span class="step-badge">Step 5: Final Conclusion</span>
              <p>The Bakhshali manuscript scientifically establishes India as the birthplace of the written symbol for zero as early as the 3rd century CE.</p>
            </div>
          </div>
        </div>
      </details>

      <!-- PYQ 4 -->
      <details class="ans-box">
        <summary>
          <span><i class="fa-solid fa-clock-rotate-left" style="color: var(--primary); margin-right: 0.5rem;"></i> Question 26 (Most Probable): Bi-Quinary Mechanism of the Abacus</span>
        </summary>
        <div class="ans-content">
          <p><strong>Exam Question:</strong> Why is the Roman counting abacus described as a "bi-quinary" calculating board? Explain how a column with only 4 lower beads and 1 upper bead can represent all digits from 0 to 9.</p>
          <div class="step-container">
            <div class="step-box step-1">
              <span class="step-badge">Step 1: Defining Bi-Quinary Structure</span>
              <p>"Bi-quinary" means a hybrid combination of base 2 (bi) and base 5 (quinary). In each decimal column: <br>
              • The <strong>lower deck</strong> contains 4 beads, each having a value of <strong>1</strong>. <br>
              • The <strong>upper deck</strong> contains 1 bead, having a value of <strong>5</strong>.</p>
            </div>
            <div class="step-box step-2">
              <span class="step-badge">Step 2: Representing Digits 0 through 9</span>
              <ul style="margin-left: 1.5rem; line-height: 1.8;">
                <li><code>0:</code> Upper bead up (inactive); all 4 lower beads down (inactive).</li>
                <li><code>1 to 4:</code> Push 1, 2, 3, or 4 lower beads up toward the center beam.</li>
                <li><code>5:</code> Pull the upper bead down to the beam (value 5); clear all lower beads to bottom.</li>
                <li><code>6 to 9:</code> Upper bead down (5) + push 1, 2, 3, or 4 lower beads up (5+1=6, 5+2=7, 5+3=8, 5+4=9).</li>
              </ul>
            </div>
            <div class="step-box step-3">
              <span class="step-badge">Step 3: Engineering Efficiency</span>
              <p>Instead of requiring 9 separate beads per column (which would be bulky and hard to read at a glance), the bi-quinary system achieves all 10 states (0 to 9) using only <strong>5 total beads</strong> per column!</p>
            </div>
            <div class="step-box step-5">
              <span class="step-badge">Step 5: Final Conclusion</span>
              <p>The bi-quinary abacus represents 0–9 using 1 upper bead (value 5) and 4 lower beads (value 1 each), drastically minimizing bead count and visual clutter.</p>
            </div>
          </div>
        </div>
      </details>

      <!-- PYQ 5 -->
      <details class="ans-box">
        <summary>
          <span><i class="fa-solid fa-clock-rotate-left" style="color: var(--primary); margin-right: 0.5rem;"></i> Question 27 (Most Probable): The Octal World — Alien Mathematics</span>
        </summary>
        <div class="ans-content">
          <p><strong>Exam Question:</strong> Suppose an astronaut lands on an alien planet whose inhabitants have 4 fingers on each hand (8 fingers in total). <br>
          (a) What base would these aliens naturally use? What digits would exist in their system? <br>
          (b) How would they write their count of 64 spaceship fuel pods? <br>
          (c) What decimal quantity does their numeral <code>125₈</code> represent?</p>
          <div class="step-container">
            <div class="step-box step-1">
              <span class="step-badge">Step 1: Part (a) — Base and Permissible Digits</span>
              <p>Because humans use base 10 due to 10 fingers, 8-fingered aliens would naturally adopt <strong>Base-8 (Octal)</strong>. <br>
              Their system would possess exactly <strong>8 digits: 0, 1, 2, 3, 4, 5, 6, 7</strong>. The digit '8' would not exist!</p>
            </div>
            <div class="step-box step-2">
              <span class="step-badge">Step 2: Part (b) — Writing Decimal 64 in Base-8</span>
              <p>In Base-8, the landmark values are: 8⁰ = 1, 8¹ = 8, 8² = 64. <br>
              64 = (1 × 8²) + (0 × 8¹) + (0 × 8⁰). <br>
              The aliens would write 64 as: <strong>100₈</strong>!</p>
            </div>
            <div class="step-box step-3">
              <span class="step-badge">Step 3: Part (c) — Decoding Alien Numeral 125₈ to Decimal</span>
              <p><code>125₈ = (1 × 8²) + (2 × 8¹) + (5 × 8⁰)</code> <br>
              = (1 × 64) + (2 × 8) + (5 × 1) <br>
              = 64 + 16 + 5 = <strong>85₁₀</strong>.</p>
            </div>
            <div class="step-box step-5">
              <span class="step-badge">Step 5: Final Answers</span>
              <p>
                <strong>(a) Base-8 (Octal); Permissible digits: 0, 1, 2, 3, 4, 5, 6, 7</strong> <br>
                <strong>(b) 64 fuel pods is written as 100₈</strong> <br>
                <strong>(c) Numeral 125₈ equals 85 in decimal</strong>
              </p>
            </div>
          </div>
        </div>
      </details>

    </section>
"""
