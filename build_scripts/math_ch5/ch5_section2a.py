# -*- coding: utf-8 -*-
"""Part 3: Section 2 Part A - Line-by-Line Conceptual Explanations (5.1 to 5.4) & SVGs 2 & 3."""

SECTION2A_CONTENT = """
    <!-- SECTION 2: LINE-BY-LINE CONCEPTUAL EXPLANATIONS (PART A) -->
    <section id="concepts" class="section-card">
      <div class="section-header">
        <div class="section-icon-box">
          <i class="fa-solid fa-book-reader"></i>
        </div>
        <div>
          <h2 class="section-title">Section 2: Complete Line-by-Line Conceptual Explanations</h2>
          <p class="section-tagline">Detailed, student-friendly pedagogical breakdown of every topic, theorem, proof, and activity in NCERT Chapter 5</p>
        </div>
      </div>

      <!-- SUBSECTION 5.1 -->
      <h3 class="subheading"><i class="fa-solid fa-crosshairs"></i> 5.1 Across the Line: The Geometry of Intersecting Lines</h3>
      <p>
        Let us start with a simple, playful experiment. Take a plain square sheet of paper and fold it in different directions. When you unfold the paper, look at the creases pressed into the sheet. Using a pencil and a wooden ruler, draw straight lines right along those creases. You will immediately see lines running in different directions across your paper.
      </p>
      <p>
        Now, pick any two lines. Look closely at how they relate to each other:
      </p>
      <ul style="margin-left: 2rem; margin-bottom: 1.25rem;">
        <li>Do they touch or cross each other on the sheet of paper?</li>
        <li>If they do not meet on the sheet right now, would they meet if we extended both lines outward, past the edges of the paper onto a wide tabletop?</li>
      </ul>

      <div class="callout callout-def">
        <div class="callout-title"><i class="fa-solid fa-layer-group"></i> What is a Plane Surface?</div>
        <p>
          In geometry, a <strong>plane surface</strong> (or simply a <strong>plane</strong>) is a perfectly flat, smooth surface that extends endlessly in all two dimensions (length and breadth), with zero thickness. Everyday examples around us include a flat tabletop, a sheet of paper, the classroom chalkboard, a window pane, and a smooth tiled floor. In this entire chapter, we explore how straight lines behave when drawn on the <em>very same plane surface</em>.
        </p>
      </div>

      <h4 class="topic-head"><i class="fa-solid fa-arrows-split-up-and-left"></i> What Happens When Two Straight Lines Meet?</h4>
      <p>
        When two straight lines meet each other on a plane surface, they cross at a single, shared point. We say that the two lines <strong>intersect</strong> each other, and the shared point where they cross is called the <strong>point of intersection</strong>.
      </p>

      <div class="callout callout-warn">
        <div class="callout-title"><i class="fa-solid fa-circle-question"></i> Critical Thought Question: Can Two Straight Lines Intersect at More Than One Point?</div>
        <p>
          <strong>Answer: Absolutely NO!</strong> Two distinct straight lines can intersect at <strong>at most one single point</strong>.
        </p>
        <p>
          <em>Why is this so?</em> Think about what a straight line is. A straight line never curves, bends, or turns around. Once two straight lines meet at a point and cross each other, they move further and further apart forever. If two lines met at a second point, at least one of them would have to curve back to touch the other. But then it would no longer be a straight line! If two straight lines share two or more points, they must be the exact same line placed on top of itself (coincident lines).
        </p>
      </div>

      <h4 class="topic-head"><i class="fa-solid fa-chart-pie"></i> The Four Angles Formed by Two Intersecting Lines</h4>
      <p>
        Whenever two straight lines, say line <span class="math-inline">l</span> and line <span class="math-inline">m</span>, intersect each other, they carve the surrounding flat space into <strong>four distinct angles</strong> around the point of intersection. Let us label these four angles cyclically in order: <span class="math-inline">∠a</span>, <span class="math-inline">∠b</span>, <span class="math-inline">∠c</span>, and <span class="math-inline">∠d</span>.
      </p>

      <!-- INLINE SVG 2: TWO INTERSECTING LINES (LINEAR PAIR & VERTICALLY OPPOSITE) -->
      <div class="diagram-card">
        <svg viewBox="0 0 700 420" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg" style="max-width: 650px; font-family: 'Plus Jakarta Sans', sans-serif;">
          <defs>
            <marker id="arrowHeadBlue" markerWidth="8" markerHeight="8" refX="5" refY="4" orient="auto">
              <path d="M 1 1 L 7 4 L 1 7 Z" fill="#0284c7" />
            </marker>
            <marker id="arrowHeadTeal" markerWidth="8" markerHeight="8" refX="5" refY="4" orient="auto">
              <path d="M 1 1 L 7 4 L 1 7 Z" fill="#0d9488" />
            </marker>
          </defs>

          <!-- Background Box -->
          <rect width="700" height="420" rx="16" fill="#f8fafc" stroke="#e2e8f0" stroke-width="2"/>

          <!-- Title -->
          <text x="350" y="32" text-anchor="middle" fill="#0f172a" font-size="16" font-weight="700">Two Intersecting Lines: Angle Architecture</text>
          <text x="350" y="52" text-anchor="middle" fill="#64748b" font-size="12">Linear Pairs (Sum = 180°) &amp; Vertically Opposite Angles (Equal)</text>

          <!-- Line l (Slope down-right) -->
          <line x1="80" y1="120" x2="620" y2="300" stroke="#0284c7" stroke-width="3.5" marker-start="url(#arrowHeadBlue)" marker-end="url(#arrowHeadBlue)"/>
          <text x="635" y="305" fill="#0284c7" font-weight="800" font-size="16">l</text>

          <!-- Line m (Slope up-right) -->
          <line x1="120" y1="340" x2="580" y2="80" stroke="#0d9488" stroke-width="3.5" marker-start="url(#arrowHeadTeal)" marker-end="url(#arrowHeadTeal)"/>
          <text x="595" y="85" fill="#0d9488" font-weight="800" font-size="16">m</text>

          <!-- Intersection Point O -->
          <circle cx="350" cy="210" r="6" fill="#0f172a"/>
          <text x="350" y="235" text-anchor="middle" fill="#0f172a" font-weight="700" font-size="14">O</text>

          <!-- Angle Arcs and Shading -->
          <!-- Top Angle: a (Obtuse ~120°) -->
          <path d="M 390 188 A 45 45 0 0 0 310 197" fill="none" stroke="#7c3aed" stroke-width="3"/>
          <circle cx="350" cy="155" r="18" fill="#ede9fe" stroke="#7c3aed" stroke-width="1.5"/>
          <text x="350" y="161" text-anchor="middle" fill="#6d28d9" font-weight="800" font-size="14">∠a</text>

          <!-- Right Angle: b (Acute ~60°) -->
          <path d="M 410 230 A 45 45 0 0 0 390 188" fill="none" stroke="#d97706" stroke-width="3"/>
          <circle cx="430" cy="210" r="18" fill="#fef3c7" stroke="#d97706" stroke-width="1.5"/>
          <text x="430" y="216" text-anchor="middle" fill="#b45309" font-weight="800" font-size="14">∠b</text>

          <!-- Bottom Angle: c (Obtuse ~120°) -->
          <path d="M 310 223 A 45 45 0 0 0 390 232" fill="none" stroke="#7c3aed" stroke-width="3"/>
          <circle cx="350" cy="265" r="18" fill="#ede9fe" stroke="#7c3aed" stroke-width="1.5"/>
          <text x="350" y="271" text-anchor="middle" fill="#6d28d9" font-weight="800" font-size="14">∠c</text>

          <!-- Left Angle: d (Acute ~60°) -->
          <path d="M 290 190 A 45 45 0 0 0 310 223" fill="none" stroke="#d97706" stroke-width="3"/>
          <circle cx="270" cy="210" r="18" fill="#fef3c7" stroke="#d97706" stroke-width="1.5"/>
          <text x="270" y="216" text-anchor="middle" fill="#b45309" font-weight="800" font-size="14">∠d</text>

          <!-- Explanatory Labels Box -->
          <g transform="translate(50, 340)">
            <rect width="600" height="60" rx="8" fill="#ffffff" stroke="#cbd5e1" stroke-width="1"/>
            <text x="20" y="25" fill="#6d28d9" font-size="12" font-weight="700">VERTICALLY OPPOSITE PAIRS: ∠a = ∠c (purple) and ∠b = ∠d (amber)</text>
            <text x="20" y="45" fill="#0369a1" font-size="12" font-weight="700">LINEAR PAIRS: ∠a + ∠b = 180°,  ∠b + ∠c = 180°,  ∠c + ∠d = 180°,  ∠d + ∠a = 180°</text>
          </g>
        </svg>
        <div class="diagram-caption">
          <i class="fa-solid fa-circle-info"></i> Figure 2.1: The four angles formed at the intersection of lines l and m. Opposite angles share identical colors, while any two adjacent angles form a straight line of 180°.
        </div>
      </div>

      <h4 class="topic-head"><i class="fa-solid fa-calculator"></i> Step-by-Step Numerical Discovery (Activity 1)</h4>
      <p>
        Imagine you measure <span class="math-inline">∠a</span> with a protractor and find it measures <span class="math-inline">120°</span>. Can you find the values of <span class="math-inline">∠b</span>, <span class="math-inline">∠c</span>, and <span class="math-inline">∠d</span> without touching your protractor again?
      </p>
      <p>
        <strong>Yes, absolutely!</strong> Let us trace the logic:
      </p>
      <ol style="margin-left: 2rem; margin-bottom: 1.25rem;">
        <li>
          <strong>Finding ∠b:</strong> Angles <span class="math-inline">∠a</span> and <span class="math-inline">∠b</span> lie side by side along the straight line <span class="math-inline">l</span>. Together, they form a straight angle, which measures exactly <span class="math-inline">180°</span>.
          <div class="math-display">
            ∠a + ∠b = 180°<br>
            120° + ∠b = 180° ⇒ ∠b = 180° - 120° = 60°
          </div>
        </li>
        <li>
          <strong>Finding ∠c:</strong> Now look at line <span class="math-inline">m</span>. Angles <span class="math-inline">∠b</span> and <span class="math-inline">∠c</span> lie side by side along line <span class="math-inline">m</span>. Therefore, they must also form a straight angle of <span class="math-inline">180°</span>.
          <div class="math-display">
            ∠b + ∠c = 180°<br>
            60° + ∠c = 180° ⇒ ∠c = 180° - 60° = 120°
          </div>
        </li>
        <li>
          <strong>Finding ∠d:</strong> Looking again along line <span class="math-inline">l</span>, angles <span class="math-inline">∠c</span> and <span class="math-inline">∠d</span> form a straight angle of <span class="math-inline">180°</span>.
          <div class="math-display">
            ∠c + ∠d = 180°<br>
            120° + ∠d = 180° ⇒ ∠d = 180° - 120° = 60°
          </div>
        </li>
      </ol>
      <p>
        Notice what just happened:
      </p>
      <div class="math-display">
        ∠a = ∠c = 120°  (Opposite to each other)<br>
        ∠b = ∠d = 60°   (Opposite to each other)
      </div>

      <div class="callout callout-hack">
        <div class="callout-title"><i class="fa-solid fa-graduation-cap"></i> Rigorous Mathematical Proof: Why Vertically Opposite Angles are Always Equal</div>
        <p>
          Does this property work for <em>any</em> angles, even if <span class="math-inline">∠a</span> is not 120°? Let us write a pure algebraic proof without assuming any number:
        </p>
        <div class="math-display">
          1. ∠a + ∠b = 180°  (Linear pair along straight line l)<br>
          2. ∠b + ∠c = 180°  (Linear pair along straight line m)<br><br>
          Since both sums equal 180°, we equate them:<br>
          ∠a + ∠b = ∠b + ∠c<br><br>
          Subtract ∠b from both sides of the equation:<br>
          ∠a + ∠b - ∠b = ∠b + ∠c - ∠b<br>
          ⇒ <strong>∠a = ∠c</strong>  [PROVED!]<br><br>
          In the exact same way:<br>
          ∠a + ∠b = 180°  and  ∠a + ∠d = 180°<br>
          ⇒ ∠a + ∠b = ∠a + ∠d<br>
          Subtract ∠a from both sides:<br>
          ⇒ <strong>∠b = ∠d</strong>  [PROVED!]
        </div>
        <p>
          Such a logical, undeniable chain of reasoning in mathematics is called a <strong>formal proof</strong>. It guarantees that the property holds true for every pair of intersecting straight lines in the universe!
        </p>
      </div>

      <h4 class="topic-head"><i class="fa-solid fa-microscope"></i> Measurements vs Pure Geometry: Why Protractors Sometimes "Lie"</h4>
      <p>
        When you measure the angles of intersecting lines on paper with a plastic protractor, you might find that <span class="math-inline">∠a + ∠b</span> adds up to <span class="math-inline">179°</span> or <span class="math-inline">181°</span>. Does that mean our mathematical law is wrong?
      </p>
      <p>
        <strong>Not at all!</strong> The discrepancy arises from real-world physical limitations:
      </p>
      <ul style="margin-left: 2rem; margin-bottom: 1.25rem;">
        <li><strong>Thickness of Drawn Lines:</strong> An "ideal" mathematical line has exactly <em>zero width</em>. But when you draw a line with a graphite pencil, the mark has a thickness of 0.5 mm to 1 mm! That graphite width introduces small angular uncertainties.</li>
        <li><strong>Protractor Parallax &amp; Tool Error:</strong> Aligning the center point and baseline of a school protractor by eye is subject to human eyesight limits and viewing angle (parallax).</li>
      </ul>
      <p>
        In mathematics, we reason with <em>ideal geometric lines</em>. While physical measurements are close approximations, mathematical deductions give the exact, eternal truth. Because physical measurements come so close to theoretical predictions, this geometry forms the backbone of architecture, civil engineering, robotics, and aerospace navigation!
      </p>

      <!-- SUBSECTION 5.2 -->
      <h3 class="subheading"><i class="fa-solid fa-shapes"></i> 5.2 Perpendicular Lines: When Intersecting Lines Form Right Angles</h3>
      <p>
        Can two straight lines intersect such that <strong>all four angles are completely equal</strong>?
      </p>
      <p>
        Let us test this mathematically. Suppose all four angles are equal to an unknown measure, say <span class="math-inline">x</span>. The four angles make a full complete turn around the intersection point, adding up to <span class="math-inline">360°</span>.
      </p>
      <div class="math-display">
        x + x + x + x = 360°<br>
        4x = 360° ⇒ x = 360° ÷ 4 = 90°
      </div>
      <p>
        Every single angle must measure exactly <strong>90°</strong> (a right angle)!
      </p>

      <div class="callout callout-def">
        <div class="callout-title"><i class="fa-solid fa-ruler-combined"></i> Definition: Perpendicular Lines (Paraspara Lamba / ପରସ୍ପର ଲମ୍ବ)</div>
        <p>
          Two lines are said to be <strong>perpendicular</strong> to each other if they intersect at a <strong>right angle (90°)</strong>. If line <span class="math-inline">l</span> is perpendicular to line <span class="math-inline">m</span>, we write it mathematically using the symbol <span class="math-inline">⊥</span>:
        </p>
        <div class="math-display" style="text-align: center;">
          <strong>l ⊥ m</strong> &nbsp;&nbsp;(Read as: "Line l is perpendicular to line m")
        </div>
        <p>
          In geometric diagrams, a right angle is always indicated by drawing a small square symbol (⊾) nestled at the corner of intersection instead of a curved arc.
        </p>
      </div>

      <!-- INLINE SVG 3: PERPENDICULAR LINES & SQUARE ORTHOGONAL MARKERS -->
      <div class="diagram-card">
        <svg viewBox="0 0 650 380" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg" style="max-width: 600px; font-family: 'Plus Jakarta Sans', sans-serif;">
          <defs>
            <marker id="arrRed" markerWidth="8" markerHeight="8" refX="5" refY="4" orient="auto">
              <path d="M 1 1 L 7 4 L 1 7 Z" fill="#dc2626" />
            </marker>
            <marker id="arrBlue" markerWidth="8" markerHeight="8" refX="5" refY="4" orient="auto">
              <path d="M 1 1 L 7 4 L 1 7 Z" fill="#0284c7" />
            </marker>
          </defs>

          <!-- Canvas Card -->
          <rect width="650" height="380" rx="16" fill="#f8fafc" stroke="#e2e8f0" stroke-width="2"/>

          <!-- Title -->
          <text x="325" y="32" text-anchor="middle" fill="#0f172a" font-size="16" font-weight="700">Perpendicular Lines: Orthogonal Geometry (l ⊥ m)</text>
          <text x="325" y="52" text-anchor="middle" fill="#64748b" font-size="12">All four angles equal 90° | Marked by square angle symbols</text>

          <!-- Background Subtle Grid -->
          <g stroke="#e2e8f0" stroke-width="1" stroke-dasharray="3,3">
            <line x1="125" y1="70" x2="125" y2="330"/>
            <line x1="225" y1="70" x2="225" y2="330"/>
            <line x1="425" y1="70" x2="425" y2="330"/>
            <line x1="525" y1="70" x2="525" y2="330"/>
            <line x1="75" y1="100" x2="575" y2="100"/>
            <line x1="75" y1="300" x2="575" y2="300"/>
          </g>

          <!-- Horizontal Line l -->
          <line x1="80" y1="200" x2="570" y2="200" stroke="#0284c7" stroke-width="4" marker-start="url(#arrBlue)" marker-end="url(#arrBlue)"/>
          <text x="585" y="205" fill="#0284c7" font-weight="800" font-size="16">l</text>

          <!-- Vertical Line m -->
          <line x1="325" y1="70" x2="325" y2="330" stroke="#dc2626" stroke-width="4" marker-start="url(#arrRed)" marker-end="url(#arrRed)"/>
          <text x="330" y="65" fill="#dc2626" font-weight="800" font-size="16">m</text>

          <!-- Intersection Center -->
          <circle cx="325" cy="200" r="5" fill="#0f172a"/>
          <text x="312" y="220" fill="#0f172a" font-weight="700" font-size="13">O</text>

          <!-- Square Right Angle Symbols in all 4 Quadrants -->
          <!-- Quadrant 1 (Top-Right) -->
          <rect x="325" y="170" width="30" height="30" fill="#e0f2fe" stroke="#0284c7" stroke-width="2"/>
          <text x="375" y="185" fill="#0369a1" font-size="13" font-weight="800">90°</text>

          <!-- Quadrant 2 (Top-Left) -->
          <rect x="295" y="170" width="30" height="30" fill="#fee2e2" stroke="#dc2626" stroke-width="2"/>
          <text x="255" y="185" fill="#b91c1c" font-size="13" font-weight="800">90°</text>

          <!-- Quadrant 3 (Bottom-Left) -->
          <rect x="295" y="200" width="30" height="30" fill="#e0f2fe" stroke="#0284c7" stroke-width="2"/>
          <text x="255" y="235" fill="#0369a1" font-size="13" font-weight="800">90°</text>

          <!-- Quadrant 4 (Bottom-Right) -->
          <rect x="325" y="200" width="30" height="30" fill="#fee2e2" stroke="#dc2626" stroke-width="2"/>
          <text x="375" y="235" fill="#b91c1c" font-size="13" font-weight="800">90°</text>
        </svg>
        <div class="diagram-caption">
          <i class="fa-solid fa-circle-info"></i> Figure 2.2: Line l is perpendicular to line m (l ⊥ m). Notice the four square right-angle markers at the intersection point O.
        </div>
      </div>

      <!-- SUBSECTION 5.3 -->
      <h3 class="subheading"><i class="fa-solid fa-grip-lines-vertical"></i> 5.3 Between Lines: Line Segments on a Plane</h3>
      <p>
        In our surroundings, lines do not always continue endlessly. Often, we deal with <strong>line segments</strong> (portions of lines bounded by two definite endpoints) or <strong>rays</strong> (starting at an endpoint and extending infinitely in one direction).
      </p>
      <p>
        Let us observe how different pairs of line segments behave when drawn on a plane:
      </p>
      <ul style="margin-left: 2rem; margin-bottom: 1.25rem;">
        <li><strong>Meeting at an Endpoint:</strong> Two line segments can meet directly at an endpoint to form a corner or angle. For example, in the textbook Fig. 5.5, line segments <span class="math-inline">FG</span> and <span class="math-inline">FH</span> meet at common endpoint <span class="math-inline">F</span> at an angle of <span class="math-inline">115.3°</span>.</li>
        <li><strong>Meeting When Extended (Converging Lines):</strong> Two line segments may not touch right now, but if you lay a ruler along them and extend their paths, they draw closer and closer together until they cross at an intersection point. For example, line segments <span class="math-inline">ST</span> and <span class="math-inline">UV</span> in Fig. 5.5 point toward each other and will intersect when extended.</li>
        <li><strong>Never Meeting When Extended (Disjoint Lines):</strong> Line segments like <span class="math-inline">OP</span> and <span class="math-inline">QR</span> maintain a constant separation. No matter how far you extend them in either direction, they never cross.</li>
      </ul>

      <!-- SUBSECTION 5.4 -->
      <h3 class="subheading"><i class="fa-solid fa-equals"></i> 5.4 Parallel Lines in the Plane &amp; Paper Folding Geometry</h3>
      <p>
        Lines that remain at the exact same distance from each other across their entire length and never meet are given a special, honored name in mathematics: <strong>Parallel Lines</strong>.
      </p>

      <div class="callout callout-def">
        <div class="callout-title"><i class="fa-solid fa-road"></i> Definition: Parallel Lines (Samantarala Saralarekha / ସମାନ୍ତରାଳ ସରଳରେଖା)</div>
        <p>
          <strong>Parallel lines</strong> are a pair of straight lines that:
        </p>
        <ol style="margin-left: 1.5rem; margin-top: 0.5rem;">
          <li>Lie in the <strong>very same flat plane</strong> (coplanar), AND</li>
          <li><strong>Never intersect or meet</strong>, no matter how far they are extended in both directions.</li>
        </ol>
        <p style="margin-top: 0.75rem;">
          If line <span class="math-inline">l</span> is parallel to line <span class="math-inline">m</span>, we write it using the double-bar symbol <span class="math-inline">∥</span>:
        </p>
        <div class="math-display" style="text-align: center;">
          <strong>l ∥ m</strong> &nbsp;&nbsp;(Read as: "Line l is parallel to line m")
        </div>
      </div>

      <div class="callout callout-warn">
        <div class="callout-title"><i class="fa-solid fa-triangle-exclamation"></i> The Essential Teacher's Warning: Why Coplanarity is Non-Negotiable!</div>
        <p>
          Students often ask: <em>"If two lines never meet, are they always parallel?"</em><br>
          <strong>The answer is NO!</strong> Think about a straight tube-light fixed horizontally on the ceiling of your room, and a straight line drawn on the floor running from left to right. Even if extended infinitely, the ceiling line and the floor line will never touch! But are they parallel? No, because they lie in completely different planes. In 3D geometry, lines that never meet and are not parallel are called <strong>skew lines</strong>.
        </p>
        <p>
          Therefore, lines are parallel <strong>only when they lie on the SAME flat plane</strong> and never meet!
        </p>
      </div>

      <h4 class="topic-head"><i class="fa-solid fa-origami"></i> Paper-Folding Discovery &amp; The 2ⁿ + 1 Doubling Law (Activity 2)</h4>
      <p>
        You do not need high-tech computers to discover deep mathematical laws. A simple sheet of newspaper holds profound geometry:
      </p>
      <ol style="margin-left: 2rem; margin-bottom: 1.25rem;">
        <li><strong>Opposite Edges of a Square Sheet:</strong> The top and bottom edges are perfectly <strong>parallel</strong> to each other. The left and right edges are also <strong>parallel</strong>.</li>
        <li><strong>Adjacent Edges:</strong> The top edge and the side edge meet at a corner to form a 90° right angle. They are <strong>perpendicular</strong> to each other.</li>
        <li>
          <strong>Fold 1 (Horizontal Half-Fold):</strong> Fold the sheet in half horizontally and unfold it. You now see a crisp horizontal crease in the middle.
          <ul style="margin-left: 1.5rem;">
            <li>How many horizontal parallel lines exist now? Exactly <strong>3 parallel lines</strong> (Top edge, crease, bottom edge).</li>
            <li>How does the crease relate to the vertical side edges? It is strictly <strong>perpendicular</strong> to them!</li>
          </ul>
        </li>
        <li>
          <strong>Fold 2 (Quarter-Fold):</strong> Fold the sheet horizontally once more and unfold it.
          <ul style="margin-left: 1.5rem;">
            <li>You now have 3 internal crease lines plus the 2 outer edges = <strong>5 parallel lines</strong>!</li>
          </ul>
        </li>
        <li>
          <strong>Fold 3 (Eighth-Fold):</strong> Fold it once more horizontally and unfold it.
          <ul style="margin-left: 1.5rem;">
            <li>You now count 7 internal creases plus the 2 outer edges = <strong>9 parallel lines</strong>!</li>
          </ul>
        </li>
      </ol>

      <div class="callout callout-hack">
        <div class="callout-title"><i class="fa-solid fa-wand-magic-sparkles"></i> The Beautiful Fold Theorem: Formula 2ⁿ + 1</div>
        <p>
          Notice the striking pattern in the number of parallel lines:
        </p>
        <div class="math-display">
          0 Folds: 2⁰ + 1 = 1 + 1 = 2 parallel lines (Top and bottom edges)<br>
          1 Fold : 2¹ + 1 = 2 + 1 = 3 parallel lines<br>
          2 Folds: 2² + 1 = 4 + 1 = 5 parallel lines<br>
          3 Folds: 2³ + 1 = 8 + 1 = 9 parallel lines<br>
          4 Folds: 2⁴ + 1 = 16 + 1 = 17 parallel lines<br>
          <strong>n Folds: 2ⁿ + 1 parallel lines!</strong>
        </div>
        <p>
          <em>Why does this happen?</em> Because each horizontal fold doubles the number of equal rectangular strips between the outer edges. If there are <span class="math-inline">2ⁿ</span> strips, there must be <span class="math-inline">2ⁿ - 1</span> internal dividing creases, plus the <span class="math-inline">2</span> boundary edges, giving:
          <span class="math-inline">(2ⁿ - 1) + 2 = 2ⁿ + 1</span> parallel lines! Pure, elegant mathematical harmony!
        </li>
      </div>

      <h4 class="topic-head"><i class="fa-solid fa-code-fork"></i> Corner Folding Geometry (Fig. 5.8 Analysis)</h4>
      <p>
        In textbook Activity 2 (Page 112), you fold the edges toward the center line and fold the top-right and bottom-left corners onto the creased line to create right-angled triangles.
      </p>
      <ul style="margin-left: 2rem; margin-bottom: 1.25rem;">
        <li>Line segments <span class="math-inline">a</span> and <span class="math-inline">p</span> lie on the outer edges and center line, which are parallel by construction. Hence, <span class="math-inline">a ∥ p</span>.</li>
        <li>Line segments <span class="math-inline">b</span> and <span class="math-inline">q</span> are both perpendicular to the horizontal creases, making them parallel to each other (<span class="math-inline">b ∥ q</span>).</li>
        <li>Line segments <span class="math-inline">c</span> and <span class="math-inline">r</span> are the hypotenuses of identical corner folds formed along the diagonal direction, so <span class="math-inline">c ∥ r</span>.</li>
      </ul>
    </section>
"""
