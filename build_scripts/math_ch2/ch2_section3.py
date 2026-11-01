# -*- coding: utf-8 -*-
"""
Module: ch2_section3.py
Contains Section 3: Rapid Revision Fact & Formula/Law Bank
Structured reference tables covering all 7 laws, powers of 2, 3, 5, 10,
metric prefixes, Indian classical large number scales, and order of magnitude timelines.
"""

def get_section_3():
    return """
    <!-- ========================================== -->
    <!-- SECTION 3: RAPID REVISION FACT & LAW BANK -->
    <!-- ========================================== -->
    <section id="section-3" class="study-section">
      <div class="section-header">
        <span class="section-badge"><i class="fa-solid fa-table-list"></i> High-Yield Reference</span>
        <h2 class="section-title">Rapid Revision Fact & Formula/Law Bank</h2>
        <p class="section-subtitle">
          Complete, structured reference tables compiling every formula, mathematical identity, power progression, and metric scaling factor for instant examination recall.
        </p>
      </div>

      <!-- Table 3.1: Master Summary of Exponent Laws -->
      <h3 class="topic-title"><i class="fa-solid fa-list-check"></i> Table 3.1: Master Summary of the Laws of Exponents</h3>
      <p>
        Use this consolidated master matrix to review conditions, algebraic statements, and typical textbook applications of all 7 exponent laws:
      </p>

      <div class="table-container">
        <table>
          <thead>
            <tr>
              <th>Law Name</th>
              <th>Algebraic Formula</th>
              <th>Underlying Condition</th>
              <th>Step-by-Step Numerical Example</th>
              <th>Examiner Caution / Trap Alert</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>1. Product Law</strong></td>
              <td class="math-font">aᵐ × aⁿ = aᵐ⁺ⁿ</td>
              <td>Same base <span class="math-font">a</span>; <span class="math-font">m, n</span> are any integers</td>
              <td><span class="math-font">2⁴ × 2³ = 2⁴⁺³ = 2⁷ = 128</span></td>
              <td>Do NOT multiply the bases! <span class="math-font">2⁴ × 2³ ≠ 4⁷</span>. Base stays 2.</td>
            </tr>
            <tr>
              <td><strong>2. Quotient Law</strong></td>
              <td class="math-font">aᵐ ÷ aⁿ = aᵐ⁻ⁿ</td>
              <td>Base <span class="math-font">a ≠ 0</span>; <span class="math-font">m, n</span> are integers</td>
              <td><span class="math-font">5⁶ ÷ 5² = 5⁶⁻² = 5⁴ = 625</span></td>
              <td>Do NOT divide the bases! <span class="math-font">5⁶ ÷ 5² ≠ 1⁴</span>. Base stays 5.</td>
            </tr>
            <tr>
              <td><strong>3. Power of a Power</strong></td>
              <td class="math-font">(aᵐ)ⁿ = aᵐˣⁿ</td>
              <td>Base <span class="math-font">a</span>; <span class="math-font">m, n</span> are integers</td>
              <td><span class="math-font">(3²)⁴ = 3²ˣ⁴ = 3⁸ = 6,561</span></td>
              <td>Multiply the exponents (<span class="math-font">2 × 4 = 8</span>), do NOT add them (<span class="math-font">2 + 4 ≠ 6</span>).</td>
            </tr>
            <tr>
              <td><strong>4. Common Exponent (Product)</strong></td>
              <td class="math-font">aᵐ × bᵐ = (a × b)ᵐ</td>
              <td>Exponents match; bases can differ</td>
              <td><span class="math-font">2³ × 5³ = (2 × 5)³ = 10³ = 1,000</span></td>
              <td>Only works when exponents are IDENTICAL. Useful for forming powers of 10.</td>
            </tr>
            <tr>
              <td><strong>5. Common Exponent (Quotient)</strong></td>
              <td class="math-font">aᵐ ÷ bᵐ = (a / b)ᵐ</td>
              <td>Denominator base <span class="math-font">b ≠ 0</span></td>
              <td><span class="math-font">12³ ÷ 4³ = (12/4)³ = 3³ = 27</span></td>
              <td>Simplifying base division first (<span class="math-font">12/4 = 3</span>) saves huge calculation time.</td>
            </tr>
            <tr>
              <td><strong>6. Zero Exponent Rule</strong></td>
              <td class="math-font">a⁰ = 1</td>
              <td>Valid for any base <span class="math-font">a ≠ 0</span></td>
              <td><span class="math-font">999⁰ = 1</span>, <span class="math-font">(–17)⁰ = 1</span></td>
              <td><span class="math-font">0⁰</span> is strictly UNDEFINED! It does NOT equal 1 or 0.</td>
            </tr>
            <tr>
              <td><strong>7. Negative Exponent Rule</strong></td>
              <td class="math-font">a⁻ⁿ = 1 / aⁿ</td>
              <td>Base <span class="math-font">a ≠ 0</span>; reciprocal relation</td>
              <td><span class="math-font">2⁻³ = 1 / 2³ = 1/8 = 0.125</span></td>
              <td>Negative exponent does NOT make the answer negative! It creates a positive fraction.</td>
            </tr>
          </tbody>
        </table>
      </div>

      <!-- Table 3.2: Powers of Base 2 Bank -->
      <h3 class="topic-title"><i class="fa-solid fa-cubes"></i> Table 3.2: Essential Powers of Base 2 (Reference Bank)</h3>
      <p>
        Powers of 2 appear everywhere in computer memory, doubling problems, and binary counting. Memorise these values for instant speed in exam halls:
      </p>

      <div class="table-container">
        <table>
          <thead>
            <tr>
              <th>Power (2ⁿ)</th>
              <th>Calculation / Factorisation</th>
              <th>Evaluated Value</th>
              <th>Real-Life / Computing Context</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td class="math-font">2⁻⁴</td>
              <td>1 / 2⁴ = 1 / 16</td>
              <td>0.0625</td>
              <td>One-sixteenth fraction</td>
            </tr>
            <tr>
              <td class="math-font">2⁻³</td>
              <td>1 / 2³ = 1 / 8</td>
              <td>0.125</td>
              <td>One-eighth unit</td>
            </tr>
            <tr>
              <td class="math-font">2⁻²</td>
              <td>1 / 2² = 1 / 4</td>
              <td>0.25</td>
              <td>One-quarter unit</td>
            </tr>
            <tr>
              <td class="math-font">2⁻¹</td>
              <td>1 / 2¹ = 1 / 2</td>
              <td>0.5</td>
              <td>Half unit</td>
            </tr>
            <tr>
              <td class="math-font">2⁰</td>
              <td>Fundamental zero fulcrum</td>
              <td>1</td>
              <td>Single unit</td>
            </tr>
            <tr>
              <td class="math-font">2¹</td>
              <td>2</td>
              <td>2</td>
              <td>First doubling</td>
            </tr>
            <tr>
              <td class="math-font">2²</td>
              <td>2 × 2</td>
              <td>4</td>
              <td>2 squared</td>
            </tr>
            <tr>
              <td class="math-font">2³</td>
              <td>2 × 2 × 2</td>
              <td>8</td>
              <td>2 cubed / 1 Byte = 8 bits</td>
            </tr>
            <tr>
              <td class="math-font">2⁴</td>
              <td>2³ × 2</td>
              <td>16</td>
              <td>Hexadecimal base</td>
            </tr>
            <tr>
              <td class="math-font">2⁵</td>
              <td>2⁴ × 2</td>
              <td>32</td>
              <td>32-bit operating systems</td>
            </tr>
            <tr>
              <td class="math-font">2⁶</td>
              <td>2⁵ × 2</td>
              <td>64</td>
              <td>64-bit modern computers; 64 squares on chessboard</td>
            </tr>
            <tr>
              <td class="math-font">2⁷</td>
              <td>2⁶ × 2</td>
              <td>128</td>
              <td>Layers after 7 folds of paper</td>
            </tr>
            <tr>
              <td class="math-font">2⁸</td>
              <td>2⁷ × 2</td>
              <td>256</td>
              <td>Values in an 8-bit byte (0 to 255)</td>
            </tr>
            <tr>
              <td class="math-font">2⁹</td>
              <td>2⁸ × 2</td>
              <td>512</td>
              <td>Standard storage block</td>
            </tr>
            <tr>
              <td class="math-font">2¹⁰</td>
              <td>2⁹ × 2</td>
              <td>1,024</td>
              <td>1 Kilobyte (KB) in computing; ~1,000 multiplier</td>
            </tr>
            <tr>
              <td class="math-font">2¹¹</td>
              <td>2¹⁰ × 2</td>
              <td>2,048</td>
              <td>The 2048 game maximum tile</td>
            </tr>
            <tr>
              <td class="math-font">2¹²</td>
              <td>2¹¹ × 2</td>
              <td>4,096</td>
              <td>4K digital video resolution width</td>
            </tr>
          </tbody>
        </table>
      </div>

      <!-- Table 3.3: Powers of Base 3 and Base 5 -->
      <h3 class="topic-title"><i class="fa-solid fa-shapes"></i> Table 3.3: Essential Powers of Base 3 and Base 5</h3>
      <div class="table-container">
        <table>
          <thead>
            <tr>
              <th>Base 3 Power</th>
              <th>Value</th>
              <th>Base 5 Power</th>
              <th>Value</th>
              <th>Prime Factorisation Applications</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td class="math-font">3⁻²</td>
              <td>1/9 ≈ 0.111</td>
              <td class="math-font">5⁻²</td>
              <td>1/25 = 0.04</td>
              <td>Fractions in scientific notation</td>
            </tr>
            <tr>
              <td class="math-font">3⁻¹</td>
              <td>1/3 ≈ 0.333</td>
              <td class="math-font">5⁻¹</td>
              <td>1/5 = 0.2</td>
              <td>Decimal tenths conversion</td>
            </tr>
            <tr>
              <td class="math-font">3⁰</td>
              <td>1</td>
              <td class="math-font">5⁰</td>
              <td>1</td>
              <td>Zero power fulcrum</td>
            </tr>
            <tr>
              <td class="math-font">3¹</td>
              <td>3</td>
              <td class="math-font">5¹</td>
              <td>5</td>
              <td>Prime factors</td>
            </tr>
            <tr>
              <td class="math-font">3²</td>
              <td>9</td>
              <td class="math-font">5²</td>
              <td>25</td>
              <td>Squares of 3 and 5</td>
            </tr>
            <tr>
              <td class="math-font">3³</td>
              <td>27</td>
              <td class="math-font">5³</td>
              <td>125</td>
              <td>Cubes of 3 and 5</td>
            </tr>
            <tr>
              <td class="math-font">3⁴</td>
              <td>81</td>
              <td class="math-font">5⁴</td>
              <td>625</td>
              <td>4th power; <span class="math-font">405 = 3⁴ × 5¹</span></td>
            </tr>
            <tr>
              <td class="math-font">3⁵</td>
              <td>243</td>
              <td class="math-font">5⁵</td>
              <td>3,125</td>
              <td>High composite factor</td>
            </tr>
            <tr>
              <td class="math-font">3⁶</td>
              <td>729</td>
              <td class="math-font">5⁶</td>
              <td>15,625</td>
              <td>Both a square (<span class="math-font">27²</span>) and a cube (<span class="math-font">9³</span>)!</td>
            </tr>
            <tr>
              <td class="math-font">3⁷</td>
              <td>2,187</td>
              <td class="math-font">5⁷</td>
              <td>78,125</td>
              <td>Appears in Chapter 2 textbook prompt</td>
            </tr>
            <tr>
              <td class="math-font">3⁸</td>
              <td>6,561</td>
              <td class="math-font">5⁸</td>
              <td>3,90,625</td>
              <td><span class="math-font">6561 = (3⁴)² = 81²</span></td>
            </tr>
          </tbody>
        </table>
      </div>

      <!-- Table 3.4: Powers of 10 Scale & Metric System -->
      <h3 class="topic-title"><i class="fa-solid fa-gauge-high"></i> Table 3.4: The Grand Powers of 10 Scale (Metric & Indian Classical)</h3>
      <p>
        Compare how ancient Indian mathematicians and modern international standards denote powers of 10:
      </p>

      <div class="table-container">
        <table>
          <thead>
            <tr>
              <th>Power of 10</th>
              <th>Expanded Value</th>
              <th>International Name & Prefix</th>
              <th>Indian Classical Decimal Name</th>
              <th>Physical / Natural Scale Context</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td class="math-font">10⁻¹⁵</td>
              <td>0.000 000 000 000 001</td>
              <td>Femto (f)</td>
              <td>—</td>
              <td>Diameter of a proton / atomic nucleus</td>
            </tr>
            <tr>
              <td class="math-font">10⁻¹²</td>
              <td>0.000 000 000 001</td>
              <td>Pico (p)</td>
              <td>—</td>
              <td>Radius of a hydrogen atom (~50 pm)</td>
            </tr>
            <tr>
              <td class="math-font">10⁻⁹</td>
              <td>0.000 000 001</td>
              <td>Nano (n)</td>
              <td>—</td>
              <td>Width of DNA double helix (~2 nm)</td>
            </tr>
            <tr>
              <td class="math-font">10⁻⁶</td>
              <td>0.000 001</td>
              <td>Micro (μ)</td>
              <td>—</td>
              <td>Diameter of human red blood cell (~7 μm)</td>
            </tr>
            <tr>
              <td class="math-font">10⁻³</td>
              <td>0.001</td>
              <td>Milli (m)</td>
              <td>—</td>
              <td>Thickness of a credit card (~1 mm)</td>
            </tr>
            <tr>
              <td class="math-font">10⁰</td>
              <td>1</td>
              <td>Unit (One)</td>
              <td>Eka (ଏକ)</td>
              <td>Single object / human heartbeat (1 s)</td>
            </tr>
            <tr>
              <td class="math-font">10¹</td>
              <td>10</td>
              <td>Deca (da)</td>
              <td>Dasa (ଦଶ)</td>
              <td>Ten fingers; Hainan gibbon population (~42)</td>
            </tr>
            <tr>
              <td class="math-font">10²</td>
              <td>100</td>
              <td>Hecto (h)</td>
              <td>Sata (ଶତ)</td>
              <td>Century; Kakapo bird population (~242)</td>
            </tr>
            <tr>
              <td class="math-font">10³</td>
              <td>1,000</td>
              <td>Kilo (k) / Thousand</td>
              <td>Sahassa / Sahasra (ସହସ୍ର)</td>
              <td>1 Kilometre; Komodo dragon population (&lt;3000)</td>
            </tr>
            <tr>
              <td class="math-font">10⁵</td>
              <td>1,00,000</td>
              <td>Hundred Thousand</td>
              <td>Laksha (ଲକ୍ଷ)</td>
              <td>African elephant population (~4.15 lakh)</td>
            </tr>
            <tr>
              <td class="math-font">10⁶</td>
              <td>10,00,000</td>
              <td>Mega (M) / Million</td>
              <td>Prayuta (ପ୍ରୟୁତ)</td>
              <td>American alligator population (~50 lakh / 5 million)</td>
            </tr>
            <tr>
              <td class="math-font">10⁷</td>
              <td>1,00,00,000</td>
              <td>Ten Million</td>
              <td>Koti (କୋଟି)</td>
              <td>Global camel population (~3.5 crore)</td>
            </tr>
            <tr>
              <td class="math-font">10⁸</td>
              <td>10,00,00,000</td>
              <td>Hundred Million</td>
              <td>Arbuda (ଅର୍ବୁଦ)</td>
              <td>Global water buffalo population (~20 crore / 200 million)</td>
            </tr>
            <tr>
              <td class="math-font">10⁹</td>
              <td>1,00,00,00,000</td>
              <td>Giga (G) / Billion</td>
              <td>Abja / Ayuta (ଅବ୍ଜ / ଆୟୁତ)</td>
              <td>Global human population (~8.2 × 10⁹); 1 billion seconds ≈ 31.7 years</td>
            </tr>
            <tr>
              <td class="math-font">10¹²</td>
              <td>10,00,00,00,00,000</td>
              <td>Tera (T) / Trillion</td>
              <td>Kharab (ଖର୍ବ)</td>
              <td>Total trees on Earth (~3 × 10¹²); Sun to Saturn distance (~1.43 × 10¹² m)</td>
            </tr>
            <tr>
              <td class="math-font">10¹⁵</td>
              <td>10¹⁵</td>
              <td>Peta (P) / Quadrillion</td>
              <td>Padma (ପଦ୍ମ)</td>
              <td>Beetle and earthworm population (~10¹⁵); Age of Himalayas (~1.7 × 10¹⁵ s)</td>
            </tr>
            <tr>
              <td class="math-font">10¹⁶</td>
              <td>10¹⁶</td>
              <td>Ten Quadrillion</td>
              <td>—</td>
              <td>Estimated global ant population (~2 × 10¹⁶)</td>
            </tr>
            <tr>
              <td class="math-font">10¹⁷</td>
              <td>10¹⁷</td>
              <td>Hundred Quadrillion</td>
              <td>Shankh (ଶଙ୍ଖ)</td>
              <td>Age of known Universe (~4.35 × 10¹⁷ seconds)</td>
            </tr>
            <tr>
              <td class="math-font">10¹⁹</td>
              <td>10¹⁹</td>
              <td>Ten Quintillion</td>
              <td>Maha-Shankh (ମହାଶଙ୍ଖ)</td>
              <td>Maha-Shankh scale in ancient Vedic/Buddhist mathematics</td>
            </tr>
            <tr>
              <td class="math-font">10⁵³</td>
              <td>10⁵³</td>
              <td>—</td>
              <td>Tallakkhana (ତଲ୍ଲକ୍ଷଣ)</td>
              <td>Recorded in Lalitavistara Sūtra (Dialogue with Arjuna)</td>
            </tr>
            <tr>
              <td class="math-font">10¹⁴⁰</td>
              <td>10¹⁴⁰</td>
              <td>—</td>
              <td>Asankhyeya (ଅସଂଖ୍ୟେୟ)</td>
              <td>Infinite/Incalculable Buddhist cosmic scale</td>
            </tr>
          </tbody>
        </table>
      </div>
    </section>
"""
