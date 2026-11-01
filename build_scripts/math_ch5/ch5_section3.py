# -*- coding: utf-8 -*-
"""Part 5: Section 3 - Rapid Revision Fact & Formula/Law Bank."""

SECTION3_CONTENT = """
    <!-- SECTION 3: RAPID REVISION FACT & FORMULA/LAW BANK -->
    <section id="factbank" class="section-card">
      <div class="section-header">
        <div class="section-icon-box">
          <i class="fa-solid fa-table"></i>
        </div>
        <div>
          <h2 class="section-title">Section 3: Rapid Revision Fact &amp; Formula/Law Bank</h2>
          <p class="section-tagline">Comprehensive quick-reference tables summarizing angle pairs, transversal theorems, parallelism tests, and folding formulas</p>
        </div>
      </div>

      <!-- TABLE 1: ANGLE RELATIONSHIPS FORMED BY INTERSECTING LINES -->
      <h3 class="subheading"><i class="fa-solid fa-circle-nodes"></i> Table 1: Angle Relationships Formed by Intersecting Lines</h3>
      <div class="table-responsive">
        <table>
          <thead>
            <tr>
              <th style="width: 20%;">Angle Relationship</th>
              <th style="width: 25%;">Geometric Position / Definition</th>
              <th style="width: 25%;">Mathematical Property / Formula</th>
              <th style="width: 30%;">Exam Hall Identification Tip</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>Adjacent Angles</strong></td>
              <td>Share a common vertex and a common arm, with non-overlapping interiors.</td>
              <td><span class="math-inline">∠AOB + ∠BOC = ∠AOC</span></td>
              <td>Look for two angles sharing a single ray like opening two pages of a book.</td>
            </tr>
            <tr>
              <td><strong>Linear Pair</strong></td>
              <td>Adjacent angles whose non-common arms form a single straight line.</td>
              <td><span class="math-inline">∠1 + ∠2 = 180°</span> (Supplementary)</td>
              <td>Forms a straight protractor baseline. If one angle is x, the other is 180° - x.</td>
            </tr>
            <tr>
              <td><strong>Vertically Opposite Angles</strong></td>
              <td>Opposite non-adjacent angles formed by two straight lines crossing.</td>
              <td><span class="math-inline">∠a = ∠c</span> &nbsp;and&nbsp; <span class="math-inline">∠b = ∠d</span> (Equal)</td>
              <td>Forms an "X" shape. Always equal, whether the lines are perpendicular or tilted.</td>
            </tr>
            <tr>
              <td><strong>Perpendicular Intersections</strong></td>
              <td>Two lines intersect such that all four angles are completely equal.</td>
              <td><span class="math-inline">∠1 = ∠2 = ∠3 = ∠4 = 90°</span> (<span class="math-inline">l ⊥ m</span>)</td>
              <td>Look for a small square box symbol (⊾) at the vertex of intersection.</td>
            </tr>
          </tbody>
        </table>
      </div>

      <!-- TABLE 2: 8-ANGLE TRANSVERSAL TAXONOMY & POSITION MATRIX -->
      <h3 class="subheading"><i class="fa-solid fa-list-check"></i> Table 2: Complete 8-Angle Transversal Taxonomy &amp; Position Matrix</h3>
      <p>
        Refer to Figure 2.3 where transversal <span class="math-inline">t</span> cuts parallel lines <span class="math-inline">l ∥ m</span>, creating angles 1 to 4 at the top vertex and angles 5 to 8 at the bottom vertex:
      </p>
      <div class="table-responsive">
        <table>
          <thead>
            <tr>
              <th style="width: 22%;">Classification Category</th>
              <th style="width: 28%;">Angle Pairs Involved</th>
              <th style="width: 25%;">Relationship (When l ∥ m)</th>
              <th style="width: 25%;">Visual Mental Model</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>Corresponding Angles</strong></td>
              <td>(∠1, ∠5), &nbsp;(∠2, ∠6),<br>(∠3, ∠7), &nbsp;(∠4, ∠8)</td>
              <td><strong>EQUAL</strong><br><span class="math-inline">∠1 = ∠5, &nbsp;∠2 = ∠6, &nbsp;∠3 = ∠7, &nbsp;∠4 = ∠8</span></td>
              <td><strong>"F-Shape"</strong><br>Same corner position (top-left to top-left, etc.)</td>
            </tr>
            <tr>
              <td><strong>Alternate Interior Angles</strong></td>
              <td>(∠3, ∠5) &nbsp;and&nbsp; (∠4, ∠6)</td>
              <td><strong>EQUAL</strong><br><span class="math-inline">∠3 = ∠5, &nbsp;∠4 = ∠6</span></td>
              <td><strong>"Z-Shape"</strong><br>Inside the parallel tracks, on opposite sides of transversal</td>
            </tr>
            <tr>
              <td><strong>Alternate Exterior Angles</strong></td>
              <td>(∠1, ∠7) &nbsp;and&nbsp; (∠2, ∠8)</td>
              <td><strong>EQUAL</strong><br><span class="math-inline">∠1 = ∠7, &nbsp;∠2 = ∠8</span></td>
              <td>Outside the parallel tracks, on opposite sides of transversal</td>
            </tr>
            <tr>
              <td><strong>Consecutive Interior Angles</strong><br>(Co-interior / Allied)</td>
              <td>(∠3, ∠6) &nbsp;and&nbsp; (∠4, ∠5)</td>
              <td><strong>SUPPLEMENTARY</strong><br><span class="math-inline">∠3 + ∠6 = 180°</span><br><span class="math-inline">∠4 + ∠5 = 180°</span></td>
              <td><strong>"C-Shape" or "U-Shape"</strong><br>Inside the parallel tracks, on the SAME side of transversal</td>
            </tr>
            <tr>
              <td><strong>Consecutive Exterior Angles</strong><br>(Co-exterior)</td>
              <td>(∠2, ∠7) &nbsp;and&nbsp; (∠1, ∠8)</td>
              <td><strong>SUPPLEMENTARY</strong><br><span class="math-inline">∠2 + ∠7 = 180°</span><br><span class="math-inline">∠1 + ∠8 = 180°</span></td>
              <td>Outside the parallel tracks, on the SAME side of transversal</td>
            </tr>
          </tbody>
        </table>
      </div>

      <!-- TABLE 3: THE THREE TESTS OF PARALLELISM -->
      <h3 class="subheading"><i class="fa-solid fa-spell-check"></i> Table 3: The Three Definitive Tests of Parallelism</h3>
      <p>
        To prove that two lines are parallel in an exam, you only need to prove <strong>any ONE</strong> of the following three conditions:
      </p>
      <div class="table-responsive">
        <table>
          <thead>
            <tr>
              <th style="width: 15%;">Test Name</th>
              <th style="width: 35%;">Condition to Check</th>
              <th style="width: 25%;">Mathematical Statement</th>
              <th style="width: 25%;">Logical Conclusion</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>Test 1: Corresponding Angles</strong></td>
              <td>Any pair of corresponding angles formed by the transversal are equal in measure.</td>
              <td><span class="math-inline">∠a = ∠b</span> (in corresponding F-positions)</td>
              <td><span class="math-inline">l ∥ m</span> (Lines are parallel)</td>
            </tr>
            <tr>
              <td><strong>Test 2: Alternate Interior Angles</strong></td>
              <td>Any pair of alternate interior angles formed by the transversal are equal in measure.</td>
              <td><span class="math-inline">∠x = ∠y</span> (in alternate Z-positions)</td>
              <td><span class="math-inline">l ∥ m</span> (Lines are parallel)</td>
            </tr>
            <tr>
              <td><strong>Test 3: Consecutive Interior Angles</strong></td>
              <td>The sum of the interior angles on the same side of the transversal equals exactly 180°.</td>
              <td><span class="math-inline">∠p + ∠q = 180°</span> (in co-interior C-positions)</td>
              <td><span class="math-inline">l ∥ m</span> (Lines are parallel)</td>
            </tr>
          </tbody>
        </table>
      </div>

      <!-- TABLE 4: PAPER FOLDING GEOMETRY & FOLD LAWS -->
      <h3 class="subheading"><i class="fa-solid fa-sheet-plastic"></i> Table 4: Paper-Folding Geometry &amp; The 2ⁿ + 1 Law</h3>
      <div class="table-responsive">
        <table>
          <thead>
            <tr>
              <th style="width: 15%;">Number of Folds (n)</th>
              <th style="width: 25%;">Formula Application (<span class="math-inline">2ⁿ + 1</span>)</th>
              <th style="width: 25%;">Total Parallel Lines Count</th>
              <th style="width: 35%;">Breakdown (Boundary Edges + Creases)</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>0 Folds</strong></td>
              <td><span class="math-inline">2⁰ + 1 = 1 + 1</span></td>
              <td><strong>2 Parallel Lines</strong></td>
              <td>2 outer boundary edges (Top &amp; Bottom) + 0 internal creases</td>
            </tr>
            <tr>
              <td><strong>1 Fold</strong></td>
              <td><span class="math-inline">2¹ + 1 = 2 + 1</span></td>
              <td><strong>3 Parallel Lines</strong></td>
              <td>2 outer boundary edges + 1 central crease</td>
            </tr>
            <tr>
              <td><strong>2 Folds</strong></td>
              <td><span class="math-inline">2² + 1 = 4 + 1</span></td>
              <td><strong>5 Parallel Lines</strong></td>
              <td>2 outer boundary edges + 3 internal creases</td>
            </tr>
            <tr>
              <td><strong>3 Folds</strong></td>
              <td><span class="math-inline">2³ + 1 = 8 + 1</span></td>
              <td><strong>9 Parallel Lines</strong></td>
              <td>2 outer boundary edges + 7 internal creases</td>
            </tr>
            <tr>
              <td><strong>4 Folds</strong></td>
              <td><span class="math-inline">2⁴ + 1 = 16 + 1</span></td>
              <td><strong>17 Parallel Lines</strong></td>
              <td>2 outer boundary edges + 15 internal creases</td>
            </tr>
            <tr>
              <td><strong>n Folds</strong></td>
              <td><span class="math-inline">2ⁿ + 1</span></td>
              <td><strong><span class="math-inline">2ⁿ + 1</span> Parallel Lines</strong></td>
              <td>2 boundary edges + <span class="math-inline">(2ⁿ - 1)</span> internal creases</td>
            </tr>
          </tbody>
        </table>
      </div>

      <!-- TABLE 5: REAL-WORLD APPLICATIONS & ENGINEERING MATRIX -->
      <h3 class="subheading"><i class="fa-solid fa-city"></i> Table 5: Real-World Applications &amp; Engineering Matrix</h3>
      <div class="table-responsive">
        <table>
          <thead>
            <tr>
              <th style="width: 25%;">Application Domain</th>
              <th style="width: 35%;">Geometric Role of Parallel / Intersecting Lines</th>
              <th style="width: 40%;">Why Precision Matters</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>Railway Track Engineering</strong></td>
              <td>The two iron rails are maintained strictly parallel (<span class="math-inline">1676  mm</span> broad gauge). Crossover tracks act as transversals.</td>
              <td>Any deviation from parallel causes train wheels to bind, climb the rail, or catastrophically derail.</td>
            </tr>
            <tr>
              <td><strong>Building Architecture &amp; Stairs</strong></td>
              <td>Stair treads must remain strictly parallel to each other and perpendicular to the vertical risers.</td>
              <td>Unequal angles or non-parallel treads cause human missteps and severe falling accidents.</td>
            </tr>
            <tr>
              <td><strong>Solar Panel Farms</strong></td>
              <td>Panels are mounted in parallel rows inclined at the exact same latitude angle facing south.</td>
              <td>Parallel alignment prevents front rows from casting shadows on rear rows, maximizing solar energy yield.</td>
            </tr>
            <tr>
              <td><strong>Textile &amp; Fabric Weaving</strong></td>
              <td>Warp threads (longitudinal) and weft threads (transverse) cross at strict 90° perpendicular angles.</td>
              <td>Non-orthogonal intersections cause warped fabrics, uneven stretching, and seam tearing.</td>
            </tr>
          </tbody>
        </table>
      </div>
    </section>
"""
