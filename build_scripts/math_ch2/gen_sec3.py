# -*- coding: utf-8 -*-
"""
Section 3: Rapid Revision Fact & Formula/Law Bank
"""

def get_section_3():
    return '''
    <!-- SECTION 3: RAPID REVISION FACT & FORMULA/LAW BANK -->
    <section id="section-3" class="study-section">
      <div class="section-header">
        <div class="section-icon icon-purple">
          <i class="fa-solid fa-bolt-lightning"></i>
        </div>
        <div>
          <h2>Section 3: Rapid Revision Fact &amp; Formula/Law Bank</h2>
          <p>Comprehensive reference tables containing mathematical laws, bracket rules, comparison theorems, and real-world modeling templates.</p>
        </div>
      </div>

      <!-- TABLE 1: FUNDAMENTAL LAWS -->
      <h3><i class="fa-solid fa-scale-balanced"></i> Table 1: Fundamental Mathematical Laws of Arithmetic Expressions</h3>
      <p>
        These algebraic laws form the bedrock of arithmetic expressions in Class 7 and lead directly into algebra in higher grades.
      </p>

      <div class="table-container">
        <table>
          <thead>
            <tr>
              <th>Property / Law</th>
              <th>Mathematical Formulation</th>
              <th>Plain-English Meaning</th>
              <th>Concrete Numerical Example</th>
              <th>Important Caveats</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>Commutative Property of Addition</strong></td>
              <td><span class="math-inline">a + b = b + a</span></td>
              <td>The order in which two terms are added does not alter their sum.</td>
              <td><span class="math-inline">6 + (−4) = (−4) + 6 = 2</span></td>
              <td>Does NOT hold for subtraction: <span class="math-inline">a − b ≠ b − a</span>.</td>
            </tr>
            <tr>
              <td><strong>Associative Property of Addition</strong></td>
              <td><span class="math-inline">(a + b) + c = a + (b + c)</span></td>
              <td>The way terms are grouped in an addition problem does not change the final sum.</td>
              <td><span class="math-inline">[(−7) + 10] + (−11) = (−7) + [10 + (−11)] = −8</span></td>
              <td>Does NOT hold for raw subtraction: <span class="math-inline">(a − b) − c ≠ a − (b − c)</span>.</td>
            </tr>
            <tr>
              <td><strong>Distributive Property (Over Addition)</strong></td>
              <td><span class="math-inline">a × (b + c) = a × b + a × c</span></td>
              <td>Multiplying a number by a sum equals the sum of the products of that number with each addend.</td>
              <td><span class="math-inline">5 × (4 + 3) = 5 × 4 + 5 × 3 = 20 + 15 = 35</span></td>
              <td>Works both left-to-right (expanding) and right-to-left (factoring out common term).</td>
            </tr>
            <tr>
              <td><strong>Distributive Property (Over Subtraction)</strong></td>
              <td><span class="math-inline">a × (b − c) = a × b − a × c</span></td>
              <td>Multiplying a number by a difference equals the difference of the individual products.</td>
              <td><span class="math-inline">25 × (100 − 3) = 25 × 100 − 25 × 3 = 2500 − 75 = 2425</span></td>
              <td>Ensure the subtraction sign is strictly preserved between terms.</td>
            </tr>
            <tr>
              <td><strong>Additive Inverse Property</strong></td>
              <td><span class="math-inline">a + (−a) = 0</span></td>
              <td>Every number has an opposite partner; combining them produces the zero element.</td>
              <td><span class="math-inline">14 + (−14) = 0</span></td>
              <td>Allows turning any subtraction into addition: <span class="math-inline">a − b = a + (−b)</span>.</td>
            </tr>
            <tr>
              <td><strong>Additive Identity Property</strong></td>
              <td><span class="math-inline">a + 0 = a</span></td>
              <td>Adding zero to any number or term leaves its value completely unchanged.</td>
              <td><span class="math-inline">245 + 0 = 245</span></td>
              <td>Useful in creating equivalent zero-pairs in mental arithmetic.</td>
            </tr>
            <tr>
              <td><strong>Multiplicative Identity Property</strong></td>
              <td><span class="math-inline">a × 1 = a</span></td>
              <td>Multiplying any term by 1 leaves the term unchanged.</td>
              <td><span class="math-inline">432 × 1 = 432</span></td>
              <td>Serves as the foundation for unit cost modeling.</td>
            </tr>
          </tbody>
        </table>
      </div>

      <!-- TABLE 2: BRACKET MASTER RULES -->
      <h3><i class="fa-solid fa-code-branch"></i> Table 2: Complete Bracket Removal &amp; Sign Inversion Rules</h3>
      <p>
        Use this quick reference whenever expanding or simplifying parenthetical expressions.
      </p>

      <div class="table-container">
        <table>
          <thead>
            <tr>
              <th>Bracket Pattern</th>
              <th>Preceding Sign</th>
              <th>Unpacked Result</th>
              <th>Memory Mechanism / Reason</th>
              <th>Textbook Example</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><span class="math-inline">+ (b + c)</span></td>
              <td>Positive (+)</td>
              <td><span class="math-inline">+ b + c</span></td>
              <td><strong>Identity Gate:</strong> Signs inside undergo zero change.</td>
              <td><span class="math-inline">14 + (12 + 10) = 14 + 12 + 10 = 36</span></td>
            </tr>
            <tr>
              <td><span class="math-inline">+ (b − c)</span></td>
              <td>Positive (+)</td>
              <td><span class="math-inline">+ b − c</span></td>
              <td><strong>Identity Gate:</strong> Subtraction inside remains subtraction.</td>
              <td><span class="math-inline">28 + (35 − 10) = 28 + 35 − 10 = 53</span></td>
            </tr>
            <tr>
              <td><span class="math-inline">− (b + c)</span></td>
              <td>Negative (−)</td>
              <td><span class="math-inline">− b − c</span></td>
              <td><strong>Inversion Gate:</strong> Subtracting both items in grocery cart.</td>
              <td><span class="math-inline">100 − (15 + 56) = 100 − 15 − 56 = 29</span></td>
            </tr>
            <tr>
              <td><span class="math-inline">− (b − c)</span></td>
              <td>Negative (−)</td>
              <td><span class="math-inline">− b + c</span></td>
              <td><strong>Correction of Over-Deduction:</strong> Adding back excess subtracted.</td>
              <td><span class="math-inline">500 − (250 − 100) = 500 − 250 + 100 = 350</span></td>
            </tr>
            <tr>
              <td><span class="math-inline">− (−b − c)</span></td>
              <td>Negative (−)</td>
              <td><span class="math-inline">+ b + c</span></td>
              <td><strong>Double Negative Flip:</strong> Inverting two negatives produces two positives.</td>
              <td><span class="math-inline">14 − (−12 − 10) = 14 + 12 + 10 = 36</span></td>
            </tr>
            <tr>
              <td><span class="math-inline">k × (b + c)</span></td>
              <td>Multiplier (<span class="math-inline">k</span>)</td>
              <td><span class="math-inline">k × b + k × c</span></td>
              <td><strong>Distributive Law:</strong> Scale each addend individually.</td>
              <td><span class="math-inline">2 × (43 + 24) = 2 × 43 + 2 × 24 = 134</span></td>
            </tr>
            <tr>
              <td><span class="math-inline">k × (b − c)</span></td>
              <td>Multiplier (<span class="math-inline">k</span>)</td>
              <td><span class="math-inline">k × b − k × c</span></td>
              <td><strong>Distributive Law:</strong> Scale minuend and subtrahend individually.</td>
              <td><span class="math-inline">8 × (100 − 5) = 8 × 100 − 8 × 5 = 760</span></td>
            </tr>
          </tbody>
        </table>
      </div>

      <!-- TABLE 3: MENTAL MATH SUPERHACKS -->
      <h3><i class="fa-solid fa-wand-magic-sparkles"></i> Table 3: Mental Math &amp; Fast Multiplication Superhacks</h3>
      <p>
        How to decompose stubborn two-digit and three-digit numbers into friendly multiples of 10, 50, 100, or 1000 using the distributive law.
      </p>

      <div class="table-container">
        <table>
          <thead>
            <tr>
              <th>Target Product</th>
              <th>Nearest Benchmark Base</th>
              <th>Distributive Decomposition</th>
              <th>Mental Step-by-Step Working</th>
              <th>Final Product</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><span class="math-inline">95 × 8</span></td>
              <td>100 (Difference: −5)</td>
              <td><span class="math-inline">(100 − 5) × 8</span></td>
              <td><span class="math-inline">800 − 40</span></td>
              <td><strong>760</strong></td>
            </tr>
            <tr>
              <td><span class="math-inline">104 × 15</span></td>
              <td>100 (Sum: +4)</td>
              <td><span class="math-inline">(100 + 4) × 15</span></td>
              <td><span class="math-inline">1500 + 60</span></td>
              <td><strong>1,560</strong></td>
            </tr>
            <tr>
              <td><span class="math-inline">49 × 50</span></td>
              <td>50 (Difference: −1)</td>
              <td><span class="math-inline">(50 − 1) × 50</span></td>
              <td><span class="math-inline">2500 − 50</span></td>
              <td><strong>2,450</strong></td>
            </tr>
            <tr>
              <td><span class="math-inline">63 × 18</span> (given <span class="math-inline">53 × 18 = 954</span>)</td>
              <td>53 (Sum: +10)</td>
              <td><span class="math-inline">(53 + 10) × 18</span></td>
              <td><span class="math-inline">954 + (10 × 18) = 954 + 180</span></td>
              <td><strong>1,134</strong></td>
            </tr>
            <tr>
              <td><span class="math-inline">97 × 25</span></td>
              <td>100 (Difference: −3)</td>
              <td><span class="math-inline">(100 − 3) × 25</span></td>
              <td><span class="math-inline">2500 − 75</span></td>
              <td><strong>2,425</strong></td>
            </tr>
            <tr>
              <td><span class="math-inline">103 × 9</span></td>
              <td>100 (Sum: +3)</td>
              <td><span class="math-inline">(100 + 3) × 9</span></td>
              <td><span class="math-inline">900 + 27</span></td>
              <td><strong>927</strong></td>
            </tr>
            <tr>
              <td><span class="math-inline">998 × 7</span></td>
              <td>1,000 (Difference: −2)</td>
              <td><span class="math-inline">(1000 − 2) × 7</span></td>
              <td><span class="math-inline">7000 − 14</span></td>
              <td><strong>6,986</strong></td>
            </tr>
          </tbody>
        </table>
      </div>

      <!-- TABLE 4: COMPARISON HEURISTICS -->
      <h3><i class="fa-solid fa-arrows-split-up-and-left"></i> Table 4: Structural Comparison Heuristics (Without Evaluation)</h3>
      <p>
        Exam questions frequently ask students to insert &gt;, &lt;, or = without calculating long sums. 
        Here is the decision matrix for instant evaluation:
      </p>

      <div class="table-container">
        <table>
          <thead>
            <tr>
              <th>Comparison Pair</th>
              <th>Analysis / Structural Shift</th>
              <th>Correct Symbol</th>
              <th>Logical Justification</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><span class="math-inline">245 + 289</span> vs <span class="math-inline">246 + 285</span></td>
              <td>First number increases by 1 (<span class="math-inline">245 → 246</span>), but second decreases by 4 (<span class="math-inline">289 → 285</span>). Net change = <span class="math-inline">+1 − 4 = −3</span>.</td>
              <td><strong>&gt;</strong></td>
              <td>LHS is 3 units greater than RHS.</td>
            </tr>
            <tr>
              <td><span class="math-inline">273 − 145</span> vs <span class="math-inline">272 − 144</span></td>
              <td>Minuend decreases by 1 (<span class="math-inline">273 → 272</span>), subtrahend also decreases by 1 (<span class="math-inline">145 → 144</span>).</td>
              <td><strong>=</strong></td>
              <td>Subtracting 1 less balances having 1 less originally. Both equal 128.</td>
            </tr>
            <tr>
              <td><span class="math-inline">364 + 587</span> vs <span class="math-inline">363 + 589</span></td>
              <td>First number decreases by 1 (<span class="math-inline">364 → 363</span>), second increases by 2 (<span class="math-inline">587 → 589</span>). Net change = <span class="math-inline">−1 + 2 = +1</span>.</td>
              <td><strong>&lt;</strong></td>
              <td>RHS gained 1 unit more than LHS.</td>
            </tr>
            <tr>
              <td><span class="math-inline">83 × 42 − 18</span> vs <span class="math-inline">83 × 40 − 18</span></td>
              <td>Both expressions subtract 18. In the multiplication, <span class="math-inline">83 × 42 &gt; 83 × 40</span>.</td>
              <td><strong>&gt;</strong></td>
              <td>LHS has two more groups of 83 (<span class="math-inline">+166</span>) than RHS.</td>
            </tr>
            <tr>
              <td><span class="math-inline">145 − 17 × 8</span> vs <span class="math-inline">145 − 17 × 6</span></td>
              <td>Both start at 145. LHS subtracts 8 groups of 17; RHS subtracts only 6 groups of 17.</td>
              <td><strong>&lt;</strong></td>
              <td>Subtracting a larger quantity leaves a smaller remainder!</td>
            </tr>
            <tr>
              <td><span class="math-inline">(16 − 11) × 12</span> vs <span class="math-inline">−11 × 12 + 16 × 12</span></td>
              <td>Distribute 12 on LHS: <span class="math-inline">16 × 12 − 11 × 12</span>. Commutative swap on RHS gives identical terms.</td>
              <td><strong>=</strong></td>
              <td>Identical terms by distributive law and commutativity of addition.</td>
            </tr>
            <tr>
              <td><span class="math-inline">(76 − 53) × 88</span> vs <span class="math-inline">88 × (53 − 76)</span></td>
              <td>LHS has positive factor <span class="math-inline">(76 − 53 = +23)</span>. RHS has negative factor <span class="math-inline">(53 − 76 = −23)</span>.</td>
              <td><strong>&gt;</strong></td>
              <td>A positive quantity is always strictly greater than its negative opposite!</td>
            </tr>
          </tbody>
        </table>
      </div>

      <!-- TABLE 5: REAL WORLD TRANSLATION -->
      <h3><i class="fa-solid fa-cart-shopping"></i> Table 5: Real-World Modeling Translation Guide</h3>
      <p>
        How to translate word problems into accurate mathematical expressions with proper terms and brackets.
      </p>

      <div class="table-container">
        <table>
          <thead>
            <tr>
              <th>Real-Life Situation Description</th>
              <th>English Linguistic Keyword</th>
              <th>Target Arithmetic Expression</th>
              <th>Terms Identified</th>
              <th>Final Evaluated Value</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>Mallika spends ₹25 every day on lunch from Mon to Fri (5 school days).</td>
              <td>"5 times 25" / "Product"</td>
              <td><span class="math-inline">5 × 25</span></td>
              <td>Single term: <span class="math-inline">5 × 25</span></td>
              <td>₹125</td>
            </tr>
            <tr>
              <td>Four friends buy dosas at ₹23 each and leave a ₹5 tip for the waiter.</td>
              <td>"5 more than 4 times 23"</td>
              <td><span class="math-inline">4 × 23 + 5</span></td>
              <td>Two terms: <span class="math-inline">4 × 23</span>, <span class="math-inline">5</span></td>
              <td>₹97</td>
            </tr>
            <tr>
              <td>Raghu has 4 packets of rice and packs 100 kg into 2 kg packets.</td>
              <td>"4 plus quotient of 100 and 2"</td>
              <td><span class="math-inline">4 + 100 ÷ 2</span></td>
              <td>Two terms: <span class="math-inline">4</span>, <span class="math-inline">100 ÷ 2</span></td>
              <td>54 packets</td>
            </tr>
            <tr>
              <td>Two friends each order a cutlet (₹43) and rasgulla (₹24).</td>
              <td>"Twice the combined sum"</td>
              <td><span class="math-inline">2 × (43 + 24)</span></td>
              <td>Single term with bracket: <span class="math-inline">2 × (43 + 24)</span></td>
              <td>₹134</td>
            </tr>
            <tr>
              <td>Metro ticket: ₹40 adult, ₹20 child. 4 adults and 3 children travel.</td>
              <td>"Sum of adult cost and child cost"</td>
              <td><span class="math-inline">4 × 40 + 3 × 20</span></td>
              <td>Two terms: <span class="math-inline">4 × 40</span>, <span class="math-inline">3 × 20</span></td>
              <td>₹220</td>
            </tr>
            <tr>
              <td>Binu earns ₹20,000/mo. Spends ₹5,000 rent, ₹5,000 food, ₹2,000 other. Annual savings.</td>
              <td>"12 times monthly net remainder"</td>
              <td><span class="math-inline">12 × [20000 − (5000 + 5000 + 2000)]</span></td>
              <td>Single compound term</td>
              <td>₹96,000</td>
            </tr>
            <tr>
              <td>Snail climbs 3 cm daytime, slips 2 cm night. 10 cm pole with treat on top.</td>
              <td>"Reaches top on day when morning climb hits 10 cm"</td>
              <td><span class="math-inline">7 × (3 − 2) + 3</span></td>
              <td>Two terms: <span class="math-inline">7 × 1</span> and <span class="math-inline">3</span></td>
              <td>Day 8 (No slip once treat reached!)</td>
            </tr>
          </tbody>
        </table>
      </div>
    </section>
'''
