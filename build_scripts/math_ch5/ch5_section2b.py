# -*- coding: utf-8 -*-
"""Part 4: Section 2 Part B - Conceptual Explanations (5.5 to 5.9), SVGs 4, 5, 6, and Bilingual Glossary."""

SECTION2B_CONTENT = """
      <!-- SUBSECTION 5.5 -->
      <h3 class="subheading"><i class="fa-solid fa-arrows-split-up-and-left"></i> 5.5 Transversals: When One Line Crosses Multiple Lines</h3>
      <p>
        We have seen what happens when two straight lines intersect at a single point, forming 4 angles. Now, what happens when <strong>one single straight line crosses two different lines</strong>?
      </p>

      <div class="callout callout-def">
        <div class="callout-title"><i class="fa-solid fa-bolt"></i> Definition: Transversal (Chedaka / ଛେଦକ / ତିର୍ଯ୍ୟକ ରେଖା)</div>
        <p>
          A line that intersects two or more lines at <strong>distinct points</strong> on the same plane is called a <strong>transversal</strong>.
        </p>
        <p>
          In textbook Fig. 5.14, line <span class="math-inline">t</span> intersects lines <span class="math-inline">l</span> and <span class="math-inline">m</span> at two separate points. Therefore, line <span class="math-inline">t</span> is the transversal.
        </p>
      </div>

      <h4 class="topic-head"><i class="fa-solid fa-list-ol"></i> The 8-Angle System: Anatomy of a Transversal Intersection</h4>
      <p>
        A transversal cutting across two lines creates two distinct intersection vertices, producing a total of <strong>8 angles</strong> (numbered 1 through 8 in standard textbook notation):
      </p>
      <ul style="margin-left: 2rem; margin-bottom: 1.25rem;">
        <li>
          <strong>Interior Angles (Antahstha Kona / ଅନ୍ତଃସ୍ଥ କୋଣ):</strong> Angles that lie in the inside channel <em>between</em> lines <span class="math-inline">l</span> and <span class="math-inline">m</span>:<br>
          <span class="math-inline">∠3, ∠4, ∠5, ∠6</span>
        </li>
        <li>
          <strong>Exterior Angles (Bahihstha Kona / ବହିଃସ୍ଥ କୋଣ):</strong> Angles that lie in the outer regions <em>outside</em> lines <span class="math-inline">l</span> and <span class="math-inline">m</span>:<br>
          <span class="math-inline">∠1, ∠2, ∠7, ∠8</span>
        </li>
      </ul>

      <div class="callout callout-hack">
        <div class="callout-title"><i class="fa-solid fa-brain"></i> The Maximum-4-Angle-Measure Law: A Fascinating Mathematical Truth</div>
        <p>
          <em>Textbook Inquiry (Page 115):</em> "Is it possible for all the eight angles to have different measurements? What about 5, 6, or 7 different angles?"
        </p>
        <p>
          <strong>Mathematical Answer: NEVER!</strong> It is strictly impossible for a transversal to form 5, 6, 7, or 8 different angle measurements!
        </p>
        <p>
          <em>Why?</em> Because around each intersection vertex, <strong>vertically opposite angles are always equal</strong>:
        </p>
        <div class="math-display">
          At top vertex: ∠1 = ∠3  and  ∠2 = ∠4<br>
          At bottom vertex: ∠5 = ∠7  and  ∠6 = ∠8
        </div>
        <p>
          Since every angle is paired with an identical vertically opposite twin, there can be <strong>at most 4 distinct angle measures</strong> in the entire system!
        </p>
        <p>
          Even better: When lines <span class="math-inline">l</span> and <span class="math-inline">m</span> are <strong>parallel</strong>, there are <strong>at most 2 distinct angle measures</strong> (one acute angle, say 60°, and its supplement, 120°). If the transversal is perpendicular, all 8 angles are equal to 90° (only 1 distinct measure)!
        </p>
      </div>

      <!-- SUBSECTION 5.6 -->
      <h3 class="subheading"><i class="fa-solid fa-f"></i> 5.6 Corresponding Angles: The "F-Shape" Geometric Key</h3>
      <p>
        When transversal <span class="math-inline">t</span> cuts across lines <span class="math-inline">l</span> and <span class="math-inline">m</span>, it creates two sets of four angles—one set around the top intersection and one set around the bottom intersection.
      </p>
      <p>
        Angles that occupy the <strong>same relative corner position</strong> at each intersection are called <strong>corresponding angles</strong>.
      </p>

      <div class="callout callout-def">
        <div class="callout-title"><i class="fa-solid fa-arrows-to-dot"></i> The 4 Pairs of Corresponding Angles (Anurupa Kona / ଅନୁରୂପ କୋଣ)</div>
        <p>
          Think of the letter <strong>"F"</strong> (upright, upside-down, or backwards). The angles nestled under the arms of the "F" are corresponding angles:
        </p>
        <ul style="margin-left: 1.5rem; margin-top: 0.5rem;">
          <li><strong>Top-Left Pair:</strong> <span class="math-inline">∠1</span> and <span class="math-inline">∠5</span></li>
          <li><strong>Top-Right Pair:</strong> <span class="math-inline">∠2</span> and <span class="math-inline">∠6</span></li>
          <li><strong>Bottom-Right Pair:</strong> <span class="math-inline">∠3</span> and <span class="math-inline">∠7</span></li>
          <li><strong>Bottom-Left Pair:</strong> <span class="math-inline">∠4</span> and <span class="math-inline">∠8</span></li>
        </ul>
      </div>

      <div class="callout callout-act">
        <div class="callout-title"><i class="fa-solid fa-stamp"></i> The Fundamental Parallel Line Postulate (Activities 3, 4, and 5)</div>
        <p>
          Through hands-on paper tracing (Activity 4) and protractor construction (Activity 3), mathematicians established the grand law connecting transversals to parallel lines:
        </p>
        <div class="math-display">
          <strong>Direct Rule:</strong> If two parallel lines are cut by a transversal, then their corresponding angles are <strong>ALWAYS EQUAL</strong>.<br><br>
          <strong>Converse Rule:</strong> If a transversal cuts two lines such that any one pair of corresponding angles is equal, then the two lines are <strong>GUARANTEED TO BE PARALLEL</strong>.
        </div>
        <p>
          In Activity 5, when lines are not parallel, corresponding angles can <em>never</em> be equal! Equality of corresponding angles is both <strong>necessary and sufficient</strong> for parallelism.
        </p>
      </div>

      <!-- INLINE SVG 4: MASTER TRANSVERSAL ANGLE SYSTEM ON PARALLEL LINES -->
      <div class="diagram-card">
        <svg viewBox="0 0 760 520" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg" style="max-width: 720px; font-family: 'Plus Jakarta Sans', sans-serif;">
          <defs>
            <marker id="arrB" markerWidth="8" markerHeight="8" refX="5" refY="4" orient="auto">
              <path d="M 1 1 L 7 4 L 1 7 Z" fill="#0284c7" />
            </marker>
            <marker id="arrT" markerWidth="8" markerHeight="8" refX="5" refY="4" orient="auto">
              <path d="M 1 1 L 7 4 L 1 7 Z" fill="#7c3aed" />
            </marker>
            <filter id="shadowBox" x="-5%" y="-5%" width="110%" height="110%">
              <feDropShadow dx="0" dy="2" stdDeviation="4" flood-color="#000000" flood-opacity="0.1"/>
            </filter>
          </defs>

          <!-- Card Base -->
          <rect width="760" height="520" rx="16" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.5" filter="url(#shadowBox)"/>

          <!-- Title -->
          <text x="380" y="32" text-anchor="middle" fill="#0f172a" font-size="16" font-weight="700">The Master Transversal System (Parallel Lines l ∥ m)</text>
          <text x="380" y="52" text-anchor="middle" fill="#64748b" font-size="12">F-Shape Corresponding | Z-Shape Alternate Interior | C-Shape Co-Interior</text>

          <!-- Parallel Line l (Top Horizontal) -->
          <line x1="80" y1="160" x2="680" y2="160" stroke="#0284c7" stroke-width="4" marker-start="url(#arrB)" marker-end="url(#arrB)"/>
          <text x="695" y="165" fill="#0284c7" font-weight="800" font-size="16">l</text>
          <!-- Arrow indicating parallel -->
          <path d="M 360 152 L 375 160 L 360 168" fill="none" stroke="#0284c7" stroke-width="3"/>

          <!-- Parallel Line m (Bottom Horizontal) -->
          <line x1="80" y1="360" x2="680" y2="360" stroke="#0284c7" stroke-width="4" marker-start="url(#arrB)" marker-end="url(#arrB)"/>
          <text x="695" y="365" fill="#0284c7" font-weight="800" font-size="16">m</text>
          <!-- Arrow indicating parallel -->
          <path d="M 360 352 L 375 360 L 360 368" fill="none" stroke="#0284c7" stroke-width="3"/>

          <!-- Transversal Line t (Slanted) -->
          <line x1="180" y1="70" x2="520" y2="450" stroke="#7c3aed" stroke-width="4" marker-start="url(#arrT)" marker-end="url(#arrT)"/>
          <text x="535" y="465" fill="#7c3aed" font-weight="800" font-size="16">t</text>

          <!-- Top Intersection Vertex (X = 260, Y = 160) -->
          <circle cx="260" cy="160" r="5" fill="#0f172a"/>
          <text x="245" y="152" fill="#0f172a" font-weight="700" font-size="13">X</text>

          <!-- Angles around X -->
          <!-- ∠1 (Top-Left, Obtuse ~125°) -->
          <circle cx="215" cy="125" r="16" fill="#ede9fe" stroke="#7c3aed" stroke-width="1.5"/>
          <text x="215" y="130" text-anchor="middle" fill="#6d28d9" font-weight="800" font-size="13">1</text>

          <!-- ∠2 (Top-Right, Acute ~55°) -->
          <circle cx="305" cy="125" r="16" fill="#fef3c7" stroke="#d97706" stroke-width="1.5"/>
          <text x="305" y="130" text-anchor="middle" fill="#b45309" font-weight="800" font-size="13">2</text>

          <!-- ∠3 (Bottom-Right, Obtuse ~125°) -->
          <circle cx="310" cy="195" r="16" fill="#ede9fe" stroke="#7c3aed" stroke-width="1.5"/>
          <text x="310" y="200" text-anchor="middle" fill="#6d28d9" font-weight="800" font-size="13">3</text>

          <!-- ∠4 (Bottom-Left, Acute ~55°) -->
          <circle cx="215" cy="195" r="16" fill="#fef3c7" stroke="#d97706" stroke-width="1.5"/>
          <text x="215" y="200" text-anchor="middle" fill="#b45309" font-weight="800" font-size="13">4</text>

          <!-- Bottom Intersection Vertex (Y = 440, Y_coord = 360) -->
          <circle cx="440" cy="360" r="5" fill="#0f172a"/>
          <text x="425" y="352" fill="#0f172a" font-weight="700" font-size="13">Y</text>

          <!-- Angles around Y -->
          <!-- ∠5 (Top-Left, Obtuse ~125°) -->
          <circle cx="395" cy="325" r="16" fill="#ede9fe" stroke="#7c3aed" stroke-width="1.5"/>
          <text x="395" y="330" text-anchor="middle" fill="#6d28d9" font-weight="800" font-size="13">5</text>

          <!-- ∠6 (Top-Right, Acute ~55°) -->
          <circle cx="485" cy="325" r="16" fill="#fef3c7" stroke="#d97706" stroke-width="1.5"/>
          <text x="485" y="330" text-anchor="middle" fill="#b45309" font-weight="800" font-size="13">6</text>

          <!-- ∠7 (Bottom-Right, Obtuse ~125°) -->
          <circle cx="490" cy="395" r="16" fill="#ede9fe" stroke="#7c3aed" stroke-width="1.5"/>
          <text x="490" y="400" text-anchor="middle" fill="#6d28d9" font-weight="800" font-size="13">7</text>

          <!-- ∠8 (Bottom-Left, Acute ~55°) -->
          <circle cx="395" cy="395" r="16" fill="#fef3c7" stroke="#d97706" stroke-width="1.5"/>
          <text x="395" y="400" text-anchor="middle" fill="#b45309" font-weight="800" font-size="13">8</text>

          <!-- Legend Table Box at Bottom -->
          <g transform="translate(40, 440)">
            <rect width="680" height="65" rx="8" fill="#f8fafc" stroke="#e2e8f0" stroke-width="1"/>
            <text x="20" y="24" fill="#6d28d9" font-size="12" font-weight="700">OBTUSE ANGLES (Purple): ∠1 = ∠3 = ∠5 = ∠7 = 125°</text>
            <text x="370" y="24" fill="#b45309" font-size="12" font-weight="700">ACUTE ANGLES (Amber): ∠2 = ∠4 = ∠6 = ∠8 = 55°</text>
            <text x="20" y="48" fill="#0369a1" font-size="12" font-weight="700">KEY THEOREM: Any Purple Angle + Any Amber Angle = 125° + 55° = 180° (Supplementary!)</text>
          </g>
        </svg>
        <div class="diagram-caption">
          <i class="fa-solid fa-circle-info"></i> Figure 2.3: The Master Transversal System. When lines are parallel, all four obtuse angles are equal to each other, all four acute angles are equal to each other, and any obtuse + acute pair sums to 180°.
        </div>
      </div>

      <!-- SUBSECTION 5.7 -->
      <h3 class="subheading"><i class="fa-solid fa-ruler"></i> 5.7 Drawing Parallel Lines: Mechanical &amp; Folding Techniques</h3>
      <p>
        How do draftsmen, architects, and artists draw perfectly parallel lines? You can do it effortlessly using standard tools from your geometry box.
      </p>

      <h4 class="topic-head"><i class="fa-solid fa-sliders"></i> Method 1: The Ruler and Sliding Set-Square Method (Figs. 5.21 &amp; 5.22)</h4>
      <ol style="margin-left: 2rem; margin-bottom: 1.25rem;">
        <li>Place your straight wooden ruler firmly on the paper along line <span class="math-inline">l</span>.</li>
        <li>Place the base of a triangular set square against the edge of the ruler.</li>
        <li>Draw a line along the upright perpendicular edge of the set square.</li>
        <li>Now, hold the ruler firmly stationary with one hand, and <strong>slide the set square</strong> along the edge of the ruler to a new position.</li>
        <li>Draw a second line along the upright edge of the set square.</li>
      </ol>
      <p>
        <em>Why does this guarantee parallel lines?</em> The straight edge of the ruler acts as a <strong>transversal</strong> line. The set square ensures that both drawn lines make the exact same <strong>90° corresponding angle</strong> with the ruler. Since corresponding angles are equal, the two drawn lines are mathematically guaranteed to be strictly parallel!
      </p>

      <!-- INLINE SVG 5: RULER & SLIDING SET-SQUARE METHOD -->
      <div class="diagram-card">
        <svg viewBox="0 0 700 360" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg" style="max-width: 650px; font-family: 'Plus Jakarta Sans', sans-serif;">
          <!-- Canvas -->
          <rect width="700" height="360" rx="16" fill="#f8fafc" stroke="#e2e8f0" stroke-width="2"/>
          <text x="350" y="32" text-anchor="middle" fill="#0f172a" font-size="16" font-weight="700">Drafting Parallel Lines: Sliding Set-Square Technique</text>
          <text x="350" y="52" text-anchor="middle" fill="#64748b" font-size="12">Ruler acts as transversal | Set-square maintains equal 90° corresponding angles</text>

          <!-- Fixed Wooden Ruler along Bottom -->
          <rect x="70" y="240" width="560" height="50" rx="4" fill="#fde68a" stroke="#d97706" stroke-width="2"/>
          <text x="90" y="270" fill="#92400e" font-weight="700" font-size="14">STATIONARY RULER (Baseline Transversal)</text>
          <!-- Ruler tick marks -->
          <g stroke="#b45309" stroke-width="1">
            <line x1="120" y1="240" x2="120" y2="255"/>
            <line x1="160" y1="240" x2="160" y2="250"/>
            <line x1="200" y1="240" x2="200" y2="255"/>
            <line x1="240" y1="240" x2="240" y2="250"/>
            <line x1="280" y1="240" x2="280" y2="255"/>
            <line x1="320" y1="240" x2="320" y2="250"/>
            <line x1="360" y1="240" x2="360" y2="255"/>
            <line x1="400" y1="240" x2="400" y2="250"/>
            <line x1="440" y1="240" x2="440" y2="255"/>
            <line x1="480" y1="240" x2="480" y2="250"/>
            <line x1="520" y1="240" x2="520" y2="255"/>
            <line x1="560" y1="240" x2="560" y2="250"/>
            <line x1="600" y1="240" x2="600" y2="255"/>
          </g>

          <!-- Set Square Position 1 (Drawn in blue) -->
          <polygon points="180,240 180,90 330,240" fill="#e0f2fe" stroke="#0284c7" stroke-width="2.5" fill-opacity="0.8"/>
          <!-- Right angle mark at (180, 240) -->
          <rect x="180" y="220" width="20" height="20" fill="none" stroke="#0369a1" stroke-width="2"/>
          <text x="210" y="215" fill="#0369a1" font-size="11" font-weight="700">90°</text>
          <!-- Drawn Parallel Line 1 -->
          <line x1="180" y1="70" x2="180" y2="240" stroke="#0369a1" stroke-width="3" stroke-dasharray="4,2"/>
          <text x="170" y="80" text-anchor="end" fill="#0369a1" font-weight="800" font-size="13">Line 1</text>

          <!-- Sliding Motion Arrow -->
          <g stroke="#d97706" stroke-width="2.5" fill="none">
            <path d="M 270 170 Q 340 150 410 170" marker-end="url(#arrB)"/>
          </g>
          <text x="340" y="145" text-anchor="middle" fill="#d97706" font-size="12" font-weight="700">SLIDE SET-SQUARE →</text>

          <!-- Set Square Position 2 (Drawn in green/teal) -->
          <polygon points="420,240 420,90 570,240" fill="#ccfbf1" stroke="#0d9488" stroke-width="2.5" fill-opacity="0.8"/>
          <!-- Right angle mark at (420, 240) -->
          <rect x="420" y="220" width="20" height="20" fill="none" stroke="#0f766e" stroke-width="2"/>
          <text x="450" y="215" fill="#0f766e" font-size="11" font-weight="700">90°</text>
          <!-- Drawn Parallel Line 2 -->
          <line x1="420" y1="70" x2="420" y2="240" stroke="#0f766e" stroke-width="3" stroke-dasharray="4,2"/>
          <text x="430" y="80" fill="#0f766e" font-weight="800" font-size="13">Line 2 (∥ Line 1)</text>

          <!-- Equidistant Dimension Line -->
          <line x1="180" y1="110" x2="420" y2="110" stroke="#7c3aed" stroke-width="1.5" stroke-dasharray="3,3"/>
          <text x="300" y="105" text-anchor="middle" fill="#7c3aed" font-size="11" font-weight="700">Constant Distance d</text>
        </svg>
        <div class="diagram-caption">
          <i class="fa-solid fa-circle-info"></i> Figure 2.4: Mechanical drafting of parallel lines. By sliding the set-square along a stationary straightedge ruler, the angle with the ruler remains locked at 90°, producing perfectly parallel lines.
        </div>
      </div>

      <h4 class="topic-head"><i class="fa-solid fa-file-contract"></i> Method 2: Paper-Folding a Parallel Line Through an External Point A (Fig. 5.24)</h4>
      <p>
        Suppose you are given a line <span class="math-inline">l</span> on a sheet of paper, and an external point <span class="math-inline">A</span> floating outside the line. How can you fold a line parallel to <span class="math-inline">l</span> passing through <span class="math-inline">A</span>?
      </p>
      <ol style="margin-left: 2rem; margin-bottom: 1.25rem;">
        <li><strong>Step 1:</strong> Fold the paper to create a crease passing through point <span class="math-inline">A</span> that is strictly perpendicular to line <span class="math-inline">l</span>. Let this crease be transversal <span class="math-inline">t</span> (<span class="math-inline">t ⊥ l</span>).</li>
        <li><strong>Step 2:</strong> Now, fold the paper a second time to create a new crease <span class="math-inline">m</span> passing through point <span class="math-inline">A</span> that is strictly perpendicular to crease <span class="math-inline">t</span> (<span class="math-inline">m ⊥ t</span>).</li>
        <li><strong>Conclusion:</strong> Lines <span class="math-inline">l</span> and <span class="math-inline">m</span> are strictly <strong>parallel to each other</strong> (<span class="math-inline">l ∥ m</span>)!</li>
      </ol>

      <div class="callout callout-def">
        <div class="callout-title"><i class="fa-solid fa-lightbulb"></i> The Perpendicular-to-a-Perpendicular Theorem</div>
        <p>
          <em>Why are lines l and m parallel?</em><br>
          Both line <span class="math-inline">l</span> and line <span class="math-inline">m</span> make an angle of <span class="math-inline">90°</span> with the same transversal crease <span class="math-inline">t</span>. Since these corresponding angles are equal (<span class="math-inline">90° = 90°</span>), line <span class="math-inline">l</span> and line <span class="math-inline">m</span> must be strictly parallel!
        </p>
        <div class="math-display" style="text-align: center;">
          <strong>Two lines perpendicular to the same transversal are always parallel to each other.</strong>
        </div>
      </div>

      <!-- SUBSECTION 5.8 -->
      <h3 class="subheading"><i class="fa-solid fa-z"></i> 5.8 Alternate Angles &amp; Consecutive Interior Angles</h3>

      <h4 class="topic-head"><i class="fa-solid fa-puzzle-piece"></i> Alternate Interior Angles: The "Z-Shape" Rule</h4>
      <p>
        Look at the inside region between lines <span class="math-inline">l</span> and <span class="math-inline">m</span>. Angles that lie on <strong>opposite (alternate) sides of the transversal</strong>, and not forming a linear pair, are called <strong>alternate interior angles</strong>.
      </p>
      <p>
        Think of the letter <strong>"Z"</strong> (or reversed "Z"). The two acute corners tucked inside the folds of the "Z" are alternate interior angles. In Figure 2.3:
      </p>
      <ul style="margin-left: 2rem; margin-bottom: 1.25rem;">
        <li><span class="math-inline">∠3</span> and <span class="math-inline">∠5</span> form one alternate interior pair.</li>
        <li><span class="math-inline">∠4</span> and <span class="math-inline">∠6</span> form the other alternate interior pair.</li>
      </ul>

      <div class="callout callout-hack">
        <div class="callout-title"><i class="fa-solid fa-graduation-cap"></i> Deductive Proof: Why Alternate Interior Angles are Equal (Activity 6)</div>
        <p>
          Let us prove why alternate interior angles must be equal when lines are parallel, without measuring:
        </p>
        <div class="math-display">
          Suppose parallel lines l and m are intersected by transversal t.<br>
          Consider alternate interior angles ∠4 and ∠6.<br><br>
          1. ∠2 = ∠6 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Corresponding Angles Postulate for l ∥ m]<br>
          2. ∠2 = ∠4 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Vertically Opposite Angles at top intersection]<br><br>
          Since both ∠6 and ∠4 are equal to ∠2, by Euclid's first axiom:<br>
          <strong>∠4 = ∠6</strong> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Q.E.D. PROVED!]<br><br>
          In the exact same way:<br>
          1. ∠1 = ∠5 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Corresponding Angles]<br>
          2. ∠1 = ∠3 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Vertically Opposite Angles]<br>
          ⇒ <strong>∠3 = ∠5</strong> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[PROVED!]
        </div>
      </div>

      <h4 class="topic-head"><i class="fa-solid fa-u"></i> Consecutive Interior Angles (Co-interior / Allied): The "C-Shape" Rule</h4>
      <p>
        Interior angles that lie on the <strong>very same side</strong> of the transversal are called <strong>consecutive interior angles</strong> (also known as <em>co-interior</em> or <em>allied angles</em>). They resemble the inside of the letter <strong>"C"</strong> or <strong>"U"</strong>.
      </p>
      <ul style="margin-left: 2rem; margin-bottom: 1.25rem;">
        <li>Right-side pair: <span class="math-inline">∠2</span> is corresponding, and <span class="math-inline">∠3</span> and <span class="math-inline">∠6</span> are on the same side.</li>
        <li>Left-side pair: <span class="math-inline">∠4</span> and <span class="math-inline">∠5</span> are on the same side.</li>
      </ul>

      <div class="callout callout-def">
        <div class="callout-title"><i class="fa-solid fa-shield-halved"></i> The Co-Interior Supplementary Law &amp; Proof (Example 3)</div>
        <p>
          <strong>Theorem:</strong> When two parallel lines are cut by a transversal, the interior angles on the same side of the transversal are <strong>supplementary (their sum is 180°)</strong>.
        </p>
        <div class="math-display">
          Proof:<br>
          1. ∠2 + ∠3 = 180° &nbsp;&nbsp;[Linear pair on straight line l]<br>
          2. But ∠2 = ∠6 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Corresponding angles for l ∥ m]<br><br>
          Substitute ∠6 in place of ∠2 in equation (1):<br>
          <strong>∠6 + ∠3 = 180°</strong> &nbsp;&nbsp;[PROVED!]<br><br>
          Similarly:<br>
          ∠1 + ∠4 = 180° &nbsp;and&nbsp; ∠1 = ∠5<br>
          ⇒ <strong>∠5 + ∠4 = 180°</strong> &nbsp;&nbsp;[PROVED!]
        </div>
      </div>

      <!-- SUBSECTION 5.9 -->
      <h3 class="subheading"><i class="fa-solid fa-eye-slash"></i> 5.9 Optical Illusions in Geometry: Why Parallel Lines Look Bent</h3>
      <p>
        Look closely at the patterns in Section 5.9 of your textbook. Your eyes will swear that the straight horizontal lines are bowed, bent, or tilted. Yet, if you place a wooden ruler across them, you discover that every single line is <strong>perfectly straight and parallel</strong>!
      </p>

      <!-- INLINE SVG 6: OPTICAL ILLUSIONS (HERING & ZOLLNER) -->
      <div class="diagram-card">
        <svg viewBox="0 0 760 380" width="100%" height="auto" xmlns="http://www.w3.org/2000/svg" style="max-width: 720px; font-family: 'Plus Jakarta Sans', sans-serif;">
          <!-- Canvas -->
          <rect width="760" height="380" rx="16" fill="#0f172a" stroke="#334155" stroke-width="2"/>
          <text x="380" y="32" text-anchor="middle" fill="#f8fafc" font-size="16" font-weight="700">Parallel Illusions: How Intersecting Lines Deceive the Human Eye</text>
          <text x="380" y="52" text-anchor="middle" fill="#94a3b8" font-size="12">Hering Illusion (Left) | Zöllner Illusion (Right) — Both pairs of red lines are strictly parallel!</text>

          <!-- HERING ILLUSION (LEFT SIDE) -->
          <g transform="translate(190, 200)">
            <!-- Radiating Background Rays from Center (0,0) -->
            <g stroke="#334155" stroke-width="1.5">
              <line x1="0" y1="0" x2="-160" y2="-120"/>
              <line x1="0" y1="0" x2="-120" y2="-130"/>
              <line x1="0" y1="0" x2="-80" y2="-135"/>
              <line x1="0" y1="0" x2="-40" y2="-138"/>
              <line x1="0" y1="0" x2="0" y2="-140"/>
              <line x1="0" y1="0" x2="40" y2="-138"/>
              <line x1="0" y1="0" x2="80" y2="-135"/>
              <line x1="0" y1="0" x2="120" y2="-130"/>
              <line x1="0" y1="0" x2="160" y2="-120"/>
              <line x1="0" y1="0" x2="-160" y2="120"/>
              <line x1="0" y1="0" x2="-120" y2="130"/>
              <line x1="0" y1="0" x2="-80" y2="135"/>
              <line x1="0" y1="0" x2="-40" y2="138"/>
              <line x1="0" y1="0" x2="0" y2="140"/>
              <line x1="0" y1="0" x2="40" y2="138"/>
              <line x1="0" y1="0" x2="80" y2="135"/>
              <line x1="0" y1="0" x2="120" y2="130"/>
              <line x1="0" y1="0" x2="160" y2="120"/>
              <line x1="0" y1="0" x2="-170" y2="-50"/>
              <line x1="0" y1="0" x2="-170" y2="50"/>
              <line x1="0" y1="0" x2="170" y2="-50"/>
              <line x1="0" y1="0" x2="170" y2="50"/>
            </g>

            <!-- Two Parallel Vertical Red Lines (x = -45 and x = +45) -->
            <line x1="-45" y1="-130" x2="-45" y2="130" stroke="#ef4444" stroke-width="3.5"/>
            <line x1="45" y1="-130" x2="45" y2="130" stroke="#ef4444" stroke-width="3.5"/>

            <text x="0" y="155" text-anchor="middle" fill="#38bdf8" font-size="13" font-weight="700">Hering Illusion</text>
            <text x="0" y="170" text-anchor="middle" fill="#94a3b8" font-size="11">Red lines appear to bow outward</text>
          </g>

          <!-- DIVIDING BORDER -->
          <line x1="380" y1="70" x2="380" y2="350" stroke="#334155" stroke-width="1.5" stroke-dasharray="4,4"/>

          <!-- ZOLLNER ILLUSION (RIGHT SIDE) -->
          <g transform="translate(570, 200)">
            <!-- Parallel Line 1 (Left) -->
            <line x1="-60" y1="-120" x2="-60" y2="120" stroke="#ef4444" stroke-width="3.5"/>
            <!-- Hatch marks sloping UP-RIGHT -->
            <g stroke="#38bdf8" stroke-width="2">
              <line x1="-80" y1="-105" x2="-40" y2="-95"/>
              <line x1="-80" y1="-75" x2="-40" y2="-65"/>
              <line x1="-80" y1="-45" x2="-40" y2="-35"/>
              <line x1="-80" y1="-15" x2="-40" y2="-5"/>
              <line x1="-80" y1="15" x2="-40" y2="25"/>
              <line x1="-80" y1="45" x2="-40" y2="55"/>
              <line x1="-80" y1="75" x2="-40" y2="85"/>
              <line x1="-80" y1="105" x2="-40" y2="115"/>
            </g>

            <!-- Parallel Line 2 (Right) -->
            <line x1="60" y1="-120" x2="60" y2="120" stroke="#ef4444" stroke-width="3.5"/>
            <!-- Hatch marks sloping DOWN-RIGHT -->
            <g stroke="#38bdf8" stroke-width="2">
              <line x1="40" y1="-95" x2="80" y2="-105"/>
              <line x1="40" y1="-65" x2="80" y2="-75"/>
              <line x1="40" y1="-35" x2="80" y2="-45"/>
              <line x1="40" y1="-5" x2="80" y2="-15"/>
              <line x1="40" y1="25" x2="80" y2="15"/>
              <line x1="40" y1="55" x2="80" y2="45"/>
              <line x1="40" y1="85" x2="80" y2="75"/>
              <line x1="40" y1="115" x2="80" y2="105"/>
            </g>

            <text x="0" y="155" text-anchor="middle" fill="#38bdf8" font-size="13" font-weight="700">Zöllner Illusion</text>
            <text x="0" y="170" text-anchor="middle" fill="#94a3b8" font-size="11">Red lines appear to tilt away</text>
          </g>
        </svg>
        <div class="diagram-caption">
          <i class="fa-solid fa-circle-info"></i> Figure 2.5: Famous geometric optical illusions. In both panels, the red vertical lines are perfectly straight, vertical, and parallel. The brain's visual cortex miscalculates orientation due to the short intersecting angles.
        </div>
      </div>

      <div class="callout callout-warn">
        <div class="callout-title"><i class="fa-solid fa-brain"></i> What Causes These Illusions? (The Neuro-Geometric Explanation)</div>
        <p>
          Why do our eyes trick us? Neuroscientists and mathematicians have discovered that the <strong>human visual cortex overestimates acute angles (&lt; 90°)</strong> and <strong>underestimates obtuse angles (&gt; 90°)</strong>.
        </p>
        <p>
          When straight parallel lines are crossed by short angled lines (like the hatches in Zöllner's illusion or the spokes in Hering's illusion), our brain subconsciously pushes the parallel line away from the acute angle corners to "widen" them. This angular distortion bends our perceptual field, creating the powerful illusion of bowing or tilting!
        </p>
      </div>

      <!-- EXHAUSTIVE BILINGUAL VOCABULARY / GLOSSARY TABLE (30 TERMS) -->
      <h3 class="subheading"><i class="fa-solid fa-language"></i> Exhaustive Bilingual Mathematical Glossary (30 Key Terms)</h3>
      <p>
        Mastering mathematics requires fluency in both concepts and precise vocabulary. The comprehensive table below provides English terms, parts of speech, formal definitions, and accurate textbook Odia (ଓଡ଼ିଆ ଭାଷା) terms aligned with BSE Odisha and CBSE NEP curricula.
      </p>

      <div class="table-responsive">
        <table>
          <thead>
            <tr>
              <th style="width: 5%;">#</th>
              <th style="width: 22%;">Term / Concept</th>
              <th style="width: 13%;">Part of Speech</th>
              <th style="width: 35%;">English Meaning / Description</th>
              <th style="width: 25%;">ଓଡ଼ିଆ ଅର୍ଥ (Odia Meaning &amp; Script)</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>1</td>
              <td><strong>Intersecting Lines</strong></td>
              <td>Noun Phrase</td>
              <td>Two or more straight lines that meet or cross at exactly one shared point on a plane.</td>
              <td class="odia-script">ପରସ୍ପରଛେଦୀ ସରଳରେଖା (Parasparachedi Saralarekha)</td>
            </tr>
            <tr>
              <td>2</td>
              <td><strong>Point of Intersection</strong></td>
              <td>Noun Phrase</td>
              <td>The unique coordinate point where two intersecting straight lines cross.</td>
              <td class="odia-script">ଛେଦବିନ୍ଦୁ (Chedabindu)</td>
            </tr>
            <tr>
              <td>3</td>
              <td><strong>Linear Pair of Angles</strong></td>
              <td>Noun Phrase</td>
              <td>A pair of adjacent angles formed by intersecting lines whose non-common arms form a straight line (sum = 180°).</td>
              <td class="odia-script">ରୈଖିକ ଯୁଗ୍ମ କୋଣ (Raikhika Yugma Kona)</td>
            </tr>
            <tr>
              <td>4</td>
              <td><strong>Vertically Opposite Angles</strong></td>
              <td>Noun Phrase</td>
              <td>The pair of opposite, non-adjacent angles formed by two intersecting lines; always equal in measure.</td>
              <td class="odia-script">ପ୍ରତୀପ କୋଣ (Pratipa Kona)</td>
            </tr>
            <tr>
              <td>5</td>
              <td><strong>Straight Angle</strong></td>
              <td>Noun Phrase</td>
              <td>An angle measuring exactly 180°, formed by two collinear opposite rays.</td>
              <td class="odia-script">ସରଳକୋଣ (Saralakona - 180°)</td>
            </tr>
            <tr>
              <td>6</td>
              <td><strong>Perpendicular Lines</strong></td>
              <td>Noun Phrase</td>
              <td>Two lines that intersect each other at an exact right angle of 90° (symbol: ⊥).</td>
              <td class="odia-script">ପରସ୍ପର ଲମ୍ବ ସରଳରେଖା (Paraspara Lamba Saralarekha)</td>
            </tr>
            <tr>
              <td>7</td>
              <td><strong>Right Angle</strong></td>
              <td>Noun</td>
              <td>An angle that measures exactly 90 degrees (symbol: ⊾).</td>
              <td class="odia-script">ସମକୋଣ (Samakona - 90°)</td>
            </tr>
            <tr>
              <td>8</td>
              <td><strong>Plane Surface</strong></td>
              <td>Noun Phrase</td>
              <td>A perfectly flat, 2D surface extending indefinitely in all directions with zero thickness.</td>
              <td class="odia-script">ସମତଳ (Samatala)</td>
            </tr>
            <tr>
              <td>9</td>
              <td><strong>Coplanar Lines</strong></td>
              <td>Noun Phrase</td>
              <td>Straight lines that lie entirely within the very same two-dimensional flat plane.</td>
              <td class="odia-script">ଏକସମତଳୀୟ ସରଳରେଖା (Ekasamataliya Saralarekha)</td>
            </tr>
            <tr>
              <td>10</td>
              <td><strong>Parallel Lines</strong></td>
              <td>Noun Phrase</td>
              <td>Coplanar straight lines that remain at constant distance apart and never meet however far extended (symbol: ∥).</td>
              <td class="odia-script">ସମାନ୍ତରାଳ ସରଳରେଖା (Samantarala Saralarekha)</td>
            </tr>
            <tr>
              <td>11</td>
              <td><strong>Equidistant</strong></td>
              <td>Adjective</td>
              <td>Maintaining the exact same perpendicular distance apart at every point along the line.</td>
              <td class="odia-script">ସମଦୂରବର୍ତ୍ତୀ (Samaduravartti)</td>
            </tr>
            <tr>
              <td>12</td>
              <td><strong>Transversal</strong></td>
              <td>Noun</td>
              <td>A straight line that cuts or crosses two or more lines at distinct points.</td>
              <td class="odia-script">ଛେଦକ / ତିର୍ଯ୍ୟକ ରେଖା (Chedaka / Tiryyaka Rekha)</td>
            </tr>
            <tr>
              <td>13</td>
              <td><strong>Interior Angles</strong></td>
              <td>Noun Phrase</td>
              <td>The four angles located in the inner region between the two intersected lines along a transversal.</td>
              <td class="odia-script">ଅନ୍ତଃସ୍ଥ କୋଣ (Antahstha Kona)</td>
            </tr>
            <tr>
              <td>14</td>
              <td><strong>Exterior Angles</strong></td>
              <td>Noun Phrase</td>
              <td>The four angles lying on the outer region beyond the two intersected lines along a transversal.</td>
              <td class="odia-script">ବହିଃସ୍ଥ କୋଣ (Bahihstha Kona)</td>
            </tr>
            <tr>
              <td>15</td>
              <td><strong>Corresponding Angles</strong></td>
              <td>Noun Phrase</td>
              <td>Angles occupying matching relative positions at each intersection along a transversal (F-shape).</td>
              <td class="odia-script">ଅନୁରୂପ କୋଣ (Anurupa Kona)</td>
            </tr>
            <tr>
              <td>16</td>
              <td><strong>Alternate Interior Angles</strong></td>
              <td>Noun Phrase</td>
              <td>Interior angles on opposite sides of the transversal, not forming a linear pair (Z-shape).</td>
              <td class="odia-script">ଏକାନ୍ତର ଅନ୍ତଃସ୍ଥ କୋଣ (Ekantara Antahstha Kona)</td>
            </tr>
            <tr>
              <td>17</td>
              <td><strong>Alternate Exterior Angles</strong></td>
              <td>Noun Phrase</td>
              <td>Exterior angles lying on opposite sides of the transversal outside the intersected lines.</td>
              <td class="odia-script">ଏକାନ୍ତର ବହିଃସ୍ଥ କୋଣ (Ekantara Bahihstha Kona)</td>
            </tr>
            <tr>
              <td>18</td>
              <td><strong>Consecutive Interior Angles</strong></td>
              <td>Noun Phrase</td>
              <td>Interior angles on the same side of the transversal (C-shape); supplementary when lines are parallel.</td>
              <td class="odia-script">ଏକପାର୍ଶ୍ୱସ୍ଥ ଅନ୍ତଃସ୍ଥ କୋଣ (Ekaparshwastha Antahstha Kona)</td>
            </tr>
            <tr>
              <td>19</td>
              <td><strong>Supplementary Angles</strong></td>
              <td>Noun Phrase</td>
              <td>Any two angles whose measures add up to exactly 180 degrees.</td>
              <td class="odia-script">ପରିପୂରକ କୋଣ (Paripuraka Kona)</td>
            </tr>
            <tr>
              <td>20</td>
              <td><strong>Complementary Angles</strong></td>
              <td>Noun Phrase</td>
              <td>Any two angles whose measures add up to exactly 90 degrees.</td>
              <td class="odia-script">ଅନୁପୂରକ କୋଣ (Anupuraka Kona)</td>
            </tr>
            <tr>
              <td>21</td>
              <td><strong>Mathematical Proof</strong></td>
              <td>Noun Phrase</td>
              <td>A logical deduction from established definitions and axioms without relying on measurement.</td>
              <td class="odia-script">ଗାଣିତିକ ପ୍ରମାଣ (Ganitika Pramana)</td>
            </tr>
            <tr>
              <td>22</td>
              <td><strong>Set Square</strong></td>
              <td>Noun Phrase</td>
              <td>A triangular drafting instrument having angles of 90°-45°-45° or 90°-60°-30° used to draw parallel and perpendicular lines.</td>
              <td class="odia-script">ସେଟ୍ ସ୍କୋୟାର (Set Square)</td>
            </tr>
            <tr>
              <td>23</td>
              <td><strong>Protractor</strong></td>
              <td>Noun</td>
              <td>A semi-circular graduated instrument used for measuring and constructing geometric angles.</td>
              <td class="odia-script">କୋଣମାପକ (Konamapaka)</td>
            </tr>
            <tr>
              <td>24</td>
              <td><strong>Line Segment</strong></td>
              <td>Noun Phrase</td>
              <td>A part of a straight line bounded by two distinct endpoints.</td>
              <td class="odia-script">ରେଖାଖଣ୍ଡ (Rekhakhanda)</td>
            </tr>
            <tr>
              <td>25</td>
              <td><strong>Ray</strong></td>
              <td>Noun</td>
              <td>A straight line segment having one fixed starting point and extending infinitely in one direction.</td>
              <td class="odia-script">ରଶ୍ମି (Rashmi)</td>
            </tr>
            <tr>
              <td>26</td>
              <td><strong>Collinear Points</strong></td>
              <td>Noun Phrase</td>
              <td>Three or more points that lie entirely along the same straight line.</td>
              <td class="odia-script">ଏକରେଖୀୟ ବିନ୍ଦୁ (Ekarekhiya Bindu)</td>
            </tr>
            <tr>
              <td>27</td>
              <td><strong>Non-coplanar (Skew) Lines</strong></td>
              <td>Noun Phrase</td>
              <td>Lines in 3-dimensional space that do not lie in the same plane and never intersect.</td>
              <td class="odia-script">ଅସମତଳୀୟ / ତିର୍ଯ୍ୟକ୍ ଅସମାନ୍ତରାଳ ରେଖା (Asamataliya Rekha)</td>
            </tr>
            <tr>
              <td>28</td>
              <td><strong>Optical Illusion</strong></td>
              <td>Noun Phrase</td>
              <td>A visual perception where the brain interprets parallel lines as bent or tilted due to background patterns.</td>
              <td class="odia-script">ଦୃଷ୍ଟିଭ୍ରମ (Drushtibhrama)</td>
            </tr>
            <tr>
              <td>29</td>
              <td><strong>Converse of a Theorem</strong></td>
              <td>Noun Phrase</td>
              <td>A geometric statement formed by reversing the given hypothesis and the conclusion.</td>
              <td class="odia-script">ପ୍ରମେୟର ବିପରୀତ ପ୍ରମାଣ (Prameyara Biparita Pramana)</td>
            </tr>
            <tr>
              <td>30</td>
              <td><strong>Degree (°)</strong></td>
              <td>Noun</td>
              <td>A standard unit of angular measurement equal to 1/360th of a full circular turn.</td>
              <td class="odia-script">ଡିଗ୍ରୀ (Degree - °)</td>
            </tr>
          </tbody>
        </table>
      </div>
    </section>
"""
