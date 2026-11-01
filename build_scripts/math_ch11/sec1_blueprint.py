# -*- coding: utf-8 -*-
"""
Section 1 Module: Hero Banner, Audio Reader, Visual Blueprint & Mind Map
Class 8 Mathematics Chapter 11: Exploring Some Geometric Themes
"""

def get_section_1():
    return """
    <!-- Hero Banner -->
    <header class="hero-banner">
      <div class="hero-badges">
        <span class="badge badge-primary"><i class="fa-solid fa-book-open"></i> NCERT Ganita Prakash Class 8 Part-II</span>
        <span class="badge badge-gold"><i class="fa-solid fa-certificate"></i> NEP 2020 Code: hegp111</span>
        <span class="badge badge-emerald"><i class="fa-solid fa-check-double"></i> 100% Zero-Omission Complete Edition</span>
      </div>
      <h1 class="hero-title">Exploring Some Geometric Themes</h1>
      <p class="hero-subtitle">
        An exhaustive, mathematically rigorous, and child-friendly master guide unlocking the mysteries of self-similar fractals, recursive area and perimeter sequences, temple architectural geometry, 3D polyhedra, the 11 valid nets of a cube, surface geodesics (Ant & Laddu shortest paths), orthographic projections (front, top, and side views), and isometric drafting on 120° grid planes.
      </p>

      <div class="hero-stats">
        <div class="stat-item">
          <i class="fa-solid fa-snowflake stat-icon"></i>
          <div class="stat-text">
            <h4>Fractal Geometry</h4>
            <p>Sierpinski Carpet, Gasket & Koch Snowflake</p>
          </div>
        </div>
        <div class="stat-item">
          <i class="fa-solid fa-cube stat-icon"></i>
          <div class="stat-text">
            <h4>Polyhedra & Nets</h4>
            <p>11 Cube Nets & Euler's Law (F + V = E + 2)</p>
          </div>
        </div>
        <div class="stat-item">
          <i class="fa-solid fa-route stat-icon"></i>
          <div class="stat-text">
            <h4>Surface Geodesics</h4>
            <p>Ant & Laddu Shortest Path via Net Unfolding</p>
          </div>
        </div>
        <div class="stat-item">
          <i class="fa-solid fa-drafting-compass stat-icon"></i>
          <div class="stat-text">
            <h4>Projections & 3D</h4>
            <p>Orthographic Views & 120° Isometric Grids</p>
          </div>
        </div>
      </div>
    </header>

    <!-- TTS Audio Reader Bar -->
    <div class="tts-container">
      <div class="tts-info">
        <div class="tts-icon-box">
          <i class="fa-solid fa-headphones"></i>
        </div>
        <div class="tts-details">
          <h4>Audio Teacher Reader (Listen to Chapter Summary)</h4>
          <p id="ttsStatus">Click Play to listen to an engaging audio overview of Chapter 11 concepts.</p>
        </div>
      </div>
      <div class="tts-controls">
        <button class="tts-btn" id="ttsPlayBtn" onclick="toggleAudioReader()">
          <i class="fa-solid fa-play" id="ttsIcon"></i> Listen to Summary
        </button>
        <select class="tts-select" id="ttsRate" onchange="updateSpeechRate()">
          <option value="0.8">0.8x Speed (Slow & Clear)</option>
          <option value="1.0" selected>1.0x Speed (Normal)</option>
          <option value="1.2">1.2x Speed (Brisk Revision)</option>
          <option value="1.4">1.4x Speed (Rapid Recap)</option>
        </select>
      </div>
    </div>

    <!-- SECTION 1: BLUEPRINT & MIND MAP -->
    <section id="section1" class="section-box">
      <div class="section-header">
        <div class="section-header-left">
          <span class="section-tag">Curriculum Architecture</span>
          <h2 class="section-title">§ 1. Visual Blueprint & Detailed Mind Map</h2>
          <p class="section-desc">
            A comprehensive visual roadmap structuring Chapter 11 into two majestic geometric pillars: Theme 1 explores self-similarity, iterative rules, and fractals across nature, mathematics, and ancient Indian temple architecture; Theme 2 develops spatial visualization of 3D solids through flat nets, surface geodesics, orthographic projections, and isometric drawings.
          </p>
        </div>
        <div>
          <span class="badge badge-primary"><i class="fa-solid fa-sitemap"></i> 5 Master Branches</span>
        </div>
      </div>

      <!-- INLINE RESPONSIVE SVG 1: CHAPTER 11 CONCEPT MIND MAP -->
      <div class="svg-graphic-box">
        <svg viewBox="0 0 1000 580" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg">
          <defs>
            <linearGradient id="bgGrad1" x1="0%" y1="0%" x2="100%" y2="100%">
              <stop offset="0%" stop-color="#0f172a" />
              <stop offset="100%" stop-color="#1e1b4b" />
            </linearGradient>
            <linearGradient id="centerGrad1" x1="0%" y1="0%" x2="100%" y2="100%">
              <stop offset="0%" stop-color="#4f46e5" />
              <stop offset="100%" stop-color="#9333ea" />
            </linearGradient>
            <linearGradient id="cardGradA" x1="0%" y1="0%" x2="100%" y2="100%">
              <stop offset="0%" stop-color="#3b82f6" />
              <stop offset="100%" stop-color="#1d4ed8" />
            </linearGradient>
            <linearGradient id="cardGradB" x1="0%" y1="0%" x2="100%" y2="100%">
              <stop offset="0%" stop-color="#0d9488" />
              <stop offset="100%" stop-color="#0f766e" />
            </linearGradient>
            <linearGradient id="cardGradC" x1="0%" y1="0%" x2="100%" y2="100%">
              <stop offset="0%" stop-color="#f59e0b" />
              <stop offset="100%" stop-color="#b45309" />
            </linearGradient>
            <linearGradient id="cardGradD" x1="0%" y1="0%" x2="100%" y2="100%">
              <stop offset="0%" stop-color="#8b5cf6" />
              <stop offset="100%" stop-color="#6d28d9" />
            </linearGradient>
            <linearGradient id="cardGradE" x1="0%" y1="0%" x2="100%" y2="100%">
              <stop offset="0%" stop-color="#ec4899" />
              <stop offset="100%" stop-color="#be185d" />
            </linearGradient>
            <filter id="glow1" x="-20%" y="-20%" width="140%" height="140%">
              <feDropShadow dx="0" dy="4" stdDeviation="6" flood-color="#4f46e5" flood-opacity="0.4" />
            </filter>
          </defs>

          <!-- Outer Background Canvas -->
          <rect width="1000" height="580" rx="20" fill="url(#bgGrad1)" />

          <!-- Connecting Curved Lines from Center to Branches -->
          <!-- To Branch A (Top Left) -->
          <path d="M 500 290 C 350 290, 220 180, 180 140" fill="none" stroke="#60a5fa" stroke-width="3" stroke-dasharray="6,4" />
          <!-- To Branch B (Top Right) -->
          <path d="M 500 290 C 650 290, 780 180, 820 140" fill="none" stroke="#2dd4bf" stroke-width="3" stroke-dasharray="6,4" />
          <!-- To Branch C (Middle Right) -->
          <path d="M 500 290 C 680 290, 760 330, 810 330" fill="none" stroke="#fbbf24" stroke-width="3" stroke-dasharray="6,4" />
          <!-- To Branch D (Bottom Right) -->
          <path d="M 500 290 C 660 380, 750 460, 800 480" fill="none" stroke="#c084fc" stroke-width="3" stroke-dasharray="6,4" />
          <!-- To Branch E (Bottom Left) -->
          <path d="M 500 290 C 350 360, 240 450, 190 480" fill="none" stroke="#f472b6" stroke-width="3" stroke-dasharray="6,4" />

          <!-- CENTRAL MASTER HUB -->
          <circle cx="500" cy="290" r="85" fill="url(#centerGrad1)" filter="url(#glow1)" stroke="#e0e7ff" stroke-width="4" />
          <text x="500" y="270" text-anchor="middle" fill="#ffffff" font-family="'Space Grotesk', sans-serif" font-size="16" font-weight="700">CLASS 8 MATH</text>
          <text x="500" y="295" text-anchor="middle" fill="#fef08a" font-family="'Space Grotesk', sans-serif" font-size="19" font-weight="800">CHAPTER 11</text>
          <text x="500" y="318" text-anchor="middle" fill="#ffffff" font-family="'Plus Jakarta Sans', sans-serif" font-size="12" font-weight="600">GEOMETRIC THEMES</text>

          <!-- BRANCH A: FRACTALS & SELF-SIMILARITY (Top Left) -->
          <g transform="translate(40, 40)">
            <rect width="280" height="150" rx="14" fill="url(#cardGradA)" stroke="#93c5fd" stroke-width="2" />
            <text x="16" y="28" fill="#ffffff" font-family="'Space Grotesk', sans-serif" font-size="15" font-weight="700">1. Fractals & Self-Similarity</text>
            <line x1="16" y1="36" x2="264" y2="36" stroke="rgba(255,255,255,0.3)" stroke-width="1.5" />
            <text x="16" y="56" fill="#e0f2fe" font-family="'Plus Jakarta Sans', sans-serif" font-size="11.5">• Nature: Ferns, Romanesco, Clouds, Coast</text>
            <text x="16" y="76" fill="#e0f2fe" font-family="'Plus Jakarta Sans', sans-serif" font-size="11.5">• Sierpinski Carpet: R_n = 8ⁿ, Area → 0</text>
            <text x="16" y="96" fill="#e0f2fe" font-family="'Plus Jakarta Sans', sans-serif" font-size="11.5">• Sierpinski Gasket: R_n = 3ⁿ, Perimeter → ∞</text>
            <text x="16" y="116" fill="#e0f2fe" font-family="'Plus Jakarta Sans', sans-serif" font-size="11.5">• Koch Snowflake: N_n = 3·4ⁿ, Finite Area</text>
            <text x="16" y="136" fill="#fef08a" font-family="'Plus Jakarta Sans', sans-serif" font-size="11" font-weight="700">★ Khajuraho Temple & Escher Fractal Art</text>
          </g>

          <!-- BRANCH B: POLYHEDRA, NETS & PLATONIC SOLIDS (Top Right) -->
          <g transform="translate(680, 40)">
            <rect width="280" height="150" rx="14" fill="url(#cardGradB)" stroke="#5eead4" stroke-width="2" />
            <text x="16" y="28" fill="#ffffff" font-family="'Space Grotesk', sans-serif" font-size="15" font-weight="700">2. Polyhedra & 2D Nets</text>
            <line x1="16" y1="36" x2="264" y2="36" stroke="rgba(255,255,255,0.3)" stroke-width="1.5" />
            <text x="16" y="56" fill="#ccfbf1" font-family="'Plus Jakarta Sans', sans-serif" font-size="11.5">• Polyhedra: Faces, Edges & Vertices</text>
            <text x="16" y="76" fill="#ccfbf1" font-family="'Plus Jakarta Sans', sans-serif" font-size="11.5">• Prism: F = n+2, V = 2n, E = 3n</text>
            <text x="16" y="96" fill="#ccfbf1" font-family="'Plus Jakarta Sans', sans-serif" font-size="11.5">• Pyramid: F = n+1, V = n+1, E = 2n</text>
            <text x="16" y="116" fill="#ccfbf1" font-family="'Plus Jakarta Sans', sans-serif" font-size="11.5">• 11 Cube Nets (1-4-1, 1-3-2, 2-2-2, 3-3)</text>
            <text x="16" y="136" fill="#fef08a" font-family="'Plus Jakarta Sans', sans-serif" font-size="11" font-weight="700">★ Dodecahedron (43,380 Nets) | No Sphere Net</text>
          </g>

          <!-- BRANCH C: SURFACE GEODESICS (Middle Right) -->
          <g transform="translate(680, 230)">
            <rect width="280" height="135" rx="14" fill="url(#cardGradC)" stroke="#fde68a" stroke-width="2" />
            <text x="16" y="28" fill="#ffffff" font-family="'Space Grotesk', sans-serif" font-size="15" font-weight="700">3. Surface Geodesics (Ant & Laddu)</text>
            <line x1="16" y1="36" x2="264" y2="36" stroke="rgba(255,255,255,0.3)" stroke-width="1.5" />
            <text x="16" y="56" fill="#fef3c7" font-family="'Plus Jakarta Sans', sans-serif" font-size="11.5">• 3D surface path = 2D straight line on net</text>
            <text x="16" y="76" fill="#fef3c7" font-family="'Plus Jakarta Sans', sans-serif" font-size="11.5">• Path must not cross empty space off-net</text>
            <text x="16" y="96" fill="#fef3c7" font-family="'Plus Jakarta Sans', sans-serif" font-size="11.5">• 30×12×12 Box: Unfolding A = 42.4 cm</text>
            <text x="16" y="116" fill="#ffffff" font-family="'Plus Jakarta Sans', sans-serif" font-size="11.5" font-weight="700">★ Unfolding B: d = √(32²+24²) = 40 cm (MIN)</text>
          </g>

          <!-- BRANCH D: ORTHOGRAPHIC PROJECTIONS (Bottom Right) -->
          <g transform="translate(680, 400)">
            <rect width="280" height="145" rx="14" fill="url(#cardGradD)" stroke="#d8b4fe" stroke-width="2" />
            <text x="16" y="28" fill="#ffffff" font-family="'Space Grotesk', sans-serif" font-size="15" font-weight="700">4. Orthographic Projections</text>
            <line x1="16" y1="36" x2="264" y2="36" stroke="rgba(255,255,255,0.3)" stroke-width="1.5" />
            <text x="16" y="56" fill="#f3e8ff" font-family="'Plus Jakarta Sans', sans-serif" font-size="11.5">• Front View: Vertical Plane (Elevation)</text>
            <text x="16" y="76" fill="#f3e8ff" font-family="'Plus Jakarta Sans', sans-serif" font-size="11.5">• Top View: Horizontal Plane (Plan)</text>
            <text x="16" y="96" fill="#f3e8ff" font-family="'Plus Jakarta Sans', sans-serif" font-size="11.5">• Side View: Side Vertical Plane (Profile)</text>
            <text x="16" y="116" fill="#f3e8ff" font-family="'Plus Jakarta Sans', sans-serif" font-size="11.5">• Line Projection length: p = l·cos θ ≤ l</text>
            <text x="16" y="134" fill="#fef08a" font-family="'Plus Jakarta Sans', sans-serif" font-size="11" font-weight="700">★ Parallel Lines Always Project to Parallel Lines</text>
          </g>

          <!-- BRANCH E: ISOMETRIC DRAFTING & OPTICAL ILLUSIONS (Bottom Left) -->
          <g transform="translate(40, 395)">
            <rect width="280" height="150" rx="14" fill="url(#cardGradE)" stroke="#fbcfe8" stroke-width="2" />
            <text x="16" y="28" fill="#ffffff" font-family="'Space Grotesk', sans-serif" font-size="15" font-weight="700">5. Isometric Grid & Illusions</text>
            <line x1="16" y1="36" x2="264" y2="36" stroke="rgba(255,255,255,0.3)" stroke-width="1.5" />
            <text x="16" y="54" fill="#fce7f3" font-family="'Plus Jakarta Sans', sans-serif" font-size="11.5">• 'Isometric' = Equal Measure (Greek)</text>
            <text x="16" y="72" fill="#fce7f3" font-family="'Plus Jakarta Sans', sans-serif" font-size="11.5">• 3 Coordinate Axes spaced at 120°</text>
            <text x="16" y="90" fill="#fce7f3" font-family="'Plus Jakarta Sans', sans-serif" font-size="11.5">• True scale drafting along length, depth, height</text>
            <text x="16" y="108" fill="#fce7f3" font-family="'Plus Jakarta Sans', sans-serif" font-size="11.5">• Cube balanced on vertex → Regular Hexagon</text>
            <text x="16" y="128" fill="#fef08a" font-family="'Plus Jakarta Sans', sans-serif" font-size="11" font-weight="700">★ Penrose Tribar & Escher Impossible Stairs</text>
          </g>

          <!-- Center Decorative Icon Elements -->
          <circle cx="500" cy="180" r="16" fill="#60a5fa" opacity="0.8" />
          <text x="500" y="185" text-anchor="middle" fill="#ffffff" font-size="12">❄</text>
          <circle cx="500" cy="400" r="16" fill="#ec4899" opacity="0.8" />
          <text x="500" y="405" text-anchor="middle" fill="#ffffff" font-size="12">📐</text>
        </svg>
        <p class="svg-caption"><strong>Figure 1.1:</strong> Architectural Curriculum Mind Map for Class 8 Mathematics Chapter 11 — Integrating Fractal Self-Similarity with 3D Spatial Geometry.</p>
      </div>

      <!-- Pedagogical Breakdown Cards -->
      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 1.5rem; margin-top: 2rem;">
        <div class="concept-card" style="margin-bottom: 0;">
          <h3 class="concept-card-title"><i class="fa-solid fa-leaf"></i> Theme 1: Self-Similarity & Fractals</h3>
          <p style="font-size: 0.9rem; color: var(--text-muted); line-height: 1.6;">
            Fractals break away from classical smooth Euclidean shapes. They exhibit recursive self-similarity: every fragment resembles the master geometry at progressively smaller scales. Through recursive mathematics, students discover the astonishing counter-intuitive reality that a shape can have an infinite boundary perimeter while enclosing a strictly finite or zero area.
          </p>
        </div>

        <div class="concept-card" style="margin-bottom: 0;">
          <h3 class="concept-card-title"><i class="fa-solid fa-cubes"></i> Theme 2: Polyhedra, Nets & Geodesics</h3>
          <p style="font-size: 0.9rem; color: var(--text-muted); line-height: 1.6;">
            Moving from 2D planes to 3D space, students master polyhedra (prisms and pyramids), their structural formulas, and the 11 valid folding nets of a cube. By transforming the complex 3D geodesic surface traversal (the famous Ant & Laddu problem) into 2D straight lines on unfolded nets, students connect spatial intuition with the Baudhāyana-Pythagoras theorem.
          </p>
        </div>

        <div class="concept-card" style="margin-bottom: 0;">
          <h3 class="concept-card-title"><i class="fa-solid fa-eye"></i> Theme 3: Projections & Isometric Art</h3>
          <p style="font-size: 0.9rem; color: var(--text-muted); line-height: 1.6;">
            Engineering design depends on accurately depicting 3D objects on 2D paper. Students explore orthographic projections (front, top, and side views), understand how distant sunlight creates true parallel projections, master 120° isometric grid drawing, and uncover why optical illusions like the Penrose Triangle trick the human brain.
          </p>
        </div>
      </div>
    </section>
"""
