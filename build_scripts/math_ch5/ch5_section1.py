# -*- coding: utf-8 -*-
"""Part 2: Section 1 - Visual Blueprint and Detailed Mind Map."""

SECTION1_CONTENT = """
    <!-- SECTION 1: VISUAL BLUEPRINT & DETAILED MIND MAP -->
    <section id="blueprint" class="section-card">
      <div class="section-header">
        <div class="section-icon-box">
          <i class="fa-solid fa-sitemap"></i>
        </div>
        <div>
          <h2 class="section-title">Section 1: Visual Blueprint & Detailed Mind Map</h2>
          <p class="section-tagline">Architectural conceptual roadmap and hierarchical knowledge tree for Chapter 5: Parallel and Intersecting Lines</p>
        </div>
      </div>

      <!-- INLINE SVG 1: CHAPTER CONCEPTUAL ARCHITECTURE BLUEPRINT -->
      <div class="diagram-card">
        <svg viewBox="0 0 1000 620" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg" style="max-width: 950px; font-family: 'Plus Jakarta Sans', sans-serif;">
          <defs>
            <linearGradient id="bgGrad" x1="0%" y1="0%" x2="100%" y2="100%">
              <stop offset="0%" stop-color="#0f172a"/>
              <stop offset="100%" stop-color="#1e293b"/>
            </linearGradient>
            <linearGradient id="coreGrad" x1="0%" y1="0%" x2="100%" y2="100%">
              <stop offset="0%" stop-color="#0284c7"/>
              <stop offset="100%" stop-color="#0369a1"/>
            </linearGradient>
            <linearGradient id="nodeBlue" x1="0%" y1="0%" x2="100%" y2="100%">
              <stop offset="0%" stop-color="#38bdf8"/>
              <stop offset="100%" stop-color="#0284c7"/>
            </linearGradient>
            <linearGradient id="nodeTeal" x1="0%" y1="0%" x2="100%" y2="100%">
              <stop offset="0%" stop-color="#2dd4bf"/>
              <stop offset="100%" stop-color="#0f766e"/>
            </linearGradient>
            <linearGradient id="nodePurple" x1="0%" y1="0%" x2="100%" y2="100%">
              <stop offset="0%" stop-color="#c084fc"/>
              <stop offset="100%" stop-color="#7c3aed"/>
            </linearGradient>
            <linearGradient id="nodeAmber" x1="0%" y1="0%" x2="100%" y2="100%">
              <stop offset="0%" stop-color="#fbbf24"/>
              <stop offset="100%" stop-color="#d97706"/>
            </linearGradient>
            <filter id="glow" x="-20%" y="-20%" width="140%" height="140%">
              <feDropShadow dx="0" dy="4" stdDeviation="6" flood-color="#0284c7" flood-opacity="0.3"/>
            </filter>
          </defs>

          <!-- Outer Background Canvas -->
          <rect width="1000" height="620" rx="20" fill="url(#bgGrad)" stroke="#334155" stroke-width="2"/>

          <!-- Header Title in SVG -->
          <text x="500" y="45" text-anchor="middle" fill="#f8fafc" font-size="20" font-weight="800" letter-spacing="1">PARALLEL &amp; INTERSECTING LINES: CORE SYSTEM</text>
          <text x="500" y="70" text-anchor="middle" fill="#94a3b8" font-size="12">NCERT Class 7 Ganita Prakash | Chapter 5 Conceptual Framework</text>

          <!-- Connection Lines from Center -->
          <!-- To Node 1 (Top Left) -->
          <path d="M 500 280 C 400 280, 260 210, 200 160" fill="none" stroke="#38bdf8" stroke-width="3" stroke-dasharray="6,4"/>
          <!-- To Node 2 (Top Right) -->
          <path d="M 500 280 C 600 280, 740 210, 800 160" fill="none" stroke="#2dd4bf" stroke-width="3" stroke-dasharray="6,4"/>
          <!-- To Node 3 (Bottom Left) -->
          <path d="M 500 320 C 400 320, 260 390, 200 450" fill="none" stroke="#c084fc" stroke-width="3" stroke-dasharray="6,4"/>
          <!-- To Node 4 (Bottom Right) -->
          <path d="M 500 320 C 600 320, 740 390, 800 450" fill="none" stroke="#fbbf24" stroke-width="3" stroke-dasharray="6,4"/>

          <!-- CENTRAL CORE HUB -->
          <g class="svg-node" transform="translate(500, 300)">
            <circle r="72" fill="url(#coreGrad)" filter="url(#glow)" stroke="#bae6fd" stroke-width="3"/>
            <text x="0" y="-12" text-anchor="middle" fill="#ffffff" font-size="14" font-weight="800">PLANE</text>
            <text x="0" y="8" text-anchor="middle" fill="#ffffff" font-size="14" font-weight="800">GEOMETRY</text>
            <text x="0" y="26" text-anchor="middle" fill="#bae6fd" font-size="11" font-weight="600">Coplanar Lines</text>
          </g>

          <!-- NODE 1: INTERSECTING LINES & ANGLE RULES (Top Left) -->
          <g class="svg-node" transform="translate(190, 150)">
            <rect x="-140" y="-60" width="280" height="120" rx="14" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
            <rect x="-140" y="-60" width="10" height="120" rx="4" fill="url(#nodeBlue)"/>
            <text x="-120" y="-32" fill="#38bdf8" font-size="14" font-weight="800">1. INTERSECTING LINES</text>
            <text x="-120" y="-10" fill="#f8fafc" font-size="12" font-weight="600">• Meet at exactly ONE point</text>
            <text x="-120" y="10" fill="#f8fafc" font-size="12" font-weight="600">• Linear Pairs: Sum = 180°</text>
            <text x="-120" y="30" fill="#f8fafc" font-size="12" font-weight="600">• Vertically Opposite: Equal (∠a = ∠c)</text>
            <text x="-120" y="48" fill="#94a3b8" font-size="11">Deductive Proof via Linear Pairs</text>
          </g>

          <!-- NODE 2: PERPENDICULAR LINES (Top Right) -->
          <g class="svg-node" transform="translate(810, 150)">
            <rect x="-140" y="-60" width="280" height="120" rx="14" fill="#1e293b" stroke="#2dd4bf" stroke-width="2"/>
            <rect x="-140" y="-60" width="10" height="120" rx="4" fill="url(#nodeTeal)"/>
            <text x="-120" y="-32" fill="#2dd4bf" font-size="14" font-weight="800">2. PERPENDICULAR (⊥)</text>
            <text x="-120" y="-10" fill="#f8fafc" font-size="12" font-weight="600">• All four angles equal (90° each)</text>
            <text x="-120" y="10" fill="#f8fafc" font-size="12" font-weight="600">• Form right angles at intersection</text>
            <text x="-120" y="30" fill="#f8fafc" font-size="12" font-weight="600">• Square angle symbol (⊾)</text>
            <text x="-120" y="48" fill="#94a3b8" font-size="11">Dot grid paper: horizontal ⊥ vertical</text>
          </g>

          <!-- NODE 3: TRANSVERSAL & 8-ANGLE SYSTEM (Bottom Left) -->
          <g class="svg-node" transform="translate(190, 460)">
            <rect x="-140" y="-70" width="280" height="140" rx="14" fill="#1e293b" stroke="#c084fc" stroke-width="2"/>
            <rect x="-140" y="-70" width="10" height="140" rx="4" fill="url(#nodePurple)"/>
            <text x="-120" y="-42" fill="#c084fc" font-size="14" font-weight="800">3. TRANSVERSAL SYSTEM</text>
            <text x="-120" y="-20" fill="#f8fafc" font-size="12" font-weight="600">• Cuts 2 lines at distinct points</text>
            <text x="-120" y="0" fill="#f8fafc" font-size="12" font-weight="600">• Forms 8 angles (Max 4 distinct)</text>
            <text x="-120" y="20" fill="#f8fafc" font-size="12" font-weight="600">• Corresponding: "F-Shape" (Equal)</text>
            <text x="-120" y="40" fill="#f8fafc" font-size="12" font-weight="600">• Alternate Interior: "Z-Shape" (Equal)</text>
            <text x="-120" y="58" fill="#94a3b8" font-size="11">Co-interior: "C-Shape" (Sum = 180°)</text>
          </g>

          <!-- NODE 4: CONSTRUCTIONS & ILLUSIONS (Bottom Right) -->
          <g class="svg-node" transform="translate(810, 460)">
            <rect x="-140" y="-70" width="280" height="140" rx="14" fill="#1e293b" stroke="#fbbf24" stroke-width="2"/>
            <rect x="-140" y="-70" width="10" height="140" rx="4" fill="url(#nodeAmber)"/>
            <text x="-120" y="-42" fill="#fbbf24" font-size="14" font-weight="800">4. GEOMETRY &amp; ILLUSIONS</text>
            <text x="-120" y="-20" fill="#f8fafc" font-size="12" font-weight="600">• Sliding Set-Square Method</text>
            <text x="-120" y="0" fill="#f8fafc" font-size="12" font-weight="600">• Paper Folding: 2ⁿ + 1 Law</text>
            <text x="-120" y="20" fill="#f8fafc" font-size="12" font-weight="600">• Perpendicular to Perpendicular = ∥</text>
            <text x="-120" y="40" fill="#f8fafc" font-size="12" font-weight="600">• Hering &amp; Zöllner Illusions</text>
            <text x="-120" y="58" fill="#94a3b8" font-size="11">Visual Cortex angle overestimation</text>
          </g>
        </svg>
        <div class="diagram-caption">
          <i class="fa-solid fa-circle-info"></i> Figure 1.1: Complete architectural blueprint of Chapter 5 showing the logical connections between coplanar lines, angle pairs, transversals, constructions, and optical illusions.
        </div>
      </div>

      <!-- DETAILED HIERARCHICAL MIND MAP -->
      <h3 class="subheading"><i class="fa-solid fa-network-wired"></i> Exhaustive Hierarchical Mind Map</h3>
      <p>
        The mind map below lays out the complete conceptual tree of the chapter. Every concept is arranged in a logical learning progression, from simple intersections on a flat surface to complex multi-parallel transversal systems and real-world optical phenomena.
      </p>

      <div style="background: #f8fafc; border: 1px solid var(--border); border-radius: var(--radius-lg); padding: 1.75rem; margin-top: 1.5rem;">
        <ul style="list-style: none; padding-left: 0; line-height: 2;">
          <li style="font-weight: 700; font-size: 1.1rem; color: var(--primary-dark);">
            <i class="fa-solid fa-folder-open" style="color: var(--primary);"></i> 1. Lines in a Plane (Samatala / ସମତଳ)
            <ul style="list-style: none; padding-left: 1.5rem; font-weight: 500; font-size: 0.95rem; color: var(--text);">
              <li>🔹 <strong>Plane Surface:</strong> Flat, 2-dimensional boundary extending indefinitely (tabletop, paper sheet, blackboard).</li>
              <li>🔹 <strong>Coplanar Lines:</strong> Lines lying on the same plane. Two coplanar lines either intersect at a single point or are parallel.</li>
              <li>🔹 <strong>Non-Coplanar (Skew) Lines:</strong> Lines in 3-dimensional space that do not lie in the same plane; they never meet, yet they are NOT parallel.</li>
            </ul>
          </li>

          <li style="font-weight: 700; font-size: 1.1rem; color: var(--secondary-dark); margin-top: 1.25rem;">
            <i class="fa-solid fa-folder-open" style="color: var(--secondary);"></i> 2. Intersecting Lines &amp; Angle Theorems (Parasparachedi Saralarekha / ପରସ୍ପରଛେଦୀ ସରଳରେଖା)
            <ul style="list-style: none; padding-left: 1.5rem; font-weight: 500; font-size: 0.95rem; color: var(--text);">
              <li>🔹 <strong>Point of Intersection:</strong> Exactly one shared point where two straight lines cross. (Two straight lines cannot meet at more than one point without coinciding completely).</li>
              <li>🔹 <strong>Four Angles Formed:</strong> Labeled cyclically as ∠a, ∠b, ∠c, ∠d.</li>
              <li>🔹 <strong>Linear Pair (Raikhika Yugma / ରୈଖିକ ଯୁଗ୍ମ):</strong> Adjacent angles on a straight line whose non-common arms form opposite rays: <span class="math-inline">∠a + ∠b = 180°</span>.</li>
              <li>🔹 <strong>Vertically Opposite Angles (Pratipa Kona / ପ୍ରତୀପ କୋଣ):</strong> Non-adjacent opposite angles across the vertex: <span class="math-inline">∠a = ∠c</span> and <span class="math-inline">∠b = ∠d</span>.</li>
              <li>🔹 <strong>Deductive Proof:</strong> Because <span class="math-inline">∠a + ∠b = 180°</span> and <span class="math-inline">∠b + ∠c = 180°</span>, subtracting ∠b from both sides proves <span class="math-inline">∠a = ∠c</span> rigorously without measurement.</li>
              <li>🔹 <strong>Measurement vs Ideal Geometry:</strong> Physical protractor parallax and line thickness create minor measurement errors; geometric deduction provides pure truth.</li>
            </ul>
          </li>

          <li style="font-weight: 700; font-size: 1.1rem; color: var(--accent-dark); margin-top: 1.25rem;">
            <i class="fa-solid fa-folder-open" style="color: var(--accent);"></i> 3. Perpendicular Lines (Paraspara Lamba / ପରସ୍ପର ଲମ୍ବ)
            <ul style="list-style: none; padding-left: 1.5rem; font-weight: 500; font-size: 0.95rem; color: var(--text);">
              <li>🔹 <strong>Right Angle Intersection:</strong> When two intersecting lines form four equal angles: <span class="math-inline">4 × 90° = 360°</span> ⇒ each angle = 90°.</li>
              <li>🔹 <strong>Symbolism &amp; Notation:</strong> Written as <span class="math-inline">l ⊥ m</span> and marked in diagrams with a small square angle symbol (⊾).</li>
              <li>🔹 <strong>Grid &amp; Dot Paper:</strong> Grid lines intersect at 90°; any horizontal line is strictly perpendicular to any vertical line.</li>
            </ul>
          </li>

          <li style="font-weight: 700; font-size: 1.1rem; color: var(--purple-dark); margin-top: 1.25rem;">
            <i class="fa-solid fa-folder-open" style="color: var(--purple);"></i> 4. Parallel Lines &amp; Transversal Mechanics (Samantarala Rekha / ସମାନ୍ତରାଳ ରେଖା)
            <ul style="list-style: none; padding-left: 1.5rem; font-weight: 500; font-size: 0.95rem; color: var(--text);">
              <li>🔹 <strong>Definition:</strong> Coplanar straight lines that never intersect, no matter how far extended in either direction. Written as <span class="math-inline">l ∥ m</span>.</li>
              <li>🔹 <strong>Arrow Notations:</strong> Single arrow (&gt;) for the first set; double arrow (&gt;&gt;) for the second set of parallel lines.</li>
              <li>🔹 <strong>Transversal (Chedaka / ଛେଦକ):</strong> A line t crossing two or more distinct lines, generating 8 angles (4 interior, 4 exterior).</li>
              <li>🔹 <strong>Angle Maximum Law:</strong> When a transversal intersects two lines, it forms 8 angles with a MAXIMUM of 4 distinct measures (due to vertically opposite pairs). When lines are parallel, there are only 2 distinct measures (an acute angle and its supplementary obtuse angle, or 1 measure if all are 90°).</li>
              <li>🔹 <strong>Corresponding Angles (Anurupa Kona / ଅନୁରୂପ କୋଣ - F-Shape):</strong> In matching relative positions. Equal if and only if lines are parallel.</li>
              <li>🔹 <strong>Alternate Interior Angles (Ekantara Antahstha / ଏକାନ୍ତର ଅନ୍ତଃସ୍ଥ - Z-Shape):</strong> On opposite sides of transversal inside the lines. Equal if and only if lines are parallel.</li>
              <li>🔹 <strong>Consecutive Interior Angles (Co-interior / Allied - C-Shape):</strong> On the same side of the transversal inside the lines. Supplementary (Sum = 180°) if and only if lines are parallel.</li>
            </ul>
          </li>

          <li style="font-weight: 700; font-size: 1.1rem; color: #0284c7; margin-top: 1.25rem;">
            <i class="fa-solid fa-folder-open" style="color: #0284c7;"></i> 5. Geometric Constructions &amp; Paper Origami Laws
            <ul style="list-style: none; padding-left: 1.5rem; font-weight: 500; font-size: 0.95rem; color: var(--text);">
              <li>🔹 <strong>Ruler &amp; Sliding Set-Square:</strong> Holding a straightedge ruler stationary and sliding a set square produces parallel lines because corresponding angles remain fixed at 90°.</li>
              <li>🔹 <strong>Unique Parallel Line:</strong> Through any point outside a line, there is exactly one line parallel to the given line (Playfair's Axiom).</li>
              <li>🔹 <strong>Paper Folding Doubling Law:</strong> Folding a sheet horizontally n times creates <span class="math-inline">2ⁿ + 1</span> parallel creases/edges (1 fold = 3 lines, 2 folds = 5 lines, 3 folds = 9 lines, etc.).</li>
              <li>🔹 <strong>Perpendicular Crease Principle:</strong> A line perpendicular to a transversal is parallel to any other line perpendicular to that same transversal.</li>
            </ul>
          </li>

          <li style="font-weight: 700; font-size: 1.1rem; color: #dc2626; margin-top: 1.25rem;">
            <i class="fa-solid fa-folder-open" style="color: #dc2626;"></i> 6. Visual Geometry &amp; Neuro-Illusions (Drushtibhrama / ଦୃଷ୍ଟିଭ୍ରମ)
            <ul style="list-style: none; padding-left: 1.5rem; font-weight: 500; font-size: 0.95rem; color: var(--text);">
              <li>🔹 <strong>Hering Illusion:</strong> Two parallel straight lines appear to bulge outwards when crossed by radiating line segments from a central focal point.</li>
              <li>🔹 <strong>Zöllner Illusion:</strong> Parallel lines appear tilted or converging when crossed by alternating short diagonal hatching slashes.</li>
              <li>🔹 <strong>Poggendorff Illusion:</strong> A continuous transversal segment passing behind an obscuring band appears disjointed or shifted.</li>
              <li>🔹 <strong>Café Wall Illusion:</strong> Perfectly parallel horizontal mortar lines between staggered dark and light tiles appear slanted.</li>
              <li>🔹 <strong>Neuro-Explanation:</strong> Human visual cortex overestimates acute angles (&lt; 90°) and underestimates obtuse angles (&gt; 90°), creating apparent curvature.</li>
            </ul>
          </li>
        </ul>
      </div>
    </section>
"""
