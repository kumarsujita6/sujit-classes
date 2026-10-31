# -*- coding: utf-8 -*-
"""
Module: ch4_section2.py
Contains Section 2: Complete Line-by-Line Conceptual Explanations & Exhaustive Bilingual Glossary.
Features:
- Etymology & Anatomy of Quadrilaterals (Convex vs Concave)
- Section 4.1: Rectangles & Squares (The Carpenter's Problem, Deductions 1-5)
- Section 4.2: Angles in a Quadrilateral (Angle Sum Proofs, Concave proof)
- Section 4.3: Parallelograms (Deductions 6-8, 4 Properties)
- Section 4.4: Rhombuses (Deductions 9-10, 6 Properties)
- Section 4.5: Playing with Quadrilaterals (Geoboard, Triangle Joining)
- Section 4.6: Kites and Trapeziums (Isosceles Trapezium RHS proof, Venn Diagrams)
- SVG Diagrams 2, 3, 4, 5, 6
- 32-term Bilingual Vocabulary Table with accurate Odia script
"""

def get_section_2():
    return """
    <!-- SECTION 2: CONCEPTS & BILINGUAL GLOSSARY -->
    <section id="section-2">
      <div class="section-header">
        <div class="section-tag"><i class="fa-solid fa-book-open"></i> Deep Mathematical Exposition</div>
        <h2 class="section-title">Section 2: Complete Line-by-Line Conceptual Explanations & Exhaustive Bilingual Glossary</h2>
        <p class="section-desc">
          A rigorous, teacher-guided walkthrough of every theorem, deduction, and geometric construction in NCERT Ganita Prakash Grade 8 Chapter 4 (NEP Code: hegp104), accompanied by an exhaustive bilingual Odia-English glossary.
        </p>
      </div>

      <!-- 2.1 ETYMOLOGY & ANATOMY -->
      <h3 class="subheading"><i class="fa-solid fa-shapes"></i> 2.1 Etymology, Elements & The Convex-Concave Distinction</h3>
      <p>
        In our study of plane geometry, we transition from three-sided polygons (triangles) to four-sided polygons. The word <strong>Quadrilateral</strong> comes from the Latin words <em>quadri</em> (four) and <em>latus</em> (sides). When four non-collinear points in a plane are connected in sequential order by straight line segments that intersect only at their endpoints, the resulting closed polygon is a quadrilateral.
      </p>

      <div class="table-container">
        <table class="data-table">
          <thead>
            <tr>
              <th>Geometric Element</th>
              <th>Count</th>
              <th>Symbolic Notation</th>
              <th>Geometric Role &amp; Meaning</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>Vertices</strong></td>
              <td>4</td>
              <td>A, B, C, D</td>
              <td>The corner endpoints where two adjacent sides meet. Non-collinear points.</td>
            </tr>
            <tr>
              <td><strong>Sides</strong></td>
              <td>4</td>
              <td>AB, BC, CD, DA</td>
              <td>The straight boundary line segments enclosing the interior region.</td>
            </tr>
            <tr>
              <td><strong>Interior Angles</strong></td>
              <td>4</td>
              <td>∠A, ∠B, ∠C, ∠D</td>
              <td>Angles formed inside the polygon between adjacent sides. Sum equals 360°.</td>
            </tr>
            <tr>
              <td><strong>Diagonals</strong></td>
              <td>2</td>
              <td>AC, BD</td>
              <td>Line segments joining non-consecutive (opposite) vertices. They provide structural bracing.</td>
            </tr>
            <tr>
              <td><strong>Pairs of Opposite Sides</strong></td>
              <td>2</td>
              <td>(AB, CD) and (BC, DA)</td>
              <td>Sides that do not share any common vertex.</td>
            </tr>
            <tr>
              <td><strong>Pairs of Adjacent Sides</strong></td>
              <td>4</td>
              <td>(AB, BC), (BC, CD), (CD, DA), (DA, AB)</td>
              <td>Sides that share a common vertex.</td>
            </tr>
          </tbody>
        </table>
      </div>

      <div class="callout callout-def">
        <div class="callout-title"><i class="fa-solid fa-circle-exclamation"></i> Convex vs. Concave Quadrilaterals</div>
        <p>
          Quadrilaterals are classified into two broad topological categories depending on the location of their diagonals and the measure of their interior angles:
        </p>
        <ul>
          <li><strong>Convex Quadrilateral:</strong> All four interior angles are strictly less than 180° (i.e., acute, right, or obtuse). Both diagonals (AC and BD) lie completely <em>inside</em> the figure. Any line segment joining two points inside the quadrilateral lies entirely inside the figure. All standard quadrilaterals studied in school (squares, rectangles, parallelograms, rhombuses, trapeziums, convex kites) are convex.</li>
          <li><strong>Concave Quadrilateral (Re-entrant):</strong> Exactly one interior angle is a <strong>reflex angle</strong> (greater than 180° but less than 360°). One of its diagonals lies entirely <em>outside</em> the interior region of the figure! A classic example is the arrowhead or dart shape. Even though one angle is reflex, the sum of all four interior angles is still strictly 360°!</li>
        </ul>
      </div>

      <!-- 2.2 RECTANGLES AND SQUARES -->
      <h3 class="subheading"><i class="fa-solid fa-ruler-combined"></i> 2.2 Section 4.1: Rectangles and Squares (The Carpenter's Problem &amp; Deductions 1 to 5)</h3>
      <p>
        The NCERT Ganita Prakash curriculum introduces quadrilaterals through a very practical hands-on problem faced by craftspeople: <strong>The Carpenter's Problem</strong>.
      </p>

      <div class="callout callout-act">
        <div class="callout-title"><i class="fa-solid fa-hammer"></i> The Carpenter's Problem (Textbook Page 83)</div>
        <p>
          A carpenter needs to put together two thin strips of wood so that when a thread is stretched taut around their endpoints, it forms a perfect <strong>rectangle</strong>. She already has one 8 cm long strip.
        </p>
        <p><strong>The Core Questions:</strong></p>
        <ol>
          <li>What must be the length of the second wooden strip?</li>
          <li>Where along their lengths should the two strips be joined (pinned/hinged)?</li>
          <li>Does the angle at which the two strips cross matter?</li>
        </ol>
      </div>

      <p>
        To answer these questions, let us analyze the geometric model. The two wooden strips represent the <strong>diagonals</strong> of the quadrilateral ABCD, say diagonals AC and BD, intersecting at point O.
      </p>

      <!-- SVG DIAGRAM 2: THE CARPENTER'S PROBLEM & RECTANGLE DIAGONAL DEDUCTIONS -->
      <div class="diagram-card">
        <div class="svg-container">
          <svg viewBox="0 0 920 440" xmlns="http://www.w3.org/2000/svg" style="background:#f8fafc; border-radius:12px; font-family:'Space Grotesk', sans-serif;">
            <defs>
              <marker id="arrow2" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
                <path d="M 0 1 L 10 5 L 0 9 z" fill="#2563eb"/>
              </marker>
            </defs>

            <text x="460" y="32" text-anchor="middle" font-size="20" font-weight="800" fill="#0f172a">THE CARPENTER'S PROBLEM &amp; DIAGONAL DEDUCTIONS</text>
            <text x="460" y="54" text-anchor="middle" font-size="12.5" fill="#64748b">Ganita Prakash Section 4.1: Proving Diagonals are Equal &amp; Bisect Each Other</text>

            <!-- LEFT PANEL: PHYSICAL STRIPS -->
            <rect x="30" y="75" width="390" height="340" rx="14" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.5"/>
            <text x="225" y="105" text-anchor="middle" font-size="15" font-weight="700" fill="#1e293b">1. Physical Carpentry Model</text>
            <text x="225" y="125" text-anchor="middle" font-size="12" fill="#64748b">Two equal strips (8 cm) hinged at midpoint O</text>

            <!-- Strips crossing -->
            <line x1="80" y1="340" x2="370" y2="160" stroke="#f59e0b" stroke-width="10" stroke-linecap="round"/>
            <line x1="80" y1="160" x2="370" y2="340" stroke="#d97706" stroke-width="10" stroke-linecap="round"/>
            <!-- Taut thread forming rectangle -->
            <polygon points="80,160 370,160 370,340 80,340" fill="rgba(37,99,235,0.06)" stroke="#2563eb" stroke-width="2.5" stroke-dasharray="6,4"/>
            <!-- Hinge pin O -->
            <circle cx="225" cy="250" r="7" fill="#dc2626" stroke="#ffffff" stroke-width="2"/>
            <text x="225" y="240" text-anchor="middle" font-size="14" font-weight="800" fill="#dc2626">O (Hinge)</text>

            <!-- Vertices -->
            <circle cx="80" cy="160" r="5" fill="#1d4ed8"/>
            <text x="65" y="155" font-size="15" font-weight="700" fill="#1d4ed8">A</text>
            <circle cx="370" cy="160" r="5" fill="#1d4ed8"/>
            <text x="385" y="155" font-size="15" font-weight="700" fill="#1d4ed8">B</text>
            <circle cx="370" cy="340" r="5" fill="#1d4ed8"/>
            <text x="385" y="355" font-size="15" font-weight="700" fill="#1d4ed8">C</text>
            <circle cx="80" cy="340" r="5" fill="#1d4ed8"/>
            <text x="65" y="355" font-size="15" font-weight="700" fill="#1d4ed8">D</text>

            <text x="225" y="380" text-anchor="middle" font-size="12" font-weight="600" fill="#047857">OA = OC = 4 cm | OB = OD = 4 cm</text>
            <text x="225" y="400" text-anchor="middle" font-size="11.5" fill="#475569">Thread ABCD forms a Rectangle for ANY angle between strips!</text>

            <!-- RIGHT PANEL: MATHEMATICAL DEDUCTION -->
            <rect x="450" y="75" width="440" height="340" rx="14" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.5"/>
            <text x="670" y="105" text-anchor="middle" font-size="15" font-weight="700" fill="#1e293b">2. Geometric Proof of Congruence</text>

            <!-- Geometric Diagram -->
            <rect x="510" y="140" width="280" height="160" fill="none" stroke="#0f172a" stroke-width="2"/>
            <!-- Diagonals -->
            <line x1="510" y1="300" x2="790" y2="140" stroke="#2563eb" stroke-width="1.8"/>
            <line x1="510" y1="140" x2="790" y2="300" stroke="#7c3aed" stroke-width="1.8"/>
            <circle cx="650" cy="220" r="4" fill="#dc2626"/>

            <!-- Vertex labels -->
            <text x="495" y="135" font-size="14" font-weight="700" fill="#0f172a">A</text>
            <text x="800" y="135" font-size="14" font-weight="700" fill="#0f172a">B</text>
            <text x="800" y="315" font-size="14" font-weight="700" fill="#0f172a">C</text>
            <text x="495" y="315" font-size="14" font-weight="700" fill="#0f172a">D</text>
            <text x="655" y="215" font-size="13" font-weight="700" fill="#dc2626">O</text>

            <!-- Right angle indicators -->
            <rect x="510" y="285" width="15" height="15" fill="none" stroke="#dc2626" stroke-width="1.5"/>
            <rect x="510" y="140" width="15" height="15" fill="none" stroke="#dc2626" stroke-width="1.5"/>

            <!-- Text summary in box -->
            <rect x="470" y="315" width="400" height="85" rx="8" fill="#eff6ff" stroke="#bfdbfe" stroke-width="1"/>
            <text x="485" y="335" font-size="11.5" font-weight="700" fill="#1e40af">Deduction 1 (Diagonals Equal):</text>
            <text x="485" y="352" font-size="11" fill="#1e3a8a">△ADC ≅ △DAB by SAS (AD common, ∠D=∠A=90°, CD=BA) ⇒ AC = BD</text>
            <text x="485" y="372" font-size="11.5" font-weight="700" fill="#1e40af">Deduction 2 (Diagonals Bisect):</text>
            <text x="485" y="389" font-size="11" fill="#1e3a8a">△AOB ≅ △COD by AAS ⇒ OA = OC and OB = OD (O is midpoint)</text>
          </svg>
        </div>
        <p class="caption">
          <strong>Figure 2.1:</strong> The Carpenter's Problem and the two cornerstone diagonal deductions for a rectangle.
        </p>
      </div>

      <h4 class="subheading-sm">Deduction 1: Why Diagonals of a Rectangle Have Equal Lengths</h4>
      <p>
        Let ABCD be a rectangle where all angles are 90° and opposite sides are equal (AB = CD and AD = BC). Consider the two overlapping right triangles sharing base AD: <strong>△ADC</strong> and <strong>△DAB</strong>.
      </p>
      <ul>
        <li><strong>AD = AD</strong> (Common base to both triangles)</li>
        <li><strong>∠ADC = ∠DAB = 90°</strong> (Every angle of a rectangle is a right angle)</li>
        <li><strong>CD = BA</strong> (Opposite sides of a rectangle are equal)</li>
      </ul>
      <p>
        Therefore, by the <strong>Side-Angle-Side (SAS) Congruence Criterion</strong>, we have:
        <br>
        <strong>△ADC ≅ △DAB</strong>.
      </p>
      <p>
        Since corresponding parts of congruent triangles are equal (CPCTC), their hypotenuses must be identical:
        <br>
        <strong>AC = BD</strong>.
        <br>
        <em>Conclusion: The second strip must also be exactly 8 cm long!</em>
      </p>

      <h4 class="subheading-sm">Deduction 2: Why Diagonals Intersect at Their Exact Midpoints (Bisection)</h4>
      <p>
        To find where the carpenter must pin the two strips, consider the opposite triangles formed inside the rectangle: <strong>△AOB</strong> and <strong>△COD</strong>.
      </p>
      <ul>
        <li>Since opposite sides of a rectangle are parallel (AB ∥ CD) with diagonal BD as a transversal, alternate interior angles are equal: <strong>∠ABO = ∠CDO</strong>.</li>
        <li>Similarly, with diagonal AC as transversal, alternate interior angles are equal: <strong>∠BAO = ∠DCO</strong>.</li>
        <li>Opposite sides are equal: <strong>AB = CD</strong>.</li>
      </ul>
      <p>
        Therefore, by the <strong>Angle-Side-Angle (ASA)</strong> or <strong>Angle-Angle-Side (AAS)</strong> condition:
        <br>
        <strong>△AOB ≅ △COD</strong>.
      </p>
      <p>
        By CPCTC, <strong>OA = OC</strong> and <strong>OB = OD</strong>. This proves that point O is the exact midpoint of both AC and BD. In geometric terminology, the diagonals <strong>bisect each other</strong>.
        <br>
        <em>Conclusion: The carpenter must drill the hinge hole at the exact center (4 cm from each end) of both 8 cm strips!</em>
      </p>

      <h4 class="subheading-sm">Deduction 3: Does the Angle Between Diagonals Matter?</h4>
      <p>
        Suppose the carpenter opens the hinged 8 cm strips at an arbitrary angle, say x = 60° (or any angle x between 0° and 180°). Will the taut thread around the four endpoints ALWAYS form a rectangle?
      </p>
      <p>
        Let us prove this algebraically:
      </p>
      <ol>
        <li>Because OA = OB = OC = OD = 4 cm, all four small interior triangles (△AOB, △BOC, △COD, △DOA) are <strong>isosceles triangles</strong>!</li>
        <li>Let the angle at the hinge be ∠AOB = x. Then vertically opposite angle ∠COD = x.</li>
        <li>The adjacent linear pair angles are ∠AOD = ∠BOC = 180° − x.</li>
        <li>In isosceles △AOB, the base angles are equal:
          <br>
          a + a + x = 180° ⇒ 2a = 180° − x ⇒ <strong>a = 90° − (x/2)</strong>.
        </li>
        <li>In adjacent isosceles △AOD, the base angles are equal:
          <br>
          b + b + (180° − x) = 180° ⇒ 2b = x ⇒ <strong>b = x/2</strong>.
        </li>
        <li>Now, calculate the total vertex angle ∠BAD:
          <br>
          <strong>∠BAD = a + b = [90° − (x/2)] + [x/2] = 90°!</strong>
        </li>
      </ol>
      <p>
        Notice that the variable <em>x cancels out completely</em>! No matter what angle x the carpenter chooses, every single corner angle is guaranteed to be exactly 90°.
      </p>

      <div class="callout callout-def">
        <div class="callout-title"><i class="fa-solid fa-star"></i> The Four Fundamental Properties of a Rectangle</div>
        <ol>
          <li><strong>All four interior angles are right angles (90°).</strong></li>
          <li><strong>Opposite sides are equal in length (AB = CD and AD = BC).</strong></li>
          <li><strong>Opposite sides are parallel to each other (AB ∥ CD and AD ∥ BC).</strong></li>
          <li><strong>The two diagonals are equal in length (AC = BD) and bisect each other (OA = OC = OB = OD).</strong></li>
        </ol>
      </div>

      <h4 class="subheading-sm">Deductions 4 &amp; 5: From Rectangles to Squares</h4>
      <p>
        <strong>Deduction 4:</strong> What if a quadrilateral simply has four 90° angles? Does it automatically have equal opposite sides?
        <br>
        Yes! In quadrilateral ABCD with ∠A = ∠B = ∠C = ∠D = 90°, drawing diagonal BD creates two right triangles: △BAD and △DCB. Because ∠A = ∠C = 90°, and alternate angles are equal (due to consecutive interior angles summing to 180°), △BAD ≅ △DCB by AAS. By CPCTC, AB = CD and AD = BC. Thus, <em>a rectangle can be defined simply as: "A quadrilateral in which all four angles are 90°."</em>
      </p>
      <p>
        <strong>Deduction 5: What makes a Rectangle a Square?</strong>
        <br>
        A <strong>Square</strong> is a special rectangle where all four sides are equal (AB = BC = CD = DA). What happens to the angle between the diagonals in a square?
      </p>
      <ul>
        <li>Consider adjacent triangles <strong>△AOB</strong> and <strong>△COB</strong> at the center O.</li>
        <li>AB = CB (All four sides of a square are equal).</li>
        <li>OA = OC (Diagonals bisect each other).</li>
        <li>OB = OB (Common side).</li>
        <li>Therefore, by <strong>SSS Congruence</strong>: <strong>△AOB ≅ △COB</strong>!</li>
        <li>By CPCTC: <strong>∠AOB = ∠COB</strong>.</li>
        <li>Since ∠AOB and ∠COB form a linear pair along straight diagonal AC:
          <br>
          ∠AOB + ∠COB = 180° ⇒ 2(∠AOB) = 180° ⇒ <strong>∠AOB = 90°!</strong>
        </li>
      </ul>
      <p>
        Furthermore, in right triangle △ADC where AD = DC, the diagonal creates an isosceles right triangle where the base angles are (180° − 90°)/2 = <strong>45°</strong> each! Thus, <em>the diagonals of a square bisect the 90° corner angles into two 45° angles.</em>
      </p>

      <!-- 2.3 ANGLES IN A QUADRILATERAL -->
      <h3 class="subheading"><i class="fa-solid fa-compass-drafting"></i> 2.3 Section 4.2: Angles in a Quadrilateral (The 360° Angle Sum Theorem)</h3>
      <p>
        Every student learns in Class 7 that the angles of a triangle sum to 180°. What is the universal law for a four-sided polygon?
      </p>

      <div class="callout callout-def">
        <div class="callout-title"><i class="fa-solid fa-certificate"></i> Theorem: The Angle Sum Property of a Quadrilateral</div>
        <p>
          <strong>Statement:</strong> The sum of the interior angle measures of any quadrilateral is strictly <strong>360°</strong>.
        </p>
        <p><strong>Formal Geometric Proof:</strong></p>
        <ol>
          <li>Let SOME be any arbitrary quadrilateral with interior angles ∠S, ∠O, ∠M, ∠E.</li>
          <li>Draw diagonal SM. This diagonal segments the quadrilateral into two distinct triangles: <strong>△SEM</strong> and <strong>△SOM</strong>.</li>
          <li>In △SEM, let the angles be ∠1, ∠2, ∠3. By the triangle angle sum theorem:
            <br>
            <strong>∠1 + ∠2 + ∠3 = 180°</strong> ...(Equation 1)
          </li>
          <li>In △SOM, let the angles be ∠4, ∠5, ∠6. By the triangle angle sum theorem:
            <br>
            <strong>∠4 + ∠5 + ∠6 = 180°</strong> ...(Equation 2)
          </li>
          <li>Adding Equation 1 and Equation 2:
            <br>
            (∠1 + ∠2 + ∠3) + (∠4 + ∠5 + ∠6) = 180° + 180° = 360°.
          </li>
          <li>Regrouping the angles at the shared vertices S and M:
            <br>
            (∠1 + ∠4) + ∠2 + (∠3 + ∠6) + ∠5 = 360°
            <br>
            <strong>∠S + ∠E + ∠M + ∠O = 360°</strong>.
          </li>
        </ol>
      </div>

      <p>
        <strong>Does this hold for Concave Quadrilaterals?</strong>
        <br>
        Yes! In textbook problem 10, consider arrowhead quadrilateral ADCB where vertex C is pushed inward, creating a reflex angle at C. Drawing diagonal BD still partitions the interior into two triangles: △ADB and △BDC. The angles of △ADB sum to 180° and the angles of △BDC sum to 180°. Adding them gives exactly 360°!
      </p>

      <div class="callout callout-warn">
        <div class="callout-title"><i class="fa-solid fa-triangle-exclamation"></i> Why a Quadrilateral Cannot Have Exactly Three 90° Angles</div>
        <p>
          Students often ask: <em>"Can I draw a quadrilateral where three angles are 90° and the fourth angle is 80°?"</em>
        </p>
        <p>
          <strong>Mathematical Impossibility:</strong> By the Angle Sum Property:
          <br>
          ∠1 + ∠2 + ∠3 + ∠4 = 360°
          <br>
          90° + 90° + 90° + ∠4 = 360°
          <br>
          270° + ∠4 = 360° ⇒ <strong>∠4 = 360° − 270° = 90° strictly!</strong>
          <br>
          Therefore, if three angles of a quadrilateral are right angles, the fourth angle is mathematically forced to be 90° as well. It is physically impossible to have three right angles without the figure being a rectangle!
        </p>
      </div>

      <!-- 2.4 PARALLELOGRAMS -->
      <h3 class="subheading"><i class="fa-solid fa-arrows-split-up-and-left"></i> 2.4 Section 4.3: Parallelograms (Deductions 6 to 8)</h3>
      <p>
        If we relax the strict condition that all angles must be 90°, but keep the condition that <strong>both pairs of opposite sides are parallel</strong>, we obtain the broad and versatile family of <strong>Parallelograms</strong>.
      </p>

      <!-- SVG DIAGRAM 3: PARALLELOGRAM & RHOMBUS PROOFS -->
      <div class="diagram-card">
        <div class="svg-container">
          <svg viewBox="0 0 920 440" xmlns="http://www.w3.org/2000/svg" style="background:#f8fafc; border-radius:12px; font-family:'Space Grotesk', sans-serif;">
            <text x="460" y="32" text-anchor="middle" font-size="20" font-weight="800" fill="#0f172a">PARALLELOGRAM &amp; RHOMBUS CONGRUENCE DEDUCTIONS</text>
            <text x="460" y="54" text-anchor="middle" font-size="12.5" fill="#64748b">Ganita Prakash Sections 4.3 &amp; 4.4: Angle, Side &amp; Diagonal Proofs</text>

            <!-- LEFT PANEL: PARALLELOGRAM -->
            <rect x="30" y="75" width="415" height="340" rx="14" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.5"/>
            <text x="237" y="105" text-anchor="middle" font-size="15" font-weight="700" fill="#065f46">1. Parallelogram Deductions (ABCD)</text>

            <!-- Parallelogram Drawing -->
            <polygon points="100,280 290,280 370,160 180,160" fill="rgba(16,185,129,0.08)" stroke="#059669" stroke-width="2.5"/>
            <!-- Diagonals -->
            <line x1="100" y1="280" x2="370" y2="160" stroke="#0284c7" stroke-width="1.8"/>
            <line x1="180" y1="160" x2="290" y2="280" stroke="#7c3aed" stroke-width="1.8"/>
            <circle cx="235" cy="220" r="4" fill="#dc2626"/>

            <!-- Vertices -->
            <text x="80" y="295" font-size="14" font-weight="700" fill="#0f172a">A</text>
            <text x="305" y="295" font-size="14" font-weight="700" fill="#0f172a">B</text>
            <text x="385" y="160" font-size="14" font-weight="700" fill="#0f172a">C</text>
            <text x="165" y="150" font-size="14" font-weight="700" fill="#0f172a">D</text>
            <text x="240" y="212" font-size="13" font-weight="700" fill="#dc2626">O</text>

            <!-- Alternate angle arcs -->
            <path d="M 125,280 A 25,25 0 0,0 120,265" fill="none" stroke="#2563eb" stroke-width="2"/>
            <path d="M 345,160 A 25,25 0 0,0 350,175" fill="none" stroke="#2563eb" stroke-width="2"/>

            <rect x="45" y="315" width="385" height="85" rx="8" fill="#f0fdf4" stroke="#bbf7d0" stroke-width="1"/>
            <text x="55" y="335" font-size="11.5" font-weight="700" fill="#065f46">Deduction 6 &amp; 7 (Sides &amp; Angles):</text>
            <text x="55" y="352" font-size="11" fill="#047857">Alternate angles equal + BD common ⇒ △ABD ≅ △CDB by AAS.</text>
            <text x="55" y="370" font-size="11" fill="#047857">⇒ Opposite sides equal (AB=CD, AD=BC) &amp; Opposite ∠ equal (∠A=∠C).</text>
            <text x="55" y="388" font-size="11" font-weight="700" fill="#065f46">Deduction 8: △AOB ≅ △COD by ASA ⇒ OA = OC, OB = OD.</text>

            <!-- RIGHT PANEL: RHOMBUS -->
            <rect x="475" y="75" width="415" height="340" rx="14" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.5"/>
            <text x="682" y="105" text-anchor="middle" font-size="15" font-weight="700" fill="#581c87">2. Rhombus 90° Diagonals (GAME)</text>

            <!-- Rhombus Drawing -->
            <polygon points="682,130 802,220 682,310 562,220" fill="rgba(124,58,237,0.08)" stroke="#7c3aed" stroke-width="2.5"/>
            <!-- Diagonals -->
            <line x1="682" y1="130" x2="682" y2="310" stroke="#dc2626" stroke-width="2"/>
            <line x1="562" y1="220" x2="802" y2="220" stroke="#dc2626" stroke-width="2"/>
            <circle cx="682" cy="220" r="4" fill="#0f172a"/>

            <!-- Right angle square at center -->
            <rect x="682" y="220" width="14" height="14" fill="none" stroke="#dc2626" stroke-width="1.5"/>

            <!-- Vertices GAME -->
            <text x="682" y="120" text-anchor="middle" font-size="14" font-weight="700" fill="#0f172a">G</text>
            <text x="815" y="225" font-size="14" font-weight="700" fill="#0f172a">A</text>
            <text x="682" y="330" text-anchor="middle" font-size="14" font-weight="700" fill="#0f172a">M</text>
            <text x="545" y="225" font-size="14" font-weight="700" fill="#0f172a">E</text>
            <text x="690" y="212" font-size="12" font-weight="700" fill="#dc2626">O</text>

            <rect x="490" y="315" width="385" height="85" rx="8" fill="#faf5ff" stroke="#e9d5ff" stroke-width="1"/>
            <text x="500" y="335" font-size="11.5" font-weight="700" fill="#581c87">Deduction 9 &amp; 10 (Rhombus 90° Intersection):</text>
            <text x="500" y="352" font-size="11" fill="#6d28d9">In △GEO and △MEO: GE=ME (equal sides), OE=OE (common),</text>
            <text x="500" y="370" font-size="11" fill="#6d28d9">OG=OM (diagonals bisect) ⇒ △GEO ≅ △MEO by SSS!</text>
            <text x="500" y="388" font-size="11" font-weight="700" fill="#581c87">⇒ ∠GOE = ∠MOE = 180°/2 = 90° (Perpendicular Bisectors!)</text>
          </svg>
        </div>
        <p class="caption">
          <strong>Figure 2.2:</strong> Mathematical proofs for Parallelograms (Deductions 6–8) and Rhombuses (Deductions 9–10).
        </p>
      </div>

      <h4 class="subheading-sm">Deduction 6: Parallelogram Angle Relationships</h4>
      <p>
        In parallelogram ABCD, opposite sides are parallel by definition: AB ∥ CD and AD ∥ BC.
      </p>
      <ul>
        <li>Treat side AD as a transversal intersecting the parallel lines AB and CD. By the parallel line theorem, consecutive interior angles on the same side of a transversal are supplementary:
          <br>
          <strong>∠A + ∠D = 180°</strong> ⇒ ∠D = 180° − ∠A.
        </li>
        <li>Treat side AB as a transversal intersecting parallel lines AD and BC:
          <br>
          <strong>∠A + ∠B = 180°</strong> ⇒ ∠B = 180° − ∠A.
        </li>
        <li>Treat side CD as a transversal intersecting parallel lines AD and BC:
          <br>
          <strong>∠C + ∠D = 180°</strong> ⇒ ∠C = 180° − ∠D = 180° − (180° − ∠A) = <strong>∠A</strong>!
        </li>
      </ul>
      <p>
        <em>Key Discoveries:</em>
        <br>
        1. <strong>Adjacent angles are supplementary:</strong> (∠A + ∠B = 180°, ∠B + ∠C = 180°, ∠C + ∠D = 180°, ∠D + ∠A = 180°).
        <br>
        2. <strong>Opposite angles are equal:</strong> (∠A = ∠C and ∠B = ∠D).
      </p>

      <h4 class="subheading-sm">Deductions 7 &amp; 8: Parallelogram Sides and Diagonal Bisection</h4>
      <p>
        <strong>Deduction 7 (Opposite sides equal):</strong> Draw diagonal BD. Because AD ∥ BC, alternate interior angles ∠ADB = ∠CBD. Because AB ∥ CD, alternate interior angles ∠ABD = ∠CDB. With common side BD, <strong>△ABD ≅ △CDB</strong> by AAS/ASA. By CPCTC:
        <br>
        <strong>AB = CD</strong> and <strong>AD = BC</strong>.
      </p>
      <p>
        <strong>Deduction 8 (Diagonals bisect each other):</strong> In opposite triangles △AOB and △COD, AB = CD, ∠OAB = ∠OCD, and ∠OBA = ∠ODC. By ASA congruence:
        <br>
        <strong>△AOB ≅ △COD</strong> ⇒ <strong>OA = OC</strong> and <strong>OB = OD</strong>.
      </p>

      <!-- 2.5 RHOMBUSES -->
      <h3 class="subheading"><i class="fa-solid fa-gem"></i> 2.5 Section 4.4: Rhombuses (Deductions 9 and 10)</h3>
      <p>
        A <strong>Rhombus</strong> is defined as a quadrilateral in which <strong>all four sides have equal length</strong>.
      </p>
      <p>
        Since all sides are equal, opposite sides are equal, which automatically makes every rhombus a parallelogram! Therefore, a rhombus inherits all properties of a parallelogram (opposite angles equal, adjacent angles supplementary, diagonals bisect). But a rhombus possesses two extraordinary additional properties:
      </p>

      <div class="callout callout-def">
        <div class="callout-title"><i class="fa-solid fa-bolt"></i> The Two Super-Properties of a Rhombus</div>
        <ol>
          <li><strong>Diagonals Bisect the Vertex Angles:</strong> In rhombus GAME, diagonal AE divides ∠G AM into two equal angles (a = b = c = d), and diagonal GM divides ∠G and ∠M into equal halves.</li>
          <li><strong>Diagonals Intersect at Exactly 90° (Perpendicular Bisectors):</strong> As proven in Deduction 10, adjacent triangles △GEO and △MEO are congruent by SSS. The linear pair angles at the center are equal: ∠GOE = ∠MOE = 180°/2 = 90°!</li>
        </ol>
      </div>

      <!-- 2.6 PLAYING WITH QUADRILATERALS -->
      <h3 class="subheading"><i class="fa-solid fa-puzzle-piece"></i> 2.6 Section 4.5: Playing with Quadrilaterals (Geoboard &amp; Triangle Joining)</h3>
      <p>
        In Section 4.5, students explore the structural behavior of quadrilaterals through physical experimentation:
      </p>
      <ul>
        <li><strong>Geoboard Exploration:</strong>
          <br>
          1. Placing two equal rubber bands perpendicular to each other so they bisect at 90° forms a <strong>Square</strong>.
          <br>
          2. Extending one diagonal equally on both ends (so diagonals are perpendicular, bisect each other, but have <em>unequal lengths</em>) produces a <strong>Rhombus</strong>.
          <br>
          3. Extending one diagonal on only <em>one</em> end (so diagonals are perpendicular, but only one is bisected) produces a <strong>Kite</strong>!
        </li>
        <li><strong>Joining Triangles:</strong>
          <br>
          1. Joining two identical <strong>equilateral triangles</strong> (side 8 cm) along their shared base produces a <strong>Rhombus</strong> with angles 60°, 120°, 60°, 120°.
          <br>
          2. Joining two identical <strong>isosceles triangles</strong> (8 cm, 8 cm, 6 cm) along the 6 cm base yields a <strong>Rhombus</strong> (all 4 sides = 8 cm). Joining them along an 8 cm leg yields a <strong>Kite</strong> (adjacent sides 8 cm, 8 cm and 6 cm, 6 cm) or a <strong>Parallelogram</strong> if one triangle is flipped!
          <br>
          3. Joining two identical <strong>scalene triangles</strong> (6 cm, 9 cm, 12 cm) along corresponding equal sides produces a <strong>Parallelogram</strong> (by translation/rotation) or a <strong>Kite</strong> (by reflection)!
        </li>
      </ul>

      <!-- 2.7 KITES AND TRAPEZIUMS -->
      <h3 class="subheading"><i class="fa-solid fa-paper-plane"></i> 2.7 Section 4.6: Kites and Trapeziums (Isosceles Trapezium RHS Proof)</h3>

      <div class="callout callout-def">
        <div class="callout-title"><i class="fa-solid fa-kite"></i> The Kite: Anatomy &amp; Symmetry</div>
        <p>
          A <strong>Kite</strong> is a quadrilateral with two distinct pairs of adjacent sides of equal length (AB = BC and CD = DA).
        </p>
        <p><strong>Core Properties of a Kite:</strong></p>
        <ul>
          <li><strong>One Axis of Reflection Symmetry:</strong> The main diagonal BD acts as a line of mirror symmetry: <strong>△ABD ≅ △CBD</strong> by SSS.</li>
          <li><strong>Perpendicular Diagonals:</strong> Diagonals intersect at right angles: <strong>AC ⊥ BD</strong>.</li>
          <li><strong>Only ONE Diagonal is Bisected:</strong> The symmetry diagonal BD bisects the cross diagonal AC (i.e., <strong>AO = OC</strong>). However, AC does NOT bisect BD! (OB ≠ OD in general).</li>
          <li><strong>One Pair of Equal Opposite Angles:</strong> The angles between the unequal sides are equal: <strong>∠BAD = ∠BCD</strong>. The other pair of opposite angles are unequal: ∠ABC ≠ ∠ADC.</li>
        </ul>
      </div>

      <!-- SVG DIAGRAM 4: KITE ANATOMY -->
      <div class="diagram-card">
        <div class="svg-container">
          <svg viewBox="0 0 860 400" xmlns="http://www.w3.org/2000/svg" style="background:#f8fafc; border-radius:12px; font-family:'Space Grotesk', sans-serif;">
            <text x="430" y="30" text-anchor="middle" font-size="19" font-weight="800" fill="#0f172a">KITE GEOMETRIC ANATOMY &amp; LINE OF SYMMETRY</text>
            <text x="430" y="50" text-anchor="middle" font-size="12" fill="#64748b">Ganita Prakash Section 4.6: Diagonal Bisection &amp; Angle Relationships</text>

            <!-- Kite Outline -->
            <polygon points="430,80 570,190 430,350 290,190" fill="rgba(244,63,94,0.08)" stroke="#e11d48" stroke-width="2.5"/>

            <!-- Diagonals -->
            <!-- Main Diagonal BD (Axis of symmetry) -->
            <line x1="430" y1="80" x2="430" y2="350" stroke="#2563eb" stroke-width="2.5" stroke-dasharray="6,4"/>
            <!-- Cross Diagonal AC -->
            <line x1="290" y1="190" x2="570" y2="190" stroke="#7c3aed" stroke-width="2"/>

            <!-- Intersection O -->
            <circle cx="430" cy="190" r="4" fill="#0f172a"/>
            <text x="445" y="185" font-size="13" font-weight="700" fill="#0f172a">O</text>
            <!-- Right angle at O -->
            <rect x="430" y="190" width="14" height="14" fill="none" stroke="#2563eb" stroke-width="1.5"/>

            <!-- Vertices -->
            <text x="430" y="70" text-anchor="middle" font-size="15" font-weight="800" fill="#be123c">B</text>
            <text x="585" y="195" font-size="15" font-weight="800" fill="#be123c">C</text>
            <text x="430" y="375" text-anchor="middle" font-size="15" font-weight="800" fill="#be123c">D</text>
            <text x="270" y="195" font-size="15" font-weight="800" fill="#be123c">A</text>

            <!-- Side equality hash marks -->
            <line x1="355" y1="130" x2="365" y2="140" stroke="#e11d48" stroke-width="2"/>
            <line x1="495" y1="140" x2="505" y2="130" stroke="#e11d48" stroke-width="2"/>
            <text x="350" y="125" font-size="12" font-weight="700" fill="#be123c">AB = BC</text>

            <line x1="355" y1="265" x2="365" y2="275" stroke="#e11d48" stroke-width="2"/>
            <line x1="360" y1="262" x2="370" y2="272" stroke="#e11d48" stroke-width="2"/>
            <line x1="495" y1="275" x2="505" y2="265" stroke="#e11d48" stroke-width="2"/>
            <line x1="490" y1="272" x2="500" y2="262" stroke="#e11d48" stroke-width="2"/>
            <text x="340" y="295" font-size="12" font-weight="700" fill="#be123c">AD = CD</text>

            <!-- Annotations -->
            <rect x="630" y="110" width="200" height="110" rx="8" fill="#eff6ff" stroke="#bfdbfe" stroke-width="1"/>
            <text x="640" y="132" font-size="12" font-weight="700" fill="#1e40af">Symmetry Diagonal (BD):</text>
            <text x="640" y="152" font-size="11" fill="#1e3a8a">• Perpendicular bisector of AC</text>
            <text x="640" y="170" font-size="11" fill="#1e3a8a">• AO = OC (cross diagonal bisected)</text>
            <text x="640" y="188" font-size="11" fill="#1e3a8a">• Bisects ∠B and ∠D</text>
            <text x="640" y="206" font-size="11" fill="#1e3a8a">• Axis of reflection symmetry</text>

            <rect x="30" y="110" width="220" height="90" rx="8" fill="#fdf2f8" stroke="#fbcfe8" stroke-width="1"/>
            <text x="40" y="132" font-size="12" font-weight="700" fill="#9d174d">Angle Relationships:</text>
            <text x="40" y="152" font-size="11" fill="#831843">• ∠A = ∠C (between unequal sides)</text>
            <text x="40" y="170" font-size="11" fill="#831843">• ∠B ≠ ∠D (unless it's a Rhombus)</text>
            <text x="40" y="188" font-size="11" fill="#831843">• AC ⊥ BD (diagonals at 90°)</text>
          </svg>
        </div>
        <p class="caption">
          <strong>Figure 2.3:</strong> Anatomy of a Kite. Note that the main diagonal BD bisects the cross diagonal AC, but AC does not bisect BD.
        </p>
      </div>

      <div class="callout callout-def">
        <div class="callout-title"><i class="fa-solid fa-shapes"></i> The Trapezium &amp; Isosceles Trapezium</div>
        <p>
          A <strong>Trapezium</strong> is defined as a quadrilateral with <strong>at least one pair of parallel opposite sides</strong>.
        </p>
        <ul>
          <li><strong>Property 1 (Co-interior Angles):</strong> If PQ ∥ SR, then consecutive angles along each non-parallel leg add up to 180°:
            <br>
            <strong>∠S + ∠P = 180°</strong> and <strong>∠R + ∠Q = 180°</strong>.
          </li>
          <li><strong>Isosceles Trapezium:</strong> When the non-parallel legs are equal in length (UX = VW), the figure becomes an <em>Isosceles Trapezium</em>.
          </li>
        </ul>
      </div>

      <!-- SVG DIAGRAM 5: ISOSCELES TRAPEZIUM CONGRUENCE -->
      <div class="diagram-card">
        <div class="svg-container">
          <svg viewBox="0 0 860 400" xmlns="http://www.w3.org/2000/svg" style="background:#f8fafc; border-radius:12px; font-family:'Space Grotesk', sans-serif;">
            <text x="430" y="30" text-anchor="middle" font-size="19" font-weight="800" fill="#0f172a">ISOSCELES TRAPEZIUM CONGRUENCE PROOF (RHS)</text>
            <text x="430" y="50" text-anchor="middle" font-size="12" fill="#64748b">Ganita Prakash Page 106: Proving Base Angles &amp; Diagonals are Equal</text>

            <!-- Trapezium UVWX -->
            <polygon points="180,310 680,310 580,150 280,150" fill="rgba(245,158,11,0.08)" stroke="#d97706" stroke-width="2.5"/>

            <!-- Altitudes XY and WZ -->
            <line x1="280" y1="150" x2="280" y2="310" stroke="#dc2626" stroke-width="2" stroke-dasharray="5,4"/>
            <line x1="580" y1="150" x2="580" y2="310" stroke="#dc2626" stroke-width="2" stroke-dasharray="5,4"/>

            <!-- Right angle boxes -->
            <rect x="280" y="294" width="16" height="16" fill="none" stroke="#dc2626" stroke-width="1.5"/>
            <rect x="264" y="294" width="16" height="16" fill="none" stroke="#dc2626" stroke-width="1.5"/>
            <rect x="580" y="294" width="16" height="16" fill="none" stroke="#dc2626" stroke-width="1.5"/>
            <rect x="564" y="294" width="16" height="16" fill="none" stroke="#dc2626" stroke-width="1.5"/>

            <!-- Vertices -->
            <text x="160" y="325" font-size="15" font-weight="800" fill="#0f172a">U</text>
            <text x="700" y="325" font-size="15" font-weight="800" fill="#0f172a">V</text>
            <text x="590" y="140" font-size="15" font-weight="800" fill="#0f172a">W</text>
            <text x="270" y="140" font-size="15" font-weight="800" fill="#0f172a">X</text>
            <text x="280" y="335" text-anchor="middle" font-size="14" font-weight="700" fill="#dc2626">Y</text>
            <text x="580" y="335" text-anchor="middle" font-size="14" font-weight="700" fill="#dc2626">Z</text>

            <!-- Side equality marks -->
            <line x1="225" y1="225" x2="235" y2="235" stroke="#d97706" stroke-width="2"/>
            <line x1="625" y1="235" x2="635" y2="225" stroke="#d97706" stroke-width="2"/>
            <text x="180" y="220" font-size="12" font-weight="700" fill="#b45309">UX (Leg)</text>
            <text x="640" y="220" font-size="12" font-weight="700" fill="#b45309">VW (Leg)</text>

            <!-- Base angles -->
            <path d="M 215,310 A 35,35 0 0,0 205,280" fill="none" stroke="#2563eb" stroke-width="2"/>
            <text x="225" y="295" font-size="13" font-weight="700" fill="#2563eb">∠U</text>
            <path d="M 645,310 A 35,35 0 0,1 655,280" fill="none" stroke="#2563eb" stroke-width="2"/>
            <text x="630" y="295" font-size="13" font-weight="700" fill="#2563eb">∠V</text>

            <!-- Bottom proof card -->
            <rect x="180" y="348" width="500" height="42" rx="6" fill="#fef3c7" stroke="#fcd34d" stroke-width="1"/>
            <text x="430" y="374" text-anchor="middle" font-size="12.5" font-weight="700" fill="#78350f">
              XY = WZ (Altitudes) &amp; UX = VW (Hypotenuses) ⇒ △UXY ≅ △VWZ (RHS) ⇒ ∠U = ∠V!
            </text>
          </svg>
        </div>
        <p class="caption">
          <strong>Figure 2.4:</strong> Rigorous RHS congruence proof showing that base angles are equal in an isosceles trapezium.
        </p>
      </div>

      <h4 class="subheading-sm">Proof: In an Isosceles Trapezium, Base Angles are Equal (Property 2)</h4>
      <p>
        Let UVWX be an isosceles trapezium with UV ∥ XW and UX = VW.
      </p>
      <ol>
        <li>Drop perpendiculars from top vertices X and W down to the base UV, meeting UV at points Y and Z respectively:
          <br>
          <strong>XY ⊥ UV</strong> and <strong>WZ ⊥ UV</strong>.
        </li>
        <li>Since XW ∥ YZ and both altitudes are perpendicular to the parallel lines, XY and WZ are parallel and represent the perpendicular distance between two parallel lines. Thus, <strong>XY = WZ</strong>, and XWZY is a rectangle.</li>
        <li>Now compare the two outside right-angled triangles: <strong>△UXY</strong> and <strong>△VWZ</strong>:
          <ul>
            <li><strong>∠UYX = ∠VZW = 90°</strong> (Right angle)</li>
            <li><strong>UX = VW</strong> (Hypotenuses are equal, given by definition of isosceles trapezium)</li>
            <li><strong>XY = WZ</strong> (Perpendicular distance between parallel lines)</li>
          </ul>
        </li>
        <li>Therefore, by the <strong>Right angle-Hypotenuse-Side (RHS) Congruence Criterion</strong>:
          <br>
          <strong>△UXY ≅ △VWZ</strong>!
        </li>
        <li>By CPCTC, the corresponding base angles are equal:
          <br>
          <strong>∠U = ∠V</strong>.
        </li>
        <li>Because consecutive co-interior angles sum to 180°:
          <br>
          ∠X = 180° − ∠U and ∠W = 180° − ∠V. Since ∠U = ∠V, we also have <strong>∠X = ∠W</strong>!
        </li>
      </ol>
      <p>
        <em>Conclusion: In an isosceles trapezium, both pairs of base angles are equal (∠U = ∠V and ∠X = ∠W), and by SSS or SAS congruence, its diagonals are also equal: <strong>UW = VX</strong>!</em>
      </p>

      <!-- SVG DIAGRAM 6: SQUARE IN A SQUARE (FIGURE IT OUT Q7) -->
      <h3 class="subheading"><i class="fa-solid fa-vector-square"></i> 2.8 The Square-in-a-Square Geometric Induction (Figure it Out Q7)</h3>
      <p>
        One of the most elegant geometric problems in Ganita Prakash Grade 8 explores what happens when we connect the midpoints of the sides of a square.
      </p>

      <div class="diagram-card">
        <div class="svg-container">
          <svg viewBox="0 0 820 420" xmlns="http://www.w3.org/2000/svg" style="background:#f8fafc; border-radius:12px; font-family:'Space Grotesk', sans-serif;">
            <text x="410" y="30" text-anchor="middle" font-size="19" font-weight="800" fill="#0f172a">SQUARE WITHIN A SQUARE: MIDPOINT GEOMETRY</text>
            <text x="410" y="50" text-anchor="middle" font-size="12" fill="#64748b">Ganita Prakash Page 108 (Figure it Out Question 7): Proof that UVWX is a Square</text>

            <!-- Outer Square CASE -->
            <rect x="250" y="70" width="320" height="320" fill="rgba(37,99,235,0.06)" stroke="#1e293b" stroke-width="2.5"/>

            <!-- Midpoints: U (top), V (right), W (bottom), X (left) -->
            <!-- Inner Square UVWX -->
            <polygon points="410,70 570,230 410,390 250,230" fill="rgba(16,185,129,0.18)" stroke="#059669" stroke-width="2.5"/>

            <!-- Vertices of outer square CASE -->
            <text x="235" y="75" font-size="15" font-weight="800" fill="#0f172a">C</text>
            <text x="585" y="75" font-size="15" font-weight="800" fill="#0f172a">A</text>
            <text x="585" y="405" font-size="15" font-weight="800" fill="#0f172a">S</text>
            <text x="235" y="405" font-size="15" font-weight="800" fill="#0f172a">E</text>

            <!-- Midpoint labels -->
            <circle cx="410" cy="70" r="5" fill="#dc2626"/>
            <text x="410" y="60" text-anchor="middle" font-size="14" font-weight="800" fill="#dc2626">U (Midpoint of CA)</text>
            <circle cx="570" cy="230" r="5" fill="#dc2626"/>
            <text x="595" y="235" font-size="14" font-weight="800" fill="#dc2626">V (Midpoint of AS)</text>
            <circle cx="410" cy="390" r="5" fill="#dc2626"/>
            <text x="410" y="412" text-anchor="middle" font-size="14" font-weight="800" fill="#dc2626">W (Midpoint of SE)</text>
            <circle cx="250" cy="230" r="5" fill="#dc2626"/>
            <text x="225" y="235" text-anchor="end" font-size="14" font-weight="800" fill="#dc2626">X (Midpoint of EC)</text>

            <!-- Corner Triangles: 45° angle arcs -->
            <path d="M 270,70 A 20,20 0 0,1 264,84" fill="none" stroke="#2563eb" stroke-width="1.5"/>
            <text x="280" y="90" font-size="11" font-weight="700" fill="#2563eb">45°</text>
            <path d="M 250,210 A 20,20 0 0,1 264,216" fill="none" stroke="#2563eb" stroke-width="1.5"/>
            <text x="270" y="210" font-size="11" font-weight="700" fill="#2563eb">45°</text>

            <!-- Linear pair indicator at vertex X -->
            <text x="275" y="248" font-size="12" font-weight="800" fill="#065f46">90°</text>

            <!-- Side dimension labels -->
            <text x="330" y="65" font-size="11" fill="#64748b">x/2</text>
            <text x="490" y="65" font-size="11" fill="#64748b">x/2</text>
            <text x="235" y="150" font-size="11" fill="#64748b">x/2</text>
            <text x="235" y="310" font-size="11" fill="#64748b">x/2</text>

            <!-- Explanatory note -->
            <rect x="20" y="120" width="190" height="150" rx="8" fill="#eff6ff" stroke="#bfdbfe" stroke-width="1"/>
            <text x="30" y="142" font-size="12" font-weight="700" fill="#1e40af">Pythagoras &amp; Angles:</text>
            <text x="30" y="162" font-size="11" fill="#1e3a8a">• Legs = x/2</text>
            <text x="30" y="180" font-size="11" fill="#1e3a8a">• Hypotenuse = x/√2</text>
            <text x="30" y="198" font-size="11" fill="#1e3a8a">• All 4 sides equal</text>
            <text x="30" y="216" font-size="11" fill="#1e3a8a">• Base ∠ = 45° each</text>
            <text x="30" y="234" font-size="11" font-weight="700" fill="#065f46">• Corner ∠ = 180°−90°</text>
            <text x="30" y="252" font-size="11" font-weight="700" fill="#065f46">  = 90° strictly!</text>
          </svg>
        </div>
        <p class="caption">
          <strong>Figure 2.5:</strong> Proof that connecting the midpoints of the sides of a square generates another perfect square inside!
        </p>
      </div>

      <!-- 2.9 EXHAUSTIVE BILINGUAL VOCABULARY -->
      <h3 class="subheading"><i class="fa-solid fa-language"></i> 2.9 Exhaustive Bilingual Vocabulary &amp; Concept Glossary (32 Terms)</h3>
      <p>
        To support students from CBSE English Medium as well as BSE Odisha (Odia Medium) who are transitioning to standard mathematical terms, here is the complete bilingual glossary for Chapter 4:
      </p>

      <div class="table-container">
        <table class="data-table">
          <thead>
            <tr>
              <th>#</th>
              <th>Term / Concept</th>
              <th>Part of Speech</th>
              <th>English Meaning &amp; Mathematical Definition</th>
              <th>ଓଡ଼ିଆ ଅର୍ଥ (Odia Meaning in Odia script)</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>1</td>
              <td><strong>Quadrilateral</strong></td>
              <td>Noun</td>
              <td>A closed four-sided polygon lying in a single plane.</td>
              <td><strong>ଚତୁର୍ଭୁଜ (Chaturbhuja)</strong></td>
            </tr>
            <tr>
              <td>2</td>
              <td><strong>Rectangle</strong></td>
              <td>Noun</td>
              <td>A parallelogram with four right angles (90°).</td>
              <td><strong>ଆୟତକ୍ଷେତ୍ର (Aayatakhetra)</strong></td>
            </tr>
            <tr>
              <td>3</td>
              <td><strong>Square</strong></td>
              <td>Noun</td>
              <td>A regular quadrilateral with four equal sides and four right angles.</td>
              <td><strong>ବର୍ଗଚିତ୍ର (Bargachitra)</strong></td>
            </tr>
            <tr>
              <td>4</td>
              <td><strong>Parallelogram</strong></td>
              <td>Noun</td>
              <td>A quadrilateral with both pairs of opposite sides parallel.</td>
              <td><strong>ସାମାନ୍ତରିକ ଚିତ୍ର (Samantarika Chitra)</strong></td>
            </tr>
            <tr>
              <td>5</td>
              <td><strong>Rhombus</strong></td>
              <td>Noun</td>
              <td>An equilateral quadrilateral with all four sides of equal length.</td>
              <td><strong>ରମ୍ବସ୍ (Rombas)</strong></td>
            </tr>
            <tr>
              <td>6</td>
              <td><strong>Trapezium</strong></td>
              <td>Noun</td>
              <td>A quadrilateral having at least one pair of parallel opposite sides.</td>
              <td><strong>ଟ୍ରାପିଜିୟମ୍ (Trapijiyam)</strong></td>
            </tr>
            <tr>
              <td>7</td>
              <td><strong>Isosceles Trapezium</strong></td>
              <td>Noun</td>
              <td>A trapezium whose non-parallel legs are equal in length.</td>
              <td><strong>ସମଦ୍ୱିବାହୁ ଟ୍ରାପିଜିୟମ୍ (Samadwibahu Trapijiyam)</strong></td>
            </tr>
            <tr>
              <td>8</td>
              <td><strong>Kite</strong></td>
              <td>Noun</td>
              <td>A quadrilateral with two distinct pairs of equal adjacent sides.</td>
              <td><strong>କାଇଟ୍ / ଚିଲପତଙ୍ଗ ଚତୁର୍ଭୁଜ (Kite / Chila Patanga Chaturbhuja)</strong></td>
            </tr>
            <tr>
              <td>9</td>
              <td><strong>Diagonal</strong></td>
              <td>Noun</td>
              <td>A straight line segment connecting two non-consecutive vertices.</td>
              <td><strong>କର୍ଣ୍ଣ (Karna)</strong></td>
            </tr>
            <tr>
              <td>10</td>
              <td><strong>Vertex (pl. Vertices)</strong></td>
              <td>Noun</td>
              <td>The intersection point where two adjacent sides meet.</td>
              <td><strong>ଶୀର୍ଷ ବିନ୍ଦୁ (Shirsha Bindu)</strong></td>
            </tr>
            <tr>
              <td>11</td>
              <td><strong>Adjacent Sides</strong></td>
              <td>Noun</td>
              <td>Two sides of a polygon that share a common vertex.</td>
              <td><strong>ସନ୍ନିହିତ ବାହୁ (Sannihita Bahu)</strong></td>
            </tr>
            <tr>
              <td>12</td>
              <td><strong>Opposite Sides</strong></td>
              <td>Noun</td>
              <td>Two sides of a quadrilateral that do not share any common vertex.</td>
              <td><strong>ବିପରୀତ ବାହୁ (Biparita Bahu)</strong></td>
            </tr>
            <tr>
              <td>13</td>
              <td><strong>Adjacent Angles</strong></td>
              <td>Noun</td>
              <td>Two angles of a polygon that share a common side.</td>
              <td><strong>ସନ୍ନିହିତ କୋଣ (Sannihita Kona)</strong></td>
            </tr>
            <tr>
              <td>14</td>
              <td><strong>Opposite Angles</strong></td>
              <td>Noun</td>
              <td>Two angles of a quadrilateral situated across from each other.</td>
              <td><strong>ବିପରୀତ କୋଣ (Biparita Kona)</strong></td>
            </tr>
            <tr>
              <td>15</td>
              <td><strong>Bisect</strong></td>
              <td>Verb</td>
              <td>To divide a line segment, angle, or figure into two equal parts.</td>
              <td><strong>ସମଦ୍ୱିଖଣ୍ଡ କରିବା (Samadwikhando Kariba)</strong></td>
            </tr>
            <tr>
              <td>16</td>
              <td><strong>Perpendicular Bisector</strong></td>
              <td>Noun</td>
              <td>A line cutting another segment at 90° through its exact midpoint.</td>
              <td><strong>ଲମ୍ବ ସମଦ୍ୱିଖଣ୍ଡକ (Lamba Samadwikhondaka)</strong></td>
            </tr>
            <tr>
              <td>17</td>
              <td><strong>Interior Angle</strong></td>
              <td>Noun</td>
              <td>An angle formed inside the boundary between two adjacent sides.</td>
              <td><strong>ଅନ୍ତଃସ୍ଥ କୋଣ (Antahastha Kona)</strong></td>
            </tr>
            <tr>
              <td>18</td>
              <td><strong>Exterior Angle</strong></td>
              <td>Noun</td>
              <td>An angle formed outside between one side and the extension of an adjacent side.</td>
              <td><strong>ବହିଃସ୍ଥ କୋଣ (Bahihstha Kona)</strong></td>
            </tr>
            <tr>
              <td>19</td>
              <td><strong>Supplementary Angles</strong></td>
              <td>Noun</td>
              <td>Two angles whose measures add up to exactly 180°.</td>
              <td><strong>ପରିପୂରକ କୋଣ (Paripuraka Kona)</strong></td>
            </tr>
            <tr>
              <td>20</td>
              <td><strong>Complementary Angles</strong></td>
              <td>Noun</td>
              <td>Two angles whose measures add up to exactly 90°.</td>
              <td><strong>ଅନୁପୂରକ କୋଣ (Anupuraka Kona)</strong></td>
            </tr>
            <tr>
              <td>21</td>
              <td><strong>Transversal</strong></td>
              <td>Noun</td>
              <td>A line that intersects two or more lines at distinct points.</td>
              <td><strong>ଛେଦକ (Chhedaka)</strong></td>
            </tr>
            <tr>
              <td>22</td>
              <td><strong>Alternate Interior Angles</strong></td>
              <td>Noun</td>
              <td>Pairs of interior angles on opposite sides of a transversal between parallel lines.</td>
              <td><strong>ଏକାନ୍ତର ଅନ୍ତଃସ୍ଥ କୋଣ (Ekantara Antahastha Kona)</strong></td>
            </tr>
            <tr>
              <td>23</td>
              <td><strong>Co-Interior Angles</strong></td>
              <td>Noun</td>
              <td>Consecutive interior angles on the same side of a transversal that sum to 180°.</td>
              <td><strong>ଏକପାର୍ଶ୍ୱସ୍ଥ ଅନ୍ତଃସ୍ଥ କୋଣ (Ekaparshwastha Antahastha Kona)</strong></td>
            </tr>
            <tr>
              <td>24</td>
              <td><strong>Congruent Triangles</strong></td>
              <td>Noun</td>
              <td>Triangles having identical shape and size with equal corresponding parts.</td>
              <td><strong>ସର୍ବସମ ତ୍ରିଭୁଜ (Sarbasama Tribhuja)</strong></td>
            </tr>
            <tr>
              <td>25</td>
              <td><strong>Convex Quadrilateral</strong></td>
              <td>Noun</td>
              <td>A quadrilateral where all interior angles are strictly &lt; 180° and diagonals lie inside.</td>
              <td><strong>ଉତ୍ତଳ ଚତୁର୍ଭୁଜ (Uttala Chaturbhuja)</strong></td>
            </tr>
            <tr>
              <td>26</td>
              <td><strong>Concave Quadrilateral</strong></td>
              <td>Noun</td>
              <td>A quadrilateral having one reflex interior angle (&gt; 180°) and a diagonal outside.</td>
              <td><strong>ଅବତଳ ଚତୁର୍ଭୁଜ (Abatala Chaturbhuja)</strong></td>
            </tr>
            <tr>
              <td>27</td>
              <td><strong>Angle Sum Property</strong></td>
              <td>Noun</td>
              <td>The fundamental law stating that the interior angles of a quadrilateral sum to 360°.</td>
              <td><strong>କୋଣ ସମଷ୍ଟି ଧର୍ମ (Kona Samashti Dharma)</strong></td>
            </tr>
            <tr>
              <td>28</td>
              <td><strong>Venn Diagram</strong></td>
              <td>Noun</td>
              <td>A diagram using closed curves to represent sets and their logical inclusions.</td>
              <td><strong>ଭେନ୍ ଚିତ୍ର (Venn Chitra)</strong></td>
            </tr>
            <tr>
              <td>29</td>
              <td><strong>Axis of Symmetry</strong></td>
              <td>Noun</td>
              <td>A line dividing a figure into two mirror-image congruent halves.</td>
              <td><strong>ପ୍ରତିସାମ୍ୟ ଅକ୍ଷ (Pratisamya Aksha)</strong></td>
            </tr>
            <tr>
              <td>30</td>
              <td><strong>Altitude (Height)</strong></td>
              <td>Noun</td>
              <td>The perpendicular distance between two parallel bases of a trapezium.</td>
              <td><strong>ଉଚ୍ଚତା / ଲମ୍ବ ଦୂରତା (Uchhata / Lamba Durata)</strong></td>
            </tr>
            <tr>
              <td>31</td>
              <td><strong>Collinear Points</strong></td>
              <td>Noun</td>
              <td>Points that all lie along a single straight line.</td>
              <td><strong>ଏକରେଖୀୟ ବିନ୍ଦୁ (Ekarekhiya Bindu)</strong></td>
            </tr>
            <tr>
              <td>32</td>
              <td><strong>Non-Collinear Points</strong></td>
              <td>Noun</td>
              <td>Points that do not all lie along the same straight line.</td>
              <td><strong>ଅଣ-ଏକରେଖୀୟ ବିନ୍ଦୁ (Ana-ekarekhiya Bindu)</strong></td>
            </tr>
          </tbody>
        </table>
      </div>
    </section>
"""
