# -*- coding: utf-8 -*-
"""
Module: ch2_section1.py
Contains Section 1: Visual Blueprint & Detailed Mind Map
Includes SVG 1 (Exponential Paper-Folding Curve vs Linear Space Ladder)
and SVG 2 (Architectural Mind Map of Power Play).
"""

def get_section_1():
    return """
    <!-- ========================================== -->
    <!-- SECTION 1: VISUAL BLUEPRINT & MIND MAP -->
    <!-- ========================================== -->
    <section id="section-1" class="study-section">
      <div class="section-header">
        <span class="section-badge"><i class="fa-solid fa-map"></i> Pedagogical Architecture</span>
        <h2 class="section-title">Visual Blueprint & Detailed Conceptual Mind Map</h2>
        <p class="section-subtitle">
          Before diving into algebraic manipulations, examine how the entire landscape of "Power Play" is constructed. From humble paper folds that leap across cosmic distances to the strict symmetrical laws of exponents and scientific notation.
        </p>
      </div>

      <!-- Conceptual Overview -->
      <div class="callout callout-def">
        <div class="callout-title"><i class="fa-solid fa-lightbulb"></i> The Big Idea: Multiplicative vs Additive Growth</div>
        <p>
          In normal everyday arithmetic, we grow quantities by <strong>adding</strong> (e.g., saving ₹10 every day gives ₹10, ₹20, ₹30... this is <em>linear growth</em>). But in <strong>exponential growth</strong>, quantities grow by <strong>multiplying</strong> over and over (e.g., doubling: 1, 2, 4, 8, 16, 32...). While linear growth climbs like a gentle staircase, exponential growth starts slowly and then erupts like a rocket into the stratosphere!
        </p>
      </div>

      <!-- SVG Diagram 1: Exponential vs Linear Growth -->
      <div class="diagram-wrapper">
        <h3 class="subtopic-title" style="margin-top:0;">Diagram 1.1: The Space Ladder Paradox — Exponential Doubling vs Linear Steps</h3>
        <svg class="responsive-svg" viewBox="0 0 860 420" xmlns="http://www.w3.org/2000/svg">
          <defs>
            <linearGradient id="bgGrad" x1="0" y1="0" x2="1" y2="1">
              <stop offset="0%" stop-color="#0f172a"/>
              <stop offset="100%" stop-color="#1e293b"/>
            </linearGradient>
            <linearGradient id="expCurveGrad" x1="0" y1="1" x2="1" y2="0">
              <stop offset="0%" stop-color="#38bdf8"/>
              <stop offset="70%" stop-color="#818cf8"/>
              <stop offset="100%" stop-color="#f43f5e"/>
            </linearGradient>
            <linearGradient id="linearGrad" x1="0" y1="1" x2="1" y2="0">
              <stop offset="0%" stop-color="#f59e0b"/>
              <stop offset="100%" stop-color="#fbbf24"/>
            </linearGradient>
            <filter id="glowEffect" x="-20%" y="-20%" width="140%" height="140%">
              <feGaussianBlur stdDeviation="3" result="blur"/>
              <feComposite in="SourceGraphic" in2="blur" operator="over"/>
            </filter>
          </defs>

          <!-- Background Canvas -->
          <rect x="0" y="0" width="860" height="420" rx="16" fill="url(#bgGrad)"/>

          <!-- Grid Lines (Log-style representation) -->
          <g stroke="rgba(255,255,255,0.08)" stroke-width="1">
            <line x1="80" y1="80" x2="800" y2="80"/>
            <line x1="80" y1="140" x2="800" y2="140"/>
            <line x1="80" y1="200" x2="800" y2="200"/>
            <line x1="80" y1="260" x2="800" y2="260"/>
            <line x1="80" y1="320" x2="800" y2="320"/>
          </g>

          <!-- Axes -->
          <line x1="80" y1="350" x2="800" y2="350" stroke="#94a3b8" stroke-width="2"/>
          <line x1="80" y1="50" x2="80" y2="350" stroke="#94a3b8" stroke-width="2"/>

          <!-- Y-Axis Labels -->
          <text x="70" y="354" fill="#94a3b8" font-family="'JetBrains Mono'" font-size="11" text-anchor="end">0.001 cm (Fold 0)</text>
          <text x="70" y="324" fill="#94a3b8" font-family="'JetBrains Mono'" font-size="11" text-anchor="end">1.024 cm (Fold 10)</text>
          <text x="70" y="264" fill="#94a3b8" font-family="'JetBrains Mono'" font-size="11" text-anchor="end">671 m - Burj Khalifa (Fold 26)</text>
          <text x="70" y="204" fill="#94a3b8" font-family="'JetBrains Mono'" font-size="11" text-anchor="end">10.7 km - Jet Flight (Fold 30)</text>
          <text x="70" y="90" fill="#f43f5e" font-family="'Space Grotesk'" font-weight="700" font-size="12" text-anchor="end">3,84,400 km - MOON!</text>

          <!-- X-Axis Labels (Folds) -->
          <text x="80" y="375" fill="#cbd5e1" font-family="'Space Grotesk'" font-size="12" text-anchor="middle">0</text>
          <text x="220" y="375" fill="#cbd5e1" font-family="'Space Grotesk'" font-size="12" text-anchor="middle">10 Folds</text>
          <text x="360" y="375" fill="#cbd5e1" font-family="'Space Grotesk'" font-size="12" text-anchor="middle">20 Folds</text>
          <text x="500" y="375" fill="#cbd5e1" font-family="'Space Grotesk'" font-size="12" text-anchor="middle">30 Folds</text>
          <text x="640" y="375" fill="#cbd5e1" font-family="'Space Grotesk'" font-size="12" text-anchor="middle">40 Folds</text>
          <text x="740" y="375" fill="#f43f5e" font-family="'Space Grotesk'" font-weight="700" font-size="13" text-anchor="middle">46 Folds</text>
          <text x="440" y="402" fill="#94a3b8" font-family="'Space Grotesk'" font-weight="600" font-size="13" text-anchor="middle">Number of Paper Folds (Multiplicative Doubling: ×2)</text>

          <!-- Linear Growth Curve (Flat yellow staircase) -->
          <path d="M 80 349 L 780 338" stroke="url(#linearGrad)" stroke-width="3" stroke-dasharray="6,4" fill="none"/>
          <text x="600" y="330" fill="#fbbf24" font-family="'Space Grotesk'" font-weight="600" font-size="12">Linear Ladder (+20 cm per step): Needs 1.92 Billion Steps!</text>

          <!-- Exponential Curve (Sweeping exponential blast) -->
          <path d="M 80 350 Q 420 348 560 300 T 700 160 T 740 70" stroke="url(#expCurveGrad)" stroke-width="5" fill="none" filter="url(#glowEffect)"/>

          <!-- Target Moon Line -->
          <line x1="80" y1="85" x2="740" y2="85" stroke="#f43f5e" stroke-width="2" stroke-dasharray="4,4"/>

          <!-- Pins & Callouts -->
          <!-- Pin 1: Fold 10 -->
          <circle cx="220" cy="348" r="5" fill="#38bdf8"/>
          <text x="225" y="338" fill="#38bdf8" font-family="'Plus Jakarta Sans'" font-size="10" font-weight="600">1.024 cm</text>

          <!-- Pin 2: Fold 26 -->
          <circle cx="440" cy="342" r="5" fill="#818cf8"/>
          <text x="445" y="332" fill="#818cf8" font-family="'Plus Jakarta Sans'" font-size="10" font-weight="600">671 m (Burj Khalifa: 830 m)</text>

          <!-- Pin 3: Fold 30 -->
          <circle cx="500" cy="330" r="5" fill="#c084fc"/>
          <text x="505" y="318" fill="#c084fc" font-family="'Plus Jakarta Sans'" font-size="10" font-weight="600">10.7 km (Airplanes Cruise)</text>

          <!-- Pin 4: Fold 46 (Moon) -->
          <circle cx="740" cy="85" r="8" fill="#f43f5e" filter="url(#glowEffect)"/>
          <circle cx="740" cy="85" r="4" fill="#ffffff"/>

          <!-- Moon Icon & Label -->
          <g transform="translate(745, 45)">
            <rect x="0" y="0" width="105" height="52" rx="8" fill="rgba(244, 63, 94, 0.25)" stroke="#f43f5e" stroke-width="1.5"/>
            <text x="10" y="20" fill="#ffffff" font-family="'Space Grotesk'" font-weight="700" font-size="12">Fold 46 Peak</text>
            <text x="10" y="35" fill="#fecdd3" font-family="'JetBrains Mono'" font-size="10">7,03,687 km</text>
            <text x="10" y="47" fill="#cbd5e1" font-family="'Plus Jakarta Sans'" font-size="9">(Moon: 3.84 × 10⁵ km)</text>
          </g>
        </svg>
        <div class="diagram-caption">
          <strong>Figure 1.1:</strong> The exponential curve demonstrates why doubling 46 times spans over 700,000 kilometres, whereas additive linear steps (like building a ladder 20 cm at a time) require nearly 200 crore steps to cover the same distance.
        </div>
      </div>

      <!-- SVG Diagram 2: Architectural Mind Map -->
      <div class="diagram-wrapper">
        <h3 class="subtopic-title" style="margin-top:0;">Diagram 1.2: Complete Architectural Mind Map of Chapter 2 (Power Play)</h3>
        <svg class="responsive-svg" viewBox="0 0 920 540" xmlns="http://www.w3.org/2000/svg">
          <defs>
            <linearGradient id="hubGrad" x1="0" y1="0" x2="1" y2="1">
              <stop offset="0%" stop-color="#0284c7"/>
              <stop offset="100%" stop-color="#0369a1"/>
            </linearGradient>
            <filter id="cardShadow" x="-10%" y="-10%" width="120%" height="120%">
              <feDropShadow dx="0" dy="4" stdDeviation="6" flood-color="#000000" flood-opacity="0.08"/>
            </filter>
          </defs>

          <!-- Connecting Curved Lines from Central Hub -->
          <g stroke="#cbd5e1" stroke-width="2.5" fill="none">
            <!-- To Branch 1 (Top Left) -->
            <path d="M 460 270 C 400 160, 260 120, 190 100"/>
            <!-- To Branch 2 (Top Right) -->
            <path d="M 460 270 C 520 160, 660 120, 730 100"/>
            <!-- To Branch 3 (Middle Right) -->
            <path d="M 460 270 C 580 270, 680 260, 740 260"/>
            <!-- To Branch 4 (Bottom Right) -->
            <path d="M 460 270 C 530 380, 670 420, 730 440"/>
            <!-- To Branch 5 (Bottom Left) -->
            <path d="M 460 270 C 390 380, 250 420, 190 440"/>
            <!-- To Branch 6 (Middle Left) -->
            <path d="M 460 270 C 340 270, 240 260, 180 260"/>
          </g>

          <!-- Central Hub -->
          <g transform="translate(370, 220)">
            <rect x="0" y="0" width="180" height="100" rx="20" fill="url(#hubGrad)" filter="url(#cardShadow)"/>
            <text x="90" y="42" fill="#ffffff" font-family="'Space Grotesk'" font-weight="800" font-size="17" text-anchor="middle">POWER PLAY</text>
            <text x="90" y="64" fill="#e0f2fe" font-family="'JetBrains Mono'" font-weight="700" font-size="14" text-anchor="middle">aᵇ = a × a × ...</text>
            <text x="90" y="82" fill="#bae6fd" font-family="'Plus Jakarta Sans'" font-size="11" text-anchor="middle">NCERT Code: hegp102</text>
          </g>

          <!-- Branch 1: Experiencing Growth (Top Left) -->
          <g transform="translate(40, 45)" filter="url(#cardShadow)">
            <rect x="0" y="0" width="260" height="95" rx="14" fill="#f0f9ff" stroke="#0284c7" stroke-width="1.5"/>
            <text x="15" y="26" fill="#0369a1" font-family="'Space Grotesk'" font-weight="700" font-size="13">1. Multiplicative Growth</text>
            <text x="15" y="46" fill="#334155" font-family="'Plus Jakarta Sans'" font-size="11.5">• Paper Folding Doubling (2ⁿ)</text>
            <text x="15" y="64" fill="#334155" font-family="'Plus Jakarta Sans'" font-size="11.5">• 46 Folds reach beyond the Moon</text>
            <text x="15" y="82" fill="#334155" font-family="'Plus Jakarta Sans'" font-size="11.5">• Multiplicative (×2) vs Linear (+d)</text>
          </g>

          <!-- Branch 2: Laws of Exponents (Top Right) -->
          <g transform="translate(620, 45)" filter="url(#cardShadow)">
            <rect x="0" y="0" width="260" height="95" rx="14" fill="#f0fdfa" stroke="#0d9488" stroke-width="1.5"/>
            <text x="15" y="26" fill="#0f766e" font-family="'Space Grotesk'" font-weight="700" font-size="13">2. The 7 Exponent Laws</text>
            <text x="15" y="46" fill="#334155" font-family="'Plus Jakarta Sans'" font-size="11.5">• Product: aᵐ × aⁿ = aᵐ⁺ⁿ</text>
            <text x="15" y="64" fill="#334155" font-family="'Plus Jakarta Sans'" font-size="11.5">• Quotient: aᵐ ÷ aⁿ = aᵐ⁻ⁿ</text>
            <text x="15" y="82" fill="#334155" font-family="'Plus Jakarta Sans'" font-size="11.5">• Power of Power: (aᵐ)ⁿ = aᵐⁿ</text>
          </g>

          <!-- Branch 3: Combinatorics & Locks (Middle Right) -->
          <g transform="translate(630, 210)" filter="url(#cardShadow)">
            <rect x="0" y="0" width="260" height="95" rx="14" fill="#fffbeb" stroke="#f59e0b" stroke-width="1.5"/>
            <text x="15" y="26" fill="#b45309" font-family="'Space Grotesk'" font-weight="700" font-size="13">3. Combinations & Passcodes</text>
            <text x="15" y="46" fill="#334155" font-family="'Plus Jakarta Sans'" font-size="11.5">• Counting Principle (m × n)</text>
            <text x="15" y="64" fill="#334155" font-family="'Plus Jakarta Sans'" font-size="11.5">• 5-Digit PIN: 10⁵ = 1,00,000</text>
            <text x="15" y="82" fill="#334155" font-family="'Plus Jakarta Sans'" font-size="11.5">• 6-Letter Lock: 26⁶ = 3.08 × 10⁸</text>
          </g>

          <!-- Branch 4: Scientific Notation (Bottom Right) -->
          <g transform="translate(620, 395)" filter="url(#cardShadow)">
            <rect x="0" y="0" width="260" height="95" rx="14" fill="#eff6ff" stroke="#3b82f6" stroke-width="1.5"/>
            <text x="15" y="26" fill="#1d4ed8" font-family="'Space Grotesk'" font-weight="700" font-size="13">4. Powers of 10 & Standard Form</text>
            <text x="15" y="46" fill="#334155" font-family="'Plus Jakarta Sans'" font-size="11.5">• Standard Form: m × 10ᵏ (1 ≤ m &lt; 10)</text>
            <text x="15" y="64" fill="#334155" font-family="'Plus Jakarta Sans'" font-size="11.5">• Decimal Expansion (Positive & Negative)</text>
            <text x="15" y="82" fill="#334155" font-family="'Plus Jakarta Sans'" font-size="11.5">• Celestial Distances & Micro-scales</text>
          </g>

          <!-- Branch 5: Zero & Negative Dimensions (Bottom Left) -->
          <g transform="translate(40, 395)" filter="url(#cardShadow)">
            <rect x="0" y="0" width="260" height="95" rx="14" fill="#f5f3ff" stroke="#7c3aed" stroke-width="1.5"/>
            <text x="15" y="26" fill="#6d28d9" font-family="'Space Grotesk'" font-weight="700" font-size="13">5. Zero & Negative Exponents</text>
            <text x="15" y="46" fill="#334155" font-family="'Plus Jakarta Sans'" font-size="11.5">• Zero Power: a⁰ = 1 (for a ≠ 0)</text>
            <text x="15" y="64" fill="#334155" font-family="'Plus Jakarta Sans'" font-size="11.5">• Negative Power: a⁻ⁿ = 1 / aⁿ</text>
            <text x="15" y="82" fill="#334155" font-family="'Plus Jakarta Sans'" font-size="11.5">• Bidirectional Power Lines (Base 4 & 7)</text>
          </g>

          <!-- Branch 6: Orders of Magnitude & History (Middle Left) -->
          <g transform="translate(30, 210)" filter="url(#cardShadow)">
            <rect x="0" y="0" width="260" height="95" rx="14" fill="#fdf2f8" stroke="#db2777" stroke-width="1.5"/>
            <text x="15" y="26" fill="#9d174d" font-family="'Space Grotesk'" font-weight="700" font-size="13">6. Orders of Magnitude & History</text>
            <text x="15" y="46" fill="#334155" font-family="'Plus Jakarta Sans'" font-size="11.5">• Time in Seconds (10⁰ to 10¹⁸ s)</text>
            <text x="15" y="64" fill="#334155" font-family="'Plus Jakarta Sans'" font-size="11.5">• Global Populations (Humans vs Ants)</text>
            <text x="15" y="82" fill="#334155" font-family="'Plus Jakarta Sans'" font-size="11.5">• Lalitavistara & Tallakkhana (10⁵³)</text>
          </g>
        </svg>
        <div class="diagram-caption">
          <strong>Figure 1.2:</strong> Comprehensive visual blueprint showing the six interconnected thematic pillars of NCERT Chapter 2.
        </div>
      </div>

      <!-- Pedagogical Concept Breakdown Cards -->
      <div class="card-grid">
        <div class="concept-card">
          <div class="card-icon"><i class="fa-solid fa-seedling"></i></div>
          <div class="card-title">Multiplication as Repeated Addition</div>
          <div class="card-text">
            In Grade 3 and 4, we learned that adding 5 three times is <span class="math-font">5 + 5 + 5 = 5 × 3 = 15</span>. Exponents take this one level higher: multiplying 5 three times is <span class="math-font">5 × 5 × 5 = 5³ = 125</span>. Exponentiation is <em>repeated multiplication</em>!
          </div>
        </div>

        <div class="concept-card">
          <div class="card-icon"><i class="fa-solid fa-rocket"></i></div>
          <div class="card-title">The Power of the Base</div>
          <div class="card-text">
            In the expression <span class="math-font">bⁿ</span>, the base <strong>b</strong> is the actual quantity that is repeating, while the exponent <strong>n</strong> acts like an instruction counter commanding: <em>"Multiply this base by itself exactly n times!"</em>
          </div>
        </div>

        <div class="concept-card">
          <div class="card-icon"><i class="fa-solid fa-arrows-split-up-and-left"></i></div>
          <div class="card-title">The Inversion Principle</div>
          <div class="card-text">
            A positive exponent means multiplying repeatedly: <span class="math-font">2³ = 1 × 2 × 2 × 2 = 8</span>. A negative exponent does the exact inverse — it commands repeated division: <span class="math-font">2⁻³ = 1 ÷ (2 × 2 × 2) = 1/8</span>.
          </div>
        </div>
      </div>
    </section>
"""
