# -*- coding: utf-8 -*-
"""
Module: ch8_section1.py
Contains Section 1: Visual Blueprint & Detailed Mind Map, featuring three intricate,
responsive inline SVG diagrams:
1. The FDP Rosetta Stone (Fractions, Decimals, Percentages transformation cycle)
2. The Dual-Scale Benchmark Number Line & Proportional Bar Model (0% to 250%)
3. The Divergence of Simple vs Compound Interest Exponential Growth Curves
"""

def get_section1():
    return """
    <!-- ========================================== -->
    <!-- SECTION 1: VISUAL BLUEPRINT & MIND MAP    -->
    <!-- ========================================== -->
    <section id="section1">
      <div class="section-header">
        <div class="section-tag"><i class="fa-solid fa-sitemap"></i> Curricular Architecture</div>
        <h2 class="section-title">Section 1: Visual Blueprint &amp; Detailed Mind Map</h2>
        <p class="section-desc">
          Percentages are simply fractions wearing a festive mask! By fixing the denominator to 100, we unlock universal comparability across unequal quantities, rapid mental estimation, commercial trade mechanics, and exponential financial growth models.
        </p>
      </div>

      <!-- INTRICATE SVG 1: THE FDP ROSETTA STONE -->
      <div class="svg-container">
        <h4 style="margin-bottom: 0.5rem; color: #1e1b4b; font-family: 'Space Grotesk', sans-serif;"><i class="fa-solid fa-arrows-spin"></i> SVG Diagram 1: The FDP Conversion Trinity (Fractions ↔ Decimals ↔ Percentages)</h4>
        <svg viewBox="0 0 960 480" xmlns="http://www.w3.org/2000/svg" style="background: #f8fafc; border-radius: 16px;">
          <defs>
            <linearGradient id="indigoGrad" x1="0%" y1="0%" x2="100%" y2="100%">
              <stop offset="0%" stop-color="#4f46e5" />
              <stop offset="100%" stop-color="#312e81" />
            </linearGradient>
            <linearGradient id="tealGrad" x1="0%" y1="0%" x2="100%" y2="100%">
              <stop offset="0%" stop-color="#0d9488" />
              <stop offset="100%" stop-color="#115e59" />
            </linearGradient>
            <linearGradient id="amberGrad" x1="0%" y1="0%" x2="100%" y2="100%">
              <stop offset="0%" stop-color="#f59e0b" />
              <stop offset="100%" stop-color="#b45309" />
            </linearGradient>
            <filter id="shadowDrop" x="-10%" y="-10%" width="120%" height="120%">
              <feDropShadow dx="0" dy="4" stdDeviation="6" flood-color="#0f172a" flood-opacity="0.12"/>
            </filter>
            <marker id="arrowIndigo" markerWidth="10" markerHeight="10" refX="6" refY="3" orient="auto">
              <path d="M0,0 L0,6 L9,3 z" fill="#4f46e5" />
            </marker>
            <marker id="arrowTeal" markerWidth="10" markerHeight="10" refX="6" refY="3" orient="auto">
              <path d="M0,0 L0,6 L9,3 z" fill="#0d9488" />
            </marker>
            <marker id="arrowAmber" markerWidth="10" markerHeight="10" refX="6" refY="3" orient="auto">
              <path d="M0,0 L0,6 L9,3 z" fill="#d97706" />
            </marker>
          </defs>

          <!-- Outer Decorative Frame -->
          <rect x="15" y="15" width="930" height="450" rx="16" fill="#ffffff" stroke="#e2e8f0" stroke-width="2"/>

          <!-- Connecting Curved Flow Paths -->
          <!-- Fraction to Decimal -->
          <path d="M 330 140 C 420 80, 540 80, 630 140" fill="none" stroke="#4f46e5" stroke-width="3" stroke-dasharray="6,4" marker-end="url(#arrowIndigo)"/>
          <!-- Decimal to Fraction -->
          <path d="M 610 160 C 530 195, 430 195, 350 160" fill="none" stroke="#0d9488" stroke-width="3" stroke-dasharray="6,4" marker-end="url(#arrowTeal)"/>

          <!-- Decimal to Percentage -->
          <path d="M 720 230 C 760 300, 700 370, 560 380" fill="none" stroke="#0d9488" stroke-width="3" stroke-dasharray="6,4" marker-end="url(#arrowTeal)"/>
          <!-- Percentage to Decimal -->
          <path d="M 520 405 C 650 420, 780 340, 740 240" fill="none" stroke="#d97706" stroke-width="3" stroke-dasharray="6,4" marker-end="url(#arrowAmber)"/>

          <!-- Percentage to Fraction -->
          <path d="M 400 380 C 260 370, 200 300, 240 230" fill="none" stroke="#d97706" stroke-width="3" stroke-dasharray="6,4" marker-end="url(#arrowAmber)"/>
          <!-- Fraction to Percentage -->
          <path d="M 220 240 C 180 340, 310 420, 440 405" fill="none" stroke="#4f46e5" stroke-width="3" stroke-dasharray="6,4" marker-end="url(#arrowIndigo)"/>

          <!-- NODE 1: FRACTIONS (Top Left) -->
          <g class="svg-hover-card" transform="translate(180, 150)">
            <circle cx="0" cy="0" r="75" fill="url(#indigoGrad)" filter="url(#shadowDrop)"/>
            <circle cx="0" cy="0" r="68" fill="none" stroke="#ffffff" stroke-width="2" stroke-opacity="0.4"/>
            <text x="0" y="-20" fill="#ffffff" font-family="'Space Grotesk', sans-serif" font-weight="700" font-size="16" text-anchor="middle">FRACTIONS</text>
            <text x="0" y="8" fill="#e0e7ff" font-family="'JetBrains Mono', monospace" font-weight="600" font-size="18" text-anchor="middle">a / b</text>
            <text x="0" y="32" fill="#c7d2fe" font-size="11" text-anchor="middle">Part-to-Whole Ratio</text>
          </g>

          <!-- NODE 2: DECIMALS (Top Right) -->
          <g class="svg-hover-card" transform="translate(780, 150)">
            <circle cx="0" cy="0" r="75" fill="url(#tealGrad)" filter="url(#shadowDrop)"/>
            <circle cx="0" cy="0" r="68" fill="none" stroke="#ffffff" stroke-width="2" stroke-opacity="0.4"/>
            <text x="0" y="-20" fill="#ffffff" font-family="'Space Grotesk', sans-serif" font-weight="700" font-size="16" text-anchor="middle">DECIMALS</text>
            <text x="0" y="8" fill="#ccfbf1" font-family="'JetBrains Mono', monospace" font-weight="600" font-size="18" text-anchor="middle">0.xyz</text>
            <text x="0" y="32" fill="#99f6e4" font-size="11" text-anchor="middle">Base-10 Multiplier</text>
          </g>

          <!-- NODE 3: PERCENTAGES (Bottom Center) -->
          <g class="svg-hover-card" transform="translate(480, 390)">
            <circle cx="0" cy="0" r="75" fill="url(#amberGrad)" filter="url(#shadowDrop)"/>
            <circle cx="0" cy="0" r="68" fill="none" stroke="#ffffff" stroke-width="2" stroke-opacity="0.4"/>
            <text x="0" y="-20" fill="#ffffff" font-family="'Space Grotesk', sans-serif" font-weight="700" font-size="15" text-anchor="middle">PERCENTAGES</text>
            <text x="0" y="8" fill="#fef3c7" font-family="'JetBrains Mono', monospace" font-weight="700" font-size="20" text-anchor="middle">p %</text>
            <text x="0" y="30" fill="#fde68a" font-size="11" text-anchor="middle">Per Hundred ( / 100)</text>
          </g>

          <!-- Transformation Action Labels & Formula Badges -->
          <!-- Fraction -> Decimal -->
          <rect x="420" y="70" width="120" height="28" rx="6" fill="#eff6ff" stroke="#93c5fd" stroke-width="1.5"/>
          <text x="480" y="89" fill="#1e40af" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="700" text-anchor="middle">Divide: a ÷ b</text>

          <!-- Decimal -> Fraction -->
          <rect x="410" y="175" width="140" height="28" rx="6" fill="#f0fdf4" stroke="#86efac" stroke-width="1.5"/>
          <text x="480" y="194" fill="#166534" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="700" text-anchor="middle">Write over 10ⁿ &amp; Reduce</text>

          <!-- Decimal -> Percentage -->
          <rect x="680" y="295" width="120" height="28" rx="6" fill="#f0fdf4" stroke="#86efac" stroke-width="1.5"/>
          <text x="740" y="314" fill="#166534" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="700" text-anchor="middle">Multiply by 100%</text>

          <!-- Percentage -> Decimal -->
          <rect x="670" y="380" width="115" height="28" rx="6" fill="#fffbeb" stroke="#fcd34d" stroke-width="1.5"/>
          <text x="727" y="399" fill="#92400e" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="700" text-anchor="middle">Divide by 100</text>

          <!-- Percentage -> Fraction -->
          <rect x="180" y="380" width="125" height="28" rx="6" fill="#fffbeb" stroke="#fcd34d" stroke-width="1.5"/>
          <text x="242" y="399" fill="#92400e" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="700" text-anchor="middle">Put over 100 &amp; Simplify</text>

          <!-- Fraction -> Percentage -->
          <rect x="160" y="295" width="120" height="28" rx="6" fill="#eff6ff" stroke="#93c5fd" stroke-width="1.5"/>
          <text x="220" y="314" fill="#1e40af" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="700" text-anchor="middle">× 100% or Eq. Denom</text>

          <!-- Center Explanatory Hub -->
          <rect x="375" y="235" width="210" height="80" rx="10" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5"/>
          <text x="480" y="258" fill="#1e1b4b" font-family="'Space Grotesk', sans-serif" font-weight="700" font-size="13" text-anchor="middle">Universal Benchmark: 100</text>
          <text x="480" y="278" fill="#475569" font-size="11" text-anchor="middle">3/5 = 0.60 = 60%</text>
          <text x="480" y="298" fill="#475569" font-size="11" text-anchor="middle">1/4 = 0.25 = 25% | 7/8 = 0.875 = 87.5%</text>
        </svg>
        <p class="svg-caption">Figure 1.1: The FDP Conversion Trinity — showing the seamless algebraic transformations between rational fractions, decimal numbers, and percentages.</p>
      </div>

      <!-- INTRICATE SVG 2: BENCHMARK DUAL NUMBER LINE & MULTIPLIERS -->
      <div class="svg-container">
        <h4 style="margin-bottom: 0.5rem; color: #1e1b4b; font-family: 'Space Grotesk', sans-serif;"><i class="fa-solid fa-ruler-horizontal"></i> SVG Diagram 2: Multi-Scale Benchmark Number Line &amp; Multipliers (0% to 250%)</h4>
        <svg viewBox="0 0 960 400" xmlns="http://www.w3.org/2000/svg" style="background: #ffffff; border-radius: 16px;">
          <!-- Frame -->
          <rect x="10" y="10" width="940" height="380" rx="14" fill="#ffffff" stroke="#e2e8f0" stroke-width="2"/>

          <!-- Section Title Inside SVG -->
          <text x="480" y="45" fill="#1e1b4b" font-family="'Space Grotesk', sans-serif" font-weight="700" font-size="16" text-anchor="middle">BENCHMARK RATIOS, DECIMALS, AND MULTIPLIER REGIMES</text>

          <!-- Main Axis Lines -->
          <!-- Percent Line -->
          <line x1="80" y1="120" x2="880" y2="120" stroke="#312e81" stroke-width="4" stroke-linecap="round"/>
          <text x="50" y="125" fill="#312e81" font-family="'Space Grotesk', sans-serif" font-weight="700" font-size="13" text-anchor="end">Percent (%)</text>

          <!-- Decimal Multiplier Line -->
          <line x1="80" y1="200" x2="880" y2="200" stroke="#0d9488" stroke-width="4" stroke-linecap="round"/>
          <text x="50" y="205" fill="#0d9488" font-family="'Space Grotesk', sans-serif" font-weight="700" font-size="13" text-anchor="end">Multiplier</text>

          <!-- Fraction Benchmark Line -->
          <line x1="80" y1="280" x2="880" y2="280" stroke="#d97706" stroke-width="4" stroke-linecap="round"/>
          <text x="50" y="285" fill="#d97706" font-family="'Space Grotesk', sans-serif" font-weight="700" font-size="13" text-anchor="end">Fraction</text>

          <!-- Ticks & Data Nodes -->
          <!-- 0% Point -->
          <g transform="translate(100, 0)">
            <line x1="0" y1="105" x2="0" y2="295" stroke="#cbd5e1" stroke-width="1.5" stroke-dasharray="3,3"/>
            <circle cx="0" cy="120" r="6" fill="#312e81"/>
            <circle cx="0" cy="200" r="6" fill="#0d9488"/>
            <circle cx="0" cy="280" r="6" fill="#d97706"/>
            <text x="0" y="100" fill="#312e81" font-weight="700" font-size="13" text-anchor="middle">0%</text>
            <text x="0" y="190" fill="#0d9488" font-weight="700" font-size="13" text-anchor="middle">0.0</text>
            <text x="0" y="310" fill="#d97706" font-weight="700" font-size="13" text-anchor="middle">0</text>
          </g>

          <!-- 25% Point -->
          <g transform="translate(190, 0)">
            <line x1="0" y1="105" x2="0" y2="295" stroke="#cbd5e1" stroke-width="1.5" stroke-dasharray="3,3"/>
            <circle cx="0" cy="120" r="5" fill="#312e81"/>
            <circle cx="0" cy="200" r="5" fill="#0d9488"/>
            <circle cx="0" cy="280" r="5" fill="#d97706"/>
            <text x="0" y="100" fill="#312e81" font-weight="700" font-size="12" text-anchor="middle">25%</text>
            <text x="0" y="190" fill="#0d9488" font-weight="700" font-size="12" text-anchor="middle">0.25</text>
            <text x="0" y="310" fill="#d97706" font-weight="700" font-size="12" text-anchor="middle">1/4</text>
          </g>

          <!-- 50% Point -->
          <g transform="translate(280, 0)">
            <line x1="0" y1="105" x2="0" y2="295" stroke="#cbd5e1" stroke-width="1.5" stroke-dasharray="3,3"/>
            <circle cx="0" cy="120" r="6" fill="#312e81"/>
            <circle cx="0" cy="200" r="6" fill="#0d9488"/>
            <circle cx="0" cy="280" r="6" fill="#d97706"/>
            <text x="0" y="100" fill="#312e81" font-weight="700" font-size="13" text-anchor="middle">50%</text>
            <text x="0" y="190" fill="#0d9488" font-weight="700" font-size="13" text-anchor="middle">0.5</text>
            <text x="0" y="310" fill="#d97706" font-weight="700" font-size="13" text-anchor="middle">1/2</text>
          </g>

          <!-- 75% Point -->
          <g transform="translate(370, 0)">
            <line x1="0" y1="105" x2="0" y2="295" stroke="#cbd5e1" stroke-width="1.5" stroke-dasharray="3,3"/>
            <circle cx="0" cy="120" r="5" fill="#312e81"/>
            <circle cx="0" cy="200" r="5" fill="#0d9488"/>
            <circle cx="0" cy="280" r="5" fill="#d97706"/>
            <text x="0" y="100" fill="#312e81" font-weight="700" font-size="12" text-anchor="middle">75%</text>
            <text x="0" y="190" fill="#0d9488" font-weight="700" font-size="12" text-anchor="middle">0.75</text>
            <text x="0" y="310" fill="#d97706" font-weight="700" font-size="12" text-anchor="middle">3/4</text>
          </g>

          <!-- 100% WHOLE Point (Highlighted) -->
          <g transform="translate(460, 0)">
            <rect x="-24" y="85" width="48" height="235" rx="8" fill="#e0e7ff" fill-opacity="0.5" stroke="#818cf8" stroke-width="1.5"/>
            <circle cx="0" cy="120" r="8" fill="#4338ca"/>
            <circle cx="0" cy="200" r="8" fill="#0d9488"/>
            <circle cx="0" cy="280" r="8" fill="#d97706"/>
            <text x="0" y="100" fill="#4338ca" font-weight="800" font-size="14" text-anchor="middle">100%</text>
            <text x="0" y="190" fill="#0d9488" font-weight="800" font-size="14" text-anchor="middle">1.0</text>
            <text x="0" y="310" fill="#d97706" font-weight="800" font-size="14" text-anchor="middle">1 (Whole)</text>
          </g>

          <!-- 150% Point -->
          <g transform="translate(590, 0)">
            <line x1="0" y1="105" x2="0" y2="295" stroke="#cbd5e1" stroke-width="1.5" stroke-dasharray="3,3"/>
            <circle cx="0" cy="120" r="5" fill="#312e81"/>
            <circle cx="0" cy="200" r="5" fill="#0d9488"/>
            <circle cx="0" cy="280" r="5" fill="#d97706"/>
            <text x="0" y="100" fill="#312e81" font-weight="700" font-size="12" text-anchor="middle">150%</text>
            <text x="0" y="190" fill="#0d9488" font-weight="700" font-size="12" text-anchor="middle">1.5</text>
            <text x="0" y="310" fill="#d97706" font-weight="700" font-size="12" text-anchor="middle">3/2</text>
          </g>

          <!-- 200% Double Point -->
          <g transform="translate(720, 0)">
            <line x1="0" y1="105" x2="0" y2="295" stroke="#cbd5e1" stroke-width="1.5" stroke-dasharray="3,3"/>
            <circle cx="0" cy="120" r="6" fill="#312e81"/>
            <circle cx="0" cy="200" r="6" fill="#0d9488"/>
            <circle cx="0" cy="280" r="6" fill="#d97706"/>
            <text x="0" y="100" fill="#312e81" font-weight="700" font-size="13" text-anchor="middle">200%</text>
            <text x="0" y="190" fill="#0d9488" font-weight="700" font-size="13" text-anchor="middle">2.0</text>
            <text x="0" y="310" fill="#d97706" font-weight="700" font-size="13" text-anchor="middle">2 (Double)</text>
          </g>

          <!-- 250% Target Surge Point -->
          <g transform="translate(850, 0)">
            <line x1="0" y1="105" x2="0" y2="295" stroke="#cbd5e1" stroke-width="1.5" stroke-dasharray="3,3"/>
            <circle cx="0" cy="120" r="6" fill="#312e81"/>
            <circle cx="0" cy="200" r="6" fill="#0d9488"/>
            <circle cx="0" cy="280" r="6" fill="#d97706"/>
            <text x="0" y="100" fill="#312e81" font-weight="700" font-size="13" text-anchor="middle">250%</text>
            <text x="0" y="190" fill="#0d9488" font-weight="700" font-size="13" text-anchor="middle">2.5</text>
            <text x="0" y="310" fill="#d97706" font-weight="700" font-size="13" text-anchor="middle">5/2 (Surge)</text>
          </g>

          <!-- Bottom Region Labels -->
          <rect x="100" y="340" width="340" height="26" rx="6" fill="#eff6ff" stroke="#bfdbfe"/>
          <text x="270" y="358" fill="#1e40af" font-size="11" font-weight="600" text-anchor="middle">◀ Fractional Reduction Domain (&lt; 100%, Multiplier &lt; 1.0)</text>

          <rect x="480" y="340" width="370" height="26" rx="6" fill="#fef2f2" stroke="#fecaca"/>
          <text x="665" y="358" fill="#991b1b" font-size="11" font-weight="600" text-anchor="middle">Expansion / Multiplier Growth Domain (&gt; 100%, Multiplier &gt; 1.0) ▶</text>
        </svg>
        <p class="svg-caption">Figure 1.2: The Dual-Scale Benchmark Number Line — visualizing how percentages map identically onto decimal multipliers and rational fractions across both reduction and growth regimes.</p>
      </div>

      <!-- INTRICATE SVG 3: SIMPLE VS COMPOUND INTEREST DIVERGENCE -->
      <div class="svg-container">
        <h4 style="margin-bottom: 0.5rem; color: #1e1b4b; font-family: 'Space Grotesk', sans-serif;"><i class="fa-solid fa-chart-line"></i> SVG Diagram 3: Capital Growth Divergence (Simple Interest vs Compound Interest @ 10% p.a. on ₹6,000)</h4>
        <svg viewBox="0 0 960 440" xmlns="http://www.w3.org/2000/svg" style="background: #ffffff; border-radius: 16px;">
          <!-- Outer border -->
          <rect x="10" y="10" width="940" height="420" rx="14" fill="#ffffff" stroke="#e2e8f0" stroke-width="2"/>

          <!-- Title -->
          <text x="480" y="42" fill="#1e1b4b" font-family="'Space Grotesk', sans-serif" font-weight="700" font-size="16" text-anchor="middle">YEAR-BY-YEAR ACCUMULATION: OPTION 1 (SIMPLE) VS OPTION 2 (COMPOUND)</text>

          <!-- Axes -->
          <!-- Y Axis -->
          <line x1="120" y1="360" x2="120" y2="80" stroke="#64748b" stroke-width="2"/>
          <!-- X Axis -->
          <line x1="120" y1="360" x2="880" y2="360" stroke="#64748b" stroke-width="2"/>

          <!-- Y-Axis Grid & Labels (₹6,000, ₹7,000, ₹8,000, ₹9,000, ₹10,000) -->
          <!-- Base ₹6,000 (y = 360) -->
          <line x1="115" y1="360" x2="880" y2="360" stroke="#e2e8f0" stroke-width="1"/>
          <text x="105" y="365" fill="#64748b" font-size="11" font-weight="600" text-anchor="end">₹6,000 (P)</text>

          <!-- ₹7,000 (y = 290) -->
          <line x1="115" y1="290" x2="880" y2="290" stroke="#f1f5f9" stroke-width="1"/>
          <text x="105" y="295" fill="#64748b" font-size="11" font-weight="600" text-anchor="end">₹7,000</text>

          <!-- ₹8,000 (y = 220) -->
          <line x1="115" y1="220" x2="880" y2="220" stroke="#f1f5f9" stroke-width="1"/>
          <text x="105" y="225" fill="#64748b" font-size="11" font-weight="600" text-anchor="end">₹8,000</text>

          <!-- ₹9,000 (y = 150) -->
          <line x1="115" y1="150" x2="880" y2="150" stroke="#f1f5f9" stroke-width="1"/>
          <text x="105" y="155" fill="#64748b" font-size="11" font-weight="600" text-anchor="end">₹9,000</text>

          <!-- ₹10,000 (y = 80) -->
          <line x1="115" y1="80" x2="880" y2="80" stroke="#f1f5f9" stroke-width="1"/>
          <text x="105" y="85" fill="#64748b" font-size="11" font-weight="600" text-anchor="end">₹10,000</text>

          <!-- X-Axis Points (Years 0, 1, 2, 3, 4, 5) -->
          <!-- Year 0: x = 150 -->
          <!-- Year 1: x = 280 -->
          <!-- Year 2: x = 420 -->
          <!-- Year 3: x = 560 -->
          <!-- Year 4: x = 700 -->
          <!-- Year 5: x = 840 -->

          <!-- Simple Interest Path (Straight Line: +₹600 each year) -->
          <!-- Y0: 6000 (y=360), Y1: 6600 (y=318), Y2: 7200 (y=276), Y3: 7800 (y=234), Y4: 8400 (y=192), Y5: 9000 (y=150) -->
          <path d="M 150 360 L 280 318 L 420 276 L 560 234 L 700 192 L 840 150" fill="none" stroke="#2563eb" stroke-width="3.5"/>

          <!-- Compound Interest Path (Geometric Curve: × 1.10 each year) -->
          <!-- Y0: 6000 (y=360), Y1: 6600 (y=318), Y2: 7260 (y=271.8), Y3: 7986 (y=221), Y4: 8784.6 (y=165), Y5: 9663 (y=103.6) -->
          <path d="M 150 360 L 280 318 L 420 271.8 L 560 221 L 700 165 L 840 103.6" fill="none" stroke="#10b981" stroke-width="3.5"/>

          <!-- Shaded Divergence Region between Y3 and Y5 -->
          <polygon points="560,234 700,192 840,150 840,103.6 700,165 560,221" fill="#ecfdf5" fill-opacity="0.6"/>

          <!-- Data Points & Tooltip Labels -->
          <!-- Year 1 Points -->
          <circle cx="280" cy="318" r="6" fill="#3b82f6"/>
          <text x="280" y="340" fill="#1e40af" font-weight="700" font-size="11" text-anchor="middle">₹6,600</text>

          <!-- Year 2 Points -->
          <circle cx="420" cy="276" r="5" fill="#2563eb"/>
          <circle cx="420" cy="271.8" r="5" fill="#10b981"/>
          <text x="420" y="295" fill="#2563eb" font-size="10" font-weight="700" text-anchor="middle">SI: ₹7,200</text>
          <text x="420" y="260" fill="#047857" font-size="10" font-weight="700" text-anchor="middle">CI: ₹7,260 (+₹60)</text>

          <!-- Year 3 Points (From Textbook Example 7) -->
          <circle cx="560" cy="234" r="6" fill="#2563eb"/>
          <circle cx="560" cy="221" r="6" fill="#10b981"/>
          <text x="560" y="252" fill="#2563eb" font-size="10" font-weight="700" text-anchor="middle">SI: ₹7,800</text>
          <text x="560" y="210" fill="#047857" font-size="10" font-weight="700" text-anchor="middle">CI: ₹7,986 (+₹186)</text>

          <!-- Year 5 Final Points -->
          <circle cx="840" cy="150" r="7" fill="#2563eb"/>
          <circle cx="840" cy="103.6" r="7" fill="#10b981"/>
          <text x="840" y="168" fill="#2563eb" font-weight="700" font-size="11" text-anchor="middle">SI: ₹9,000</text>
          <text x="840" y="93" fill="#047857" font-weight="700" font-size="12" text-anchor="middle">CI: ₹9,663 (+₹663!)</text>

          <!-- X Axis Labels -->
          <text x="150" y="380" fill="#475569" font-weight="700" font-size="12" text-anchor="middle">Start (Yr 0)</text>
          <text x="280" y="380" fill="#475569" font-weight="700" font-size="12" text-anchor="middle">Year 1</text>
          <text x="420" y="380" fill="#475569" font-weight="700" font-size="12" text-anchor="middle">Year 2</text>
          <text x="560" y="380" fill="#475569" font-weight="700" font-size="12" text-anchor="middle">Year 3</text>
          <text x="700" y="380" fill="#475569" font-weight="700" font-size="12" text-anchor="middle">Year 4</text>
          <text x="840" y="380" fill="#475569" font-weight="700" font-size="12" text-anchor="middle">Year 5</text>

          <!-- Legend Box -->
          <rect x="150" y="65" width="310" height="42" rx="8" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5"/>
          <line x1="165" y1="86" x2="195" y2="86" stroke="#2563eb" stroke-width="3"/>
          <circle cx="180" cy="86" r="4" fill="#2563eb"/>
          <text x="205" y="90" fill="#1e3a8a" font-size="11" font-weight="700">Option 1: Simple Interest (Linear)</text>

          <line x1="315" y1="86" x2="345" y2="86" stroke="#10b981" stroke-width="3"/>
          <circle cx="330" cy="86" r="4" fill="#10b981"/>
          <text x="355" y="90" fill="#064e3b" font-size="11" font-weight="700">Option 2: Compounded (Exponential)</text>
        </svg>
        <p class="svg-caption">Figure 1.3: Visualizing the Interest on Interest Gap — Option 1 adds fixed ₹600 each year, whereas Option 2 compounds principal by 1.10× annually, creating rapid exponential divergence.</p>
      </div>

      <!-- DETAILED TEXT-BASED CONCEPT TREE & HIERARCHICAL MIND MAP -->
      <h3 class="subheading"><i class="fa-solid fa-network-wired"></i> Hierarchical Chapter Mind Map</h3>
      <div style="background: #ffffff; border: 1px solid var(--border); border-radius: var(--radius-lg); padding: 1.75rem; box-shadow: var(--shadow-sm); line-height: 1.8;">
        <ul style="list-style: none; padding-left: 0;">
          <li style="margin-bottom: 1.25rem;">
            <strong style="color: #4338ca; font-size: 1.15rem;"><i class="fa-solid fa-folder-open"></i> 1. Foundations of "Per Centum" (The Denominator 100)</strong>
            <ul style="padding-left: 1.75rem; margin-top: 0.35rem; color: #334155;">
              <li><strong>Etymology &amp; Definition:</strong> Latin <em>per centum</em> meaning "by the hundred". A fraction whose denominator is fixed at 100: <code>x% = x / 100</code>.</li>
              <li><strong>Why 100?</strong> Unifies comparisons across unequal bases (e.g., 9/34 sugar vs 13/45 sugar). Aligns directly with base-10 decimal place values (0.01 = 1 hundredth).</li>
              <li><strong>The Metric Ladder:</strong> <em>Per Decem</em> (per 10) ↔ <em>Per Centum</em> (per 100) ↔ <em>Per Mille</em> (per 1,000, ‰) ↔ <em>Per Lakh / Million</em>.</li>
            </ul>
          </li>

          <li style="margin-bottom: 1.25rem;">
            <strong style="color: #0d9488; font-size: 1.15rem;"><i class="fa-solid fa-folder-open"></i> 2. The Conversion Trinity (Fraction ↔ Decimal ↔ Percentage)</strong>
            <ul style="padding-left: 1.75rem; margin-top: 0.35rem; color: #334155;">
              <li><strong>Fraction to Percentage:</strong> Three equivalent routes:
                <ul>
                  <li><em>Method 1 (Equivalent Denominator):</em> Multiply numerator and denominator by factor <code>k = 100 / b</code>.</li>
                  <li><em>Method 2 (Unitary Scaling):</em> Value out of <code>b</code> is <code>a</code>; out of 1 is <code>a/b</code>; out of 100 is <code>(a/b) × 100</code>.</li>
                  <li><em>Method 3 (100% Multiplication):</em> <code>Fraction × 100%</code>.</li>
                </ul>
              </li>
              <li><strong>Percentage to Fraction:</strong> Replace % with <code>/ 100</code> and reduce by dividing by common factors.</li>
              <li><strong>Decimal Interlock:</strong> Move decimal point two positions right for %, two positions left for decimal (<code>0.825 ↔ 82.5%</code>).</li>
            </ul>
          </li>

          <li style="margin-bottom: 1.25rem;">
            <strong style="color: #d97706; font-size: 1.15rem;"><i class="fa-solid fa-folder-open"></i> 3. Free-Hand Mental Computation Toolkit</strong>
            <ul style="padding-left: 1.75rem; margin-top: 0.35rem; color: #334155;">
              <li><strong>10% Anchor:</strong> Shift decimal 1 place left (<code>10% of 280 = 28</code>).</li>
              <li><strong>1% Anchor:</strong> Shift decimal 2 places left (<code>1% of 280 = 2.8</code>).</li>
              <li><strong>Derived Benchmarks:</strong> <code>5% = half of 10%</code> | <code>20% = double of 10%</code> | <code>25% = half of 50% (divide by 4)</code> | <code>15% = 10% + 5%</code>.</li>
              <li><strong>Commutative Multiplication Law:</strong> <code>x% of y = y% of x</code>. High-speed evaluation: <code>16% of 50 = 50% of 16 = 8</code>!</li>
            </ul>
          </li>

          <li style="margin-bottom: 1.25rem;">
            <strong style="color: #7c3aed; font-size: 1.15rem;"><i class="fa-solid fa-folder-open"></i> 4. Commercial Arithmetic &amp; Trading Flow</strong>
            <ul style="padding-left: 1.75rem; margin-top: 0.35rem; color: #334155;">
              <li><strong>Base of Profit/Loss:</strong> Always calculated on <strong>Cost Price (CP)</strong>: <code>Profit% = (Profit / CP) × 100</code>.</li>
              <li><strong>Overhead Expenses:</strong> Additional costs (freight, repairs, packaging) must be added to purchase price to yield <em>Effective Cost Price</em>.</li>
              <li><strong>Trade Discounts:</strong> Always calculated on <strong>Marked Price (MP)</strong>: <code>Discount% = (Discount / MP) × 100</code>; <code>SP = MP × (1 - d/100)</code>.</li>
              <li><strong>Indirect Taxes (GST):</strong> Added on actual selling price: <code>Final Bill = SP × (1 + GST%/100)</code>.</li>
            </ul>
          </li>

          <li style="margin-bottom: 1.25rem;">
            <strong style="color: #059669; font-size: 1.15rem;"><i class="fa-solid fa-folder-open"></i> 5. Capital Growth: Simple vs Compound Interest</strong>
            <ul style="padding-left: 1.75rem; margin-top: 0.35rem; color: #334155;">
              <li><strong>Simple Interest (SI):</strong> Interest paid out linearly; principal never changes: <code>SI = (P × R × T) / 100</code>; <code>A = P(1 + RT/100)</code>.</li>
              <li><strong>Compound Interest (CI):</strong> Interest added back to principal each period (interest on interest): <code>A = P(1 + R/100)ᵗ</code>. Multiplier compounding: <code>A = P × mᵗ</code>.</li>
              <li><strong>Depreciation &amp; Decay:</strong> Reductions over time (vehicles, equipment, village migration): <code>A = P(1 - R/100)ᵗ</code>.</li>
            </ul>
          </li>

          <li>
            <strong style="color: #dc2626; font-size: 1.15rem;"><i class="fa-solid fa-folder-open"></i> 6. Deceptive Percentages &amp; Fallacy Traps</strong>
            <ul style="padding-left: 1.75rem; margin-top: 0.35rem; color: #334155;">
              <li><strong>Non-Additivity of Successive Discounts:</strong> "30% + 20% off" is NOT 50% off! It is <code>1 - (0.70 × 0.80) = 44% off</code>.</li>
              <li><strong>The Markup-Discount Asymmetry (Surbhi's Mishap):</strong> Marking up by 50% (<code>1.5x</code>) and discounting by 50% results in <code>0.75x</code> (a 25% net loss!). A 50% markup requires a <code>33.33%</code> discount to break even.</li>
            </ul>
          </li>
        </ul>
      </div>
    </section>
"""
