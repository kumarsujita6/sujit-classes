# -*- coding: utf-8 -*-
"""
Section 2: Complete Line-by-Line Conceptual Explanations & Exhaustive Bilingual Glossary
Class 8 Mathematics Chapter 10: Proportional Reasoning - 2
"""

def get_section_2():
    return """
    <!-- ==========================================================
         SECTION 2: COMPLETE LINE-BY-LINE CONCEPTUAL EXPLANATIONS
         ========================================================== -->
    <section id="section2" class="section-box">
      <div class="section-header">
        <div class="section-header-left">
          <span class="section-tag"><i class="fa-solid fa-book-open-reader"></i> Comprehensive Theory</span>
          <h2 class="section-title">Section 2: Complete Line-by-Line Conceptual Explanations</h2>
          <p class="section-desc">
            Every concept, definition, derivation, and textbook nuance explained in crystal-clear, teacher-guided language with zero omissions.
          </p>
        </div>
      </div>

      <!-- 2.1 Proportionality: A Quick Recap -->
      <div class="concept-card">
        <h3 class="concept-card-title"><i class="fa-solid fa-arrows-spin"></i> 2.1 Proportionality — A Quick Recap</h3>
        <p>
          In our daily lives, quantities rarely exist in isolation; they change in harmony with one another. When two or more related quantities change by the <strong>exact same multiplying factor</strong>, we say that their relationship is a <strong>proportional relationship</strong>.
        </p>

        <div class="callout callout-def">
          <div class="callout-title"><i class="fa-solid fa-lightbulb"></i> Mathematical Definition: Proportional Relationship</div>
          <p>
            Two quantities <em>x</em> and <em>y</em> are said to be in <strong>direct proportion</strong> if the ratio of any value of <em>x</em> to its corresponding value of <em>y</em> remains constant. That is:
          </p>
          <div class="math-block">
            x / y = k &nbsp;&nbsp;(where k is a positive constant called the Constant of Proportionality)
          </div>
          <p>
            This implies that if <em>x</em> is multiplied by any factor <em>m</em>, the corresponding value of <em>y</em> must also be multiplied by the same factor <em>m</em>.
          </p>
        </div>

        <h4>The Culinary Idli Batter Paradigm</h4>
        <p>
          Consider the traditional preparation of South Indian idlis. Idli batter is prepared by fermenting a mixture of rice and urad dal (black gram). The softness, fluffiness, and authentic taste of the idlis depend strictly on preserving the ratio of these two ingredients:
        </p>
        <ul>
          <li><strong>Standard Recipe:</strong> For every 2 cups of rice, exactly 1 cup of urad dal is added. We write this ratio as <code>2 : 1</code>.</li>
          <li><strong>Viswanath's Batch:</strong> Viswanath prepares a family breakfast using <strong>6 cups of rice</strong> and <strong>3 cups of urad dal</strong> (Ratio <code>6 : 3</code>).</li>
          <li><strong>Puneet's Batch:</strong> Puneet prepares a smaller breakfast using <strong>4 cups of rice</strong> and <strong>2 cups of urad dal</strong> (Ratio <code>4 : 2</code>).</li>
        </ul>
        <p>
          <em>Will Viswanath's and Puneet's idlis taste identical?</em><br>
          Yes! If cooked in the same way, their idlis will taste exactly identical because both ingredient mixtures maintain the identical proportion. Let us prove this mathematically using two equivalent methods:
        </p>

        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 1rem; margin: 1.25rem 0;">
          <div style="background: #f8fafc; border: 1px solid var(--border); padding: 1.25rem; border-radius: 12px;">
            <h5 style="color: var(--primary); margin-bottom: 0.5rem;"><i class="fa-solid fa-divide"></i> Method 1: Fraction Simplification</h5>
            <p style="font-size: 0.9rem; margin-bottom: 0.4rem;">
              • Viswanath's ratio: <code>6 / 3 = 2 / 1 = 2</code><br>
              • Puneet's ratio: <code>4 / 2 = 2 / 1 = 2</code>
            </p>
            <p style="font-size: 0.85rem; color: var(--text-muted); margin-bottom: 0;">
              Since both fractions simplify to the same irreducible fraction <code>2/1</code>, the ratios are equivalent.
            </p>
          </div>

          <div style="background: #f8fafc; border: 1px solid var(--border); padding: 1.25rem; border-radius: 12px;">
            <h5 style="color: var(--secondary); margin-bottom: 0.5rem;"><i class="fa-solid fa-xmark"></i> Method 2: Cross-Multiplication</h5>
            <p style="font-size: 0.9rem; margin-bottom: 0.4rem;">
              Set the two ratios side by side: <code>6 : 3</code> and <code>4 : 2</code>.<br>
              • Product of Extremes = <code>6 × 2 = 12</code><br>
              • Product of Means = <code>3 × 4 = 12</code>
            </p>
            <p style="font-size: 0.85rem; color: var(--text-muted); margin-bottom: 0;">
              Since the cross-products are equal (<code>12 = 12</code>), the two ratios form a valid proportion: <code>6 : 3 :: 4 : 2</code>.
            </p>
          </div>
        </div>

        <div class="callout callout-hack">
          <div class="callout-title"><i class="fa-solid fa-wand-magic-sparkles"></i> Teacher's Algebraic Proof: Why Cross-Multiplication Works</div>
          <p>
            Suppose we are testing if two ratios <em>a : b</em> and <em>c : d</em> are in proportion. That is, we test if:
          </p>
          <div class="math-block">
            a / b = c / d
          </div>
          <p>
            Multiply both sides of the equation by the common denominator <code>b × d</code>:
          </p>
          <div class="math-block">
            (a / b) × (b × d) = (c / d) × (b × d)<br>
            ⇒ a × d = b × c
          </div>
          <p>
            Hence, <strong>Product of Extremes (a × d) = Product of Means (b × c)</strong> is a necessary and sufficient mathematical condition for any two ratios to be proportional!
          </p>
        </div>
      </div>

      <!-- SVG 2: Direct Proportion vs Inverse Proportion Graphs -->
      <div class="svg-graphic-box">
        <svg viewBox="0 0 950 420" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg" style="font-family: 'Plus Jakarta Sans', sans-serif;">
          <rect width="950" height="420" fill="#f8fafc" rx="16" />

          <!-- Panel 1: Direct Proportion (Left) -->
          <g transform="translate(60, 40)">
            <rect x="0" y="0" width="380" height="340" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.5" rx="12" />
            <text x="190" y="30" text-anchor="middle" font-family="'Space Grotesk', sans-serif" font-size="16" font-weight="700" fill="#0369a1">DIRECT PROPORTION (y = k · x)</text>
            <text x="190" y="48" text-anchor="middle" font-size="11" fill="#64748b">Quotient is Constant: y / x = k</text>
            
            <!-- Axes -->
            <line x1="50" y1="280" x2="340" y2="280" stroke="#475569" stroke-width="2" marker-end="url(#arrow)" />
            <line x1="50" y1="280" x2="50" y2="70" stroke="#475569" stroke-width="2" />
            <text x="340" y="300" text-anchor="end" font-size="12" font-weight="600" fill="#475569">Quantity x →</text>
            <text x="40" y="70" text-anchor="end" font-size="12" font-weight="600" fill="#475569">Quantity y ↑</text>
            <text x="42" y="295" font-size="11" fill="#94a3b8">0</text>

            <!-- Direct Line Ray passing through origin -->
            <line x1="50" y1="280" x2="310" y2="90" stroke="#0284c7" stroke-width="3.5" />
            
            <!-- Points on direct ray -->
            <circle cx="115" cy="232" r="5" fill="#0369a1" />
            <line x1="115" y1="280" x2="115" y2="232" stroke="#94a3b8" stroke-dasharray="3,3" />
            <line x1="50" y1="232" x2="115" y2="232" stroke="#94a3b8" stroke-dasharray="3,3" />
            <text x="115" y="295" text-anchor="middle" font-size="10" fill="#0f172a">x₁</text>
            <text x="38" y="235" text-anchor="end" font-size="10" fill="#0f172a">y₁</text>

            <circle cx="230" cy="148" r="5" fill="#0369a1" />
            <line x1="230" y1="280" x2="230" y2="148" stroke="#94a3b8" stroke-dasharray="3,3" />
            <line x1="50" y1="148" x2="230" y2="148" stroke="#94a3b8" stroke-dasharray="3,3" />
            <text x="230" y="295" text-anchor="middle" font-size="10" fill="#0f172a">2x₁</text>
            <text x="38" y="151" text-anchor="end" font-size="10" fill="#0f172a">2y₁</text>

            <rect x="80" y="80" width="160" height="35" rx="6" fill="#e0f2fe" stroke="#0284c7" />
            <text x="160" y="102" text-anchor="middle" font-size="11" font-weight="700" fill="#0369a1">Straight line through (0,0)</text>
          </g>

          <!-- Panel 2: Inverse Proportion (Right) -->
          <g transform="translate(510, 40)">
            <rect x="0" y="0" width="380" height="340" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.5" rx="12" />
            <text x="190" y="30" text-anchor="middle" font-family="'Space Grotesk', sans-serif" font-size="16" font-weight="700" fill="#0d9488">INVERSE PROPORTION (x · y = k)</text>
            <text x="190" y="48" text-anchor="middle" font-size="11" fill="#64748b">Product is Constant: x · y = Area k</text>
            
            <!-- Axes -->
            <line x1="50" y1="280" x2="340" y2="280" stroke="#475569" stroke-width="2" />
            <line x1="50" y1="280" x2="50" y2="70" stroke="#475569" stroke-width="2" />
            <text x="340" y="300" text-anchor="end" font-size="12" font-weight="600" fill="#475569">Speed x (km/h) →</text>
            <text x="40" y="70" text-anchor="end" font-size="12" font-weight="600" fill="#475569">Time y (h) ↑</text>
            <text x="42" y="295" font-size="11" fill="#94a3b8">0</text>

            <!-- Shaded constant area rectangle 1 -->
            <rect x="50" y="190" width="80" height="90" fill="#ccfbf1" opacity="0.6" stroke="#0d9488" stroke-width="1" stroke-dasharray="2,2" />
            <text x="90" y="240" text-anchor="middle" font-size="10" font-weight="700" fill="#0f766e">Area = k</text>

            <!-- Shaded constant area rectangle 2 -->
            <rect x="50" y="235" width="160" height="45" fill="#fef3c7" opacity="0.6" stroke="#d97706" stroke-width="1" stroke-dasharray="2,2" />
            <text x="150" y="262" text-anchor="middle" font-size="10" font-weight="700" fill="#b45309">Area = k</text>

            <!-- Hyperbolic Curve -->
            <path d="M 65 95 Q 90 220, 310 268" fill="none" stroke="#0d9488" stroke-width="3.5" />
            
            <circle cx="90" cy="225" r="5" fill="#0d9488" />
            <circle cx="170" cy="250" r="5" fill="#0d9488" />
            <circle cx="270" cy="265" r="5" fill="#0d9488" />

            <rect x="180" y="80" width="180" height="35" rx="6" fill="#f0fdfa" stroke="#0d9488" />
            <text x="270" y="102" text-anchor="middle" font-size="11" font-weight="700" fill="#0f766e">Rectangular Hyperbola</text>
          </g>
        </svg>
        <p class="svg-caption"><strong>Figure 2.1:</strong> Geometric &amp; Graphic Comparison: Direct variation forms a linear ray through the origin (constant gradient y/x = k), whereas Inverse variation forms a rectangular hyperbola where each point defines a rectangle of invariant area (x · y = k).</p>
      </div>

      <!-- 2.2 Ratios in Maps & Cartographic Scales -->
      <div class="concept-card">
        <h3 class="concept-card-title"><i class="fa-solid fa-map-location-dot"></i> 2.2 Ratios in Maps &amp; Cartographic Scales</h3>
        <p>
          Have you ever held an atlas or examined a printed geographic map and noticed a tiny ratio printed in the bottom corner, such as <code>1 : 60,00,000</code>? This mathematical ratio is called the <strong>Representative Fraction (RF)</strong> or the <strong>Map Scale</strong>.
        </p>

        <div class="callout callout-def">
          <div class="callout-title"><i class="fa-solid fa-ruler-combined"></i> Definition: Representative Fraction (RF)</div>
          <p>
            A <strong>Representative Fraction (RF)</strong> is a dimensionless ratio that expresses the relationship between a measured distance on a map and the corresponding actual geographical distance on the ground:
          </p>
          <div class="math-block">
            RF = Distance on the Map / Corresponding Actual Distance on the Ground
          </div>
          <p>
            <strong>Crucial Rule of Cartography:</strong> Both the numerator (map distance) and the denominator (ground distance) must be expressed in the <em>exact same unit of measurement</em> before writing the ratio!
          </p>
        </div>

        <h4>Deconstructing Scale RF 1 : 60,00,000</h4>
        <p>
          What does <code>RF 1 : 60,00,000</code> physically mean?
        </p>
        <ul>
          <li>It means that <strong>1 centimeter</strong> on the map corresponds to <strong>60,00,000 centimeters</strong> on the surface of the Earth.</li>
          <li>It also means <strong>1 millimeter</strong> on the map corresponds to <strong>60,00,000 millimeters</strong> on the ground.</li>
          <li>Because people do not measure driving distances in centimeters, we must bridge metric units using proportional conversion factors!</li>
        </ul>

        <div class="callout callout-act">
          <div class="callout-title"><i class="fa-solid fa-calculator"></i> Step-by-Step Metric Unit Conversion Proof</div>
          <p>
            Let us convert <code>60,00,000 cm</code> into kilometers:
          </p>
          <ol>
            <li><strong>Step 1 (Centimeters to Metres):</strong> Since <code>1 metre = 100 centimetres</code>, divide by 100:
              <div class="math-block">60,00,000 cm ÷ 100 = 60,000 metres</div>
            </li>
            <li><strong>Step 2 (Metres to Kilometres):</strong> Since <code>1 kilometre = 1,000 metres</code>, divide by 1,000:
              <div class="math-block">60,000 metres ÷ 1,000 = 60 kilometres</div>
            </li>
          </ol>
          <p>
            <strong>Master Conversion Benchmark:</strong> <code>1 kilometre = 1,000 × 100 = 1,00,000 cm</code> (one lakh centimeters).<br>
            Therefore, on a map with <code>RF 1 : 60,00,000</code>:
          </p>
          <div class="math-block" style="background: #ecfdf5; border-color: #10b981; color: #065f46; font-weight: 700;">
            1 cm on the map = 60 km of actual geographical ground distance!
          </div>
        </div>

        <h4>Geographical Straight-Line Distance vs. Actual Road Distance</h4>
        <p>
          The textbook presents an imperative real-world caution: <em>The distance calculated using a map scale is the direct geographical distance (as the crow flies), not the road distance!</em>
        </p>
        <div class="data-table-wrapper">
          <table class="data-table">
            <thead>
              <tr>
                <th>Measurement Type</th>
                <th>Physical Meaning</th>
                <th>How It Is Measured</th>
                <th>Why It Differs</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>Geographical Distance (Crow-Flight)</strong></td>
                <td>The shortest, straight-line geodesic arc between two coordinate points on the Earth's surface.</td>
                <td>Measured with a straight ruler on the map and multiplied by the scale factor (e.g., <code>distance in cm × 60 km</code>).</td>
                <td>Ignores all terrain obstacles, rivers, hills, valleys, and national borders.</td>
              </tr>
              <tr>
                <td><strong>Road / Travel Distance</strong></td>
                <td>The actual odometer mileage travelled by a bus, car, or train along constructed highways.</td>
                <td>Measured using vehicle odometers, digital GPS navigation algorithms, or flexible curve-following string on topographic sheets.</td>
                <td>Roads must bend around mountains, traverse designated bridges, pass through toll gates, and follow bypasses, making road distance typically <strong>15% to 35% longer</strong> than geographical straight-line distance.</td>
              </tr>
            </tbody>
          </table>
        </div>

        <h4>Analysing the South India Map (Page 56)</h4>
        <p>
          Using the South India map given in the textbook with <code>RF 1 : 60,00,000</code>:
        </p>
        <ul>
          <li><strong>Bengaluru to Chennai:</strong> The straight-line distance measured with a ruler on the map is approximately <strong>4.83 cm to 5.0 cm</strong>.
            <div class="math-block">Actual Distance = 4.83 cm × 60 km/cm ≈ 290 km to 300 km</div>
            (The actual highway driving distance via NH48 / NH44 is approximately 345 km).
          </li>
          <li><strong>Mangaluru to Chennai:</strong> The ruler distance on the map across the entire width of Peninsular India (west coast to east coast) measures approximately <strong>9.8 cm to 10.0 cm</strong>.
            <div class="math-block">Actual Distance = 10.0 cm × 60 km/cm = 600 km</div>
            (The winding rail/road route crossing the Western Ghats is approximately 710 km).
          </li>
        </ul>

        <h4>Classroom Map-Making Activity (Scale 1 : 50)</h4>
        <p>
          The textbook encourages students to act as civil engineers and architects by drafting a scale blueprint of their own classroom:
        </p>
        <ul>
          <li><strong>Chosen Scale:</strong> <code>1 : 50</code>.</li>
          <li><strong>What 1 : 50 means:</strong> <code>1 cm on paper = 50 cm in the room</code> (which equals <code>0.5 metres</code>). Conversely, <strong>2 cm on paper represents 1 full metre</strong> in the room!</li>
          <li><strong>Classroom Dimensions:</strong> If a standard classroom measures <strong>8 metres long</strong> and <strong>6 metres wide</strong>:
            <div class="math-block">
              Drawing Length = 8 m ÷ 0.5 m/cm = 16 cm<br>
              Drawing Width = 6 m ÷ 0.5 m/cm = 12 cm
            </div>
          </li>
          <li><strong>Marking Objects:</strong> A teacher's table measuring <code>100 cm × 50 cm</code> will be drawn as a neat rectangle of <code>2 cm × 1 cm</code>. Ceiling fans, tube lights, student dual-desks, and doors are positioned with architectural symbols according to their scaled coordinates.</li>
        </ul>
      </div>

      <!-- SVG 3: Cartographic Scale & Representative Fraction Map -->
      <div class="svg-graphic-box">
        <svg viewBox="0 0 950 400" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg" style="font-family: 'Plus Jakarta Sans', sans-serif;">
          <defs>
            <linearGradient id="mapBg" x1="0%" y1="0%" x2="100%" y2="100%">
              <stop offset="0%" stop-color="#f0fdf4" />
              <stop offset="100%" stop-color="#e0f2fe" />
            </linearGradient>
            <filter id="mapShadow">
              <feDropShadow dx="0" dy="3" stdDeviation="4" flood-opacity="0.1" />
            </filter>
          </defs>
          <rect width="950" height="400" fill="#f8fafc" rx="16" />

          <!-- Map Frame -->
          <rect x="40" y="30" width="540" height="340" fill="url(#mapBg)" stroke="#0369a1" stroke-width="2" rx="10" filter="url(#mapShadow)" />
          
          <!-- Latitude & Longitude grid lines -->
          <line x1="40" y1="110" x2="580" y2="110" stroke="#bae6fd" stroke-width="1" stroke-dasharray="4,4" />
          <line x1="40" y1="190" x2="580" y2="190" stroke="#bae6fd" stroke-width="1" stroke-dasharray="4,4" />
          <line x1="40" y1="270" x2="580" y2="270" stroke="#bae6fd" stroke-width="1" stroke-dasharray="4,4" />
          <line x1="175" y1="30" x2="175" y2="370" stroke="#bae6fd" stroke-width="1" stroke-dasharray="4,4" />
          <line x1="310" y1="30" x2="310" y2="370" stroke="#bae6fd" stroke-width="1" stroke-dasharray="4,4" />
          <line x1="445" y1="30" x2="445" y2="370" stroke="#bae6fd" stroke-width="1" stroke-dasharray="4,4" />

          <!-- Coastline mock curve -->
          <path d="M 120 30 C 130 140, 110 220, 190 320 C 230 360, 260 370, 280 370" fill="none" stroke="#0284c7" stroke-width="2" />
          <text x="80" y="200" fill="#0284c7" font-size="12" font-weight="700" letter-spacing="2">ARABIAN SEA</text>
          <text x="470" y="200" fill="#0284c7" font-size="12" font-weight="700" letter-spacing="2">BAY OF BENGAL</text>

          <!-- Cities -->
          <!-- Mangaluru -->
          <circle cx="150" cy="190" r="6" fill="#dc2626" stroke="#ffffff" stroke-width="2" />
          <text x="145" y="175" text-anchor="end" font-size="12" font-weight="700" fill="#0f172a">Mangaluru</text>

          <!-- Bengaluru -->
          <circle cx="280" cy="200" r="6" fill="#dc2626" stroke="#ffffff" stroke-width="2" />
          <text x="280" y="185" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a">Bengaluru</text>

          <!-- Chennai -->
          <circle cx="450" cy="210" r="6" fill="#dc2626" stroke="#ffffff" stroke-width="2" />
          <text x="460" y="205" text-anchor="start" font-size="12" font-weight="700" fill="#0f172a">Chennai</text>

          <!-- Straight-line vectors (Geographical Distance) -->
          <line x1="280" y1="200" x2="450" y2="210" stroke="#059669" stroke-width="3" />
          <text x="365" y="195" text-anchor="middle" font-size="11" font-weight="700" fill="#047857">~4.8 cm (≈ 290 km)</text>

          <line x1="150" y1="190" x2="450" y2="210" stroke="#7c3aed" stroke-width="2.5" stroke-dasharray="5,3" />
          <text x="300" y="245" text-anchor="middle" font-size="11" font-weight="700" fill="#6d28d9">Mangaluru to Chennai: ~10 cm (≈ 600 km)</text>

          <!-- Curving winding road line (Road Distance) -->
          <path d="M 280 200 Q 330 170, 360 215 T 450 210" fill="none" stroke="#dc2626" stroke-width="2" stroke-dasharray="2,2" />
          <text x="390" y="270" text-anchor="middle" font-size="10" font-weight="600" fill="#dc2626">Actual Winding Highway (345 km)</text>

          <!-- Compass Rose -->
          <g transform="translate(520, 75)">
            <circle cx="0" cy="0" r="22" fill="#ffffff" stroke="#cbd5e1" />
            <polygon points="0,-18 5,-4 0,0 -5,-4" fill="#dc2626" />
            <polygon points="0,18 5,4 0,0 -5,4" fill="#475569" />
            <polygon points="18,0 4,5 0,0 4,-5" fill="#475569" />
            <polygon points="-18,0 -4,5 0,0 -4,-5" fill="#475569" />
            <text x="0" y="-22" text-anchor="middle" font-size="10" font-weight="800" fill="#dc2626">N</text>
          </g>

          <!-- RF Scale Legend on Map -->
          <rect x="360" y="325" width="205" height="35" rx="6" fill="#ffffff" stroke="#0369a1" />
          <text x="462" y="347" text-anchor="middle" font-size="12" font-weight="800" fill="#0369a1">RF = 1 : 60,00,000</text>

          <!-- Side Explanation Card (Right) -->
          <g transform="translate(610, 30)">
            <rect x="0" y="0" width="300" height="340" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.5" rx="12" />
            <rect x="0" y="0" width="300" height="40" rx="12" fill="#0369a1" />
            <text x="150" y="25" text-anchor="middle" font-size="13" font-weight="700" fill="#ffffff">SCALE MATHEMATICS</text>
            
            <text x="20" y="65" font-size="12" font-weight="700" fill="#0f172a">1. The Scale Formula:</text>
            <text x="20" y="85" font-size="11" font-family="'JetBrains Mono', monospace" fill="#0369a1">Ground Dist = Map Dist × N</text>

            <text x="20" y="118" font-size="12" font-weight="700" fill="#0f172a">2. Metric Chain Rule:</text>
            <text x="20" y="136" font-size="11" fill="#475569">• 1 km = 1,000 m = 1,00,000 cm</text>
            <text x="20" y="154" font-size="11" fill="#475569">• 60,00,000 cm = 60 km</text>
            <text x="20" y="172" font-size="11" font-weight="700" fill="#059669">• 1 cm on paper = 60 km real</text>

            <text x="20" y="206" font-size="12" font-weight="700" fill="#0f172a">3. Classroom Architecture:</text>
            <text x="20" y="224" font-size="11" fill="#475569">• Scale 1 : 50</text>
            <text x="20" y="242" font-size="11" fill="#475569">• 1 cm = 50 cm = 0.5 m</text>
            <text x="20" y="260" font-size="11" fill="#475569">• 2 cm = 1.0 m</text>

            <rect x="15" y="280" width="270" height="45" rx="8" fill="#f0f9ff" stroke="#bae6fd" />
            <text x="150" y="298" text-anchor="middle" font-size="10" font-weight="700" fill="#0369a1">Crow-Flight ≠ Road Distance</text>
            <text x="150" y="314" text-anchor="middle" font-size="9" fill="#0284c7">Curved terrain adds 15–35% length</text>
          </g>
        </svg>
        <p class="svg-caption"><strong>Figure 2.2:</strong> Visual Cartography &amp; Representative Fraction (RF). 1 cm on the map converts directly to 60 km of geodesic straight-line distance, while real roads curve through geography.</p>
      </div>

      <!-- 2.3 Ratios with More than 2 Terms -->
      <div class="concept-card">
        <h3 class="concept-card-title"><i class="fa-solid fa-layer-group"></i> 2.3 Ratios with More Than 2 Terms (Multi-Term Ratios)</h3>
        <p>
          In elementary math, students examine comparisons between two items: boys to girls (<code>3 : 4</code>) or length to width (<code>16 : 9</code>). However, the real physical world compounds multiple ingredients simultaneously.
        </p>

        <h4>Viswanath's Grand Spice Mix (Sambar / Rasam Powder)</h4>
        <p>
          Viswanath invents a proprietary South Indian spice blend by grinding four distinct aromatic spices:
        </p>
        <div class="data-table-wrapper">
          <table class="data-table">
            <thead>
              <tr>
                <th>Spice Constituent</th>
                <th>Viswanath's Master Recipe</th>
                <th>Ratio Term</th>
                <th>Puneet's Halved Recipe</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>Coriander Seeds</strong> (Dhania)</td>
                <td>8 spoons</td>
                <td><strong>8</strong></td>
                <td>4 spoons (8 × 0.5)</td>
              </tr>
              <tr>
                <td><strong>Red Chillies</strong> (Lal Mirch)</td>
                <td>4 chillies</td>
                <td><strong>4</strong></td>
                <td>2 chillies (4 × 0.5)</td>
              </tr>
              <tr>
                <td><strong>Toor Dal</strong> (Pigeon Pea)</td>
                <td>2 spoons</td>
                <td><strong>2</strong></td>
                <td>1 spoon (2 × 0.5)</td>
              </tr>
              <tr>
                <td><strong>Fenugreek Seeds</strong> (Methi)</td>
                <td>1 spoon</td>
                <td><strong>1</strong></td>
                <td>0.5 spoon (1 × 0.5)</td>
              </tr>
            </tbody>
          </table>
        </div>

        <p>
          The master compounding ratio has <strong>4 terms</strong>:
        </p>
        <div class="math-block">
          Coriander : Red Chillies : Toor Dal : Fenugreek = 8 : 4 : 2 : 1
        </div>
        <p>
          Now, Puneet opens his pantry and discovers he has only <strong>2 red chillies</strong>. How can Puneet make a spice mix that preserves the identical taste, aroma, and pungency of Viswanath's blend?
        </p>
        <ul>
          <li>Puneet determines the <strong>scaling factor</strong> by comparing his available red chillies to Viswanath's:
            <div class="math-block">Scaling Factor = Puneet's Chillies / Viswanath's Chillies = 2 / 4 = 1/2 = 0.5</div>
          </li>
          <li>To preserve authentic flavor balance, <em>every single other ingredient must be scaled by the identical factor of 0.5</em>!
            <br>• Coriander seeds = <code>8 × 0.5 = 4 spoons</code>
            <br>• Toor dal = <code>2 × 0.5 = 1 spoon</code>
            <br>• Fenugreek seeds = <code>1 × 0.5 = 0.5 spoon</code>
          </li>
        </ul>
        <p>
          Puneet's resulting recipe is <code>4 : 2 : 1 : 0.5</code>. Both recipes are in perfect proportion:
        </p>
        <div class="math-block" style="background: #fefce8; border-color: #fde047; color: #854d0e; font-weight: 700;">
          8 : 4 : 2 : 1 :: 4 : 2 : 1 : 0.5
        </div>

        <div class="callout callout-def">
          <div class="callout-title"><i class="fa-solid fa-scale-balanced"></i> General Law of Multi-Term Proportion</div>
          <p>
            When two ratios containing multiple terms are proportional:
          </p>
          <div class="math-block">
            a : b : c : d :: p : q : r : s
          </div>
          <p>
            Then the corresponding terms share an invariant quotient:
          </p>
          <div class="math-block">
            a / p = b / q = c / r = d / s = k
          </div>
        </div>

        <h4>Real-World Engineering: Structural Cement Concrete</h4>
        <p>
          Cement concrete is the world's most ubiquitous engineered construction material. It is an unyielding composite synthesized from three coarse and fine aggregates: <strong>Cement</strong>, <strong>Sand</strong>, and <strong>Gravel (Stone Aggregate)</strong>.
        </p>
        <ul>
          <li>For high-strength structural members such as earthquake-resistant columns, ceiling slabs, and bridge beams (Standard Grade M20), the universal volumetric ratio is:
            <div class="math-block">Cement : Sand : Gravel = 1 : 1.5 : 3</div>
          </li>
          <li><strong>Textbook Example 2:</strong> A mason has <strong>3 bags of cement</strong>. How much sand, gravel, and total concrete will be produced?
            <br>• Cement parts = 1. Since we have 3 bags, our multiplier is <code>3 ÷ 1 = 3</code>.
            <br>• Sand required = <code>1.5 × 3 = 4.5 bags</code>.
            <br>• Gravel required = <code>3 × 3 = 9 bags</code>.
            <br>• Total concrete mixture = <code>3 + 4.5 + 9 = 16.5 bags</code>!
          </li>
        </ul>
      </div>

      <!-- SVG 4: Concrete Compounding Multi-Term Ratio Diagram -->
      <div class="svg-graphic-box">
        <svg viewBox="0 0 950 360" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg" style="font-family: 'Plus Jakarta Sans', sans-serif;">
          <defs>
            <linearGradient id="cementGrad" x1="0%" y1="0%" x2="100%" y2="100%">
              <stop offset="0%" stop-color="#94a3b8" />
              <stop offset="100%" stop-color="#64748b" />
            </linearGradient>
            <linearGradient id="sandGrad" x1="0%" y1="0%" x2="100%" y2="100%">
              <stop offset="0%" stop-color="#fde047" />
              <stop offset="100%" stop-color="#ca8a04" />
            </linearGradient>
            <linearGradient id="gravelGrad" x1="0%" y1="0%" x2="100%" y2="100%">
              <stop offset="0%" stop-color="#cbd5e1" />
              <stop offset="100%" stop-color="#475569" />
            </linearGradient>
          </defs>
          <rect width="950" height="360" fill="#f8fafc" rx="16" />

          <text x="475" y="35" text-anchor="middle" font-family="'Space Grotesk', sans-serif" font-size="18" font-weight="700" fill="#0f172a">MULTI-TERM RATIO COMPOUNDING: STRUCTURAL CONCRETE</text>
          <text x="475" y="55" text-anchor="middle" font-size="12" fill="#64748b">Cement : Sand : Gravel = 1 : 1.5 : 3 (Sum of Parts = 5.5 Units)</text>

          <!-- 1 Batch (5.5 Units) Visual Box -->
          <g transform="translate(60, 80)">
            <rect x="0" y="0" width="360" height="230" fill="#ffffff" stroke="#cbd5e1" rx="12" />
            <text x="180" y="30" text-anchor="middle" font-size="14" font-weight="700" fill="#0369a1">Single Standard Unit Batch (5.5 Units)</text>

            <!-- Stacked Blocks -->
            <!-- Cement: 1 part (width 50) -->
            <rect x="30" y="60" width="55" height="100" fill="url(#cementGrad)" rx="6" />
            <text x="57" y="115" text-anchor="middle" fill="#ffffff" font-size="11" font-weight="700">1.0</text>
            <text x="57" y="180" text-anchor="middle" font-size="11" font-weight="600" fill="#475569">Cement</text>

            <!-- Sand: 1.5 parts (width 82) -->
            <rect x="95" y="60" width="82" height="100" fill="url(#sandGrad)" rx="6" />
            <text x="136" y="115" text-anchor="middle" fill="#713f12" font-size="11" font-weight="700">1.5</text>
            <text x="136" y="180" text-anchor="middle" font-size="11" font-weight="600" fill="#713f12">Sand</text>

            <!-- Gravel: 3.0 parts (width 145) -->
            <rect x="187" y="60" width="145" height="100" fill="url(#gravelGrad)" rx="6" />
            <text x="259" y="115" text-anchor="middle" fill="#ffffff" font-size="11" font-weight="700">3.0</text>
            <text x="259" y="180" text-anchor="middle" font-size="11" font-weight="600" fill="#334155">Gravel</text>

            <rect x="30" y="200" width="302" height="18" fill="#e0f2fe" rx="4" />
            <text x="181" y="213" text-anchor="middle" font-size="10" font-weight="700" fill="#0369a1">Total Volume = 1 + 1.5 + 3 = 5.5 Units</text>
          </g>

          <!-- Scaling Arrow -->
          <g transform="translate(435, 180)">
            <line x1="0" y1="0" x2="60" y2="0" stroke="#0284c7" stroke-width="4" marker-end="url(#arrow)" />
            <text x="30" y="-12" text-anchor="middle" font-size="11" font-weight="700" fill="#0284c7">× 20 Scale</text>
            <text x="30" y="22" text-anchor="middle" font-size="10" fill="#64748b">(110 ÷ 5.5)</text>
          </g>

          <!-- Scaled Batch (110 Units) Visual Box -->
          <g transform="translate(515, 80)">
            <rect x="0" y="0" width="380" height="230" fill="#ffffff" stroke="#cbd5e1" rx="12" />
            <text x="190" y="30" text-anchor="middle" font-size="14" font-weight="700" fill="#059669">Scaled Production Batch (110 Units)</text>

            <!-- Stacked Blocks -->
            <!-- Cement: 20 units -->
            <rect x="25" y="60" width="60" height="100" fill="url(#cementGrad)" rx="6" />
            <text x="55" y="115" text-anchor="middle" fill="#ffffff" font-size="11" font-weight="700">20 u</text>
            <text x="55" y="180" text-anchor="middle" font-size="11" font-weight="600" fill="#475569">Cement</text>

            <!-- Sand: 30 units -->
            <rect x="95" y="60" width="90" height="100" fill="url(#sandGrad)" rx="6" />
            <text x="140" y="115" text-anchor="middle" fill="#713f12" font-size="11" font-weight="700">30 u</text>
            <text x="140" y="180" text-anchor="middle" font-size="11" font-weight="600" fill="#713f12">Sand</text>

            <!-- Gravel: 60 units -->
            <rect x="195" y="60" width="160" height="100" fill="url(#gravelGrad)" rx="6" />
            <text x="275" y="115" text-anchor="middle" fill="#ffffff" font-size="11" font-weight="700">60 u</text>
            <text x="275" y="180" text-anchor="middle" font-size="11" font-weight="600" fill="#334155">Gravel</text>

            <rect x="25" y="200" width="330" height="18" fill="#ecfdf5" rx="4" />
            <text x="190" y="213" text-anchor="middle" font-size="10" font-weight="700" fill="#059669">Total Concrete = 20 + 30 + 60 = 110 Units</text>
          </g>
        </svg>
        <p class="svg-caption"><strong>Figure 2.3:</strong> Proportional scaling in structural concrete formulation. Multiplying each term by the common factor of 20 expands a 5.5-unit batch into 110 units while maintaining exact structural integrity.</p>
      </div>

      <!-- 2.4 Dividing a Whole in a Given Ratio -->
      <div class="concept-card">
        <h3 class="concept-card-title"><i class="fa-solid fa-pie-chart"></i> 2.4 Dividing a Whole in a Given Multi-Term Ratio</h3>
        <p>
          A frequent challenge in engineering, commerce, estate inheritance, and geometry is partitioning a known total quantity (a "whole" <em>W</em>) into pieces governed by a multi-term ratio <code>a : b : c : ...</code>.
        </p>

        <div class="callout callout-def">
          <div class="callout-title"><i class="fa-solid fa-square-root-variable"></i> Master Partition Theorem</div>
          <p>
            When a whole quantity <em>W</em> is divided in the multi-term ratio <code>a : b : c : ...</code>:
          </p>
          <ol>
            <li>Compute the total number of parts by summing the ratio terms:
              <div class="math-block">Sum of Parts (S) = a + b + c + ...</div>
            </li>
            <li>Determine the physical magnitude of <strong>one single part</strong>:
              <div class="math-block">Value of 1 Part = W / (a + b + c + ...)</div>
            </li>
            <li>Multiply the value of one part by each individual term:
              <div class="math-block">
                Part A = W × [a / (a + b + c + ...)]<br>
                Part B = W × [b / (a + b + c + ...)]<br>
                Part C = W × [c / (a + b + c + ...)]
              </div>
            </li>
          </ol>
        </div>

        <h4>Deep-Dive Geometric Application: Triangle Angle Sum Property</h4>
        <p>
          In <strong>Example 5 (Page 60)</strong>, students are tasked with constructing a triangle whose interior angles are in the ratio <code>1 : 3 : 5</code>.
        </p>
        <ul>
          <li>We know from Euclid's Geometry that the sum of interior angles in any Euclidean triangle is strictly <strong>180°</strong>.
            <div class="math-block">∠A + ∠B + ∠C = 180°</div>
          </li>
          <li>Sum of the ratio terms = <code>1 + 3 + 5 = 9 parts</code>.</li>
          <li>Value of 1 part = <code>180° ÷ 9 = 20°</code>.</li>
          <li>Evaluating the three interior angles:
            <br>• <strong>∠A</strong> = <code>1 × 20° = 20°</code>
            <br>• <strong>∠B</strong> = <code>3 × 20° = 60°</code>
            <br>• <strong>∠C</strong> = <code>5 × 20° = 100°</code>
          </li>
          <li><em>Verification Check:</em> <code>20° + 60° + 100° = 180°</code>. Because one angle is greater than 90° (∠C = 100°), this triangle is classified as an <strong>obtuse-angled scalene triangle</strong>!</li>
        </ul>

        <h4>Geometric Fallacy: Sidelength Ratios vs. Congruence &amp; Existence</h4>
        <p>
          Questions 4 and 5 of "Figure It Out" (Page 60) explore two of the most profound conceptual traps in middle school geometry:
        </p>

        <div class="callout callout-warn">
          <div class="callout-title"><i class="fa-solid fa-triangle-exclamation"></i> Trap 1: Do Triangles with Sidelength Ratio 3 : 4 : 5 Have to Be Congruent?</div>
          <p>
            <strong>The Question:</strong> Construct a triangle with sidelengths in the ratio <code>3 : 4 : 5</code>. Will all triangles drawn with this ratio be <em>congruent</em> to each other?
          </p>
          <p>
            <strong>The Teacher's Explanation:</strong> <strong>ABSOLUTELY NOT!</strong><br>
            • Triangles with sides in the ratio <code>3 : 4 : 5</code> have sides that can measure <code>(3 cm, 4 cm, 5 cm)</code>, or <code>(6 cm, 8 cm, 10 cm)</code>, or <code>(30 cm, 40 cm, 50 cm)</code>.<br>
            • All these triangles share identical interior angles (90°, 53.13°, 36.87°). Therefore, they are <strong>SIMILAR (सଦୃଶ)</strong>.<br>
            • However, <strong>CONGRUENCE (ସର୍ବସମତା)</strong> strictly demands that corresponding sides have <em>identical physical lengths</em> (so that one triangle completely covers the other when superimposed). A triangle with sides 6, 8, 10 cm is four times larger in area than a triangle of 3, 4, 5 cm! Thus, they are similar, but NOT congruent.
          </p>
        </div>

        <div class="callout callout-warn">
          <div class="callout-title"><i class="fa-solid fa-ban"></i> Trap 2: Can You Construct a Triangle with Sidelengths in Ratio 1 : 3 : 5?</div>
          <p>
            <strong>The Question:</strong> Can you construct a triangle with sidelengths in the ratio <code>1 : 3 : 5</code>? Why or why not?
          </p>
          <p>
            <strong>The Teacher's Explanation:</strong> <strong>NO! SUCH A TRIANGLE CAN NEVER EXIST!</strong><br>
            • By the fundamental <strong>Triangle Inequality Theorem (ତ୍ରିଭୁଜର ଅସମତା ସୂତ୍ର)</strong>: <em>The sum of the lengths of any two sides of a triangle must be strictly greater than the length of the third side.</em>
          </p>
          <div class="math-block">
            Side 1 = 1x,&nbsp;&nbsp;Side 2 = 3x,&nbsp;&nbsp;Side 3 = 5x (where x > 0)<br>
            Sum of two shorter sides = 1x + 3x = 4x<br>
            Comparison: 4x &lt; 5x &nbsp;&nbsp;(The sum of the two shorter sides is LESS than the longest side!)
          </div>
          <p>
            If you try to draw this with a compass and ruler: draw a base segment of 5 cm. From one end, draw an arc of radius 1 cm; from the other end, draw an arc of radius 3 cm. Even if stretched completely flat along the base line, <code>1 cm + 3 cm = 4 cm</code>, leaving a 1 cm empty gap! The arcs will never intersect. Hence, no closed polygon can be formed.
          </p>
        </div>
      </div>

      <!-- 2.5 A Slice of the Pie: Pie Charts -->
      <div class="concept-card">
        <h3 class="concept-card-title"><i class="fa-solid fa-chart-pie"></i> 2.5 A Slice of the Pie: Pie Charts (Circle Graphs)</h3>
        <p>
          A <strong>Pie Chart</strong> (also termed a <em>Circle Graph</em> or <em>ବୃତ୍ତଲେଖ</em> in Odia) is a circular statistical graphic divided into radial slices or sectors. The arc length, central angle, and surface area of each sector are directly proportional to the quantity or frequency it represents.
        </p>

        <h4>Why Does a Circle Form the Ideal Proportional Canvas?</h4>
        <ul>
          <li>A complete geometric revolution around a central point measures exactly <strong>360°</strong>.</li>
          <li>Therefore, the entire data set (the total frequency <em>N</em> or 100%) corresponds to the complete 360° circle.</li>
          <li>Each data component occupies a central sector angle θ proportional to its share of the whole:
            <div class="math-block">
              Central Angle (θ) / 360° = Component Frequency (f) / Total Frequency (N)
            </div>
            <div class="math-block" style="background: #eff6ff; border-color: #3b82f6; color: #1e40af; font-weight: 700;">
              Central Angle (θ) = [Frequency (f) / Total Frequency (N)] × 360°
            </div>
          </li>
        </ul>

        <h4>The Textbook Assessment Grade Study (40 Students)</h4>
        <p>
          The textbook introduces pie charts through the examination results of 40 students across 5 grade categories:
        </p>
        <div class="data-table-wrapper">
          <table class="data-table">
            <thead>
              <tr>
                <th>Grade</th>
                <th>Student Count (f)</th>
                <th>Ratio Term (÷ HCF 2)</th>
                <th>Fraction of Whole (f / 40)</th>
                <th>Calculation for Central Angle (θ)</th>
                <th>Sector Central Angle (θ)</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>Grade A</strong></td>
                <td>12</td>
                <td>6</td>
                <td>12 / 40 = 3 / 10</td>
                <td>(12 / 40) × 360° = 12 × 9°</td>
                <td><strong>108°</strong></td>
              </tr>
              <tr>
                <td><strong>Grade B</strong></td>
                <td>10</td>
                <td>5</td>
                <td>10 / 40 = 1 / 4</td>
                <td>(10 / 40) × 360° = 10 × 9°</td>
                <td><strong>90°</strong> (Right Angle)</td>
              </tr>
              <tr>
                <td><strong>Grade C</strong></td>
                <td>8</td>
                <td>4</td>
                <td>8 / 40 = 1 / 5</td>
                <td>(8 / 40) × 360° = 8 × 9°</td>
                <td><strong>72°</strong></td>
              </tr>
              <tr>
                <td><strong>Grade D</strong></td>
                <td>6</td>
                <td>3</td>
                <td>6 / 40 = 3 / 20</td>
                <td>(6 / 40) × 360° = 6 × 9°</td>
                <td><strong>54°</strong></td>
              </tr>
              <tr>
                <td><strong>Grade E</strong></td>
                <td>4</td>
                <td>2</td>
                <td>4 / 40 = 1 / 10</td>
                <td>(4 / 40) × 360° = 4 × 9°</td>
                <td><strong>36°</strong></td>
              </tr>
              <tr style="background: #f8fafc; font-weight: 700;">
                <td><strong>Total</strong></td>
                <td><strong>40</strong></td>
                <td><strong>20</strong></td>
                <td><strong>40 / 40 = 1</strong></td>
                <td><strong>—</strong></td>
                <td><strong>360°</strong></td>
              </tr>
            </tbody>
          </table>
        </div>

        <div class="callout callout-hack">
          <div class="callout-title"><i class="fa-solid fa-lightbulb"></i> The HCF Simplification Trick for Pie Charts</div>
          <p>
            Notice the ratio of students: <code>12 : 10 : 8 : 6 : 4</code>.<br>
            Instead of multiplying large numbers, divide all frequencies by their <strong>Highest Common Factor (HCF = 2)</strong>:<br>
            The simplified ratio is <code>6 : 5 : 4 : 3 : 2</code>.<br>
            Sum of simplified parts = <code>6 + 5 + 4 + 3 + 2 = 20 parts</code>.<br>
            Therefore, <strong>Each 1 part = 360° ÷ 20 = 18°</strong>!<br>
            Now simply multiply each simplified term by 18°:
          </p>
          <div class="math-block">
            Grade A = 6 × 18° = 108°<br>
            Grade B = 5 × 18° = 90°<br>
            Grade C = 4 × 18° = 72°<br>
            Grade D = 3 × 18° = 54°<br>
            Grade E = 2 × 18° = 36°
          </div>
          <p>This mental math trick saves substantial time during examinations and prevents arithmetic slips!</p>
        </div>

        <h4>Step-by-Step Protractor &amp; Compass Drafting Protocol</h4>
        <ol>
          <li><strong>Step 1 (Base Circle &amp; Baseline Radius):</strong> Use a compass to draw a clean circle of convenient radius (typically 4 cm to 6 cm). Mark the centre as point <em>A</em>. Draw a horizontal radius segment <em>AB</em> to the right.</li>
          <li><strong>Step 2 (Plotting Sector 1 - Grade A):</strong> Align the baseline of your protractor on radius <em>AB</em> with the centre hole at <em>A</em>. Measure <strong>108°</strong> in an anti-clockwise direction and mark point <em>C</em> on the circumference. Connect radius <em>AC</em>.</li>
          <li><strong>Step 3 (Plotting Sector 2 - Grade B):</strong> Rotate your paper or protractor so that the protractor baseline rests on new radius <em>AC</em>. Measure <strong>90°</strong> anti-clockwise and mark point <em>D</em>. Connect radius <em>AD</em>.</li>
          <li><strong>Step 4 (Plotting Sector 3 - Grade C):</strong> Align the protractor on radius <em>AD</em>, measure <strong>72°</strong> anti-clockwise, and draw radius <em>AE</em>.</li>
          <li><strong>Step 5 (Plotting Sector 4 - Grade D):</strong> Align the protractor on radius <em>AE</em>, measure <strong>54°</strong> anti-clockwise, and draw radius <em>AF</em>.</li>
          <li><strong>Step 6 (Automatic Self-Verification - Grade E):</strong> Measure the remaining sector between radius <em>AF</em> and original baseline <em>AB</em> with your protractor. It must measure exactly <strong>36°</strong>! If it does not, a drawing error occurred in one of the earlier sectors.</li>
          <li><strong>Step 7 (Styling &amp; Identification):</strong> Colour each sector with distinctive pastel hues, write the central angle and category label inside or beside the sector, and provide a clear title and legend.</li>
        </ol>
      </div>

      <!-- SVG 5: Master Pie Chart Construction & Grade Distribution -->
      <div class="svg-graphic-box">
        <svg viewBox="0 0 950 420" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg" style="font-family: 'Plus Jakarta Sans', sans-serif;">
          <defs>
            <filter id="pieShadow">
              <feDropShadow dx="0" dy="4" stdDeviation="6" flood-opacity="0.12" />
            </filter>
          </defs>
          <rect width="950" height="420" fill="#f8fafc" rx="16" />

          <!-- Left Side: Rendered Pie Chart -->
          <g transform="translate(240, 210)" filter="url(#pieShadow)">
            <!-- Outer circle border -->
            <circle cx="0" cy="0" r="160" fill="#ffffff" stroke="#cbd5e1" stroke-width="2" />

            <!-- Slices plotted mathematically with radius 160 -->
            <!-- 
              Angles:
              Base AB at 0° (radius to (160, 0))
              Grade A: 108° (from 0° to 108°) -> cos(108°)=-0.3090, sin(108°)=0.9511 -> end (-49.44, 152.17)
              Grade B: 90° (from 108° to 198°) -> cos(198°)=-0.9511, sin(198°)=-0.3090 -> end (-152.17, -49.44)
              Grade C: 72° (from 198° to 270°) -> cos(270°)=0, sin(270°)=-1 -> end (0, -160)
              Grade D: 54° (from 270° to 324°) -> cos(324°)=0.8090, sin(324°)=-0.5878 -> end (129.44, -94.05)
              Grade E: 36° (from 324° to 360°/0°) -> end (160, 0)
              Note: SVG y-axis points DOWNWARDS!
              Let us map counter-clockwise visually:
              0° = (160, 0)
              Angle phi in SVG coords (clockwise or standard math with -y):
              Let's use clean standard SVG paths:
            -->

            <!-- Sector A: 108° (0° to 108° counter-clockwise => in SVG coords y is negative) -->
            <!-- 0°: (160, 0); 108°: (160*cos(108°), -160*sin(108°)) = (-49.4, -152.2) -->
            <path d="M 0 0 L 160 0 A 160 160 0 0 0 -49.44 -152.17 Z" fill="#0284c7" />
            <text x="60" y="-80" fill="#ffffff" font-size="14" font-weight="700">Grade A</text>
            <text x="60" y="-62" fill="#e0f2fe" font-size="12">12 sts (108°)</text>

            <!-- Sector B: 90° (108° to 198°) -> 198°: (-152.2, 49.4) in standard math, in SVG (-152.2, 49.4) -->
            <path d="M 0 0 L -49.44 -152.17 A 160 160 0 0 0 -152.17 49.44 Z" fill="#0d9488" />
            <text x="-120" y="-40" fill="#ffffff" font-size="14" font-weight="700">Grade B</text>
            <text x="-120" y="-22" fill="#ccfbf1" font-size="12">10 sts (90°)</text>

            <!-- Sector C: 72° (198° to 270°) -> 270°: (0, 160) -->
            <path d="M 0 0 L -152.17 49.44 A 160 160 0 0 0 0 160 Z" fill="#f59e0b" />
            <text x="-80" y="110" fill="#ffffff" font-size="13" font-weight="700">Grade C</text>
            <text x="-80" y="126" fill="#fef3c7" font-size="11">8 sts (72°)</text>

            <!-- Sector D: 54° (270° to 324°) -> 324°: (129.4, 94.1) -->
            <path d="M 0 0 L 0 160 A 160 160 0 0 0 129.44 94.05 Z" fill="#7c3aed" />
            <text x="35" y="130" fill="#ffffff" font-size="12" font-weight="700">Grade D</text>
            <text x="35" y="146" fill="#ede9fe" font-size="11">6 sts (54°)</text>

            <!-- Sector E: 36° (324° to 360°) -> 360°: (160, 0) -->
            <path d="M 0 0 L 129.44 94.05 A 160 160 0 0 0 160 0 Z" fill="#ef4444" />
            <text x="110" y="55" fill="#ffffff" font-size="12" font-weight="700">Grade E</text>
            <text x="110" y="70" fill="#fee2e2" font-size="10">4 sts (36°)</text>

            <!-- Center pivot point -->
            <circle cx="0" cy="0" r="5" fill="#ffffff" stroke="#0f172a" stroke-width="2" />
            <text x="-15" y="-6" font-size="12" font-weight="800" fill="#0f172a">A</text>
            <text x="168" y="5" font-size="12" font-weight="800" fill="#0f172a">B</text>
          </g>

          <!-- Right Side: Step-by-Step Construction Legend & Properties -->
          <g transform="translate(480, 30)">
            <rect x="0" y="0" width="430" height="360" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.5" rx="12" />
            <rect x="0" y="0" width="430" height="40" rx="12" fill="#0284c7" />
            <text x="215" y="25" text-anchor="middle" font-size="14" font-weight="700" fill="#ffffff">PIE CHART CONSTRUCTION FORMULAS</text>

            <!-- Table of Angle Fractions -->
            <g transform="translate(20, 60)">
              <rect x="0" y="0" width="390" height="185" fill="#f8fafc" stroke="#e2e8f0" rx="8" />
              <text x="15" y="25" font-size="12" font-weight="700" fill="#0284c7">Central Angle Formula:</text>
              <text x="15" y="45" font-size="12" font-family="'JetBrains Mono', monospace" fill="#0f172a">θ = (Frequency / Total N) × 360°</text>

              <line x1="15" y1="58" x2="375" y2="58" stroke="#cbd5e1" />
              
              <text x="15" y="80" font-size="11" fill="#0284c7">■ Grade A (12 sts):</text>
              <text x="140" y="80" font-size="11" font-family="'JetBrains Mono', monospace">(12 / 40) × 360° = 108° (30%)</text>

              <text x="15" y="102" font-size="11" fill="#0d9488">■ Grade B (10 sts):</text>
              <text x="140" y="102" font-size="11" font-family="'JetBrains Mono', monospace">(10 / 40) × 360° = 90°  (25%)</text>

              <text x="15" y="124" font-size="11" fill="#f59e0b">■ Grade C (8 sts):</text>
              <text x="140" y="124" font-size="11" font-family="'JetBrains Mono', monospace">(8 / 40) × 360° = 72°  (20%)</text>

              <text x="15" y="146" font-size="11" fill="#7c3aed">■ Grade D (6 sts):</text>
              <text x="140" y="146" font-size="11" font-family="'JetBrains Mono', monospace">(6 / 40) × 360° = 54°  (15%)</text>

              <text x="15" y="168" font-size="11" fill="#ef4444">■ Grade E (4 sts):</text>
              <text x="140" y="168" font-size="11" font-family="'JetBrains Mono', monospace">(4 / 40) × 360° = 36°  (10%)</text>
            </g>

            <!-- Verification callout box -->
            <rect x="20" y="260" width="390" height="80" fill="#ecfdf5" stroke="#10b981" rx="8" />
            <text x="35" y="282" font-size="11" font-weight="700" fill="#065f46">Crucial Verification Check:</text>
            <text x="35" y="302" font-size="11" fill="#047857">• Sum of angles = 108° + 90° + 72° + 54° + 36° = 360°</text>
            <text x="35" y="322" font-size="11" fill="#047857">• Sum of percentages = 30% + 25% + 20% + 15% + 10% = 100%</text>
          </g>
        </svg>
        <p class="svg-caption"><strong>Figure 2.4:</strong> Complete geometric construction of the 40-student assessment pie chart with sector boundaries, central angles (θ), and percentage allocations.</p>
      </div>

      <!-- 2.6 Inverse Proportions: The Reciprocal World -->
      <div class="concept-card">
        <h3 class="concept-card-title"><i class="fa-solid fa-arrows-left-right"></i> 2.6 Inverse Proportions: The Reciprocal Universe</h3>
        <p>
          In direct proportion, when one variable increases, the other variable increases at the identical rate. But consider real-life situations:
        </p>
        <ul>
          <li>If you ride your bicycle faster to school, do you take <em>more</em> time or <em>less</em> time? (Less time!)</li>
          <li>If more construction workers join a building site, will they take <em>more</em> days or <em>fewer</em> days to finish the wall? (Fewer days!)</li>
          <li>If a hostel admits 20 additional students, will the stored grain last for <em>more</em> days or <em>fewer</em> days? (Fewer days!)</li>
        </ul>
        <p>
          These scenarios represent the realm of <strong>Inverse Proportion (ବ୍ୟସ୍ତ ସମାନୁପାତ)</strong>, where quantities move in opposite directions under a strict reciprocal law!
        </p>

        <h4>The Journey from Lucknow to Kanpur (90 km Distance)</h4>
        <p>
          Puneeth's father travels between Lucknow and Kanpur, a fixed highway distance of <strong>90 km</strong>. He records his travel duration using various modes of transportation:
        </p>
        <div class="data-table-wrapper">
          <table class="data-table">
            <thead>
              <tr>
                <th>Mode of Travel</th>
                <th>Speed (x in km/h)</th>
                <th>Speed Factor vs Walking</th>
                <th>Time Taken (y in hours)</th>
                <th>Time Factor vs Walking</th>
                <th>Product (x · y = Distance)</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>Walking on Foot</strong></td>
                <td>5 km/h</td>
                <td>1× (Base)</td>
                <td>18 hours</td>
                <td>1× (Base)</td>
                <td><code>5 × 18 = 90 km</code></td>
              </tr>
              <tr>
                <td><strong>Bicycle</strong></td>
                <td>15 km/h</td>
                <td><strong>3× faster</strong> (15 ÷ 5)</td>
                <td>6 hours</td>
                <td><strong>1/3 duration</strong> (18 ÷ 3)</td>
                <td><code>15 × 6 = 90 km</code></td>
              </tr>
              <tr>
                <td><strong>Motorcycle</strong></td>
                <td>30 km/h</td>
                <td><strong>6× faster</strong> (30 ÷ 5)</td>
                <td>3 hours</td>
                <td><strong>1/6 duration</strong> (18 ÷ 6)</td>
                <td><code>30 × 3 = 90 km</code></td>
              </tr>
              <tr>
                <td><strong>Car on Highway</strong></td>
                <td>60 km/h</td>
                <td><strong>12× faster</strong> (60 ÷ 5)</td>
                <td>1.5 hours</td>
                <td><strong>1/12 duration</strong> (18 ÷ 12)</td>
                <td><code>60 × 1.5 = 90 km</code></td>
              </tr>
            </tbody>
          </table>
        </div>

        <div class="callout callout-def">
          <div class="callout-title"><i class="fa-solid fa-balance-scale"></i> Mathematical Definition: Inverse Proportion</div>
          <p>
            Two quantities <em>x</em> and <em>y</em> are said to vary in <strong>inverse proportion</strong> if there exists a relation of the type:
          </p>
          <div class="math-block">
            x · y = k &nbsp;&nbsp;(where k is a positive constant called the Constant of Inverse Variation)
          </div>
          <p>
            Equivalently, if <em>(x₁, y₁)</em> and <em>(x₂, y₂)</em> are corresponding pairs of values of the two quantities:
          </p>
          <div class="math-block">
            x₁ · y₁ = x₂ · y₂ = k
          </div>
          <p>
            Dividing both sides reveals the reciprocal ratio statement:
          </p>
          <div class="math-block">
            x₁ / x₂ = y₂ / y₁
          </div>
          <p>
            <strong>The Golden Reciprocal Law:</strong> When quantity <em>x</em> is multiplied by any factor <em>n</em>, the corresponding quantity <em>y</em> is automatically multiplied by the reciprocal factor <code>1/n</code> (divided by <em>n</em>)!
          </p>
        </div>

        <h4>Work, Time, and Worker-Days (The Product Invariant)</h4>
        <p>
          In civil work, harvesting, and manufacturing, the total quantum of work <em>W</em> required to complete an objective is measured in <strong>Worker-Days (ଶ୍ରମିକ-ଦିବସ)</strong> or <strong>Man-Hours</strong>:
        </p>
        <div class="math-block">
          Total Work (W) = Number of Workers (W) × Number of Days (D) = Constant k
        </div>
        <ul>
          <li><strong>Textbook Example 3:</strong> 20 workers take 4 days to lay a road. How many days will 10 workers take?
            <div class="math-block">
              Total Work Volume = 20 workers × 4 days = 80 worker-days.<br>
              Let d be the days for 10 workers:<br>
              10 × d = 80 ⇒ d = 80 ÷ 10 = 8 days!
            </div>
            Notice: Workers halved (20 → 10, factor of 1/2), so days doubled (4 → 8, factor of 2)!
          </li>
          <li><strong>Textbook Example 4:</strong> 2 identical pumps fill a water reservoir in 18 hours. If 2 more pumps of the same capacity are added, how long will it take?
            <div class="math-block">
              Initial Pumps = 2. Added Pumps = 2. New Total Pumps = 2 + 2 = 4 pumps!<br>
              Inverse Equation: 2 pumps × 18 hours = 4 pumps × t hours<br>
              36 = 4t ⇒ t = 36 ÷ 4 = 9 hours!
            </div>
          </li>
          <li><strong>Textbook Example 5:</strong> A boarding school has food grains for 80 students lasting 15 days. If 20 more students join, how long will the food last?
            <div class="math-block">
              Initial Students = 80. Food days = 15. Total student-days of grain = 80 × 15 = 1200.<br>
              New Student Population = 80 + 20 = 100 students.<br>
              Let d be the new number of days:<br>
              100 × d = 1200 ⇒ d = 1200 ÷ 100 = 12 days!
            </div>
          </li>
        </ul>

        <h4>The Combined Work Rate Theorem (Ram &amp; Shyam)</h4>
        <p>
          What happens when two people with <em>different working speeds</em> collaborate together on a shared task?
        </p>
        <div class="callout callout-def">
          <div class="callout-title"><i class="fa-solid fa-users-gear"></i> Theorem: Combined Work Rate via Unitary Method</div>
          <p>
            If Person A completes 1 full unit of work in <strong>t₁ hours</strong>, and Person B completes the same work in <strong>t₂ hours</strong>:
          </p>
          <ol>
            <li><strong>Rate of Person A in 1 hour</strong> = <code>1 / t₁</code> units of work.</li>
            <li><strong>Rate of Person B in 1 hour</strong> = <code>1 / t₂</code> units of work.</li>
            <li><strong>Combined Rate working together in 1 hour</strong>:
              <div class="math-block">Combined 1-Hour Work = 1 / t₁ + 1 / t₂ = (t₁ + t₂) / (t₁ · t₂)</div>
            </li>
            <li><strong>Total Time (T) needed to finish 1 complete unit of work together</strong>:
              <div class="math-block" style="background: #ecfdf5; border-color: #10b981; color: #065f46; font-weight: 700;">
                T = 1 / [Combined Rate] = (t₁ · t₂) / (t₁ + t₂)
              </div>
            </li>
          </ol>
        </div>

        <p>
          Let us verify <strong>Example 6 (Page 66-67)</strong> using this exact rigorous framework:
        </p>
        <ul>
          <li><strong>Ram's speed:</strong> Ram takes <strong>1 hour</strong> to cut a basket of vegetables. In 1 hour, Ram finishes <code>1 / 1 = 1 unit</code> of work.</li>
          <li><strong>Shyam's speed:</strong> Shyam takes <strong>1.5 hours</strong> (which is <code>3/2 hours</code>). In 1 hour, Shyam finishes:
            <div class="math-block">1 ÷ (3/2) = 2/3 unit of work.</div>
          </li>
          <li><strong>Working together for 1 hour:</strong>
            <div class="math-block">Combined Work = 1 + 2/3 = 5/3 units of work!</div>
          </li>
          <li><strong>Time needed to complete 1 unit of work:</strong>
            <div class="math-block">
              Time = 1 ÷ (5/3) = 3/5 of an hour!
            </div>
            Converting into clock minutes:
            <div class="math-block" style="background: #f0fdfa; border-color: #14b8a6; color: #0f766e; font-weight: 700;">
              Time = (3/5) × 60 minutes = 3 × 12 = 36 minutes!
            </div>
          </li>
        </ul>
      </div>

      <!-- SVG 6: Living Beings 24-Hour Sleep Clocks -->
      <div class="svg-graphic-box">
        <svg viewBox="0 0 950 480" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg" style="font-family: 'Plus Jakarta Sans', sans-serif;">
          <rect width="950" height="480" fill="#f8fafc" rx="16" />

          <text x="475" y="32" text-anchor="middle" font-family="'Space Grotesk', sans-serif" font-size="18" font-weight="700" fill="#0f172a">24-HOUR CIRCULAR SLEEP CLOCKS OF LIVING BEINGS (PAGE 67 Q4)</text>
          <text x="475" y="52" text-anchor="middle" font-size="12" fill="#64748b">Blue Sector = Hours Spent Sleeping &nbsp;|&nbsp; Yellow/Orange Sector = Hours Awake</text>

          <!-- Row 1: 4 Animals -->
          <!-- 1. Giraffe: 2.5 hrs (2.5/24 = 37.5°) -->
          <g transform="translate(130, 150)">
            <circle cx="0" cy="0" r="55" fill="#f59e0b" stroke="#cbd5e1" stroke-width="1.5" />
            <!-- 37.5° slice: from (0, -55) to (55*sin(37.5°), -55*cos(37.5°)) = (33.5, -43.6) -->
            <path d="M 0 0 L 0 -55 A 55 55 0 0 1 33.48 -43.61 Z" fill="#1e40af" />
            <circle cx="0" cy="0" r="28" fill="#ffffff" stroke="#e2e8f0" />
            <text x="0" y="4" text-anchor="middle" font-size="9" font-weight="800" fill="#1e40af">2.5 h</text>
            <text x="0" y="75" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a">1. Giraffe</text>
            <text x="0" y="90" text-anchor="middle" font-size="10" fill="#64748b">Sleep: 2.5 hrs (37.5°)</text>
          </g>

          <!-- 2. Elephant: 3.5 hrs (3.5/24 = 52.5°) -->
          <g transform="translate(360, 150)">
            <circle cx="0" cy="0" r="55" fill="#f59e0b" stroke="#cbd5e1" stroke-width="1.5" />
            <!-- 52.5° slice: (55*sin(52.5°), -55*cos(52.5°)) = (43.6, -33.5) -->
            <path d="M 0 0 L 0 -55 A 55 55 0 0 1 43.63 -33.49 Z" fill="#1e40af" />
            <circle cx="0" cy="0" r="28" fill="#ffffff" stroke="#e2e8f0" />
            <text x="0" y="4" text-anchor="middle" font-size="9" font-weight="800" fill="#1e40af">3.5 h</text>
            <text x="0" y="75" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a">2. Elephant</text>
            <text x="0" y="90" text-anchor="middle" font-size="10" fill="#64748b">Sleep: 3.5 hrs (52.5°)</text>
          </g>

          <!-- 3. Human: 8.0 hrs (8/24 = 1/3 = 120°) -->
          <g transform="translate(590, 150)">
            <circle cx="0" cy="0" r="55" fill="#f59e0b" stroke="#cbd5e1" stroke-width="1.5" />
            <!-- 120° slice: (55*sin(120°), -55*cos(120°)) = (47.63, 27.5) -->
            <path d="M 0 0 L 0 -55 A 55 55 0 0 1 47.63 27.5 Z" fill="#1e40af" />
            <circle cx="0" cy="0" r="28" fill="#ffffff" stroke="#e2e8f0" />
            <text x="0" y="4" text-anchor="middle" font-size="9" font-weight="800" fill="#1e40af">8.0 h</text>
            <text x="0" y="75" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a">3. Human</text>
            <text x="0" y="90" text-anchor="middle" font-size="10" fill="#64748b">Sleep: 8.0 hrs (120°)</text>
          </g>

          <!-- 4. Dog: 10.5 hrs (10.5/24 = 157.5°) -->
          <g transform="translate(820, 150)">
            <circle cx="0" cy="0" r="55" fill="#f59e0b" stroke="#cbd5e1" stroke-width="1.5" />
            <!-- 157.5° slice: (55*sin(157.5°), -55*cos(157.5°)) = (21.05, 50.81) -->
            <path d="M 0 0 L 0 -55 A 55 55 0 0 1 21.05 50.81 Z" fill="#1e40af" />
            <circle cx="0" cy="0" r="28" fill="#ffffff" stroke="#e2e8f0" />
            <text x="0" y="4" text-anchor="middle" font-size="9" font-weight="800" fill="#1e40af">10.5 h</text>
            <text x="0" y="75" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a">4. Dog</text>
            <text x="0" y="90" text-anchor="middle" font-size="10" fill="#64748b">Sleep: 10.5 hrs (157.5°)</text>
          </g>

          <!-- Row 2: Next 4 Animals -->
          <!-- 5. Cat: 13.0 hrs (13/24 = 195°) -->
          <g transform="translate(130, 350)">
            <circle cx="0" cy="0" r="55" fill="#f59e0b" stroke="#cbd5e1" stroke-width="1.5" />
            <!-- 195° slice (large arc flag = 1): (55*sin(195°), -55*cos(195°)) = (-14.23, 53.13) -->
            <path d="M 0 0 L 0 -55 A 55 55 0 1 1 -14.23 53.13 Z" fill="#1e40af" />
            <circle cx="0" cy="0" r="28" fill="#ffffff" stroke="#e2e8f0" />
            <text x="0" y="4" text-anchor="middle" font-size="9" font-weight="800" fill="#1e40af">13.0 h</text>
            <text x="0" y="75" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a">5. Cat</text>
            <text x="0" y="90" text-anchor="middle" font-size="10" fill="#64748b">Sleep: 13.0 hrs (195°)</text>
          </g>

          <!-- 6. Squirrel: 15.0 hrs (15/24 = 225°) -->
          <g transform="translate(360, 350)">
            <circle cx="0" cy="0" r="55" fill="#f59e0b" stroke="#cbd5e1" stroke-width="1.5" />
            <!-- 225° slice: (-38.89, 38.89) -->
            <path d="M 0 0 L 0 -55 A 55 55 0 1 1 -38.89 38.89 Z" fill="#1e40af" />
            <circle cx="0" cy="0" r="28" fill="#ffffff" stroke="#e2e8f0" />
            <text x="0" y="4" text-anchor="middle" font-size="9" font-weight="800" fill="#1e40af">15.0 h</text>
            <text x="0" y="75" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a">6. Squirrel</text>
            <text x="0" y="90" text-anchor="middle" font-size="10" fill="#64748b">Sleep: 15.0 hrs (225°)</text>
          </g>

          <!-- 7. Python / Snake: 18.0 hrs (18/24 = 3/4 = 270°) -->
          <g transform="translate(590, 350)">
            <circle cx="0" cy="0" r="55" fill="#f59e0b" stroke="#cbd5e1" stroke-width="1.5" />
            <!-- 270° slice: (-55, 0) -->
            <path d="M 0 0 L 0 -55 A 55 55 0 1 1 -55 0 Z" fill="#1e40af" />
            <circle cx="0" cy="0" r="28" fill="#ffffff" stroke="#e2e8f0" />
            <text x="0" y="4" text-anchor="middle" font-size="9" font-weight="800" fill="#1e40af">18.0 h</text>
            <text x="0" y="75" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a">7. Python</text>
            <text x="0" y="90" text-anchor="middle" font-size="10" fill="#64748b">Sleep: 18.0 hrs (270°)</text>
          </g>

          <!-- 8. Bat: 20.0 hrs (20/24 = 5/6 = 300°) -->
          <g transform="translate(820, 350)">
            <circle cx="0" cy="0" r="55" fill="#f59e0b" stroke="#cbd5e1" stroke-width="1.5" />
            <!-- 300° slice: (-47.63, -27.5) -->
            <path d="M 0 0 L 0 -55 A 55 55 0 1 1 -47.63 -27.5 Z" fill="#1e40af" />
            <circle cx="0" cy="0" r="28" fill="#ffffff" stroke="#e2e8f0" />
            <text x="0" y="4" text-anchor="middle" font-size="9" font-weight="800" fill="#1e40af">20.0 h</text>
            <text x="0" y="75" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a">8. Bat</text>
            <text x="0" y="90" text-anchor="middle" font-size="10" fill="#64748b">Sleep: 20.0 hrs (300°)</text>
          </g>
        </svg>
        <p class="svg-caption"><strong>Figure 2.5:</strong> The 8 Living Beings sleep charts from Page 67 Q4. Notice how the blue sleep sector expands as daily sleep hours increase from 2.5 hours (Giraffe) up to 20 hours (Bat).</p>
      </div>

      <!-- SVG 7: Combined Work Rate Dynamic Model -->
      <div class="svg-graphic-box">
        <svg viewBox="0 0 950 340" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg" style="font-family: 'Plus Jakarta Sans', sans-serif;">
          <defs>
            <linearGradient id="pipeGrad" x1="0%" y1="0%" x2="100%" y2="0%">
              <stop offset="0%" stop-color="#0284c7" />
              <stop offset="100%" stop-color="#38bdf8" />
            </linearGradient>
            <linearGradient id="shyamGrad" x1="0%" y1="0%" x2="100%" y2="0%">
              <stop offset="0%" stop-color="#0d9488" />
              <stop offset="100%" stop-color="#2dd4bf" />
            </linearGradient>
          </defs>
          <rect width="950" height="340" fill="#f8fafc" rx="16" />

          <text x="475" y="32" text-anchor="middle" font-family="'Space Grotesk', sans-serif" font-size="18" font-weight="700" fill="#0f172a">COMBINED WORK THEOREM: ADDING RECIPROCAL WORK RATES</text>
          <text x="475" y="52" text-anchor="middle" font-size="12" fill="#64748b">Why Rates Add Directly While Time Adds Inversely (Ram &amp; Shyam Vegetable Cutting)</text>

          <!-- Ram Pipeline -->
          <g transform="translate(60, 90)">
            <rect x="0" y="0" width="240" height="70" rx="8" fill="#ffffff" stroke="#0284c7" stroke-width="1.5" />
            <text x="15" y="25" font-size="13" font-weight="700" fill="#0369a1">Ram (Solo: 1.0 hour)</text>
            <text x="15" y="45" font-size="11" fill="#64748b">1-Hour Cutting Rate:</text>
            <text x="15" y="60" font-size="12" font-weight="700" fill="#0284c7">1.0 Unit of Work / hour</text>
            <!-- Pipe visual -->
            <rect x="240" y="20" width="80" height="30" fill="url(#pipeGrad)" />
            <polygon points="320,15 340,35 320,55" fill="#0284c7" />
          </g>

          <!-- Shyam Pipeline -->
          <g transform="translate(60, 190)">
            <rect x="0" y="0" width="240" height="70" rx="8" fill="#ffffff" stroke="#0d9488" stroke-width="1.5" />
            <text x="15" y="25" font-size="13" font-weight="700" fill="#0f766e">Shyam (Solo: 1.5 hours)</text>
            <text x="15" y="45" font-size="11" fill="#64748b">1-Hour Cutting Rate:</text>
            <text x="15" y="60" font-size="12" font-weight="700" fill="#0d9488">2/3 Unit of Work / hour</text>
            <!-- Pipe visual -->
            <rect x="240" y="20" width="80" height="30" fill="url(#shyamGrad)" />
            <polygon points="320,15 340,35 320,55" fill="#0d9488" />
          </g>

          <!-- Combined Chamber (Right) -->
          <g transform="translate(480, 80)">
            <rect x="0" y="0" width="410" height="200" rx="12" fill="#ffffff" stroke="#cbd5e1" stroke-width="2" />
            <rect x="0" y="0" width="410" height="38" rx="12" fill="#0f172a" />
            <text x="205" y="25" text-anchor="middle" font-size="13" font-weight="700" fill="#ffffff">SHARED WORK BASKET (WORKING TOGETHER)</text>

            <text x="20" y="65" font-size="12" font-weight="700" fill="#0f172a">1. Combined Cutting Speed (Rates Sum):</text>
            <text x="20" y="85" font-size="12" font-family="'JetBrains Mono', monospace" fill="#0369a1">Rate = 1 + 2/3 = 5/3 units per hour</text>

            <text x="20" y="118" font-size="12" font-weight="700" fill="#0f172a">2. Time Taken for 1 Basket (Reciprocal):</text>
            <text x="20" y="138" font-size="12" font-family="'JetBrains Mono', monospace" fill="#059669">Time = 1 ÷ (5/3) = 3/5 hour</text>

            <rect x="20" y="152" width="370" height="35" rx="6" fill="#ecfdf5" stroke="#10b981" />
            <text x="205" y="174" text-anchor="middle" font-size="12" font-weight="800" fill="#065f46">Final Result: (3/5) × 60 min = 36 Minutes!</text>
          </g>
        </svg>
        <p class="svg-caption"><strong>Figure 2.6:</strong> The Combined Work Dynamic Model. You cannot average completion times ((1 + 1.5)/2 = 1.25 hrs is false!). Instead, add reciprocal work rates (1 + 2/3 = 5/3 units/hr) and take the inverse to find the true collaborative duration (36 minutes).</p>
      </div>

      <!-- Exhaustive Bilingual Vocabulary Table -->
      <div class="concept-card">
        <h3 class="concept-card-title"><i class="fa-solid fa-language"></i> Exhaustive Bilingual Mathematical Glossary (35 Terms)</h3>
        <p>
          Master the exact mathematical lexicon required for CBSE English Medium and BSE Odisha bilingual fluency.
        </p>

        <div class="data-table-wrapper">
          <table class="data-table vocab-table">
            <thead>
              <tr>
                <th style="width: 20%;">Term / Concept</th>
                <th style="width: 12%;">Part of Speech</th>
                <th style="width: 38%;">English Mathematical Meaning</th>
                <th style="width: 30%;">ଓଡ଼ିଆ ଅର୍ଥ (Odia Meaning in Odia Script)</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>Ratio</strong></td>
                <td><em>Noun</em></td>
                <td>A quantitative comparison of two or more quantities of the same kind by division.</td>
                <td>ଅନୁପାତ (Anupata)</td>
              </tr>
              <tr>
                <td><strong>Proportion</strong></td>
                <td><em>Noun</em></td>
                <td>An equation stating that two ratios are strictly equal (a:b :: c:d).</td>
                <td>ସମାନୁପାତ (Samanupata)</td>
              </tr>
              <tr>
                <td><strong>Direct Proportion</strong></td>
                <td><em>Noun phrase</em></td>
                <td>Variation where two quantities increase or decrease by the same multiplying factor (x/y = k).</td>
                <td>ପ୍ରତ୍ୟକ୍ଷ ସମାନୁପାତ / ସରଳ ସମାନୁପାତ</td>
              </tr>
              <tr>
                <td><strong>Inverse Proportion</strong></td>
                <td><em>Noun phrase</em></td>
                <td>Variation where an increase in one quantity produces a proportional reciprocal decrease in the other (xy = k).</td>
                <td>ବ୍ୟସ୍ତ ସମାନୁପାତ (Byasta Samanupata)</td>
              </tr>
              <tr>
                <td><strong>Representative Fraction (RF)</strong></td>
                <td><em>Noun phrase</em></td>
                <td>The dimensionless scale ratio of a distance measured on a map to the corresponding ground distance.</td>
                <td>ପ୍ରତିନିଧିମୂଳକ ଭଗ୍ନାଂଶ (Pratinidhimulaka Bhagnansa)</td>
              </tr>
              <tr>
                <td><strong>Map Scale</strong></td>
                <td><em>Noun phrase</em></td>
                <td>The calibrated mathematical ratio representing real earth distances on a drafted paper map.</td>
                <td>ମାପଦଣ୍ଡ / ମାନଚିତ୍ର ସ୍କେଲ</td>
              </tr>
              <tr>
                <td><strong>Map Distance</strong></td>
                <td><em>Noun phrase</em></td>
                <td>The physical distance measured with a ruler between two map points.</td>
                <td>ମାନଚିତ୍ର ଦୂରତା (Manachitra Durata)</td>
              </tr>
              <tr>
                <td><strong>Ground Distance</strong></td>
                <td><em>Noun phrase</em></td>
                <td>The actual physical distance between two geographical locations on the Earth's surface.</td>
                <td>ଭୂମିର ପ୍ରକୃତ ଦୂରତା (Bhumira Prakruta Durata)</td>
              </tr>
              <tr>
                <td><strong>Straight-Line Distance</strong></td>
                <td><em>Noun phrase</em></td>
                <td>The direct geodesic crow-flight path between two points ignoring surface obstacles.</td>
                <td>ସରଳରୈଖିକ ଦୂରତା / ବିହଙ୍ଗମ ଦୂରତା</td>
              </tr>
              <tr>
                <td><strong>Road Distance</strong></td>
                <td><em>Noun phrase</em></td>
                <td>The actual mileage traversed along highways, curves, and topography.</td>
                <td>ସଡ଼କ ଦୂରତା / ଯାତ୍ରା ପଥର ଦୂରତା</td>
              </tr>
              <tr>
                <td><strong>Multi-Term Ratio</strong></td>
                <td><em>Noun phrase</em></td>
                <td>A combined ratio connecting three or more simultaneous terms (a : b : c : d).</td>
                <td>ବହୁ-ପଦ ବିଶିଷ୍ଟ ଅନୁପାତ</td>
              </tr>
              <tr>
                <td><strong>Scaling Factor</strong></td>
                <td><em>Noun phrase</em></td>
                <td>The multiplying multiplier used to dilate or contract every term in a ratio uniformly.</td>
                <td>ମାପକ ଗୁଣାଙ୍କ / ସାଧାରଣ ଗୁଣକ</td>
              </tr>
              <tr>
                <td><strong>Antecedent</strong></td>
                <td><em>Noun</em></td>
                <td>The first or leading term in a ratio comparison.</td>
                <td>ପୂର୍ବପଦ (Purbapada)</td>
              </tr>
              <tr>
                <td><strong>Consequent</strong></td>
                <td><em>Noun</em></td>
                <td>The second or trailing term in a ratio comparison.</td>
                <td>ଉତ୍ତରପଦ (Uttaripada)</td>
              </tr>
              <tr>
                <td><strong>Extremes</strong></td>
                <td><em>Noun</em></td>
                <td>The first and fourth terms (a and d) in a four-term proportion statement.</td>
                <td>ପ୍ରାନ୍ତରାଶି (Prantarasi)</td>
              </tr>
              <tr>
                <td><strong>Means</strong></td>
                <td><em>Noun</em></td>
                <td>The middle terms (b and c) in a four-term proportion statement.</td>
                <td>ମଧ୍ୟରାଶି (Madhyarasi)</td>
              </tr>
              <tr>
                <td><strong>Cross-Multiplication</strong></td>
                <td><em>Noun</em></td>
                <td>The algebraic method multiplying extremes and means to test proportionality (a·d = b·c).</td>
                <td>ବଜ୍ର-ଗୁଣନ (Bajra-gunana)</td>
              </tr>
              <tr>
                <td><strong>Product of Extremes</strong></td>
                <td><em>Noun phrase</em></td>
                <td>The multiplication result of the outermost terms in a proportion.</td>
                <td>ପ୍ରାନ୍ତରାଶିଦ୍ୱୟର ଗୁଣଫଳ</td>
              </tr>
              <tr>
                <td><strong>Product of Means</strong></td>
                <td><em>Noun phrase</em></td>
                <td>The multiplication result of the innermost terms in a proportion.</td>
                <td>ମଧ୍ୟରାଶିଦ୍ୱୟର ଗୁଣଫଳ</td>
              </tr>
              <tr>
                <td><strong>Pie Chart</strong></td>
                <td><em>Noun phrase</em></td>
                <td>A circular statistical graphic whose sectors represent proportionate data shares.</td>
                <td>ବୃତ୍ତଲେଖ / ପାଇ ଚାର୍ଟ (Bruttalekha)</td>
              </tr>
              <tr>
                <td><strong>Circle Graph</strong></td>
                <td><em>Noun phrase</em></td>
                <td>Synonym for pie chart, dividing a 360° disc into frequency-proportional sectors.</td>
                <td>ବୃତ୍ତାକାର ଲେଖଚିତ୍ର (Bruttakara Lekhachitra)</td>
              </tr>
              <tr>
                <td><strong>Central Angle</strong></td>
                <td><em>Noun phrase</em></td>
                <td>The angle subtended at the centre of a circle by the bounding radii of a sector (θ).</td>
                <td>କେନ୍ଦ୍ରସ୍ଥ କୋଣ (Kendrastha Kona)</td>
              </tr>
              <tr>
                <td><strong>Sector</strong></td>
                <td><em>Noun</em></td>
                <td>The pie-shaped region of a circle enclosed between two radii and their connecting arc.</td>
                <td>ବୃତ୍ତକଳା (Bruttakala)</td>
              </tr>
              <tr>
                <td><strong>Frequency</strong></td>
                <td><em>Noun</em></td>
                <td>The number of times a particular observation, grade, or event occurs in a data set.</td>
                <td>ବାରମ୍ବାରତା (Barambarata)</td>
              </tr>
              <tr>
                <td><strong>Total Frequency</strong></td>
                <td><em>Noun phrase</em></td>
                <td>The cumulative summation of all individual frequencies in a survey or study (N).</td>
                <td>ମୋଟ ବାରମ୍ବାରତା (Mota Barambarata)</td>
              </tr>
              <tr>
                <td><strong>Constant of Variation</strong></td>
                <td><em>Noun phrase</em></td>
                <td>The invariant numerical value (k) maintained across proportional relationships.</td>
                <td>ପରିବର୍ତ୍ତନର ସ୍ଥିରାଙ୍କ (Paribartanara Sthiranka)</td>
              </tr>
              <tr>
                <td><strong>Rectangular Hyperbola</strong></td>
                <td><em>Noun phrase</em></td>
                <td>The symmetric smooth curve representing inverse variation (xy = k) on a cartesian plane.</td>
                <td>ଆୟତାକାର ପରାବଳୟ (Ayatakara Parabalaya)</td>
              </tr>
              <tr>
                <td><strong>Reciprocal</strong></td>
                <td><em>Noun</em></td>
                <td>The multiplicative inverse of a number x, equal to 1/x (where x ≠ 0).</td>
                <td>ବ୍ୟୁତ୍କ୍ରମ / ଗୁଣନାତ୍ମକ ବିଲୋମୀ (Byutkrama)</td>
              </tr>
              <tr>
                <td><strong>Rate of Work</strong></td>
                <td><em>Noun phrase</em></td>
                <td>The fractional portion of a task accomplished by an agent in one unit of time.</td>
                <td>କାର୍ଯ୍ୟର ହାର (Karjyyara Hara)</td>
              </tr>
              <tr>
                <td><strong>Worker-Days (Man-Days)</strong></td>
                <td><em>Noun phrase</em></td>
                <td>The compound unit multiplying the number of workers by days worked to quantify total labour.</td>
                <td>ଶ୍ରମିକ-ଦିବସ (Sramika-dibasa)</td>
              </tr>
              <tr>
                <td><strong>Congruence</strong></td>
                <td><em>Noun</em></td>
                <td>The geometric property where figures possess identically equal size and shape.</td>
                <td>ସର୍ବସମତା (Sarbasamata)</td>
              </tr>
              <tr>
                <td><strong>Similarity</strong></td>
                <td><em>Noun</em></td>
                <td>The geometric property where figures have identical shape and angle ratios, but different sizes.</td>
                <td>ସାଦୃଶ୍ୟ (Sadrusya)</td>
              </tr>
              <tr>
                <td><strong>Triangle Inequality</strong></td>
                <td><em>Noun phrase</em></td>
                <td>The fundamental theorem dictating that the sum of any two triangle sides must exceed the third.</td>
                <td>ତ୍ରିଭୁଜର ଅସମତା ସୂତ୍ର</td>
              </tr>
              <tr>
                <td><strong>Unitary Method</strong></td>
                <td><em>Noun phrase</em></td>
                <td>The technique of solving proportional problems by first evaluating the value of a single unit.</td>
                <td>ଐକିକ ନିୟମ (Aikika Niyama)</td>
              </tr>
              <tr>
                <td><strong>Whole</strong></td>
                <td><em>Noun</em></td>
                <td>The complete, unbroken entity or total collection being partitioned into proportional shares.</td>
                <td>ସମଗ୍ର / ସମ୍ପୂର୍ଣ୍ଣ ଅଂଶ</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </section>
"""
