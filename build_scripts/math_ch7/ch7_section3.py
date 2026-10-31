# -*- coding: utf-8 -*-
"""
Module: ch7_section3.py
Contains Section 3: Rapid Revision Fact & Formula/Law Bank with 6 comprehensive
structured reference tables and quick-revision formula cards.
"""

def get_section3():
    return """
    <!-- ========================================== -->
    <!-- SECTION 3: RAPID REVISION FORMULA BANK     -->
    <!-- ========================================== -->
    <section id="section3">
      <div class="section-header">
        <div class="section-tag"><i class="fa-solid fa-table-list"></i> Mathematical Formula Vault</div>
        <h2 class="section-title">Section 3: Rapid Revision Fact &amp; Formula/Law Bank</h2>
        <p class="section-desc">
          Structured reference tables summarizing every definition, algebraic law, ancient Trairāśika identity, group sharing formula, and unit conversion metric required for CBSE and BSE examinations.
        </p>
      </div>

      <!-- TABLE 1: CORE DEFINITIONS & AXIOMS -->
      <h3 class="subheading"><i class="fa-solid fa-shapes"></i> Table 3.1: Fundamental Definitions &amp; Axiomatic Laws</h3>
      <div class="table-container">
        <table class="data-table">
          <thead>
            <tr>
              <th>Concept / Term</th>
              <th>Symbolic Notation</th>
              <th>Mathematical Definition</th>
              <th>Governing Condition / Invariant Property</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>Ratio</strong></td>
              <td><em>a : b</em> or <em>a / b</em></td>
              <td>Quotient of quantity <em>a</em> divided by quantity <em>b</em> of the same kind.</td>
              <td><em>b ≠ 0</em>; units must match; dimensionless number.</td>
            </tr>
            <tr>
              <td><strong>Antecedent</strong></td>
              <td><em>a</em> in <em>a : b</em></td>
              <td>The first term or numerator of the comparison.</td>
              <td>Order matters: <em>a : b ≠ b : a</em> (unless <em>a = b</em>).</td>
            </tr>
            <tr>
              <td><strong>Consequent</strong></td>
              <td><em>b</em> in <em>a : b</em></td>
              <td>The second term or denominator of the comparison.</td>
              <td>Cannot be zero (division by zero is undefined).</td>
            </tr>
            <tr>
              <td><strong>Equivalent Ratios</strong></td>
              <td><em>a : b = ka : kb</em></td>
              <td>Ratios formed by scaling both terms by a non-zero multiplier <em>k</em>.</td>
              <td><em>k ≠ 0</em>. Preserves fractional value.</td>
            </tr>
            <tr>
              <td><strong>Simplest Form</strong></td>
              <td><em>(a ÷ g) : (b ÷ g)</em></td>
              <td>Reduced ratio where <em>g = HCF(a, b)</em> and <em>HCF(a', b') = 1</em>.</td>
              <td>Terms are mutually co-prime integers.</td>
            </tr>
            <tr>
              <td><strong>Proportion</strong></td>
              <td><em>a : b :: c : d</em></td>
              <td>Statement expressing equality of two ratios: <em>a / b = c / d</em>.</td>
              <td>Read: "<em>a is to b as c is to d</em>".</td>
            </tr>
            <tr>
              <td><strong>Extremes &amp; Means</strong></td>
              <td><em>a, d</em> (Extremes)<br><em>b, c</em> (Means)</td>
              <td>Extremes are the outer terms; Means are the inner terms.</td>
              <td>Fundamental Law: <em>a × d = b × c</em>.</td>
            </tr>
            <tr>
              <td><strong>Direct Variation</strong></td>
              <td><em>y ∝ x</em> or <em>y = kx</em></td>
              <td>Quantities increase or decrease together at a constant rate <em>k</em>.</td>
              <td>Ratio <em>y / x = k</em> (Constant of Proportionality).</td>
            </tr>
            <tr>
              <td><strong>Inverse Variation</strong></td>
              <td><em>y ∝ 1/x</em> or <em>xy = C</em></td>
              <td>An increase in <em>x</em> causes a proportional decrease in <em>y</em>.</td>
              <td>Product <em>x × y = C</em> (Constant Product).</td>
            </tr>
          </tbody>
        </table>
      </div>

      <!-- TABLE 2: TRAIRĀŚIKA & CROSS-MULTIPLICATION MATRIX -->
      <h3 class="subheading"><i class="fa-solid fa-calculator"></i> Table 3.2: Trairāśika &amp; Missing Term Calculation Matrix</h3>
      <div class="table-container">
        <table class="data-table">
          <thead>
            <tr>
              <th>Missing Term</th>
              <th>Proportion Setup</th>
              <th>Cross-Multiplication Equation</th>
              <th>Direct Solution Formula</th>
              <th>Trairāśika Sanskrit Mapping</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>Fourth Term (d)</strong></td>
              <td><em>a : b :: c : d</em></td>
              <td><em>a × d = b × c</em></td>
              <td><strong style="color: #4f46e5;">d = (b × c) ÷ a</strong></td>
              <td><em>Ichchhāphala = (Phala × Ichchhā) ÷ Pramāṇa</em></td>
            </tr>
            <tr>
              <td><strong>Third Term (c)</strong></td>
              <td><em>a : b :: c : d</em></td>
              <td><em>b × c = a × d</em></td>
              <td><strong style="color: #4f46e5;">c = (a × d) ÷ b</strong></td>
              <td><em>Ichchhā = (Pramāṇa × Ichchhāphala) ÷ Phala</em></td>
            </tr>
            <tr>
              <td><strong>Second Term (b)</strong></td>
              <td><em>a : b :: c : d</em></td>
              <td><em>b × c = a × d</em></td>
              <td><strong style="color: #4f46e5;">b = (a × d) ÷ c</strong></td>
              <td><em>Phala = (Pramāṇa × Ichchhāphala) ÷ Ichchhā</em></td>
            </tr>
            <tr>
              <td><strong>First Term (a)</strong></td>
              <td><em>a : b :: c : d</em></td>
              <td><em>a × d = b × c</em></td>
              <td><strong style="color: #4f46e5;">a = (b × c) ÷ d</strong></td>
              <td><em>Pramāṇa = (Phala × Ichchhā) ÷ Ichchhāphala</em></td>
            </tr>
            <tr>
              <td><strong>Mean Proportional (m)</strong></td>
              <td><em>a : m :: m : b</em></td>
              <td><em>m² = a × b</em></td>
              <td><strong style="color: #059669;">m = √(a × b)</strong></td>
              <td>Continuous proportion (Geometrical mean)</td>
            </tr>
          </tbody>
        </table>
      </div>

      <!-- TABLE 3: GROUP SHARING & MIXTURE PARTITIONING -->
      <h3 class="subheading"><i class="fa-solid fa-users"></i> Table 3.3: Group Sharing &amp; Mixture Partitioning Laws</h3>
      <div class="table-container">
        <table class="data-table">
          <thead>
            <tr>
              <th>Problem Category</th>
              <th>Given Quantities</th>
              <th>Ratio Distribution</th>
              <th>Calculated Shares / Quantities</th>
              <th>Practical Application</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>Two-Way Partition</strong></td>
              <td>Total quantity <em>x</em></td>
              <td><em>m : n</em></td>
              <td>
                Part 1 = <em>x × [m / (m + n)]</em><br>
                Part 2 = <em>x × [n / (m + n)]</em>
              </td>
              <td>Sharing ₹4,500 in ratio 2 : 3 (₹1,800 and ₹2,700).</td>
            </tr>
            <tr>
              <td><strong>Three-Way Partition</strong></td>
              <td>Total quantity <em>x</em></td>
              <td><em>p : q : r</em></td>
              <td>
                Part 1 = <em>x × [p / (p + q + r)]</em><br>
                Part 2 = <em>x × [q / (p + q + r)]</em><br>
                Part 3 = <em>x × [r / (p + q + r)]</em>
              </td>
              <td>Concrete mixing (Cement : Sand : Gravel = 1 : 2 : 4).</td>
            </tr>
            <tr>
              <td><strong>Partnership Profit</strong></td>
              <td>Total profit <em>P</em>, investments <em>I₁</em> and <em>I₂</em></td>
              <td><em>I₁ : I₂</em></td>
              <td>
                Share 1 = <em>P × [I₁ / (I₁ + I₂)]</em><br>
                Share 2 = <em>P × [I₂ / (I₁ + I₂)]</em>
              </td>
              <td>Prashanti (₹75k) &amp; Bhuvan (₹25k) sharing ₹4k profit.</td>
            </tr>
            <tr>
              <td><strong>Mixture Component Addition</strong></td>
              <td>Mixture <em>W</em> in ratio <em>m : n</em>; add component <em>B</em> to get <em>p : q</em></td>
              <td>Old <em>m:n</em>, New <em>p:q</em></td>
              <td>
                Fixed Component <em>A = W × [m/(m+n)]</em>.<br>
                New Total <em>B = A × (q / p)</em>.<br>
                Added <em>B = (New B) - (Old B)</em>.
              </td>
              <td>40 kg sand-cement (3:1), adding cement to make 5:2.</td>
            </tr>
            <tr>
              <td><strong>Pure Component Blending</strong></td>
              <td>1 bucket mix (<em>m : n</em>) + 1 bucket pure <em>B</em></td>
              <td>Original <em>m : n</em></td>
              <td>
                Total parts in 1 bucket = <em>m + n</em>.<br>
                Added Pure <em>B = (m + n)</em>.<br>
                New Ratio = <strong>m : [n + (m + n)]</strong>
              </td>
              <td>Orange paint (3 red : 5 yellow) + 1 bucket pure yellow ⇒ 3 : 13.</td>
            </tr>
          </tbody>
        </table>
      </div>

      <!-- TABLE 4: COMPLETE UNIT CONVERSIONS -->
      <h3 class="subheading"><i class="fa-solid fa-ruler-combined"></i> Table 3.4: Master Unit Conversion Standards</h3>
      <div class="table-container">
        <table class="data-table">
          <thead>
            <tr>
              <th>Physical Dimension</th>
              <th>Primary Unit</th>
              <th>Target Unit</th>
              <th>Exact / Standard Conversion Factor</th>
              <th>Reverse Conversion Factor</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td rowspan="3"><strong>Length</strong></td>
              <td>1 metre (m)</td>
              <td>Feet (ft)</td>
              <td><strong>1 m = 3.281 ft</strong></td>
              <td>1 ft ≈ 0.3048 m</td>
            </tr>
            <tr>
              <td>1 foot (ft)</td>
              <td>Inches (in)</td>
              <td><strong>1 ft = 12 inches</strong></td>
              <td>1 in ≈ 0.0833 ft</td>
            </tr>
            <tr>
              <td>1 inch (in)</td>
              <td>Centimetres (cm)</td>
              <td><strong>1 in = 2.54 cm</strong></td>
              <td>1 cm ≈ 0.3937 in</td>
            </tr>
            <tr>
              <td rowspan="4"><strong>Area (Land)</strong></td>
              <td>1 square metre (m²)</td>
              <td>Square feet (sq ft)</td>
              <td><strong>1 m² = 10.764 sq ft</strong></td>
              <td>1 sq ft ≈ 0.0929 m²</td>
            </tr>
            <tr>
              <td>1 acre</td>
              <td>Square feet (sq ft)</td>
              <td><strong>1 acre = 43,560 sq ft</strong></td>
              <td>1 sq ft = 1/43,560 acre</td>
            </tr>
            <tr>
              <td>1 hectare (ha)</td>
              <td>Square metres (m²)</td>
              <td><strong>1 ha = 10,000 m²</strong></td>
              <td>1 m² = 0.0001 ha</td>
            </tr>
            <tr>
              <td>1 hectare (ha)</td>
              <td>Acres</td>
              <td><strong>1 ha = 2.471 acres</strong></td>
              <td>1 acre ≈ 0.4047 ha</td>
            </tr>
            <tr>
              <td rowspan="3"><strong>Volume / Capacity</strong></td>
              <td>1 millilitre (mL)</td>
              <td>Cubic centimetre (cc)</td>
              <td><strong>1 mL = 1 cc (cm³)</strong></td>
              <td>1 cc = 1 mL</td>
            </tr>
            <tr>
              <td>1 Litre (L)</td>
              <td>Millilitres (mL)</td>
              <td><strong>1 L = 1,000 mL</strong></td>
              <td>1 mL = 0.001 L</td>
            </tr>
            <tr>
              <td>1 cubic metre (m³)</td>
              <td>Litres (L)</td>
              <td><strong>1 m³ = 1,000 L</strong></td>
              <td>1 L = 0.001 m³</td>
            </tr>
            <tr>
              <td rowspan="2"><strong>Mass / Weight</strong></td>
              <td>1 kilogram (kg)</td>
              <td>Grams (g)</td>
              <td><strong>1 kg = 1,000 g</strong></td>
              <td>1 g = 0.001 kg</td>
            </tr>
            <tr>
              <td>1 tonne (metric ton)</td>
              <td>Kilograms (kg)</td>
              <td><strong>1 tonne = 1,000 kg</strong></td>
              <td>1 kg = 0.001 tonne</td>
            </tr>
            <tr>
              <td rowspan="2"><strong>Temperature</strong></td>
              <td>Celsius (°C)</td>
              <td>Fahrenheit (°F)</td>
              <td><strong style="color: #dc2626;">°F = (9/5) × °C + 32</strong></td>
              <td>Freezing point: 0 °C = 32 °F</td>
            </tr>
            <tr>
              <td>Fahrenheit (°F)</td>
              <td>Celsius (°C)</td>
              <td><strong style="color: #dc2626;">°C = (5/9) × (°F - 32)</strong></td>
              <td>Room temp: 77 °F = 25 °C</td>
            </tr>
          </tbody>
        </table>
      </div>

      <!-- TABLE 5: DIRECT VS INVERSE PROPORTION COMPARISON -->
      <h3 class="subheading"><i class="fa-solid fa-arrows-split-up-and-left"></i> Table 3.5: Direct Proportion vs Inverse Variation Comparative Blueprint</h3>
      <div class="table-container">
        <table class="data-table">
          <thead>
            <tr>
              <th>Feature / Parameter</th>
              <th>Direct Proportion (ପ୍ରତ୍ୟକ୍ଷ ସମାନୁପାତ)</th>
              <th>Inverse Variation (ବ୍ୟସ୍ତ ସମାନୁପାତ)</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>Behavior</strong></td>
              <td>Both quantities increase or decrease together by the same factor.</td>
              <td>When one quantity increases, the other decreases proportionally.</td>
            </tr>
            <tr>
              <td><strong>Governing Equation</strong></td>
              <td><em>y / x = k</em> (or <em>y = kx</em>)</td>
              <td><em>x × y = C</em> (or <em>y = C / x</em>)</td>
            </tr>
            <tr>
              <td><strong>Invariant Metric</strong></td>
              <td>The <strong>ratio (quotient)</strong> is constant: <em>y₁/x₁ = y₂/x₂</em>.</td>
              <td>The <strong>product</strong> is constant: <em>x₁ × y₁ = x₂ × y₂</em>.</td>
            </tr>
            <tr>
              <td><strong>Graph Characteristic</strong></td>
              <td>A straight line passing through the origin <em>(0, 0)</em>.</td>
              <td>A smooth downward curved rectangular hyperbola (never touches axes).</td>
            </tr>
            <tr>
              <td><strong>Real-World Example 1</strong></td>
              <td>Midday meal rice vs Number of students (more students = more rice).</td>
              <td>Speed vs Travel time (higher speed = less travel time).</td>
            </tr>
            <tr>
              <td><strong>Real-World Example 2</strong></td>
              <td>Cost of identical pens vs Number of pens purchased.</td>
              <td>Number of workers vs Days required to build a wall.</td>
            </tr>
            <tr>
              <td><strong>Applicability of Rule of Three</strong></td>
              <td><span style="color: #15803d; font-weight: 700;">✓ 100% Valid: d = (b × c) / a</span></td>
              <td><span style="color: #b91c1c; font-weight: 700;">✗ Invalid! Use x₂ = (x₁ × y₁) / y₂</span></td>
            </tr>
          </tbody>
        </table>
      </div>

      <!-- TABLE 6: GEOMETRIC SCALING & ASPECT RATIO INVARIANTS -->
      <h3 class="subheading"><i class="fa-solid fa-expand"></i> Table 3.6: Geometric Scaling Laws &amp; Dimensional Invariants</h3>
      <div class="table-container">
        <table class="data-table">
          <thead>
            <tr>
              <th>Geometric Dimension</th>
              <th>Original Measure</th>
              <th>Linear Scale Factor <em>k</em></th>
              <th>Scaled Measure</th>
              <th>Ratio of Scaled to Original</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>Linear Dimension (Length, Width, Height)</strong></td>
              <td><em>L, W, H</em></td>
              <td>Multiply by <em>k</em></td>
              <td><em>kL, kW, kH</em></td>
              <td><strong>k : 1</strong></td>
            </tr>
            <tr>
              <td><strong>Perimeter (Boundary Length)</strong></td>
              <td><em>P = 2(L + W)</em></td>
              <td>Multiply by <em>k</em></td>
              <td><em>2(kL + kW) = kP</em></td>
              <td><strong>k : 1</strong></td>
            </tr>
            <tr>
              <td><strong>Surface Area (2D Area)</strong></td>
              <td><em>A = L × W</em></td>
              <td>Each side multiplied by <em>k</em></td>
              <td><em>(kL) × (kW) = k²A</em></td>
              <td><strong style="color: #4f46e5;">k² : 1</strong></td>
            </tr>
            <tr>
              <td><strong>Volume (3D Capacity)</strong></td>
              <td><em>V = L × W × H</em></td>
              <td>Each dimension multiplied by <em>k</em></td>
              <td><em>(kL) × (kW) × (kH) = k³V</em></td>
              <td><strong style="color: #059669;">k³ : 1</strong></td>
            </tr>
            <tr>
              <td><strong>Aspect Ratio (Width ÷ Height)</strong></td>
              <td><em>W / H</em></td>
              <td>Same scale factor <em>k</em> for both</td>
              <td><em>(kW) / (kH) = W / H</em></td>
              <td><strong style="color: #15803d;">1 : 1 (INVARIANT!)</strong></td>
            </tr>
          </tbody>
        </table>
      </div>
    </section>
"""
