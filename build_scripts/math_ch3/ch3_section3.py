# -*- coding: utf-8 -*-
"""
Module: ch3_section3.py
Contains Section 3: Rapid Revision Fact & Formula/Law Bank.
Includes 6 comprehensive, beautifully styled markdown/HTML comparison tables.
"""

def get_section_3():
    return """
    <!-- ======================================================== -->
    <!-- SECTION 3: RAPID REVISION FACT & FORMULA/LAW BANK        -->
    <!-- ======================================================== -->
    <section id="section-3">
      <div class="section-header">
        <span class="section-badge"><i class="fa-solid fa-vault"></i> Rapid Memory Bank</span>
        <h2 class="section-title">Section 3: Rapid Revision Fact & Formula/Law Bank</h2>
        <p class="section-desc">
          Structured comparative tables, mathematical laws of base systems, chronological timelines, and multi-base equivalence charts for instant pre-exam recall.
        </p>
      </div>

      <!-- TABLE 3.1: MASTER COMPARATIVE MATRIX OF WORLD NUMBER SYSTEMS -->
      <h4><i class="fa-solid fa-table-cells-large" style="color: var(--primary);"></i> Table 3.1: Master Comparative Matrix of World Number Systems</h4>
      <div class="table-wrapper">
        <table>
          <thead>
            <tr>
              <th>Civilization / System</th>
              <th>Base (n)</th>
              <th>Landmark Symbols Used</th>
              <th>Place Value?</th>
              <th>Zero Concept?</th>
              <th>Major Computational Advantage</th>
              <th>Fatal Mathematical Limitation</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>Prehistoric Tallies (Lebombo / Ishango)</strong></td>
              <td>None (1)</td>
              <td>Carved notches / cuts on bones</td>
              <td><span style="color: var(--danger-dark); font-weight: 700;">No</span></td>
              <td><span style="color: var(--danger-dark); font-weight: 700;">No</span></td>
              <td>Direct 1-to-1 physical correlation; durable permanent record</td>
              <td>Extremely tedious; unwieldy for sets larger than 30–40</td>
            </tr>
            <tr>
              <td><strong>Gumulgal Tribe (Australia)</strong></td>
              <td>2 (Group size)</td>
              <td>urapon (1), ukasar (2)</td>
              <td><span style="color: var(--danger-dark); font-weight: 700;">No</span></td>
              <td><span style="color: var(--danger-dark); font-weight: 700;">No</span></td>
              <td>Compounds describe counts up to 6 using only two spoken words</td>
              <td>No names beyond 6 (termed <em>ras</em> - "many")</td>
            </tr>
            <tr>
              <td><strong>Roman Numerals (Rome, 8th c. BCE)</strong></td>
              <td>Mixed (5, 10)</td>
              <td>I, V, X, L, C, D, M</td>
              <td><span style="color: var(--danger-dark); font-weight: 700;">No</span> (Additive)</td>
              <td><span style="color: var(--danger-dark); font-weight: 700;">No</span></td>
              <td>Compact stone monument engravings; clear subtractive rules</td>
              <td>Multiplication & division nearly impossible without an abacus</td>
            </tr>
            <tr>
              <td><strong>Egyptian Hieroglyphic (3000 BCE)</strong></td>
              <td>10 (Decimal)</td>
              <td>7 Hieroglyphs (Stroke, Heel, Coil, Lotus, Finger, Frog, God)</td>
              <td><span style="color: var(--danger-dark); font-weight: 700;">No</span> (Additive)</td>
              <td><span style="color: var(--danger-dark); font-weight: 700;">No</span></td>
              <td>Landmark powers 10⁰ to 10⁶; 10 of any symbol = 1 next symbol</td>
              <td>Requires endless creation of new symbols for higher powers</td>
            </tr>
            <tr>
              <td><strong>Mesopotamian / Babylonian (2000 BCE)</strong></td>
              <td>60 (Sexagesimal)</td>
              <td>Wedge (▼ = 1) and Corner (◄ = 10)</td>
              <td><span style="color: #16a34a; font-weight: 700;">Yes</span> (Positional)</td>
              <td>Blank space / Slanted double-wedge</td>
              <td>Divisible by 1, 2, 3, 4, 5, 6, 10, 12, 15, 20, 30; perfect for fractions</td>
              <td>No terminal zero; blank spaces created ambiguity (e.g. 62 vs 3602)</td>
            </tr>
            <tr>
              <td><strong>Mayan Vigesimal (300–900 CE)</strong></td>
              <td>20 (3rd tier = 360)</td>
              <td>Seashell (0), Dot (1), Bar (— = 5)</td>
              <td><span style="color: #16a34a; font-weight: 700;">Yes</span> (Vertical)</td>
              <td><span style="color: #16a34a; font-weight: 700;">Yes</span> (Seashell placeholder)</td>
              <td>True positional zero placeholder; solar calendar harmony (360 days)</td>
              <td>Irregular 3rd tier (360 instead of 400) ruined general base arithmetic</td>
            </tr>
            <tr>
              <td><strong>Chinese Rod Numerals (3rd c. BCE)</strong></td>
              <td>10 (Decimal)</td>
              <td>Bamboo rods in Zong (Vertical) & Heng (Horizontal)</td>
              <td><span style="color: #16a34a; font-weight: 700;">Yes</span> (Positional)</td>
              <td>Empty grid square / later 〇</td>
              <td>Alternating rod directions eliminated adjacent digit collision</td>
              <td>Physical rods can be displaced; requires counting board surface</td>
            </tr>
            <tr>
              <td><strong>Hindu Number System (India, c. 200 BCE–628 CE)</strong></td>
              <td>10 (Decimal)</td>
              <td>Ten Universal Digits: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9</td>
              <td><span style="color: #16a34a; font-weight: 700;">Yes</span> (Universal)</td>
              <td><span style="color: #16a34a; font-weight: 700;">Yes</span> (Placeholder + Ring Number)</td>
              <td>Only 10 digits express all quantities; lightning-fast arithmetic algorithms</td>
              <td><strong>None!</strong> Accepted as the universal standard for all humanity!</td>
            </tr>
          </tbody>
        </table>
      </div>

      <!-- TABLE 3.2: LANDMARK NUMBERS ACROSS DIFFERENT BASES -->
      <h4><i class="fa-solid fa-calculator" style="color: var(--secondary);"></i> Table 3.2: Powers and Landmark Numbers Across Bases (n⁰ to n⁵)</h4>
      <div class="table-wrapper">
        <table>
          <thead>
            <tr>
              <th>Base System</th>
              <th>Base (n)</th>
              <th>n⁰ (1st Landmark)</th>
              <th>n¹ (2nd Landmark)</th>
              <th>n² (3rd Landmark)</th>
              <th>n³ (4th Landmark)</th>
              <th>n⁴ (5th Landmark)</th>
              <th>n⁵ (6th Landmark)</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>Binary (Base-2)</strong></td>
              <td>n = 2</td>
              <td>1</td>
              <td>2</td>
              <td>4</td>
              <td>8</td>
              <td>16</td>
              <td>32</td>
            </tr>
            <tr>
              <td><strong>Base-4</strong></td>
              <td>n = 4</td>
              <td>1</td>
              <td>4</td>
              <td>16</td>
              <td>64</td>
              <td>256</td>
              <td>1,024</td>
            </tr>
            <tr>
              <td><strong>Base-5 (Quinary)</strong></td>
              <td>n = 5</td>
              <td>1</td>
              <td>5</td>
              <td>25</td>
              <td>125</td>
              <td>625</td>
              <td>3,125</td>
            </tr>
            <tr>
              <td><strong>Base-7 (Septenary)</strong></td>
              <td>n = 7</td>
              <td>1</td>
              <td>7</td>
              <td>49</td>
              <td>343</td>
              <td>2,401</td>
              <td>16,807</td>
            </tr>
            <tr>
              <td><strong>Octal (Base-8)</strong></td>
              <td>n = 8</td>
              <td>1</td>
              <td>8</td>
              <td>64</td>
              <td>512</td>
              <td>4,096</td>
              <td>32,768</td>
            </tr>
            <tr>
              <td><strong>Decimal (Base-10)</strong></td>
              <td>n = 10</td>
              <td>1</td>
              <td>10</td>
              <td>100</td>
              <td>1,000</td>
              <td>10,000</td>
              <td>100,000</td>
            </tr>
            <tr>
              <td><strong>Pure Base-20 (Vigesimal)</strong></td>
              <td>n = 20</td>
              <td>1</td>
              <td>20</td>
              <td>400</td>
              <td>8,000</td>
              <td>160,000</td>
              <td>3,200,000</td>
            </tr>
            <tr>
              <td><strong>Mayan Base-20 (Calendar)</strong></td>
              <td>n = 20*</td>
              <td>1</td>
              <td>20</td>
              <td><strong>360</strong> (18×20)</td>
              <td><strong>7,200</strong> (360×20)</td>
              <td><strong>144,000</strong></td>
              <td><strong>2,880,000</strong></td>
            </tr>
            <tr>
              <td><strong>Sexagesimal (Base-60)</strong></td>
              <td>n = 60</td>
              <td>1</td>
              <td>60</td>
              <td>3,600</td>
              <td>216,000</td>
              <td>12,960,000</td>
              <td>777,600,000</td>
            </tr>
          </tbody>
        </table>
      </div>

      <!-- TABLE 3.3: DECIMAL PLACE-VALUE VS ADDITIVE/GROUPING SYSTEMS -->
      <h4><i class="fa-solid fa-code-compare" style="color: var(--purple);"></i> Table 3.3: Additive Systems vs Positional Decimal Place-Value</h4>
      <div class="table-wrapper">
        <table>
          <thead>
            <tr>
              <th>Evaluation Parameter</th>
              <th>Additive Systems (Egyptian / Roman)</th>
              <th>Positional Decimal System (Hindu System)</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>Total Unique Digits Needed</strong></td>
              <td>Infinite (new symbols must be invented for every new power)</td>
              <td>Exactly <strong>ten finite digits</strong> (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)</td>
            </tr>
            <tr>
              <td><strong>Role of Position</strong></td>
              <td>Does not determine power (e.g. <code>XI</code> and <code>IX</code> use position only for subtraction)</td>
              <td><strong>Position is supreme</strong>: shifts value by a factor of 10 for every column to the left</td>
            </tr>
            <tr>
              <td><strong>Compactness of Writing</strong></td>
              <td>Very bulky (e.g., 2999 requires 15 characters: <code>MMCMXCIX</code>)</td>
              <td>Extremely compact (e.g., <code>2999</code> requires just 4 digits)</td>
            </tr>
            <tr>
              <td><strong>Algorithm for Addition</strong></td>
              <td>Physical gathering of symbols and manual regrouping</td>
              <td>Standard column-by-column carry-over algorithm</td>
            </tr>
            <tr>
              <td><strong>Algorithm for Multiplication</strong></td>
              <td>Extremely cumbersome; requires repeated doubling or abacus</td>
              <td>Compact cross-multiplication and column shifting</td>
            </tr>
            <tr>
              <td><strong>Handling Zero / Empty Columns</strong></td>
              <td>Omitted entirely; impossible to distinguish without context</td>
              <td>Digit <code>0</code> acts as a rock-solid, unambiguous placeholder</td>
            </tr>
          </tbody>
        </table>
      </div>

      <!-- TABLE 3.4: CHRONOLOGICAL MASTER TIMELINE -->
      <h4><i class="fa-solid fa-timeline" style="color: var(--accent-dark);"></i> Table 3.4: Chronological Master Timeline of Human Number Evolution</h4>
      <div class="table-wrapper">
        <table>
          <thead>
            <tr>
              <th>Approximate Date</th>
              <th>Historical Milestone / Discovery</th>
              <th>Geographical Region</th>
              <th>Key Significance to Modern Mathematics</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>~44,000 BCE</strong></td>
              <td>Lebombo Bone Artifact</td>
              <td>Border Cave, South Africa</td>
              <td>29 notches on baboon fibula; world's oldest mathematical tally and lunar calendar.</td>
            </tr>
            <tr>
              <td><strong>~25,000 BCE</strong></td>
              <td>Ishango Bone Artifact</td>
              <td>Lake Edward, DR Congo</td>
              <td>Notches arranged in grouped columns exhibiting primes and doubling patterns.</td>
            </tr>
            <tr>
              <td><strong>~3,000 BCE</strong></td>
              <td>Egyptian Hieroglyphic Numerals</td>
              <td>Nile River Valley, Egypt</td>
              <td>First base-10 system with landmark symbols for powers 10⁰ to 10⁶.</td>
            </tr>
            <tr>
              <td><strong>~2,000 BCE</strong></td>
              <td>Babylonian Sexagesimal Cuneiform</td>
              <td>Mesopotamia (Iraq)</td>
              <td>First place-value system (Base-60); origin of 60 seconds, 60 minutes, and 360° circle.</td>
            </tr>
            <tr>
              <td><strong>~1,500 BCE</strong></td>
              <td>Vedic Decadic Oral Hierarchy</td>
              <td>Ancient India (Yajurveda)</td>
              <td>Oral number names based on powers of 10 from eka (10⁰) to parārdha (10¹²).</td>
            </tr>
            <tr>
              <td><strong>~8th c. BCE</strong></td>
              <td>Roman Numeral System</td>
              <td>Ancient Rome, Italy</td>
              <td>Landmark additive/subtractive system (I, V, X, L, C, D, M) widespread across Europe.</td>
            </tr>
            <tr>
              <td><strong>~3rd c. BCE</strong></td>
              <td>Chinese Rod Numerals (Suàn Chóu)</td>
              <td>Ancient China</td>
              <td>Base-10 positional computing system with alternating Zong and Heng orientations.</td>
            </tr>
            <tr>
              <td><strong>~300–900 CE</strong></td>
              <td>Mayan Vigesimal System</td>
              <td>Central America (Mesoamerica)</td>
              <td>Independent invention of place-value with a seashell zero placeholder and solar 360s tier.</td>
            </tr>
            <tr>
              <td><strong>~3rd–4th c. CE</strong></td>
              <td>The Bakhshali Manuscript</td>
              <td>Khyber Pakhtunkhwa, India</td>
              <td>Oldest physical birch-bark document featuring zero written as a solid dot (śūnya-bindu).</td>
            </tr>
            <tr>
              <td><strong>499 CE</strong></td>
              <td>Aryabhata's <em>Āryabhaṭīya</em></td>
              <td>Kusumapura (Patna), India</td>
              <td>Formulation of decimal place-value: <em>“Sthānāt sthānaṁ daśaguṇaṁ syāt”</em>.</td>
            </tr>
            <tr>
              <td><strong>628 CE</strong></td>
              <td>Brahmagupta's <em>Brāhmasphuṭasiddhānta</em></td>
              <td>Bhinmal (Rajasthan), India</td>
              <td>First codified arithmetic operational laws of zero (śūnya), negatives (ṛṇa), and positives (dhana).</td>
            </tr>
            <tr>
              <td><strong>c. 825 CE</strong></td>
              <td>Al-Khwārizmī’s Hindu Numeral Treatise</td>
              <td>House of Wisdom, Baghdad</td>
              <td>Spread Indian mathematics to the Islamic world; origin of the term <em>algorithm</em>.</td>
            </tr>
            <tr>
              <td><strong>1202 CE</strong></td>
              <td>Fibonacci’s <em>Liber Abaci</em></td>
              <td>Pisa, Italy</td>
              <td>Advocated Hindu-Arabic numerals across Europe, replacing Roman numerals in trade.</td>
            </tr>
            <tr>
              <td><strong>1814 CE</strong></td>
              <td>Pierre-Simon Laplace's Tribute</td>
              <td>Paris, France</td>
              <td>Hailed India's invention of zero and place value as the supreme masterstroke of arithmetic.</td>
            </tr>
          </tbody>
        </table>
      </div>

      <!-- TABLE 3.5: BRAHMAGUPTA'S CODIFIED LAWS OF ZERO -->
      <h4><i class="fa-solid fa-circle-nodes" style="color: #dc2626;"></i> Table 3.5: Brahmagupta's Algebraic Laws of Zero and Integers (628 CE)</h4>
      <div class="table-wrapper">
        <table>
          <thead>
            <tr>
              <th>Operation</th>
              <th>Sanskrit Codified Principle</th>
              <th>Modern Algebraic Formula</th>
              <th>Pedagogical Explanation</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>Addition with Zero</strong></td>
              <td>Adding zero to positive gives positive; adding zero to negative gives negative.</td>
              <td><code class="math-code">a + 0 = a</code> &nbsp; and &nbsp; <code class="math-code">(-a) + 0 = -a</code></td>
              <td>Zero is the additive identity element: adding nothing leaves the quantity unchanged.</td>
            </tr>
            <tr>
              <td><strong>Self-Cancellation (Origin of 0)</strong></td>
              <td>A positive minus positive of equal magnitude is zero; negative minus negative is zero.</td>
              <td><code class="math-code">a - a = 0</code> &nbsp; and &nbsp; <code class="math-code">(-a) - (-a) = 0</code></td>
              <td>A debt (ṛṇa) repaid by an equal fortune (dhana) results in complete balance (śūnya).</td>
            </tr>
            <tr>
              <td><strong>Subtraction with Zero</strong></td>
              <td>Subtracting zero from any number leaves it unchanged; subtracting a number from zero reverses sign.</td>
              <td><code class="math-code">a - 0 = a</code> &nbsp; and &nbsp; <code class="math-code">0 - a = -a</code></td>
              <td>Taking away nothing changes nothing; removing a positive from void creates a debt (negative).</td>
            </tr>
            <tr>
              <td><strong>Multiplication by Zero</strong></td>
              <td>The product of zero and positive, or zero and negative, is zero.</td>
              <td><code class="math-code">a × 0 = 0</code> &nbsp; and &nbsp; <code class="math-code">(-a) × 0 = 0</code></td>
              <td>Repeating any quantity zero times results in total emptiness.</td>
            </tr>
            <tr>
              <td><strong>Multiplication of Signs</strong></td>
              <td>Product of two fortunes is a fortune; product of two debts is a fortune!</td>
              <td><code class="math-code">(+a) × (+b) = +ab</code> <br> <code class="math-code">(-a) × (-b) = +ab</code></td>
              <td>First historical enunciation of the rule: negative times negative equals positive!</td>
            </tr>
            <tr>
              <td><strong>Division by Zero (Modern Correction)</strong></td>
              <td>Brahmagupta wrote 0 ÷ 0 = 0, but modern mathematics proves division by zero is <strong>undefined</strong>.</td>
              <td><code class="math-code">a ÷ 0 = \text{Undefined}</code> (for a ≠ 0)</td>
              <td>If a/0 = k, then k × 0 = a. Since k × 0 = 0 for all numbers, no finite unique k can exist!</td>
            </tr>
          </tbody>
        </table>
      </div>

      <!-- TABLE 3.6: MULTI-BASE NUMBER CONVERSION REFERENCE -->
      <h4><i class="fa-solid fa-arrow-right-arrow-left" style="color: #0369a1;"></i> Table 3.6: Multi-Base Number Conversion Reference (Decimal 0 to 25)</h4>
      <div class="table-wrapper">
        <table>
          <thead>
            <tr>
              <th>Base-10 (Decimal)</th>
              <th>Base-2 (Binary)</th>
              <th>Base-5 (Quinary)</th>
              <th>Base-8 (Octal)</th>
              <th>Mesopotamian (Base-60)</th>
              <th>Roman Numeral</th>
            </tr>
          </thead>
          <tbody>
            <tr><td><strong>0</strong></td><td><code>0</code></td><td><code>0</code></td><td><code>0</code></td><td>(Blank / Placeholder)</td><td><em>(None)</em></td></tr>
            <tr><td><strong>1</strong></td><td><code>1</code></td><td><code>1</code></td><td><code>1</code></td><td>▼</td><td>I</td></tr>
            <tr><td><strong>2</strong></td><td><code>10</code></td><td><code>2</code></td><td><code>2</code></td><td>▼▼</td><td>II</td></tr>
            <tr><td><strong>3</strong></td><td><code>11</code></td><td><code>3</code></td><td><code>3</code></td><td>▼▼▼</td><td>III</td></tr>
            <tr><td><strong>4</strong></td><td><code>100</code></td><td><code>4</code></td><td><code>4</code></td><td>▼▼▼▼</td><td>IV</td></tr>
            <tr><td><strong>5</strong></td><td><code>101</code></td><td><code>10</code></td><td><code>5</code></td><td>▼▼▼▼▼</td><td>V</td></tr>
            <tr><td><strong>6</strong></td><td><code>110</code></td><td><code>11</code></td><td><code>6</code></td><td>▼▼▼▼▼▼</td><td>VI</td></tr>
            <tr><td><strong>7</strong></td><td><code>111</code></td><td><code>12</code></td><td><code>7</code></td><td>▼▼▼▼▼▼▼</td><td>VII</td></tr>
            <tr><td><strong>8</strong></td><td><code>1000</code></td><td><code>13</code></td><td><code>10</code></td><td>▼▼▼▼▼▼▼▼</td><td>VIII</td></tr>
            <tr><td><strong>9</strong></td><td><code>1001</code></td><td><code>14</code></td><td><code>11</code></td><td>▼▼▼▼▼▼▼▼▼</td><td>IX</td></tr>
            <tr><td><strong>10</strong></td><td><code>1010</code></td><td><code>20</code></td><td><code>12</code></td><td>◄</td><td>X</td></tr>
            <tr><td><strong>11</strong></td><td><code>1011</code></td><td><code>21</code></td><td><code>13</code></td><td>◄ ▼</td><td>XI</td></tr>
            <tr><td><strong>12</strong></td><td><code>1100</code></td><td><code>22</code></td><td><code>14</code></td><td>◄ ▼▼</td><td>XII</td></tr>
            <tr><td><strong>13</strong></td><td><code>1101</code></td><td><code>23</code></td><td><code>15</code></td><td>◄ ▼▼▼</td><td>XIII</td></tr>
            <tr><td><strong>14</strong></td><td><code>1110</code></td><td><code>24</code></td><td><code>16</code></td><td>◄ ▼▼▼▼</td><td>XIV</td></tr>
            <tr><td><strong>15</strong></td><td><code>1111</code></td><td><code>30</code></td><td><code>17</code></td><td>◄ ▼▼▼▼▼</td><td>XV</td></tr>
            <tr><td><strong>16</strong></td><td><code>10000</code></td><td><code>31</code></td><td><code>20</code></td><td>◄ ▼▼▼▼▼▼</td><td>XVI</td></tr>
            <tr><td><strong>17</strong></td><td><code>10001</code></td><td><code>32</code></td><td><code>21</code></td><td>◄ ▼▼▼▼▼▼▼</td><td>XVII</td></tr>
            <tr><td><strong>18</strong></td><td><code>10010</code></td><td><code>33</code></td><td><code>22</code></td><td>◄ ▼▼▼▼▼▼▼▼</td><td>XVIII</td></tr>
            <tr><td><strong>19</strong></td><td><code>10011</code></td><td><code>34</code></td><td><code>23</code></td><td>◄ ▼▼▼▼▼▼▼▼▼</td><td>XIX</td></tr>
            <tr><td><strong>20</strong></td><td><code>10100</code></td><td><code>40</code></td><td><code>24</code></td><td>◄◄</td><td>XX</td></tr>
            <tr><td><strong>21</strong></td><td><code>10101</code></td><td><code>41</code></td><td><code>25</code></td><td>◄◄ ▼</td><td>XXI</td></tr>
            <tr><td><strong>22</strong></td><td><code>10110</code></td><td><code>42</code></td><td><code>26</code></td><td>◄◄ ▼▼</td><td>XXII</td></tr>
            <tr><td><strong>23</strong></td><td><code>10111</code></td><td><code>43</code></td><td><code>27</code></td><td>◄◄ ▼▼▼</td><td>XXIII</td></tr>
            <tr><td><strong>24</strong></td><td><code>11000</code></td><td><code>44</code></td><td><code>30</code></td><td>◄◄ ▼▼▼▼</td><td>XXIV</td></tr>
            <tr><td><strong>25</strong></td><td><code>11001</code></td><td><code>100</code></td><td><code>31</code></td><td>◄◄ ▼▼▼▼▼</td><td>XXV</td></tr>
          </tbody>
        </table>
      </div>

    </section>
"""
