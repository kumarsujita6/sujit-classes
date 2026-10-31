# -*- coding: utf-8 -*-
"""
Module: ch7_section1.py
Contains Section 1: Visual Blueprint & Detailed Mind Map, including an intricate
responsive SVG visualizer for digital image aspect ratios and geometric scaling.
"""

def get_section1():
    return """
    <!-- ========================================== -->
    <!-- SECTION 1: VISUAL BLUEPRINT & MIND MAP    -->
    <!-- ========================================== -->
    <section id="section1">
      <div class="section-header">
        <div class="section-tag"><i class="fa-solid fa-sitemap"></i> Curricular Architecture</div>
        <h2 class="section-title">Section 1: Visual Blueprint & Detailed Mind Map</h2>
        <p class="section-desc">
          Proportional reasoning is the foundation of advanced mathematics, physics, engineering, and everyday decision making. It allows us to recognize, model, and predict multiplicative relationships between two or more changing quantities.
        </p>
      </div>

      <!-- INTRICATE SVG 1: DIGITAL IMAGE ASPECT RATIOS & GEOMETRIC DISTORTIONS -->
      <div class="svg-container">
        <svg viewBox="0 0 1000 520" xmlns="http://www.w3.org/2000/svg" style="background: #f8fafc; border-radius: 16px;">
          <defs>
            <linearGradient id="blueGrad" x1="0%" y1="0%" x2="100%" y2="100%">
              <stop offset="0%" stop-color="#4f46e5" stop-opacity="0.15" />
              <stop offset="100%" stop-color="#3730a3" stop-opacity="0.25" />
            </linearGradient>
            <linearGradient id="emeraldGrad" x1="0%" y1="0%" x2="100%" y2="100%">
              <stop offset="0%" stop-color="#059669" stop-opacity="0.15" />
              <stop offset="100%" stop-color="#047857" stop-opacity="0.25" />
            </linearGradient>
            <linearGradient id="amberGrad" x1="0%" y1="0%" x2="100%" y2="100%">
              <stop offset="0%" stop-color="#d97706" stop-opacity="0.15" />
              <stop offset="100%" stop-color="#b45309" stop-opacity="0.25" />
            </linearGradient>
            <linearGradient id="redGrad" x1="0%" y1="0%" x2="100%" y2="100%">
              <stop offset="0%" stop-color="#dc2626" stop-opacity="0.12" />
              <stop offset="100%" stop-color="#991b1b" stop-opacity="0.22" />
            </linearGradient>
            <filter id="shadowEffect" x="-5%" y="-5%" width="110%" height="110%">
              <feDropShadow dx="2" dy="4" stdDeviation="4" flood-color="#0f172a" flood-opacity="0.08"/>
            </filter>
          </defs>

          <!-- Diagram Header -->
          <rect x="20" y="15" width="960" height="50" rx="10" fill="#0f172a" />
          <text x="500" y="46" font-family="'Space Grotesk', sans-serif" font-size="18" font-weight="700" fill="#f8fafc" text-anchor="middle">
            FIG 7.1: GEOMETRIC ASPECT RATIO &amp; IMAGE SCALING BENCHMARK (NCERT SEC 7.1)
          </text>

          <!-- IMAGE A (ORIGINAL) -->
          <g transform="translate(40, 90)" filter="url(#shadowEffect)">
            <rect x="0" y="0" width="180" height="120" rx="8" fill="url(#blueGrad)" stroke="#4f46e5" stroke-width="2.5" />
            <!-- Inner Mock Tiger Outline -->
            <path d="M 40,75 Q 60,35 90,60 T 140,65 Q 150,90 120,95 T 50,90 Z" fill="#4f46e5" fill-opacity="0.2" stroke="#4f46e5" stroke-width="1.5" />
            <circle cx="75" cy="55" r="4" fill="#3730a3" />
            <text x="90" y="-12" font-family="'Space Grotesk', sans-serif" font-size="14" font-weight="700" fill="#1e1b4b" text-anchor="middle">IMAGE A (Original)</text>
            <text x="90" y="145" font-family="'JetBrains Mono', monospace" font-size="12" font-weight="700" fill="#4f46e5" text-anchor="middle">Width = 60 mm</text>
            <text x="90" y="162" font-family="'JetBrains Mono', monospace" font-size="12" font-weight="700" fill="#4f46e5" text-anchor="middle">Height = 40 mm</text>
            <rect x="35" y="175" width="110" height="24" rx="12" fill="#e0e7ff" />
            <text x="90" y="191" font-family="'Space Grotesk', sans-serif" font-size="11" font-weight="800" fill="#3730a3" text-anchor="middle">RATIO 3 : 2 (1.50)</text>
            <text x="90" y="215" font-family="'Plus Jakarta Sans', sans-serif" font-size="11" font-weight="600" fill="#059669" text-anchor="middle">✓ Perfect Natural Form</text>
          </g>

          <!-- IMAGE B (ELONGATED / DISTORTED) -->
          <g transform="translate(260, 90)" filter="url(#shadowEffect)">
            <rect x="0" y="30" width="160" height="60" rx="8" fill="url(#redGrad)" stroke="#dc2626" stroke-width="2" stroke-dasharray="4 2" />
            <path d="M 30,68 Q 65,45 100,58 T 140,62 Q 145,78 115,80 T 40,78 Z" fill="#dc2626" fill-opacity="0.2" stroke="#dc2626" stroke-width="1.5" />
            <text x="80" y="-12" font-family="'Space Grotesk', sans-serif" font-size="14" font-weight="700" fill="#991b1b" text-anchor="middle">IMAGE B (Distorted)</text>
            <text x="80" y="145" font-family="'JetBrains Mono', monospace" font-size="12" font-weight="700" fill="#dc2626" text-anchor="middle">Width = 40 mm</text>
            <text x="80" y="162" font-family="'JetBrains Mono', monospace" font-size="12" font-weight="700" fill="#dc2626" text-anchor="middle">Height = 20 mm</text>
            <rect x="25" y="175" width="110" height="24" rx="12" fill="#fee2e2" />
            <text x="80" y="191" font-family="'Space Grotesk', sans-serif" font-size="11" font-weight="800" fill="#991b1b" text-anchor="middle">RATIO 2 : 1 (2.00)</text>
            <text x="80" y="215" font-family="'Plus Jakarta Sans', sans-serif" font-size="11" font-weight="600" fill="#dc2626" text-anchor="middle">✗ Stretched Horizontally</text>
          </g>

          <!-- IMAGE C (SCALED DOWN) -->
          <g transform="translate(460, 90)" filter="url(#shadowEffect)">
            <rect x="20" y="30" width="90" height="60" rx="8" fill="url(#emeraldGrad)" stroke="#059669" stroke-width="2.5" />
            <path d="M 35,68 Q 50,48 65,60 T 95,62 Q 100,75 80,78 T 40,75 Z" fill="#059669" fill-opacity="0.2" stroke="#059669" stroke-width="1.2" />
            <circle cx="58" cy="58" r="2.5" fill="#047857" />
            <text x="65" y="-12" font-family="'Space Grotesk', sans-serif" font-size="14" font-weight="700" fill="#065f46" text-anchor="middle">IMAGE C (Scaled 0.5×)</text>
            <text x="65" y="145" font-family="'JetBrains Mono', monospace" font-size="12" font-weight="700" fill="#059669" text-anchor="middle">Width = 30 mm</text>
            <text x="65" y="162" font-family="'JetBrains Mono', monospace" font-size="12" font-weight="700" fill="#059669" text-anchor="middle">Height = 20 mm</text>
            <rect x="10" y="175" width="110" height="24" rx="12" fill="#d1fae5" />
            <text x="65" y="191" font-family="'Space Grotesk', sans-serif" font-size="11" font-weight="800" fill="#047857" text-anchor="middle">RATIO 3 : 2 (1.50)</text>
            <text x="65" y="215" font-family="'Plus Jakarta Sans', sans-serif" font-size="11" font-weight="600" fill="#059669" text-anchor="middle">✓ Similar (Proportional)</text>
          </g>

          <!-- IMAGE D (SCALED UP 1.5×) -->
          <g transform="translate(620, 70)" filter="url(#shadowEffect)">
            <rect x="0" y="0" width="180" height="120" rx="8" fill="url(#amberGrad)" stroke="#d97706" stroke-width="2.5" />
            <path d="M 40,75 Q 60,35 90,60 T 140,65 Q 150,90 120,95 T 50,90 Z" fill="#d97706" fill-opacity="0.2" stroke="#d97706" stroke-width="1.5" />
            <circle cx="75" cy="55" r="4" fill="#b45309" />
            <text x="90" y="-12" font-family="'Space Grotesk', sans-serif" font-size="14" font-weight="700" fill="#78350f" text-anchor="middle">IMAGE D (Scaled 1.5×)</text>
            <text x="90" y="145" font-family="'JetBrains Mono', monospace" font-size="12" font-weight="700" fill="#d97706" text-anchor="middle">Width = 90 mm</text>
            <text x="90" y="162" font-family="'JetBrains Mono', monospace" font-size="12" font-weight="700" fill="#d97706" text-anchor="middle">Height = 60 mm</text>
            <rect x="35" y="175" width="110" height="24" rx="12" fill="#fef3c7" />
            <text x="90" y="191" font-family="'Space Grotesk', sans-serif" font-size="11" font-weight="800" fill="#b45309" text-anchor="middle">RATIO 3 : 2 (1.50)</text>
            <text x="90" y="215" font-family="'Plus Jakarta Sans', sans-serif" font-size="11" font-weight="600" fill="#059669" text-anchor="middle">✓ Similar (Proportional)</text>
          </g>

          <!-- IMAGE E (SQUARE / SQUISHED) -->
          <g transform="translate(840, 90)" filter="url(#shadowEffect)">
            <rect x="10" y="20" width="80" height="80" rx="8" fill="url(#redGrad)" stroke="#dc2626" stroke-width="2" stroke-dasharray="4 2" />
            <path d="M 25,65 Q 40,40 55,55 T 80,60 Q 82,80 65,80 T 30,78 Z" fill="#dc2626" fill-opacity="0.2" stroke="#dc2626" stroke-width="1.5" />
            <text x="50" y="-12" font-family="'Space Grotesk', sans-serif" font-size="14" font-weight="700" fill="#991b1b" text-anchor="middle">IMAGE E (Distorted)</text>
            <text x="50" y="145" font-family="'JetBrains Mono', monospace" font-size="12" font-weight="700" fill="#dc2626" text-anchor="middle">Width = 40 mm</text>
            <text x="50" y="162" font-family="'JetBrains Mono', monospace" font-size="12" font-weight="700" fill="#dc2626" text-anchor="middle">Height = 40 mm</text>
            <rect x="-5" y="175" width="110" height="24" rx="12" fill="#fee2e2" />
            <text x="50" y="191" font-family="'Space Grotesk', sans-serif" font-size="11" font-weight="800" fill="#991b1b" text-anchor="middle">RATIO 1 : 1 (1.00)</text>
            <text x="50" y="215" font-family="'Plus Jakarta Sans', sans-serif" font-size="11" font-weight="600" fill="#dc2626" text-anchor="middle">✗ Squished / Compressed</text>
          </g>

          <!-- BOTTOM COMPARISON SUMMARY BANNER -->
          <g transform="translate(30, 340)">
            <rect x="0" y="0" width="940" height="155" rx="12" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.5" />
            <rect x="0" y="0" width="940" height="36" rx="12" fill="#f1f5f9" />
            <text x="25" y="24" font-family="'Space Grotesk', sans-serif" font-size="14" font-weight="700" fill="#0f172a">
              MATHEMATICAL DEDUCTION: WHY ARE IMAGES A, C, AND D SIMILAR WHILE B AND E ARE DISTORTED?
            </text>

            <text x="25" y="62" font-family="'Plus Jakarta Sans', sans-serif" font-size="13" fill="#334155">
              • <strong>Image A (60 : 40)</strong> simplifies by dividing both terms by HCF(60, 40) = 20 ⇒ <strong>3 : 2</strong>. Scale Factor = 1.0.
            </text>
            <text x="25" y="85" font-family="'Plus Jakarta Sans', sans-serif" font-size="13" fill="#334155">
              • <strong>Image C (30 : 20)</strong> simplifies by dividing both terms by HCF(30, 20) = 10 ⇒ <strong>3 : 2</strong>. Derived from Image A by multiplying by factor 1/2.
            </text>
            <text x="25" y="108" font-family="'Plus Jakarta Sans', sans-serif" font-size="13" fill="#334155">
              • <strong>Image D (90 : 60)</strong> simplifies by dividing both terms by HCF(90, 60) = 30 ⇒ <strong>3 : 2</strong>. Derived from Image A by multiplying by factor 3/2.
            </text>
            <text x="25" y="131" font-family="'Plus Jakarta Sans', sans-serif" font-size="13" fill="#b91c1c">
              • <strong>Image B (40 : 20 = 2 : 1)</strong> and <strong>Image E (40 : 40 = 1 : 1)</strong> have different simplest ratios. Thus, they are <strong>NOT proportional</strong> (distorted).
            </text>
            <text x="750" y="142" font-family="'JetBrains Mono', monospace" font-size="12" font-weight="700" fill="#4f46e5">
              60:40 :: 30:20 :: 90:60
            </text>
          </g>
        </svg>
        <p class="svg-caption">
          Figure 7.1: Visual proof of proportionality. Two visual figures are geometrically similar if and only if the ratio of corresponding dimensions (width : height) remains invariant under scaling.
        </p>
      </div>

      <!-- COMPREHENSIVE MIND MAP TILES -->
      <h3 class="subheading"><i class="fa-solid fa-network-wired"></i> The 6 Architectural Pillars of Chapter 7</h3>
      <p>
        Every concept in Chapter 7 connects directly into a unified conceptual framework. Explore each pillar below before diving into line-by-line theory:
      </p>

      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 1.5rem; margin-top: 1.5rem;">
        
        <!-- Pillar 1 -->
        <div style="background: #f8fafc; border: 1.5px solid var(--border); border-radius: var(--radius-md); padding: 1.5rem; border-top: 4px solid #4f46e5;">
          <h4 style="font-family: 'Space Grotesk', sans-serif; font-size: 1.15rem; color: #312e81; margin-bottom: 0.6rem; display: flex; align-items: center; gap: 0.5rem;">
            <i class="fa-solid fa-shapes"></i> 1. Ratios &amp; Simplest Forms
          </h4>
          <p style="font-size: 0.925rem; color: #475569; margin-bottom: 0.75rem;">
            A ratio <em>a : b</em> compares two quantities of the same kind by division. The terms <em>a</em> (antecedent) and <em>b</em> (consequent) are reduced to simplest form by dividing by their HCF:
          </p>
          <div class="highlight-pill" style="display: block; text-align: center; margin-bottom: 0.75rem;">
            Simplest Form: a/HCF(a, b) : b/HCF(a, b)
          </div>
          <p style="font-size: 0.85rem; color: #64748b; margin-bottom: 0;">
            <strong>Critical Insight:</strong> Ratios are pure dimensionless numbers. Adding a constant to both terms breaks the ratio!
          </p>
        </div>

        <!-- Pillar 2 -->
        <div style="background: #f8fafc; border: 1.5px solid var(--border); border-radius: var(--radius-md); padding: 1.5rem; border-top: 4px solid #059669;">
          <h4 style="font-family: 'Space Grotesk', sans-serif; font-size: 1.15rem; color: #065f46; margin-bottom: 0.6rem; display: flex; align-items: center; gap: 0.5rem;">
            <i class="fa-solid fa-scale-balanced"></i> 2. The Law of Proportion
          </h4>
          <p style="font-size: 0.925rem; color: #475569; margin-bottom: 0.75rem;">
            Two ratios are in proportion (<em>a : b :: c : d</em>) if they represent the same numerical value. By cross-multiplication, the fundamental invariance law states:
          </p>
          <div class="highlight-pill" style="display: block; text-align: center; margin-bottom: 0.75rem;">
            Product of Extremes = Product of Means ⇒ a × d = b × c
          </div>
          <p style="font-size: 0.85rem; color: #64748b; margin-bottom: 0;">
            Any unknown fourth term can be computed directly as <em>d = (b × c) / a</em>.
          </p>
        </div>

        <!-- Pillar 3 -->
        <div style="background: #f8fafc; border: 1.5px solid var(--border); border-radius: var(--radius-md); padding: 1.5rem; border-top: 4px solid #d97706;">
          <h4 style="font-family: 'Space Grotesk', sans-serif; font-size: 1.15rem; color: #78350f; margin-bottom: 0.6rem; display: flex; align-items: center; gap: 0.5rem;">
            <i class="fa-solid fa-scroll"></i> 3. Ancient Indian Trairāśika
          </h4>
          <p style="font-size: 0.925rem; color: #475569; margin-bottom: 0.75rem;">
            Formalized by Āryabhaṭa I (499 CE) and Bhāskara II in <em>Līlāvatī</em>, the Rule of Three links three known quantities to find the desired yield:
          </p>
          <div class="highlight-pill" style="display: block; text-align: center; margin-bottom: 0.75rem;">
            Ichchhāphala = (Phala × Ichchhā) ÷ Pramāṇa
          </div>
          <p style="font-size: 0.85rem; color: #64748b; margin-bottom: 0;">
            Solves commercial trading, saffron currency exchange, midday meal food allocation, and bricklaying.
          </p>
        </div>

        <!-- Pillar 4 -->
        <div style="background: #f8fafc; border: 1.5px solid var(--border); border-radius: var(--radius-md); padding: 1.5rem; border-top: 4px solid #7c3aed;">
          <h4 style="font-family: 'Space Grotesk', sans-serif; font-size: 1.15rem; color: #4c1d95; margin-bottom: 0.6rem; display: flex; align-items: center; gap: 0.5rem;">
            <i class="fa-solid fa-pie-chart"></i> 4. Partitioning &amp; Sharing (m : n)
          </h4>
          <p style="font-size: 0.925rem; color: #475569; margin-bottom: 0.75rem;">
            To divide a quantity <em>x</em> in the ratio <em>m : n</em>, split the whole into <em>(m + n)</em> equal groups. The size of one group is <em>x / (m + n)</em>:
          </p>
          <div class="highlight-pill" style="display: block; text-align: center; margin-bottom: 0.75rem;">
            Part 1 = m × [x / (m+n)] &nbsp;|&nbsp; Part 2 = n × [x / (m+n)]
          </div>
          <p style="font-size: 0.85rem; color: #64748b; margin-bottom: 0;">
            Applied in partnership profits (Prashanti &amp; Bhuvan), cement mixtures, and paint tinting.
          </p>
        </div>

        <!-- Pillar 5 -->
        <div style="background: #f8fafc; border: 1.5px solid var(--border); border-radius: var(--radius-md); padding: 1.5rem; border-top: 4px solid #0284c7;">
          <h4 style="font-family: 'Space Grotesk', sans-serif; font-size: 1.15rem; color: #0369a1; margin-bottom: 0.6rem; display: flex; align-items: center; gap: 0.5rem;">
            <i class="fa-solid fa-ruler-combined"></i> 5. Unit Conversions &amp; Standards
          </h4>
          <p style="font-size: 0.925rem; color: #475569; margin-bottom: 0.75rem;">
            Quantities must share identical units before proportional comparison. Key standard factors:
          </p>
          <div class="highlight-pill" style="display: block; text-align: center; margin-bottom: 0.75rem;">
            1 acre = 43,560 sq ft &nbsp;|&nbsp; 1 L = 1,000 mL = 1,000 cc
          </div>
          <p style="font-size: 0.85rem; color: #64748b; margin-bottom: 0;">
            Temperature: <em>°F = (9/5)°C + 32</em> and <em>°C = (5/9)(°F - 32)</em>.
          </p>
        </div>

        <!-- Pillar 6 -->
        <div style="background: #f8fafc; border: 1.5px solid var(--border); border-radius: var(--radius-md); padding: 1.5rem; border-top: 4px solid #e11d48;">
          <h4 style="font-family: 'Space Grotesk', sans-serif; font-size: 1.15rem; color: #9f1239; margin-bottom: 0.6rem; display: flex; align-items: center; gap: 0.5rem;">
            <i class="fa-solid fa-arrow-down-up-across-line"></i> 6. Non-Proportional Boundaries
          </h4>
          <p style="font-size: 0.925rem; color: #475569; margin-bottom: 0.75rem;">
            Not all relationships are directly proportional! Recognizing when proportional reasoning fails prevents critical calculation errors:
          </p>
          <div class="highlight-pill" style="display: block; text-align: center; margin-bottom: 0.75rem;">
            Speed × Time = Constant &nbsp;(Inverse Proportion)
          </div>
          <p style="font-size: 0.85rem; color: #64748b; margin-bottom: 0;">
            Market pricing (shampoo bottles vs sachets) is influenced by packaging, marketing, and volume tiers.
          </p>
        </div>

      </div>
    </section>
"""
