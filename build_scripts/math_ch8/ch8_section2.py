# -*- coding: utf-8 -*-
"""
Module: ch8_section2.py
Contains Section 2: Complete Line-by-Line Conceptual Explanations & Exhaustive Bilingual
Vocabulary/Glossary Table (30 technical terms) with authentic Odia textbook terminology.
"""

def get_section2():
    return """
    <!-- ========================================== -->
    <!-- SECTION 2: CONCEPTS & BILINGUAL GLOSSARY   -->
    <!-- ========================================== -->
    <section id="section2">
      <div class="section-header">
        <div class="section-tag"><i class="fa-solid fa-lightbulb"></i> Conceptual Foundations</div>
        <h2 class="section-title">Section 2: Complete Line-by-Line Conceptual Explanations</h2>
        <p class="section-desc">
          Every concept explained in crystal-clear, friendly language with zero jargon, intuitive real-world analogies, step-by-step mathematical reasoning, and an exhaustive bilingual English-Odia glossary.
        </p>
      </div>

      <!-- CONCEPT 2.1 -->
      <h3 class="subheading"><i class="fa-solid fa-mask"></i> 2.1 The True Meaning of "Percent" &amp; The Great Disguise</h3>
      <p>
        Imagine you go to a market during the Durga Puja festival and see a big colorful banner: <strong>“Mega Clearance Sale — Up to 50% Off!”</strong>. Later that evening, your sister proudly tells the family: <strong>“I scored 83% in my Grade 8 board exams!”</strong>
      </p>
      <p>
        What do these percentages actually mean? The word <strong>percent</strong> comes directly from two ancient Latin words: <em>per</em> (meaning "for each" or "out of") and <em>centum</em> (meaning "one hundred"). Therefore, <strong>percent literally means "out of one hundred"</strong>.
      </p>

      <div class="callout callout-def">
        <div class="callout-title"><i class="fa-solid fa-book-bookmark"></i> Formal Definition: Percentage as a Fraction</div>
        <p>
          A <strong>percentage</strong> is simply a fraction whose denominator is fixed at <strong>100</strong>. It is denoted by the universal symbol <strong>‘%’</strong> (pronounced <em>per cent</em>).
        </p>
        <p style="font-family: 'JetBrains Mono', monospace; font-size: 1.1rem; font-weight: 700; color: #1e3a8a; margin: 0.5rem 0;">
          x% = x / 100 = 0.01 × x
        </p>
        <p>
          When you say <strong>50%</strong>, you are secretly saying <strong>50/100</strong> (which simplifies to 1/2). When you say <strong>83%</strong>, you are secretly saying <strong>83/100</strong> (or 0.83). The percentage sign ‘%’ is just a festive mask or <em>disguise</em> worn by a fraction with denominator 100!
        </p>
      </div>

      <div class="callout callout-hack">
        <div class="callout-title"><i class="fa-solid fa-lightbulb"></i> Why Do We Need Percentages? Why Not Just Keep Using Fractions?</div>
        <p>
          Let us look at a real puzzle from a biscuit-making bakery:
        </p>
        <ul>
          <li><strong>Variety 1:</strong> Sugar makes up <strong>9 / 34</strong> of the total weight.</li>
          <li><strong>Variety 2:</strong> Sugar makes up <strong>13 / 45</strong> of the total weight.</li>
        </ul>
        <p>
          Which variety is sweeter? At a glance, nobody can easily tell! The denominators 34 and 45 are completely different. To compare them as fractions, you would have to find the Least Common Multiple (LCM) of 34 and 45 (which is 1530!), multiply large numbers, and spend five minutes doing tedious long division.
        </p>
        <p>
          Now, let us put them in their percentage disguise:
        </p>
        <ul>
          <li><strong>Variety 1:</strong> (9 ÷ 34) × 100 = <strong>26.47%</strong></li>
          <li><strong>Variety 2:</strong> (13 ÷ 45) × 100 = <strong>28.88%</strong></li>
        </ul>
        <p>
          Immediately, within one second, any school child can see that <strong>Variety 2 is sweeter</strong> because 28.88 is greater than 26.47! Percentages create a <strong>level playing field</strong> by scaling every fraction to a common baseline of 100.
        </p>
      </div>

      <div class="callout callout-def">
        <div class="callout-title"><i class="fa-solid fa-scale-balanced"></i> Why Choose 100? The Proportional Metric Scale</div>
        <p>
          Could we choose a denominator of 10, 50, 1000, or 43 instead? In theory, yes! But 100 is magical for four specific reasons:
        </p>
        <ol>
          <li><strong>Decimal Harmony:</strong> Our entire numbering system is Base 10. The number 100 is 10², which fits decimals like a glove: <code>31% = 31/100 = 0.31</code>. You just slide the decimal point two places!</li>
          <li><strong>The "Sweet Spot" of Granularity:</strong> "Per 10" (<em>per decem</em>) is too small to show fine differences (9/34 would be 2.6 out of 10). "Per 1,000" (<em>per mille</em>, ‰) is used in ocean salinity and birth rates, but numbers become unnecessarily large for shopping. <strong>100 is large enough to give fine detail, yet small enough to visualize mentally!</strong></li>
        </ol>
      </div>

      <!-- CONCEPT 2.2 -->
      <h3 class="subheading"><i class="fa-solid fa-arrows-split-up-and-left"></i> 2.2 The FDP Rosetta Stone: Converting Fractions, Decimals, and Percentages</h3>
      <p>
        Fractions, decimals, and percentages are three different dialects of the very same mathematical language. A master student must be able to switch between them instantly.
      </p>

      <div class="callout callout-act">
        <div class="callout-title"><i class="fa-solid fa-route"></i> Three Equivalent Methods to Turn a Fraction into a Percentage</div>
        <p>Suppose Surya wants to save <strong>3 / 5</strong> of his prize money to buy canvas boards. What percentage is he saving?</p>
        <ol>
          <li>
            <strong>Method 1: Equivalent Fraction with Denominator 100:</strong><br>
            We find what number multiplies 5 to make 100. Since 100 ÷ 5 = 20, we multiply both numerator and denominator by 20:<br>
            <code>(3 × 20) / (5 × 20) = 60 / 100 = 60%</code>.
          </li>
          <li>
            <strong>Method 2: Unitary Method (Step-by-Step Scaling):</strong><br>
            Out of 5 parts, Surya saves 3 parts.<br>
            Out of 1 part, he saves 3 / 5 parts.<br>
            Out of 100 parts, he saves (3 / 5) × 100 = 3 × 20 = <strong>60%</strong>.
          </li>
          <li>
            <strong>Method 3: Direct 100% Multiplication:</strong><br>
            Since 100% equals 100/100 = 1, multiplying any number by 100% does not change its value at all!<br>
            <code>(3 / 5) × 100% = (300 / 5)% = 60%</code>.
          </li>
        </ol>
      </div>

      <div class="callout callout-hack">
        <div class="callout-title"><i class="fa-solid fa-repeat"></i> Handling Repeating / Non-Terminating Decimals</div>
        <p>
          Some fractions do not divide cleanly into terminating decimals because their denominators contain prime factors other than 2 or 5:
        </p>
        <ul>
          <li><code>1 / 3 = 0.3333... = 33.33% = 33 ⅓%</code></li>
          <li><code>2 / 3 = 0.6666... = 66.67% = 66 ⅔%</code></li>
          <li><code>1 / 6 = 0.1666... = 16.67% = 16 ⅔%</code></li>
          <li><code>5 / 11 = 0.4545... = 45.45% = 45 ⁵/₁₁%</code></li>
        </ul>
        <p>In Grade 8 exams, you can write the answer either rounded to two decimal places (e.g., 33.33%) or as a mixed fraction percentage (33 ⅓%).</p>
      </div>

      <!-- CONCEPT 2.3 -->
      <h3 class="subheading"><i class="fa-solid fa-calculator"></i> 2.3 Finding Percentage of a Quantity &amp; Free-Hand Mental Toolkit</h3>
      <p>
        When someone asks you: <em>“What is 25% of 120 grams?”</em>, how should you think?
      </p>
      <p>
        Mathematically, the word <strong>“of”</strong> in mathematics always means <strong>multiplication (×)</strong>.
      </p>
      <div style="background: #f1f5f9; padding: 1rem 1.5rem; border-radius: var(--radius-md); font-family: 'JetBrains Mono', monospace; font-size: 1.05rem; margin: 1rem 0; border: 1px solid var(--border);">
        y% of Q = (y / 100) × Q = 0.01 × y × Q
      </div>
      <p>
        Therefore, 25% of 120 g = (25/100) × 120 = (1/4) × 120 = <strong>30 grams</strong>.
      </p>

      <div class="callout callout-hack">
        <div class="callout-title"><i class="fa-solid fa-wand-magic-sparkles"></i> The Free-Hand Mental Math Toolkit (No Pen &amp; Paper Needed!)</div>
        <p>
          To be lightning fast in exams and daily life, master these <strong>mental benchmark anchors</strong>:
        </p>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 1rem; margin-top: 0.75rem;">
          <div style="background: #ffffff; padding: 0.85rem; border-radius: var(--radius-sm); border: 1px solid #cbd5e1;">
            <strong style="color: #4338ca;">10% Anchor (Slide 1 place left):</strong><br>
            To find 10% of any number, just divide by 10 (shift decimal point 1 place left).<br>
            <em>Example:</em> 10% of 280 = <strong>28</strong>. 10% of 35 = <strong>3.5</strong>.
          </div>
          <div style="background: #ffffff; padding: 0.85rem; border-radius: var(--radius-sm); border: 1px solid #cbd5e1;">
            <strong style="color: #0d9488;">1% Anchor (Slide 2 places left):</strong><br>
            To find 1% of any number, just divide by 100 (shift decimal point 2 places left).<br>
            <em>Example:</em> 1% of 280 = <strong>2.8</strong>. 1% of 35 = <strong>0.35</strong>.
          </div>
          <div style="background: #ffffff; padding: 0.85rem; border-radius: var(--radius-sm); border: 1px solid #cbd5e1;">
            <strong style="color: #d97706;">5% Benchmark (Half of 10%):</strong><br>
            Find 10% first, then take half!<br>
            <em>Example:</em> For 80: 10% is 8, so 5% is <strong>4</strong>.
          </div>
          <div style="background: #ffffff; padding: 0.85rem; border-radius: var(--radius-sm); border: 1px solid #cbd5e1;">
            <strong style="color: #7c3aed;">20% Benchmark (Double of 10%):</strong><br>
            Find 10% first, then double it!<br>
            <em>Example:</em> For 80: 10% is 8, so 20% is 8 × 2 = <strong>16</strong>.
          </div>
          <div style="background: #ffffff; padding: 0.85rem; border-radius: var(--radius-sm); border: 1px solid #cbd5e1;">
            <strong style="color: #059669;">25% Benchmark (Quarter / Half of Half):</strong><br>
            Divide the number by 4 (or halve it, then halve again).<br>
            <em>Example:</em> 25% of 80 = 80 ÷ 4 = <strong>20</strong>.
          </div>
          <div style="background: #ffffff; padding: 0.85rem; border-radius: var(--radius-sm); border: 1px solid #cbd5e1;">
            <strong style="color: #b91c1c;">15% Benchmark (10% + 5% Combo):</strong><br>
            Take 10% and add 5% to it!<br>
            <em>Example:</em> For 80: 10% is 8, 5% is 4. So 15% is 8 + 4 = <strong>12</strong>!
          </div>
        </div>
      </div>

      <!-- CONCEPT 2.4 -->
      <h3 class="subheading"><i class="fa-solid fa-shuffle"></i> 2.4 The Commutative Property: x% of y = y% of x</h3>
      <p>
        Here is one of the most astonishing and elegant secrets in all of arithmetic:
      </p>
      <div class="callout callout-def">
        <div class="callout-title"><i class="fa-solid fa-infinity"></i> Algebraic Proof of Commutativity</div>
        <p>
          Let <em>x</em> and <em>y</em> be any two numbers. Then:
        </p>
        <p style="font-family: 'JetBrains Mono', monospace; font-size: 1.05rem; font-weight: 700; color: #1e3a8a;">
          x% of y = (x / 100) × y = (x × y) / 100
        </p>
        <p>
          Because standard multiplication of numbers is commutative (<em>x × y = y × x</em>), we can rewrite the numerator:
        </p>
        <p style="font-family: 'JetBrains Mono', monospace; font-size: 1.05rem; font-weight: 700; color: #1e3a8a;">
          (x × y) / 100 = (y × x) / 100 = (y / 100) × x = y% of x.
        </p>
        <p>
          <strong>Conclusion:</strong> Calculating <code>x% of y</code> gives the exact same result as calculating <code>y% of x</code>!
        </p>
      </div>

      <p>
        <strong>Why is this useful?</strong> Because sometimes one calculation looks terrifying, but its reversed version is child's play!
      </p>
      <ul>
        <li><strong>Question:</strong> What is <strong>16% of 50</strong>?</li>
        <li><strong>The Hard Way:</strong> 16 × 50 ÷ 100 = 800 ÷ 100 = 8 (requires scratch paper).</li>
        <li><strong>The Genius Commutative Way:</strong> Flip it! <strong>16% of 50 = 50% of 16</strong>. And 50% of 16 is just half of 16, which is <strong>8</strong>! Done mentally in under 1 second!</li>
        <li><strong>Another Example:</strong> What is <strong>4% of 75</strong>? Flip it to <strong>75% of 4</strong>! Three-quarters of 4 is simply <strong>3</strong>!</li>
      </ul>

      <!-- CONCEPT 2.5 -->
      <h3 class="subheading"><i class="fa-solid fa-arrow-trend-up"></i> 2.5 Multipliers &amp; Percentages Greater Than 100%</h3>
      <p>
        Can a percentage ever exceed 100%? <strong>Yes, absolutely!</strong>
      </p>
      <p>
        When you compare a part of a single pizza to the whole pizza, the fraction cannot exceed 1 (you cannot eat 5 slices out of 4). But when you compare <strong>growth, production targets, or harvests over time</strong>, quantities can multiply many times over!
      </p>
      <ul>
        <li><strong>100% of target:</strong> Multiplier is <code>1.0</code> (Target achieved exactly).</li>
        <li><strong>120% of target:</strong> Multiplier is <code>1.2</code> (Exceeded target by 20%).</li>
        <li><strong>150% of target:</strong> Multiplier is <code>1.5</code> (Target achieved plus half as much again).</li>
        <li><strong>200% of target:</strong> Multiplier is <code>2.0</code> (Achieved exactly twice or double the target).</li>
        <li><strong>250% of harvest:</strong> Multiplier is <code>2.5</code> (A farmer harvesting 260 kg last year who harvests 650 kg this year has achieved <code>(650 / 260) × 100 = 250%</code> of last year's yield).</li>
      </ul>

      <!-- CONCEPT 2.6 -->
      <h3 class="subheading"><i class="fa-solid fa-chart-line"></i> 2.6 Percentage Change (Increase and Decrease) &amp; KYC</h3>
      <p>
        In economics, science, and everyday life, we constantly measure how things change. Did petrol prices go up? Did theater footfalls go down after COVID?
      </p>
      <div class="callout callout-def">
        <div class="callout-title"><i class="fa-solid fa-percent"></i> The Fundamental Law of Percentage Change</div>
        <p>
          Percentage change always measures the <strong>absolute change</strong> relative to the <strong>original starting value</strong>:
        </p>
        <p style="font-family: 'JetBrains Mono', monospace; font-size: 1.05rem; font-weight: 700; color: #1e3a8a; margin: 0.5rem 0;">
          Percentage Increase = (Increase in Value / Original Starting Value) × 100%<br>
          Percentage Decrease = (Decrease in Value / Original Starting Value) × 100%
        </p>
      </div>

      <div class="callout callout-warn">
        <div class="callout-title"><i class="fa-solid fa-triangle-exclamation"></i> Critical Base Alert: Always Divide by the ORIGINAL Value!</div>
        <p>
          Students frequently make the fatal mistake of dividing by the <em>new final value</em> instead of the original value!
        </p>
        <ul>
          <li><strong>Example 1:</strong> Tomato price rises from ₹30 to ₹42. The change is ₹12. The percentage increase is <code>(12 / 30) × 100 = 40%</code> (NOT 12/42!).</li>
          <li><strong>Example 2:</strong> Theater footfall drops from 160 to 100. The drop is 60 people. The percentage decrease is <code>(60 / 160) × 100 = 37.5%</code> (NOT 60/100!).</li>
        </ul>
      </div>

      <!-- CONCEPT 2.7 -->
      <h3 class="subheading"><i class="fa-solid fa-shop"></i> 2.7 Commercial Arithmetic: Cost Price, Profit, Loss, Discount &amp; GST</h3>
      <p>
        Commerce is the heartbeat of society. Let us understand the journey of a product from the factory to your hands:
      </p>

      <div style="background: #ffffff; border: 1px solid var(--border); border-radius: var(--radius-md); padding: 1.25rem; margin-bottom: 1.25rem;">
        <h4 style="color: #1e1b4b; margin-bottom: 0.5rem;"><i class="fa-solid fa-tag"></i> Key Commercial Vocabulary &amp; Equations</h4>
        <ul style="padding-left: 1.25rem; line-height: 1.8;">
          <li><strong>Cost Price (CP):</strong> The total expenditure incurred to acquire or manufacture the article.</li>
          <li><strong>Overhead Expenses (OH):</strong> Additional costs incurred after purchasing, such as freight transportation, labor charges, repairs, or packaging. <strong>Effective CP = Purchase Price + Overheads.</strong></li>
          <li><strong>Selling Price (SP):</strong> The price at which the article is finally sold to the customer.</li>
          <li><strong>Profit (Gain):</strong> Occurs when <code>SP &gt; CP</code>. Profit = <code>SP - CP</code>.</li>
          <li><strong>Loss:</strong> Occurs when <code>SP &lt; CP</code>. Loss = <code>CP - SP</code>.</li>
          <li><strong>Profit % or Loss %:</strong> ALWAYS calculated with respect to <strong>Cost Price (CP)</strong>:
            <div style="font-family: 'JetBrains Mono', monospace; font-weight: 700; color: #4338ca; margin: 0.25rem 0;">
              Profit% = (Profit / CP) × 100% &nbsp;&nbsp;|&nbsp;&nbsp; Loss% = (Loss / CP) × 100%
            </div>
          </li>
          <li><strong>Marked Price (MP) / List Price:</strong> The printed price tag on an article before any discount is applied.</li>
          <li><strong>Discount:</strong> The price reduction offered on the Marked Price: <code>Discount = MP - SP</code>.</li>
          <li><strong>Discount %:</strong> ALWAYS calculated with respect to <strong>Marked Price (MP)</strong>:
            <div style="font-family: 'JetBrains Mono', monospace; font-weight: 700; color: #0d9488; margin: 0.25rem 0;">
              Discount% = (Discount / MP) × 100% &nbsp;&nbsp;⇒&nbsp;&nbsp; SP = MP × (1 - d/100)
            </div>
          </li>
          <li><strong>Goods and Services Tax (GST):</strong> An indirect government tax charged on the actual selling price of goods and services:
            <div style="font-family: 'JetBrains Mono', monospace; font-weight: 700; color: #b45309; margin: 0.25rem 0;">
              GST Amount = (GST% / 100) × SP &nbsp;&nbsp;⇒&nbsp;&nbsp; Final Bill = SP × (1 + GST%/100)
            </div>
          </li>
        </ul>
      </div>

      <!-- CONCEPT 2.8 -->
      <h3 class="subheading"><i class="fa-solid fa-piggy-bank"></i> 2.8 Capital Growth: The Mechanics of Simple vs Compound Interest</h3>
      <p>
        When you deposit money in a bank, the bank uses your money to issue loans to businesses and homeowners. In return for using your money, the bank pays you extra money called <strong>Interest</strong>.
      </p>
      <ul>
        <li><strong>Principal (P):</strong> The initial amount of money deposited or borrowed.</li>
        <li><strong>Rate of Interest (R):</strong> The percentage paid per year (per annum, abbreviated as <em>p.a.</em>).</li>
        <li><strong>Time Period (T or t):</strong> The duration for which the money remains invested.</li>
      </ul>

      <div class="callout callout-def">
        <div class="callout-title"><i class="fa-solid fa-coins"></i> Option 1: Simple Interest (Linear Non-Compounding Growth)</div>
        <p>
          In <strong>Simple Interest (SI)</strong>, the interest earned each year is paid out or kept separate. The principal amount remains fixed at <em>P</em> for the entire duration!
        </p>
        <p style="font-family: 'JetBrains Mono', monospace; font-size: 1.05rem; font-weight: 700; color: #1e3a8a;">
          SI = (P × R × T) / 100 &nbsp;&nbsp;|&nbsp;&nbsp; Total Amount A = P + SI = P × (1 + (R × T) / 100)
        </p>
        <p>
          <em>Example:</em> If you deposit ₹6,000 at 10% p.a. for 3 years:
          Each year you earn 10% of ₹6,000 = ₹600.
          Over 3 years, total SI = ₹600 × 3 = ₹1,800. Total amount received = ₹6,000 + ₹1,800 = <strong>₹7,800</strong>.
        </p>
      </div>

      <div class="callout callout-def">
        <div class="callout-title"><i class="fa-solid fa-seedling"></i> Option 2: Compound Interest (The "Interest on Interest" Engine)</div>
        <p>
          In <strong>Compound Interest (CI)</strong>, the interest earned at the end of each year is NOT paid out—it is <strong>added back to the principal</strong>!
          Therefore, in the next year, you earn interest on both your original principal AND on the previous interest.
        </p>
        <p style="font-family: 'JetBrains Mono', monospace; font-size: 1.05rem; font-weight: 700; color: #064e3b;">
          Annual Multiplier m = (1 + R / 100)<br>
          Amount after t years: A = P × (1 + R / 100)ᵗ &nbsp;&nbsp;|&nbsp;&nbsp; CI = A - P
        </p>
        <p>
          <em>Watch the magic on ₹6,000 at 10% p.a.:</em>
        </p>
        <ul>
          <li><strong>Year 1:</strong> Interest = 10% of ₹6,000 = ₹600. New Principal = ₹6,000 + ₹600 = <strong>₹6,600</strong> (= ₹6,000 × 1.10).</li>
          <li><strong>Year 2:</strong> Interest = 10% of ₹6,600 = ₹660! (Notice the extra ₹60!). New Principal = ₹6,600 + ₹660 = <strong>₹7,260</strong> (= ₹6,000 × 1.10²).</li>
          <li><strong>Year 3:</strong> Interest = 10% of ₹7,260 = ₹726! (Notice the extra ₹126!). Final Amount = ₹7,260 + ₹726 = <strong>₹7,986</strong> (= ₹6,000 × 1.10³).</li>
        </ul>
        <p>
          Total Compound Interest = ₹7,986 - ₹6,000 = <strong>₹1,986</strong>.
          Compared to Simple Interest (₹1,800), compounding yielded an <strong>extra ₹186 for free</strong> because of interest earning interest!
        </p>
      </div>

      <!-- CONCEPT 2.9 -->
      <h3 class="subheading"><i class="fa-solid fa-arrow-trend-down"></i> 2.9 Depreciation &amp; Exponential Decay</h3>
      <p>
        Just as investments can grow by compounding, physical assets like vehicles, smartphones, machines, and televisions lose value over time due to wear, tear, and technological obsolescence. This reduction in value is called <strong>Depreciation</strong>.
      </p>
      <div class="callout callout-def">
        <div class="callout-title"><i class="fa-solid fa-car-crash"></i> The Depreciation Formula</div>
        <p>
          If an article with initial purchase value <em>P</em> depreciates at an annual rate of <em>R%</em> per year, its depreciated book value <em>A</em> after <em>n</em> years is given by:
        </p>
        <p style="font-family: 'JetBrains Mono', monospace; font-size: 1.05rem; font-weight: 700; color: #7f1d1d;">
          A = P × (1 - R / 100)ⁿ
        </p>
        <p>
          <em>Example:</em> A TV bought for ₹21,000 depreciates by 5% in its first year.
          Its value after 1 year is <code>₹21,000 × (1 - 0.05) = ₹21,000 × 0.95 = ₹19,950</code>.
        </p>
      </div>

      <!-- CONCEPT 2.10 -->
      <h3 class="subheading"><i class="fa-solid fa-triangle-exclamation"></i> 2.10 Deceptive Percentages &amp; The Non-Additivity Fallacy</h3>
      <p>
        Percentages can play mind tricks on unsuspecting shoppers and business owners. The NCERT textbook highlights two monumental psychological traps:
      </p>

      <div class="callout callout-warn">
        <div class="callout-title"><i class="fa-solid fa-cake-candles"></i> Trap 1: The Successive Discount Illusion (Bakery Cakely vs Cakify)</div>
        <p>
          Bakery <em>Cakely</em> advertises: <strong>“30% + 20% Discount on All Cakes!”</strong><br>
          Bakery <em>Cakify</em> advertises: <strong>“Flat 50% Discount on All Cakes!”</strong>
        </p>
        <p>
          Many students naively assume 30% + 20% = 50%, so both shops must charge the same! <strong>This is completely false!</strong>
        </p>
        <ul>
          <li>Suppose a cake is marked at ₹200.</li>
          <li>At <strong>Cakify (Flat 50%)</strong>: Discount = 50% of ₹200 = ₹100. Price you pay = <strong>₹100</strong>.</li>
          <li>At <strong>Cakely (30% + 20%)</strong>: First discount = 30% of ₹200 = ₹60, bringing price to ₹140. Now the second 20% discount applies <em>only on the remaining ₹140</em>: 20% of ₹140 = ₹28! Final price you pay = ₹140 - ₹28 = <strong>₹112</strong>!</li>
        </ul>
        <p>
          <strong>Cakify is cheaper!</strong> A successive discount of 30% and 20% is equivalent to a single net discount of <code>1 - (0.70 × 0.80) = 1 - 0.56 = 44%</code>, NOT 50%!
        </p>
      </div>

      <div class="callout callout-warn">
        <div class="callout-title"><i class="fa-solid fa-fire-burner"></i> Trap 2: Surbhi's Mishap (The Markup &amp; Discount Asymmetry)</div>
        <p>
          Surbhi bought cookware from a wholesaler for cost price <em>x</em>. She marked it up with a <strong>50% profit margin</strong>, setting the price to <em>1.5x</em>. Later, to clear unsold stock without loss, she offered a <strong>50% discount</strong>, believing she would break even.
        </p>
        <p>
          <strong>What actually happened?</strong><br>
          A 50% discount on <em>1.5x</em> is <code>0.50 × 1.5x = 0.75x</code>!<br>
          She sold goods that cost her <em>x</em> for only <em>0.75x</em>, suffering a <strong>massive 25% net loss</strong>!
        </p>
        <p>
          <strong>The Mathematical Truth:</strong> To reverse a 50% markup and return to original cost price <em>x</em>, the required discount is:
          <code>(1.5x - x) / 1.5x = 0.5x / 1.5x = 1/3 = 33.33%</code>!
        </p>
      </div>

      <!-- EXHAUSTIVE BILINGUAL VOCABULARY TABLE -->
      <h3 class="subheading"><i class="fa-solid fa-language"></i> Exhaustive Bilingual Vocabulary &amp; Glossary Table</h3>
      <p>
        Master these 30 foundational mathematical and commercial terms in both English and standard textbook Odia (ଓଡ଼ିଆ):
      </p>

      <div class="table-container">
        <table class="data-table">
          <thead>
            <tr>
              <th style="width: 22%;">Term / Concept</th>
              <th style="width: 14%;">Part of Speech</th>
              <th style="width: 38%;">English Meaning</th>
              <th style="width: 26%;">ଓଡ଼ିଆ ଅର୍ଥ (Odia Meaning)</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>Percentage</strong></td>
              <td><span class="pos-badge">Noun</span></td>
              <td>A fraction whose denominator is fixed at 100; parts per hundred</td>
              <td><span class="odia-text">ଶତକଡ଼ା / ପ୍ରତିଶତ</span></td>
            </tr>
            <tr>
              <td><strong>Per Centum</strong></td>
              <td><span class="pos-badge">Phrase</span></td>
              <td>Latin root phrase meaning "by the hundred" or "out of one hundred"</td>
              <td><span class="odia-text">ପ୍ରତି ଶହେରେ</span></td>
            </tr>
            <tr>
              <td><strong>Fraction</strong></td>
              <td><span class="pos-badge">Noun</span></td>
              <td>A numerical quantity that is not a whole number; a part-to-whole ratio</td>
              <td><span class="odia-text">ଭଗ୍ନାଂଶ</span></td>
            </tr>
            <tr>
              <td><strong>Numerator</strong></td>
              <td><span class="pos-badge">Noun</span></td>
              <td>The top number of a fraction showing how many parts are taken</td>
              <td><span class="odia-text">ଲବ</span></td>
            </tr>
            <tr>
              <td><strong>Denominator</strong></td>
              <td><span class="pos-badge">Noun</span></td>
              <td>The bottom number of a fraction representing the total parts in a whole</td>
              <td><span class="odia-text">ହର</span></td>
            </tr>
            <tr>
              <td><strong>Decimal</strong></td>
              <td><span class="pos-badge">Noun / Adj</span></td>
              <td>A fraction expressed in the base-10 positional notation system</td>
              <td><span class="odia-text">ଦଶମିକ</span></td>
            </tr>
            <tr>
              <td><strong>Equivalent Fraction</strong></td>
              <td><span class="pos-badge">Noun</span></td>
              <td>Fractions that have the same value even though they look different</td>
              <td><span class="odia-text">ସମତୁଲ୍ୟ ଭଗ୍ନାଂଶ</span></td>
            </tr>
            <tr>
              <td><strong>Unitary Method</strong></td>
              <td><span class="pos-badge">Noun</span></td>
              <td>Problem-solving technique finding the value of 1 unit first</td>
              <td><span class="odia-text">ଐକିକ ନିୟମ</span></td>
            </tr>
            <tr>
              <td><strong>Multiplier</strong></td>
              <td><span class="pos-badge">Noun</span></td>
              <td>A factor by which a quantity is multiplied to scale its value</td>
              <td><span class="odia-text">ଗୁଣକ</span></td>
            </tr>
            <tr>
              <td><strong>Commutative Law</strong></td>
              <td><span class="pos-badge">Noun</span></td>
              <td>The algebraic property where order of operands does not change result</td>
              <td><span class="odia-text">କ୍ରମବିନିମୟ ନିୟମ</span></td>
            </tr>
            <tr>
              <td><strong>Ratio</strong></td>
              <td><span class="pos-badge">Noun</span></td>
              <td>A quantitative comparison showing relative sizes of two or more values</td>
              <td><span class="odia-text">ଅନୁପାତ</span></td>
            </tr>
            <tr>
              <td><strong>Proportion</strong></td>
              <td><span class="pos-badge">Noun</span></td>
              <td>An equation stating that two given ratios are strictly equal</td>
              <td><span class="odia-text">ସମାନୁପାତ</span></td>
            </tr>
            <tr>
              <td><strong>Percentage Increase</strong></td>
              <td><span class="pos-badge">Noun</span></td>
              <td>The relative growth of a quantity divided by its original value × 100</td>
              <td><span class="odia-text">ଶତକଡ଼ା ବୃଦ୍ଧି</span></td>
            </tr>
            <tr>
              <td><strong>Percentage Decrease</strong></td>
              <td><span class="pos-badge">Noun</span></td>
              <td>The relative reduction of a quantity divided by its original value × 100</td>
              <td><span class="odia-text">ଶତକଡ଼ା ହ୍ରାସ</span></td>
            </tr>
            <tr>
              <td><strong>Cost Price (CP)</strong></td>
              <td><span class="pos-badge">Noun</span></td>
              <td>The actual price paid to purchase or manufacture an article</td>
              <td><span class="odia-text">କ୍ରୟ ମୂଲ୍ୟ</span></td>
            </tr>
            <tr>
              <td><strong>Selling Price (SP)</strong></td>
              <td><span class="pos-badge">Noun</span></td>
              <td>The price at which an article is sold to a buyer</td>
              <td><span class="odia-text">ବିକ୍ରୟ ମୂଲ୍ୟ</span></td>
            </tr>
            <tr>
              <td><strong>Profit (Gain)</strong></td>
              <td><span class="pos-badge">Noun</span></td>
              <td>The financial surplus earned when Selling Price exceeds Cost Price</td>
              <td><span class="odia-text">ଲାଭ</span></td>
            </tr>
            <tr>
              <td><strong>Loss</strong></td>
              <td><span class="pos-badge">Noun</span></td>
              <td>The financial deficit incurred when Cost Price exceeds Selling Price</td>
              <td><span class="odia-text">କ୍ଷତି</span></td>
            </tr>
            <tr>
              <td><strong>Overhead Expenses</strong></td>
              <td><span class="pos-badge">Noun</span></td>
              <td>Incidental costs like freight, repairs, and labor added to purchase price</td>
              <td><span class="odia-text">ଉପରିସ୍ଥ ଖର୍ଚ୍ଚ</span></td>
            </tr>
            <tr>
              <td><strong>Marked Price (MP)</strong></td>
              <td><span class="pos-badge">Noun</span></td>
              <td>The listed or tagged catalog price of an article before discount</td>
              <td><span class="odia-text">ଲିଖିତ ମୂଲ୍ୟ / ଧାର୍ଯ୍ୟ ମୂଲ୍ୟ</span></td>
            </tr>
            <tr>
              <td><strong>Discount</strong></td>
              <td><span class="pos-badge">Noun</span></td>
              <td>A reduction granted by a merchant from the marked catalog price</td>
              <td><span class="odia-text">ରିହାତି / ଛାଡ଼</span></td>
            </tr>
            <tr>
              <td><strong>Successive Discount</strong></td>
              <td><span class="pos-badge">Noun</span></td>
              <td>Consecutive discounts where each applies to the previously reduced price</td>
              <td><span class="odia-text">କ୍ରମିକ ରିହାତି</span></td>
            </tr>
            <tr>
              <td><strong>GST</strong></td>
              <td><span class="pos-badge">Noun</span></td>
              <td>Goods and Services Tax; indirect value tax levied by the government</td>
              <td><span class="odia-text">ଦ୍ରବ୍ୟ ଓ ସେବା କର (ଜିଏସଟି)</span></td>
            </tr>
            <tr>
              <td><strong>Principal</strong></td>
              <td><span class="pos-badge">Noun</span></td>
              <td>The capital sum of money initially deposited, invested, or borrowed</td>
              <td><span class="odia-text">ମୂଳଧନ</span></td>
            </tr>
            <tr>
              <td><strong>Interest</strong></td>
              <td><span class="pos-badge">Noun</span></td>
              <td>The rental compensation fee paid for borrowing or using capital over time</td>
              <td><span class="odia-text">ସୁଧ</span></td>
            </tr>
            <tr>
              <td><strong>Simple Interest (SI)</strong></td>
              <td><span class="pos-badge">Noun</span></td>
              <td>Interest calculated solely on the unchanged original principal sum</td>
              <td><span class="odia-text">ସରଳ ସୁଧ</span></td>
            </tr>
            <tr>
              <td><strong>Compound Interest (CI)</strong></td>
              <td><span class="pos-badge">Noun</span></td>
              <td>Interest calculated on both initial principal and accumulated past interest</td>
              <td><span class="odia-text">ଚକ୍ରବୃଦ୍ଧି ସୁଧ</span></td>
            </tr>
            <tr>
              <td><strong>Amount (Maturity Value)</strong></td>
              <td><span class="pos-badge">Noun</span></td>
              <td>The total sum of Principal plus accumulated Interest: A = P + I</td>
              <td><span class="odia-text">ସୁଧମୂଳ / ମିଶ୍ରଧନ</span></td>
            </tr>
            <tr>
              <td><strong>Depreciation</strong></td>
              <td><span class="pos-badge">Noun</span></td>
              <td>The steady decrease in monetary value of physical assets over time</td>
              <td><span class="odia-text">ଅବକ୍ଷୟ / ମୂଲ୍ୟହ୍ରାସ</span></td>
            </tr>
            <tr>
              <td><strong>Per Annum (p.a.)</strong></td>
              <td><span class="pos-badge">Adverb</span></td>
              <td>Latin phrase meaning "yearly" or "for each year"</td>
              <td><span class="odia-text">ବାର୍ଷିକ</span></td>
            </tr>
          </tbody>
        </table>
      </div>
    </section>
"""
