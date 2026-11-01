# -*- coding: utf-8 -*-
"""
Section 2 Module: Complete Conceptual Explanations & Bilingual Glossary
Class 8 Mathematics Chapter 11: Exploring Some Geometric Themes
"""

def get_section_2():
    return """
    <!-- SECTION 2: CONCEPTS & VOCABULARY -->
    <section id="section2" class="section-box">
      <div class="section-header">
        <div class="section-header-left">
          <span class="section-tag">Theoretical Foundation</span>
          <h2 class="section-title">§ 2. Comprehensive Conceptual Explanations & Bilingual Glossary</h2>
          <p class="section-desc">
            Mastering the core principles of recursive fractals, 3D polyhedra, folding nets, surface geodesics, orthographic projection planes, and isometric spatial geometry with teacher-led step-by-step clarity.
          </p>
        </div>
        <div>
          <span class="badge badge-emerald"><i class="fa-solid fa-graduation-cap"></i> Complete Theory</span>
        </div>
      </div>

      <!-- PART 2.1: THE MAGIC OF FRACTALS & SELF-SIMILARITY -->
      <div class="concept-card">
        <h3 class="concept-card-title"><i class="fa-solid fa-seedling"></i> 2.1 The Magic of Fractals and Self-Similarity</h3>
        <p>
          In classical geometry, we usually study smooth, simple shapes such as circles, squares, rectangles, and triangles. But when we step outdoors and look at nature, mountains are not cones, clouds are not spheres, and coastlines are not straight lines. Nature creates shapes of incredible beauty and complexity using a principle called <strong>self-similarity</strong>.
        </p>

        <div class="callout callout-def">
          <div class="callout-title"><i class="fa-solid fa-circle-info"></i> What is a Fractal?</div>
          <p>
            A <strong>fractal</strong> is a geometric shape that exhibits <strong>self-similarity</strong>. This means that if you zoom in on any small part of the shape, that small part looks identical (or nearly identical) to the whole shape itself! The word ‘fractal’ was coined in 1975 by the Polish-French mathematician <strong>Benoit Mandelbrot</strong>, derived from the Latin word <em>fractus</em>, meaning ‘broken’ or ‘fractured’.
          </p>
        </div>

        <p>
          <strong>Fractals in the Natural World:</strong>
        </p>
        <ul style="margin-left: 1.5rem; margin-bottom: 1.25rem; line-height: 1.8;">
          <li><strong>The Fern Leaf:</strong> If you observe a fern frond, the entire frond is made of smaller leaflets (pinnae). If you examine a single leaflet, it is made of even tinier leaf-like structures (pinnules), which replicate the shape of the entire plant.</li>
          <li><strong>Romanesco Broccoli:</strong> One of nature’s most stunning mathematical masterpieces. Each conical bud on a head of Romanesco is composed of a series of smaller conical buds, arranged in logarithmic Fibonacci spirals.</li>
          <li><strong>Trees & River Systems:</strong> A tree trunk splits into thick limbs, which divide into branches, which divide into twigs, which carry leaf veins. Similarly, a major river splits into tributaries, which split into smaller streams, mimicking the branching of human blood vessels and lightning bolts.</li>
          <li><strong>Coastlines & Clouds:</strong> A rocky bay on a satellite map looks just as jagged when seen from an airplane, from a cliff-top, or under a magnifying glass on a pebble. This is known in mathematics as the <em>Coastline Paradox</em>.</li>
        </ul>

        <div class="callout callout-act">
          <div class="callout-title"><i class="fa-solid fa-lightbulb"></i> Nikola Tesla's Secret Method: Mental Visualization</div>
          <p>
            The great inventor <strong>Nikola Tesla</strong> (1856–1943), who gave humanity alternating current (AC) electricity and radio transformers, wrote: <em>“When I get an idea I start at once building it up in my imagination. I change the construction, make improvements, and operate the device entirely in my mind.”</em> Before putting pencil to paper, training your mind to visualize 3D transformations, rotations, and folding patterns will make you a formidable mathematical thinker!
          </p>
        </div>
      </div>

      <!-- PART 2.2: THE MATHEMATICAL FRACTALS -->
      <div class="concept-card">
        <h3 class="concept-card-title"><i class="fa-solid fa-shapes"></i> 2.2 Mathematical Fractals: Sierpinski Carpet, Sierpinski Gasket & Koch Snowflake</h3>
        <p>
          While natural fractals eventually reach an atomic limit, <strong>mathematical fractals</strong> can be repeated infinitely through recursive geometric rules (iterations). Let us study three iconic mathematical fractals prescribed in Ganita Prakash.
        </p>

        <h4 style="font-size: 1.15rem; color: var(--primary-dark); margin: 1.25rem 0 0.5rem;"><i class="fa-solid fa-border-all"></i> A. The Sierpinski Carpet</h4>
        <p>
          Discovered in 1916 by the brilliant Polish mathematician <strong>Wacław Sierpiński</strong>, the Sierpinski Carpet is generated by repeatedly removing the central square from a grid of 9 squares:
        </p>
        <ul style="margin-left: 1.5rem; margin-bottom: 1rem; line-height: 1.8;">
          <li><strong>Step 0 (Initiator):</strong> Start with a solid square of side length <span class="math-inline">s</span> and area <span class="math-inline">A₀ = s²</span>. Number of remaining squares <span class="math-inline">R₀ = 1</span>, Holes <span class="math-inline">H₀ = 0</span>.</li>
          <li><strong>Step 1 (First Iteration):</strong> Divide the square into a 3 × 3 grid of 9 equal smaller squares (each of side <span class="math-inline">s/3</span>). Cut out and remove the central square. Now, remaining squares <span class="math-inline">R₁ = 8</span>, new holes created = 1 (total holes <span class="math-inline">H₁ = 1</span>). Total area remaining <span class="math-inline">A₁ = (8/9) A₀</span>.</li>
          <li><strong>Step 2 (Second Iteration):</strong> Apply the exact same rule to each of the 8 remaining squares. Each square gives rise to 8 even smaller squares and 1 new central hole. Remaining squares <span class="math-inline">R₂ = 8 × 8 = 8² = 64</span>. New holes added = 8, so total holes <span class="math-inline">H₂ = 1 + 8 = 9</span>. Total area remaining <span class="math-inline">A₂ = (8/9) × A₁ = (8/9)² A₀ = 64/81 A₀</span>.</li>
          <li><strong>Step n (General Formula):</strong>
            <div class="math-block">
              Remaining Squares: Rₙ = 8ⁿ &nbsp;&nbsp;|&nbsp;&nbsp; Holes: Hₙ = 1 + 8 + 8² + ... + 8ⁿ⁻¹ = (8ⁿ - 1) / 7 &nbsp;&nbsp;|&nbsp;&nbsp; Area: Aₙ = (8/9)ⁿ × A₀
            </div>
          </li>
        </ul>
        <p>
          <strong>The Infinite Limit Paradox:</strong> Since <span class="math-inline">8/9 &lt; 1</span>, as <span class="math-inline">n → ∞</span>, <span class="math-inline">(8/9)ⁿ → 0</span>! Thus, the area of the Sierpinski Carpet approaches <strong>exactly zero</strong>, yet it contains an infinite network of boundary lines and uncountably many points!
        </p>

        <h4 style="font-size: 1.15rem; color: var(--primary-dark); margin: 1.75rem 0 0.5rem;"><i class="fa-solid fa-play"></i> B. The Sierpinski Gasket (Sierpinski Triangle)</h4>
        <p>
          Sierpiński applied a similar recursive subtraction to an equilateral triangle:
        </p>
        <ul style="margin-left: 1.5rem; margin-bottom: 1rem; line-height: 1.8;">
          <li><strong>Step 0:</strong> Start with a solid equilateral triangle of side length <span class="math-inline">s</span> and area <span class="math-inline">A₀ = (√3 / 4) s²</span>. Remaining triangles <span class="math-inline">R₀ = 1</span>, Holes <span class="math-inline">H₀ = 0</span>, Perimeter <span class="math-inline">P₀ = 3s</span>.</li>
          <li><strong>Step 1:</strong> Connect the midpoints of the three sides. By the Midpoint Theorem, this divides the large triangle into 4 congruent equilateral triangles, each having side length <span class="math-inline">s/2</span> and area <span class="math-inline">A₀/4</span>. Remove the inverted central triangle!
          <br>Remaining triangles <span class="math-inline">R₁ = 3</span>, Holes <span class="math-inline">H₁ = 1</span>.
          <br>Area remaining <span class="math-inline">A₁ = 3 × (A₀/4) = (3/4) A₀</span>.
          <br>Total perimeter of remaining 3 triangles: <span class="math-inline">P₁ = 3 × [3 × (s/2)] = 9s/2 = 3s × (3/2)¹</span>.</li>
          <li><strong>Step 2:</strong> Repeat the midpoint cutout on each of the 3 remaining triangles.
          <br>Remaining triangles <span class="math-inline">R₂ = 3 × 3 = 3² = 9</span>.
          <br>Holes <span class="math-inline">H₂ = 1 + 3 = 4</span>.
          <br>Area remaining <span class="math-inline">A₂ = (3/4)² A₀ = 9/16 A₀</span>.
          <br>Perimeter <span class="math-inline">P₂ = 9 × [3 × (s/4)] = 27s/4 = 3s × (3/2)²</span>.</li>
          <li><strong>General Formulas for Step n:</strong>
            <div class="math-block">
              Rₙ = 3ⁿ &nbsp;&nbsp;|&nbsp;&nbsp; Hₙ = (3ⁿ - 1) / 2 &nbsp;&nbsp;|&nbsp;&nbsp; Aₙ = (3/4)ⁿ × A₀ &nbsp;&nbsp;|&nbsp;&nbsp; Pₙ = 3s × (3/2)ⁿ
            </div>
          </li>
        </ul>

        <div class="callout callout-warn">
          <div class="callout-title"><i class="fa-solid fa-triangle-exclamation"></i> Mind-Bending Asymptotic Contrast!</div>
          <p>
            Notice what happens as <span class="math-inline">n → ∞</span>:
            <br>1. Area: Because <span class="math-inline">3/4 &lt; 1</span>, <span class="math-inline">Aₙ = (3/4)ⁿ A₀ → 0</span> (The area vanishes to zero!).
            <br>2. Perimeter: Because <span class="math-inline">3/2 &gt; 1</span>, <span class="math-inline">Pₙ = 3s × (1.5)ⁿ → ∞</span> (The perimeter grows beyond all limits to infinity!).
            <br>A shape with <strong>zero area</strong> but <strong>infinite boundary length</strong>!
          </p>
        </div>

        <!-- INLINE RESPONSIVE SVG 2: SIERPINSKI CARPET & GASKET GENERATION -->
        <div class="svg-graphic-box">
          <svg viewBox="0 0 960 420" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg">
            <defs>
              <linearGradient id="sqFill" x1="0%" y1="0%" x2="100%" y2="100%">
                <stop offset="0%" stop-color="#4f46e5" />
                <stop offset="100%" stop-color="#3730a3" />
              </linearGradient>
              <linearGradient id="triFill" x1="0%" y1="0%" x2="100%" y2="100%">
                <stop offset="0%" stop-color="#0891b2" />
                <stop offset="100%" stop-color="#0e7490" />
              </linearGradient>
            </defs>
            <rect width="960" height="420" rx="16" fill="#f8fafc" stroke="#e2e8f0" stroke-width="2" />
            
            <!-- Panel Header -->
            <text x="480" y="32" text-anchor="middle" fill="#0f172a" font-family="'Space Grotesk', sans-serif" font-size="17" font-weight="700">Recursive Cascade of Sierpinski Fractals</text>

            <!-- SUB-SECTION A: SIERPINSKI CARPET (Top Row) -->
            <g transform="translate(40, 50)">
              <text x="0" y="22" fill="#4f46e5" font-family="'Space Grotesk', sans-serif" font-size="14" font-weight="700">Sierpinski Carpet Iterations:</text>
              
              <!-- Step 0 -->
              <g transform="translate(190, 0)">
                <rect width="90" height="90" fill="url(#sqFill)" rx="4" />
                <text x="45" y="112" text-anchor="middle" fill="#475569" font-family="'Plus Jakarta Sans', sans-serif" font-size="11" font-weight="600">Step 0: R₀=1, H₀=0</text>
                <text x="45" y="126" text-anchor="middle" fill="#64748b" font-family="'JetBrains Mono', monospace" font-size="10">Area = A₀</text>
              </g>

              <path d="M 305 45 L 340 45" stroke="#94a3b8" stroke-width="2" marker-end="url(#arrow)" />
              <text x="322" y="38" text-anchor="middle" fill="#64748b" font-size="10">÷9</text>

              <!-- Step 1 -->
              <g transform="translate(365, 0)">
                <rect width="90" height="90" fill="url(#sqFill)" rx="4" />
                <!-- Central Cutout -->
                <rect x="30" y="30" width="30" height="30" fill="#ffffff" stroke="#cbd5e1" stroke-width="1" />
                <text x="45" y="112" text-anchor="middle" fill="#475569" font-family="'Plus Jakarta Sans', sans-serif" font-size="11" font-weight="600">Step 1: R₁=8, H₁=1</text>
                <text x="45" y="126" text-anchor="middle" fill="#64748b" font-family="'JetBrains Mono', monospace" font-size="10">Area = (8/9)A₀</text>
              </g>

              <path d="M 480 45 L 515 45" stroke="#94a3b8" stroke-width="2" />
              <text x="498" y="38" text-anchor="middle" fill="#64748b" font-size="10">÷9</text>

              <!-- Step 2 -->
              <g transform="translate(540, 0)">
                <rect width="90" height="90" fill="url(#sqFill)" rx="4" />
                <!-- Central Cutout level 1 -->
                <rect x="30" y="30" width="30" height="30" fill="#ffffff" />
                <!-- 8 level 2 cutouts -->
                <rect x="10" y="10" width="10" height="10" fill="#ffffff" />
                <rect x="40" y="10" width="10" height="10" fill="#ffffff" />
                <rect x="70" y="10" width="10" height="10" fill="#ffffff" />
                <rect x="10" y="40" width="10" height="10" fill="#ffffff" />
                <rect x="70" y="40" width="10" height="10" fill="#ffffff" />
                <rect x="10" y="70" width="10" height="10" fill="#ffffff" />
                <rect x="40" y="70" width="10" height="10" fill="#ffffff" />
                <rect x="70" y="70" width="10" height="10" fill="#ffffff" />
                <text x="45" y="112" text-anchor="middle" fill="#475569" font-family="'Plus Jakarta Sans', sans-serif" font-size="11" font-weight="600">Step 2: R₂=64, H₂=9</text>
                <text x="45" y="126" text-anchor="middle" fill="#64748b" font-family="'JetBrains Mono', monospace" font-size="10">Area = (64/81)A₀</text>
              </g>

              <!-- Step n formula badge -->
              <g transform="translate(680, 15)">
                <rect width="180" height="70" rx="8" fill="#eef2ff" stroke="#c7d2fe" stroke-width="1.5" />
                <text x="90" y="24" text-anchor="middle" fill="#3730a3" font-family="'Space Grotesk', sans-serif" font-size="12" font-weight="700">Step n Formula</text>
                <text x="90" y="44" text-anchor="middle" fill="#1e1b4b" font-family="'JetBrains Mono', monospace" font-size="11">Rₙ = 8ⁿ | Hₙ = (8ⁿ-1)/7</text>
                <text x="90" y="60" text-anchor="middle" fill="#059669" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="700">Area → 0 as n → ∞</text>
              </g>
            </g>

            <!-- DIVIDER LINE -->
            <line x1="40" y1="205" x2="920" y2="205" stroke="#e2e8f0" stroke-width="1.5" stroke-dasharray="4,4" />

            <!-- SUB-SECTION B: SIERPINSKI GASKET / TRIANGLE (Bottom Row) -->
            <g transform="translate(40, 225)">
              <text x="0" y="25" fill="#0891b2" font-family="'Space Grotesk', sans-serif" font-size="14" font-weight="700">Sierpinski Gasket Iterations:</text>
              
              <!-- Step 0 Triangle -->
              <g transform="translate(180, 10)">
                <polygon points="50,5 5,90 95,90" fill="url(#triFill)" />
                <text x="50" y="112" text-anchor="middle" fill="#475569" font-family="'Plus Jakarta Sans', sans-serif" font-size="11" font-weight="600">Step 0: R₀=1, H₀=0</text>
                <text x="50" y="126" text-anchor="middle" fill="#64748b" font-family="'JetBrains Mono', monospace" font-size="10">P₀ = 3s, A₀</text>
              </g>

              <path d="M 305 60 L 340 60" stroke="#94a3b8" stroke-width="2" />
              <text x="322" y="53" text-anchor="middle" fill="#64748b" font-size="10">Midpoints</text>

              <!-- Step 1 Triangle -->
              <g transform="translate(360, 10)">
                <polygon points="50,5 5,90 95,90" fill="url(#triFill)" />
                <!-- Inverted cutout -->
                <polygon points="27.5,47.5 72.5,47.5 50,90" fill="#ffffff" />
                <text x="50" y="112" text-anchor="middle" fill="#475569" font-family="'Plus Jakarta Sans', sans-serif" font-size="11" font-weight="600">Step 1: R₁=3, H₁=1</text>
                <text x="50" y="126" text-anchor="middle" fill="#64748b" font-family="'JetBrains Mono', monospace" font-size="10">P₁ = 4.5s, A = 0.75A₀</text>
              </g>

              <path d="M 480 60 L 515 60" stroke="#94a3b8" stroke-width="2" />
              <text x="498" y="53" text-anchor="middle" fill="#64748b" font-size="10">Midpoints</text>

              <!-- Step 2 Triangle -->
              <g transform="translate(535, 10)">
                <polygon points="50,5 5,90 95,90" fill="url(#triFill)" />
                <!-- Central level 1 -->
                <polygon points="27.5,47.5 72.5,47.5 50,90" fill="#ffffff" />
                <!-- 3 level 2 cutouts -->
                <polygon points="38.75,26.25 61.25,26.25 50,47.5" fill="#ffffff" />
                <polygon points="16.25,68.75 38.75,68.75 27.5,90" fill="#ffffff" />
                <polygon points="61.25,68.75 83.75,68.75 72.5,90" fill="#ffffff" />
                <text x="50" y="112" text-anchor="middle" fill="#475569" font-family="'Plus Jakarta Sans', sans-serif" font-size="11" font-weight="600">Step 2: R₂=9, H₂=4</text>
                <text x="50" y="126" text-anchor="middle" fill="#64748b" font-family="'JetBrains Mono', monospace" font-size="10">P₂ = 6.75s, A = (9/16)A₀</text>
              </g>

              <!-- Step n formula badge -->
              <g transform="translate(680, 25)">
                <rect width="180" height="70" rx="8" fill="#ecfeff" stroke="#a5f3fc" stroke-width="1.5" />
                <text x="90" y="24" text-anchor="middle" fill="#0e7490" font-family="'Space Grotesk', sans-serif" font-size="12" font-weight="700">Gasket Limits</text>
                <text x="90" y="44" text-anchor="middle" fill="#155e75" font-family="'JetBrains Mono', monospace" font-size="11">Rₙ = 3ⁿ | Pₙ = 3s(1.5)ⁿ</text>
                <text x="90" y="60" text-anchor="middle" fill="#dc2626" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="700">Area → 0, Perimeter → ∞</text>
              </g>
            </g>
          </svg>
          <p class="svg-caption"><strong>Figure 2.1:</strong> Recursive generation of the Sierpinski Carpet (top) and Sierpinski Gasket (bottom) showcasing asymptotic area decay to zero.</p>
        </div>

        <h4 style="font-size: 1.15rem; color: var(--primary-dark); margin: 1.75rem 0 0.5rem;"><i class="fa-solid fa-snowflake"></i> C. The Koch Snowflake</h4>
        <p>
          First described in 1904 by the Swedish mathematician <strong>Niels Fabian Helge von Koch</strong>, the Koch Snowflake begins with an equilateral triangle and iteratively adds triangular ‘bumps’ onto each edge:
        </p>
        <ul style="margin-left: 1.5rem; margin-bottom: 1rem; line-height: 1.8;">
          <li><strong>Step 0 (Initiator):</strong> An equilateral triangle with side length <span class="math-inline">s = 1</span>. Number of sides <span class="math-inline">N₀ = 3</span>. Side length <span class="math-inline">L₀ = 1</span>. Perimeter <span class="math-inline">P₀ = 3 × 1 = 3</span>. Area = <span class="math-inline">A₀</span>.</li>
          <li><strong>Step 1 (First Iteration):</strong>
            <br>1. Divide each side into 3 equal segments of length <span class="math-inline">1/3</span>.
            <br>2. On the middle segment, erect an outward-pointing equilateral triangle of side <span class="math-inline">1/3</span>.
            <br>3. Remove the base of this small triangle.
            <br><em>Effect:</em> Every single straight side is replaced by 4 smaller segments of length <span class="math-inline">1/3</span> (forming a bump shape).
            <br>Number of sides: <span class="math-inline">N₁ = 3 × 4 = 12</span>.
            <br>Side length: <span class="math-inline">L₁ = 1/3</span>.
            <br>Perimeter: <span class="math-inline">P₁ = 12 × (1/3) = 4 = 3 × (4/3)¹</span>.
            <br>Area: 3 small triangles are added, each of area <span class="math-inline">A₀ / 9</span>. So <span class="math-inline">A₁ = A₀ + 3(A₀/9) = A₀ [1 + 1/3]</span>.
          </li>
          <li><strong>Step 2 (Second Iteration):</strong> Replace each of the 12 sides with 4 segments of length <span class="math-inline">1/9</span>.
            <br>Number of sides: <span class="math-inline">N₂ = 12 × 4 = 3 × 4² = 48</span>.
            <br>Side length: <span class="math-inline">L₂ = 1/3² = 1/9</span>.
            <br>Perimeter: <span class="math-inline">P₂ = 48 × (1/9) = 16/3 = 3 × (4/3)² ≈ 5.33</span>.
          </li>
          <li><strong>Step n (General Formula):</strong>
            <div class="math-block">
              Number of Sides: Nₙ = 3 × 4ⁿ &nbsp;&nbsp;|&nbsp;&nbsp; Segment Length: Lₙ = s / 3ⁿ &nbsp;&nbsp;|&nbsp;&nbsp; Perimeter: Pₙ = 3s × (4/3)ⁿ
            </div>
          </li>
        </ul>

        <div class="callout callout-def">
          <div class="callout-title"><i class="fa-solid fa-infinity"></i> The Koch Snowflake Area-Perimeter Miracle</div>
          <p>
            As the number of iterations <span class="math-inline">n → ∞</span>:
            <br>• <strong>Perimeter:</strong> Since <span class="math-inline">4/3 &gt; 1</span>, <span class="math-inline">Pₙ = 3s × (1.333...)ⁿ → ∞</span> (Infinite perimeter!).
            <br>• <strong>Area:</strong> The total area added forms a converging geometric series:
            <span class="math-inline">Aₙ = A₀ [ 1 + (1/3) ∑_{k=1}^n (4/9)^k ]</span>.
            As <span class="math-inline">n → ∞</span>, this sum equals exactly <span class="math-inline">(8/5) A₀ = 1.6 × A₀</span>!
            <br><strong>Conclusion:</strong> The Koch Snowflake has an <strong>infinite perimeter</strong> that encloses a <strong>strictly finite area</strong>! You could fill it with a finite cup of paint, but you could never paint its boundary with a finite paintbrush!
          </p>
        </div>

        <!-- INLINE RESPONSIVE SVG 3: KOCH SNOWFLAKE GENERATION -->
        <div class="svg-graphic-box">
          <svg viewBox="0 0 960 380" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg">
            <rect width="960" height="380" rx="16" fill="#f8fafc" stroke="#e2e8f0" stroke-width="2" />
            <text x="480" y="32" text-anchor="middle" fill="#0f172a" font-family="'Space Grotesk', sans-serif" font-size="17" font-weight="700">Construction of the Koch Snowflake (Infinite Perimeter in Finite Area)</text>

            <!-- Step 0 -->
            <g transform="translate(60, 60)">
              <polygon points="110,30 20,185 200,185" fill="#e0e7ff" stroke="#4f46e5" stroke-width="2.5" />
              <text x="110" y="215" text-anchor="middle" fill="#1e1b4b" font-family="'Space Grotesk', sans-serif" font-size="14" font-weight="700">Step 0 (Triangle)</text>
              <text x="110" y="235" text-anchor="middle" fill="#475569" font-family="'Plus Jakarta Sans', sans-serif" font-size="12">Sides: N₀ = 3</text>
              <text x="110" y="255" text-anchor="middle" fill="#475569" font-family="'JetBrains Mono', monospace" font-size="11">Perimeter: P₀ = 3s</text>
              <text x="110" y="275" text-anchor="middle" fill="#64748b" font-family="'JetBrains Mono', monospace" font-size="11">Area = A₀</text>
            </g>

            <path d="M 300 150 L 335 150" stroke="#94a3b8" stroke-width="2" />
            <text x="318" y="142" text-anchor="middle" fill="#64748b" font-size="10">Add 3 Bumps</text>

            <!-- Step 1 (Star of David base) -->
            <g transform="translate(365, 60)">
              <!-- 12-sided polygon -->
              <polygon points="110,30 140,82 200,82 170,134 200,185 140,185 110,237 80,185 20,185 50,134 20,82 80,82" fill="#c7d2fe" stroke="#4338ca" stroke-width="2.5" />
              <text x="110" y="215" text-anchor="middle" fill="#1e1b4b" font-family="'Space Grotesk', sans-serif" font-size="14" font-weight="700">Step 1 (12 Sides)</text>
              <text x="110" y="235" text-anchor="middle" fill="#475569" font-family="'Plus Jakarta Sans', sans-serif" font-size="12">Sides: N₁ = 12</text>
              <text x="110" y="255" text-anchor="middle" fill="#475569" font-family="'JetBrains Mono', monospace" font-size="11">Perimeter: P₁ = 4s</text>
              <text x="110" y="275" text-anchor="middle" fill="#64748b" font-family="'JetBrains Mono', monospace" font-size="11">Area = 1.33 A₀</text>
            </g>

            <path d="M 605 150 L 640 150" stroke="#94a3b8" stroke-width="2" />
            <text x="622" y="142" text-anchor="middle" fill="#64748b" font-size="10">Add 12 Bumps</text>

            <!-- Step 2 Snowflake schematic -->
            <g transform="translate(670, 60)">
              <circle cx="110" cy="134" r="85" fill="#e0f2fe" stroke="#0284c7" stroke-width="1.5" stroke-dasharray="3,3" />
              <!-- Multi-point schematic snowflake star -->
              <polygon points="110,30 120,60 135,55 130,75 155,70 145,90 175,90 160,110 195,120 170,134 195,148 160,158 175,178 145,178 155,198 130,193 135,213 120,208 110,238 100,208 85,213 90,193 65,198 75,178 45,178 60,158 25,148 50,134 25,120 60,110 45,90 75,90 65,70 90,75 85,55 100,60" fill="#a5b4fc" stroke="#312e81" stroke-width="2" />
              <text x="110" y="215" text-anchor="middle" fill="#1e1b4b" font-family="'Space Grotesk', sans-serif" font-size="14" font-weight="700">Step 2 (48 Sides)</text>
              <text x="110" y="235" text-anchor="middle" fill="#475569" font-family="'Plus Jakarta Sans', sans-serif" font-size="12">Sides: N₂ = 48</text>
              <text x="110" y="255" text-anchor="middle" fill="#475569" font-family="'JetBrains Mono', monospace" font-size="11">Perimeter: P₂ = 5.33s</text>
              <text x="110" y="275" text-anchor="middle" fill="#059669" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="700">Total Area Limit = 1.6 A₀</text>
            </g>

            <!-- Bump Replacement Diagram in Footer -->
            <g transform="translate(180, 310)">
              <rect width="600" height="50" rx="8" fill="#ffffff" stroke="#cbd5e1" stroke-width="1" />
              <text x="20" y="30" fill="#0f172a" font-family="'Plus Jakarta Sans', sans-serif" font-size="12" font-weight="600">The 1-to-4 Bump Rule:</text>
              <!-- Original 1 segment -->
              <line x1="180" y1="28" x2="260" y2="28" stroke="#dc2626" stroke-width="2.5" />
              <text x="220" y="20" text-anchor="middle" fill="#dc2626" font-size="10">Length L</text>
              
              <text x="290" y="32" fill="#64748b" font-size="14">➔</text>
              
              <!-- 4 segments bump -->
              <polyline points="330,28 355,28 367.5,12 380,28 405,28" fill="none" stroke="#059669" stroke-width="2.5" />
              <text x="367.5" y="44" text-anchor="middle" fill="#059669" font-size="10">4 segments of length L/3 (Total = 4L/3)</text>
              <text x="490" y="30" fill="#4f46e5" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="700">Perimeter × 4/3 each step!</text>
            </g>
          </svg>
          <p class="svg-caption"><strong>Figure 2.2:</strong> The Koch Snowflake construction illustrating side multiplication by 4 and segment length reduction by 1/3 at each step.</p>
        </div>
      </div>

      <!-- PART 2.3: FRACTALS IN ART & ARCHITECTURE -->
      <div class="concept-card">
        <h3 class="concept-card-title"><i class="fa-solid fa-gopuram"></i> 2.3 Fractals in Art, Architecture & Culture</h3>
        <p>
          Long before European mathematicians formulated fractal equations in the 20th century, ancient and medieval civilizations intuitively used fractal geometry in monumental architecture, textile weaving, and sacred art.
        </p>

        <h4 style="font-size: 1.15rem; color: var(--primary-dark); margin: 1.25rem 0 0.5rem;"><i class="fa-solid fa-synagogue"></i> A. Ancient Indian Temple Architecture</h4>
        <p>
          The most breathtaking historical expression of fractal geometry on Earth exists in the Hindu and Jain temple architecture of medieval India.
        </p>
        <ul style="margin-left: 1.5rem; margin-bottom: 1rem; line-height: 1.8;">
          <li><strong>Kandariya Mahadev Temple (Khajuraho, Madhya Pradesh, c. 1025 CE):</strong> Built by the Chandela dynasty, this 31-metre high temple dedicated to Shiva exhibits pure fractal morphology. The central mountain-like tower, known as the <em>Shikhara</em>, is surrounded by 84 smaller cascading miniature spires known as <em>Urushringas</em>. Each urushringa is itself a self-similar replica of the central shikhara, and on each urushringa are carved even smaller replicas!</li>
          <li><strong>Spiritual & Philosophical Significance:</strong> In Indian temple philosophy, the temple represents <em>Mount Meru</em> (the cosmic axis) and the infinite universe. It embodies the profound Vedic philosophy of <em>Brahman</em> (the infinite supreme cosmos) and <em>Atman</em> (the individual soul): the infinite whole is contained completely and perfectly within every individual part!</li>
          <li><strong>Other Renowned Fractal Temples:</strong> The soaring Gopurams of the <strong>Meenakshi Amman Temple</strong> in Madurai, the towering vimanas of <strong>Virupaksha Temple</strong> in Hampi (Vijayanagara), the temples of <strong>Puri and Konark</strong> in Odisha with their rekha-deula cluster pinnacles, and the river ghat temples of Varanasi.</li>
        </ul>

        <h4 style="font-size: 1.15rem; color: var(--primary-dark); margin: 1.5rem 0 0.5rem;"><i class="fa-solid fa-rug"></i> B. Traditional African Cultural Fractals</h4>
        <p>
          Ethnomathematicians (such as Ron Eglash) have documented how traditional African societies utilized nested fractal patterns in city layouts, pottery, and textiles:
        </p>
        <ul style="margin-left: 1.5rem; margin-bottom: 1rem; line-height: 1.8;">
          <li><strong>Nigerian Fulani Wedding Blankets:</strong> The nomadic Fulani weavers of West Africa create celebrated wedding blankets adorned with diamond-shaped motifs. Inside each large diamond is woven a smaller diamond, inside of which is woven an even tinier diamond, creating a self-similar recursive hierarchy.</li>
          <li><strong>Village Settlements:</strong> In many Cameroonian and southern African settlements, circular houses are arranged in a circular ring to form a family enclosure, and multiple family enclosures are arranged in a massive circular village ring.</li>
        </ul>

        <h4 style="font-size: 1.15rem; color: var(--primary-dark); margin: 1.5rem 0 0.5rem;"><i class="fa-solid fa-palette"></i> C. M.C. Escher: The Modern Maestro of Fractal Art</h4>
        <p>
          The Dutch graphic artist <strong>M.C. Escher</strong> (1898–1972) bridges the gap between pure mathematics and visual wonder. In works like <em>‘Smaller and Smaller’</em> (1956), Escher created a woodcut where repeating silhouettes of lizards are tiled across a plane such that the lizards become progressively halved in size as they approach the center, packing infinite visual self-similarity into a finite woodcut.
        </p>

        <h4 style="font-size: 1.15rem; color: var(--primary-dark); margin: 1.5rem 0 0.5rem;"><i class="fa-solid fa-scissors"></i> D. Geometric Dissections & Corner Cutting</h4>
        <p>
          When you cut corners from standard 2D shapes, remarkable geometric transformations occur:
        </p>
        <ul style="margin-left: 1.5rem; margin-bottom: 0.5rem; line-height: 1.8;">
          <li><strong>Cutting Square Corners at Midpoints:</strong> If you take a square of side <span class="math-inline">s</span> and slice off all four corners by cutting along segments connecting adjacent edge midpoints, the leftover center shape is a <strong>rotated square (diamond)</strong> of side length <span class="math-inline">s/√2</span> and area <span class="math-inline">A/2</span>! The four severed triangular corners can be reassembled into another identical square of area <span class="math-inline">A/2</span>.</li>
          <li><strong>Cutting Equilateral Triangle at 1/3 Marks:</strong> If each side of an equilateral triangle is divided into thirds and the three corner triangles are cut away, the shape left over is a <strong>regular hexagon</strong>!</li>
          <li><strong>Cutting Square at 1/3 Marks:</strong> If the sides of a square are divided into thirds and the four triangular corners are sliced away, the shape left over is an <strong>octagon</strong> (having 4 long sides and 4 corner sides).</li>
        </ul>
      </div>

      <!-- PART 2.4: VISUALISING SOLIDS & PROFILES -->
      <div class="concept-card">
        <h3 class="concept-card-title"><i class="fa-solid fa-cube"></i> 2.4 Visualising 3D Solids: Profiles & Contrasting Viewpoints</h3>
        <p>
          Every three-dimensional solid occupies volume in physical space. But when light shines on a solid, or when our eyes observe it from a distance, we see its <strong>2D silhouette or profile</strong>. The shape of this profile depends completely on our viewing angle!
        </p>

        <div class="callout callout-def">
          <div class="callout-title"><i class="fa-solid fa-eye"></i> What is a Profile?</div>
          <p>
            A <strong>profile</strong> is the 2D outline of an object as viewed from a specific direction. Imagine an object bursting through a thin sheet of cardboard perpendicularly—the hole it punches in the cardboard has the exact shape of the object’s profile!
          </p>
        </div>

        <p><strong>Contrasting Profiles from Different Viewpoints:</strong></p>
        <div class="data-table-wrapper">
          <table class="data-table">
            <thead>
              <tr>
                <th>Solid Shape</th>
                <th>Viewpoint A Profile</th>
                <th>Viewpoint B Profile</th>
                <th>Why Does This Happen?</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>Cylinder</strong></td>
                <td><strong>Circle</strong> (from top or bottom)</td>
                <td><strong>Rectangle</strong> (from side)</td>
                <td>Circular parallel bases project as a disk; parallel curved wall elements project as straight vertical boundaries.</td>
              </tr>
              <tr>
                <td><strong>Cone</strong></td>
                <td><strong>Circle</strong> (from base)</td>
                <td><strong>Isosceles Triangle</strong> (from side)</td>
                <td>The flat circular base produces a circle; the apex and circular base tangents form an isosceles triangle.</td>
              </tr>
              <tr>
                <td><strong>Triangular Prism</strong></td>
                <td><strong>Triangle</strong> (from ends)</td>
                <td><strong>Rectangle</strong> (from side)</td>
                <td>Two parallel triangular bases yield triangles; the three rectangular lateral faces yield rectangles.</td>
              </tr>
              <tr>
                <td><strong>Frustum of a Cone</strong></td>
                <td><strong>Concentric Circles</strong> (from top/bottom)</td>
                <td><strong>Isosceles Trapezium</strong> (from side)</td>
                <td>A cone sliced parallel to its base has unequal top and bottom circles, creating a trapezoidal silhouette.</td>
              </tr>
              <tr>
                <td><strong>Pentagonal Prism</strong></td>
                <td><strong>Regular Pentagon</strong> (from top/bottom)</td>
                <td><strong>Rectangle</strong> (from side)</td>
                <td>Two congruent pentagonal faces project as pentagons; rectangular walls project as rectangular profiles.</td>
              </tr>
              <tr>
                <td><strong>Sphere</strong></td>
                <td><strong>Circle</strong> (from ANY direction!)</td>
                <td><strong>Circle</strong> (from ANY direction!)</td>
                <td>Due to perfect 3D rotational symmetry, a sphere's profile is invariant—always a circle of radius R.</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>

      <!-- PART 2.5: POLYHEDRA & PLATONIC SOLIDS -->
      <div class="concept-card">
        <h3 class="concept-card-title"><i class="fa-solid fa-gem"></i> 2.5 Polyhedra, Prisms, Pyramids & Platonic Solids</h3>
        <p>
          A solid bounded entirely by flat plane polygonal surfaces is called a <strong>polyhedron</strong> (plural: <em>polyhedra</em>, from Greek <em>poly</em> = many, <em>hedra</em> = seats/faces). Curved shapes like cylinders, cones, and spheres are solids, but they are <strong>not</strong> polyhedra because their boundaries contain curved surfaces.
        </p>

        <p><strong>Structural Elements of a Polyhedron:</strong></p>
        <ul style="margin-left: 1.5rem; margin-bottom: 1rem; line-height: 1.8;">
          <li><strong>Face (F):</strong> Each flat 2D polygonal boundary surface.</li>
          <li><strong>Edge (E):</strong> The straight line segment where two adjacent faces meet.</li>
          <li><strong>Vertex (V):</strong> The sharp corner point where three or more edges intersect.</li>
        </ul>

        <h4 style="font-size: 1.15rem; color: var(--primary-dark); margin: 1.25rem 0 0.5rem;"><i class="fa-solid fa-shapes"></i> Prisms vs Pyramids: Master Formula Bank</h4>
        <div class="data-table-wrapper">
          <table class="data-table">
            <thead>
              <tr>
                <th>Family</th>
                <th>Geometric Definition</th>
                <th>Faces (F)</th>
                <th>Vertices (V)</th>
                <th>Edges (E)</th>
                <th>Euler Verification: F + V - E</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>Prism (n-gon base)</strong></td>
                <td>2 congruent parallel n-gon bases + n rectangular lateral faces</td>
                <td><span class="math-inline">F = n + 2</span></td>
                <td><span class="math-inline">V = 2n</span></td>
                <td><span class="math-inline">E = 3n</span></td>
                <td><span class="math-inline">(n+2) + 2n - 3n = 2</span> (Always 2!)</td>
              </tr>
              <tr>
                <td><strong>Pyramid (n-gon base)</strong></td>
                <td>1 n-gon base + n triangular lateral faces meeting at an apex point</td>
                <td><span class="math-inline">F = n + 1</span></td>
                <td><span class="math-inline">V = n + 1</span></td>
                <td><span class="math-inline">E = 2n</span></td>
                <td><span class="math-inline">(n+1) + (n+1) - 2n = 2</span> (Always 2!)</td>
              </tr>
              <tr>
                <td><strong>Decagonal Prism (n=10)</strong></td>
                <td>10-sided polygon top and bottom + 10 rectangular sides</td>
                <td><span class="math-inline">F = 10 + 2 = 12</span></td>
                <td><span class="math-inline">V = 2(10) = 20</span></td>
                <td><span class="math-inline">E = 3(10) = 30</span></td>
                <td><span class="math-inline">12 + 20 - 30 = 2</span></td>
              </tr>
              <tr>
                <td><strong>Decagonal Pyramid (n=10)</strong></td>
                <td>10-sided polygon base + 10 triangular sides to apex</td>
                <td><span class="math-inline">F = 10 + 1 = 11</span></td>
                <td><span class="math-inline">V = 10 + 1 = 11</span></td>
                <td><span class="math-inline">E = 2(10) = 20</span></td>
                <td><span class="math-inline">11 + 11 - 20 = 2</span></td>
              </tr>
            </tbody>
          </table>
        </div>

        <h4 style="font-size: 1.15rem; color: var(--primary-dark); margin: 1.5rem 0 0.5rem;"><i class="fa-solid fa-dice-d20"></i> The Five Platonic Solids (Regular Polyhedra)</h4>
        <p>
          A polyhedron is called <strong>regular</strong> if all its faces are congruent regular polygons and the same number of faces meet at each vertex. In three-dimensional space, exactly <strong>five</strong> regular convex polyhedra exist:
        </p>
        <ol style="margin-left: 1.5rem; margin-bottom: 0.5rem; line-height: 1.8;">
          <li><strong>Regular Tetrahedron:</strong> 4 faces (all equilateral triangles), 4 vertices, 6 edges. (Has only 2 distinct nets).</li>
          <li><strong>Cube (Regular Hexahedron):</strong> 6 faces (all squares), 8 vertices, 12 edges. (Has exactly 11 distinct nets).</li>
          <li><strong>Regular Octahedron:</strong> 8 faces (all equilateral triangles), 6 vertices, 12 edges. Formed by gluing two square pyramids base-to-base! (Has exactly 11 distinct nets).</li>
          <li><strong>Regular Dodecahedron:</strong> 12 faces (all regular pentagons), 20 vertices, 30 edges. (Mathematicians have proven it has <strong>43,380 distinct nets!</strong>).</li>
          <li><strong>Regular Icosahedron:</strong> 20 faces (all equilateral triangles), 12 vertices, 30 edges. (Has 43,380 distinct nets).</li>
        </ol>
      </div>

      <!-- PART 2.6: FLAT NETS OF SOLIDS -->
      <div class="concept-card">
        <h3 class="concept-card-title"><i class="fa-solid fa-map"></i> 2.6 Flat Nets of 3D Solids</h3>
        <p>
          Manufacturing physical packaging boxes, cartons, architectural ductwork, and spacecraft fairings starts with flat sheet materials.
        </p>

        <div class="callout callout-def">
          <div class="callout-title"><i class="fa-solid fa-box-open"></i> What is a Net?</div>
          <p>
            A <strong>net</strong> is a 2D flat layout of connected polygons that can be folded along their shared edges to perfectly enclose a 3D solid without any overlapping faces or empty gaps. When studying nets mathematically, we consider only the unfolding of the boundary faces, excluding manufacturing glue flaps or adhesive tape tabs.
          </p>
        </div>

        <h4 style="font-size: 1.15rem; color: var(--primary-dark); margin: 1.25rem 0 0.5rem;"><i class="fa-solid fa-cube"></i> The 11 Valid Nets of a Cube</h4>
        <p>
          Out of the 35 possible arrangements of 6 connected squares (hexaminoes), exactly <strong>11 nets</strong> can fold into a closed 3D cube. Any other arrangement will result in faces crashing into each other or leaving an open hole. The 11 nets are classified into 4 structural families:
        </p>
        <ul style="margin-left: 1.5rem; margin-bottom: 1rem; line-height: 1.8;">
          <li><strong>Family 1: "1-4-1" Pattern (6 Nets):</strong> A central row of 4 squares, with 1 square attached to the top row and 1 square attached to the bottom row (e.g., the Latin Cross, T-shape).</li>
          <li><strong>Family 2: "1-3-2" Pattern (3 Nets):</strong> A central row of 3 squares, with 1 square on one side and 2 squares on the other side in a staircase step.</li>
          <li><strong>Family 3: "2-2-2" Pattern (1 Net):</strong> Three rows of 2 squares each, offset like a zigzag staircase.</li>
          <li><strong>Family 4: "3-3" Pattern (1 Net):</strong> Two rows of 3 squares each, offset by 1 square.</li>
        </ul>

        <div class="callout callout-warn">
          <div class="callout-title"><i class="fa-solid fa-ban"></i> Golden Rules to Spot PROHIBITED (Invalid) Cube Nets Instantly</div>
          <p>
            1. <strong>The 2 × 2 Square Cluster Rule:</strong> Any arrangement containing a solid 2 × 2 block of 4 squares can NEVER fold into a cube. Two faces will inevitably overlap, leaving an empty face opposite!
            <br>2. <strong>The 5-in-a-Row Rule:</strong> Any arrangement with 5 or 6 squares in a single straight row can NEVER form a cube (the 5th square wraps over the 1st square).
            <br>3. <strong>The Same-Side Overlap Rule:</strong> In a 1-4-1 structure, if the two single squares are on the SAME side of the 4-in-a-row strip, they will fold up to collide and overlap, leaving the bottom face uncovered!
          </p>
        </div>

        <h4 style="font-size: 1.15rem; color: var(--primary-dark); margin: 1.5rem 0 0.5rem;"><i class="fa-solid fa-earth-americas"></i> Why Can a Sphere NEVER Have a Flat Net?</h4>
        <p>
          Try wrapping a basketball with a single flat sheet of paper. You will quickly discover it is completely impossible without wrinkling, crinkling, tearing, or stretching the paper!
          <br><em>The Mathematical Truth:</em> In 1827, the titan of mathematics <strong>Carl Friedrich Gauss</strong> proved his celebrated <em>Theorema Egregium</em> ("Remarkable Theorem"). He proved that a flat plane has a <strong>zero Gaussian curvature (<span class="math-inline">K = 0</span>)</strong>, while a sphere of radius <span class="math-inline">R</span> has an intrinsic <strong>positive Gaussian curvature (<span class="math-inline">K = 1/R² &gt; 0</span>)</strong>. Because curvature is an intrinsic property that cannot be changed by bending, a sphere can never be flattened onto a 2D plane without distortion. This is the exact reason why all 2D world maps distort continents (e.g., Greenland appears larger than Africa on Mercator projections)!
        </p>

        <!-- INLINE RESPONSIVE SVG 4: THE 11 VALID NETS OF A CUBE -->
        <div class="svg-graphic-box">
          <svg viewBox="0 0 960 480" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg">
            <rect width="960" height="480" rx="16" fill="#f8fafc" stroke="#e2e8f0" stroke-width="2" />
            <text x="480" y="32" text-anchor="middle" fill="#0f172a" font-family="'Space Grotesk', sans-serif" font-size="17" font-weight="700">The 11 Valid Folding Nets of a Cube (Classified by Pattern)</text>

            <!-- GROUP 1: "1-4-1" CLASS (6 Nets) -->
            <g transform="translate(30, 50)">
              <text x="0" y="20" fill="#4f46e5" font-family="'Space Grotesk', sans-serif" font-size="13" font-weight="700">Class 1: "1-4-1" Pattern (6 nets)</text>
              
              <!-- Net 1: T-shape -->
              <g transform="translate(10, 35)">
                <rect x="0" y="20" width="80" height="20" fill="#c7d2fe" stroke="#4f46e5" stroke-width="1.5" />
                <line x1="20" y1="20" x2="20" y2="40" stroke="#4f46e5" stroke-width="1" />
                <line x1="40" y1="20" x2="40" y2="40" stroke="#4f46e5" stroke-width="1" />
                <line x1="60" y1="20" x2="60" y2="40" stroke="#4f46e5" stroke-width="1" />
                <!-- Top flap at pos 1 -->
                <rect x="0" y="0" width="20" height="20" fill="#c7d2fe" stroke="#4f46e5" stroke-width="1.5" />
                <!-- Bottom flap at pos 1 -->
                <rect x="0" y="40" width="20" height="20" fill="#c7d2fe" stroke="#4f46e5" stroke-width="1.5" />
                <text x="40" y="75" text-anchor="middle" fill="#475569" font-size="10">#1 (Pos 1-1)</text>
              </g>

              <!-- Net 2: Latin Cross -->
              <g transform="translate(110, 35)">
                <rect x="0" y="20" width="80" height="20" fill="#c7d2fe" stroke="#4f46e5" stroke-width="1.5" />
                <line x1="20" y1="20" x2="20" y2="40" stroke="#4f46e5" stroke-width="1" />
                <line x1="40" y1="20" x2="40" y2="40" stroke="#4f46e5" stroke-width="1" />
                <line x1="60" y1="20" x2="60" y2="40" stroke="#4f46e5" stroke-width="1" />
                <rect x="20" y="0" width="20" height="20" fill="#c7d2fe" stroke="#4f46e5" stroke-width="1.5" />
                <rect x="20" y="40" width="20" height="20" fill="#c7d2fe" stroke="#4f46e5" stroke-width="1.5" />
                <text x="40" y="75" text-anchor="middle" fill="#475569" font-size="10">#2 (Pos 2-2)</text>
              </g>

              <!-- Net 3: Offset 1 -->
              <g transform="translate(210, 35)">
                <rect x="0" y="20" width="80" height="20" fill="#c7d2fe" stroke="#4f46e5" stroke-width="1.5" />
                <line x1="20" y1="20" x2="20" y2="40" stroke="#4f46e5" stroke-width="1" />
                <line x1="40" y1="20" x2="40" y2="40" stroke="#4f46e5" stroke-width="1" />
                <line x1="60" y1="20" x2="60" y2="40" stroke="#4f46e5" stroke-width="1" />
                <rect x="0" y="0" width="20" height="20" fill="#c7d2fe" stroke="#4f46e5" stroke-width="1.5" />
                <rect x="20" y="40" width="20" height="20" fill="#c7d2fe" stroke="#4f46e5" stroke-width="1.5" />
                <text x="40" y="75" text-anchor="middle" fill="#475569" font-size="10">#3 (Pos 1-2)</text>
              </g>

              <!-- Net 4: Offset 2 -->
              <g transform="translate(310, 35)">
                <rect x="0" y="20" width="80" height="20" fill="#c7d2fe" stroke="#4f46e5" stroke-width="1.5" />
                <line x1="20" y1="20" x2="20" y2="40" stroke="#4f46e5" stroke-width="1" />
                <line x1="40" y1="20" x2="40" y2="40" stroke="#4f46e5" stroke-width="1" />
                <line x1="60" y1="20" x2="60" y2="40" stroke="#4f46e5" stroke-width="1" />
                <rect x="0" y="0" width="20" height="20" fill="#c7d2fe" stroke="#4f46e5" stroke-width="1.5" />
                <rect x="40" y="40" width="20" height="20" fill="#c7d2fe" stroke="#4f46e5" stroke-width="1.5" />
                <text x="40" y="75" text-anchor="middle" fill="#475569" font-size="10">#4 (Pos 1-3)</text>
              </g>

              <!-- Net 5: Offset 3 -->
              <g transform="translate(410, 35)">
                <rect x="0" y="20" width="80" height="20" fill="#c7d2fe" stroke="#4f46e5" stroke-width="1.5" />
                <line x1="20" y1="20" x2="20" y2="40" stroke="#4f46e5" stroke-width="1" />
                <line x1="40" y1="20" x2="40" y2="40" stroke="#4f46e5" stroke-width="1" />
                <line x1="60" y1="20" x2="60" y2="40" stroke="#4f46e5" stroke-width="1" />
                <rect x="0" y="0" width="20" height="20" fill="#c7d2fe" stroke="#4f46e5" stroke-width="1.5" />
                <rect x="60" y="40" width="20" height="20" fill="#c7d2fe" stroke="#4f46e5" stroke-width="1.5" />
                <text x="40" y="75" text-anchor="middle" fill="#475569" font-size="10">#5 (Pos 1-4)</text>
              </g>

              <!-- Net 6: Offset 4 -->
              <g transform="translate(510, 35)">
                <rect x="0" y="20" width="80" height="20" fill="#c7d2fe" stroke="#4f46e5" stroke-width="1.5" />
                <line x1="20" y1="20" x2="20" y2="40" stroke="#4f46e5" stroke-width="1" />
                <line x1="40" y1="20" x2="40" y2="40" stroke="#4f46e5" stroke-width="1" />
                <line x1="60" y1="20" x2="60" y2="40" stroke="#4f46e5" stroke-width="1" />
                <rect x="20" y="0" width="20" height="20" fill="#c7d2fe" stroke="#4f46e5" stroke-width="1.5" />
                <rect x="40" y="40" width="20" height="20" fill="#c7d2fe" stroke="#4f46e5" stroke-width="1.5" />
                <text x="40" y="75" text-anchor="middle" fill="#475569" font-size="10">#6 (Pos 2-3)</text>
              </g>
            </g>

            <!-- GROUP 2: OTHER CLASSES (5 Nets) -->
            <g transform="translate(30, 180)">
              <text x="0" y="20" fill="#0d9488" font-family="'Space Grotesk', sans-serif" font-size="13" font-weight="700">Class 2: "1-3-2" (3 nets) &nbsp;|&nbsp; Class 3: "2-2-2" (1 net) &nbsp;|&nbsp; Class 4: "3-3" (1 net)</text>
              
              <!-- Net 7: 1-3-2 Type A -->
              <g transform="translate(10, 35)">
                <rect x="0" y="0" width="20" height="20" fill="#ccfbf1" stroke="#0d9488" stroke-width="1.5" />
                <rect x="0" y="20" width="60" height="20" fill="#ccfbf1" stroke="#0d9488" stroke-width="1.5" />
                <line x1="20" y1="20" x2="20" y2="40" stroke="#0d9488" stroke-width="1" />
                <line x1="40" y1="20" x2="40" y2="40" stroke="#0d9488" stroke-width="1" />
                <rect x="40" y="40" width="40" height="20" fill="#ccfbf1" stroke="#0d9488" stroke-width="1.5" />
                <line x1="60" y1="40" x2="60" y2="60" stroke="#0d9488" stroke-width="1" />
                <text x="40" y="75" text-anchor="middle" fill="#475569" font-size="10">#7 (1-3-2 A)</text>
              </g>

              <!-- Net 8: 1-3-2 Type B -->
              <g transform="translate(130, 35)">
                <rect x="20" y="0" width="20" height="20" fill="#ccfbf1" stroke="#0d9488" stroke-width="1.5" />
                <rect x="0" y="20" width="60" height="20" fill="#ccfbf1" stroke="#0d9488" stroke-width="1.5" />
                <line x1="20" y1="20" x2="20" y2="40" stroke="#0d9488" stroke-width="1" />
                <line x1="40" y1="20" x2="40" y2="40" stroke="#0d9488" stroke-width="1" />
                <rect x="40" y="40" width="40" height="20" fill="#ccfbf1" stroke="#0d9488" stroke-width="1.5" />
                <line x1="60" y1="40" x2="60" y2="60" stroke="#0d9488" stroke-width="1" />
                <text x="40" y="75" text-anchor="middle" fill="#475569" font-size="10">#8 (1-3-2 B)</text>
              </g>

              <!-- Net 9: 1-3-2 Type C -->
              <g transform="translate(250, 35)">
                <rect x="0" y="0" width="20" height="20" fill="#ccfbf1" stroke="#0d9488" stroke-width="1.5" />
                <rect x="0" y="20" width="60" height="20" fill="#ccfbf1" stroke="#0d9488" stroke-width="1.5" />
                <line x1="20" y1="20" x2="20" y2="40" stroke="#0d9488" stroke-width="1" />
                <line x1="40" y1="20" x2="40" y2="40" stroke="#0d9488" stroke-width="1" />
                <rect x="20" y="40" width="40" height="20" fill="#ccfbf1" stroke="#0d9488" stroke-width="1.5" />
                <line x1="40" y1="40" x2="40" y2="60" stroke="#0d9488" stroke-width="1" />
                <text x="40" y="75" text-anchor="middle" fill="#475569" font-size="10">#9 (1-3-2 C)</text>
              </g>

              <!-- Net 10: 2-2-2 (Staircase) -->
              <g transform="translate(380, 35)">
                <rect x="0" y="0" width="40" height="20" fill="#fef3c7" stroke="#d97706" stroke-width="1.5" />
                <line x1="20" y1="0" x2="20" y2="20" stroke="#d97706" stroke-width="1" />
                <rect x="20" y="20" width="40" height="20" fill="#fef3c7" stroke="#d97706" stroke-width="1.5" />
                <line x1="40" y1="20" x2="40" y2="40" stroke="#d97706" stroke-width="1" />
                <rect x="40" y="40" width="40" height="20" fill="#fef3c7" stroke="#d97706" stroke-width="1.5" />
                <line x1="60" y1="40" x2="60" y2="60" stroke="#d97706" stroke-width="1" />
                <text x="40" y="75" text-anchor="middle" fill="#475569" font-size="10">#10 (2-2-2 Zigzag)</text>
              </g>

              <!-- Net 11: 3-3 (Double Tower) -->
              <g transform="translate(510, 35)">
                <rect x="0" y="0" width="60" height="20" fill="#fce7f3" stroke="#be185d" stroke-width="1.5" />
                <line x1="20" y1="0" x2="20" y2="20" stroke="#be185d" stroke-width="1" />
                <line x1="40" y1="0" x2="40" y2="20" stroke="#be185d" stroke-width="1" />
                <rect x="20" y="20" width="60" height="20" fill="#fce7f3" stroke="#be185d" stroke-width="1.5" />
                <line x1="40" y1="20" x2="40" y2="40" stroke="#be185d" stroke-width="1" />
                <line x1="60" y1="20" x2="60" y2="40" stroke="#be185d" stroke-width="1" />
                <text x="40" y="75" text-anchor="middle" fill="#475569" font-size="10">#11 (3-3 Double)</text>
              </g>
            </g>

            <!-- GROUP 3: PROHIBITED NETS (TRAPS) -->
            <g transform="translate(30, 320)">
              <rect width="900" height="135" rx="10" fill="#fef2f2" stroke="#fecaca" stroke-width="1.5" />
              <text x="20" y="28" fill="#dc2626" font-family="'Space Grotesk', sans-serif" font-size="14" font-weight="700">🚫 COMMON PROHIBITED PATTERNS (CANNOT FOLD INTO A CUBE):</text>
              
              <!-- Bad Pattern A: 2x2 Block -->
              <g transform="translate(40, 45)">
                <rect x="0" y="0" width="40" height="40" fill="#fee2e2" stroke="#dc2626" stroke-width="1.5" />
                <line x1="20" y1="0" x2="20" y2="40" stroke="#dc2626" stroke-width="1" />
                <line x1="0" y1="20" x2="40" y2="20" stroke="#dc2626" stroke-width="1" />
                <rect x="40" y="0" width="40" height="20" fill="#fee2e2" stroke="#dc2626" stroke-width="1.5" />
                <line x1="60" y1="0" x2="60" y2="20" stroke="#dc2626" stroke-width="1" />
                <!-- Red Cross -->
                <line x1="-5" y1="-5" x2="85" y2="45" stroke="#dc2626" stroke-width="3" opacity="0.8" />
                <text x="40" y="60" text-anchor="middle" fill="#991b1b" font-size="10" font-weight="700">2×2 Block (Faces Collide)</text>
              </g>

              <!-- Bad Pattern B: 5 in a row -->
              <g transform="translate(260, 45)">
                <rect x="0" y="0" width="100" height="20" fill="#fee2e2" stroke="#dc2626" stroke-width="1.5" />
                <line x1="20" y1="0" x2="20" y2="20" stroke="#dc2626" stroke-width="1" />
                <line x1="40" y1="0" x2="40" y2="20" stroke="#dc2626" stroke-width="1" />
                <line x1="60" y1="0" x2="60" y2="20" stroke="#dc2626" stroke-width="1" />
                <line x1="80" y1="0" x2="80" y2="20" stroke="#dc2626" stroke-width="1" />
                <rect x="40" y="20" width="20" height="20" fill="#fee2e2" stroke="#dc2626" stroke-width="1.5" />
                <line x1="-5" y1="-5" x2="105" y2="45" stroke="#dc2626" stroke-width="3" opacity="0.8" />
                <text x="50" y="60" text-anchor="middle" fill="#991b1b" font-size="10" font-weight="700">5 in a Row (Overlaps 1st)</text>
              </g>

              <!-- Bad Pattern C: Flaps on same side -->
              <g transform="translate(520, 45)">
                <rect x="0" y="20" width="80" height="20" fill="#fee2e2" stroke="#dc2626" stroke-width="1.5" />
                <line x1="20" y1="20" x2="20" y2="40" stroke="#dc2626" stroke-width="1" />
                <line x1="40" y1="20" x2="40" y2="40" stroke="#dc2626" stroke-width="1" />
                <line x1="60" y1="20" x2="60" y2="40" stroke="#dc2626" stroke-width="1" />
                <rect x="0" y="0" width="20" height="20" fill="#fee2e2" stroke="#dc2626" stroke-width="1.5" />
                <rect x="40" y="0" width="20" height="20" fill="#fee2e2" stroke="#dc2626" stroke-width="1.5" />
                <line x1="-5" y1="-5" x2="85" y2="45" stroke="#dc2626" stroke-width="3" opacity="0.8" />
                <text x="40" y="60" text-anchor="middle" fill="#991b1b" font-size="10" font-weight="700">Both Flaps on Top (Bottom Open)</text>
              </g>
            </g>
          </svg>
          <p class="svg-caption"><strong>Figure 2.3:</strong> Complete taxonomy of all 11 valid cube nets and the 3 fatal prohibited configurations.</p>
        </div>
      </div>

      <!-- PART 2.7: SURFACE GEODESICS (ANT & LADDU) -->
      <div class="concept-card">
        <h3 class="concept-card-title"><i class="fa-solid fa-route"></i> 2.7 Surface Geodesics: Shortest Paths on 3D Polyhedra</h3>
        <p>
          On a flat plane, the shortest distance between two points is a straight line segment. But what is the shortest path between two points on the surface of a three-dimensional solid (like a cuboid), if a tiny insect is constrained to walk strictly along the exterior surface? Such shortest paths along surfaces are called <strong>geodesics</strong>.
        </p>

        <div class="callout callout-def">
          <div class="callout-title"><i class="fa-solid fa-compass"></i> The Unfolding Geodesic Theorem</div>
          <p>
            Any continuous path along the faces of a polyhedron transforms into a path of the <strong>exact same length</strong> when the traversed faces are unfolded flat onto a 2D plane! Therefore, to find the shortest path between two points on a cuboid:
            <br>1. Unfold the adjacent faces along their shared hinge edge onto a single flat 2D plane.
            <br>2. Draw a straight line between the start point and the end point on the unfolded net.
            <br>3. Compute the straight-line length using the <strong>Baudhāyana-Pythagoras Theorem</strong>: <span class="math-inline">d = √(Δx² + Δy²)</span>.
            <br>4. <em>Crucial Guardrail:</em> Check that the straight line stays strictly inside the unfolded faces! If it cuts across empty air outside the net, that unfolding is invalid and an alternative unfolding path must be chosen!
          </p>
        </div>

        <h4 style="font-size: 1.15rem; color: var(--primary-dark); margin: 1.5rem 0 0.5rem;"><i class="fa-solid fa-bug"></i> The Master Challenge: Ant & Laddu on a 30 cm × 12 cm × 12 cm Cuboid</h4>
        <p>
          Consider the famous puzzle from page 87 of Ganita Prakash: A closed room/box has length = 30 cm, width = 12 cm, and height = 12 cm.
          <br>• An ant is sitting on one end wall (12 cm × 12 cm), exactly 1 cm from the ceiling and midway between the side walls (6 cm from each side).
          <br>• A sweet laddu is stuck to the opposite end wall, exactly 1 cm from the floor and midway between the side walls (6 cm from each side).
          <br>What is the shortest crawling distance for the ant to reach the laddu?
        </p>

        <p>Because the box has 6 faces, there are three primary ways the ant can navigate across the intermediate faces:</p>
        <ul style="margin-left: 1.5rem; margin-bottom: 1rem; line-height: 1.8;">
          <li><strong>Option A (Crawling via Ceiling and Far Wall):</strong>
            <br>The ant climbs 1 cm up to the ceiling, walks 30 cm along the ceiling, and crawls 11 cm down the opposite wall.
            <br>Unfolded horizontal span = <span class="math-inline">1 + 30 + 11 = 42 cm</span>.
            <br>Lateral offset = 0 cm (both are centered horizontally). But if it deviates laterally: <span class="math-inline">d = 42 cm</span>.
          </li>
          <li><strong>Option B (Crawling via End Wall ➔ Side Wall ➔ Opposite End Wall):</strong>
            <br>The ant walks across the side wall! Unfolding the start wall, side wall, and destination wall into a flat strip:
            <br>Horizontal distance: from center of start wall to edge is 6 cm; length of side wall is 30 cm; from edge of destination wall to center is 6 cm.
            <br>Total horizontal span = <span class="math-inline">6 + 30 + 6 = 42 cm</span>.
            <br>Vertical distance: ant starts 11 cm above floor; laddu is 1 cm above floor. Vertical difference = <span class="math-inline">11 - 1 = 10 cm</span>.
            <br>Diagonal distance = <span class="math-inline">√(42² + 10²) = √(1764 + 100) = √1864 ≈ 43.17 cm</span>.
          </li>
          <li><strong>Option C (The Brilliant Diagonal Spiral via End ➔ Ceiling ➔ Side ➔ Floor):</strong>
            <br>When the cuboid is unfolded so that the faces form a 5-face spiral cross (as shown on textbook page 87):
            <br>One leg of the right triangle = <span class="math-inline">1 + 12 + 12 - 1 = 24 cm</span>!
            <br>The other leg of the right triangle = <span class="math-inline">6 + 30 - 4 = 32 cm</span>!
            <br>Applying Baudhāyana-Pythagoras:
            <div class="math-block">
              d² = 24² + 32² = 576 + 1024 = 1600 &nbsp;&nbsp;⇒&nbsp;&nbsp; d = √1600 = 40.0 cm!
            </div>
            <p><strong>Victory:</strong> 40 cm is strictly shorter than 42 cm or 43.17 cm! By traversing five faces in a helical wrap, the ant saves 2 full centimeters!</p>
          </li>
        </ul>

        <!-- INLINE RESPONSIVE SVG 5: ANT & LADDU GEODESIC UNFOLDING -->
        <div class="svg-graphic-box">
          <svg viewBox="0 0 960 400" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg">
            <rect width="960" height="400" rx="16" fill="#f8fafc" stroke="#e2e8f0" stroke-width="2" />
            <text x="480" y="32" text-anchor="middle" fill="#0f172a" font-family="'Space Grotesk', sans-serif" font-size="17" font-weight="700">Surface Geodesic on a Cuboid: Unfolding Analysis of the 40 cm Shortest Path</text>

            <!-- 3D Perspective Box (Left) -->
            <g transform="translate(60, 70)">
              <text x="110" y="20" text-anchor="middle" fill="#4f46e5" font-family="'Space Grotesk', sans-serif" font-size="14" font-weight="700">3D Cuboid (30 × 12 × 12 cm)</text>
              
              <!-- Front Face (12 x 12) -->
              <rect x="30" y="100" width="70" height="70" fill="#e0e7ff" stroke="#4f46e5" stroke-width="2" />
              <!-- Top Face -->
              <polygon points="30,100 130,40 200,40 100,100" fill="#c7d2fe" stroke="#4f46e5" stroke-width="2" />
              <!-- Side Face (30 x 12) -->
              <polygon points="100,100 200,40 200,110 100,170" fill="#a5b4fc" stroke="#4f46e5" stroke-width="2" />

              <!-- Ant marker -->
              <circle cx="65" cy="110" r="5" fill="#dc2626" />
              <text x="65" y="95" text-anchor="middle" fill="#dc2626" font-family="'Plus Jakarta Sans', sans-serif" font-size="11" font-weight="700">🐜 Ant (1cm from top)</text>

              <!-- Laddu marker (ghosted back) -->
              <circle cx="165" cy="100" r="5" fill="#d97706" />
              <text x="175" y="125" text-anchor="middle" fill="#d97706" font-family="'Plus Jakarta Sans', sans-serif" font-size="11" font-weight="700">🍬 Laddu (far wall)</text>

              <!-- Dimensions -->
              <text x="65" y="185" text-anchor="middle" fill="#64748b" font-size="11">12 cm</text>
              <text x="160" y="150" text-anchor="middle" fill="#64748b" font-size="11">30 cm</text>
              <text x="15" y="140" fill="#64748b" font-size="11">12 cm</text>
            </g>

            <!-- Unfolded Flat Net (Right) -->
            <g transform="translate(380, 60)">
              <text x="270" y="20" text-anchor="middle" fill="#059669" font-family="'Space Grotesk', sans-serif" font-size="14" font-weight="700">Flat 2D Net Unfolding (Right Triangle 24 × 32 cm)</text>
              
              <!-- Grid background representing unfolded faces -->
              <!-- End Face 1 -->
              <rect x="40" y="140" width="60" height="60" fill="#e0e7ff" stroke="#6366f1" stroke-width="1.5" />
              <!-- Side Face 1 -->
              <rect x="100" y="140" width="160" height="60" fill="#c7d2fe" stroke="#6366f1" stroke-width="1.5" />
              <!-- Floor Face -->
              <rect x="100" y="200" width="160" height="60" fill="#e0e7ff" stroke="#6366f1" stroke-width="1.5" />
              <!-- End Face 2 (shifted) -->
              <rect x="260" y="80" width="60" height="60" fill="#e0e7ff" stroke="#6366f1" stroke-width="1.5" />
              <!-- Top Face -->
              <rect x="100" y="80" width="160" height="60" fill="#ede9fe" stroke="#6366f1" stroke-width="1.5" />

              <!-- Ant at (70, 145) -->
              <circle cx="70" cy="145" r="5" fill="#dc2626" />
              <text x="50" y="135" fill="#dc2626" font-size="10" font-weight="700">Ant (A)</text>

              <!-- Laddu at (290, 85) -->
              <circle cx="290" cy="85" r="5" fill="#d97706" />
              <text x="300" y="80" fill="#d97706" font-size="10" font-weight="700">Laddu (L)</text>

              <!-- Shortest Line Segment in RED -->
              <line x1="70" y1="145" x2="290" y2="85" stroke="#dc2626" stroke-width="3" stroke-dasharray="6,3" />

              <!-- Pythagorean Right Triangle Triangle Construction -->
              <!-- Horizontal leg: 32 cm -->
              <line x1="70" y1="145" x2="290" y2="145" stroke="#059669" stroke-width="2" />
              <!-- Vertical leg: 24 cm -->
              <line x1="290" y1="145" x2="290" y2="85" stroke="#059669" stroke-width="2" />

              <text x="180" y="165" text-anchor="middle" fill="#059669" font-family="'JetBrains Mono', monospace" font-size="12" font-weight="700">Horizontal Leg = 32 cm</text>
              <text x="310" y="120" fill="#059669" font-family="'JetBrains Mono', monospace" font-size="12" font-weight="700">Vertical = 24 cm</text>

              <!-- Formula Box -->
              <g transform="translate(110, 275)">
                <rect width="320" height="45" rx="8" fill="#ecfdf5" stroke="#a7f3d0" stroke-width="1.5" />
                <text x="160" y="22" text-anchor="middle" fill="#065f46" font-family="'Space Grotesk', sans-serif" font-size="12" font-weight="700">Baudhāyana Theorem Verification:</text>
                <text x="160" y="38" text-anchor="middle" fill="#047857" font-family="'JetBrains Mono', monospace" font-size="12" font-weight="800">d = √(32² + 24²) = √(1024 + 576) = √1600 = 40 cm</text>
              </g>
            </g>
          </svg>
          <p class="svg-caption"><strong>Figure 2.4:</strong> Transformation of a 3D surface traversal into a 2D Euclidean straight line on an unfolded cuboid net, proving the 40 cm geodesic minimum.</p>
        </div>
      </div>

      <!-- PART 2.8: ORTHOGRAPHIC PROJECTIONS -->
      <div class="concept-card">
        <h3 class="concept-card-title"><i class="fa-solid fa-drafting-compass"></i> 2.8 Orthographic Projections: Front, Top & Side Views</h3>
        <p>
          In engineering, architecture, and manufacturing, 3D objects must be drafted on 2D paper with absolute precision. This is accomplished using <strong>orthographic projections</strong>.
        </p>

        <div class="callout callout-def">
          <div class="callout-title"><i class="fa-solid fa-arrows-to-dot"></i> What is an Orthographic Projection?</div>
          <p>
            An <strong>orthographic projection</strong> is a parallel projection in which the projection rays are perpendicular (at 90°) to the plane of projection. The projection of a point <span class="math-inline">P</span> onto a plane <span class="math-inline">M</span> is the point <span class="math-inline">O</span> where the perpendicular line from <span class="math-inline">P</span> strikes <span class="math-inline">M</span>. The collection of all projected points forms the 2D projection of the object.
          </p>
        </div>

        <h4 style="font-size: 1.15rem; color: var(--primary-dark); margin: 1.25rem 0 0.5rem;"><i class="fa-solid fa-ruler"></i> The Length of a Projected Line Segment</h4>
        <p>
          Let a straight line segment have actual length <span class="math-inline">l</span> in space, and let <span class="math-inline">p</span> be the length of its projection on a plane:
        </p>
        <ul style="margin-left: 1.5rem; margin-bottom: 1rem; line-height: 1.8;">
          <li><strong>Case 1 (Line Parallel to Plane):</strong> The projection has the exact same length as the original line segment: <span class="math-inline">p = l</span>.</li>
          <li><strong>Case 2 (Line Tilted at an Angle θ):</strong> By dropping perpendiculars, we form a right triangle where <span class="math-inline">p = l × cos θ</span>. Since <span class="math-inline">cos θ ≤ 1</span>, the projected length is always <strong>less than or equal to</strong> the true length (<span class="math-inline">p ≤ l</span>).</li>
          <li><strong>Case 3 (Line Perpendicular to Plane, θ = 90°):</strong> All points of the segment project onto the exact same single point! The projected length is <span class="math-inline">p = 0</span>.</li>
          <li><strong>Universal Law:</strong> For any line segment in space, its projected length satisfies:
            <div class="math-block">0 ≤ p ≤ l</div>
          </li>
        </ul>

        <h4 style="font-size: 1.15rem; color: var(--primary-dark); margin: 1.5rem 0 0.5rem;"><i class="fa-solid fa-sun"></i> The Sunlight vs Torchlight Principle</h4>
        <p>
          When you hold an object in front of a wall and shine a flashlight/torch on it, the light originates from a point source. The light rays diverge outwards, casting a shadow that is <strong>magnified, stretched, and perspective-distorted</strong>.
          <br>However, the <strong>Sun</strong> is located approximately 150 million kilometers away! Because of this immense distance, sunlight rays reaching Earth are effectively <strong>perfectly parallel</strong>. Therefore, when sunlight strikes a plane at 90°, the shadow cast by an object is identical to its true <strong>orthographic projection</strong>!
          <br><em>Crucial Invariance:</em> Under parallel projection, <strong>parallel lines always project to parallel lines</strong> (or collapse into a single line or point). This guarantees that a square can project into a rectangle, a line, or a parallelogram, but it can <strong>never</strong> project into a trapezium with non-parallel sides!
        </p>

        <h4 style="font-size: 1.15rem; color: var(--primary-dark); margin: 1.5rem 0 0.5rem;"><i class="fa-solid fa-cubes-stacked"></i> The Three Principal Orthographic Views</h4>
        <p>
          Because a single 2D projection loses depth information, engineers and architects always record <strong>three mutually perpendicular views</strong>:
        </p>
        <ul style="margin-left: 1.5rem; margin-bottom: 1rem; line-height: 1.8;">
          <li><strong>1. Front View (Elevation):</strong> The projection onto the <strong>Vertical Plane</strong> located behind the object, viewed straight from the front. Captures <em>Length</em> and <em>Height</em>.</li>
          <li><strong>2. Top View (Plan):</strong> The projection onto the <strong>Horizontal Plane</strong> located underneath the object, viewed directly from above. Captures <em>Length</em> and <em>Depth</em>.</li>
          <li><strong>3. Side View (Profile / End Elevation):</strong> The projection onto the <strong>Side Profile Plane</strong>, viewed from the left or right. Captures <em>Depth</em> and <em>Height</em>.</li>
        </ul>

        <!-- INLINE RESPONSIVE SVG 6: ORTHOGRAPHIC PROJECTIONS -->
        <div class="svg-graphic-box">
          <svg viewBox="0 0 960 420" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg">
            <rect width="960" height="420" rx="16" fill="#f8fafc" stroke="#e2e8f0" stroke-width="2" />
            <text x="480" y="32" text-anchor="middle" fill="#0f172a" font-family="'Space Grotesk', sans-serif" font-size="17" font-weight="700">Orthographic Projections: Front, Top & Side Views of a Stepped Cube Block</text>

            <!-- 3D Object in Space (Left) -->
            <g transform="translate(60, 70)">
              <text x="120" y="20" text-anchor="middle" fill="#4f46e5" font-family="'Space Grotesk', sans-serif" font-size="14" font-weight="700">3D Stepped Block</text>
              
              <!-- Draw 3-cube L-shape in isometric/oblique 3D -->
              <!-- Cube 1 (Bottom Left) -->
              <polygon points="50,150 90,130 90,170 50,190" fill="#a5b4fc" stroke="#3730a3" stroke-width="1.5" />
              <polygon points="50,150 90,130 130,150 90,170" fill="#e0e7ff" stroke="#3730a3" stroke-width="1.5" />
              <polygon points="90,170 130,150 130,190 90,210" fill="#818cf8" stroke="#3730a3" stroke-width="1.5" />

              <!-- Cube 2 (Bottom Right) -->
              <polygon points="130,150 170,130 170,170 130,190" fill="#a5b4fc" stroke="#3730a3" stroke-width="1.5" />
              <polygon points="130,150 170,130 210,150 170,170" fill="#e0e7ff" stroke="#3730a3" stroke-width="1.5" />
              <polygon points="170,170 210,150 210,190 170,210" fill="#818cf8" stroke="#3730a3" stroke-width="1.5" />

              <!-- Cube 3 (Top Left - stacked on Cube 1) -->
              <polygon points="50,110 90,90 90,130 50,150" fill="#a5b4fc" stroke="#3730a3" stroke-width="1.5" />
              <polygon points="50,110 90,90 130,110 90,130" fill="#e0e7ff" stroke="#3730a3" stroke-width="1.5" />
              <polygon points="90,130 130,110 130,150 90,170" fill="#818cf8" stroke="#3730a3" stroke-width="1.5" />

              <!-- Directional Sight Arrows -->
              <!-- Front View Arrow -->
              <path d="M 40 230 L 70 200" stroke="#dc2626" stroke-width="2.5" marker-end="url(#arrow)" />
              <text x="25" y="245" fill="#dc2626" font-size="11" font-weight="700">FRONT ➔</text>

              <!-- Top View Arrow -->
              <path d="M 90 40 L 90 70" stroke="#059669" stroke-width="2.5" />
              <text x="90" y="30" text-anchor="middle" fill="#059669" font-size="11" font-weight="700">TOP ↓</text>

              <!-- Side View Arrow -->
              <path d="M 230 200 L 205 185" stroke="#0891b2" stroke-width="2.5" />
              <text x="240" y="215" fill="#0891b2" font-size="11" font-weight="700">SIDE ⬅</text>
            </g>

            <!-- Orthographic Views (Right Side) -->
            <g transform="translate(400, 70)">
              <!-- Vertical and Horizontal Reference Planes Crosshair -->
              <line x1="20" y1="160" x2="520" y2="160" stroke="#cbd5e1" stroke-width="2" stroke-dasharray="4,4" />
              <line x1="260" y1="20" x2="260" y2="310" stroke="#cbd5e1" stroke-width="2" stroke-dasharray="4,4" />

              <!-- Quadrant 2: FRONT VIEW (Top Left) -->
              <g transform="translate(80, 40)">
                <rect width="100" height="100" rx="4" fill="#ffffff" stroke="#e2e8f0" stroke-width="1" />
                <text x="50" y="-10" text-anchor="middle" fill="#dc2626" font-family="'Space Grotesk', sans-serif" font-size="13" font-weight="700">FRONT VIEW (Elevation)</text>
                <!-- L-shape: 2 high on left, 1 high on right -->
                <rect x="10" y="10" width="40" height="40" fill="#fee2e2" stroke="#dc2626" stroke-width="2" />
                <rect x="10" y="50" width="40" height="40" fill="#fee2e2" stroke="#dc2626" stroke-width="2" />
                <rect x="50" y="50" width="40" height="40" fill="#fee2e2" stroke="#dc2626" stroke-width="2" />
                <text x="50" y="115" text-anchor="middle" fill="#64748b" font-size="10">2 Columns (H=2, H=1)</text>
              </g>

              <!-- Quadrant 3: TOP VIEW (Bottom Left, directly below Front) -->
              <g transform="translate(80, 180)">
                <rect width="100" height="100" rx="4" fill="#ffffff" stroke="#e2e8f0" stroke-width="1" />
                <text x="50" y="-10" text-anchor="middle" fill="#059669" font-family="'Space Grotesk', sans-serif" font-size="13" font-weight="700">TOP VIEW (Plan)</text>
                <!-- Top view: 1 row of 2 cubes -->
                <rect x="10" y="30" width="40" height="40" fill="#d1fae5" stroke="#059669" stroke-width="2" />
                <rect x="50" y="30" width="40" height="40" fill="#d1fae5" stroke="#059669" stroke-width="2" />
                <text x="50" y="115" text-anchor="middle" fill="#64748b" font-size="10">1 Row of 2 Squares</text>
              </g>

              <!-- Quadrant 1: SIDE VIEW (Top Right, beside Front) -->
              <g transform="translate(340, 40)">
                <rect width="100" height="100" rx="4" fill="#ffffff" stroke="#e2e8f0" stroke-width="1" />
                <text x="50" y="-10" text-anchor="middle" fill="#0891b2" font-family="'Space Grotesk', sans-serif" font-size="13" font-weight="700">SIDE VIEW (Profile)</text>
                <!-- Side view: 1 column of 2 cubes high -->
                <rect x="30" y="10" width="40" height="40" fill="#cffafe" stroke="#0891b2" stroke-width="2" />
                <rect x="30" y="50" width="40" height="40" fill="#cffafe" stroke="#0891b2" stroke-width="2" />
                <text x="50" y="115" text-anchor="middle" fill="#64748b" font-size="10">1 Column of 2 Squares</text>
              </g>
            </g>
          </svg>
          <p class="svg-caption"><strong>Figure 2.5:</strong> Orthographic projection system showing how Front View (Elevation), Top View (Plan), and Side View (Profile) completely capture 3D geometry on 2D planes.</p>
        </div>
      </div>

      <!-- PART 2.9: ISOMETRIC PROJECTIONS & OPTICAL ILLUSIONS -->
      <div class="concept-card">
        <h3 class="concept-card-title"><i class="fa-solid fa-cubes"></i> 2.9 Isometric Projections & The Mystery of Optical Illusions</h3>
        <p>
          While orthographic projections require three separate 2D drawings (front, top, side), <strong>isometric projection</strong> allows engineers and artists to draw a single 2D image that creates an instant, measurable 3D representation!
        </p>

        <div class="callout callout-def">
          <div class="callout-title"><i class="fa-solid fa-shapes"></i> What is an Isometric Projection?</div>
          <p>
            Derived from the Greek words <em>isos</em> (equal) and <em>metron</em> (measure), <strong>isometric</strong> means ‘equal measure’. In an isometric drawing:
            <br>• The solid is tilted such that its three coordinate axes (length, depth, height) make equal angles of <strong>120° with each other</strong>.
            <br>• Distances along all three axes are drawn to the <strong>same true scale</strong>!
            <br>• Vertical lines represent the <strong>height axis (|)</strong>, while lines tilted at 30° above the horizontal to the right represent <strong>length</strong>, and lines tilted at 30° to the left represent <strong>depth</strong>.
          </p>
        </div>

        <h4 style="font-size: 1.15rem; color: var(--primary-dark); margin: 1.25rem 0 0.5rem;"><i class="fa-solid fa-cube"></i> Balancing a Cube on a Single Vertex</h4>
        <p>
          Imagine balancing a solid cube perfectly on one of its corner vertices so that its long internal body diagonal is vertical. If you look straight down from above, the silhouette of the cube is a <strong>regular hexagon</strong>! The vertex facing you becomes the center of the hexagon, and three internal edges radiate outwards to three of the vertices at 120° angles, dividing the hexagon into three congruent rhombuses (the top, front-left, and front-right faces of the cube). This hexagonal tiling forms the geometric basis of <strong>isometric dot paper</strong>!
        </p>

        <h4 style="font-size: 1.15rem; color: var(--primary-dark); margin: 1.5rem 0 0.5rem;"><i class="fa-solid fa-eye-slash"></i> The Impossible Penrose Triangle & Why the Illusion Works</h4>
        <p>
          The <strong>Penrose Triangle</strong> (also known as the <em>Impossible Tribar</em>) was devised by Swedish artist Oscar Reutersvärd in 1934 and independently popularized by mathematician <strong>Roger Penrose</strong> and artist <strong>M.C. Escher</strong> (in famous prints such as <em>Waterfall</em> and <em>Ascending and Descending</em>).
        </p>
        <ul style="margin-left: 1.5rem; margin-bottom: 1rem; line-height: 1.8;">
          <li><strong>What Makes it Impossible?</strong> On paper, it depicts three straight beams of square cross-section joined at right angles (90°) at their vertices, forming a closed triangle! In Euclidean 3D space, the sum of angles of a triangle is 180°. A triangle cannot possibly have three 90° angles (<span class="math-inline">90° + 90° + 90° = 270°</span>)!</li>
          <li><strong>Why Does the Brain Fall for It?</strong>
            <br>1. <strong>Local Consistency:</strong> Every single corner, taken in isolation, is completely realistic and obeys standard 90° perspective rules.
            <br>2. <strong>Lack of Vanishing Points:</strong> Isometric drawings use parallel projection without vanishing points. Parallel lines do not converge with distance. Therefore, the brain has no depth cues to realize that the ends of the beams do not actually meet in 3D space—one end is actually much closer to the viewer than the other!
            <br>3. <strong>Forced Closure:</strong> When the artist draws the two disconnected ends touching each other on the 2D page, the visual cortex involuntarily forces a 3D interpretation, creating a mesmerizing impossibility!
          </li>
        </ul>

        <!-- INLINE RESPONSIVE SVG 7: ISOMETRIC GRID & THE PENROSE TRIANGLE -->
        <div class="svg-graphic-box">
          <svg viewBox="0 0 960 420" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg">
            <rect width="960" height="420" rx="16" fill="#f8fafc" stroke="#e2e8f0" stroke-width="2" />
            <text x="480" y="32" text-anchor="middle" fill="#0f172a" font-family="'Space Grotesk', sans-serif" font-size="17" font-weight="700">Isometric Coordinate System (120° Spacing) & The Impossible Penrose Triangle</text>

            <!-- Coordinate Axes Diagram (Left) -->
            <g transform="translate(60, 60)">
              <text x="120" y="20" text-anchor="middle" fill="#4f46e5" font-family="'Space Grotesk', sans-serif" font-size="14" font-weight="700">The 3 Isometric Axes (120° Apart)</text>
              
              <!-- Center Hub -->
              <circle cx="120" cy="160" r="6" fill="#4f46e5" />
              
              <!-- Height Axis (Vertical Up) -->
              <line x1="120" y1="160" x2="120" y2="50" stroke="#4f46e5" stroke-width="3" />
              <text x="120" y="40" text-anchor="middle" fill="#4f46e5" font-family="'Space Grotesk', sans-serif" font-size="12" font-weight="700">Height (|) 90°</text>

              <!-- Length Axis (30 deg above horizontal to Right, 120 from Height) -->
              <line x1="120" y1="160" x2="215" y2="215" stroke="#059669" stroke-width="3" />
              <text x="220" y="235" text-anchor="middle" fill="#059669" font-family="'Space Grotesk', sans-serif" font-size="12" font-weight="700">Length (/) 30°</text>

              <!-- Depth Axis (30 deg above horizontal to Left, 120 from Height) -->
              <line x1="120" y1="160" x2="25" y2="215" stroke="#d97706" stroke-width="3" />
              <text x="25" y="235" text-anchor="middle" fill="#d97706" font-family="'Space Grotesk', sans-serif" font-size="12" font-weight="700">Depth (&#92;) 150°</text>

              <!-- Angle arcs -->
              <path d="M 120 120 A 40 40 0 0 1 155 180" fill="none" stroke="#64748b" stroke-width="1.5" stroke-dasharray="3,3" />
              <text x="155" y="145" fill="#64748b" font-size="10">120°</text>

              <path d="M 85 180 A 40 40 0 0 1 120 120" fill="none" stroke="#64748b" stroke-width="1.5" stroke-dasharray="3,3" />
              <text x="75" y="145" fill="#64748b" font-size="10">120°</text>

              <path d="M 155 180 A 40 40 0 0 1 85 180" fill="none" stroke="#64748b" stroke-width="1.5" stroke-dasharray="3,3" />
              <text x="120" y="210" text-anchor="middle" fill="#64748b" font-size="10">120°</text>

              <!-- Explanatory pill -->
              <rect x="20" y="270" width="200" height="50" rx="6" fill="#eef2ff" stroke="#c7d2fe" stroke-width="1" />
              <text x="120" y="290" text-anchor="middle" fill="#3730a3" font-size="11" font-weight="700">All 3 Axes Equal True Scale</text>
              <text x="120" y="308" text-anchor="middle" fill="#4338ca" font-size="10">No perspective foreshortening!</text>
            </g>

            <!-- Divider -->
            <line x1="320" y1="60" x2="320" y2="380" stroke="#e2e8f0" stroke-width="1.5" />

            <!-- The Impossible Penrose Triangle (Right) -->
            <g transform="translate(360, 60)">
              <text x="270" y="20" text-anchor="middle" fill="#dc2626" font-family="'Space Grotesk', sans-serif" font-size="14" font-weight="700">The Impossible Penrose Tribar</text>
              
              <!-- Draw Penrose Triangle using 3-color shaded isometric facets -->
              <g transform="translate(140, 40)">
                <!-- Face 1 (Light / Top faces) -->
                <polygon points="120,20 145,35 65,175 40,160" fill="#e0e7ff" stroke="#312e81" stroke-width="1.5" />
                <polygon points="40,160 65,175 185,175 185,145 90,145 120,95" fill="#a5b4fc" stroke="#312e81" stroke-width="1.5" />
                <polygon points="120,20 120,50 185,145 210,130" fill="#6366f1" stroke="#312e81" stroke-width="1.5" />
                
                <!-- Inner facets that create the optical contradiction -->
                <polygon points="120,50 145,65 95,145 70,145" fill="#4338ca" stroke="#312e81" stroke-width="1.5" />
                <polygon points="145,65 185,130 160,145 120,80" fill="#818cf8" stroke="#312e81" stroke-width="1.5" />
                <polygon points="95,145 185,145 160,160 70,160" fill="#3730a3" stroke="#312e81" stroke-width="1.5" />
              </g>

              <!-- Explanatory Callout Box below Tribar -->
              <g transform="translate(40, 250)">
                <rect width="480" height="75" rx="8" fill="#fef2f2" stroke="#fecaca" stroke-width="1.5" />
                <text x="240" y="24" text-anchor="middle" fill="#991b1b" font-family="'Space Grotesk', sans-serif" font-size="13" font-weight="700">Why the Brain is Fooled (Optical Analysis):</text>
                <text x="240" y="45" text-anchor="middle" fill="#7f1d1d" font-family="'Plus Jakarta Sans', sans-serif" font-size="11.5">1. Each corner by itself represents a physically valid 90° joint.</text>
                <text x="240" y="63" text-anchor="middle" fill="#7f1d1d" font-family="'Plus Jakarta Sans', sans-serif" font-size="11.5">2. In 3D space, the ends do not meet; parallel isometric projection forces them to touch!</text>
              </g>
            </g>
          </svg>
          <p class="svg-caption"><strong>Figure 2.6:</strong> The 120° Isometric grid coordinate foundation (left) and the famous Penrose Impossible Triangle (right).</p>
        </div>
      </div>

      <!-- PART 2.10: EXHAUSTIVE BILINGUAL VOCABULARY / GLOSSARY TABLE -->
      <div class="concept-card">
        <h3 class="concept-card-title"><i class="fa-solid fa-language"></i> 2.10 Exhaustive Bilingual Mathematical Vocabulary Bank (30 Terms)</h3>
        <p>
          Mastering these technical terms in both English and Odia script (ଓଡ଼ିଆ ଲିପି) ensures crystal-clear conceptual comprehension for middle school students across CBSE and BSE Odisha curriculums.
        </p>

        <div class="data-table-wrapper">
          <table class="data-table vocab-table">
            <thead>
              <tr>
                <th style="width: 22%;">Term / Concept</th>
                <th style="width: 14%;">Part of Speech</th>
                <th style="width: 34%;">English Meaning & Definition</th>
                <th style="width: 30%;">ଓଡ଼ିଆ ଅର୍ଥ (Odia Meaning in Script)</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>Fractal</strong></td>
                <td>Noun</td>
                <td>A geometric shape exhibiting self-similarity at progressively smaller scales.</td>
                <td>ଭଗ୍ନାଂଶାକୃତି / ଫ୍ରାକ୍ଟାଲ୍ (ଆତ୍ମ-ସଦୃଶ ଆକୃତି)</td>
              </tr>
              <tr>
                <td><strong>Self-Similarity</strong></td>
                <td>Noun</td>
                <td>The property where parts of an object resemble the whole object.</td>
                <td>ଆତ୍ମ-ସାଦୃଶ୍ୟ (ନିଜ ସହିତ ସମାନତା)</td>
              </tr>
              <tr>
                <td><strong>Iteration</strong></td>
                <td>Noun</td>
                <td>The process of repeatedly applying a mathematical rule or geometric step.</td>
                <td>ପୁନରାବୃତ୍ତି / ଚକ୍ରାବୃତ୍ତି</td>
              </tr>
              <tr>
                <td><strong>Sierpinski Carpet</strong></td>
                <td>Proper Noun</td>
                <td>A square fractal formed by repeatedly removing the central square of 9 sub-squares.</td>
                <td>ସିଅରପିନସ୍କି କାର୍ପେଟ୍</td>
              </tr>
              <tr>
                <td><strong>Sierpinski Gasket</strong></td>
                <td>Proper Noun</td>
                <td>A triangular fractal formed by removing the central inverted equilateral triangle.</td>
                <td>ସିଅରପିନସ୍କି ତ୍ରିଭୁଜ (ଗ୍ୟାସ୍କେଟ୍)</td>
              </tr>
              <tr>
                <td><strong>Koch Snowflake</strong></td>
                <td>Proper Noun</td>
                <td>A fractal curve with infinite perimeter enclosing a strictly finite area.</td>
                <td>କୋଚ୍ ସ୍ନୋ-ଫ୍ଲେକ୍ (ତୁଷାର କଣିକା ଆକୃତି)</td>
              </tr>
              <tr>
                <td><strong>Solid</strong></td>
                <td>Noun</td>
                <td>A three-dimensional closed geometric object having length, width, and height.</td>
                <td>ତ୍ରିମାତ୍ରିକ ବସ୍ତୁ / ଘନ ବସ୍ତୁ</td>
              </tr>
              <tr>
                <td><strong>Profile</strong></td>
                <td>Noun</td>
                <td>The 2D outline or boundary silhouette of an object viewed from a specific angle.</td>
                <td>ପାର୍ଶ୍ୱ ଚିତ୍ର / ବାହ୍ୟ ରୂପରେଖା</td>
              </tr>
              <tr>
                <td><strong>Polyhedron</strong></td>
                <td>Noun</td>
                <td>A 3D solid bounded entirely by flat polygonal faces (plural: polyhedra).</td>
                <td>ବହୁତଳକ (ସମତଳ ପୃଷ୍ଠ ବିଶିଷ୍ଟ ଘନ)</td>
              </tr>
              <tr>
                <td><strong>Face</strong></td>
                <td>Noun</td>
                <td>Each individual flat polygonal boundary surface of a polyhedron.</td>
                <td>ଫଳକ / ପୃଷ୍ଠତଳ</td>
              </tr>
              <tr>
                <td><strong>Edge</strong></td>
                <td>Noun</td>
                <td>The straight line segment along which two adjacent faces of a solid meet.</td>
                <td>ଧାର / ବାହୁ</td>
              </tr>
              <tr>
                <td><strong>Vertex</strong></td>
                <td>Noun</td>
                <td>The sharp corner point where three or more edges intersect (plural: vertices).</td>
                <td>ଶୀର୍ଷ ବିନ୍ଦୁ</td>
              </tr>
              <tr>
                <td><strong>Net</strong></td>
                <td>Noun</td>
                <td>A flat 2D folding pattern that can be folded to construct a 3D solid.</td>
                <td>ଜାଲ / ନେଟ୍ (ପ୍ରସାରିତ ଚିତ୍ର)</td>
              </tr>
              <tr>
                <td><strong>Regular Tetrahedron</strong></td>
                <td>Noun</td>
                <td>A 4-faced regular polyhedron whose faces are all equilateral triangles.</td>
                <td>ନିୟମିତ ଚତୁସ୍ତଳକ</td>
              </tr>
              <tr>
                <td><strong>Cube (Hexahedron)</strong></td>
                <td>Noun</td>
                <td>A 6-faced regular polyhedron whose faces are all congruent squares.</td>
                <td>ଘନକ / ନିୟମିତ ଷଡ଼ତଳକ</td>
              </tr>
              <tr>
                <td><strong>Regular Octahedron</strong></td>
                <td>Noun</td>
                <td>An 8-faced regular polyhedron formed by joining two square pyramids base-to-base.</td>
                <td>ନିୟମିତ ଅଷ୍ଟତଳକ</td>
              </tr>
              <tr>
                <td><strong>Regular Dodecahedron</strong></td>
                <td>Noun</td>
                <td>A 12-faced regular polyhedron whose faces are all regular pentagons.</td>
                <td>ନିୟମିତ ଦ୍ୱାଦଶତଳକ (୪୩,୩୮୦ ଜାଲ ବିଶିଷ୍ଟ)</td>
              </tr>
              <tr>
                <td><strong>Prism</strong></td>
                <td>Noun</td>
                <td>A polyhedron with two congruent parallel bases and parallelogram lateral faces.</td>
                <td>ପ୍ରିଜିମ୍ (ସମାନ୍ତରାଳ ଭିତ୍ତିକ ବହୁତଳକ)</td>
              </tr>
              <tr>
                <td><strong>Pyramid</strong></td>
                <td>Noun</td>
                <td>A polyhedron with one polygonal base and triangular lateral faces meeting at an apex.</td>
                <td>ପିରାମିଡ୍ (ଶୀର୍ଷଗାମୀ ବହୁତଳକ)</td>
              </tr>
              <tr>
                <td><strong>Geodesic / Shortest Path</strong></td>
                <td>Noun</td>
                <td>The absolute shortest path connecting two points along a curved or polygonal surface.</td>
                <td>କ୍ଷୁଦ୍ରତମ ପଥ / ଭୂ-ପୃଷ୍ଠୀୟ ସରଳରେଖା</td>
              </tr>
              <tr>
                <td><strong>Unfolding</strong></td>
                <td>Noun</td>
                <td>The geometric operation of flattening the adjacent 3D faces of a solid onto a 2D plane.</td>
                <td>ପ୍ରସାରଣ / ଉନ୍ମୋଚନ</td>
              </tr>
              <tr>
                <td><strong>Projection</strong></td>
                <td>Noun</td>
                <td>The image formed by dropping perpendiculars from all points of an object onto a plane.</td>
                <td>ପ୍ରକ୍ଷେପ / ଛାୟାଚିତ୍ର</td>
              </tr>
              <tr>
                <td><strong>Orthographic Projection</strong></td>
                <td>Noun</td>
                <td>A parallel projection where projection lines strike the projection plane at right angles (90°).</td>
                <td>ଲମ୍ବ ପ୍ରକ୍ଷେପ (ସମକୋଣୀୟ ପ୍ରକ୍ଷେପ)</td>
              </tr>
              <tr>
                <td><strong>Front View (Elevation)</strong></td>
                <td>Noun</td>
                <td>The 2D orthographic projection of an object viewed from the front onto a vertical plane.</td>
                <td>ସମ୍ମୁଖ ଦୃଶ୍ୟ (ସମ୍ମୁଖ ଉନ୍ନତି)</td>
              </tr>
              <tr>
                <td><strong>Top View (Plan)</strong></td>
                <td>Noun</td>
                <td>The 2D orthographic projection of an object viewed from above onto a horizontal plane.</td>
                <td>ଊର୍ଦ୍ଧ୍ୱ ଦୃଶ୍ୟ / ଉପର ଦୃଶ୍ୟ (ପ୍ଲାନ୍)</td>
              </tr>
              <tr>
                <td><strong>Side View (Profile)</strong></td>
                <td>Noun</td>
                <td>The 2D orthographic projection of an object viewed from the side onto a profile plane.</td>
                <td>ପାର୍ଶ୍ୱ ଦୃଶ୍ୟ</td>
              </tr>
              <tr>
                <td><strong>Isometric Projection</strong></td>
                <td>Noun</td>
                <td>A 3D drawing where the three principal axes are spaced at 120° and drawn to true scale.</td>
                <td>ଆଇସୋମେଟ୍ରିକ୍ ପ୍ରକ୍ଷେପ (ସମମାପ ଦୃଶ୍ୟ)</td>
              </tr>
              <tr>
                <td><strong>Isometric Grid</strong></td>
                <td>Noun</td>
                <td>A triangular grid of lines spaced at 60° and 120° used for sketching 3D solids.</td>
                <td>ଆଇସୋମେଟ୍ରିକ୍ ଗ୍ରିଡ୍ (ସମମାପ ଜାଲି)</td>
              </tr>
              <tr>
                <td><strong>Optical Illusion</strong></td>
                <td>Noun</td>
                <td>A visual drawing that deceives the brain into seeing a physically impossible 3D object.</td>
                <td>ଦୃଷ୍ଟିଭ୍ରମ / ମାୟାଚିତ୍ର</td>
              </tr>
              <tr>
                <td><strong>Euler's Formula</strong></td>
                <td>Proper Noun</td>
                <td>The topological invariant for convex polyhedra: Faces + Vertices - Edges = 2.</td>
                <td>ଅଏଲରଙ୍କ ସୂତ୍ର (ଫଳକ + ଶୀର୍ଷ - ଧାର = ୨)</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </section>
"""
