# -*- coding: utf-8 -*-
"""
Section 3 Module: Rapid Revision Fact & Formula/Law Bank
Class 8 Mathematics Chapter 12: Tales by Dots and Lines (NCERT NEP code: hegp112)
"""

def get_section_3():
    return """
    <!-- SECTION 3: RAPID REVISION FACT & FORMULA BANK -->
    <section id="section3" class="section-box">
      <div class="section-header">
        <div class="section-header-left">
          <span class="section-tag">Quick Reference Vault</span>
          <h2 class="section-title">§ 3. Rapid Revision Fact &amp; Formula/Law Bank</h2>
          <p class="section-desc">
            Complete, high-density structured tables consolidating all statistical theorems, algebraic transformation invariants, spreadsheet formulas, and graph selection criteria for rapid exam revision.
          </p>
        </div>
        <div>
          <span class="badge badge-gold"><i class="fa-solid fa-bolt"></i> 5 Master Tables</span>
        </div>
      </div>

      <!-- TABLE 3.1: MASTER FORMULAS & THEOREMS -->
      <div class="concept-card">
        <h3 class="concept-card-title"><i class="fa-solid fa-square-root-variable"></i> Table 3.1: Master Statistical Formulas &amp; Transformation Laws</h3>
        <p>Core algebraic equations governing central tendency and linear transformations:</p>
        
        <div class="table-container">
          <table>
            <thead>
              <tr>
                <th style="width: 20%;">Concept / Property</th>
                <th style="width: 25%;">Standard Mathematical Formula</th>
                <th style="width: 30%;">Variable Meaning / Conditions</th>
                <th style="width: 25%;">Concrete Numerical Example</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>Arithmetic Mean (Ungrouped)</strong></td>
                <td><span class="math-inline">x̄ = (&Sigma; x_i) / n</span></td>
                <td>Sum of all individual values divided by count of values <span class="math-inline">n</span>.</td>
                <td>Data {3, 7}: <br><span class="math-inline">x̄ = (3 + 7)/2 = 5</span></td>
              </tr>
              <tr>
                <td><strong>The Fulcrum Condition (Zero Net Deviation)</strong></td>
                <td><span class="math-inline">&Sigma; (x_i - x̄) = 0</span><br><span class="math-inline">&Sigma; d_left = &Sigma; d_right</span></td>
                <td>Total distance of values to the left of the mean equals total distance to the right.</td>
                <td>Data {10, 10, 11, 17}, mean=12:<br>Left: 2+2+1 = 5; Right: 5</td>
              </tr>
              <tr>
                <td><strong>Linear Shifting (Addition)</strong></td>
                <td><span class="math-inline">x'ᵢ = xᵢ + c &rArr; x̄' = x̄ + c</span></td>
                <td>Adding a constant <span class="math-inline">c</span> to every value shifts the mean by <span class="math-inline">c</span>.</td>
                <td>If mean is 150.2 cm, removing 1 cm shoes: <span class="math-inline">150.2 - 1 = 149.2 cm</span></td>
              </tr>
              <tr>
                <td><strong>Linear Shifting (Subtraction)</strong></td>
                <td><span class="math-inline">x'ᵢ = xᵢ - c &rArr; x̄' = x̄ - c</span></td>
                <td>Subtracting constant <span class="math-inline">c</span> from every value reduces mean by <span class="math-inline">c</span>.</td>
                <td>Data {8, 12}, x̄=10; subtract 2: {6, 10}, x̄'=8</td>
              </tr>
              <tr>
                <td><strong>Uniform Scaling (Multiplication)</strong></td>
                <td><span class="math-inline">x'ᵢ = k&middot;xᵢ &rArr; x̄' = k &times; x̄</span></td>
                <td>Multiplying every value by factor <span class="math-inline">k</span> scales the mean by <span class="math-inline">k</span>.</td>
                <td>If scores double (<span class="math-inline">k=2</span>) with old mean 24, new mean = <span class="math-inline">24 &times; 2 = 48</span></td>
              </tr>
              <tr>
                <td><strong>Uniform Scaling (Division)</strong></td>
                <td><span class="math-inline">x'ᵢ = xᵢ / k &rArr; x̄' = x̄ / k</span></td>
                <td>Dividing every value by <span class="math-inline">k &ne; 0</span> divides the mean by <span class="math-inline">k</span>.</td>
                <td>Converting grams to kg: <span class="math-inline">x̄_kg = x̄_g / 1000</span></td>
              </tr>
              <tr>
                <td><strong>Combined Linear Form</strong></td>
                <td><span class="math-inline">yᵢ = a&middot;xᵢ + b &rArr; ȳ = a&middot;x̄ + b</span></td>
                <td>General linear mapping preserves mean under slope and intercept.</td>
                <td>Celsius to Fahrenheit: <br><span class="math-inline">T̄_F = (9/5) T̄_C + 32</span></td>
              </tr>
              <tr>
                <td><strong>Median (Odd N)</strong></td>
                <td><span class="math-inline">Median = [(N + 1) / 2]ᵗʰ</span> value</td>
                <td>Direct middle observation of ordered data.</td>
                <td>{4, 7, <strong>9</strong>, 11, 15}: N=5 &rArr; 3rd value = 9</td>
              </tr>
              <tr>
                <td><strong>Median (Even N)</strong></td>
                <td><span class="math-inline">Median = [Val(N/2) + Val(N/2 + 1)] / 2</span></td>
                <td>Arithmetic average of the two central sorted values.</td>
                <td>{2, 5, <strong>8, 12</strong>, 16, 20}: <br>Median = (8 + 12)/2 = 10</td>
              </tr>
              <tr>
                <td><strong>Weighted Mean (Frequency Table)</strong></td>
                <td><span class="math-inline">x̄ = (&Sigma; f_i&middot;x_i) / (&Sigma; f_i)</span></td>
                <td>Sum of frequency-weighted values divided by total count <span class="math-inline">N = &Sigma; f</span>.</td>
                <td>Family sizes: &Sigma;fx = 188, &Sigma;f = 36 &rArr; <span class="math-inline">x̄ = 188 / 36 &approx; 5.22</span></td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>

      <!-- TABLE 3.2: SENSITIVITY & BEHAVIOR MATRIX -->
      <div class="concept-card">
        <h3 class="concept-card-title"><i class="fa-solid fa-arrows-spin"></i> Table 3.2: Data Mutation &amp; Sensitivity Response Matrix</h3>
        <p>A comprehensive behavior guide showing how central tendencies react when datasets are modified:</p>

        <div class="table-container">
          <table>
            <thead>
              <tr>
                <th style="width: 25%;">Data Alteration Event</th>
                <th style="width: 22%;">Impact on Arithmetic Mean (x̄)</th>
                <th style="width: 22%;">Impact on Median</th>
                <th style="width: 31%;">Physical / Geometric Reason</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>Include value &gt; old mean</strong></td>
                <td><span class="badge badge-emerald"><i class="fa-solid fa-arrow-up"></i> Increases</span></td>
                <td>Increases or Stays Same</td>
                <td>Adds torque to the RHS arm of the seesaw; fulcrum must shift right.</td>
              </tr>
              <tr>
                <td><strong>Include value &lt; old mean</strong></td>
                <td><span class="badge badge-gold"><i class="fa-solid fa-arrow-down"></i> Decreases</span></td>
                <td>Decreases or Stays Same</td>
                <td>Adds torque to the LHS arm; fulcrum must shift left.</td>
              </tr>
              <tr>
                <td><strong>Include value = old mean</strong></td>
                <td><span class="badge badge-primary"><i class="fa-solid fa-minus"></i> Unchanged</span></td>
                <td>May shift slightly or stay same</td>
                <td>New weight sits directly on top of the fulcrum (distance = 0).</td>
              </tr>
              <tr>
                <td><strong>Remove value &gt; old mean</strong></td>
                <td><span class="badge badge-gold"><i class="fa-solid fa-arrow-down"></i> Decreases</span></td>
                <td>Decreases or Stays Same</td>
                <td>Removing right-side weight tilts board left; fulcrum must slide left.</td>
              </tr>
              <tr>
                <td><strong>Remove value &lt; old mean</strong></td>
                <td><span class="badge badge-emerald"><i class="fa-solid fa-arrow-up"></i> Increases</span></td>
                <td>Increases or Stays Same</td>
                <td>Removing left-side weight tilts board right; fulcrum must slide right.</td>
              </tr>
              <tr>
                <td><strong>Remove value = old mean</strong></td>
                <td><span class="badge badge-primary"><i class="fa-solid fa-minus"></i> Unchanged</span></td>
                <td>May shift slightly or stay same</td>
                <td>Removing zero-torque pivot weight leaves balance unaffected.</td>
              </tr>
              <tr>
                <td><strong>Add extreme massive outlier</strong></td>
                <td><span class="badge badge-gold"><i class="fa-solid fa-explosion"></i> Massive Increase</span></td>
                <td><span class="badge badge-emerald"><i class="fa-solid fa-shield"></i> Highly Robust</span></td>
                <td>Mean accounts for exact numerical magnitude; median only cares about rank order.</td>
              </tr>
              <tr>
                <td><strong>Include multiple values with &Sigma;(x_new - x̄) = 0</strong></td>
                <td><span class="badge badge-primary"><i class="fa-solid fa-equals"></i> Strictly Unchanged</span></td>
                <td>May shift or stay same</td>
                <td>Left deviations of added values exactly cancel right deviations!</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>

      <!-- TABLE 3.3: DATA VISUALIZATION SELECTOR -->
      <div class="concept-card">
        <h3 class="concept-card-title"><i class="fa-solid fa-chart-pie"></i> Table 3.3: Data Visualization Tool Selector</h3>
        <p>Choosing the perfect visual representation for various mathematical and real-world scenarios:</p>

        <div class="table-container">
          <table>
            <thead>
              <tr>
                <th style="width: 18%;">Visualization Type</th>
                <th style="width: 25%;">When to Use (Best Context)</th>
                <th style="width: 25%;">Key Advantages</th>
                <th style="width: 32%;">Textbook Chapter Example</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>Dot Plot</strong></td>
                <td>Small to medium discrete datasets (N &lt; 50) on a single numerical scale.</td>
                <td>Preserves individual raw data points; instantly displays clusters, gaps, and fulcrum balance.</td>
                <td>Song lengths in albums, missing value balance at x̄=9, bicycle ride frequency.</td>
              </tr>
              <tr>
                <td><strong>Clustered Column Graph</strong></td>
                <td>Comparing 2 to 3 discrete categories across a limited number of groups (e.g., 2 to 4 months).</td>
                <td>Direct side-by-side bar height comparison for discrete categorical groups.</td>
                <td>Comparing male vs female literacy across 4 districts. (Fails when time points exceed 6!).</td>
              </tr>
              <tr>
                <td><strong>Line Graph (Time Series)</strong></td>
                <td>Continuous or ordered progression across chronological time (months, years, ages).</td>
                <td>Lightweight, avoids bar clutter; slope directly reveals rate of change and temporal trends.</td>
                <td>Kerala vs Punjab monthly temperatures, space rocket launches 2012–2024, iodised salt prices.</td>
              </tr>
              <tr>
                <td><strong>24-Hour Activity Strip</strong></td>
                <td>Visualizing personal daily routines, sleep schedules, or school timetables across 24 hours.</td>
                <td>Transforms continuous daily time into intuitive color-coded ribbons (e.g., 48 half-hour cells).</td>
                <td>Manoj's weekday vs weekend activity strip (sleep, study, meals, transit, sports).</td>
              </tr>
              <tr>
                <td><strong>Choropleth Map / Infographic</strong></td>
                <td>Geographic spatial distributions and regional lifestyle preferences across states.</td>
                <td>Provides immediate spatial pattern recognition using color gradients.</td>
                <td>State-wise Rice vs Wheat per capita preference map with clear north-south geographical split.</td>
              </tr>
              <tr>
                <td><strong>Hexagonal Board (Hex)</strong></td>
                <td>Connection game analysis and network graph topology.</td>
                <td>Demonstrates mathematical parity, topological path connectivity, and no-draw game theory.</td>
                <td>Piet Hein and John Nash's 11 &times; 11 Rhombus Game of Hex.</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>

      <!-- TABLE 3.4: SPREADSHEET REFERENCE SHEET -->
      <div class="concept-card">
        <h3 class="concept-card-title"><i class="fa-solid fa-table-cells"></i> Table 3.4: Digital Spreadsheet Syntax &amp; Formula Master Sheet</h3>
        <p>Essential functions and range expressions used in modern spreadsheet analysis:</p>

        <div class="table-container">
          <table>
            <thead>
              <tr>
                <th style="width: 18%;">Function Name</th>
                <th style="width: 22%;">Standard Syntax</th>
                <th style="width: 25%;">Range Example</th>
                <th style="width: 35%;">Practical Classroom Application</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>SUM</strong></td>
                <td><span class="math-inline">=SUM(StartCell:EndCell)</span></td>
                <td><span class="math-inline">=SUM(B5:G5)</span></td>
                <td>Calculates the total aggregate marks scored by a student across all 6 academic subjects.</td>
              </tr>
              <tr>
                <td><strong>AVERAGE</strong></td>
                <td><span class="math-inline">=AVERAGE(StartCell:EndCell)</span></td>
                <td><span class="math-inline">=AVERAGE(F3:F24)</span></td>
                <td>Calculates the class average score for Mathematics across all 22 students in Grade 8.</td>
              </tr>
              <tr>
                <td><strong>COUNT</strong></td>
                <td><span class="math-inline">=COUNT(StartCell:EndCell)</span></td>
                <td><span class="math-inline">=COUNT(B3:B24)</span></td>
                <td>Counts the number of students who appeared for the Odia midterm examination.</td>
              </tr>
              <tr>
                <td><strong>MAX</strong></td>
                <td><span class="math-inline">=MAX(StartCell:EndCell)</span></td>
                <td><span class="math-inline">=MAX(E3:E24)</span></td>
                <td>Identifies the highest score obtained in English across the entire grade.</td>
              </tr>
              <tr>
                <td><strong>MIN</strong></td>
                <td><span class="math-inline">=MIN(StartCell:EndCell)</span></td>
                <td><span class="math-inline">=MIN(G3:G24)</span></td>
                <td>Finds the minimum mark scored in Social Science for remedial intervention planning.</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>

      <!-- TABLE 3.5: REAL-WORLD CASE STUDY SYNTHESIS -->
      <div class="concept-card">
        <h3 class="concept-card-title"><i class="fa-solid fa-earth-asia"></i> Table 3.5: Real-World NCERT Case Study Synthesis</h3>
        <p>Key takeaways from the rich empirical data investigations featured in Chapter 12:</p>

        <div class="table-container">
          <table>
            <thead>
              <tr>
                <th style="width: 20%;">Case Investigation</th>
                <th style="width: 25%;">Empirical Dataset</th>
                <th style="width: 25%;">Key Mathematical Observation</th>
                <th style="width: 30%;">Conceptual / Geographic Takeaway</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>Punjab vs Kerala Temperatures</strong></td>
                <td>Monthly maximum temperatures in 2023 across 12 months.</td>
                <td>Punjab fluctuates widely (19&deg;C to 38&deg;C); Kerala stays remarkably flat (29&deg;C to 33&deg;C).</td>
                <td>Maritime influence moderates coastal temperatures (high specific heat of sea) vs extreme continental inland climate.</td>
              </tr>
              <tr>
                <td><strong>Space Jam (Launches 2012–2024)</strong></td>
                <td>Annual count of objects launched into Earth orbit by USA, China, Russia, and World.</td>
                <td>Global launches surged from &lt;200 to ~2,900; slope steepened dramatically after 2019.</td>
                <td>USA launched ~3/4 of all objects in 2022–2024 due to private commercial satellite megaconstellations (e.g., Starlink).</td>
              </tr>
              <tr>
                <td><strong>Indian Coastal Rainfall Regimes</strong></td>
                <td>Monthly rainfall days in Mumbai, Udupi, Kovalam, Chennai, Puri, Rameswaram.</td>
                <td>West coast peaks intensely in June–August; Coromandel east coast peaks in October–December.</td>
                <td>Southwest Monsoon drenches the Western Ghats; Retreating Northeast Monsoon delivers rain to Tamil Nadu coast.</td>
              </tr>
              <tr>
                <td><strong>Rice vs Wheat Consumption Map</strong></td>
                <td>Per capita staple grain difference index across Indian states (-100 to +100).</td>
                <td>A distinct red boundary line splits India into a rice-dominant South/East and wheat-dominant North/West.</td>
                <td>Agricultural cropping patterns (alluvial wet soils vs dry black/loamy soils) dictate traditional culinary staples.</td>
              </tr>
              <tr>
                <td><strong>The "Sleepy-Deepy" Lifespan Curve</strong></td>
                <td>Daily sleep duration data points across ages 6 to 75.</td>
                <td>6-year-olds sleep ~9.6 hours; dips to ~7.8 hours in working adulthood (30–45); rises to ~8.5 hours in seniors.</td>
                <td>Sleep is non-linear across life; plotting 80 points with a smooth line graph prevents the clutter of 70 separate bar columns.</td>
              </tr>
              <tr>
                <td><strong>Astronomical Solar &amp; Lunar Cycles</strong></td>
                <td>Sunrise/sunset times over 365 days; moonrise/moonset times over 30 days.</td>
                <td>Sun rises and sets with 24-hr regularity; Moon rises ~50 minutes later every single day.</td>
                <td>Amavasya occurs when Moon rises at sunrise and sets at sunset; Purnima occurs when Moon rises at sunset and sets at sunrise.</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </section>
"""
