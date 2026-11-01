# -*- coding: utf-8 -*-
"""
Section 5 Part 2 Module: LAQs (5M), Case Studies & PYQs
Class 8 Mathematics Chapter 12: Tales by Dots and Lines (NCERT NEP code: hegp112)
"""

def get_section_5_part2():
    return """
    <!-- SECTION 5: COMPLETE EXAM QUESTION BANK (PART 2) -->
    <section id="section5b" class="section-box">
      <div class="section-header">
        <div class="section-header-left">
          <span class="section-tag">Exam Hall Readiness • Long Answers &amp; Cases</span>
          <h2 class="section-title">§ 5. Complete Exam Question Bank (Part 2: 5M LAQs, Case Studies &amp; PYQs)</h2>
          <p class="section-desc">
            Mastering 5-mark structured Long Answer Questions with step-by-step marking schemes, 2 competency-based real-world case studies, and 5 previous years' / most probable board exam questions.
          </p>
        </div>
        <div>
          <span class="badge badge-emerald"><i class="fa-solid fa-award"></i> 5M &amp; Cases</span>
        </div>
      </div>

      <!-- ========================================================
           SUBSECTION 5D: 4 LONG ANSWER QUESTIONS (5 MARKS EACH)
           ======================================================== -->
      <div style="margin-bottom: 2.5rem;">
        <h3 style="font-family: 'Space Grotesk', sans-serif; font-size: 1.4rem; color: var(--primary-dark); margin-bottom: 1.25rem;">
          <i class="fa-solid fa-file-signature"></i> Part 5D: Long Answer Questions (5 Marks with Step Marking Schemes)
        </h3>

        <!-- LAQ 1 -->
        <div class="solved-card">
          <div class="solved-title"><i class="fa-solid fa-certificate"></i> Question 17: Rigorous Algebraic Proofs of Shifting &amp; Scaling Theorems (5 Marks)</div>
          <p>
            (a) State and prove algebraically the <strong>Linear Shifting Invariant Theorem</strong> for the arithmetic mean of <span class="math-inline">n</span> observations. [2 Marks]
            <br>(b) State and prove algebraically the <strong>Uniform Scaling Theorem</strong> for the arithmetic mean. [2 Marks]
            <br>(c) A teacher computed the mean mark of 35 students as 42. Later, every student's score was increased by 5 marks for neatness and then scaled up by 10% (<span class="math-inline">&times; 1.1</span>) for school moderation. Find the final moderated class average. [1 Mark]
          </p>
          <details class="ans-box">
            <summary>View Complete 5-Mark Solution &amp; Marking Scheme</summary>
            <div class="ans-content">
              <div class="step-box">
                <div class="step-num">1</div>
                <div class="step-text">
                  <strong>(a) Proof of Linear Shifting Theorem [2 Marks]:</strong>
                  <br>&bull; <em>Statement:</em> If a constant <span class="math-inline">c</span> is added to every observation in a collection, the new mean increases by <span class="math-inline">c</span>. [0.5M]
                  <br>&bull; <em>Algebraic Proof:</em> Let the original values be <span class="math-inline">x_1, x_2, ..., x_n</span> with mean <span class="math-inline">x̄ = (&Sigma; x_i) / (n)</span>.
                  <br>New values are <span class="math-inline">x'_i = x_i + c</span>.
                  <br><span class="math-inline">x̄' = ((x_1 + c) + (x_2 + c) + ... + (x_n + c)) / (n)</span>
                  <br><span class="math-inline">x̄' = ((x_1 + x_2 + ... + x_n) + n&middot; c) / (n)</span> [0.5M]
                  <br><span class="math-inline">x̄' = (&Sigma; x_i) / (n) + (n&middot; c) / (n) = x̄ + c</span>. [1M] (Q.E.D.)
                </div>
              </div>
              <div class="step-box">
                <div class="step-num">2</div>
                <div class="step-text">
                  <strong>(b) Proof of Uniform Scaling Theorem [2 Marks]:</strong>
                  <br>&bull; <em>Statement:</em> If every observation is multiplied by a constant <span class="math-inline">k</span>, the new mean is <span class="math-inline">k &middot; x̄</span>. [0.5M]
                  <br>&bull; <em>Algebraic Proof:</em> New values are <span class="math-inline">x'_i = k&middot; x_i</span>.
                  <br><span class="math-inline">x̄' = (k&middot; x_1 + k&middot; x_2 + ... + k&middot; x_n) / (n)</span>
                  <br>By the Distributive Law of algebra:
                  <br><span class="math-inline">x̄' = (k &middot; (x_1 + x_2 + ... + x_n)) / (n) = k &middot; &le;ft((&Sigma; x_i) / (n)) = k &middot; x̄</span>. [1.5M] (Q.E.D.)
                </div>
              </div>
              <div class="step-box">
                <div class="step-num">3</div>
                <div class="step-text">
                  <strong>(c) Numerical Application [1 Mark]:</strong>
                  <br>Initial mean <span class="math-inline">x̄ = 42</span>.
                  <br>Step 1 (Shift +5): <span class="math-inline">x̄_1 = 42 + 5 = 47</span>.
                  <br>Step 2 (Scale &times; 1.1): <span class="math-inline">x̄_2 = 47 &times; 1.1 = 51.7</span>. [1M]
                  <br><strong>Final Moderated Class Average = 51.7 marks</strong>.
                </div>
              </div>
            </div>
          </details>
        </div>

        <!-- LAQ 2 -->
        <div class="solved-card">
          <div class="solved-title"><i class="fa-solid fa-certificate"></i> Question 18: Full Grouped Frequency Distribution Analysis (5 Marks)</div>
          <p>
            The table below gives the weekly pocket money (in ₹) of 50 Grade 8 students:
            <br>Pocket Money (<span class="math-inline">x</span>): 50, 60, 70, 80, 90, 100
            <br>No. of Students (<span class="math-inline">f</span>): 6, 12, 14, 10, 5, 3
            <br>(i) Construct the complete calculation table showing <span class="math-inline">f_i &middot; x_i</span> and cumulative frequencies (<span class="math-inline">cf</span>). [1 Mark]
            <br>(ii) Calculate the weighted arithmetic mean pocket money. [1.5 Marks]
            <br>(iii) Determine the median pocket money using the cumulative frequency column. [1.5 Marks]
            <br>(iv) Identify the modal pocket money and compare it with the mean and median. [1 Mark]
          </p>
          <details class="ans-box">
            <summary>View Complete 5-Mark Solution &amp; Marking Scheme</summary>
            <div class="ans-content">
              <div class="step-box">
                <div class="step-num">1</div>
                <div class="step-text">
                  <strong>(i) Structured Calculation Table [1 Mark]:</strong>
                  <div class="table-container">
                    <table>
                      <thead>
                        <tr>
                          <th>Pocket Money (x)</th>
                          <th>Frequency (f)</th>
                          <th>f &times; x</th>
                          <th>Cumulative Frequency (cf)</th>
                        </tr>
                      </thead>
                      <tbody>
                        <tr><td>50</td><td>6</td><td>300</td><td>6</td></tr>
                        <tr><td>60</td><td>12</td><td>720</td><td>18</td></tr>
                        <tr><td>70</td><td>14</td><td>980</td><td>32</td></tr>
                        <tr><td>80</td><td>10</td><td>800</td><td>42</td></tr>
                        <tr><td>90</td><td>5</td><td>450</td><td>47</td></tr>
                        <tr><td>100</td><td>3</td><td>300</td><td>50</td></tr>
                        <tr>
                          <td><strong>Total</strong></td>
                          <td><strong>&Sigma;f = 50</strong></td>
                          <td><strong>&Sigma;fx = 3550</strong></td>
                          <td>-</td>
                        </tr>
                      </tbody>
                    </table>
                  </div>
                </div>
              </div>
              <div class="step-box">
                <div class="step-num">2</div>
                <div class="step-text">
                  <strong>(ii) Weighted Arithmetic Mean [1.5 Marks]:</strong>
                  <br><span class="math-inline">x̄ = (&Sigma; f_i &middot; x_i) / (&Sigma; f_i) = (3550) / (50)</span> [1M]
                  <br><span class="math-inline">x̄ = <strong>₹71.00</strong></span>. [0.5M]
                </div>
              </div>
              <div class="step-box">
                <div class="step-num">3</div>
                <div class="step-text">
                  <strong>(iii) Median Determination [1.5 Marks]:</strong>
                  <br>Total count <span class="math-inline">N = 50</span> (even).
                  <br>Median positions = <span class="math-inline">N/2 = 25th</span> and <span class="math-inline">(N/2 + 1) = 26th</span> values. [0.5M]
                  <br>Looking at the <span class="math-inline">cf</span> column:
                  <br>Up to ₹60, <span class="math-inline">cf = 18</span> (covers positions 1 to 18).
                  <br>Up to ₹70, <span class="math-inline">cf = 32</span> (covers positions 19 to 32).
                  <br>Both the 25th and 26th values fall into the class <span class="math-inline">x = 70</span>! [0.5M]
                  <br><span class="math-inline">Median = (70 + 70) / (2) = <strong>₹70.00</strong></span>. [0.5M]
                </div>
              </div>
              <div class="step-box">
                <div class="step-num">4</div>
                <div class="step-text">
                  <strong>(iv) Mode &amp; Comparison [1 Mark]:</strong>
                  <br>The highest frequency is 14, corresponding to <strong>Mode = ₹70</strong>. [0.5M]
                  <br><em>Comparison:</em> Mean (₹71) &approx; Median (₹70) = Mode (₹70). The distribution is nearly symmetric with a slight positive skewness towards ₹90 and ₹100. [0.5M]
                </div>
              </div>
            </div>
          </details>
        </div>

        <!-- LAQ 3 -->
        <div class="solved-card">
          <div class="solved-title"><i class="fa-solid fa-certificate"></i> Question 19: Climate Line Graph Construction &amp; Scientific Interpretation (5 Marks)</div>
          <p>
            Monthly rainfall in mm for Cuttack (Odisha) and Jodhpur (Rajasthan) is recorded below:
            <br>Months: Jan, Mar, May, Jul, Aug, Oct, Dec
            <br>Cuttack: 10, 25, 80, 320, 360, 160, 5
            <br>Jodhpur: 3, 4, 10, 120, 110, 8, 2
            <br>(a) Visualise this data by drawing/describing a dual-line graph with axes, units, and scales. [2 Marks]
            <br>(b) Calculate the rate of rainfall surge (in mm/month) from May to July for both cities. [1.5 Marks]
            <br>(c) Explain the climatological and geographic reasons for the vast difference in rainfall between Cuttack and Jodhpur during July–August. [1.5 Marks]
          </p>
          <details class="ans-box">
            <summary>View Complete 5-Mark Solution &amp; Marking Scheme</summary>
            <div class="ans-content">
              <div class="step-box">
                <div class="step-num">1</div>
                <div class="step-text">
                  <strong>(a) Graph Specification &amp; Axes [2 Marks]:</strong>
                  <br>&bull; <em>Horizontal X-axis:</em> Chronological calendar months (Jan, Mar, May, Jul, Aug, Oct, Dec). [0.5M]
                  <br>&bull; <em>Vertical Y-axis:</em> Rainfall in millimeters (Scale: 0 to 400 mm, 50 mm grid intervals). [0.5M]
                  <br>&bull; <em>Line Profiles:</em> Cuttack plotted with an intense high-amplitude blue line peaking at 360 mm in August; Jodhpur plotted with an arid brown line staying below 15 mm for 10 months and peaking modestly at 120 mm in July. [1M]
                </div>
              </div>
              <div class="step-box">
                <div class="step-num">2</div>
                <div class="step-text">
                  <strong>(b) Rate of Rainfall Surge (May to July) [1.5 Marks]:</strong>
                  <br>Time duration = 2 months (May to July).
                  <br>&bull; <em>Cuttack Surge:</em> <span class="math-inline">&Delta; y = 320 - 80 = 240  mm</span>.
                  <br>Rate of increase = <span class="math-inline">240  mm / 2  months = <strong>120  mm/month</strong></span>. [0.75M]
                  <br>&bull; <em>Jodhpur Surge:</em> <span class="math-inline">&Delta; y = 120 - 10 = 110  mm</span>.
                  <br>Rate of increase = <span class="math-inline">110  mm / 2  months = <strong>55  mm/month</strong></span>. [0.75M]
                  <br>Cuttack's monsoon surge is more than twice as steep!
                </div>
              </div>
              <div class="step-box">
                <div class="step-num">3</div>
                <div class="step-text">
                  <strong>(c) Geographic &amp; Climatological Explanation [1.5 Marks]:</strong>
                  <br>&bull; <strong>Cuttack (Odisha):</strong> Located in coastal eastern India along the Bay of Bengal branch of the Southwest Monsoon. Warm, moisture-laden maritime depressions regularly strike the Odisha coast, generating torrential rainfall (360 mm peak). [0.75M]
                  <br>&bull; <strong>Jodhpur (Rajasthan):</strong> Located in western India on the leeward side of the Aravalli range in the Thar Desert. Monsoon winds run parallel to the Aravallis without relief lifting, leaving Jodhpur arid with only brief sporadic showers. [0.75M]
                </div>
              </div>
            </div>
          </details>
        </div>

        <!-- LAQ 4 -->
        <div class="solved-card">
          <div class="solved-title"><i class="fa-solid fa-certificate"></i> Question 20: Reverse-Engineering Datasets from Central Tendencies (5 Marks)</div>
          <p>
            Construct an ordered dataset of <strong>7 distinct positive integers</strong> that satisfies ALL of the following statistical conditions simultaneously:
            <br>1. Arithmetic Mean = <strong>15</strong>
            <br>2. Median = <strong>14</strong>
            <br>3. Minimum value = <strong>4</strong>
            <br>4. Range (Max - Min) = <strong>24</strong>
            <br>5. Exactly two values are multiples of 5
            <br>Show your complete algebraic reasoning and verify each property step-by-step. [5 Marks]
          </p>
          <details class="ans-box">
            <summary>View Complete 5-Mark Solution &amp; Marking Scheme</summary>
            <div class="ans-content">
              <div class="step-box">
                <div class="step-num">1</div>
                <div class="step-text">
                  <strong>Step 1: Establishing Boundary Values [1 Mark]:</strong>
                  <br>Let the 7 ordered numbers be <span class="math-inline">x_1 &lt; x_2 &lt; x_3 &lt; x_4 &lt; x_5 &lt; x_6 &lt; x_7</span>.
                  <br>&bull; Minimum = <span class="math-inline">x_1 = 4</span>. [0.5M]
                  <br>&bull; Range = <span class="math-inline">x_7 - x_1 = 24 &rArr; x_7 = 4 + 24 = 28</span>. [0.5M]
                </div>
              </div>
              <div class="step-box">
                <div class="step-num">2</div>
                <div class="step-text">
                  <strong>Step 2: Fixing the Median [1 Mark]:</strong>
                  <br>For <span class="math-inline">N = 7</span> (odd), the median is the 4th value: <span class="math-inline">x_4 = 14</span>. [1M]
                  <br>Now our dataset structure is: <span class="math-inline">[4, x_2, x_3, 14, x_5, x_6, 28]</span>.
                </div>
              </div>
              <div class="step-box">
                <div class="step-num">3</div>
                <div class="step-text">
                  <strong>Step 3: Calculating Required Sum of Remaining Values [1.5 Marks]:</strong>
                  <br>Total required sum = <span class="math-inline">7 &times; 15 = 105</span>. [0.5M]
                  <br>Known values sum = <span class="math-inline">4 + 14 + 28 = 46</span>.
                  <br>Remaining sum for <span class="math-inline">(x_2 + x_3 + x_5 + x_6) = 105 - 46 = 59</span>. [1M]
                </div>
              </div>
              <div class="step-box">
                <div class="step-num">4</div>
                <div class="step-text">
                  <strong>Step 4: Choosing Distinct Values &amp; Multiples of 5 [1.5 Marks]:</strong>
                  <br>&bull; We require <span class="math-inline">4 &lt; x_2 &lt; x_3 &lt; 14</span> and <span class="math-inline">14 &lt; x_5 &lt; x_6 &lt; 28</span>.
                  <br>&bull; Exactly two numbers must be multiples of 5.
                  <br>Let us choose <strong>10</strong> (which lies between 4 and 14) and <strong>20</strong> (which lies between 14 and 28).
                  <br>Let <span class="math-inline">x_3 = 10</span>. Then <span class="math-inline">x_2</span> can be <strong>6</strong>. (Left sum = <span class="math-inline">6 + 10 = 16</span>).
                  <br>Then remaining sum for <span class="math-inline">x_5 + x_6 = 59 - 16 = 43</span>.
                  <br>Let <span class="math-inline">x_5 = 20</span> (multiple of 5). Then <span class="math-inline">x_6 = 43 - 20 = 23</span>! [1M]
                  <br>&bull; Check ordering: <span class="math-inline">4 &lt; 6 &lt; 10 &lt; 14 &lt; 20 &lt; 23 &lt; 28</span>. All 7 numbers are strictly distinct positive integers! [0.5M]
                </div>
              </div>
              <div class="step-box">
                <div class="step-num">5</div>
                <div class="step-text">
                  <strong>Verification of All 5 Conditions:</strong>
                  <br>1. Mean: <span class="math-inline">(4 + 6 + 10 + 14 + 20 + 23 + 28)/7 = 105/7 = 15</span>. &check;
                  <br>2. Median: 4th value = 14. &check;
                  <br>3. Minimum = 4. &check;
                  <br>4. Range = <span class="math-inline">28 - 4 = 24</span>. &check;
                  <br>5. Multiples of 5: {10, 20} (exactly two). &check;
                  <br><strong>Constructed Dataset: {4, 6, 10, 14, 20, 23, 28}</strong>.
                </div>
              </div>
            </div>
          </details>
        </div>
      </div>

      <!-- ========================================================
           SUBSECTION 5E: 2 COMPETENCY-BASED CASE STUDIES
           ======================================================== -->
      <div style="margin-bottom: 2.5rem;">
        <h3 style="font-family: 'Space Grotesk', sans-serif; font-size: 1.4rem; color: var(--primary-dark); margin-bottom: 1.25rem;">
          <i class="fa-solid fa-briefcase"></i> Part 5E: Competency-Based Real-World Case Studies
        </h3>

        <!-- Case Study 1 -->
        <div class="solved-card">
          <div class="solved-title"><i class="fa-solid fa-car-battery"></i> Case Study 1: Smart City Electric Bus Fleet &amp; Charging Station Analytics</div>
          <p>
            Bhubaneswar Smart City operates a fleet of electric buses. The charging duration (in minutes) for 8 buses on Monday morning was recorded as:
            <br><span class="math-block" style="text-align:center;"><strong>45, 50, 52, 55, 58, 60, 62, 98</strong></span>
            A smart charging management dashboard tracks battery diagnostics, charging durations, and energy grid stability.
          </p>
          <div style="margin-top: 1rem;">
            <strong>Answer the following questions:</strong>
            <br><strong>Q1.1:</strong> Calculate the arithmetic mean charging duration of the 8 buses.
            <br><strong>Q1.2:</strong> Determine the median charging duration of the fleet.
            <br><strong>Q1.3:</strong> Identify the outlier in this dataset. Explain how the outlier influences the mean versus the median.
            <br><strong>Q1.4:</strong> If next week a software update reduces charging time by exactly 5 minutes for all buses, what will be the new mean and median?
          </div>
          <details class="ans-box" style="margin-top: 1rem;">
            <summary>View Complete Solutions for Case Study 1</summary>
            <div class="ans-content">
              <div class="step-box">
                <div class="step-num">1</div>
                <div class="step-text">
                  <strong>Solution 1.1 (Mean Charging Duration):</strong>
                  <br>Sum = <span class="math-inline">45 + 50 + 52 + 55 + 58 + 60 + 62 + 98 = 480  minutes</span>.
                  <br><span class="math-inline">Mean = 480 / 8 = <strong>60.0  minutes</strong></span>.
                </div>
              </div>
              <div class="step-box">
                <div class="step-num">2</div>
                <div class="step-text">
                  <strong>Solution 1.2 (Median Charging Duration):</strong>
                  <br><span class="math-inline">N = 8</span> (even). Middle values are 4th (55 min) and 5th (58 min).
                  <br><span class="math-inline">Median = (55 + 58) / 2 = 113 / 2 = <strong>56.5  minutes</strong></span>.
                </div>
              </div>
              <div class="step-box">
                <div class="step-num">3</div>
                <div class="step-text">
                  <strong>Solution 1.3 (Outlier Analysis):</strong>
                  <br>The outlier is <strong>98 minutes</strong> (perhaps a bus undergoing deep balancing or cell calibration).
                  <br>Without 98: Sum of 7 buses = 382 &rArr; Mean = <span class="math-inline">382 / 7 &approx; 54.57  min</span>.
                  <br>The single outlier inflated the mean from ~54.6 to 60.0 minutes (+5.4 min increase!). However, the median only shifted from 55 min to 56.5 min (+1.5 min). This proves the median is far more resilient to operational anomalies.
                </div>
              </div>
              <div class="step-box">
                <div class="step-num">4</div>
                <div class="step-text">
                  <strong>Solution 1.4 (Uniform Shifting by -5 min):</strong>
                  <br>By the Linear Shifting Theorem, subtracting 5 from every value reduces both the mean and the median by exactly 5 minutes:
                  <br>&bull; <strong>New Mean = 60.0 - 5 = 55.0 minutes</strong>.
                  <br>&bull; <strong>New Median = 56.5 - 5 = 51.5 minutes</strong>.
                </div>
              </div>
            </div>
          </details>
        </div>

        <!-- Case Study 2 -->
        <div class="solved-card">
          <div class="solved-title"><i class="fa-solid fa-cloud-showers-heavy"></i> Case Study 2: Odisha Coastal Cyclone Warning &amp; Precipitation Monitoring</div>
          <p>
            During severe cyclonic storm 'Dana', the Odisha Special Relief Commissioner (SRC) monitored 24-hour rainfall (in cm) across 10 coastal administrative blocks:
            <br>Blocks: Puri, Konark, Astaranga, Paradip, Kujang, Ersama, Chandbali, Rajnagar, Dhamra, Basudevpur
            <br>Rainfall (cm): 18, 22, 25, 30, 28, 34, 26, 24, 32, 21
          </p>
          <div style="margin-top: 1rem;">
            <strong>Answer the following questions:</strong>
            <br><strong>Q2.1:</strong> Find the mean 24-hour rainfall across these 10 coastal blocks.
            <br><strong>Q2.2:</strong> Arrange the data in ascending order and determine the median rainfall.
            <br><strong>Q2.3:</strong> Verify the physical balance of distances: prove that total deviations to the left of the mean equal total deviations to the right.
            <br><strong>Q2.4:</strong> Any block recording rainfall more than 2 cm above the mean requires immediate National Disaster Response Force (NDRF) deployment. Which blocks qualify?
          </div>
          <details class="ans-box" style="margin-top: 1rem;">
            <summary>View Complete Solutions for Case Study 2</summary>
            <div class="ans-content">
              <div class="step-box">
                <div class="step-num">1</div>
                <div class="step-text">
                  <strong>Solution 2.1 (Mean Rainfall):</strong>
                  <br>Sum = <span class="math-inline">18 + 22 + 25 + 30 + 28 + 34 + 26 + 24 + 32 + 21 = 260  cm</span>.
                  <br><span class="math-inline">Mean = 260 / 10 = <strong>26.0  cm</strong></span>.
                </div>
              </div>
              <div class="step-box">
                <div class="step-num">2</div>
                <div class="step-text">
                  <strong>Solution 2.2 (Median Rainfall):</strong>
                  <br>Sorted list: 18, 21, 22, 24, <strong>25, 26</strong>, 28, 30, 32, 34.
                  <br>Middle values are 5th (25 cm) and 6th (26 cm).
                  <br><span class="math-inline">Median = (25 + 26) / 2 = <strong>25.5  cm</strong></span>.
                </div>
              </div>
              <div class="step-box">
                <div class="step-num">3</div>
                <div class="step-text">
                  <strong>Solution 2.3 (Distance Balance Verification):</strong>
                  <br>&bull; <em>Leftward distances from 26:</em>
                  <br>(26 - 18) = 8; (26 - 21) = 5; (26 - 22) = 4; (26 - 24) = 2; (26 - 25) = 1.
                  <br>Total LHS Distance = <span class="math-inline">8 + 5 + 4 + 2 + 1 = <strong>20  cm</strong></span>.
                  <br>&bull; <em>Rightward distances from 26:</em>
                  <br>(26 - 26) = 0; (28 - 26) = 2; (30 - 26) = 4; (32 - 26) = 6; (34 - 26) = 8.
                  <br>Total RHS Distance = <span class="math-inline">0 + 2 + 4 + 6 + 8 = <strong>20  cm</strong></span>.
                  <br>Since Total LHS (20) = Total RHS (20), the fulcrum condition is rigorously proven!
                </div>
              </div>
              <div class="step-box">
                <div class="step-num">4</div>
                <div class="step-text">
                  <strong>Solution 2.4 (NDRF Deployment Criterion):</strong>
                  <br>Threshold = <span class="math-inline">Mean + 2  cm = 26 + 2 = 28  cm</span>.
                  <br>Blocks with rainfall strictly greater than 28 cm:
                  <br>1. <strong>Paradip (30 cm)</strong>
                  <br>2. <strong>Dhamra (32 cm)</strong>
                  <br>3. <strong>Ersama (34 cm)</strong>
                  <br>These 3 high-impact coastal blocks qualify for urgent NDRF deployment.
                </div>
              </div>
            </div>
          </details>
        </div>
      </div>

      <!-- ========================================================
           SUBSECTION 5F: 5 PREVIOUS YEARS & MOST PROBABLE QUESTIONS
           ======================================================== -->
      <div style="margin-bottom: 2.5rem;">
        <h3 style="font-family: 'Space Grotesk', sans-serif; font-size: 1.4rem; color: var(--primary-dark); margin-bottom: 1.25rem;">
          <i class="fa-solid fa-clock-rotate-left"></i> Part 5F: Previous Years' Questions (PYQs) &amp; Probable Board Questions
        </h3>

        <!-- PYQ 1 -->
        <div class="solved-card">
          <div class="solved-title"><i class="fa-solid fa-star"></i> PYQ 1: Sum and Mean of First n Odd Natural Numbers</div>
          <p>
            Prove that the arithmetic mean of the first <span class="math-inline">n</span> odd natural numbers is always identically equal to <span class="math-inline">n</span>. Hence, find the mean of the first 125 odd natural numbers.
          </p>
          <details class="ans-box">
            <summary>View Complete Model Solution</summary>
            <div class="ans-content">
              <div class="step-box">
                <div class="step-num">1</div>
                <div class="step-text"><strong>Given:</strong> First <span class="math-inline">n</span> odd natural numbers: <span class="math-inline">1, 3, 5, 7, ..., (2n - 1)</span>.</div>
              </div>
              <div class="step-box">
                <div class="step-num">2</div>
                <div class="step-text"><strong>Algebraic Proof:</strong>
                  <br>The sequence is an AP with <span class="math-inline">a = 1</span>, common difference <span class="math-inline">d = 2</span>, and last term <span class="math-inline">l = 2n - 1</span>.
                  <br>Sum of an AP = <span class="math-inline">S_n = (n) / (2)[a + l] = (n) / (2)[1 + (2n - 1)] = (n) / (2)[2n] = n^2</span>.
                  <br>Arithmetic Mean = <span class="math-inline">(S_n) / (n) = (n^2) / (n) = <strong>n</strong></span>. (Q.E.D.)
                </div>
              </div>
              <div class="step-box">
                <div class="step-num">3</div>
                <div class="step-text"><strong>Application:</strong> For <span class="math-inline">n = 125</span>, the mean of the first 125 odd natural numbers is simply <strong>125</strong>.</div>
              </div>
            </div>
          </details>
        </div>

        <!-- PYQ 2 -->
        <div class="solved-card">
          <div class="solved-title"><i class="fa-solid fa-star"></i> PYQ 2: Correcting Multiple Entry Errors</div>
          <p>
            The mean of 50 numbers was 38. Later, it was detected that two numbers were wrongly recorded as 46 and 28 instead of their true values 64 and 82. Calculate the correct arithmetic mean.
          </p>
          <details class="ans-box">
            <summary>View Complete Model Solution</summary>
            <div class="ans-content">
              <div class="step-box">
                <div class="step-num">1</div>
                <div class="step-text">
                  <strong>Calculations:</strong>
                  <br>&bull; Initial Sum = <span class="math-inline">50 &times; 38 = 1900</span>.
                  <br>&bull; Wrong numbers sum = <span class="math-inline">46 + 28 = 74</span>.
                  <br>&bull; Correct numbers sum = <span class="math-inline">64 + 82 = 146</span>.
                  <br>&bull; Corrected Total Sum = <span class="math-inline">1900 - 74 + 146 = 1900 + 72 = 1972</span>.
                  <br>&bull; Correct Mean = <span class="math-inline">1972 / 50 = <strong>39.44</strong></span>.
                </div>
              </div>
            </div>
          </details>
        </div>

        <!-- PYQ 3 -->
        <div class="solved-card">
          <div class="solved-title"><i class="fa-solid fa-star"></i> PYQ 3: Finding Two Missing Symmetric Values on a Dot Plot</div>
          <p>
            A dot plot has mean 20. Six known values are 12, 15, 18, 22, 25, 26. Two values <span class="math-inline">a</span> and <span class="math-inline">b</span> are missing. If <span class="math-inline">a &lt; 20</span>, <span class="math-inline">b &gt; 20</span>, and <span class="math-inline">b - a = 12</span>, find <span class="math-inline">a</span> and <span class="math-inline">b</span>.
          </p>
          <details class="ans-box">
            <summary>View Complete Model Solution</summary>
            <div class="ans-content">
              <div class="step-box">
                <div class="step-num">1</div>
                <div class="step-text">
                  <strong>Step-by-Step Solution:</strong>
                  <br>&bull; Total count <span class="math-inline">n = 8</span>. Total required sum = <span class="math-inline">8 &times; 20 = 160</span>.
                  <br>&bull; Sum of 6 known numbers = <span class="math-inline">12 + 15 + 18 + 22 + 25 + 26 = 118</span>.
                  <br>&bull; Therefore, <span class="math-inline">a + b = 160 - 118 = 42</span>.
                  <br>&bull; We are given <span class="math-inline">b - a = 12</span>.
                  <br>&bull; Adding equations: <span class="math-inline">2b = 54 &rArr; b = 27</span>.
                  <br>&bull; Subtracting: <span class="math-inline">a = 42 - 27 = 15</span>.
                  <br><strong>Values: a = 15 and b = 27</strong>.
                </div>
              </div>
            </div>
          </details>
        </div>

        <!-- PYQ 4 -->
        <div class="solved-card">
          <div class="solved-title"><i class="fa-solid fa-star"></i> PYQ 4: The Truncated Axis Illusion in Business Charts</div>
          <p>
            A company advertisement displays a line graph where sales appear to skyrocket by 400% from 2023 to 2024. Upon inspection, the Y-axis starts at 980 instead of 0. Sales in 2023 were 990 units and in 2024 were 1030 units.
            <br>(i) What is the actual percentage increase in sales?
            <br>(ii) Why did the company truncate the axis? Explain the visual deception.
          </p>
          <details class="ans-box">
            <summary>View Complete Model Solution</summary>
            <div class="ans-content">
              <div class="step-box">
                <div class="step-num">1</div>
                <div class="step-text">
                  <strong>Analysis &amp; Calculations:</strong>
                  <br>&bull; (i) Actual Increase = <span class="math-inline">1030 - 990 = 40  units</span>.
                  <br>Actual Percentage Increase = <span class="math-inline">(40 / 990) &times; 100% &approx; <strong>4.04%</strong></span>!
                  <br>&bull; (ii) The company truncated the baseline at 980 so that 990 was plotted at height <span class="math-inline">990 - 980 = 10</span>, while 1030 was plotted at height <span class="math-inline">1030 - 980 = 50</span>. On paper, the bar or dot height was 5 times taller (<span class="math-inline">50 / 10 = 5</span>), misleading viewers into believing sales grew by 400% when real sales grew by only 4%!
                </div>
              </div>
            </div>
          </details>
        </div>

        <!-- PYQ 5 -->
        <div class="solved-card">
          <div class="solved-title"><i class="fa-solid fa-star"></i> PYQ 5: Spreadsheet Weighted Grade Model Design</div>
          <p>
            In a continuous assessment scheme, Internal Assessment has weight 20% (0.2), Practicals have weight 30% (0.3), and Term End Exam has weight 50% (0.5).
            <br>For student Priya, these scores are stored in cells B4, C4, and D4 respectively. Write the spreadsheet formula to compute her final weighted score.
          </p>
          <details class="ans-box">
            <summary>View Complete Model Solution</summary>
            <div class="ans-content">
              <div class="step-box">
                <div class="step-num">1</div>
                <div class="step-text">
                  <strong>Spreadsheet Formula:</strong>
                  <div class="math-block">=(B4*0.2) + (C4*0.3) + (D4*0.5)</div>
                  <br><em>Or using SUMPRODUCT if weights are in row 2 (B2:D2):</em>
                  <div class="math-block">=SUMPRODUCT(B4:D4, B2:D2)</div>
                </div>
              </div>
            </div>
          </details>
        </div>
      </div>
    </section>
"""
