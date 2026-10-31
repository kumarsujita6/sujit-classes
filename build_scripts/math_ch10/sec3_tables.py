# -*- coding: utf-8 -*-
"""
Section 3: Rapid Revision Fact & Formula/Law Bank
Class 8 Mathematics Chapter 10: Proportional Reasoning - 2
"""

def get_section_3():
    return """
    <!-- ==========================================================
         SECTION 3: RAPID REVISION FACT & FORMULA/LAW BANK
         ========================================================== -->
    <section id="section3" class="section-box">
      <div class="section-header">
        <div class="section-header-left">
          <span class="section-tag"><i class="fa-solid fa-table-list"></i> Summary Tables &amp; Laws</span>
          <h2 class="section-title">Section 3: Rapid Revision Fact &amp; Formula/Law Bank</h2>
          <p class="section-desc">
            High-yield comparative tables, algebraic formulas, cartographic conversion matrices, and mental math shortcuts compiled for instant exam recall.
          </p>
        </div>
      </div>

      <!-- Master Comparison Table: Direct vs Inverse Proportion -->
      <div class="concept-card">
        <h3 class="concept-card-title"><i class="fa-solid fa-code-compare"></i> Master Comparison Matrix: Direct vs. Inverse Proportion</h3>
        <p>
          Memorise this fundamental dichotomy. Recognizing whether a physical problem behaves according to direct or inverse variation is the single most critical step in solving proportional reasoning questions!
        </p>

        <div class="data-table-wrapper">
          <table class="data-table">
            <thead>
              <tr>
                <th style="width: 18%;">Feature / Dimension</th>
                <th style="width: 41%;">Direct Proportion (ସରଳ ସମାନୁପାତ)</th>
                <th style="width: 41%;">Inverse Proportion (ବ୍ୟସ୍ତ ସମାନୁପାତ)</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>Core Verbal Definition</strong></td>
                <td>As one quantity increases, the other quantity increases by the <strong>exact same multiplying factor</strong>.</td>
                <td>As one quantity increases, the other quantity decreases by the <strong>exact reciprocal factor</strong>.</td>
              </tr>
              <tr>
                <td><strong>Governing Algebraic Formula</strong></td>
                <td><code class="math-inline">x / y = k</code> &nbsp;(or <code class="math-inline">y = k · x</code>)</td>
                <td><code class="math-inline">x · y = k</code> &nbsp;(or <code class="math-inline">y = k / x</code>)</td>
              </tr>
              <tr>
                <td><strong>Invariant Mathematical Property</strong></td>
                <td>The <strong>QUOTIENT (Ratio)</strong> remains strictly constant: <code class="math-inline">x₁ / y₁ = x₂ / y₂</code></td>
                <td>The <strong>PRODUCT</strong> remains strictly constant: <code class="math-inline">x₁ · y₁ = x₂ · y₂</code></td>
              </tr>
              <tr>
                <td><strong>Pairwise Proportion Statement</strong></td>
                <td><code class="math-inline">x₁ / x₂ = y₁ / y₂</code> &nbsp;(Direct equality of ratios)</td>
                <td><code class="math-inline">x₁ / x₂ = y₂ / y₁</code> &nbsp;(Reciprocal flip of y-ratio)</td>
              </tr>
              <tr>
                <td><strong>Graphical Geometric Curve</strong></td>
                <td>A <strong>straight line ray</strong> originating from or passing through the origin <code>(0, 0)</code>.</td>
                <td>A smooth curving <strong>rectangular hyperbola</strong> asymptotic to both axes (never touches 0).</td>
              </tr>
              <tr>
                <td><strong>Visual Meaning of Constant k</strong></td>
                <td>The <strong>gradient / slope</strong> of the straight ray: <code class="math-inline">k = Δy / Δx</code>.</td>
                <td>The <strong>area of the rectangle</strong> formed under any point on the curve: <code class="math-inline">Area = x · y = k</code>.</td>
              </tr>
              <tr>
                <td><strong>Canonical Real-World Examples</strong></td>
                <td>
                  • Pencils bought vs. total cost paid.<br>
                  • Kilometers driven vs. litres of petrol consumed.<br>
                  • Height of an object vs. length of its cast shadow.<br>
                  • Total pages in a book vs. reading time at steady speed.
                </td>
                <td>
                  • Speed of travel vs. time taken for a fixed journey.<br>
                  • Number of workers hired vs. days to finish a fixed job.<br>
                  • Number of water pipes filling vs. hours to fill a cistern.<br>
                  • Number of hostellers sharing grain vs. days provisions last.
                </td>
              </tr>
              <tr>
                <td><strong>Standard Exam Hall Trap</strong></td>
                <td>Assuming that "both quantities increase" guarantees direct proportion (e.g., age and height increase, but NOT proportionally!).</td>
                <td>Attempting to use direct cross-multiplication (<code class="math-inline">x₁ · y₂ = x₂ · y₁</code>) instead of constant product (<code class="math-inline">x₁ · y₁ = x₂ · y₂</code>).</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>

      <!-- Formula Master Deck -->
      <div class="concept-card">
        <h3 class="concept-card-title"><i class="fa-solid fa-calculator"></i> The Master Formula Deck</h3>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 1.25rem;">
          
          <!-- Card 1 -->
          <div style="background: #f0f9ff; border: 1px solid #bae6fd; border-radius: 12px; padding: 1.25rem;">
            <h4 style="color: #0369a1; font-size: 1rem; margin-bottom: 0.5rem;"><i class="fa-solid fa-arrows-split-up-and-left"></i> 1. Direct Proportion (Trairāśika)</h4>
            <div class="math-block" style="font-size: 0.95rem; margin: 0.5rem 0;">
              x₁ / y₁ = x₂ / y₂ &nbsp;⇒&nbsp; x₁ · y₂ = x₂ · y₁
            </div>
            <p style="font-size: 0.825rem; color: #0c4a6e; margin-bottom: 0;">
              Finding the fourth unknown: <code>y₂ = (x₂ · y₁) / x₁</code>.
            </p>
          </div>

          <!-- Card 2 -->
          <div style="background: #f0fdfa; border: 1px solid #ccfbf1; border-radius: 12px; padding: 1.25rem;">
            <h4 style="color: #0f766e; font-size: 1rem; margin-bottom: 0.5rem;"><i class="fa-solid fa-arrows-turn-to-dots"></i> 2. Inverse Proportion (Constant Product)</h4>
            <div class="math-block" style="font-size: 0.95rem; margin: 0.5rem 0;">
              x₁ · y₁ = x₂ · y₂ &nbsp;⇒&nbsp; y₂ = (x₁ · y₁) / x₂
            </div>
            <p style="font-size: 0.825rem; color: #134e4a; margin-bottom: 0;">
              Product of initial pair divided by the new primary variable.
            </p>
          </div>

          <!-- Card 3 -->
          <div style="background: #fefce8; border: 1px solid #fef08a; border-radius: 12px; padding: 1.25rem;">
            <h4 style="color: #854d0e; font-size: 1rem; margin-bottom: 0.5rem;"><i class="fa-solid fa-cubes-stacked"></i> 3. Multi-Term Ratio Expansion</h4>
            <div class="math-block" style="font-size: 0.95rem; margin: 0.5rem 0;">
              a : b : c : d :: p : q : r : s &nbsp;⇒&nbsp; a/p = b/q = c/r = d/s = k
            </div>
            <p style="font-size: 0.825rem; color: #713f12; margin-bottom: 0;">
              Every corresponding term pairs to the identical scale factor k.
            </p>
          </div>

          <!-- Card 4 -->
          <div style="background: #fdf2f8; border: 1px solid #fbcfe8; border-radius: 12px; padding: 1.25rem;">
            <h4 style="color: #9d174d; font-size: 1rem; margin-bottom: 0.5rem;"><i class="fa-solid fa-chart-pie"></i> 4. Pie Chart Central Sector Angle</h4>
            <div class="math-block" style="font-size: 0.95rem; margin: 0.5rem 0;">
              θ = (Frequency f / Total N) × 360° = (% / 100) × 360°
            </div>
            <p style="font-size: 0.825rem; color: #831843; margin-bottom: 0;">
              Converts discrete frequency counts or percentages into protractor degrees.
            </p>
          </div>

          <!-- Card 5 -->
          <div style="background: #f5f3ff; border: 1px solid #ddd6fe; border-radius: 12px; padding: 1.25rem;">
            <h4 style="color: #5b21b6; font-size: 1rem; margin-bottom: 0.5rem;"><i class="fa-solid fa-map"></i> 5. Cartographic Ground Distance</h4>
            <div class="math-block" style="font-size: 0.95rem; margin: 0.5rem 0;">
              Actual Ground Dist = Map Distance (cm) × Scale Factor (N)
            </div>
            <p style="font-size: 0.825rem; color: #4c1d95; margin-bottom: 0;">
              For RF 1:60,00,000: <code>Ground km = (Map cm × 60,00,000) ÷ 1,00,000 = Map cm × 60</code>.
            </p>
          </div>

          <!-- Card 6 -->
          <div style="background: #ecfdf5; border: 1px solid #a7f3d0; border-radius: 12px; padding: 1.25rem;">
            <h4 style="color: #065f46; font-size: 1rem; margin-bottom: 0.5rem;"><i class="fa-solid fa-user-group"></i> 6. Combined Collaborative Work</h4>
            <div class="math-block" style="font-size: 0.95rem; margin: 0.5rem 0;">
              1 / T_total = 1 / t₁ + 1 / t₂ &nbsp;⇒&nbsp; T_total = (t₁ · t₂) / (t₁ + t₂)
            </div>
            <p style="font-size: 0.825rem; color: #047857; margin-bottom: 0;">
              Harmonic combination rule for two workers or two inflow pumps.
            </p>
          </div>

        </div>
      </div>

      <!-- Mental Math Multiplier & Benchmark Table -->
      <div class="concept-card">
        <h3 class="concept-card-title"><i class="fa-solid fa-bolt"></i> Speed Benchmark &amp; Angle Conversion Table for Pie Charts</h3>
        <p>
          Instantly convert standard percentages and fractions to circular degrees without pen-and-paper calculation:
        </p>

        <div class="data-table-wrapper">
          <table class="data-table">
            <thead>
              <tr>
                <th>Fraction of Whole</th>
                <th>Decimal Equivalent</th>
                <th>Percentage (%)</th>
                <th>Central Sector Angle (θ)</th>
                <th>Visual Sector Appearance</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>1 / 1</strong></td>
                <td>1.00</td>
                <td>100%</td>
                <td><strong>360°</strong></td>
                <td>Complete full circle</td>
              </tr>
              <tr>
                <td><strong>1 / 2</strong></td>
                <td>0.50</td>
                <td>50%</td>
                <td><strong>180°</strong></td>
                <td>Exact semicircle (straight diameter)</td>
              </tr>
              <tr>
                <td><strong>1 / 3</strong></td>
                <td>0.333...</td>
                <td>33.33%</td>
                <td><strong>120°</strong></td>
                <td>One-third circle (peace sign third)</td>
              </tr>
              <tr>
                <td><strong>1 / 4</strong></td>
                <td>0.25</td>
                <td>25%</td>
                <td><strong>90°</strong></td>
                <td>Exact quadrant (perpendicular right angle)</td>
              </tr>
              <tr>
                <td><strong>1 / 5</strong></td>
                <td>0.20</td>
                <td>20%</td>
                <td><strong>72°</strong></td>
                <td>One-fifth circle (pentagon sector)</td>
              </tr>
              <tr>
                <td><strong>1 / 6</strong></td>
                <td>0.166...</td>
                <td>16.67%</td>
                <td><strong>60°</strong></td>
                <td>Equilateral triangle sector</td>
              </tr>
              <tr>
                <td><strong>1 / 8</strong></td>
                <td>0.125</td>
                <td>12.5%</td>
                <td><strong>45°</strong></td>
                <td>Half a right angle</td>
              </tr>
              <tr>
                <td><strong>1 / 10</strong></td>
                <td>0.10</td>
                <td>10%</td>
                <td><strong>36°</strong></td>
                <td>One-tenth circle</td>
              </tr>
              <tr>
                <td><strong>1 / 12</strong></td>
                <td>0.0833...</td>
                <td>8.33%</td>
                <td><strong>30°</strong></td>
                <td>Single hour on 12-hour clock face</td>
              </tr>
              <tr>
                <td><strong>1 / 20</strong></td>
                <td>0.05</td>
                <td>5%</td>
                <td><strong>18°</strong></td>
                <td>Slim slice</td>
              </tr>
              <tr>
                <td><strong>1 / 36</strong></td>
                <td>0.0277...</td>
                <td>2.78%</td>
                <td><strong>10°</strong></td>
                <td>Narrow sliver</td>
              </tr>
              <tr>
                <td><strong>1 / 360</strong></td>
                <td>0.00277...</td>
                <td>0.278%</td>
                <td><strong>1°</strong></td>
                <td>Single degree graduation mark</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>

      <!-- Unit Conversion Master Matrix -->
      <div class="concept-card">
        <h3 class="concept-card-title"><i class="fa-solid fa-arrows-split-up-and-left"></i> Cartography &amp; Time Unit Conversion Matrix</h3>
        <div class="data-table-wrapper">
          <table class="data-table">
            <thead>
              <tr>
                <th>Conversion Target</th>
                <th>Standard Metric Equation</th>
                <th>Proportional Scale Application</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>Centimetres to Metres</strong></td>
                <td><code>1 m = 100 cm</code> &nbsp;(Divide cm by 100)</td>
                <td>Used when scaling classroom blueprints (e.g., 50 cm = 0.5 m).</td>
              </tr>
              <tr>
                <td><strong>Metres to Kilometres</strong></td>
                <td><code>1 km = 1,000 m</code> &nbsp;(Divide m by 1,000)</td>
                <td>Used to translate intermediate surveyor meters into geographical kilometers.</td>
              </tr>
              <tr>
                <td><strong>Centimetres to Kilometres</strong></td>
                <td><code>1 km = 1,00,000 cm</code> &nbsp;(Divide cm by 10⁵)</td>
                <td><strong>Master Cartographic Key:</strong> To convert map cm with RF 1:N to real km, compute: <code>km = (Map cm × N) ÷ 1,00,000</code>.</td>
              </tr>
              <tr>
                <td><strong>Hours to Minutes</strong></td>
                <td><code>1 hour = 60 minutes</code> &nbsp;(Multiply hours by 60)</td>
                <td>Used to convert fractional hour solutions (e.g., <code>3/5 hour = 36 min</code>; <code>1.5 hours = 90 min</code>).</td>
              </tr>
              <tr>
                <td><strong>Speed: km/h to m/s</strong></td>
                <td><code>1 km/h = (1,000 m) / (3,600 s) = 5/18 m/s</code></td>
                <td>Multiply speed in km/h by <code>5/18</code> to obtain metric physics speed in m/s.</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </section>
"""
