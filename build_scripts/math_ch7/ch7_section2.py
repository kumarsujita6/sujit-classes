# -*- coding: utf-8 -*-
"""
Module: ch7_section2.py
Contains Section 2: Complete Line-by-Line Conceptual Explanations,
SVG Diagrams 2, 3, 4, 5, 6, and Exhaustive Bilingual Vocabulary Table (English + Odia).
"""

def get_section2():
    return """
    <!-- ========================================== -->
    <!-- SECTION 2: CONCEPTUAL DEEP DIVE & GLOSSARY -->
    <!-- ========================================== -->
    <section id="section2">
      <div class="section-header">
        <div class="section-tag"><i class="fa-solid fa-book-open"></i> Core Pedagogical Depth</div>
        <h2 class="section-title">Section 2: Complete Line-by-Line Conceptual Explanations</h2>
        <p class="section-desc">
          Master the mathematical mechanics of proportional thinking, from geometric aspect ratios and ancient Indian Trairāśika to partnership sharing, unit harmonization, and logic grids.
        </p>
      </div>

      <!-- 2.1 OBSERVING SIMILARITY IN CHANGE -->
      <h3 class="subheading"><i class="fa-solid fa-image"></i> 2.1 Observing Similarity in Change &amp; Aspect Ratios</h3>
      <p>
        In our digital world, we encounter images, videos, and graphics on phones, tablets, laptops, and large screens. Whenever an image is resized, it either maintains its natural look or becomes distorted.
      </p>
      <p>
        Consider the five digital images analyzed in the NCERT textbook (Image A, B, C, D, and E):
      </p>
      <ul>
        <li><strong>Image A (Original):</strong> Width = 60 mm, Height = 40 mm. The tiger looks natural and lifelike.</li>
        <li><strong>Image B (Distorted):</strong> Width = 40 mm, Height = 20 mm. The tiger appears stretched horizontally and unusually thin!</li>
        <li><strong>Image C (Reduced):</strong> Width = 30 mm, Height = 20 mm. Despite being smaller, the tiger looks completely normal.</li>
        <li><strong>Image D (Enlarged):</strong> Width = 90 mm, Height = 60 mm. Despite being larger, the tiger preserves its exact proportions.</li>
        <li><strong>Image E (Distorted):</strong> Width = 40 mm, Height = 40 mm. The image is a square, making the tiger look compressed and unnaturally fat!</li>
      </ul>

      <div class="callout callout-def">
        <div class="callout-title"><i class="fa-solid fa-lightbulb"></i> What is an Aspect Ratio?</div>
        <p>
          The <strong>aspect ratio</strong> of a two-dimensional shape is the numerical relationship between its width (horizontal measurement) and height (vertical measurement), expressed as:
        </p>
        <p style="text-align: center; font-size: 1.15rem; font-weight: 700; color: #312e81;">
          Aspect Ratio = Width : Height = Width ÷ Height
        </p>
        <p>
          Two rectangular shapes are <strong>similar</strong> if and only if their aspect ratios are mathematically equivalent. When you scale an image by multiplying both the width and height by the <em>same positive factor</em>, the aspect ratio remains unchanged, and no distortion occurs.
        </p>
      </div>

      <p>
        Let us compute the aspect ratios of the five images:
      </p>
      <div class="table-container">
        <table class="data-table">
          <thead>
            <tr>
              <th>Image Name</th>
              <th>Width (mm)</th>
              <th>Height (mm)</th>
              <th>Ratio (Width : Height)</th>
              <th>Simplest Form (Divided by HCF)</th>
              <th>Visual Appearance</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>Image A</strong></td>
              <td>60</td>
              <td>40</td>
              <td>60 : 40</td>
              <td><strong>3 : 2</strong> (Divided by 20)</td>
              <td><span style="color: #15803d; font-weight: 700;">✓ Natural (Baseline)</span></td>
            </tr>
            <tr>
              <td><strong>Image B</strong></td>
              <td>40</td>
              <td>20</td>
              <td>40 : 20</td>
              <td><strong>2 : 1</strong> (Divided by 20)</td>
              <td><span style="color: #b91c1c; font-weight: 700;">✗ Elongated / Stretched</span></td>
            </tr>
            <tr>
              <td><strong>Image C</strong></td>
              <td>30</td>
              <td>20</td>
              <td>30 : 20</td>
              <td><strong>3 : 2</strong> (Divided by 10)</td>
              <td><span style="color: #15803d; font-weight: 700;">✓ Natural (Scaled by 1/2)</span></td>
            </tr>
            <tr>
              <td><strong>Image D</strong></td>
              <td>90</td>
              <td>60</td>
              <td>90 : 60</td>
              <td><strong>3 : 2</strong> (Divided by 30)</td>
              <td><span style="color: #15803d; font-weight: 700;">✓ Natural (Scaled by 3/2)</span></td>
            </tr>
            <tr>
              <td><strong>Image E</strong></td>
              <td>40</td>
              <td>40</td>
              <td>40 : 40</td>
              <td><strong>1 : 1</strong> (Divided by 40)</td>
              <td><span style="color: #b91c1c; font-weight: 700;">✗ Squished / Compressed</span></td>
            </tr>
          </tbody>
        </table>
      </div>

      <!-- 2.2 THE MATHEMATICAL NOTION OF RATIO -->
      <h3 class="subheading"><i class="fa-solid fa-divide"></i> 2.2 What is a Ratio? Conceptual Mechanics</h3>
      <p>
        In mathematics, we compare two quantities using two fundamental methods:
      </p>
      <ol>
        <li>
          <strong>Comparison by Subtraction (Difference):</strong> Tells us <em>how much more</em> or <em>how much less</em> one quantity is compared to another. For example, if Ananya has 10 pencils and Rohit has 6 pencils, Ananya has <em>10 - 6 = 4 more pencils</em>.
        </li>
        <li>
          <strong>Comparison by Division (Ratio):</strong> Tells us <em>how many times</em> one quantity contains or is contained in another. Using the same example, the ratio of Ananya's pencils to Rohit's pencils is <em>10 ÷ 6 = 5/3</em> or <em>5 : 3</em>.
        </li>
      </ol>

      <div class="callout callout-def">
        <div class="callout-title"><i class="fa-solid fa-bookmark"></i> Formal Definition of a Ratio</div>
        <p>
          A <strong>ratio</strong> is a mathematical comparison of two quantities of the <strong>same kind</strong> and expressed in the <strong>same units</strong>, obtained by dividing the first quantity by the second.
        </p>
        <p>
          The ratio of a quantity <em>a</em> to a quantity <em>b</em> is written as <strong>a : b</strong> (read as "<em>a is to b</em>") or as a fraction <strong>a/b</strong>, where <em>b ≠ 0</em>.
        </p>
        <p>
          In the ratio <em>a : b</em>:
        </p>
        <ul style="margin-bottom: 0;">
          <li><strong>a</strong> is called the <strong>First Term</strong> or <strong>Antecedent</strong> (ପୂର୍ବପଦ).</li>
          <li><strong>b</strong> is called the <strong>Second Term</strong> or <strong>Consequent</strong> (ଉତ୍ତରପଦ).</li>
        </ul>
      </div>

      <div class="callout callout-warn">
        <div class="callout-title"><i class="fa-solid fa-triangle-exclamation"></i> Three Non-Negotiable Rules of Ratios</div>
        <ul>
          <li><strong>Same Kind &amp; Unit:</strong> We cannot form a ratio between 5 apples and 3 rupees, nor between 2 metres and 500 grams. To compare 2 metres and 50 centimetres, we must first convert metres to centimetres (200 cm : 50 cm = 4 : 1).</li>
          <li><strong>Order Matters:</strong> The ratio <em>a : b</em> is completely different from <em>b : a</em> unless <em>a = b</em>. For example, 3 : 2 (1.5) is not the same as 2 : 3 (0.67).</li>
          <li><strong>No Units:</strong> Because a ratio is a fraction of two quantities with the same units, the units cancel out completely! A ratio is a <strong>pure, dimensionless number</strong>.</li>
        </ul>
      </div>

      <!-- 2.3 EQUIVALENT RATIOS & SIMPLEST FORM -->
      <h3 class="subheading"><i class="fa-solid fa-filter"></i> 2.3 Equivalent Ratios &amp; Simplest Form</h3>
      <p>
        Just like equivalent fractions, we obtain <strong>equivalent ratios</strong> by multiplying or dividing both terms of the ratio by the same non-zero number:
      </p>
      <div style="background: #eef2ff; border: 1px solid #c7d2fe; border-radius: var(--radius-md); padding: 1.25rem; text-align: center; margin: 1.5rem 0;">
        <span style="font-family: 'JetBrains Mono', monospace; font-size: 1.1rem; color: #3730a3; font-weight: 700;">
          a : b = (a × k) : (b × k) &nbsp;&nbsp;and&nbsp;&nbsp; a : b = (a ÷ k) : (b ÷ k) &nbsp;&nbsp;(for any k ≠ 0)
        </span>
      </div>

      <p>
        <strong>Simplest Form (Lowest Terms):</strong> A ratio <em>a : b</em> is in its simplest form if the integers <em>a</em> and <em>b</em> are co-prime, meaning their Highest Common Factor (HCF / ଗ.ସା.ଗୁ.) is 1.
      </p>

      <div class="callout callout-hack">
        <div class="callout-title"><i class="fa-solid fa-wand-magic-sparkles"></i> Teacher Memory Trick: The HCF Reduction Shortcut</div>
        <p>
          To reduce any large ratio <em>a : b</em> to simplest form in one single step, compute <strong>HCF(a, b)</strong> and divide both terms by it!
        </p>
        <p>
          <em>Example:</em> Reduce 72 : 96.
          <br>HCF(72, 96) = 24.
          <br>Dividing both by 24: (72 ÷ 24) : (96 ÷ 24) = <strong>3 : 4</strong>.
        </p>
      </div>

      <!-- 2.4 THE CRITICAL AGE COUNTEREXAMPLE -->
      <h4 class="subheading-sm"><i class="fa-solid fa-clock-rotate-left"></i> The Critical Age Problem: Why Adding Breaks Proportion</h4>
      <p>
        One of the most dangerous blunders students make is assuming that adding or subtracting the same number from both terms preserves the ratio. <strong>It does not!</strong>
      </p>
      <p>
        Let us examine <strong>Example 6 from the NCERT textbook</strong>:
      </p>
      <div style="background: #fffbeb; border-left: 5px solid #d97706; padding: 1.25rem; border-radius: var(--radius-sm); margin: 1rem 0;">
        <p>
          <strong>Scenario:</strong> When Neelima was 3 years old, her mother's age was 10 times her age (30 years).
        </p>
        <p>
          • Initial Ratio (Neelima : Mother) = 3 : 30 = <strong>1 : 10</strong>.
        </p>
        <p>
          Now, fast-forward 9 years later, when Neelima is 12 years old. Her mother is now <em>30 + 9 = 39 years old</em>.
        </p>
        <p>
          • New Ratio = 12 : 39 = <strong>4 : 13</strong>.
        </p>
        <p style="color: #b45309; font-weight: 700; margin-bottom: 0;">
          Notice that 1 : 10 ≠ 4 : 13! Even though exactly 9 years were added to both ages, the ratio changed dramatically. Proportionality is preserved ONLY by multiplication or division by a factor, NEVER by addition or subtraction.
        </p>
      </div>

      <!-- 2.5 THE LAW OF PROPORTION -->
      <h3 class="subheading"><i class="fa-solid fa-scale-balanced"></i> 2.4 Proportion &amp; Cross-Multiplication Law</h3>
      <p>
        When two ratios are equivalent in their simplest forms, we say they are <strong>in proportion</strong> or <strong>proportional</strong>.
      </p>
      <p>
        We write this using the double-colon symbol <strong>'::'</strong> (or the equals sign <strong>'='</strong>):
      </p>
      <div style="background: #f0fdf4; border: 1.5px solid #86efac; border-radius: var(--radius-md); padding: 1.25rem; text-align: center; margin: 1.5rem 0;">
        <span style="font-family: 'Space Grotesk', sans-serif; font-size: 1.3rem; color: #166534; font-weight: 800;">
          a : b :: c : d &nbsp;&nbsp;⟺&nbsp;&nbsp; a/b = c/d
        </span>
        <p style="font-size: 0.95rem; color: #15803d; margin-top: 0.5rem; margin-bottom: 0;">
          (Read as: "<em>a is to b as c is to d</em>")
        </p>
      </div>

      <p>
        In the proportion <em>a : b :: c : d</em>:
      </p>
      <ul>
        <li><strong>a</strong> and <strong>d</strong> are the outer terms, called the <strong>Extremes</strong> (ପ୍ରାନ୍ତ ପଦ).</li>
        <li><strong>b</strong> and <strong>c</strong> are the middle terms, called the <strong>Means</strong> (ମଧ୍ୟ ପଦ).</li>
      </ul>

      <div class="callout callout-def">
        <div class="callout-title"><i class="fa-solid fa-certificate"></i> The Fundamental Law of Proportion (Cross-Multiplication)</div>
        <p>
          For any four quantities to be in proportion, the product of the extremes MUST equal the product of the means:
        </p>
        <p style="text-align: center; font-size: 1.25rem; font-weight: 800; color: #1e1b4b; font-family: 'JetBrains Mono', monospace;">
          Product of Extremes = Product of Means &nbsp;⇒&nbsp; a × d = b × c
        </p>
        <p>
          <strong>Rigorous Proof:</strong>
          <br>1. If <em>a : b :: c : d</em>, then by definition <em>a / b = c / d</em>.
          <br>2. Multiply both sides of the equation by the common denominator <em>(b × d)</em>:
          <br>&nbsp;&nbsp;&nbsp;&nbsp;<em>(a / b) × (b × d) = (c / d) × (b × d)</em>
          <br>3. Cancelling <em>b</em> on the left and <em>d</em> on the right gives:
          <br>&nbsp;&nbsp;&nbsp;&nbsp;<strong>a × d = b × c</strong> (Proved).
        </p>
      </div>

      <!-- INTRICATE SVG 2: TRAIRASIKA ANCIENT BEAM BALANCE -->
      <div class="svg-container">
        <svg viewBox="0 0 950 480" xmlns="http://www.w3.org/2000/svg" style="background: #ffffff; border-radius: 16px;">
          <defs>
            <linearGradient id="beamGrad" x1="0%" y1="0%" x2="100%" y2="0%">
              <stop offset="0%" stop-color="#3730a3" />
              <stop offset="50%" stop-color="#4f46e5" />
              <stop offset="100%" stop-color="#059669" />
            </linearGradient>
            <filter id="shadowGlow" x="-10%" y="-10%" width="120%" height="120%">
              <feDropShadow dx="0" dy="6" stdDeviation="6" flood-color="#4f46e5" flood-opacity="0.15"/>
            </filter>
          </defs>

          <!-- Title Bar -->
          <rect x="25" y="15" width="900" height="45" rx="8" fill="#1e1b4b" />
          <text x="475" y="44" font-family="'Space Grotesk', sans-serif" font-size="16" font-weight="700" fill="#ffffff" text-anchor="middle">
            FIG 7.2: TRAIRĀŚIKA BALANCE &amp; CROSS-MULTIPLICATION EQUILIBRIUM (ĀRYABHAṬA I, 499 CE)
          </text>

          <!-- Central Fulcrum Pillar -->
          <polygon points="475,140 445,340 505,340" fill="#334155" />
          <rect x="420" y="340" width="110" height="20" rx="4" fill="#0f172a" />
          <circle cx="475" cy="140" r="14" fill="#f59e0b" stroke="#b45309" stroke-width="3" />

          <!-- Balance Beam -->
          <rect x="125" y="132" width="700" height="16" rx="8" fill="url(#beamGrad)" />

          <!-- Left Pan: Product of Extremes (a × d) -->
          <line x1="200" y1="140" x2="200" y2="230" stroke="#64748b" stroke-width="2.5" />
          <line x1="200" y1="230" x2="130" y2="280" stroke="#94a3b8" stroke-width="1.5" />
          <line x1="200" y1="230" x2="270" y2="280" stroke="#94a3b8" stroke-width="1.5" />
          <path d="M 120,280 Q 200,320 280,280 Z" fill="#e0e7ff" stroke="#4f46e5" stroke-width="2" filter="url(#shadowGlow)" />
          
          <rect x="145" y="235" width="110" height="42" rx="6" fill="#3730a3" />
          <text x="200" y="255" font-family="'Space Grotesk', sans-serif" font-size="12" font-weight="700" fill="#ffffff" text-anchor="middle">EXTREMES</text>
          <text x="200" y="271" font-family="'JetBrains Mono', monospace" font-size="14" font-weight="800" fill="#fde047" text-anchor="middle">a × d</text>

          <!-- Right Pan: Product of Means (b × c) -->
          <line x1="750" y1="140" x2="750" y2="230" stroke="#64748b" stroke-width="2.5" />
          <line x1="750" y1="230" x2="680" y2="280" stroke="#94a3b8" stroke-width="1.5" />
          <line x1="750" y1="230" x2="820" y2="280" stroke="#94a3b8" stroke-width="1.5" />
          <path d="M 670,280 Q 750,320 830,280 Z" fill="#d1fae5" stroke="#059669" stroke-width="2" filter="url(#shadowGlow)" />

          <rect x="695" y="235" width="110" height="42" rx="6" fill="#047857" />
          <text x="750" y="255" font-family="'Space Grotesk', sans-serif" font-size="12" font-weight="700" fill="#ffffff" text-anchor="middle">MEANS</text>
          <text x="750" y="271" font-family="'JetBrains Mono', monospace" font-size="14" font-weight="800" fill="#fde047" text-anchor="middle">b × c</text>

          <!-- Equal Sign in the Center -->
          <circle cx="475" cy="90" r="28" fill="#ffffff" stroke="#f59e0b" stroke-width="3" />
          <text x="475" y="99" font-family="'Space Grotesk', sans-serif" font-size="28" font-weight="800" fill="#d97706" text-anchor="middle">=</text>

          <!-- Explanatory Labels below -->
          <g transform="translate(50, 375)">
            <rect x="0" y="0" width="850" height="90" rx="10" fill="#f8fafc" stroke="#e2e8f0" stroke-width="1.5" />
            <text x="25" y="28" font-family="'Space Grotesk', sans-serif" font-size="13" font-weight="700" fill="#0f172a">
              THE ARITHMETIC LAW: a : b :: c : d  ⟺  (a)(d) = (b)(c)
            </text>
            <text x="25" y="52" font-family="'Plus Jakarta Sans', sans-serif" font-size="12" fill="#475569">
              • <strong>Pramāṇa (a):</strong> Known Standard Input &nbsp;&nbsp;|&nbsp;&nbsp; <strong>Phala (b):</strong> Known Standard Output
            </text>
            <text x="25" y="74" font-family="'Plus Jakarta Sans', sans-serif" font-size="12" fill="#475569">
              • <strong>Ichchhā (c):</strong> Desired Inquiry Input &nbsp;&nbsp;|&nbsp;&nbsp; <strong>Ichchhāphala (d):</strong> Desired Unknown Result = <em>(Phala × Ichchhā) ÷ Pramāṇa</em>
            </text>
          </g>
        </svg>
        <p class="svg-caption">
          Figure 7.2: The Trairāśika balance. Perfect balance is achieved when the cross product of the extremes (a × d) equals the cross product of the means (b × c).
        </p>
      </div>

      <!-- 2.6 ANCIENT INDIAN TRAIRĀŚIKA -->
      <h3 class="subheading"><i class="fa-solid fa-landmark"></i> 2.5 Ancient Indian Trairāśika: The Rule of Three</h3>
      <p>
        The principle of proportionality has deep roots in ancient Indian mathematics. Long before modern algebraic notation was developed in Europe, Indian mathematicians mastered proportional problem-solving under the name <strong>Trairāśika</strong> (ତ୍ରୈରାଶିକ, literally "<em>Rule of Three Quantities</em>").
      </p>
      <p>
        Master mathematicians such as <strong>Āryabhaṭa I</strong> (born 476 CE; composed the <em>Āryabhaṭīya</em> in 499 CE), <strong>Brahmagupta</strong> (628 CE; <em>Brāhmasphuṭasiddhānta</em>), and <strong>Bhāskarāchārya II</strong> (1150 CE; <em>Līlāvatī</em>) defined the algorithm systematically:
      </p>

      <div class="callout callout-def">
        <div class="callout-title"><i class="fa-solid fa-scroll"></i> Āryabhaṭa's Trairāśika Verse (Āryabhaṭīya, Gaṇitapāda 26)</div>
        <p style="font-style: italic; color: #1e1b4b; font-size: 1.05rem;">
          "त्रैराशिक-फल-राशिं तमथेच्छया संहते कृत्वा ।<br>
          लब्धं प्रमाण-भजितं तस्मादिच्छा-फलं भवति ॥"
        </p>
        <p>
          <em>Translation:</em> In the Rule of Three, multiply the <strong>Phala</strong> (fruit) by the <strong>Ichchhā</strong> (requisition), and divide the resulting product by the <strong>Pramāṇa</strong> (measure). The result obtained is the <strong>Ichchhāphala</strong> (yield).
        </p>
        <div style="background: #ffffff; border-radius: var(--radius-sm); padding: 1rem; margin-top: 0.75rem; border: 1px solid #cbd5e1;">
          <p style="font-family: 'JetBrains Mono', monospace; font-size: 1.15rem; font-weight: 700; color: #4f46e5; text-align: center; margin-bottom: 0;">
            Ichchhāphala = (Phala × Ichchhā) ÷ Pramāṇa
          </p>
        </div>
      </div>

      <p>
        Let us map the Sanskrit terms to modern variables:
      </p>
      <div class="table-container">
        <table class="data-table">
          <thead>
            <tr>
              <th>Sanskrit Term</th>
              <th>Literal English Meaning</th>
              <th>Mathematical Role</th>
              <th>Modern Variable</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>Pramāṇa (ପ୍ରମାଣ)</strong></td>
              <td>Measure / Benchmark</td>
              <td>The standard known quantity or input</td>
              <td><em>a</em></td>
            </tr>
            <tr>
              <td><strong>Phala (ଫଳ)</strong></td>
              <td>Fruit / Produce</td>
              <td>The known result or output produced by Pramāṇa</td>
              <td><em>b</em></td>
            </tr>
            <tr>
              <td><strong>Ichchhā (ଇଚ୍ଛା)</strong></td>
              <td>Desire / Requisition</td>
              <td>The new query quantity or requirement</td>
              <td><em>c</em></td>
            </tr>
            <tr>
              <td><strong>Ichchhāphala (ଇଚ୍ଛାଫଳ)</strong></td>
              <td>Desired Yield / Desired Fruit</td>
              <td>The unknown quantity to be found</td>
              <td><em>d = x</em></td>
            </tr>
          </tbody>
        </table>
      </div>

      <!-- 2.7 SHARING BUT NOT EQUALLY -->
      <h3 class="subheading"><i class="fa-solid fa-pie-chart"></i> 2.6 Sharing, but Not Equally! (Partitioning a Whole into m : n)</h3>
      <p>
        In daily life, resources, expenses, and profits are frequently shared in unequal proportions. For example:
      </p>
      <ul>
        <li>Two business partners divide monthly profits in proportion to their initial capital investments.</li>
        <li>A mason mixes cement, sand, and gravel in fixed ratios (e.g., 1 : 2 : 4) to prepare strong concrete.</li>
        <li>A chef mixes rice and urad dal in the ratio 2 : 1 to prepare soft idli batter.</li>
      </ul>

      <div class="callout callout-act">
        <div class="callout-title"><i class="fa-solid fa-dice"></i> Textbook Counter Activity (Section 7.5)</div>
        <p>
          Suppose you and your friend have <strong>12 counters</strong>:
        </p>
        <ul>
          <li><strong>Equal Share:</strong> Each gets 6 counters. The ratio is 6 : 6, which simplifies to <strong>1 : 1</strong>.</li>
          <li><strong>Partner gets 5:</strong> You get <em>12 - 5 = 7 counters</em>. The ratio is <strong>5 : 7</strong>.</li>
          <li>
            <strong>Share in Ratio 3 : 1:</strong>
            <br>• Round 1: Partner takes 3, you take 1 (4 taken, 8 left).
            <br>• Round 2: Partner takes 3, you take 1 (4 taken, 4 left).
            <br>• Round 3: Partner takes 3, you take 1 (4 taken, 0 left).
            <br>Partner gets <em>3 + 3 + 3 = 9</em> counters, you get <em>1 + 1 + 1 = 3</em> counters.
          </li>
        </ul>
      </div>

      <p>
        What if you have to share <strong>42 counters</strong> in the ratio <strong>4 : 3</strong>?
        Repeating physical rounds would take forever! Instead, we use the <strong>Unit Group Method</strong>:
      </p>

      <!-- INTRICATE SVG 3: TAPE DIAGRAM / BAR MODEL FOR SHARING -->
      <div class="svg-container">
        <svg viewBox="0 0 950 400" xmlns="http://www.w3.org/2000/svg" style="background: #ffffff; border-radius: 16px;">
          <defs>
            <linearGradient id="partnerBar" x1="0%" y1="0%" x2="100%" y2="0%">
              <stop offset="0%" stop-color="#4f46e5" />
              <stop offset="100%" stop-color="#6366f1" />
            </linearGradient>
            <linearGradient id="yourBar" x1="0%" y1="0%" x2="100%" y2="0%">
              <stop offset="0%" stop-color="#059669" />
              <stop offset="100%" stop-color="#10b981" />
            </linearGradient>
          </defs>

          <!-- Title Bar -->
          <rect x="25" y="15" width="900" height="42" rx="8" fill="#0f172a" />
          <text x="475" y="42" font-family="'Space Grotesk', sans-serif" font-size="15" font-weight="700" fill="#ffffff" text-anchor="middle">
            FIG 7.3: BAR MODEL (TAPE DIAGRAM) • PARTITIONING 42 IN THE RATIO 4 : 3
          </text>

          <!-- Total Bracket Top -->
          <path d="M 125,95 L 125,85 L 475,85 L 825,85 L 825,95" fill="none" stroke="#334155" stroke-width="2" />
          <text x="475" y="75" font-family="'Space Grotesk', sans-serif" font-size="16" font-weight="800" fill="#1e1b4b" text-anchor="middle">
            THE WHOLE = 42 COUNTERS (7 EQUAL UNITS)
          </text>

          <!-- 7 Equal Boxes: 4 for Partner (Indigo), 3 for You (Emerald) -->
          <!-- Box 1 -->
          <rect x="125" y="105" width="100" height="65" rx="6" fill="url(#partnerBar)" stroke="#3730a3" stroke-width="2" />
          <text x="175" y="143" font-family="'JetBrains Mono', monospace" font-size="20" font-weight="800" fill="#ffffff" text-anchor="middle">6</text>
          <!-- Box 2 -->
          <rect x="225" y="105" width="100" height="65" rx="6" fill="url(#partnerBar)" stroke="#3730a3" stroke-width="2" />
          <text x="275" y="143" font-family="'JetBrains Mono', monospace" font-size="20" font-weight="800" fill="#ffffff" text-anchor="middle">6</text>
          <!-- Box 3 -->
          <rect x="325" y="105" width="100" height="65" rx="6" fill="url(#partnerBar)" stroke="#3730a3" stroke-width="2" />
          <text x="375" y="143" font-family="'JetBrains Mono', monospace" font-size="20" font-weight="800" fill="#ffffff" text-anchor="middle">6</text>
          <!-- Box 4 -->
          <rect x="425" y="105" width="100" height="65" rx="6" fill="url(#partnerBar)" stroke="#3730a3" stroke-width="2" />
          <text x="475" y="143" font-family="'JetBrains Mono', monospace" font-size="20" font-weight="800" fill="#ffffff" text-anchor="middle">6</text>

          <!-- Box 5 -->
          <rect x="525" y="105" width="100" height="65" rx="6" fill="url(#yourBar)" stroke="#047857" stroke-width="2" />
          <text x="575" y="143" font-family="'JetBrains Mono', monospace" font-size="20" font-weight="800" fill="#ffffff" text-anchor="middle">6</text>
          <!-- Box 6 -->
          <rect x="625" y="105" width="100" height="65" rx="6" fill="url(#yourBar)" stroke="#047857" stroke-width="2" />
          <text x="675" y="143" font-family="'JetBrains Mono', monospace" font-size="20" font-weight="800" fill="#ffffff" text-anchor="middle">6</text>
          <!-- Box 7 -->
          <rect x="725" y="105" width="100" height="65" rx="6" fill="url(#yourBar)" stroke="#047857" stroke-width="2" />
          <text x="775" y="143" font-family="'JetBrains Mono', monospace" font-size="20" font-weight="800" fill="#ffffff" text-anchor="middle">6</text>

          <!-- Bottom Bracket for Partner -->
          <path d="M 125,185 L 125,195 L 325,195 L 525,195 L 525,185" fill="none" stroke="#4f46e5" stroke-width="2.5" />
          <text x="325" y="222" font-family="'Space Grotesk', sans-serif" font-size="15" font-weight="700" fill="#312e81" text-anchor="middle">
            Partner's Share = 4 Units × 6 = 24
          </text>

          <!-- Bottom Bracket for You -->
          <path d="M 525,185 L 525,195 L 675,195 L 825,195 L 825,185" fill="none" stroke="#059669" stroke-width="2.5" />
          <text x="675" y="222" font-family="'Space Grotesk', sans-serif" font-size="15" font-weight="700" fill="#065f46" text-anchor="middle">
            Your Share = 3 Units × 6 = 18
          </text>

          <!-- Step-by-Step Logic Explanation Banner -->
          <g transform="translate(60, 260)">
            <rect x="0" y="0" width="830" height="110" rx="8" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5" />
            <text x="20" y="28" font-family="'Space Grotesk', sans-serif" font-size="13" font-weight="700" fill="#0f172a">
              ALGEBRAIC PROOF OF THE GENERAL PARTITIONING THEOREM:
            </text>
            <text x="20" y="52" font-family="'Plus Jakarta Sans', sans-serif" font-size="12" fill="#334155">
              1. Total Number of Parts = <em>m + n</em> (In this case, 4 + 3 = 7 parts).
            </text>
            <text x="20" y="74" font-family="'Plus Jakarta Sans', sans-serif" font-size="12" fill="#334155">
              2. Value of 1 Unit Part = <em>Total Quantity ÷ (m + n)</em> ⇒ 42 ÷ 7 = <strong>6</strong>.
            </text>
            <text x="20" y="96" font-family="'Plus Jakarta Sans', sans-serif" font-size="12" fill="#334155">
              3. First Share = <em>m × [x / (m + n)]</em> = 4 × 6 = <strong>24</strong> &nbsp;|&nbsp; Second Share = <em>n × [x / (m + n)]</em> = 3 × 6 = <strong>18</strong>. Sum = 24 + 18 = 42 ✓.
            </text>
          </g>
        </svg>
        <p class="svg-caption">
          Figure 7.3: Tape diagram visualizer for ratio division. The whole is partitioned into (m + n) equal blocks, each representing the unit value x / (m + n).
        </p>
      </div>

      <div class="callout callout-def">
        <div class="callout-title"><i class="fa-solid fa-calculator"></i> General Partitioning Formula</div>
        <p>
          To divide any quantity <strong>x</strong> into two parts in the ratio <strong>m : n</strong>:
        </p>
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1rem; margin-top: 0.75rem;">
          <div style="background: white; padding: 1rem; border-radius: var(--radius-sm); border: 1px solid #c7d2fe; text-align: center;">
            <span style="font-size: 0.85rem; color: #64748b; font-weight: 600;">FIRST PART</span><br>
            <strong style="font-size: 1.25rem; color: #4f46e5; font-family: 'JetBrains Mono', monospace;">
              m × [ x / (m + n) ]
            </strong>
          </div>
          <div style="background: white; padding: 1rem; border-radius: var(--radius-sm); border: 1px solid #a7f3d0; text-align: center;">
            <span style="font-size: 0.85rem; color: #64748b; font-weight: 600;">SECOND PART</span><br>
            <strong style="font-size: 1.25rem; color: #059669; font-family: 'JetBrains Mono', monospace;">
              n × [ x / (m + n) ]
            </strong>
          </div>
        </div>
      </div>

      <!-- 2.8 BOUNDARIES OF PROPORTION -->
      <h3 class="subheading"><i class="fa-solid fa-triangle-exclamation"></i> 2.7 Boundaries of Proportional Reasoning: When Rule of Three Fails!</h3>
      <p>
        A key objective of the NEP 2020 Ganita Prakash curriculum is developing critical thinking. Not every real-world phenomenon is directly proportional. Students must recognize when proportional models apply and when they do not.
      </p>

      <h4 class="subheading-sm">Case 1: Inverse Variation (Speed vs Time)</h4>
      <p>
        Consider <strong>Puneeth's Father's Motorcycle Journey (NCERT Page 171)</strong>:
        <br>Puneeth's father rode from Lucknow to Kanpur at 50 km/h and took 2 hours.
        <br>If he increases his speed to 75 km/h, will he take <em>more time</em> or <em>less time</em>?
      </p>
      <ul>
        <li>If a student blindly writes: <em>50 : 2 :: 75 : x ⇒ x = (2 × 75) / 50 = 3 hours</em>, they have committed a <strong>fatal logic error</strong>!</li>
        <li>Riding faster must decrease the travel time, not increase it!</li>
        <li>Here, <strong>Distance = Speed × Time = Constant</strong> (50 × 2 = 100 km).</li>
        <li>At 75 km/h, the time is <em>100 ÷ 75 = 4/3 hours = 1 hour 20 minutes (80 minutes)</em>.</li>
        <li>This is <strong>Inverse Proportion</strong> (ବ୍ୟସ୍ତ ସମାନୁପାତ), not Direct Proportion.</li>
      </ul>

      <h4 class="subheading-sm">Case 2: Real-World Commercial Packaging (The Shampoo Mystery)</h4>
      <p>
        In <strong>Activity 2 (NCERT Page 171)</strong>, students collect prices of different sizes of shampoo containers:
      </p>
      <div class="table-container">
        <table class="data-table">
          <thead>
            <tr>
              <th>Container Size</th>
              <th>Volume (mL)</th>
              <th>Retail Price (₹)</th>
              <th>Unit Cost (₹ per mL)</th>
              <th>Proportionality Status</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>Sachet</td>
              <td>6 mL</td>
              <td>₹2</td>
              <td>₹0.33 / mL</td>
              <td>Baseline low-cost entry sachet</td>
            </tr>
            <tr>
              <td>Small Bottle</td>
              <td>180 mL</td>
              <td>₹154</td>
              <td>₹0.86 / mL</td>
              <td><strong>2.6× more expensive per mL!</strong></td>
            </tr>
            <tr>
              <td>Medium Bottle</td>
              <td>340 mL</td>
              <td>₹276</td>
              <td>₹0.81 / mL</td>
              <td>Moderate volume discount</td>
            </tr>
            <tr>
              <td>Large Bottle</td>
              <td>1,000 mL</td>
              <td>₹540</td>
              <td>₹0.54 / mL</td>
              <td>Best bottle value (economy of scale)</td>
            </tr>
          </tbody>
        </table>
      </div>
      <p>
        <strong>Why are prices not proportional to volumes?</strong>
        <br>1. <strong>Sachet Penetration Pricing:</strong> Companies price small sachets cheaply to make the product accessible to rural and low-income buyers.
        <br>2. <strong>Packaging &amp; Dispenser Overheads:</strong> Plastic pump bottles, molds, caps, and branded printing cost significantly more to manufacture than simple plastic pouches.
        <br>3. <strong>Ecological Footprint:</strong> Although sachets have a cheaper upfront price, millions of discarded non-biodegradable multi-layer sachets create catastrophic plastic pollution. Environmentally, large refill packs are far superior.
      </p>

      <!-- INTRICATE SVG 4: DIRECT VS INVERSE PROPORTION GRAPH -->
      <div class="svg-container">
        <svg viewBox="0 0 950 420" xmlns="http://www.w3.org/2000/svg" style="background: #ffffff; border-radius: 16px;">
          <defs>
            <marker id="arrow" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
              <path d="M 0 0 L 10 5 L 0 10 z" fill="#64748b"/>
            </marker>
          </defs>

          <!-- Title Bar -->
          <rect x="25" y="15" width="900" height="42" rx="8" fill="#1e293b" />
          <text x="475" y="42" font-family="'Space Grotesk', sans-serif" font-size="15" font-weight="700" fill="#ffffff" text-anchor="middle">
            FIG 7.4: GRAPHICAL SIGNATURES • DIRECT PROPORTION VS INVERSE VARIATION
          </text>

          <!-- Graph 1: Direct Proportion (Left) -->
          <g transform="translate(60, 80)">
            <rect x="0" y="0" width="380" height="250" rx="8" fill="#f8fafc" stroke="#e2e8f0" />
            <text x="190" y="25" font-family="'Space Grotesk', sans-serif" font-size="13" font-weight="700" fill="#15803d" text-anchor="middle">
              DIRECT PROPORTION: y = kx
            </text>
            <!-- Axes -->
            <line x1="50" y1="210" x2="350" y2="210" stroke="#64748b" stroke-width="2" marker-end="url(#arrow)" />
            <line x1="50" y1="210" x2="50" y2="40" stroke="#64748b" stroke-width="2" marker-end="url(#arrow)" />
            <text x="350" y="235" font-family="'Plus Jakarta Sans', sans-serif" font-size="11" fill="#475569" text-anchor="middle">Quantity (x)</text>
            <text x="35" y="45" font-family="'Plus Jakarta Sans', sans-serif" font-size="11" fill="#475569" text-anchor="middle">Price (y)</text>
            <!-- Linear Line passing through Origin -->
            <line x1="50" y1="210" x2="320" y2="60" stroke="#059669" stroke-width="3.5" />
            <circle cx="50" cy="210" r="5" fill="#047857" />
            <circle cx="140" cy="160" r="4" fill="#047857" />
            <circle cx="230" cy="110" r="4" fill="#047857" />
            <circle cx="320" cy="60" r="4" fill="#047857" />
            <text x="210" y="100" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="700" fill="#047857">Slope k = y/x = const</text>
            <text x="190" y="240" font-family="'Plus Jakarta Sans', sans-serif" font-size="11" font-weight="600" fill="#059669" text-anchor="middle">
              Straight line starting from origin (0, 0)
            </text>
          </g>

          <!-- Graph 2: Inverse Proportion (Right) -->
          <g transform="translate(510, 80)">
            <rect x="0" y="0" width="380" height="250" rx="8" fill="#f8fafc" stroke="#e2e8f0" />
            <text x="190" y="25" font-family="'Space Grotesk', sans-serif" font-size="13" font-weight="700" fill="#b91c1c" text-anchor="middle">
              INVERSE VARIATION: y = k / x (xy = C)
            </text>
            <!-- Axes -->
            <line x1="50" y1="210" x2="350" y2="210" stroke="#64748b" stroke-width="2" marker-end="url(#arrow)" />
            <line x1="50" y1="210" x2="50" y2="40" stroke="#64748b" stroke-width="2" marker-end="url(#arrow)" />
            <text x="350" y="235" font-family="'Plus Jakarta Sans', sans-serif" font-size="11" fill="#475569" text-anchor="middle">Speed (x)</text>
            <text x="35" y="45" font-family="'Plus Jakarta Sans', sans-serif" font-size="11" fill="#475569" text-anchor="middle">Time (y)</text>
            <!-- Hyperbolic Curve -->
            <path d="M 65,55 Q 90,160 330,195" fill="none" stroke="#dc2626" stroke-width="3.5" />
            <circle cx="95" cy="140" r="4" fill="#b91c1c" />
            <circle cx="160" cy="175" r="4" fill="#b91c1c" />
            <circle cx="280" cy="192" r="4" fill="#b91c1c" />
            <text x="180" y="145" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="700" fill="#b91c1c">Product x × y = const</text>
            <text x="190" y="240" font-family="'Plus Jakarta Sans', sans-serif" font-size="11" font-weight="600" fill="#b91c1c" text-anchor="middle">
              Smooth downward curve (Hyperbola)
            </text>
          </g>

          <!-- Bottom Footer Note -->
          <text x="475" y="380" font-family="'Plus Jakarta Sans', sans-serif" font-size="12" font-weight="600" fill="#475569" text-anchor="middle">
            Rule of Three applies ONLY to direct proportion (Graph 1), where double the input yields double the output!
          </text>
        </svg>
        <p class="svg-caption">
          Figure 7.4: Direct proportion forms a straight line passing through (0,0), while inverse variation forms a downward curved rectangular hyperbola.
        </p>
      </div>

      <!-- 2.9 UNIT CONVERSIONS & DIMENSIONAL CONSISTENCY -->
      <h3 class="subheading"><i class="fa-solid fa-ruler"></i> 2.8 Unit Conversions &amp; Dimensional Consistency</h3>
      <p>
        In practical engineering, agriculture, and land measurement, problem solvers encounter quantities measured in different systems of units. Before any ratio can be formed or Trairāśika applied, <strong>both terms must be converted to the same unit</strong>.
      </p>

      <!-- INTRICATE SVG 5: UNIT CONVERSION ROADMAP -->
      <div class="svg-container">
        <svg viewBox="0 0 950 360" xmlns="http://www.w3.org/2000/svg" style="background: #ffffff; border-radius: 16px;">
          <!-- Title Bar -->
          <rect x="25" y="15" width="900" height="42" rx="8" fill="#312e81" />
          <text x="475" y="42" font-family="'Space Grotesk', sans-serif" font-size="15" font-weight="700" fill="#ffffff" text-anchor="middle">
            FIG 7.5: STANDARD CURRICULAR UNIT CONVERSION ROADMAP (NCERT SEC 7.6)
          </text>

          <!-- Node 1: Length -->
          <g transform="translate(40, 85)">
            <rect x="0" y="0" width="200" height="220" rx="10" fill="#eef2ff" stroke="#4f46e5" stroke-width="2" />
            <rect x="0" y="0" width="200" height="38" rx="10" fill="#4f46e5" />
            <text x="100" y="24" font-family="'Space Grotesk', sans-serif" font-size="13" font-weight="700" fill="#ffffff" text-anchor="middle">LENGTH</text>
            <text x="15" y="70" font-family="'Plus Jakarta Sans', sans-serif" font-size="12" font-weight="600" fill="#1e1b4b">1 metre = 3.281 feet</text>
            <text x="15" y="105" font-family="'Plus Jakarta Sans', sans-serif" font-size="12" font-weight="600" fill="#1e1b4b">1 foot = 12 inches</text>
            <text x="15" y="140" font-family="'Plus Jakarta Sans', sans-serif" font-size="12" font-weight="600" fill="#1e1b4b">1 inch = 2.54 cm</text>
            <text x="15" y="175" font-family="'Plus Jakarta Sans', sans-serif" font-size="12" font-weight="600" fill="#1e1b4b">1 km = 1,000 metres</text>
            <rect x="15" y="190" width="170" height="20" rx="4" fill="#e0e7ff" />
            <text x="100" y="204" font-family="'JetBrains Mono', monospace" font-size="10" font-weight="700" fill="#3730a3" text-anchor="middle">1 m ≈ 39.37 inches</text>
          </g>

          <!-- Node 2: Area -->
          <g transform="translate(260, 85)">
            <rect x="0" y="0" width="200" height="220" rx="10" fill="#ecfdf5" stroke="#059669" stroke-width="2" />
            <rect x="0" y="0" width="200" height="38" rx="10" fill="#059669" />
            <text x="100" y="24" font-family="'Space Grotesk', sans-serif" font-size="13" font-weight="700" fill="#ffffff" text-anchor="middle">AREA (LAND)</text>
            <text x="15" y="70" font-family="'Plus Jakarta Sans', sans-serif" font-size="11" font-weight="600" fill="#065f46">1 m² = 10.764 sq ft</text>
            <text x="15" y="105" font-family="'Plus Jakarta Sans', sans-serif" font-size="11" font-weight="700" fill="#047857">1 acre = 43,560 sq ft</text>
            <text x="15" y="140" font-family="'Plus Jakarta Sans', sans-serif" font-size="11" font-weight="600" fill="#065f46">1 hectare = 10,000 m²</text>
            <text x="15" y="175" font-family="'Plus Jakarta Sans', sans-serif" font-size="11" font-weight="600" fill="#065f46">1 hectare = 2.471 acres</text>
            <rect x="15" y="190" width="170" height="20" rx="4" fill="#d1fae5" />
            <text x="100" y="204" font-family="'JetBrains Mono', monospace" font-size="10" font-weight="700" fill="#065f46" text-anchor="middle">1 acre ≈ 4,046.86 m²</text>
          </g>

          <!-- Node 3: Volume -->
          <g transform="translate(480, 85)">
            <rect x="0" y="0" width="200" height="220" rx="10" fill="#fef3c7" stroke="#d97706" stroke-width="2" />
            <rect x="0" y="0" width="200" height="38" rx="10" fill="#d97706" />
            <text x="100" y="24" font-family="'Space Grotesk', sans-serif" font-size="13" font-weight="700" fill="#ffffff" text-anchor="middle">VOLUME &amp; CAPACITY</text>
            <text x="15" y="70" font-family="'Plus Jakarta Sans', sans-serif" font-size="12" font-weight="600" fill="#78350f">1 mL = 1 cm³ (cc)</text>
            <text x="15" y="105" font-family="'Plus Jakarta Sans', sans-serif" font-size="12" font-weight="700" fill="#92400e">1 Litre = 1,000 mL</text>
            <text x="15" y="140" font-family="'Plus Jakarta Sans', sans-serif" font-size="12" font-weight="600" fill="#78350f">1 Litre = 1,000 cc</text>
            <text x="15" y="175" font-family="'Plus Jakarta Sans', sans-serif" font-size="12" font-weight="600" fill="#78350f">1 m³ = 1,000 Litres</text>
            <rect x="15" y="190" width="170" height="20" rx="4" fill="#fde68a" />
            <text x="100" y="204" font-family="'JetBrains Mono', monospace" font-size="10" font-weight="700" fill="#92400e" text-anchor="middle">1 kL = 1 cubic metre</text>
          </g>

          <!-- Node 4: Temperature -->
          <g transform="translate(700, 85)">
            <rect x="0" y="0" width="210" height="220" rx="10" fill="#fee2e2" stroke="#dc2626" stroke-width="2" />
            <rect x="0" y="0" width="210" height="38" rx="10" fill="#dc2626" />
            <text x="105" y="24" font-family="'Space Grotesk', sans-serif" font-size="13" font-weight="700" fill="#ffffff" text-anchor="middle">TEMPERATURE</text>
            <text x="15" y="70" font-family="'Plus Jakarta Sans', sans-serif" font-size="11" font-weight="600" fill="#991b1b">0 °C = 32 °F (Freezing)</text>
            <text x="15" y="95" font-family="'Plus Jakarta Sans', sans-serif" font-size="11" font-weight="600" fill="#991b1b">100 °C = 212 °F (Boiling)</text>
            <text x="15" y="130" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="700" fill="#b91c1c">°F = (9/5)°C + 32</text>
            <text x="15" y="160" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="700" fill="#b91c1c">°C = (5/9)(°F - 32)</text>
            <rect x="15" y="185" width="180" height="24" rx="4" fill="#fecaca" />
            <text x="105" y="201" font-family="'Space Grotesk', sans-serif" font-size="11" font-weight="800" fill="#7f1d1d" text-anchor="middle">25 °C = 77 °F</text>
          </g>
        </svg>
        <p class="svg-caption">
          Figure 7.5: Master unit conversion matrix. Memorize the critical anchors: 1 acre = 43,560 sq ft, 1 m = 3.281 ft, 1 L = 1,000 mL, and °F = 1.8°C + 32.
        </p>
      </div>

      <!-- 2.10 LOGIC RECREATION: BINAIRO / TAKUZU PUZZLES -->
      <h3 class="subheading"><i class="fa-solid fa-puzzle-piece"></i> 2.9 Mathematical Logic in Proportion: The Binairo (Takuzu) Grid</h3>
      <p>
        At the conclusion of Chapter 7 (NCERT Page 178), students are introduced to <strong>Binairo</strong> (also known worldwide as <em>Takuzu</em>). Binairo is a grid logic puzzle governed by proportional parity rules:
      </p>
      <ul>
        <li><strong>Rule 1 (Equal Balance):</strong> Every single row and every column must contain an <em>equal number</em> of horizontal (—) and vertical (|) marks. (In a 6×6 grid, exactly 3 horizontal and 3 vertical lines per row and column).</li>
        <li><strong>Rule 2 (No Triplets):</strong> No more than two identical marks can be placed consecutively in any row or column (e.g., three horizontal lines in a row — — — is strictly forbidden).</li>
        <li><strong>Rule 3 (Uniqueness):</strong> All completed rows must be completely unique, and all completed columns must be completely unique.</li>
      </ul>

      <!-- INTRICATE SVG 6: BINAIRO 6X6 PUZZLE VISUALIZER -->
      <div class="svg-container">
        <svg viewBox="0 0 950 360" xmlns="http://www.w3.org/2000/svg" style="background: #ffffff; border-radius: 16px;">
          <!-- Title -->
          <rect x="25" y="15" width="900" height="42" rx="8" fill="#0f172a" />
          <text x="475" y="42" font-family="'Space Grotesk', sans-serif" font-size="15" font-weight="700" fill="#ffffff" text-anchor="middle">
            FIG 7.6: BINAIRO (TAKUZU) 6×6 LOGIC PUZZLE • BALANCED PARITY GRID
          </text>

          <!-- Left: Starting Clue Grid -->
          <g transform="translate(100, 75)">
            <rect x="0" y="0" width="240" height="240" rx="8" fill="#f8fafc" stroke="#334155" stroke-width="2" />
            <text x="120" y="-12" font-family="'Space Grotesk', sans-serif" font-size="13" font-weight="700" fill="#334155" text-anchor="middle">STARTING PUZZLE</text>
            <!-- 6x6 Grid lines -->
            <path d="M 40,0 L 40,240 M 80,0 L 80,240 M 120,0 L 120,240 M 160,0 L 160,240 M 200,0 L 200,240" stroke="#cbd5e1" stroke-width="1.5" />
            <path d="M 0,40 L 240,40 M 0,80 L 240,80 M 0,120 L 240,120 M 0,160 L 240,160 M 0,200 L 240,200" stroke="#cbd5e1" stroke-width="1.5" />
            
            <!-- Clues -->
            <!-- Row 1: (0,0)=|, (0,2)=| -->
            <line x1="20" y1="8" x2="20" y2="32" stroke="#4f46e5" stroke-width="4" stroke-linecap="round" />
            <line x1="100" y1="8" x2="100" y2="32" stroke="#4f46e5" stroke-width="4" stroke-linecap="round" />
            <!-- Row 2: (1,1)=—, (1,4)=| -->
            <line x1="48" y1="60" x2="72" y2="60" stroke="#d97706" stroke-width="4" stroke-linecap="round" />
            <line x1="180" y1="48" x2="180" y2="72" stroke="#4f46e5" stroke-width="4" stroke-linecap="round" />
            <!-- Row 3: (2,3)=—, (2,5)=— -->
            <line x1="128" y1="100" x2="152" y2="100" stroke="#d97706" stroke-width="4" stroke-linecap="round" />
            <line x1="208" y1="100" x2="232" y2="100" stroke="#d97706" stroke-width="4" stroke-linecap="round" />
            <!-- Row 4: (3,0)=|, (3,2)=— -->
            <line x1="20" y1="128" x2="20" y2="152" stroke="#4f46e5" stroke-width="4" stroke-linecap="round" />
            <line x1="88" y1="140" x2="112" y2="140" stroke="#d97706" stroke-width="4" stroke-linecap="round" />
            <!-- Row 5: (4,1)=|, (4,4)=— -->
            <line x1="60" y1="168" x2="60" y2="192" stroke="#4f46e5" stroke-width="4" stroke-linecap="round" />
            <line x1="168" y1="180" x2="192" y2="180" stroke="#d97706" stroke-width="4" stroke-linecap="round" />
            <!-- Row 6: (5,3)=|, (5,5)=| -->
            <line x1="140" y1="208" x2="140" y2="232" stroke="#4f46e5" stroke-width="4" stroke-linecap="round" />
            <line x1="220" y1="208" x2="220" y2="232" stroke="#4f46e5" stroke-width="4" stroke-linecap="round" />
          </g>

          <!-- Middle Deductive Arrow -->
          <g transform="translate(390, 180)">
            <rect x="0" y="-25" width="160" height="50" rx="8" fill="#e0e7ff" stroke="#6366f1" stroke-width="1.5" />
            <text x="80" y="-5" font-family="'Space Grotesk', sans-serif" font-size="12" font-weight="700" fill="#312e81" text-anchor="middle">DEDUCTIVE LOGIC</text>
            <text x="80" y="14" font-family="'Plus Jakarta Sans', sans-serif" font-size="11" font-weight="600" fill="#4338ca" text-anchor="middle">3 '|' and 3 '—' per line ➔</text>
          </g>

          <!-- Right: Fully Solved Grid -->
          <g transform="translate(600, 75)">
            <rect x="0" y="0" width="240" height="240" rx="8" fill="#f0fdf4" stroke="#16a34a" stroke-width="2" />
            <text x="120" y="-12" font-family="'Space Grotesk', sans-serif" font-size="13" font-weight="700" fill="#15803d" text-anchor="middle">SOLVED BALANCED STATE</text>
            <!-- 6x6 Grid lines -->
            <path d="M 40,0 L 40,240 M 80,0 L 80,240 M 120,0 L 120,240 M 160,0 L 160,240 M 200,0 L 200,240" stroke="#bbf7d0" stroke-width="1.5" />
            <path d="M 0,40 L 240,40 M 0,80 L 240,80 M 0,120 L 240,120 M 0,160 L 240,160 M 0,200 L 240,200" stroke="#bbf7d0" stroke-width="1.5" />
            
            <!-- Row 1: | — | — | — -->
            <line x1="20" y1="8" x2="20" y2="32" stroke="#15803d" stroke-width="3.5" />
            <line x1="48" y1="20" x2="72" y2="20" stroke="#15803d" stroke-width="3.5" />
            <line x1="100" y1="8" x2="100" y2="32" stroke="#15803d" stroke-width="3.5" />
            <line x1="128" y1="20" x2="152" y2="20" stroke="#15803d" stroke-width="3.5" />
            <line x1="180" y1="8" x2="180" y2="32" stroke="#15803d" stroke-width="3.5" />
            <line x1="208" y1="20" x2="232" y2="20" stroke="#15803d" stroke-width="3.5" />

            <!-- Row 2: — — | | — | -->
            <line x1="8" y1="60" x2="32" y2="60" stroke="#15803d" stroke-width="3.5" />
            <line x1="48" y1="60" x2="72" y2="60" stroke="#15803d" stroke-width="3.5" />
            <line x1="100" y1="48" x2="100" y2="72" stroke="#15803d" stroke-width="3.5" />
            <line x1="140" y1="48" x2="140" y2="72" stroke="#15803d" stroke-width="3.5" />
            <line x1="168" y1="60" x2="192" y2="60" stroke="#15803d" stroke-width="3.5" />
            <line x1="220" y1="48" x2="220" y2="72" stroke="#15803d" stroke-width="3.5" />

            <!-- Row 3: | | — — | — -->
            <line x1="20" y1="88" x2="20" y2="112" stroke="#15803d" stroke-width="3.5" />
            <line x1="60" y1="88" x2="60" y2="112" stroke="#15803d" stroke-width="3.5" />
            <line x1="88" y1="100" x2="112" y2="100" stroke="#15803d" stroke-width="3.5" />
            <line x1="128" y1="100" x2="152" y2="100" stroke="#15803d" stroke-width="3.5" />
            <line x1="180" y1="88" x2="180" y2="112" stroke="#15803d" stroke-width="3.5" />
            <line x1="208" y1="100" x2="232" y2="100" stroke="#15803d" stroke-width="3.5" />

            <!-- Row 4: | — — | — | -->
            <line x1="20" y1="128" x2="20" y2="152" stroke="#15803d" stroke-width="3.5" />
            <line x1="48" y1="140" x2="72" y2="140" stroke="#15803d" stroke-width="3.5" />
            <line x1="88" y1="140" x2="112" y2="140" stroke="#15803d" stroke-width="3.5" />
            <line x1="140" y1="128" x2="140" y2="152" stroke="#15803d" stroke-width="3.5" />
            <line x1="168" y1="140" x2="192" y2="140" stroke="#15803d" stroke-width="3.5" />
            <line x1="220" y1="128" x2="220" y2="152" stroke="#15803d" stroke-width="3.5" />

            <!-- Row 5: — | | — — | -->
            <line x1="8" y1="180" x2="32" y2="180" stroke="#15803d" stroke-width="3.5" />
            <line x1="60" y1="168" x2="60" y2="192" stroke="#15803d" stroke-width="3.5" />
            <line x1="100" y1="168" x2="100" y2="192" stroke="#15803d" stroke-width="3.5" />
            <line x1="128" y1="180" x2="152" y2="180" stroke="#15803d" stroke-width="3.5" />
            <line x1="168" y1="180" x2="192" y2="180" stroke="#15803d" stroke-width="3.5" />
            <line x1="220" y1="168" x2="220" y2="192" stroke="#15803d" stroke-width="3.5" />

            <!-- Row 6: — | — | | — -->
            <line x1="8" y1="220" x2="32" y2="220" stroke="#15803d" stroke-width="3.5" />
            <line x1="60" y1="208" x2="60" y2="232" stroke="#15803d" stroke-width="3.5" />
            <line x1="88" y1="220" x2="112" y2="220" stroke="#15803d" stroke-width="3.5" />
            <line x1="140" y1="208" x2="140" y2="232" stroke="#15803d" stroke-width="3.5" />
            <line x1="180" y1="208" x2="180" y2="232" stroke="#15803d" stroke-width="3.5" />
            <line x1="208" y1="220" x2="232" y2="220" stroke="#15803d" stroke-width="3.5" />
          </g>
        </svg>
        <p class="svg-caption">
          Figure 7.6: Binairo logic puzzle grid. Perfect 1:1 balance of vertical and horizontal markers satisfies the discrete proportional condition across every row and column.
        </p>
      </div>

      <!-- 2.11 EXHAUSTIVE BILINGUAL VOCABULARY TABLE (ENGLISH + ODIA) -->
      <h3 class="subheading"><i class="fa-solid fa-language"></i> 2.10 Exhaustive Bilingual Glossary &amp; Vocabulary Bank</h3>
      <p>
        Mastering terminology in both English and standard textbook Odia (ଓଡ଼ିଆ) empowers bilingual middle school learners to excel in both CBSE and BSE Odisha state board examinations:
      </p>

      <div class="table-container">
        <table class="data-table">
          <thead>
            <tr>
              <th>#</th>
              <th>Term / Concept</th>
              <th>Part of Speech</th>
              <th>English Meaning &amp; Mathematical Definition</th>
              <th>ଓଡ଼ିଆ ଅର୍ଥ (Odia Meaning in Odia Script)</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>1</td>
              <td><strong>Ratio</strong></td>
              <td>Noun</td>
              <td>Comparison of two quantities of the same kind by division (<em>a : b</em>).</td>
              <td><strong>ଅନୁପାତ</strong> (ଦୁଇଟି ସଜାତୀୟ ରାଶିର ଭାଗକ୍ରିୟା ଦ୍ୱାରା ତୁଳନା)</td>
            </tr>
            <tr>
              <td>2</td>
              <td><strong>Proportion</strong></td>
              <td>Noun</td>
              <td>An equality between two ratios (<em>a : b :: c : d</em>).</td>
              <td><strong>ସମାନୁପାତ</strong> (ଦୁଇଟି ଅନୁପାତର ସମାନତା)</td>
            </tr>
            <tr>
              <td>3</td>
              <td><strong>Proportional Reasoning</strong></td>
              <td>Noun phrase</td>
              <td>Mathematical thinking based on multiplicative and scaling relations.</td>
              <td><strong>ସମାନୁପାତିକ ଯୁକ୍ତି / ବିଚାର</strong> (ଗୁଣାତ୍ମକ ସମ୍ପର୍କ ଉପରେ ଆଧାରିତ ଗାଣିତିକ ଚିନ୍ତନ)</td>
            </tr>
            <tr>
              <td>4</td>
              <td><strong>Terms of Ratio</strong></td>
              <td>Noun phrase</td>
              <td>The two numbers <em>a</em> and <em>b</em> forming the ratio <em>a : b</em>.</td>
              <td><strong>ଅନୁପାତର ପଦ</strong> (ଅନୁପାତ ଗଠନ କରୁଥିବା ଦୁଇଟି ସଂଖ୍ୟା)</td>
            </tr>
            <tr>
              <td>5</td>
              <td><strong>Antecedent (First Term)</strong></td>
              <td>Noun</td>
              <td>The first term 'a' in the ratio <em>a : b</em>.</td>
              <td><strong>ପୂର୍ବପଦ</strong> (ଅନୁପାତର ପ୍ରଥମ ପଦ 'a')</td>
            </tr>
            <tr>
              <td>6</td>
              <td><strong>Consequent (Second Term)</strong></td>
              <td>Noun</td>
              <td>The second term 'b' in the ratio <em>a : b</em>.</td>
              <td><strong>ଉତ୍ତରପଦ</strong> (ଅନୁପାତର ଦ୍ୱିତୀୟ ପଦ 'b')</td>
            </tr>
            <tr>
              <td>7</td>
              <td><strong>Extremes (Outer Terms)</strong></td>
              <td>Noun (plural)</td>
              <td>The outermost terms <em>a</em> and <em>d</em> in <em>a : b :: c : d</em>.</td>
              <td><strong>ପ୍ରାନ୍ତ ପଦ</strong> (ସମାନୁପାତର ପ୍ରଥମ ଓ ଚତୁର୍ଥ ପଦ)</td>
            </tr>
            <tr>
              <td>8</td>
              <td><strong>Means (Middle Terms)</strong></td>
              <td>Noun (plural)</td>
              <td>The interior middle terms <em>b</em> and <em>c</em> in <em>a : b :: c : d</em>.</td>
              <td><strong>ମଧ୍ୟ ପଦ</strong> (ସମାନୁପାତର ଦ୍ୱିତୀୟ ଓ ତୃତୀୟ ପଦ)</td>
            </tr>
            <tr>
              <td>9</td>
              <td><strong>Simplest Form</strong></td>
              <td>Noun phrase</td>
              <td>A ratio where HCF of both terms is 1 (co-prime terms).</td>
              <td><strong>ସରଳତମ ରୂପ / ଲଘୁଷ୍ଠ ଆକାର</strong> (ପଦଦ୍ୱୟର ଗ.ସା.ଗୁ. ୧ ହେବା)</td>
            </tr>
            <tr>
              <td>10</td>
              <td><strong>Equivalent Ratios</strong></td>
              <td>Noun phrase</td>
              <td>Ratios that represent the exact same quotient or fraction.</td>
              <td><strong>ସମତୁଲ୍ୟ ଅନୁପାତ</strong> (ସମାନ ମୂଲ୍ୟ ପ୍ରକାଶ କରୁଥିବା ଅନୁପାତ)</td>
            </tr>
            <tr>
              <td>11</td>
              <td><strong>Cross-Multiplication</strong></td>
              <td>Noun</td>
              <td>Multiplying extremes and means across an equality: <em>ad = bc</em>.</td>
              <td><strong>ବଜ୍ର ଗୁଣନ / ତେର୍ଚ୍ଛା ଗୁଣନ</strong> (ପ୍ରାନ୍ତପଦ ଗୁଣନଫଳ = ମଧ୍ୟପଦ ଗୁଣନଫଳ)</td>
            </tr>
            <tr>
              <td>12</td>
              <td><strong>Trairāśika (Rule of Three)</strong></td>
              <td>Noun</td>
              <td>Ancient Indian algorithm to find a 4th unknown from 3 known proportional terms.</td>
              <td><strong>ତ୍ରୈରାଶିକ ନିୟମ</strong> (ତିନୋଟି ଜ୍ଞାତ ରାଶିରୁ ଅଜ୍ଞାତ ଚତୁର୍ଥ ରାଶି ନିର୍ଣ୍ଣୟ ନିୟମ)</td>
            </tr>
            <tr>
              <td>13</td>
              <td><strong>Pramāṇa (Measure)</strong></td>
              <td>Noun</td>
              <td>The known standard reference quantity in Trairāśika ('a').</td>
              <td><strong>ପ୍ରମାଣ</strong> (ତ୍ରୈରାଶିକରେ ଦିଆଯାଇଥିବା ପ୍ରମାଣିକ ମାପ)</td>
            </tr>
            <tr>
              <td>14</td>
              <td><strong>Phala (Fruit / Result)</strong></td>
              <td>Noun</td>
              <td>The known output or produce yielded by Pramāṇa ('b').</td>
              <td><strong>ଫଳ</strong> (ପ୍ରମାଣରୁ ମିଳୁଥିବା ଜ୍ଞାତ ପରିଣାମ ବା ଉତ୍ପାଦ)</td>
            </tr>
            <tr>
              <td>15</td>
              <td><strong>Ichchhā (Requisition)</strong></td>
              <td>Noun</td>
              <td>The new question input or desired inquiry in Trairāśika ('c').</td>
              <td><strong>ଇଚ୍ଛା</strong> (ନୂତନ ପ୍ରଶ୍ନର ଅଭୀପ୍ସିତ ମାପ ବା ଚାହିଦା)</td>
            </tr>
            <tr>
              <td>16</td>
              <td><strong>Ichchhāphala (Yield)</strong></td>
              <td>Noun</td>
              <td>The unknown fourth result to be computed ('d').</td>
              <td><strong>ଇଚ୍ଛାଫଳ</strong> (ଇଚ୍ଛାରୁ ମିଳିବାକୁ ଥିବା ଫଳାଫଳ ବା ଅଜ୍ଞାତ ରାଶି)</td>
            </tr>
            <tr>
              <td>17</td>
              <td><strong>Unitary Method</strong></td>
              <td>Noun phrase</td>
              <td>Finding the value of a single unit first, then multiplying by desired units.</td>
              <td><strong>ଐକିକ ନିୟମ</strong> (ପ୍ରଥମେ ଗୋଟିଏ ଏକକର ମୂଲ୍ୟ ବାହାର କରି ସମାଧାନ କରିବା)</td>
            </tr>
            <tr>
              <td>18</td>
              <td><strong>Direct Proportion</strong></td>
              <td>Noun phrase</td>
              <td>Relation where two quantities increase or decrease by the same factor (<em>y/x = k</em>).</td>
              <td><strong>ପ୍ରତ୍ୟକ୍ଷ ସମାନୁପାତ</strong> (ଗୋଟିଏ ବଢ଼ିଲେ ଅନ୍ୟଟି ସମାନ ହାରରେ ବଢ଼ିବା)</td>
            </tr>
            <tr>
              <td>19</td>
              <td><strong>Inverse Proportion</strong></td>
              <td>Noun phrase</td>
              <td>Relation where an increase in one causes a proportional decrease in other (<em>xy = k</em>).</td>
              <td><strong>ବ୍ୟସ୍ତ ସମାନୁପାତ</strong> (ଗୋଟିଏ ବଢ଼ିଲେ ଅନ୍ୟଟି ସମାନ ହାରରେ କମିବା)</td>
            </tr>
            <tr>
              <td>20</td>
              <td><strong>Constant of Proportionality</strong></td>
              <td>Noun phrase</td>
              <td>The invariant constant ratio <em>k = y / x</em> in a direct proportional relationship.</td>
              <td><strong>ସମାନୁପାତିକ ସ୍ଥିରାଙ୍କ</strong> (ଅନୁପାତର ଅପରିବର୍ତ୍ତନୀୟ ମୂଲ୍ୟ 'k')</td>
            </tr>
            <tr>
              <td>21</td>
              <td><strong>Aspect Ratio</strong></td>
              <td>Noun phrase</td>
              <td>The proportional ratio of the width to the height of an image or screen.</td>
              <td><strong>ଦୈର୍ଘ୍ୟ-ପ୍ରସ୍ଥ ଅନୁପାତ</strong> (ଛବିର ପ୍ରସ୍ଥ ଓ ଉଚ୍ଚତାର ଅନୁପାତ)</td>
            </tr>
            <tr>
              <td>22</td>
              <td><strong>Distortion</strong></td>
              <td>Noun</td>
              <td>Unnatural stretching or squishing caused by non-proportional scaling.</td>
              <td><strong>ବିକୃତି</strong> (ଅସମାନୁପାତିକ ପରିବର୍ତ୍ତନ ଯୋଗୁଁ ଆକାର ନଷ୍ଟ ହେବା)</td>
            </tr>
            <tr>
              <td>23</td>
              <td><strong>Geometric Similarity</strong></td>
              <td>Noun phrase</td>
              <td>Property of figures having the same shape with proportional corresponding sides.</td>
              <td><strong>ଜ୍ୟାମିତିକ ସାଦୃଶ୍ୟ</strong> (ସମାନ ଆକୃତି ଏବଂ ସମାନୁପାତିକ ବାହୁ ବିଶିଷ୍ଟ ଚିତ୍ର)</td>
            </tr>
            <tr>
              <td>24</td>
              <td><strong>Partitioning (Group Division)</strong></td>
              <td>Noun</td>
              <td>Dividing a total quantity into parts according to a given ratio <em>m : n</em>.</td>
              <td><strong>ଭାଗ ବଣ୍ଟନ</strong> (ଏକ ସମୁଦାୟ ରାଶିକୁ ନିର୍ଦ୍ଦିଷ୍ଟ ଅନୁପାତରେ ବିଭାଜନ କରିବା)</td>
            </tr>
            <tr>
              <td>25</td>
              <td><strong>Highest Common Factor (HCF)</strong></td>
              <td>Noun phrase</td>
              <td>The greatest positive integer that divides two numbers without remainder.</td>
              <td><strong>ଗରିଷ୍ଠ ସାଧାରଣ ଗୁଣନୀୟକ (ଗ.ସା.ଗୁ.)</strong></td>
            </tr>
            <tr>
              <td>26</td>
              <td><strong>Scale Factor</strong></td>
              <td>Noun phrase</td>
              <td>The positive multiplier used to enlarge or reduce geometric dimensions.</td>
              <td><strong>ମାପ ଗୁଣକ</strong> (ଚିତ୍ର ବା ମାପ ବୃଦ୍ଧି/ହ୍ରାସ ପାଇଁ ବ୍ୟବହୃତ ଗୁଣକ)</td>
            </tr>
            <tr>
              <td>27</td>
              <td><strong>Dimensional Consistency</strong></td>
              <td>Noun phrase</td>
              <td>Harmonizing units so both terms in a ratio share the exact same measurement unit.</td>
              <td><strong>ଏକକ ସଙ୍ଗତି</strong> (ଅନୁପାତ ଗଠନ ପୂର୍ବରୁ ଉଭୟ ରାଶିକୁ ଏକା ଏକକରେ ରୂପାନ୍ତର)</td>
            </tr>
            <tr>
              <td>28</td>
              <td><strong>Population Density</strong></td>
              <td>Noun phrase</td>
              <td>The ratio of total population to total surface area (people per sq km).</td>
              <td><strong>ଜନସଂଖ୍ୟା ଘନତ୍ୱ</strong> (ପ୍ରତି ବର୍ଗ କିଲୋମିଟରରେ ବସବାସ କରୁଥିବା ଲୋକସଂଖ୍ୟା)</td>
            </tr>
            <tr>
              <td>29</td>
              <td><strong>Alloy</strong></td>
              <td>Noun</td>
              <td>A homogeneous mixture of two or more metals in a fixed mass ratio.</td>
              <td><strong>ମିଶ୍ରଧାତୁ</strong> (ନିର୍ଦ୍ଦିଷ୍ଟ ଅନୁପାତରେ ମିଶ୍ରିତ ଧାତୁ, ଯଥା କପ୍ରୋ-ନିକେଲ୍)</td>
            </tr>
            <tr>
              <td>30</td>
              <td><strong>Cupro-Nickel</strong></td>
              <td>Noun</td>
              <td>An alloy of copper and nickel (3:1 ratio) used in minting modern ₹10 coins.</td>
              <td><strong>କପ୍ରୋ-ନିକେଲ୍</strong> (ତମ୍ବା ଓ ନିକେଲ୍ ର ୩ : ୧ ମିଶ୍ରଧାତୁ)</td>
            </tr>
            <tr>
              <td>31</td>
              <td><strong>Pala &amp; Niska</strong></td>
              <td>Noun (historical)</td>
              <td>Ancient Indian units of mass (Pala) and gold coinage (Niska) in <em>Līlāvatī</em>.</td>
              <td><strong>ପଳ ଓ ନିଷ୍କ</strong> (ପ୍ରାଚୀନ ଭାରତୀୟ ଓଜନ ଏବଂ ସ୍ୱର୍ଣ୍ଣ ମୁଦ୍ରା ଏକକ)</td>
            </tr>
            <tr>
              <td>32</td>
              <td><strong>Binairo (Takuzu)</strong></td>
              <td>Noun</td>
              <td>A balanced logic grid puzzle played with equal horizontal and vertical line marks.</td>
              <td><strong>ବିନାଇରୋ (ତର୍କ କୂଟପ୍ରଶ୍ନ)</strong> (ସମାନୁପାତିକ ସନ୍ତୁଳନ ଉପରେ ଆଧାରିତ ଗ୍ରୀଡ୍ ଖେଳ)</td>
            </tr>
          </tbody>
        </table>
      </div>
    </section>
"""
