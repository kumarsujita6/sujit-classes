# -*- coding: utf-8 -*-
"""
Module: ch8_section3.py
Contains Section 3: Rapid Revision Fact & Formula/Law Bank, presented in structured,
high-density HTML data tables with comprehensive algebraic expressions and mental shortcuts.
"""

def get_section3():
    return """
    <!-- ========================================== -->
    <!-- SECTION 3: RAPID REVISION FACT & FORMULA   -->
    <!-- ========================================== -->
    <section id="section3">
      <div class="section-header">
        <div class="section-tag"><i class="fa-solid fa-table"></i> Mathematical Formula Bank</div>
        <h2 class="section-title">Section 3: Rapid Revision Fact &amp; Formula/Law Bank</h2>
        <p class="section-desc">
          High-yield summary tables compiling every algebraic transformation rule, commercial equation, interest formula, and benchmark mental fraction equivalent in Class 8 Mathematics.
        </p>
      </div>

      <!-- TABLE 3.1: FUNDAMENTAL CONVERSION LAWS -->
      <h3 class="subheading"><i class="fa-solid fa-repeat"></i> Table 3.1: Fundamental Conversion Laws &amp; Transformations</h3>
      <div class="table-container">
        <table class="data-table">
          <thead>
            <tr>
              <th style="width: 25%;">Operation / Target</th>
              <th style="width: 35%;">Algebraic Formula / Law</th>
              <th style="width: 40%;">Worked Example &amp; Practical Notes</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>Fraction to Percentage</strong></td>
              <td><code>p% = (a / b) × 100%</code></td>
              <td><code>3/4 × 100% = 75%</code>. Or multiply numerator &amp; denominator by factor <code>100/b</code>.</td>
            </tr>
            <tr>
              <td><strong>Percentage to Fraction</strong></td>
              <td><code>Fraction = p / 100</code> (reduced to lowest terms)</td>
              <td><code>45% = 45/100 = 9/20</code>. Divide by HCF of numerator and 100.</td>
            </tr>
            <tr>
              <td><strong>Decimal to Percentage</strong></td>
              <td><code>p% = Decimal × 100%</code></td>
              <td><code>0.825 × 100% = 82.5%</code>. Shift decimal point 2 places right and append ‘%’.</td>
            </tr>
            <tr>
              <td><strong>Percentage to Decimal</strong></td>
              <td><code>Decimal = p / 100</code></td>
              <td><code>6.5% = 6.5 / 100 = 0.065</code>. Shift decimal point 2 places left.</td>
            </tr>
            <tr>
              <td><strong>Percentage of a Quantity</strong></td>
              <td><code>Value = (p / 100) × Quantity</code></td>
              <td><code>20% of ₹5,000 = 0.20 × 5000 = ₹1,000</code>. ‘Of’ represents multiplication.</td>
            </tr>
            <tr>
              <td><strong>Finding the Whole Quantity</strong></td>
              <td><code>Total = (Given Value / p) × 100</code></td>
              <td>If 40% of a journey is 92 km, Total = <code>(92 / 40) × 100 = 230 km</code>.</td>
            </tr>
            <tr>
              <td><strong>Commutative Multiplication</strong></td>
              <td><code>x% of y = y% of x</code></td>
              <td><code>8% of 50 = 50% of 8 = 4</code>. Extremely powerful when one number is 50, 25, 20, or 10.</td>
            </tr>
            <tr>
              <td><strong>Ratio to Percentage</strong></td>
              <td>If ratio is <code>a : b</code>, Total = <code>a + b</code><br>Part 1% = <code>[a / (a+b)] × 100</code></td>
              <td>Millet kanji ratio 2 : 7 ⇒ Total = 9. Millet% = <code>(2 / 9) × 100 = 22.22%</code>.</td>
            </tr>
          </tbody>
        </table>
      </div>

      <!-- TABLE 3.2: THE BENCHMARK FDP EQUIVALENCE TABLE -->
      <h3 class="subheading"><i class="fa-solid fa-list-ol"></i> Table 3.2: Benchmark Fractions, Decimals, and Percentages (Memory Bank)</h3>
      <div class="table-container">
        <table class="data-table">
          <thead>
            <tr>
              <th style="width: 15%;">Fraction (a/b)</th>
              <th style="width: 15%;">Decimal Value</th>
              <th style="width: 20%;">Percentage (%)</th>
              <th style="width: 50%;">Mental Calculation Trick / Anchor</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>1 / 1</strong></td>
              <td>1.0</td>
              <td><strong>100%</strong></td>
              <td>The complete whole; standard reference baseline</td>
            </tr>
            <tr>
              <td><strong>1 / 2</strong></td>
              <td>0.5</td>
              <td><strong>50%</strong></td>
              <td>Divide by 2; exact half</td>
            </tr>
            <tr>
              <td><strong>1 / 3</strong></td>
              <td>0.3333...</td>
              <td><strong>33 ⅓% (≈ 33.33%)</strong></td>
              <td>Divide by 3; non-terminating repeating decimal</td>
            </tr>
            <tr>
              <td><strong>2 / 3</strong></td>
              <td>0.6666...</td>
              <td><strong>66 ⅔% (≈ 66.67%)</strong></td>
              <td>Double of 1/3; non-terminating repeating decimal</td>
            </tr>
            <tr>
              <td><strong>1 / 4</strong></td>
              <td>0.25</td>
              <td><strong>25%</strong></td>
              <td>Divide by 4 (halve twice); a quarter</td>
            </tr>
            <tr>
              <td><strong>3 / 4</strong></td>
              <td>0.75</td>
              <td><strong>75%</strong></td>
              <td>Three quarters; 50% + 25% or multiply 25% by 3</td>
            </tr>
            <tr>
              <td><strong>1 / 5</strong></td>
              <td>0.2</td>
              <td><strong>20%</strong></td>
              <td>Divide by 5 (or double and shift 1 decimal place left)</td>
            </tr>
            <tr>
              <td><strong>2 / 5</strong></td>
              <td>0.4</td>
              <td><strong>40%</strong></td>
              <td>Double of 1/5 (2 × 20%)</td>
            </tr>
            <tr>
              <td><strong>3 / 5</strong></td>
              <td>0.6</td>
              <td><strong>60%</strong></td>
              <td>Triple of 1/5 (3 × 20%)</td>
            </tr>
            <tr>
              <td><strong>4 / 5</strong></td>
              <td>0.8</td>
              <td><strong>80%</strong></td>
              <td>Four times 1/5 (100% - 20%)</td>
            </tr>
            <tr>
              <td><strong>1 / 6</strong></td>
              <td>0.1666...</td>
              <td><strong>16 ⅔% (≈ 16.67%)</strong></td>
              <td>Half of 1/3; divide 33.33% by 2</td>
            </tr>
            <tr>
              <td><strong>5 / 6</strong></td>
              <td>0.8333...</td>
              <td><strong>83 ⅓% (≈ 83.33%)</strong></td>
              <td>100% minus 1/6 (100% - 16.67%)</td>
            </tr>
            <tr>
              <td><strong>1 / 8</strong></td>
              <td>0.125</td>
              <td><strong>12.5% (12 ½%)</strong></td>
              <td>Half of 1/4 (25% ÷ 2); halve three times</td>
            </tr>
            <tr>
              <td><strong>3 / 8</strong></td>
              <td>0.375</td>
              <td><strong>37.5%</strong></td>
              <td>3 × 12.5% (25% + 12.5%)</td>
            </tr>
            <tr>
              <td><strong>5 / 8</strong></td>
              <td>0.625</td>
              <td><strong>62.5%</strong></td>
              <td>5 × 12.5% (50% + 12.5%)</td>
            </tr>
            <tr>
              <td><strong>7 / 8</strong></td>
              <td>0.875</td>
              <td><strong>87.5%</strong></td>
              <td>100% minus 1/8 (100% - 12.5%)</td>
            </tr>
            <tr>
              <td><strong>1 / 10</strong></td>
              <td>0.1</td>
              <td><strong>10%</strong></td>
              <td>The master anchor; slide decimal point 1 place left</td>
            </tr>
            <tr>
              <td><strong>1 / 11</strong></td>
              <td>0.0909...</td>
              <td><strong>9.09%</strong></td>
              <td>Repeating 09; 5/11 = 45.45%</td>
            </tr>
            <tr>
              <td><strong>1 / 12</strong></td>
              <td>0.0833...</td>
              <td><strong>8 ⅓% (≈ 8.33%)</strong></td>
              <td>Half of 1/6 (16.67% ÷ 2)</td>
            </tr>
            <tr>
              <td><strong>1 / 16</strong></td>
              <td>0.0625</td>
              <td><strong>6.25% (6 ¼%)</strong></td>
              <td>Half of 1/8 (12.5% ÷ 2)</td>
            </tr>
            <tr>
              <td><strong>1 / 20</strong></td>
              <td>0.05</td>
              <td><strong>5%</strong></td>
              <td>Half of 10% (slide 1 place left and divide by 2)</td>
            </tr>
            <tr>
              <td><strong>1 / 25</strong></td>
              <td>0.04</td>
              <td><strong>4%</strong></td>
              <td>Divide by 25 (or multiply numerator by 4 over 100)</td>
            </tr>
            <tr>
              <td><strong>1 / 50</strong></td>
              <td>0.02</td>
              <td><strong>2%</strong></td>
              <td>Divide by 50 (or multiply by 2 over 100)</td>
            </tr>
            <tr>
              <td><strong>1 / 100</strong></td>
              <td>0.01</td>
              <td><strong>1%</strong></td>
              <td>The fundamental unit; slide decimal point 2 places left</td>
            </tr>
          </tbody>
        </table>
      </div>

      <!-- TABLE 3.3: COMMERCIAL MATHEMATICS FORMULA BANK -->
      <h3 class="subheading"><i class="fa-solid fa-cash-register"></i> Table 3.3: Commercial Math &amp; Trading Formulas</h3>
      <div class="table-container">
        <table class="data-table">
          <thead>
            <tr>
              <th style="width: 25%;">Concept / Variable</th>
              <th style="width: 35%;">Mathematical Formula</th>
              <th style="width: 40%;">Core Rule &amp; Examination Notes</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>Effective Cost Price</strong></td>
              <td><code>Effective CP = Purchase Price + Overheads</code></td>
              <td>Freight, transport, packaging, and repair expenses must be added to purchase price before calculating profit/loss.</td>
            </tr>
            <tr>
              <td><strong>Profit (Gain)</strong></td>
              <td><code>Profit = SP - CP</code> &nbsp;(valid when <code>SP &gt; CP</code>)</td>
              <td>Financial surplus generated in the sale.</td>
            </tr>
            <tr>
              <td><strong>Loss</strong></td>
              <td><code>Loss = CP - SP</code> &nbsp;(valid when <code>CP &gt; SP</code>)</td>
              <td>Financial deficit suffered in the sale.</td>
            </tr>
            <tr>
              <td><strong>Profit Percentage</strong></td>
              <td><code>Profit% = (Profit / CP) × 100%</code></td>
              <td><strong>ALWAYS calculated on Cost Price (CP)</strong>, never on Selling Price!</td>
            </tr>
            <tr>
              <td><strong>Loss Percentage</strong></td>
              <td><code>Loss% = (Loss / CP) × 100%</code></td>
              <td><strong>ALWAYS calculated on Cost Price (CP)</strong>, never on Selling Price!</td>
            </tr>
            <tr>
              <td><strong>SP from CP &amp; Profit%</strong></td>
              <td><code>SP = CP × (1 + Profit%/100)</code></td>
              <td>Multiplier is greater than 1.0. E.g., for 20% profit, <code>SP = 1.20 × CP</code>.</td>
            </tr>
            <tr>
              <td><strong>SP from CP &amp; Loss%</strong></td>
              <td><code>SP = CP × (1 - Loss%/100)</code></td>
              <td>Multiplier is less than 1.0. E.g., for 15% loss, <code>SP = 0.85 × CP</code>.</td>
            </tr>
            <tr>
              <td><strong>Trade Discount</strong></td>
              <td><code>Discount = MP - SP</code></td>
              <td>The price reduction granted off the marked list price.</td>
            </tr>
            <tr>
              <td><strong>Discount Percentage</strong></td>
              <td><code>Discount% = (Discount / MP) × 100%</code></td>
              <td><strong>ALWAYS calculated on Marked Price (MP)</strong>, never on CP or SP!</td>
            </tr>
            <tr>
              <td><strong>SP from MP &amp; Discount%</strong></td>
              <td><code>SP = MP × (1 - Discount%/100)</code></td>
              <td>If a shirt marked ₹800 has 25% discount, <code>SP = 800 × 0.75 = ₹600</code>.</td>
            </tr>
            <tr>
              <td><strong>Successive Discounts</strong></td>
              <td><code>Single Equivalent d% = [1 - (1 - d₁/100)(1 - d₂/100)] × 100%</code></td>
              <td>For discounts of 30% and 20%: <code>1 - (0.7 × 0.8) = 1 - 0.56 = 44%</code>. NOT 50%!</td>
            </tr>
            <tr>
              <td><strong>Goods and Services Tax (GST)</strong></td>
              <td><code>Final Bill Amount = SP × (1 + GST%/100)</code></td>
              <td>GST is added to the net selling price after all trade discounts are applied.</td>
            </tr>
          </tbody>
        </table>
      </div>

      <!-- TABLE 3.4: SIMPLE VS COMPOUND INTEREST & DEPRECIATION -->
      <h3 class="subheading"><i class="fa-solid fa-chart-line"></i> Table 3.4: Financial Capital Growth &amp; Depreciation Law Bank</h3>
      <div class="table-container">
        <table class="data-table">
          <thead>
            <tr>
              <th style="width: 25%;">Financial Regimes</th>
              <th style="width: 35%;">Governing Formula</th>
              <th style="width: 40%;">Mechanism &amp; Distinctive Nature</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>Simple Interest (SI)</strong></td>
              <td><code>SI = (P × R × T) / 100</code></td>
              <td>Interest is linear and paid out periodically. The principal <em>P</em> remains constant every year.</td>
            </tr>
            <tr>
              <td><strong>Total Amount (SI)</strong></td>
              <td><code>A = P + SI = P × [1 + (R × T) / 100]</code></td>
              <td>Growth is arithmetic (increases by a fixed constant amount each year).</td>
            </tr>
            <tr>
              <td><strong>Compound Amount (CI)</strong></td>
              <td><code>A = P × (1 + R / 100)ᵗ</code></td>
              <td>Annual compounding. Earned interest is added to principal at the end of each period.</td>
            </tr>
            <tr>
              <td><strong>Compound Interest (CI)</strong></td>
              <td><code>CI = Amount - Principal = A - P</code></td>
              <td>Represents accumulated interest including all "interest-on-interest" cascades.</td>
            </tr>
            <tr>
              <td><strong>Depreciation of Assets</strong></td>
              <td><code>A = P × (1 - R / 100)ⁿ</code></td>
              <td>Used for vehicle wear, electronics obsolescence, or decreasing populations. Minus sign reflects annual decay.</td>
            </tr>
            <tr>
              <td><strong>Net Two-Stage Change Formula</strong></td>
              <td><code>Net% Change = x + y + (x × y) / 100</code></td>
              <td>Valid for successive percentage changes where <em>x</em> and <em>y</em> carry their own sign (+ for increase, - for decrease).</td>
            </tr>
          </tbody>
        </table>
      </div>
    </section>
"""
