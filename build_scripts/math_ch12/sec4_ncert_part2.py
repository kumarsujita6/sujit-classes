# -*- coding: utf-8 -*-
"""
Section 4 Part 2 Module: Figure it Out 2 & Figure it Out 3 (Back Exercises)
Class 8 Mathematics Chapter 12: Tales by Dots and Lines (NCERT NEP code: hegp112)
"""

def get_section_4_part2():
    return """
    <!-- SECTION 4: 100% SOLVED NCERT QUESTIONS (PART 2) -->
    <section id="section4b" class="section-box">
      <div class="section-header">
        <div class="section-header-left">
          <span class="section-tag">Textbook Mastery • Zero-Omission</span>
          <h2 class="section-title">§ 4. 100% Solved NCERT Questions (Part 2: Figure it Out 2 &amp; End Exercises)</h2>
          <p class="section-desc">
            Complete, rigorous step-by-step solutions for Figure it Out 2 (Line Graphs &amp; Infographics) and Figure it Out 3 (All 15 Back Exercises + Game of Hex) from Book Pages 122 to 134 in 5-step presentation format.
          </p>
        </div>
        <div>
          <span class="badge badge-emerald"><i class="fa-solid fa-check-double"></i> FIO 2 + FIO 3 Solved</span>
        </div>
      </div>

      <!-- ========================================================
           SUBSECTION 4C: FIGURE IT OUT 2 (BOOK PAGES 122-124)
           ======================================================== -->
      <div style="margin-bottom: 2.5rem;">
        <h3 style="font-family: 'Space Grotesk', sans-serif; font-size: 1.4rem; color: var(--primary-dark); margin-bottom: 1.25rem;">
          <i class="fa-solid fa-chart-line"></i> Part 4C: Complete Solutions to 'Figure it Out 2' (Line Graphs &amp; Infographics)
        </h3>

        <!-- FIO 2 Q1 -->
        <div class="solved-card">
          <div class="solved-title"><i class="fa-solid fa-calculator"></i> Question 1: Shop Customers Visiting vs Purchasing Line Graph (Book p. 122)</div>
          <p>
            The average number of customers visiting a shop and purchasing items over different days of the week is given:
            <br>Days: Mon, Tue, Wed, Thu, Fri, Sat, Sun
            <br>Visiting: 16, 19, 10, 14, 20, 22, 35
            <br>Purchasing: 10, 8, 7, 11, 12, 16, 26
            <br>Visualise this data on a dual-line graph and share key interpretations.
          </p>
          <details class="ans-box">
            <summary>View 5-Step Solution</summary>
            <div class="ans-content">
              <div class="step-box">
                <div class="step-num">1</div>
                <div class="step-text"><strong>Given Information &amp; Context:</strong> Paired time-series data for a 7-day week measuring two related variables: footfall (visitors) and conversions (purchasers).</div>
              </div>
              <div class="step-box">
                <div class="step-num">2</div>
                <div class="step-text"><strong>Core Mathematical Principle:</strong> A dual-line graph plots two distinct series on the same coordinate grid. The horizontal X-axis represents chronological days (Mon–Sun); the vertical Y-axis represents customer count (0 to 40). The gap between the two lines represents non-purchasing visitors.</div>
              </div>
              <div class="step-box">
                <div class="step-num">3</div>
                <div class="step-text"><strong>Step-by-Step Plotting &amp; Analytical Findings:</strong>
                  <br>&bull; <em>Plotting coordinates:</em>
                  <br>Visiting Line (Blue): Mon(16), Tue(19), Wed(10), Thu(14), Fri(20), Sat(22), Sun(35).
                  <br>Purchasing Line (Green): Mon(10), Tue(8), Wed(7), Thu(11), Fri(12), Sat(16), Sun(26).
                  <br>&bull; <em>Observations:</em>
                  <br>1. <strong>Weekly Peak:</strong> Sunday experiences both the highest footfall (35 visitors) and the highest sales (26 buyers). The steep upward slope from Saturday to Sunday illustrates weekend shopping surge.
                  <br>2. <strong>Midweek Trough:</strong> Wednesday has the lowest footfall (10 visitors) and sales (7 buyers).
                  <br>3. <strong>Purchasing Ratio:</strong> On Sunday, <span class="math-inline">26 / 35 &approx; 74.3%</span> of visitors make a purchase; on Tuesday, only <span class="math-inline">8 / 19 &approx; 42.1%</span> make a purchase.
                </div>
              </div>
              <div class="step-box">
                <div class="step-num">4</div>
                <div class="step-text"><strong>Verification &amp; Check:</strong> In every single day, Purchasing &le; Visiting, ensuring the green line runs strictly below or touches the blue line at all times.</div>
              </div>
              <div class="step-box">
                <div class="step-num">5</div>
                <div class="step-text"><strong>Concluding Statement:</strong> The dual-line graph shows that both store traffic and sales peak dramatically on Sunday, with Wednesday recording the weekly minimum.</div>
              </div>
            </div>
          </details>
        </div>

        <!-- FIO 2 Q2 -->
        <div class="solved-card">
          <div class="solved-title"><i class="fa-solid fa-calculator"></i> Question 2: Coastal Cities Monthly Rainfall Days Comparison (Book p. 122–123)</div>
          <p>
            The table records monthly average rainy days for Mangaluru, New Delhi, Port Blair, and Rameswaram:
            <br>(i) What could be the possible method to compile this data?
            <br>(ii) Mark the data on a line graph.
            <br>(iii) Fill New Delhi data from the graph.
            <br>(iv) Which city receives the most and least rainy days per year?
            <br>(v) When is the rainy season in New Delhi and Rameswaram?
          </p>
          <details class="ans-box">
            <summary>View 5-Step Solution</summary>
            <div class="ans-content">
              <div class="step-box">
                <div class="step-num">1</div>
                <div class="step-text"><strong>Given Information &amp; Context:</strong> Meteorological data tracking days with measurable precipitation across 12 calendar months for four diverse Indian cities.</div>
              </div>
              <div class="step-box">
                <div class="step-num">2</div>
                <div class="step-text"><strong>Core Mathematical Principle:</strong> Multi-year statistical averaging: Daily rainfall records collected over 10 to 30 years are averaged for each calendar month to establish climatological baselines.</div>
              </div>
              <div class="step-box">
                <div class="step-num">3</div>
                <div class="step-text"><strong>Step-by-Step Analysis &amp; Answers:</strong>
                  <br>&bull; <strong>(i) Data Compilation Method:</strong> Weather stations operated by the India Meteorological Department (IMD) record daily precipitation using rain gauges. Over many years (e.g., 30 years), the total number of rainy days in June is summed and divided by 30 to get June's monthly average.
                  <br>&bull; <strong>(iii) New Delhi Rainfall Profile:</strong> In northern India, New Delhi has very low rainfall from Jan to May (&lt;2 days/month). In July and August, monsoon arrives with ~8 to 10 rainy days per month, before tapering off by October.
                  <br>&bull; <strong>(iv) Most vs Least Annual Rainy Days:</strong>
                  <br>- <strong>Port Blair &amp; Mangaluru</strong> receive the highest number of annual rainy days (Port Blair has over 140 rainy days due to its equatorial island location).
                  <br>- <strong>New Delhi</strong> receives the least number of annual rainy days (around 30–35 days total).
                  <br>&bull; <strong>(v) Rainy Seasons:</strong>
                  <br>- <strong>New Delhi:</strong> July to August (Southwest Monsoon).
                  <br>- <strong>Rameswaram:</strong> October to December (Retreating Northeast Monsoon, peaking in November with 10.4 rainy days).
                </div>
              </div>
              <div class="step-box">
                <div class="step-num">4</div>
                <div class="step-text"><strong>Verification &amp; Check:</strong> Mangaluru peaks in July (27.7 days, SW monsoon) while Rameswaram is dry in July (1 day) and peaks in November (10.4 days, NE monsoon), perfectly verifying opposite coastal wind regimes.</div>
              </div>
              <div class="step-box">
                <div class="step-num">5</div>
                <div class="step-text"><strong>Concluding Statement:</strong> Port Blair records the most rainy days; New Delhi the least. New Delhi's monsoon occurs in July–August, while Rameswaram's occurs in October–December.</div>
              </div>
            </div>
          </details>
        </div>

        <!-- FIO 2 Q3 -->
        <div class="solved-card">
          <div class="solved-title"><i class="fa-solid fa-calculator"></i> Question 3: Monthly Births in India Over Time (Book p. 123)</div>
          <p>
            The line graph shows the number of registered births in India across every month over multiple years:
            <br>(i) What are your observations?
            <br>(ii) What was the approximate number of births in July 2017?
            <br>(iii) What time period does the graph capture?
            <br>(iv) Compare the number of births in January in 2018, 2019, and 2020.
            <br>(v) Estimate the total number of births in the year 2019.
          </p>
          <details class="ans-box">
            <summary>View 5-Step Solution</summary>
            <div class="ans-content">
              <div class="step-box">
                <div class="step-num">1</div>
                <div class="step-text"><strong>Given Information &amp; Context:</strong> A continuous multi-year time-series line graph showing monthly births in India (measured in lakhs/millions).</div>
              </div>
              <div class="step-box">
                <div class="step-num">2</div>
                <div class="step-text"><strong>Core Mathematical Principle:</strong> Periodic seasonality in demographic time series: Reading peak coordinates, reading vertical values for specific months, and integrating (summing) monthly values to compute an annual total.</div>
              </div>
              <div class="step-box">
                <div class="step-num">3</div>
                <div class="step-text"><strong>Step-by-Step Analysis:</strong>
                  <br>&bull; <strong>(i) Observations:</strong> Births in India display a distinct recurring annual wave! Births consistently peak during August, September, and October (late monsoon/autumn), while dipping to annual lows around February and March.
                  <br>&bull; <strong>(ii) Births in July 2017:</strong> Reading off the vertical axis at the July 2017 marker indicates approximately <strong>21 to 22 lakh births</strong> (~2.15 million).
                  <br>&bull; <strong>(iii) Time Period Captured:</strong> The horizontal axis spans from <strong>mid-2016 to 2021</strong> (approximately 5 years of monthly data).
                  <br>&bull; <strong>(iv) Comparison of January Births (2018, 2019, 2020):</strong> Across these three consecutive years, January births remained fairly stable around 18–19 lakhs, showing only slight demographic variations.
                  <br>&bull; <strong>(v) Annual Estimate for 2019:</strong> With average monthly births of approximately 20 lakhs:
                  <div class="math-block">Annual Total &approx; 20  lakhs &times; 12  months &approx; 240  lakhs = <strong>2.4  Crores (24 million)</strong></div>
                </div>
              </div>
              <div class="step-box">
                <div class="step-num">4</div>
                <div class="step-text"><strong>Verification &amp; Check:</strong> According to official census and civil registration system (CRS) data, India registers approximately 2.4 to 2.5 crore births annually, perfectly matching our graphical estimation!</div>
              </div>
              <div class="step-box">
                <div class="step-num">5</div>
                <div class="step-text"><strong>Concluding Statement:</strong> Monthly births show annual seasonal periodicity peaking in autumn, yielding an estimated <strong>2.4 crore births</strong> in India in 2019.</div>
              </div>
            </div>
          </details>
        </div>

        <!-- In-Text Infographic: Rice vs Wheat -->
        <div class="solved-card">
          <div class="solved-title"><i class="fa-solid fa-map-location-dot"></i> In-Text Investigation: Rice vs Wheat Geographic Preference Infographic (Book p. 124)</div>
          <p>
            An infographic maps state-wise preference between rice and wheat from -100 (mostly wheat) to +100 (mostly rice):
            <br>(i) The value of Karnataka is hidden. What could it reasonably be?
            <br>(ii) Top 5 states where rice is most popular.
            <br>(iii) Top 5 states where wheat is most popular.
            <br>(iv) List states where consumption is balanced.
          </p>
          <details class="ans-box">
            <summary>View 5-Step Solution</summary>
            <div class="ans-content">
              <div class="step-box">
                <div class="step-num">1</div>
                <div class="step-text"><strong>Given Information &amp; Context:</strong> A thematic choropleth map of India with a continuous index from -100 (deep brown: high wheat) to +100 (deep green: high rice).</div>
              </div>
              <div class="step-box">
                <div class="step-num">2</div>
                <div class="step-text"><strong>Core Mathematical Principle:</strong> Spatial continuity and geographic interpolation: Neighboring regions with similar agro-climatic conditions exhibit similar cultural and dietary consumption indices.</div>
              </div>
              <div class="step-box">
                <div class="step-num">3</div>
                <div class="step-text"><strong>Step-by-Step Analysis:</strong>
                  <br>&bull; <strong>(i) Karnataka's Hidden Value:</strong> Karnataka is surrounded by Kerala (+90), Tamil Nadu (+85), Andhra Pradesh (+90), and Maharashtra (-20). South Karnataka traditionally consumes rice and ragi, while North Karnataka consumes jowar and wheat. Thus, Karnataka's overall state score is moderately rice-dominant, approximately <strong>+50 to +65</strong>.
                  <br>&bull; <strong>(ii) Top 5 Rice States (Score near +100):</strong>
                  <br>1. Odisha &nbsp;|&nbsp; 2. West Bengal &nbsp;|&nbsp; 3. Kerala &nbsp;|&nbsp; 4. Assam &nbsp;|&nbsp; 5. Andhra Pradesh.
                  <br>&bull; <strong>(iii) Top 5 Wheat States (Score near -100):</strong>
                  <br>1. Punjab &nbsp;|&nbsp; 2. Haryana &nbsp;|&nbsp; 3. Rajasthan &nbsp;|&nbsp; 4. Madhya Pradesh &nbsp;|&nbsp; 5. Uttar Pradesh.
                  <br>&bull; <strong>(iv) Balanced States (Score near 0):</strong>
                  <br>Maharashtra, Gujarat, and parts of Chhattisgarh display balanced consumption of both rice and wheat.
                </div>
              </div>
              <div class="step-box">
                <div class="step-num">4</div>
                <div class="step-text"><strong>Verification &amp; Check:</strong> The red dividing line on the map traces the Vindhya-Satpura range and the Tropic of Cancer, matching the geological boundary between alluvial/coastal rice plains and northern wheat fields.</div>
              </div>
              <div class="step-box">
                <div class="step-num">5</div>
                <div class="step-text"><strong>Concluding Statement:</strong> Karnataka's value is around <strong>+55</strong>; eastern/southern coastal states prefer rice; north-western inland states prefer wheat.</div>
              </div>
            </div>
          </details>
        </div>
      </div>

      <!-- ========================================================
           SUBSECTION 4D: FIGURE IT OUT 3 (END EXERCISES 1 TO 15)
           ======================================================== -->
      <div style="margin-bottom: 2.5rem;">
        <h3 style="font-family: 'Space Grotesk', sans-serif; font-size: 1.4rem; color: var(--primary-dark); margin-bottom: 1.25rem;">
          <i class="fa-solid fa-graduation-cap"></i> Part 4D: Complete Solutions to 'Figure it Out 3' (Back Exercises 1 to 15 + Hex)
        </h3>

        <!-- FIO 3 Q1 -->
        <div class="solved-card">
          <div class="solved-title"><i class="fa-solid fa-calculator"></i> Exercise 1: Mean Grids (3 &times; 3 Magic Square of Averages) (Book p. 127)</div>
          <p>
            (i) Fill the 3 &times; 3 grid with 9 distinct numbers such that the average along each row, column, and diagonal is <strong>10</strong>.
            <br>(ii) Can we fill the grid by changing a few numbers and still get 10 as the average in all directions?
          </p>
          <details class="ans-box">
            <summary>View 5-Step Solution</summary>
            <div class="ans-content">
              <div class="step-box">
                <div class="step-num">1</div>
                <div class="step-text"><strong>Given Information &amp; Context:</strong> A 3 &times; 3 grid containing 9 distinct cells. Every line of 3 numbers must have an average of 10.</div>
              </div>
              <div class="step-box">
                <div class="step-num">2</div>
                <div class="step-text"><strong>Core Mathematical Principle:</strong> If the average of 3 numbers is 10, their sum must be <span class="math-inline">3 &times; 10 = 30</span>! In any 3 &times; 3 magic square with sum <span class="math-inline">S = 30</span>, the central cell must strictly equal <span class="math-inline">S / 3 = 10</span>.</div>
              </div>
              <div class="step-box">
                <div class="step-num">3</div>
                <div class="step-text"><strong>Step-by-Step Construction:</strong>
                  <br>&bull; (i) Standard construction using the 9 consecutive numbers symmetric about 10: {6, 7, 8, 9, <strong>10</strong>, 11, 12, 13, 14}.
                  <br>Arranging them in magic square order:
                  <div class="math-block" style="text-align: center;">
                    [ 13 &nbsp;&nbsp; 8 &nbsp;&nbsp; 9 ] &rArr; Sum = 30, Mean = 10<br>
                    [ &nbsp;6 &nbsp;&nbsp; 10 &nbsp;&nbsp; 14 ] &rArr; Sum = 30, Mean = 10<br>
                    [ 11 &nbsp;&nbsp; 12 &nbsp;&nbsp; 7 ] &rArr; Sum = 30, Mean = 10
                  </div>
                  <br>Checking Columns:
                  <br>Col 1: 13 + 6 + 11 = 30 &rArr; Mean = 10.
                  <br>Col 2: 8 + 10 + 12 = 30 &rArr; Mean = 10.
                  <br>Col 3: 9 + 14 + 7 = 30 &rArr; Mean = 10.
                  <br>Checking Diagonals:
                  <br>Main diag: 13 + 10 + 7 = 30 &rArr; Mean = 10.
                  <br>Anti diag: 9 + 10 + 11 = 30 &rArr; Mean = 10.
                  <br>&bull; (ii) Yes! By adding or subtracting a constant <span class="math-inline">d</span> to complementary pairs around the center 10 (e.g., using {2, 4, 6, 8, 10, 12, 14, 16, 18}), infinitely many distinct grids can be formed with mean 10!
                </div>
              </div>
              <div class="step-box">
                <div class="step-num">4</div>
                <div class="step-text"><strong>Verification &amp; Check:</strong> All 8 lines sum to 30, so every line average is <span class="math-inline">30 / 3 = 10</span>. All 9 entries are strictly distinct.</div>
              </div>
              <div class="step-box">
                <div class="step-num">5</div>
                <div class="step-text"><strong>Concluding Statement:</strong> The grid with rows [13, 8, 9], [6, 10, 14], and [11, 12, 7] has a mean of 10 in all rows, columns, and diagonals.</div>
              </div>
            </div>
          </details>
        </div>

        <!-- FIO 3 Q2 -->
        <div class="solved-card">
          <div class="solved-title"><i class="fa-solid fa-calculator"></i> Exercise 2: Constructing Datasets Satisfying Specific Mean/Median Constraints (Book p. 127)</div>
          <p>
            Give two examples of data collections that satisfy each condition:
            <br>(i) 3 numbers whose mean is 8.
            <br>(ii) 4 numbers whose median is 15.5.
            <br>(iii) 5 numbers whose mean is 13.6.
            <br>(iv) 6 numbers whose mean = median.
            <br>(v) 6 numbers whose mean &gt; median.
          </p>
          <details class="ans-box">
            <summary>View 5-Step Solution</summary>
            <div class="ans-content">
              <div class="step-box">
                <div class="step-num">1</div>
                <div class="step-text"><strong>Given Information &amp; Context:</strong> Five distinct mathematical design constraints on datasets of varying sizes.</div>
              </div>
              <div class="step-box">
                <div class="step-num">2</div>
                <div class="step-text"><strong>Core Mathematical Principle:</strong>
                  <br>&bull; Mean constraint: <span class="math-inline">Sum = n &times; Mean</span>.
                  <br>&bull; Median constraint: The central value(s) in sorted order must produce the target.
                  <br>&bull; Skewness: If extreme high outliers exist, Mean &gt; Median. If symmetric, Mean = Median.</div>
              </div>
              <div class="step-box">
                <div class="step-num">3</div>
                <div class="step-text"><strong>Step-by-Step Construction:</strong>
                  <br>&bull; <strong>(i) 3 numbers, Mean = 8:</strong> Target sum = <span class="math-inline">3 &times; 8 = 24</span>.
                  <br>Example A: <strong>{7, 8, 9}</strong> (<span class="math-inline">7+8+9=24</span>).
                  <br>Example B: <strong>{2, 6, 16}</strong> (<span class="math-inline">2+6+16=24</span>).
                  <br>&bull; <strong>(ii) 4 numbers, Median = 15.5:</strong> Sum of 2 middle numbers = <span class="math-inline">15.5 &times; 2 = 31</span>.
                  <br>Example A: <strong>{10, 15, 16, 20}</strong> (<span class="math-inline">(15+16)/2 = 15.5</span>).
                  <br>Example B: <strong>{5, 14, 17, 30}</strong> (<span class="math-inline">(14+17)/2 = 15.5</span>).
                  <br>&bull; <strong>(iii) 5 numbers, Mean = 13.6:</strong> Target sum = <span class="math-inline">5 &times; 13.6 = 68</span>.
                  <br>Example A: <strong>{10, 12, 14, 15, 17}</strong> (Sum = 68).
                  <br>Example B: <strong>{8, 10, 12, 18, 20}</strong> (Sum = 68).
                  <br>&bull; <strong>(iv) 6 numbers, Mean = Median:</strong> Any symmetric distribution!
                  <br>Example A: <strong>{2, 4, 6, 8, 10, 12}</strong> (Mean = 7, Median = (6+8)/2 = 7).
                  <br>Example B: <strong>{5, 5, 5, 5, 5, 5}</strong> (Mean = 5, Median = 5).
                  <br>&bull; <strong>(v) 6 numbers, Mean &gt; Median:</strong> Introduce a large positive outlier!
                  <br>Example A: <strong>{1, 2, 3, 4, 5, 45}</strong> (Median = (3+4)/2 = 3.5; Mean = 60/6 = 10 &gt; 3.5).
                  <br>Example B: <strong>{10, 10, 10, 10, 10, 100}</strong> (Median = 10; Mean = 150/6 = 25 &gt; 10).
                </div>
              </div>
              <div class="step-box">
                <div class="step-num">4</div>
                <div class="step-text"><strong>Verification &amp; Check:</strong> All sums and median averages match the target requirements perfectly.</div>
              </div>
              <div class="step-box">
                <div class="step-num">5</div>
                <div class="step-text"><strong>Concluding Statement:</strong> Datasets successfully constructed fulfilling all 5 criteria with verifiable arithmetic.</div>
              </div>
            </div>
          </details>
        </div>

        <!-- FIO 3 Q3 -->
        <div class="solved-card">
          <div class="solved-title"><i class="fa-solid fa-calculator"></i> Exercise 3: Filling Blanks for Median 13 (Book p. 127)</div>
          <p>
            Fill in the blanks such that the median of the collection is <strong>13</strong>:
            <br>5, 21, 14, _____, ______, ______
            <br>How many possibilities exist if only counting numbers (positive integers) are allowed?
          </p>
          <details class="ans-box">
            <summary>View 5-Step Solution</summary>
            <div class="ans-content">
              <div class="step-box">
                <div class="step-num">1</div>
                <div class="step-text"><strong>Given Information &amp; Context:</strong> Total count <span class="math-inline">N = 6</span> (even). Three known numbers: 5, 14, 21. Three unknown counting numbers: <span class="math-inline">a, b, c &isin; {1, 2, 3, ...}</span>. Target median = 13.</div>
              </div>
              <div class="step-box">
                <div class="step-num">2</div>
                <div class="step-text"><strong>Core Mathematical Principle:</strong> For <span class="math-inline">N = 6</span>, the median is the average of the 3rd and 4th values in sorted order: <span class="math-inline">(x_{(3)} + x_{(4)}) / 2 = 13 &rArr; x_{(3)} + x_{(4)} = 26</span>.</div>
              </div>
              <div class="step-box">
                <div class="step-num">3</div>
                <div class="step-text"><strong>Step-by-Step Analysis:</strong>
                  <br>&bull; The known numbers are: 5 (which is &lt; 13), and 14, 21 (which are &gt; 13).
                  <br>&bull; Currently, we have one value below 13 (5) and two values above 13 (14, 21).
                  <br>&bull; To place the median at 13:
                  <br>If <span class="math-inline">x_{(4)} = 14</span>, then <span class="math-inline">x_{(3)} = 26 - 14 = 12</span>.
                  <br>In this case, the sorted array is: <span class="math-inline">a, 5  (or  5, a), 12, 14, 21, c</span> where <span class="math-inline">a &le; 12</span> and <span class="math-inline">c &ge; 14</span>.
                  <br>Here, the two missing numbers are 12 and any counting number <span class="math-inline">a &le; 12</span>, plus any number <span class="math-inline">c &ge; 14</span>.
                  <br>Since <span class="math-inline">c</span> can be any integer <span class="math-inline">&ge; 14</span> (14, 15, 16, 17, 18, ...), there are <strong>infinitely many possibilities</strong>!
                  <br>&bull; Another case: If the two middle numbers are both 13, then <span class="math-inline">x_{(3)} = 13</span> and <span class="math-inline">x_{(4)} = 13</span>. Then the missing numbers include two 13s and one number &le; 13.
                </div>
              </div>
              <div class="step-box">
                <div class="step-num">4</div>
                <div class="step-text"><strong>Verification &amp; Check:</strong> Example collection: {5, 8, <strong>12, 14</strong>, 21, 50}. The 3rd and 4th values are 12 and 14. Median = <span class="math-inline">(12+14)/2 = 13</span>! Because the largest number can be arbitrarily large, the count of possibilities is unbounded.</div>
              </div>
              <div class="step-box">
                <div class="step-num">5</div>
                <div class="step-text"><strong>Concluding Statement:</strong> One valid filling is <strong>8, 12, 50</strong>. There are <strong>infinitely many possibilities</strong> because the numbers on the extremes are unconstrained.</div>
              </div>
            </div>
          </details>
        </div>

        <!-- FIO 3 Q4 -->
        <div class="solved-card">
          <div class="solved-title"><i class="fa-solid fa-calculator"></i> Exercise 4: Filling Blanks for Mean 6.5 (Book p. 127)</div>
          <p>
            Fill in the blanks such that the mean of the collection is <strong>6.5</strong>:
            <br>3, 11, ____, _____, 15, 6
            <br>How many possibilities exist if only counting numbers are allowed?
          </p>
          <details class="ans-box">
            <summary>View 5-Step Solution</summary>
            <div class="ans-content">
              <div class="step-box">
                <div class="step-num">1</div>
                <div class="step-text"><strong>Given Information &amp; Context:</strong> Total count <span class="math-inline">n = 6</span>. Four known values: 3, 11, 15, 6. Two unknown counting numbers: <span class="math-inline">x, y &isin; {1, 2, 3, ...}</span>. Target mean = 6.5.</div>
              </div>
              <div class="step-box">
                <div class="step-num">2</div>
                <div class="step-text"><strong>Core Mathematical Principle:</strong> <span class="math-inline">Total Sum = n &times; Mean = 6 &times; 6.5 = 39</span>.</div>
              </div>
              <div class="step-box">
                <div class="step-num">3</div>
                <div class="step-text"><strong>Step-by-Step Calculation:</strong>
                  <br>&bull; Sum of the 4 known numbers: <span class="math-inline">3 + 11 + 15 + 6 = 35</span>.
                  <br>&bull; Remaining sum for <span class="math-inline">x + y</span>:
                  <div class="math-block">x + y = 39 - 35 = 4</div>
                  <br>&bull; Since only counting numbers (positive integers <span class="math-inline">&ge; 1</span>) are allowed:
                  <br>Possibility 1: <span class="math-inline">x = 1, y = 3</span> &rArr; Pair (1, 3)
                  <br>Possibility 2: <span class="math-inline">x = 2, y = 2</span> &rArr; Pair (2, 2)
                  <br>Possibility 3: <span class="math-inline">x = 3, y = 1</span> &rArr; Pair (3, 1)
                </div>
              </div>
              <div class="step-box">
                <div class="step-num">4</div>
                <div class="step-text"><strong>Verification &amp; Check:</strong> If considered as an unordered set of two missing numbers, the sets are {1, 3} and {2, 2}. If considered as distinct blanks, there are <strong>3 ordered pairs</strong>.</div>
              </div>
              <div class="step-box">
                <div class="step-num">5</div>
                <div class="step-text"><strong>Concluding Statement:</strong> The blanks can be filled with <strong>1 and 3</strong> (or 2 and 2). Exactly <strong>3 ordered possibilities</strong> (or 2 distinct sets) exist.</div>
              </div>
            </div>
          </details>
        </div>

        <!-- FIO 3 Q5 -->
        <div class="solved-card">
          <div class="solved-title"><i class="fa-solid fa-calculator"></i> Exercise 5: True/False with Algebraic Justification (Book p. 127)</div>
          <p>
            Check whether each statement below is true. Justify using algebra:
            <br>(i) The average of two even numbers is even.
            <br>(ii) The average of any two multiples of 5 will be a multiple of 5.
            <br>(iii) The average of any 5 multiples of 5 will also be a multiple of 5.
          </p>
          <details class="ans-box">
            <summary>View 5-Step Solution</summary>
            <div class="ans-content">
              <div class="step-box">
                <div class="step-num">1</div>
                <div class="step-text"><strong>Given Information &amp; Context:</strong> Three arithmetic assertions regarding divisibility and parity of averages.</div>
              </div>
              <div class="step-box">
                <div class="step-num">2</div>
                <div class="step-text"><strong>Core Mathematical Principle:</strong> An even number is of the form <span class="math-inline">2m</span>. A multiple of 5 is of the form <span class="math-inline">5m</span>.</div>
              </div>
              <div class="step-box">
                <div class="step-num">3</div>
                <div class="step-text"><strong>Step-by-Step Algebraic Analysis:</strong>
                  <br>&bull; <strong>(i) Average of two even numbers:</strong>
                  <br>Let the two evens be <span class="math-inline">2a</span> and <span class="math-inline">2b</span>.
                  <br><span class="math-inline">Average = (2a + 2b)/2 = a + b</span>.
                  <br>If <span class="math-inline">a</span> and <span class="math-inline">b</span> have different parities (one even, one odd), their sum <span class="math-inline">a + b</span> is <strong>ODD</strong>!
                  <br><em>Counter-example:</em> 2 and 6. Average = <span class="math-inline">(2 + 6)/2 = 8/2 = 4</span> (even). But for 2 and 4, average = <span class="math-inline">(2 + 4)/2 = 6/2 = 3</span> (<strong>ODD!</strong>).
                  <br>Result: <strong>FALSE</strong>.
                  <br>&bull; <strong>(ii) Average of two multiples of 5:</strong>
                  <br>Let the numbers be <span class="math-inline">5a</span> and <span class="math-inline">5b</span>.
                  <br><span class="math-inline">Average = 5(a + b)/2</span>.
                  <br>For this to be a multiple of 5, <span class="math-inline">(a + b)</span> must be divisible by 2 (i.e., even). If <span class="math-inline">(a + b)</span> is odd, the average is not even an integer!
                  <br><em>Counter-example:</em> 5 and 10. Average = <span class="math-inline">(5 + 10)/2 = 15/2 = 7.5</span> (not a multiple of 5).
                  <br>Result: <strong>FALSE</strong>.
                  <br>&bull; <strong>(iii) Average of five multiples of 5:</strong>
                  <br>Let the numbers be <span class="math-inline">5a, 5b, 5c, 5d, 5e</span> where <span class="math-inline">a, b, c, d, e &isin; integers</span>.
                  <br><span class="math-inline">Average = (5a + 5b + 5c + 5d + 5e)/5 = 5(a + b + c + d + e)/5 = a + b + c + d + e</span>.
                  <br>Since <span class="math-inline">a, b, c, d, e</span> are integers, their sum is an integer. But is it necessarily a multiple of 5?
                  <br><em>Counter-example:</em> Let numbers be 5, 5, 5, 5, 10. (All are multiples of 5).
                  <br>Sum = 30. Average = <span class="math-inline">30 / 5 = 6</span>. But <strong>6 is NOT a multiple of 5</strong>!
                  <br>Result: <strong>FALSE</strong>.
                </div>
              </div>
              <div class="step-box">
                <div class="step-num">4</div>
                <div class="step-text"><strong>Verification &amp; Check:</strong> All three assertions fail under simple, easily verifiable counter-examples.</div>
              </div>
              <div class="step-box">
                <div class="step-num">5</div>
                <div class="step-text"><strong>Concluding Statement:</strong> All three statements are <strong>FALSE</strong> in general!</div>
              </div>
            </div>
          </details>
        </div>

        <!-- FIO 3 Q6 -->
        <div class="solved-card">
          <div class="solved-title"><i class="fa-solid fa-calculator"></i> Exercise 6: New Admissions Height Impact on Mean &amp; Median (Book p. 128)</div>
          <p>
            Two new students joined Sudhakar's class just after the class average height was found to be <strong>150.2 cm</strong>.
            <br>(i) Which general statement is correct? (a) Average increases because there are 2 new values; (b) Remains same; (c) Heights of new students must be measured; (d) Everyone must be measured again.
            <br>(ii) The heights of the two new joinees are 149 cm and 152 cm. What happens to class average height?
            <br>(iii) What happens to class median height?
          </p>
          <details class="ans-box">
            <summary>View 5-Step Solution</summary>
            <div class="ans-content">
              <div class="step-box">
                <div class="step-num">1</div>
                <div class="step-text"><strong>Given Information &amp; Context:</strong> Initial class size <span class="math-inline">n = 24</span>. Initial mean <span class="math-inline">x̄ = 150.2  cm</span>. Two new students join with heights 149 cm and 152 cm.</div>
              </div>
              <div class="step-box">
                <div class="step-num">2</div>
                <div class="step-text"><strong>Core Mathematical Principle:</strong> Compare the average of the new joinees to the existing class mean:
                  <div class="math-block">x̄_new_joinees = (149 + 152) / 2 = 301 / 2 = 150.5 cm</div>
                </div>
              </div>
              <div class="step-box">
                <div class="step-num">3</div>
                <div class="step-text"><strong>Step-by-Step Analysis:</strong>
                  <br>&bull; <strong>(i) General Case:</strong> Statement <strong>(c)</strong> is correct. You only need to measure the two new students, because their data combined with the old sum is sufficient.
                  <br>&bull; <strong>(ii) Impact on Average:</strong>
                  <br>The average of the two new joinees is <span class="math-inline">150.5  cm</span>.
                  <br>Since <span class="math-inline">150.5 &gt; 150.2</span> (their combined average is greater than the class average), they add a net positive deviation!
                  <br>Therefore, the class average height <strong>will increase</strong>! Option <strong>(b)</strong>.
                  <br>&bull; <strong>(iii) Impact on Median:</strong>
                  <br>We do not know the exact heights of all individual students in the class, nor do we know the previous median.
                  <br>Therefore, statement <strong>(d) "The information is not sufficient to make a claim about median"</strong> is correct!
                </div>
              </div>
              <div class="step-box">
                <div class="step-num">4</div>
                <div class="step-text"><strong>Verification &amp; Check:</strong> Net deviation of new joinees = <span class="math-inline">(149 - 150.2) + (152 - 150.2) = -1.2 + 1.8 = +0.6</span>. Since net deviation &gt; 0, the mean must increase by <span class="math-inline">0.6 / 26 &approx; 0.023  cm</span>.</div>
              </div>
              <div class="step-box">
                <div class="step-num">5</div>
                <div class="step-text"><strong>Concluding Statement:</strong> (i) Correct statement is <strong>(c)</strong>; (ii) Average <strong>increases</strong>; (iii) Correct option is <strong>(d) insufficient information</strong>.</div>
              </div>
            </div>
          </details>
        </div>

        <!-- FIO 3 Q7 -->
        <div class="solved-card">
          <div class="solved-title"><i class="fa-solid fa-calculator"></i> Exercise 7: Verifying Mean 17 on Dot Plot via Balance Method (Book p. 128)</div>
          <p>
            Is 17 the average of the data shown in the dot plot?
            <br>Crosses per value: 14(2), 15(2), 16(3), 17(5), 18(4), 19(4), 20(3), 21(2).
            <br>Share the method you used to answer this question.
          </p>
          <details class="ans-box">
            <summary>View 5-Step Solution</summary>
            <div class="ans-content">
              <div class="step-box">
                <div class="step-num">1</div>
                <div class="step-text"><strong>Given Information &amp; Context:</strong> Data with counts: 14(2), 15(2), 16(3), 17(5), 18(4), 19(4), 20(3), 21(2). Tested mean = 17.</div>
              </div>
              <div class="step-box">
                <div class="step-num">2</div>
                <div class="step-text"><strong>Core Mathematical Principle:</strong> The Lever Balance Law: 17 can only be the average if the sum of all leftward distances equals the sum of all rightward distances from 17!</div>
              </div>
              <div class="step-box">
                <div class="step-num">3</div>
                <div class="step-text"><strong>Step-by-Step Calculation (The Distance Balance Method):</strong>
                  <br>&bull; <em>Left-Hand Side Distances from 17:</em>
                  <br>At 16 (dist = 1): <span class="math-inline">3 &times; 1 = 3</span>
                  <br>At 15 (dist = 2): <span class="math-inline">2 &times; 2 = 4</span>
                  <br>At 14 (dist = 3): <span class="math-inline">2 &times; 3 = 6</span>
                  <br><strong>Total LHS Distance = 3 + 4 + 6 = 13 units.</strong>
                  <br>&bull; <em>Right-Hand Side Distances from 17:</em>
                  <br>At 18 (dist = 1): <span class="math-inline">4 &times; 1 = 4</span>
                  <br>At 19 (dist = 2): <span class="math-inline">4 &times; 2 = 8</span>
                  <br>At 20 (dist = 3): <span class="math-inline">3 &times; 3 = 9</span>
                  <br>At 21 (dist = 4): <span class="math-inline">2 &times; 4 = 8</span>
                  <br><strong>Total RHS Distance = 4 + 8 + 9 + 8 = 29 units!</strong>
                </div>
              </div>
              <div class="step-box">
                <div class="step-num">4</div>
                <div class="step-text"><strong>Verification &amp; Check:</strong> Notice that <span class="math-inline">13 &ne; 29</span>! The right side has far more torque (29 units) than the left side (13 units). Therefore, 17 is NOT the center of balance; the true average lies to the right (around 17.64).</div>
              </div>
              <div class="step-box">
                <div class="step-num">5</div>
                <div class="step-text"><strong>Concluding Statement:</strong> <strong>No, 17 is not the average.</strong> The total rightward distance (29) vastly exceeds the leftward distance (13).</div>
              </div>
            </div>
          </details>
        </div>

        <!-- FIO 3 Q8 -->
        <div class="solved-card">
          <div class="solved-title"><i class="fa-solid fa-calculator"></i> Exercise 8: Weight Group Recalculation (Lost 2 kg, Gained 1 kg x 2) (Book p. 128–129)</div>
          <p>
            The average weight of a group was <strong>65.3 kg</strong> and median was <strong>67 kg</strong>. This month, one person lost 2 kg (-2 kg) and two persons each gained 1 kg (+1 kg, +1 kg). What can we say about the change in mean weight and median weight?
          </p>
          <details class="ans-box">
            <summary>View 5-Step Solution</summary>
            <div class="ans-content">
              <div class="step-box">
                <div class="step-num">1</div>
                <div class="step-text"><strong>Given Information &amp; Context:</strong> Initial mean = 65.3 kg; Initial median = 67 kg. Individual changes: Person A (-2 kg), Person B (+1 kg), Person C (+1 kg).</div>
              </div>
              <div class="step-box">
                <div class="step-num">2</div>
                <div class="step-text"><strong>Core Mathematical Principle:</strong>
                  <br>&bull; Net change in group total weight = Sum of all individual changes.
                  <br>&bull; Change in Mean = <span class="math-inline">(Net Change in Total) / n</span>.</div>
              </div>
              <div class="step-box">
                <div class="step-num">3</div>
                <div class="step-text"><strong>Step-by-Step Calculation:</strong>
                  <br>&bull; <em>Net Change in Total Weight:</em>
                  <div class="math-block">Net Change = (-2) + (+1) + (+1) = 0  kg!</div>
                  <br>&bull; <em>Impact on Mean:</em> Since the net change in total group weight is exactly zero, <strong>the mean weight remains completely unchanged at 65.3 kg</strong>!
                  <br>&bull; <em>Impact on Median:</em> If the person who lost weight and the persons who gained weight were on opposite sides of 67 kg, their ranking relative to the middle could remain identical, leaving the median unchanged. However, if someone crossed the median mark, the median might shift slightly. Thus, the median <strong>most likely stays the same or may change slightly</strong> depending on individual starting weights.
                </div>
              </div>
              <div class="step-box">
                <div class="step-num">4</div>
                <div class="step-text"><strong>Verification &amp; Check:</strong> Total weight before = <span class="math-inline">65.3 &times; n</span>. Total weight after = <span class="math-inline">65.3 &times; n - 2 + 1 + 1 = 65.3 &times; n</span>. Dividing by <span class="math-inline">n</span> gives exactly 65.3 kg.</div>
              </div>
              <div class="step-box">
                <div class="step-num">5</div>
                <div class="step-text"><strong>Concluding Statement:</strong> The <strong>mean weight is strictly unchanged (0 kg change)</strong>, while the median weight is <strong>unlikely to change significantly</strong>.</div>
              </div>
            </div>
          </details>
        </div>

        <!-- FIO 3 Q9 -->
        <div class="solved-card">
          <div class="solved-title"><i class="fa-solid fa-calculator"></i> Exercise 9: Retail Price of Iodised Salt 2016–2025 (Book p. 129)</div>
          <p>
            A 10-year table records the retail price of iodised salt (in ₹) across 6 states/UTs (Andaman &amp; Nicobar, Assam, Gujarat, Mizoram, Uttar Pradesh, West Bengal).
            <br>(i) Plot any 3 states on a line graph.
            <br>(ii) Compare price variation in Gujarat vs Uttar Pradesh.
            <br>(iii) In which state has the price increased the most from 2016 to 2025?
          </p>
          <details class="ans-box">
            <summary>View 5-Step Solution</summary>
            <div class="ans-content">
              <div class="step-box">
                <div class="step-num">1</div>
                <div class="step-text"><strong>Given Information &amp; Context:</strong> Salt prices across a 10-year window (2016 to 2025). Notable values:
                  <br>&bull; Gujarat: 2016 = ₹16.5 &rArr; 2025 = ₹19.2 (Net increase = ₹2.7).
                  <br>&bull; Uttar Pradesh: 2016 = ₹16.15 &rArr; 2025 = ₹24.81 (Net increase = ₹8.66).
                  <br>&bull; West Bengal: 2016 = ₹9.47 &rArr; 2025 = ₹23.99 (Net increase = ₹14.52).
                  <br>&bull; Mizoram: 2016 = ₹20.0 &rArr; 2025 = ₹29.8 (Net increase = ₹9.8).
                  <br>&bull; Assam: 2016 = ₹6.0 &rArr; 2025 = ₹12.35 (Net increase = ₹6.35).
                </div>
              </div>
              <div class="step-box">
                <div class="step-num">2</div>
                <div class="step-text"><strong>Core Mathematical Principle:</strong> Net price increase = <span class="math-inline">Price_{2025} - Price_{2016}</span>. Percentage increase = <span class="math-inline">(&Delta; P / P_{2016}) &times; 100%</span>.</div>
              </div>
              <div class="step-box">
                <div class="step-num">3</div>
                <div class="step-text"><strong>Step-by-Step Analysis:</strong>
                  <br>&bull; <strong>(ii) Gujarat vs Uttar Pradesh Comparison:</strong>
                  <br>Gujarat is India's leading producer of salt (accounting for over 75% of national production from coastal salt pans). Because transportation and logistics costs are minimal within Gujarat, its salt price remained remarkably stable (hovering between ₹13 and ₹19 over the entire decade).
                  <br>In contrast, Uttar Pradesh is an inland state requiring long-distance freight transit. Its price rose steadily from ₹16.15 to ₹24.81 (an increase of over 53%).
                  <br>&bull; <strong>(iii) Maximum Absolute Increase:</strong>
                  <br>In <strong>West Bengal</strong>, the price surged from ₹9.47 in 2016 to ₹23.99 in 2025—an absolute increase of <strong>₹14.52 per kg</strong> (over 153% inflation)!
                </div>
              </div>
              <div class="step-box">
                <div class="step-num">4</div>
                <div class="step-text"><strong>Verification &amp; Check:</strong> West Bengal increase: <span class="math-inline">23.99 - 9.47 = 14.52</span>, which is higher than Mizoram (9.80) and UP (8.66).</div>
              </div>
              <div class="step-box">
                <div class="step-num">5</div>
                <div class="step-text"><strong>Concluding Statement:</strong> Salt prices were most stable in <strong>Gujarat</strong> (local production) and experienced the greatest increase in <strong>West Bengal</strong> (+₹14.52).</div>
              </div>
            </div>
          </details>
        </div>

        <!-- FIO 3 Q10 -->
        <div class="solved-card">
          <div class="solved-title"><i class="fa-solid fa-calculator"></i> Exercise 10: Lighting Sources in India 1983–2023 (Book p. 130)</div>
          <p>
            Referring to the historical lighting source graph, validate each statement:
            <br>(i) In 1983, the majority in rural areas used kerosene as primary lighting while urban used electricity.
            <br>(ii) The use of kerosene has decreased over time in both rural and urban areas.
            <br>(iii) In the year 2000, 10% of urban households used electricity as primary lighting.
            <br>(iv) In 2023, there were no power cuts.
          </p>
          <details class="ans-box">
            <summary>View 5-Step Solution</summary>
            <div class="ans-content">
              <div class="step-box">
                <div class="step-num">1</div>
                <div class="step-text"><strong>Given Information &amp; Context:</strong> A dual time-series graph tracking percentage of households using kerosene vs electricity across rural and urban India from 1983 to 2023.</div>
              </div>
              <div class="step-box">
                <div class="step-num">2</div>
                <div class="step-text"><strong>Core Mathematical Principle:</strong> Graph interpretation protocol: Distinguish between what data directly proves versus unsupported extrapolations.</div>
              </div>
              <div class="step-box">
                <div class="step-num">3</div>
                <div class="step-text"><strong>Step-by-Step Analysis:</strong>
                  <br>&bull; (i) <strong>VALID:</strong> In 1983, rural kerosene usage was well above 70% (a clear majority), while urban electricity was around 65% (a majority).
                  <br>&bull; (ii) <strong>VALID:</strong> Both rural and urban kerosene lines trend downwards continuously towards zero by 2023.
                  <br>&bull; (iii) <strong>INVALID:</strong> In 2000, approximately 10% of urban households used <em>kerosene</em>, while ~90% used electricity! The statement mistakenly swapped the two sources.
                  <br>&bull; (iv) <strong>INVALID:</strong> The graph records household primary connection type, not the quality or uninterrupted continuity of power supply! One cannot infer power cuts from connection stats.
                </div>
              </div>
              <div class="step-box">
                <div class="step-num">4</div>
                <div class="step-text"><strong>Verification &amp; Check:</strong> Statements (i) and (ii) directly mirror the graph lines; (iii) misreads the variable; (iv) makes an invalid causal leap.</div>
              </div>
              <div class="step-box">
                <div class="step-num">5</div>
                <div class="step-text"><strong>Concluding Statement:</strong> Statements <strong>(i) and (ii) are VALID</strong>; statements <strong>(iii) and (iv) are INVALID</strong>.</div>
              </div>
            </div>
          </details>
        </div>

        <!-- FIO 3 Q11 -->
        <div class="solved-card">
          <div class="solved-title"><i class="fa-solid fa-calculator"></i> Exercise 11: Daily Time Spent on Hobbies &amp; Games (Book p. 130–131)</div>
          <p>
            Based on the line graph of daily hobby and playtime:
            <br>(i) How long do children aged 10 in urban areas spend on hobbies and games?
            <br>(ii) At what age is the average time spent daily on hobbies by rural kids 1.5 hours?
            <br>(iii) Are these statements correct? (a) Daily hobby time for 15-year-olds is twice that of 10-year-olds; (b) All rural kids aged 15 spend at least 1 hour on hobbies.
          </p>
          <details class="ans-box">
            <summary>View 5-Step Solution</summary>
            <div class="ans-content">
              <div class="step-box">
                <div class="step-num">1</div>
                <div class="step-text"><strong>Given Information &amp; Context:</strong> Line graphs tracking daily average hobby hours for rural and urban youth across ages 6 to 18.</div>
              </div>
              <div class="step-box">
                <div class="step-num">2</div>
                <div class="step-text"><strong>Core Mathematical Principle:</strong> Reading point coordinates on line graphs and differentiating between <strong>group average</strong> versus <strong>individual performance</strong>.</div>
              </div>
              <div class="step-box">
                <div class="step-num">3</div>
                <div class="step-text"><strong>Step-by-Step Analysis:</strong>
                  <br>&bull; <strong>(i) Urban 10-year-olds:</strong> Locating age 10 on the X-axis and moving up to the urban line gives approximately <strong>1.2 to 1.3 hours (around 75 minutes)</strong>.
                  <br>&bull; <strong>(ii) Rural kids at 1.5 hours:</strong> Tracing horizontally from 1.5 hours on the Y-axis to the rural curve intersects at <strong>Age 12</strong> (option c).
                  <br>&bull; <strong>(iii-a) "Twice that of 10-year-olds":</strong> Reading values shows time increases only modestly (from ~1.2h to ~1.6h), which is NOT double! <strong>INCORRECT</strong>.
                  <br>&bull; <strong>(iii-b) "ALL rural kids spend at least 1 hour":</strong> <strong>INCORRECT!</strong> The graph shows the <em>average</em>. An average of 1.5 hours can easily include individual children who spend 0 minutes and others who spend 3 hours!
                </div>
              </div>
              <div class="step-box">
                <div class="step-num">4</div>
                <div class="step-text"><strong>Verification &amp; Check:</strong> Confusing a population average with individual universality is a classic statistical trap.</div>
              </div>
              <div class="step-box">
                <div class="step-num">5</div>
                <div class="step-text"><strong>Concluding Statement:</strong> (i) ~1.25 hours; (ii) <strong>12 years</strong>; (iii) Both statements (a) and (b) are <strong>INCORRECT</strong>.</div>
              </div>
            </div>
          </details>
        </div>

        <!-- FIO 3 Q12 & Q13 -->
        <div class="solved-card">
          <div class="solved-title"><i class="fa-solid fa-calculator"></i> Exercises 12 &amp; 13: Activity Strip &amp; Sleep Tracking Projects (Book p. 131)</div>
          <p>
            Summary and model methodology for the student projects:
            <br>&bull; Exercise 12: Constructing a 48-box activity strip and calculating average time per activity.
            <br>&bull; Exercise 13: Tracking family sleep duration and comparing nationwide Grade 8 school timings.
          </p>
          <details class="ans-box">
            <summary>View 5-Step Solution</summary>
            <div class="ans-content">
              <div class="step-box">
                <div class="step-num">1</div>
                <div class="step-text"><strong>Project Objectives:</strong> Experiential data collection, discretization of 24-hour continuous time, and empirical statistical aggregation.</div>
              </div>
              <div class="step-box">
                <div class="step-num">2</div>
                <div class="step-text"><strong>Core Methodological Framework:</strong>
                  <br>&bull; Strip Discretization: <span class="math-inline">24  hours &times; 2 = 48  cells</span> of 30 minutes each.
                  <br>&bull; Average Activity Time = <span class="math-inline">(Total cells assigned to activity &times; 0.5  hours) / 7  days</span>.</div>
              </div>
              <div class="step-box">
                <div class="step-num">3</div>
                <div class="step-text"><strong>Model Student Results:</strong>
                  <br>&bull; <em>Student Activity Profile:</em> Sleep: 8.5h (17 cells); School/Study: 7.0h (14 cells); Meals/Hygiene: 2.5h (5 cells); Sports/Hobbies: 2.5h (5 cells); Travel: 1.5h (3 cells); Leisure/Family: 2.0h (4 cells). Total = 24.0 hours (48 cells).
                  <br>&bull; <em>Comparison with Adults:</em> Adults show higher work hours (~9 hours), lower sleep (~6.5 to 7 hours), and negligible playtime.
                  <br>&bull; <em>Grade 8 School Timings Survey:</em> Most Indian schools operate between 6 to 7.5 hours daily (e.g., 8:00 AM to 2:00 PM in summer, or 9:30 AM to 4:00 PM in winter).
                </div>
              </div>
              <div class="step-box">
                <div class="step-num">4</div>
                <div class="step-text"><strong>Verification &amp; Check:</strong> All 48 cells sum to exactly 24 hours (1440 minutes), verifying complete coverage of daily routines.</div>
              </div>
              <div class="step-box">
                <div class="step-num">5</div>
                <div class="step-text"><strong>Concluding Statement:</strong> Activity strips provide a tactile, visual medium connecting arithmetic fractions to real-world time management.</div>
              </div>
            </div>
          </details>
        </div>

        <!-- FIO 3 Q14 -->
        <div class="solved-card">
          <div class="solved-title"><i class="fa-solid fa-calculator"></i> Exercise 14: Sunrise &amp; Sunset Graphs Across 4 Indian Locations (Book p. 131–132)</div>
          <p>
            Analyze the annual sunrise and sunset curves for 4 Indian locations:
            <br>(i) At which place does the sun rise earliest in January? What is the day length there?
            <br>(ii) Which place has the longest day length over the year?
            <br>(iii) Share observations on day length variations with latitude.
          </p>
          <details class="ans-box">
            <summary>View 5-Step Solution</summary>
            <div class="ans-content">
              <div class="step-box">
                <div class="step-num">1</div>
                <div class="step-text"><strong>Given Information &amp; Context:</strong> Four graph plots showing sunrise (bottom line) and sunset (top line) across 365 days for four locations in India spanning different latitudes and longitudes.</div>
              </div>
              <div class="step-box">
                <div class="step-num">2</div>
                <div class="step-text"><strong>Core Mathematical Principle:</strong>
                  <br>&bull; Day Length = <span class="math-inline">Sunset Time - Sunrise Time</span> (vertical distance between the two curves).
                  <br>&bull; Earth's axial tilt (23.5&deg;) causes higher latitude regions to experience extreme seasonal swings in day length.</div>
              </div>
              <div class="step-box">
                <div class="step-num">3</div>
                <div class="step-text"><strong>Step-by-Step Analysis:</strong>
                  <br>&bull; <strong>(i) Earliest Sunrise in January:</strong> Easternmost locations experience sunrise first due to Earth's rotation from west to east. In eastern India (e.g., eastern Assam/Arunachal Pradesh or Port Blair), the sun rises earliest in January (around 5:30 to 6:00 AM). Approximate day length in January is around <strong>10.5 to 11 hours</strong>.
                  <br>&bull; <strong>(ii) Longest Day Length over the Year:</strong> During the Summer Solstice (June 21), regions at the highest northern latitude experience the longest day length. <strong>Srinagar (Jammu &amp; Kashmir)</strong> records the longest summer day length in India (~14 hours and 25 minutes)!
                  <br>&bull; <strong>(iii) Latitudinal Observations:</strong> Near the equator (Kanyakumari), the sunrise and sunset lines are nearly parallel horizontal lines (day length is almost a constant 12 hours). In the far north (Srinagar), the lines diverge dramatically in June and pinch together in December.
                </div>
              </div>
              <div class="step-box">
                <div class="step-num">4</div>
                <div class="step-text"><strong>Verification &amp; Check:</strong> Astronomical ephemeris data confirms Srinagar has the highest day length variance (5 hours variation) while southern India varies by under 1 hour.</div>
              </div>
              <div class="step-box">
                <div class="step-num">5</div>
                <div class="step-text"><strong>Concluding Statement:</strong> Eastern locations experience earlier sunrises; northernmost latitudes experience the greatest daylight swings between summer and winter.</div>
              </div>
            </div>
          </details>
        </div>

        <!-- FIO 3 Q15 -->
        <div class="solved-card">
          <div class="solved-title"><i class="fa-solid fa-calculator"></i> Exercise 15: Moonrise and Moonset Rhythms over a Month (Book p. 132)</div>
          <p>
            The graph shows moonrise and moonset times over a calendar month:
            <br>(i) Find on what dates <strong>Amavasya (New Moon)</strong> and <strong>Purnima (Full Moon)</strong> occurred.
            <br>(ii) What patterns and regularities do you notice?
          </p>
          <details class="ans-box">
            <summary>View 5-Step Solution</summary>
            <div class="ans-content">
              <div class="step-box">
                <div class="step-num">1</div>
                <div class="step-text"><strong>Given Information &amp; Context:</strong> A 30-day plot tracking local moonrise and moonset clock times.</div>
              </div>
              <div class="step-box">
                <div class="step-num">2</div>
                <div class="step-text"><strong>Core Mathematical Principle:</strong>
                  <br>&bull; <strong>Amavasya (New Moon):</strong> Moon is in conjunction with the Sun. It rises around <strong>sunrise (~6:00 AM)</strong> and sets around <strong>sunset (~6:00 PM)</strong>.
                  <br>&bull; <strong>Purnima (Full Moon):</strong> Moon is in opposition to the Sun. It rises around <strong>sunset (~6:00 PM)</strong> and sets around <strong>sunrise (~6:00 AM)</strong>.</div>
              </div>
              <div class="step-box">
                <div class="step-num">3</div>
                <div class="step-text"><strong>Step-by-Step Analysis:</strong>
                  <br>&bull; <strong>(i) Locating Lunar Dates:</strong>
                  <br>- Search for the date where the Moonrise line crosses 6:00 AM (06:00) &rArr; That date is <strong>Amavasya (New Moon)</strong>.
                  <br>- Search for the date roughly 14–15 days later where Moonrise crosses 6:00 PM (18:00) &rArr; That date is <strong>Purnima (Full Moon)</strong>.
                  <br>&bull; <strong>(ii) Key Observations:</strong>
                  <br>1. The Moon rises approximately <strong>50 minutes later every single day</strong>! This causes the moonrise curve to slope steadily upward across the 24-hour scale.
                  <br>2. When moonrise passes midnight (24:00), it wraps around to 00:00, creating a sawtooth cyclic progression across successive weeks.
                </div>
              </div>
              <div class="step-box">
                <div class="step-num">4</div>
                <div class="step-text"><strong>Verification &amp; Check:</strong> Lunar orbital period is 29.53 days. Daily lag = <span class="math-inline">24  hours / 29.53 &approx; 48.7  minutes &approx; 50  minutes</span>. Mathematics matches celestial physics perfectly!</div>
              </div>
              <div class="step-box">
                <div class="step-num">5</div>
                <div class="step-text"><strong>Concluding Statement:</strong> Amavasya coincides with morning moonrise (~6 AM) and Purnima with evening moonrise (~6 PM), driven by the steady ~50-minute daily lunar revolution lag.</div>
              </div>
            </div>
          </details>
        </div>

        <!-- FIO 3 Q16: GAME OF HEX -->
        <div class="solved-card">
          <div class="solved-title"><i class="fa-solid fa-dice-d20"></i> Mathematical Exploration 16: The Strategic Geometry of Hex (Book p. 134)</div>
          <p>
            Hex is a two-player connection game on an 11 &times; 11 rhombus of hexagons.
            <br>(i) Explain the rules and winning condition.
            <br>(ii) Why can a game of Hex NEVER end in a draw? Explain John Nash's topological proof.
          </p>
          <details class="ans-box">
            <summary>View 5-Step Solution</summary>
            <div class="ans-content">
              <div class="step-box">
                <div class="step-num">1</div>
                <div class="step-text"><strong>Given Information &amp; Context:</strong> An 11 &times; 11 rhombus board containing 121 regular hexagonal cells. Two opposite edges are colored Blue; the other two opposite edges are colored Red.</div>
              </div>
              <div class="step-box">
                <div class="step-num">2</div>
                <div class="step-text"><strong>Core Mathematical Principle:</strong> Graph Theory and Topology: The Hex board is a planar graph where adjacent hexagons share edges. Two intersecting paths connecting opposite boundaries must intersect or mutually block.</div>
              </div>
              <div class="step-box">
                <div class="step-num">3</div>
                <div class="step-text"><strong>Step-by-Step Analysis &amp; Rules:</strong>
                  <br>&bull; <strong>Rules:</strong> Players take turns placing a colored stone on any unoccupied hexagon. Stones cannot be moved or removed once placed.
                  <br>&bull; <strong>Winning Condition:</strong> The first player to establish an unbroken chain of adjacent hexagons of their color connecting their two designated sides wins immediately.
                  <br>&bull; <strong>John Nash's "No Draws" Proof (1949):</strong>
                  <br>Suppose all 121 cells are filled without any empty spaces remaining.
                  <br>Could it happen that neither Blue nor Red has formed a connecting bridge?
                  <br><strong>No!</strong> Because the board is a closed rhombus, if Player 1 is prevented from connecting their sides, there must exist a continuous barrier blocking them. But in Hex, the only thing that can block Player 1 is a line of Player 2's stones! And because any complete barrier from one side of the board to the other connects Player 2's own designated borders, Player 2 has automatically won!
                </div>
              </div>
              <div class="step-box">
                <div class="step-num">4</div>
                <div class="step-text"><strong>Verification &amp; Check:</strong> This is a discrete version of the famous <em>Brouwer Fixed-Point Theorem</em> in algebraic topology. In fact, David Gale proved in 1979 that the Hex theorem is mathematically equivalent to Brouwer's fixed-point theorem!</div>
              </div>
              <div class="step-box">
                <div class="step-num">5</div>
                <div class="step-text"><strong>Concluding Statement:</strong> Hex is a mathematically pure strategy game where ties are impossible—one player is guaranteed to win every game.</div>
              </div>
            </div>
          </details>
        </div>
      </div>
    </section>
"""
