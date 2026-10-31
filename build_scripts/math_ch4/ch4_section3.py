# -*- coding: utf-8 -*-
"""
Module: ch4_section3.py
Contains Section 3: Rapid Revision Fact & Formula/Law Bank
Features:
- Master Property Matrix Table (comparing all 8 quad types across 12 properties)
- Rapid Formulas Bank (Perimeters, Areas, Diagonals)
- Minimal Sufficient Conditions for Identification Bank
"""

def get_section_3():
    return """
    <!-- SECTION 3: RAPID REVISION FACT & FORMULA BANK -->
    <section id="section-3">
      <div class="section-header">
        <div class="section-tag"><i class="fa-solid fa-table-list"></i> Quick Reference Vault</div>
        <h2 class="section-title">Section 3: Rapid Revision Fact &amp; Formula/Law Bank</h2>
        <p class="section-desc">
          High-yield reference tables comparing every structural property, symmetry order, area and perimeter formula, and the minimal conditions needed to prove quadrilateral classifications.
        </p>
      </div>

      <h3 class="subheading"><i class="fa-solid fa-table"></i> 3.1 The Master Quadrilateral Comparison Matrix</h3>
      <p>
        Use this exhaustive 12-property matrix to instantly compare and contrast any two quadrilaterals for your exams:
      </p>

      <div class="table-container">
        <table class="data-table">
          <thead>
            <tr>
              <th>Property</th>
              <th>General Quad</th>
              <th>Trapezium</th>
              <th>Isosceles Trapezium</th>
              <th>Kite</th>
              <th>Parallelogram</th>
              <th>Rhombus</th>
              <th>Rectangle</th>
              <th>Square</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>Opposite Sides Parallel</strong></td>
              <td>None</td>
              <td>At least 1 pair</td>
              <td>1 pair only</td>
              <td>None</td>
              <td>Both pairs (2)</td>
              <td>Both pairs (2)</td>
              <td>Both pairs (2)</td>
              <td>Both pairs (2)</td>
            </tr>
            <tr>
              <td><strong>Opposite Sides Equal</strong></td>
              <td>No</td>
              <td>No</td>
              <td>No (legs equal)</td>
              <td>No</td>
              <td>Yes</td>
              <td>Yes (all 4 equal)</td>
              <td>Yes</td>
              <td>Yes (all 4 equal)</td>
            </tr>
            <tr>
              <td><strong>All Four Sides Equal</strong></td>
              <td>No</td>
              <td>No</td>
              <td>No</td>
              <td>No</td>
              <td>No</td>
              <td>Yes</td>
              <td>No</td>
              <td>Yes</td>
            </tr>
            <tr>
              <td><strong>Opposite Angles Equal</strong></td>
              <td>No</td>
              <td>No</td>
              <td>No</td>
              <td>1 pair only</td>
              <td>Yes</td>
              <td>Yes</td>
              <td>Yes (all 90°)</td>
              <td>Yes (all 90°)</td>
            </tr>
            <tr>
              <td><strong>Consecutive Angles Supplementary</strong></td>
              <td>No</td>
              <td>Along legs only</td>
              <td>Along legs only</td>
              <td>No</td>
              <td>Yes (all pairs)</td>
              <td>Yes (all pairs)</td>
              <td>Yes (all 90°+90°)</td>
              <td>Yes (all 90°+90°)</td>
            </tr>
            <tr>
              <td><strong>All Four Angles 90°</strong></td>
              <td>No</td>
              <td>No</td>
              <td>No</td>
              <td>No</td>
              <td>No</td>
              <td>No</td>
              <td>Yes</td>
              <td>Yes</td>
            </tr>
            <tr>
              <td><strong>Diagonals Equal in Length</strong></td>
              <td>No</td>
              <td>No</td>
              <td>Yes</td>
              <td>No</td>
              <td>No</td>
              <td>No</td>
              <td>Yes</td>
              <td>Yes</td>
            </tr>
            <tr>
              <td><strong>Diagonals Bisect Each Other</strong></td>
              <td>No</td>
              <td>No</td>
              <td>No</td>
              <td>No (only 1 bisected)</td>
              <td>Yes</td>
              <td>Yes</td>
              <td>Yes</td>
              <td>Yes</td>
            </tr>
            <tr>
              <td><strong>Diagonals Perpendicular (90°)</strong></td>
              <td>No</td>
              <td>No</td>
              <td>No</td>
              <td>Yes</td>
              <td>No</td>
              <td>Yes</td>
              <td>No</td>
              <td>Yes</td>
            </tr>
            <tr>
              <td><strong>Diagonals Bisect Vertex Angles</strong></td>
              <td>No</td>
              <td>No</td>
              <td>No</td>
              <td>Only symmetry diagonal</td>
              <td>No</td>
              <td>Yes</td>
              <td>No</td>
              <td>Yes (into 45°-45°)</td>
            </tr>
            <tr>
              <td><strong>Lines of Reflection Symmetry</strong></td>
              <td>0</td>
              <td>0</td>
              <td>1 (vertical bisector)</td>
              <td>1 (main diagonal)</td>
              <td>0</td>
              <td>2 (diagonals)</td>
              <td>2 (midpoint lines)</td>
              <td>4 (2 diag + 2 mid)</td>
            </tr>
            <tr>
              <td><strong>Order of Rotational Symmetry</strong></td>
              <td>1</td>
              <td>1</td>
              <td>1</td>
              <td>1</td>
              <td>2 (at 180°)</td>
              <td>2 (at 180°)</td>
              <td>2 (at 180°)</td>
              <td>4 (at 90°, 180°, 270°)</td>
            </tr>
          </tbody>
        </table>
      </div>

      <h3 class="subheading"><i class="fa-solid fa-calculator"></i> 3.2 Perimeter, Area &amp; Diagonal Metric Bank</h3>
      <p>
        The table below provides all primary computational formulas required for standard Class 8 numerical problems:
      </p>

      <div class="table-container">
        <table class="data-table">
          <thead>
            <tr>
              <th>Figure Name</th>
              <th>Perimeter Formula</th>
              <th>Area Formula</th>
              <th>Diagonal Relations</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>General Quadrilateral</strong></td>
              <td>P = a + b + c + d</td>
              <td>Area = ½ × d × (h₁ + h₂)</td>
              <td>d is diagonal length; h₁, h₂ are perpendicular offsets from opposite vertices.</td>
            </tr>
            <tr>
              <td><strong>Rectangle</strong></td>
              <td>P = 2(l + b)</td>
              <td>Area = l × b</td>
              <td>d = √(l² + b²) (Pythagorean Theorem)</td>
            </tr>
            <tr>
              <td><strong>Square</strong></td>
              <td>P = 4a</td>
              <td>Area = a² = ½ × d²</td>
              <td>d = a√2  ⇒  a = d / √2</td>
            </tr>
            <tr>
              <td><strong>Parallelogram</strong></td>
              <td>P = 2(a + b)</td>
              <td>Area = Base × Height = b × h</td>
              <td>d₁² + d₂² = 2(a² + b²) (Parallelogram Law of Diagonals)</td>
            </tr>
            <tr>
              <td><strong>Rhombus</strong></td>
              <td>P = 4a</td>
              <td>Area = ½ × d₁ × d₂ = b × h</td>
              <td>d₁ ⊥ d₂ and a² = (d₁/2)² + (d₂/2)²  ⇒  4a² = d₁² + d₂²</td>
            </tr>
            <tr>
              <td><strong>Trapezium</strong></td>
              <td>P = a + b + c + d</td>
              <td>Area = ½ × (Sum of Parallel Bases) × h = ½(a + b)h</td>
              <td>In Isosceles Trapezium: d₁ = d₂</td>
            </tr>
            <tr>
              <td><strong>Kite</strong></td>
              <td>P = 2(a + b)</td>
              <td>Area = ½ × d₁ × d₂</td>
              <td>d₁ ⊥ d₂ with one diagonal bisecting the other.</td>
            </tr>
          </tbody>
        </table>
      </div>

      <h3 class="subheading"><i class="fa-solid fa-key"></i> 3.3 Minimal Sufficient Conditions for Identification</h3>
      <p>
        In geometric reasoning questions and exams, you do not need to prove all 10 properties to establish a quadrilateral's type. Proving any <strong>ONE</strong> of the following minimal sufficient conditions is legally and geometrically complete:
      </p>

      <div class="table-container">
        <table class="data-table">
          <thead>
            <tr>
              <th>Target Shape</th>
              <th>Starting Base Shape</th>
              <th>Minimal Sufficient Condition to Prove</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>Parallelogram</strong></td>
              <td>Any Quadrilateral</td>
              <td>
                • Both pairs of opposite sides are parallel, OR<br>
                • Both pairs of opposite sides are equal, OR<br>
                • Both pairs of opposite angles are equal, OR<br>
                • <strong>ONE pair of opposite sides is BOTH equal AND parallel</strong>, OR<br>
                • The diagonals bisect each other.
              </td>
            </tr>
            <tr>
              <td><strong>Rectangle</strong></td>
              <td>Parallelogram</td>
              <td>
                • At least ONE angle is 90° (all 4 then become 90° automatically), OR<br>
                • The diagonals are equal in length (AC = BD).
              </td>
            </tr>
            <tr>
              <td><strong>Rhombus</strong></td>
              <td>Parallelogram</td>
              <td>
                • Adjacent sides are equal (a = b), OR<br>
                • The diagonals are perpendicular to each other (d₁ ⊥ d₂), OR<br>
                • At least one diagonal bisects the vertex angles.
              </td>
            </tr>
            <tr>
              <td><strong>Square</strong></td>
              <td>Parallelogram</td>
              <td>
                • One angle is 90° AND adjacent sides are equal, OR<br>
                • Diagonals are equal AND intersect at 90°.
              </td>
            </tr>
            <tr>
              <td><strong>Square</strong></td>
              <td>Rectangle</td>
              <td>
                • Adjacent sides are equal, OR<br>
                • Diagonals intersect at 90°.
              </td>
            </tr>
            <tr>
              <td><strong>Square</strong></td>
              <td>Rhombus</td>
              <td>
                • At least one angle is 90°, OR<br>
                • Diagonals are equal in length.
              </td>
            </tr>
            <tr>
              <td><strong>Isosceles Trapezium</strong></td>
              <td>Trapezium</td>
              <td>
                • The non-parallel sides (legs) are equal, OR<br>
                • The base angles are equal, OR<br>
                • The diagonals are equal in length.
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </section>
"""
