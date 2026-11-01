# -*- coding: utf-8 -*-
"""
Section 5 Part 1 Module: MCQs, Assertion-Reasoning & Short Answer Questions
Class 8 Mathematics Chapter 12: Tales by Dots and Lines (NCERT NEP code: hegp112)
"""

def get_section_5_part1():
    return """
    <!-- SECTION 5: COMPLETE EXAM QUESTION BANK (PART 1) -->
    <section id="section5" class="section-box">
      <div class="section-header">
        <div class="section-header-left">
          <span class="section-tag">Exam Hall Readiness</span>
          <h2 class="section-title">§ 5. Complete Exam Question Bank (Part 1: MCQs, Assertion-Reason &amp; SAQs)</h2>
          <p class="section-desc">
            Rigorous examination practice designed around CBSE and BSE Odisha patterns. Includes an interactive MCQ quiz engine with immediate feedback, trap explanations, standard Assertion-Reasoning drills, and 2M/3M Short Answer Questions.
          </p>
        </div>
        <div>
          <span class="badge badge-emerald"><i class="fa-solid fa-trophy"></i> Exam Ready</span>
        </div>
      </div>

      <!-- ========================================================
           SUBSECTION 5A: 5 INTERACTIVE CONCEPTUAL MCQS
           ======================================================== -->
      <div style="margin-bottom: 2.5rem;">
        <h3 style="font-family: 'Space Grotesk', sans-serif; font-size: 1.4rem; color: var(--primary-dark); margin-bottom: 1.25rem;">
          <i class="fa-solid fa-circle-question"></i> Part 5A: Conceptual MCQs (Interactive Quiz Engine)
        </h3>

        <!-- Interactive Score Banner -->
        <div class="score-banner">
          <h3>Interactive Concept Mastery Quiz</h3>
          <p>Test your knowledge! Click on the best answer. Get instant visual evaluation and detailed trap explanations.</p>
          <div style="font-family: 'JetBrains Mono', monospace; font-size: 1.1rem; margin-top: 0.5rem;" id="quizScoreDisplay">
            Score: <span id="currentScore">0</span> / 5 Completed
          </div>
        </div>

        <!-- MCQ 1 -->
        <div class="quiz-card" id="mcqCard1">
          <div class="quiz-q-num">Question 1 • Single Choice</div>
          <div class="quiz-q-text">
            A dataset of 20 observations has an arithmetic mean of 45. If each of the 20 numbers is increased by 7 and then multiplied by 2, what is the new arithmetic mean?
          </div>
          <div class="options-grid">
            <button class="opt-btn" onclick="checkMCQ(1, 'A', false)">
              <span>(A)</span> 90
            </button>
            <button class="opt-btn" onclick="checkMCQ(1, 'B', true)">
              <span>(B)</span> 104
            </button>
            <button class="opt-btn" onclick="checkMCQ(1, 'C', false)">
              <span>(C)</span> 97
            </button>
            <button class="opt-btn" onclick="checkMCQ(1, 'D', false)">
              <span>(D)</span> 59
            </button>
          </div>
          <div class="eval-box" id="evalBox1"></div>
        </div>

        <!-- MCQ 2 -->
        <div class="quiz-card" id="mcqCard2">
          <div class="quiz-q-num">Question 2 • Single Choice</div>
          <div class="quiz-q-text">
            On a number line dot plot, the mean of five numbers is 18. Points lie at 12, 14, 18, 22, and <span class="math-inline">x</span>. Using the balance of distances (fulcrum principle), what is the value of <span class="math-inline">x</span>?
          </div>
          <div class="options-grid">
            <button class="opt-btn" onclick="checkMCQ(2, 'A', false)">
              <span>(A)</span> 20
            </button>
            <button class="opt-btn" onclick="checkMCQ(2, 'B', false)">
              <span>(B)</span> 26
            </button>
            <button class="opt-btn" onclick="checkMCQ(2, 'C', true)">
              <span>(C)</span> 24
            </button>
            <button class="opt-btn" onclick="checkMCQ(2, 'D', false)">
              <span>(D)</span> 16
            </button>
          </div>
          <div class="eval-box" id="evalBox2"></div>
        </div>

        <!-- MCQ 3 -->
        <div class="quiz-card" id="mcqCard3">
          <div class="quiz-q-num">Question 3 • Single Choice</div>
          <div class="quiz-q-text">
            A frequency distribution lists test scores: Score 10 (f = 2), Score 20 (f = 5), Score 30 (f = 8), Score 40 (f = 5). What is the median score?
          </div>
          <div class="options-grid">
            <button class="opt-btn" onclick="checkMCQ(3, 'A', false)">
              <span>(A)</span> 25
            </button>
            <button class="opt-btn" onclick="checkMCQ(3, 'B', true)">
              <span>(B)</span> 30
            </button>
            <button class="opt-btn" onclick="checkMCQ(3, 'C', false)">
              <span>(C)</span> 20
            </button>
            <button class="opt-btn" onclick="checkMCQ(3, 'D', false)">
              <span>(D)</span> 35
            </button>
          </div>
          <div class="eval-box" id="evalBox3"></div>
        </div>

        <!-- MCQ 4 -->
        <div class="quiz-card" id="mcqCard4">
          <div class="quiz-q-num">Question 4 • Single Choice</div>
          <div class="quiz-q-text">
            Which spreadsheet formula correctly computes the arithmetic average of marks entered in cells C4, C5, C6, C7, C8, and C9?
          </div>
          <div class="options-grid">
            <button class="opt-btn" onclick="checkMCQ(4, 'A', false)">
              <span>(A)</span> =MEAN(C4:C9)
            </button>
            <button class="opt-btn" onclick="checkMCQ(4, 'B', false)">
              <span>(B)</span> =SUM(C4:C9)/C
            </button>
            <button class="opt-btn" onclick="checkMCQ(4, 'C', true)">
              <span>(C)</span> =AVERAGE(C4:C9)
            </button>
            <button class="opt-btn" onclick="checkMCQ(4, 'D', false)">
              <span>(D)</span> =AVG(C4 to C9)
            </button>
          </div>
          <div class="eval-box" id="evalBox4"></div>
        </div>

        <!-- MCQ 5 -->
        <div class="quiz-card" id="mcqCard5">
          <div class="quiz-q-num">Question 5 • Single Choice</div>
          <div class="quiz-q-text">
            On a line graph plotting temperature across 12 months, the line segment between March and May is much steeper than between January and March. What does this geometric steepness signify?
          </div>
          <div class="options-grid">
            <button class="opt-btn" onclick="checkMCQ(5, 'A', true)">
              <span>(A)</span> The rate of temperature increase is faster between March and May.
            </button>
            <button class="opt-btn" onclick="checkMCQ(5, 'B', false)">
              <span>(B)</span> Total rainfall was higher between March and May.
            </button>
            <button class="opt-btn" onclick="checkMCQ(5, 'C', false)">
              <span>(C)</span> The average temperature is lower between March and May.
            </button>
            <button class="opt-btn" onclick="checkMCQ(5, 'D', false)">
              <span>(D)</span> The days were shorter between March and May.
            </button>
          </div>
          <div class="eval-box" id="evalBox5"></div>
        </div>
      </div>

      <!-- ========================================================
           SUBSECTION 5B: 5 ASSERTION & REASONING QUESTIONS
           ======================================================== -->
      <div style="margin-bottom: 2.5rem;">
        <h3 style="font-family: 'Space Grotesk', sans-serif; font-size: 1.4rem; color: var(--primary-dark); margin-bottom: 1.25rem;">
          <i class="fa-solid fa-scale-unbalanced-flip"></i> Part 5B: Assertion &amp; Reasoning Questions
        </h3>
        <p style="font-size: 0.9rem; color: var(--text-muted); margin-bottom: 1.25rem;">
          <strong>Direction:</strong> In each question below, an <em>Assertion (A)</em> is followed by a <em>Reason (R)</em>. Choose the correct option:
          <br><strong>(A)</strong> Both (A) and (R) are true, and (R) is the correct explanation of (A).
          <br><strong>(B)</strong> Both (A) and (R) are true, but (R) is NOT the correct explanation of (A).
          <br><strong>(C)</strong> (A) is true, but (R) is false.
          <br><strong>(D)</strong> (A) is false, but (R) is true.
        </p>

        <!-- A&R 1 -->
        <div class="solved-card">
          <div class="solved-title"><i class="fa-solid fa-code-compare"></i> Question 6: Assertion &amp; Reason on Linear Transformation</div>
          <p>
            <strong>Assertion (A):</strong> If the mean mark of 30 students in a mathematics test is 62, and the teacher awards 3 bonus marks to every student, the new mean mark will be 65.
            <br><strong>Reason (R):</strong> When a constant <span class="math-inline">c</span> is added to each observation in a dataset, the new mean increases by <span class="math-inline">c</span> because <span class="math-inline">x̄' = (&Sigma; (x_i + c)) / (n) = x̄ + c</span>.
          </p>
          <details class="ans-box">
            <summary>View Model Answer &amp; Explanation</summary>
            <div class="ans-content">
              <div class="step-box">
                <div class="step-num"><i class="fa-solid fa-check"></i></div>
                <div class="step-text">
                  <strong>Correct Answer: (A) Both (A) and (R) are true, and (R) is the correct explanation of (A).</strong>
                  <br>&bull; <em>Explanation:</em> Assertion (A) directly applies the linear shifting theorem with <span class="math-inline">x̄ = 62</span> and <span class="math-inline">c = 3</span>, yielding <span class="math-inline">x̄' = 62 + 3 = 65</span>. Reason (R) provides the exact algebraic theorem and proof explaining why this rigid translation occurs.
                </div>
              </div>
            </div>
          </details>
        </div>

        <!-- A&R 2 -->
        <div class="solved-card">
          <div class="solved-title"><i class="fa-solid fa-code-compare"></i> Question 7: Assertion &amp; Reason on Outlier Sensitivity</div>
          <p>
            <strong>Assertion (A):</strong> If an extreme outlier (such as ₹10,00,000) is added to a dataset of typical middle-class pocket allowances, the median increases drastically.
            <br><strong>Reason (R):</strong> The median is a positional measure of central tendency determined by the middle rank, making it highly robust against extreme values.
          </p>
          <details class="ans-box">
            <summary>View Model Answer &amp; Explanation</summary>
            <div class="ans-content">
              <div class="step-box">
                <div class="step-num"><i class="fa-solid fa-check"></i></div>
                <div class="step-text">
                  <strong>Correct Answer: (D) (A) is false, but (R) is true.</strong>
                  <br>&bull; <em>Explanation:</em> Assertion (A) is completely <strong>false</strong>! It is the <em>mean</em> that explodes when a massive outlier is added, not the median. Reason (R) is a completely <strong>true</strong> mathematical statement defining the robustness of the median.
                </div>
              </div>
            </div>
          </details>
        </div>

        <!-- A&R 3 -->
        <div class="solved-card">
          <div class="solved-title"><i class="fa-solid fa-code-compare"></i> Question 8: Assertion &amp; Reason on Uniqueness of the Fulcrum</div>
          <p>
            <strong>Assertion (A):</strong> For any collection of real numbers, there exists one and only one value where the sum of distances of points to its left equals the sum of distances of points to its right.
            <br><strong>Reason (R):</strong> Moving the center point to the right simultaneously increases all leftward distances and decreases all rightward distances, destroying balance.
          </p>
          <details class="ans-box">
            <summary>View Model Answer &amp; Explanation</summary>
            <div class="ans-content">
              <div class="step-box">
                <div class="step-num"><i class="fa-solid fa-check"></i></div>
                <div class="step-text">
                  <strong>Correct Answer: (A) Both (A) and (R) are true, and (R) is the correct explanation of (A).</strong>
                  <br>&bull; <em>Explanation:</em> Assertion (A) states the uniqueness of the arithmetic mean as the physical fulcrum. Reason (R) provides the rigorous proof by contradiction demonstrating that any deviation from the mean destroys distance equality.
                </div>
              </div>
            </div>
          </details>
        </div>

        <!-- A&R 4 -->
        <div class="solved-card">
          <div class="solved-title"><i class="fa-solid fa-code-compare"></i> Question 9: Assertion &amp; Reason on Frequency Distributions</div>
          <p>
            <strong>Assertion (A):</strong> In a frequency table where score 5 appears with frequency 10, the score 5 contributes 50 to the total sum.
            <br><strong>Reason (R):</strong> The weighted arithmetic mean formula is given by <span class="math-inline">x̄ = (&Sigma; f_i &middot; x_i) / (&Sigma; f_i)</span>.
          </p>
          <details class="ans-box">
            <summary>View Model Answer &amp; Explanation</summary>
            <div class="ans-content">
              <div class="step-box">
                <div class="step-num"><i class="fa-solid fa-check"></i></div>
                <div class="step-text">
                  <strong>Correct Answer: (A) Both (A) and (R) are true, and (R) is the correct explanation of (A).</strong>
                  <br>&bull; <em>Explanation:</em> The contribution of any distinct observation is its frequency times its value (<span class="math-inline">f_i &middot; x_i = 10 &times; 5 = 50</span>), as stated in the numerator of the weighted mean formula in (R).
                </div>
              </div>
            </div>
          </details>
        </div>

        <!-- A&R 5 -->
        <div class="solved-card">
          <div class="solved-title"><i class="fa-solid fa-code-compare"></i> Question 10: Assertion &amp; Reason on Line Graphs vs Column Graphs</div>
          <p>
            <strong>Assertion (A):</strong> Line graphs are preferred over clustered column graphs when tracking multi-country satellite launch data across 15 consecutive years.
            <br><strong>Reason (R):</strong> Connecting data points with line segments clearly visualizes the continuous rate of change (slope) and avoids the visual clutter of 60 separate columns.
          </p>
          <details class="ans-box">
            <summary>View Model Answer &amp; Explanation</summary>
            <div class="ans-content">
              <div class="step-box">
                <div class="step-num"><i class="fa-solid fa-check"></i></div>
                <div class="step-text">
                  <strong>Correct Answer: (A) Both (A) and (R) are true, and (R) is the correct explanation of (A).</strong>
                  <br>&bull; <em>Explanation:</em> When the number of time points multiplied by the number of categories is large (<span class="math-inline">15 &times; 4 = 60</span>), bar charts become crowded and illegible. Line graphs reveal trends and rates of change with visual elegance.
                </div>
              </div>
            </div>
          </details>
        </div>
      </div>

      <!-- ========================================================
           SUBSECTION 5C: 6 SHORT ANSWER QUESTIONS (2M / 3M)
           ======================================================== -->
      <div style="margin-bottom: 2.5rem;">
        <h3 style="font-family: 'Space Grotesk', sans-serif; font-size: 1.4rem; color: var(--primary-dark); margin-bottom: 1.25rem;">
          <i class="fa-solid fa-pen-to-square"></i> Part 5C: Short Answer Questions (2-Mark &amp; 3-Mark Topper Models)
        </h3>

        <!-- SAQ 1 -->
        <div class="solved-card">
          <div class="solved-title"><i class="fa-solid fa-feather-pointed"></i> Question 11: Correcting an Incorrectly Recorded Observation (2 Marks)</div>
          <p>
            The average of 25 numbers was found to be 78.4. Later, it was discovered that one number was misread as 96 instead of its actual value of 69. Find the correct arithmetic mean.
          </p>
          <details class="ans-box">
            <summary>View Model Solution [2M]</summary>
            <div class="ans-content">
              <div class="step-box">
                <div class="step-num">1</div>
                <div class="step-text"><strong>Given:</strong> Total observations <span class="math-inline">n = 25</span>; Incorrect mean = 78.4; Misread value = 96; True value = 69.</div>
              </div>
              <div class="step-box">
                <div class="step-num">2</div>
                <div class="step-text"><strong>Step-by-Step Calculation:</strong>
                  <br>&bull; Incorrect Total Sum = <span class="math-inline">78.4 &times; 25 = 1960</span>. [1M]
                  <br>&bull; True Total Sum = <span class="math-inline">1960 - 96 + 69 = 1960 - 27 = 1933</span>.
                  <br>&bull; Correct Mean = <span class="math-inline">1933 / 25 = 77.32</span>. [1M]
                </div>
              </div>
              <div class="step-box">
                <div class="step-num">3</div>
                <div class="step-text"><strong>Final Answer:</strong> The correct arithmetic mean is <strong>77.32</strong>.</div>
              </div>
            </div>
          </details>
        </div>

        <!-- SAQ 2 -->
        <div class="solved-card">
          <div class="solved-title"><i class="fa-solid fa-feather-pointed"></i> Question 12: Combined Mean of Two Sections (3 Marks)</div>
          <p>
            Section A of Class 8 has 30 students with an average mathematics score of 72. Section B has 20 students with an average mathematics score of 82. Calculate the combined average score of all 50 students.
          </p>
          <details class="ans-box">
            <summary>View Model Solution [3M]</summary>
            <div class="ans-content">
              <div class="step-box">
                <div class="step-num">1</div>
                <div class="step-text"><strong>Given:</strong> Section A: <span class="math-inline">n_1 = 30, x̄_1 = 72</span>; Section B: <span class="math-inline">n_2 = 20, x̄_2 = 82</span>.</div>
              </div>
              <div class="step-box">
                <div class="step-num">2</div>
                <div class="step-text"><strong>Step-by-Step Calculation:</strong>
                  <br>&bull; Total marks in Section A = <span class="math-inline">n_1 &times; x̄_1 = 30 &times; 72 = 2160</span>. [1M]
                  <br>&bull; Total marks in Section B = <span class="math-inline">n_2 &times; x̄_2 = 20 &times; 82 = 1640</span>. [1M]
                  <br>&bull; Combined Total Marks = <span class="math-inline">2160 + 1640 = 3800</span>.
                  <br>&bull; Combined Average = <span class="math-inline">3800 / (30 + 20) = 3800 / 50 = 76</span>. [1M]
                </div>
              </div>
              <div class="step-box">
                <div class="step-num">3</div>
                <div class="step-text"><strong>Final Answer:</strong> The combined average score of all 50 students is <strong>76 marks</strong>. (Notice that simply averaging 72 and 82 gives 77, which is WRONG because Section A has more students!).</div>
              </div>
            </div>
          </details>
        </div>

        <!-- SAQ 3 -->
        <div class="solved-card">
          <div class="solved-title"><i class="fa-solid fa-feather-pointed"></i> Question 13: Fulcrum Distance Balance for an Unknown Coordinate (2 Marks)</div>
          <p>
            On a number line, weights are placed at coordinates 4, 7, 10, and <span class="math-inline">k</span>. If the arithmetic mean is known to be 8, find the value of <span class="math-inline">k</span> using the balance of distances.
          </p>
          <details class="ans-box">
            <summary>View Model Solution [2M]</summary>
            <div class="ans-content">
              <div class="step-box">
                <div class="step-num">1</div>
                <div class="step-text"><strong>Given:</strong> Mean <span class="math-inline">x̄ = 8</span>. Points: 4, 7, 10, <span class="math-inline">k</span>.</div>
              </div>
              <div class="step-box">
                <div class="step-num">2</div>
                <div class="step-text"><strong>Distance Balance Method:</strong>
                  <br>&bull; Left distances from 8: Point 4 has distance <span class="math-inline">8 - 4 = 4</span>; Point 7 has distance <span class="math-inline">8 - 7 = 1</span>.
                  <br>Total Left Distance = <span class="math-inline">4 + 1 = 5</span>. [1M]
                  <br>&bull; Right distances from 8: Point 10 has distance <span class="math-inline">10 - 8 = 2</span>.
                  <br>&bull; For equilibrium: Total Left = Total Right &rArr; <span class="math-inline">5 = 2 + d_k &rArr; d_k = 3</span>.
                  <br>Since <span class="math-inline">k</span> must provide rightward torque: <span class="math-inline">k = 8 + 3 = 11</span>. [1M]
                </div>
              </div>
              <div class="step-box">
                <div class="step-num">3</div>
                <div class="step-text"><strong>Final Answer:</strong> The unknown coordinate is <strong>k = 11</strong>.</div>
              </div>
            </div>
          </details>
        </div>

        <!-- SAQ 4 -->
        <div class="solved-card">
          <div class="solved-title"><i class="fa-solid fa-feather-pointed"></i> Question 14: Difference Between Mean and Median in a Skewed Distribution (3 Marks)</div>
          <p>
            Consider the daily earnings of 5 casual laborers and their site contractor:
            <br>₹400, ₹450, ₹450, ₹500, ₹550, and ₹12,000.
            <br>(i) Calculate the arithmetic mean. (ii) Calculate the median. (iii) Which measure better represents the typical worker? Explain.
          </p>
          <details class="ans-box">
            <summary>View Model Solution [3M]</summary>
            <div class="ans-content">
              <div class="step-box">
                <div class="step-num">1</div>
                <div class="step-text"><strong>Given:</strong> Sorted values: 400, 450, 450, 500, 550, 12000. Count <span class="math-inline">n = 6</span>.</div>
              </div>
              <div class="step-box">
                <div class="step-num">2</div>
                <div class="step-text"><strong>Step-by-Step Calculations:</strong>
                  <br>&bull; <strong>(i) Mean:</strong> Sum = <span class="math-inline">400 + 450 + 450 + 500 + 550 + 12000 = 14350</span>.
                  <br>Mean = <span class="math-inline">14350 / 6 = ₹2,391.67</span>. [1M]
                  <br>&bull; <strong>(ii) Median:</strong> The two middle values are 450 and 500.
                  <br>Median = <span class="math-inline">(450 + 500) / 2 = ₹475</span>. [1M]
                  <br>&bull; <strong>(iii) Assessment:</strong> The <strong>median (₹475)</strong> is the superior representative. The contractor's ₹12,000 creates an extreme positive outlier that distorts the mean to ₹2,391.67—an amount that none of the laborers actually earns! [1M]
                </div>
              </div>
              <div class="step-box">
                <div class="step-num">3</div>
                <div class="step-text"><strong>Final Answer:</strong> Mean = <strong>₹2,391.67</strong>; Median = <strong>₹475</strong>; Median is the better measure because it is immune to the contractor's outlier.</div>
              </div>
            </div>
          </details>
        </div>

        <!-- SAQ 5 -->
        <div class="solved-card">
          <div class="solved-title"><i class="fa-solid fa-feather-pointed"></i> Question 15: Interpreting Slopes on a Time-Series Line Graph (2 Marks)</div>
          <p>
            A line graph shows the water level in an Odisha reservoir over 6 months:
            <br>June (12m), July (18m), August (26m), September (27m), October (24m), November (20m).
            <br>(i) During which one-month period did water rise the fastest?
            <br>(ii) During which period was water level practically stationary?
          </p>
          <details class="ans-box">
            <summary>View Model Solution [2M]</summary>
            <div class="ans-content">
              <div class="step-box">
                <div class="step-num">1</div>
                <div class="step-text"><strong>Core Mathematical Principle:</strong> Rate of change = <span class="math-inline">&Delta; y / &Delta; x</span>. The steeper the line segment, the faster the rate of change; a nearly horizontal line signifies stationary conditions.</div>
              </div>
              <div class="step-box">
                <div class="step-num">2</div>
                <div class="step-text"><strong>Calculations:</strong>
                  <br>&bull; June to July increase = <span class="math-inline">18 - 12 = 6 m</span>.
                  <br>&bull; July to August increase = <span class="math-inline">26 - 18 = 8 m</span>. (Steepest segment! [1M])
                  <br>&bull; August to September change = <span class="math-inline">27 - 26 = 1 m</span>. (Nearly flat/stationary! [1M])
                </div>
              </div>
              <div class="step-box">
                <div class="step-num">3</div>
                <div class="step-text"><strong>Final Answer:</strong> (i) Water rose fastest during <strong>July to August (+8m)</strong>; (ii) Water was practically stationary during <strong>August to September (+1m)</strong>.</div>
              </div>
            </div>
          </details>
        </div>

        <!-- SAQ 6 -->
        <div class="solved-card">
          <div class="solved-title"><i class="fa-solid fa-feather-pointed"></i> Question 16: Finding Missing Frequency in a Distribution (3 Marks)</div>
          <p>
            The mean of the following discrete frequency distribution is <strong>15</strong>. Find the missing frequency <span class="math-inline">f</span>:
            <br>Value (<span class="math-inline">x</span>): 5, 10, 15, 20, 25
            <br>Frequency (<span class="math-inline">f</span>): 6, <span class="math-inline">f</span>, 6, 10, 5
          </p>
          <details class="ans-box">
            <summary>View Model Solution [3M]</summary>
            <div class="ans-content">
              <div class="step-box">
                <div class="step-num">1</div>
                <div class="step-text"><strong>Given:</strong> Values <span class="math-inline">x_i</span> and frequencies <span class="math-inline">f_i</span>. Given mean <span class="math-inline">x̄ = 15</span>.</div>
              </div>
              <div class="step-box">
                <div class="step-num">2</div>
                <div class="step-text"><strong>Step-by-Step Calculation:</strong>
                  <br>&bull; Sum of frequencies <span class="math-inline">N = 6 + f + 6 + 10 + 5 = 27 + f</span>. [1M]
                  <br>&bull; Sum of products <span class="math-inline">&Sigma; f &middot; x = (5 &times; 6) + (10 &times; f) + (15 &times; 6) + (20 &times; 10) + (25 &times; 5)</span>
                  <br><span class="math-inline">&Sigma; f &middot; x = 30 + 10f + 90 + 200 + 125 = 445 + 10f</span>. [1M]
                  <br>&bull; Equate to Mean formula:
                  <br><span class="math-inline">(445 + 10f) / (27 + f) = 15</span>
                  <br><span class="math-inline">445 + 10f = 15(27 + f) = 405 + 15f</span>
                  <br><span class="math-inline">445 - 405 = 15f - 10f</span>
                  <br><span class="math-inline">40 = 5f &rArr; f = 8</span>. [1M]
                </div>
              </div>
              <div class="step-box">
                <div class="step-num">3</div>
                <div class="step-text"><strong>Final Answer:</strong> The missing frequency is <strong>f = 8</strong>.</div>
              </div>
            </div>
          </details>
        </div>
      </div>
    </section>
"""
