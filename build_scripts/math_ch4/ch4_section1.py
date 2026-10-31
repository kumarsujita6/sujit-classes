# -*- coding: utf-8 -*-
"""
Module: ch4_section1.py
Contains Section 1: Visual Blueprint & Detailed Mind Map
Includes SVG 1: Master Visual Taxonomy & Euler-Venn Blueprint of Quadrilaterals,
the Rigidity Paradox, and architectural taxonomy breakdown.
"""

def get_section_1():
    return """
    <!-- SECTION 1: VISUAL BLUEPRINT & MIND MAP -->
    <section id="section-1">
      <div class="section-header">
        <div class="section-tag"><i class="fa-solid fa-sitemap"></i> Conceptual Architecture</div>
        <h2 class="section-title">Section 1: Visual Blueprint & Detailed Mind Map</h2>
        <p class="section-desc">
          Quadrilaterals form the structural backbone of our physical world—from window frames and doors to architectural trusses and navigational kites. Explore their complete evolutionary taxonomy, symmetry properties, and geometric relationships below.
        </p>
      </div>

      <div class="callout callout-def">
        <div class="callout-title"><i class="fa-solid fa-shapes"></i> The Foundational Nature of 4-Sided Polygons</div>
        <p>
          The word <strong>Quadrilateral</strong> originates from two classical Latin roots: <em>quadri</em> (meaning "four") and <em>latus</em> (meaning "side"). In Euclidean plane geometry, a quadrilateral is defined as a closed two-dimensional figure enclosed by four non-collinear line segments intersecting only at their four endpoints (called <strong>vertices</strong>).
        </p>
        <p>
          Unlike three-sided polygons (triangles), which are naturally <strong>rigid</strong> and cannot change shape without altering side lengths, four-sided figures are inherently <strong>flexible linkages</strong>. A simple hinged rectangular frame can wobble and shear into an infinite family of parallelograms. To lock a quadrilateral into structural rigidity, human engineers and carpenters must introduce a <strong>diagonal brace</strong>, triangulating the interior space into two rigid triangles!
        </p>
      </div>

      <h3 class="subheading"><i class="fa-solid fa-diagram-project"></i> Master Visual Taxonomy & Euler-Venn Hierarchy</h3>
      <p>
        The following responsive diagram displays the complete taxonomic hierarchy and nested classification of quadrilaterals. Notice how adding geometric constraints (parallelism, right angles, equal sides) narrows the classification down from an arbitrary four-sided polygon to the ultimate geometric perfection: the <strong>Square</strong>.
      </p>

      <!-- SVG DIAGRAM 1: MASTER TAXONOMY & EULER-VENN BLUEPRINT -->
      <div class="diagram-card">
        <div class="svg-container">
          <svg viewBox="0 0 960 560" xmlns="http://www.w3.org/2000/svg" style="background:#f8fafc; border-radius:12px; font-family:'Space Grotesk', sans-serif;">
            <defs>
              <linearGradient id="gradQuad" x1="0%" y1="0%" x2="100%" y2="100%">
                <stop offset="0%" stop-color="#3b82f6" stop-opacity="0.12"/>
                <stop offset="100%" stop-color="#1d4ed8" stop-opacity="0.2"/>
              </linearGradient>
              <linearGradient id="gradTrap" x1="0%" y1="0%" x2="100%" y2="100%">
                <stop offset="0%" stop-color="#f59e0b" stop-opacity="0.15"/>
                <stop offset="100%" stop-color="#d97706" stop-opacity="0.25"/>
              </linearGradient>
              <linearGradient id="gradPara" x1="0%" y1="0%" x2="100%" y2="100%">
                <stop offset="0%" stop-color="#10b981" stop-opacity="0.15"/>
                <stop offset="100%" stop-color="#059669" stop-opacity="0.25"/>
              </linearGradient>
              <linearGradient id="gradRect" x1="0%" y1="0%" x2="100%" y2="100%">
                <stop offset="0%" stop-color="#06b6d4" stop-opacity="0.2"/>
                <stop offset="100%" stop-color="#0891b2" stop-opacity="0.3"/>
              </linearGradient>
              <linearGradient id="gradRhom" x1="0%" y1="0%" x2="100%" y2="100%">
                <stop offset="0%" stop-color="#8b5cf6" stop-opacity="0.2"/>
                <stop offset="100%" stop-color="#7c3aed" stop-opacity="0.3"/>
              </linearGradient>
              <linearGradient id="gradSquare" x1="0%" y1="0%" x2="100%" y2="100%">
                <stop offset="0%" stop-color="#ec4899" stop-opacity="0.3"/>
                <stop offset="100%" stop-color="#be185d" stop-opacity="0.45"/>
              </linearGradient>
              <linearGradient id="gradKite" x1="0%" y1="0%" x2="100%" y2="100%">
                <stop offset="0%" stop-color="#f43f5e" stop-opacity="0.12"/>
                <stop offset="100%" stop-color="#e11d48" stop-opacity="0.22"/>
              </linearGradient>
              <filter id="shadowBox" x="-5%" y="-5%" width="110%" height="110%">
                <feDropShadow dx="0" dy="4" stdDeviation="4" flood-opacity="0.08"/>
              </filter>
            </defs>

            <!-- Title -->
            <text x="480" y="38" text-anchor="middle" font-size="22" font-weight="800" fill="#0f172a">MASTER TAXONOMY & EULER-VENN BLUEPRINT OF QUADRILATERALS</text>
            <text x="480" y="60" text-anchor="middle" font-size="13" font-weight="500" fill="#64748b">Ganita Prakash Class 8 Chapter 4 - Complete Hierarchical Classification</text>

            <!-- OUTER ENCLOSURE: ALL QUADRILATERALS -->
            <rect x="25" y="80" width="910" height="460" rx="20" fill="url(#gradQuad)" stroke="#2563eb" stroke-width="2" stroke-dasharray="6,4" filter="url(#shadowBox)"/>
            <text x="50" y="112" font-size="16" font-weight="800" fill="#1d4ed8"><tspan fill="#2563eb">●</tspan> ALL QUADRILATERALS (4-Sided Closed Polygons, Angle Sum = 360°)</text>

            <!-- LEFT REGION: KITE FAMILY -->
            <rect x="50" y="135" width="220" height="380" rx="16" fill="url(#gradKite)" stroke="#e11d48" stroke-width="1.8" filter="url(#shadowBox)"/>
            <text x="70" y="165" font-size="15" font-weight="700" fill="#9f1239">KITE FAMILY</text>
            <text x="70" y="185" font-size="12" fill="#be123c">2 pairs adjacent equal sides</text>
            <text x="70" y="202" font-size="12" fill="#be123c">Diagonals perpendicular (⊥)</text>
            <text x="70" y="219" font-size="12" fill="#be123c">1 diagonal bisects the other</text>
            <text x="70" y="236" font-size="12" fill="#be123c">1 axis of reflection symmetry</text>

            <!-- Kite Miniature Icon -->
            <polygon points="160,260 195,310 160,390 125,310" fill="#ffe4e6" stroke="#e11d48" stroke-width="2"/>
            <line x1="160" y1="260" x2="160" y2="390" stroke="#9f1239" stroke-width="1.5" stroke-dasharray="3,3"/>
            <line x1="125" y1="310" x2="195" y2="310" stroke="#9f1239" stroke-width="1.5" stroke-dasharray="3,3"/>
            <text x="160" y="415" text-anchor="middle" font-size="12" font-weight="700" fill="#9f1239">General Kite (AB=AD, CB=CD)</text>

            <!-- Overlap notice between Kite & Rhombus -->
            <rect x="65" y="435" width="190" height="65" rx="8" fill="#ffffff" stroke="#f43f5e" stroke-width="1"/>
            <text x="75" y="455" font-size="11" font-weight="700" fill="#9f1239">Special Case Overlap:</text>
            <text x="75" y="472" font-size="10.5" fill="#475569">If all 4 sides become equal,</text>
            <text x="75" y="488" font-size="10.5" font-weight="700" fill="#7c3aed">the Kite becomes a Rhombus!</text>

            <!-- RIGHT REGION: TRAPEZIUM ENCLOSURE -->
            <rect x="295" y="135" width="620" height="380" rx="16" fill="url(#gradTrap)" stroke="#d97706" stroke-width="1.8" filter="url(#shadowBox)"/>
            <text x="315" y="165" font-size="15" font-weight="700" fill="#92400e">TRAPEZIUM FAMILY (At least one pair of parallel opposite sides)</text>
            <text x="315" y="185" font-size="12" fill="#b45309">Consecutive co-interior angles add to 180° (∠A+∠D=180°, ∠B+∠C=180°)</text>

            <!-- Isosceles Trapezium Sub-box -->
            <rect x="315" y="200" width="180" height="150" rx="10" fill="#fef3c7" stroke="#b45309" stroke-width="1.5"/>
            <text x="325" y="222" font-size="12.5" font-weight="700" fill="#78350f">Isosceles Trapezium</text>
            <text x="325" y="240" font-size="11" fill="#92400e">• Non-parallel legs equal</text>
            <text x="325" y="255" font-size="11" fill="#92400e">• Base angles equal</text>
            <text x="325" y="270" font-size="11" fill="#92400e">• Diagonals equal in length</text>
            <!-- Mini Isosceles Trapezium -->
            <polygon points="350,325 460,325 440,290 370,290" fill="#fde68a" stroke="#78350f" stroke-width="1.5"/>
            <text x="405" y="342" text-anchor="middle" font-size="10.5" font-weight="600" fill="#78350f">AD = BC, AB ∥ DC</text>

            <!-- PARALLELOGRAM ENCLOSURE (Inside Trapezium) -->
            <rect x="510" y="200" width="385" height="300" rx="14" fill="url(#gradPara)" stroke="#059669" stroke-width="2" filter="url(#shadowBox)"/>
            <text x="525" y="226" font-size="14.5" font-weight="700" fill="#065f46">PARALLELOGRAM (Both pairs opposite sides ∥)</text>
            <text x="525" y="244" font-size="11" fill="#047857">• Opposite sides equal &amp; parallel | • Opposite angles equal</text>
            <text x="525" y="259" font-size="11" fill="#047857">• Adjacent angles supplementary (180°) | • Diagonals bisect each other</text>

            <!-- SUB-BOX: RECTANGLE -->
            <rect x="525" y="275" width="170" height="135" rx="10" fill="url(#gradRect)" stroke="#0891b2" stroke-width="1.6"/>
            <text x="535" y="298" font-size="13" font-weight="700" fill="#155e75">RECTANGLE</text>
            <text x="535" y="315" font-size="10.5" fill="#0e7490">• All 4 angles = 90°</text>
            <text x="535" y="330" font-size="10.5" fill="#0e7490">• Diagonals are EQUAL</text>
            <text x="535" y="345" font-size="10.5" fill="#0e7490">• Diagonals bisect each other</text>
            <!-- Mini rectangle -->
            <rect x="560" y="355" width="80" height="42" fill="#cffafe" stroke="#0891b2" stroke-width="1.5"/>
            <text x="600" y="380" text-anchor="middle" font-size="10" font-weight="600" fill="#164e63">All ∠ = 90°</text>

            <!-- SUB-BOX: RHOMBUS -->
            <rect x="710" y="275" width="170" height="135" rx="10" fill="url(#gradRhom)" stroke="#7c3aed" stroke-width="1.6"/>
            <text x="720" y="298" font-size="13" font-weight="700" fill="#581c87">RHOMBUS</text>
            <text x="720" y="315" font-size="10.5" fill="#6d28d9">• All 4 sides EQUAL</text>
            <text x="720" y="330" font-size="10.5" fill="#6d28d9">• Diagonals ⊥ at 90°</text>
            <text x="720" y="345" font-size="10.5" fill="#6d28d9">• Diagonals bisect angles</text>
            <!-- Mini rhombus -->
            <polygon points="795,355 835,376 795,397 755,376" fill="#ede9fe" stroke="#7c3aed" stroke-width="1.5"/>
            <text x="795" y="380" text-anchor="middle" font-size="10" font-weight="600" fill="#4c1d95">a = b = c = d</text>

            <!-- INTERSECTION: SQUARE -->
            <rect x="590" y="420" width="230" height="70" rx="10" fill="url(#gradSquare)" stroke="#be185d" stroke-width="2.2" filter="url(#shadowBox)"/>
            <text x="705" y="443" text-anchor="middle" font-size="14" font-weight="800" fill="#831843">★ SQUARE (Rectangle ∩ Rhombus) ★</text>
            <text x="705" y="460" text-anchor="middle" font-size="10.5" fill="#9d174d">Equilateral (all sides =) &amp; Equiangular (all angles = 90°)</text>
            <text x="705" y="476" text-anchor="middle" font-size="10.5" font-weight="700" fill="#701a75">Diagonals: EQUAL, BISECT at 90°, BISECT Angles (45°-45°)</text>

            <!-- Connector arrows showing Square inheritance -->
            <line x1="610" y1="410" x2="635" y2="420" stroke="#0891b2" stroke-width="2" marker-end="url(#arrow)"/>
            <line x1="795" y1="410" x2="770" y2="420" stroke="#7c3aed" stroke-width="2" marker-end="url(#arrow)"/>
          </svg>
        </div>
        <p class="caption">
          <strong>Figure 1.1:</strong> Complete Taxonomic Tree of Quadrilaterals. Notice that every square is simultaneously a rectangle, a rhombus, a parallelogram, a trapezium, and a kite!
        </p>
      </div>

      <h3 class="subheading"><i class="fa-solid fa-network-wired"></i> Detailed Mind Map: The Four Structural Pillars</h3>
      <p>
        To truly master Grade 8 geometry without getting lost in definitions, keep the following <strong>Four Structural Pillars</strong> in mind:
      </p>

      <div class="table-container">
        <table class="data-table">
          <thead>
            <tr>
              <th>Structural Pillar</th>
              <th>Key Geometric Principle</th>
              <th>How It Applies to Quadrilaterals</th>
              <th>NCERT Ganita Prakash Reference</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>1. Angle Sum Pillar</strong></td>
              <td>Universal interior sum = 360°</td>
              <td>Splitting any quadrilateral into two triangles with a single diagonal gives 180° + 180° = 360°. This holds true for both convex and concave quadrilaterals!</td>
              <td>Section 4.2 (Pages 94–95)</td>
            </tr>
            <tr>
              <td><strong>2. Parallelism Pillar</strong></td>
              <td>Transversal Co-Interior &amp; Alternate Angles</td>
              <td>Parallel sides force consecutive interior angles to sum to 180° and force alternate interior angles along diagonals to be equal, creating congruent triangles.</td>
              <td>Section 4.1 &amp; 4.3 (Pages 89, 96–97)</td>
            </tr>
            <tr>
              <td><strong>3. Congruence Pillar</strong></td>
              <td>SAS, ASA, AAS, SSS, and RHS Proofs</td>
              <td>Diagonals divide quadrilaterals into congruent triangles. CPCTC (Corresponding Parts of Congruent Triangles are Congruent) proves side equalities and diagonal bisection.</td>
              <td>Deductions 1, 2, 4, 7, 8, 10</td>
            </tr>
            <tr>
              <td><strong>4. Diagonal Behavior Pillar</strong></td>
              <td>Diagonals as Structural Fingerprints</td>
              <td>Each special quadrilateral has a unique diagonal signature: equal in rectangles; perpendicular in rhombuses &amp; kites; perpendicular bisectors of equal length in squares!</td>
              <td>Deductions 1, 2, 3, 5, 8, 10</td>
            </tr>
          </tbody>
        </table>
      </div>

      <div class="callout callout-hack">
        <div class="callout-title"><i class="fa-solid fa-wand-magic-sparkles"></i> Teacher's Golden Classification Trick</div>
        <p>
          Whenever an exam question asks: <em>"Is Every X a Y?"</em>, always check the <strong>conditions</strong>:
        </p>
        <ul>
          <li><strong>Moving UP the tree (Specific → General): ALWAYS TRUE!</strong> Every Square is a Rectangle. Every Rectangle is a Parallelogram. Every Parallelogram is a Trapezium.</li>
          <li><strong>Moving DOWN the tree (General → Specific): FALSE!</strong> Not every Parallelogram is a Rectangle (it needs four 90° angles). Not every Rectangle is a Square (it needs equal sides).</li>
        </ul>
      </div>
    </section>
"""
