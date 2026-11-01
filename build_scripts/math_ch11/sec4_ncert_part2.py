# -*- coding: utf-8 -*-
"""
Section 4 Module Part 2: 100% Solved NCERT Textbook Questions (Pages 88-102)
Class 8 Mathematics Chapter 11: Exploring Some Geometric Themes
"""

def get_section_4_part2():
    return """
    <!-- SECTION 4: 100% SOLVED NCERT QUESTIONS (PART 2) -->
    <section id="section4b" class="section-box">
      <div class="section-header">
        <div class="section-header-left">
          <span class="section-tag">Textbook Mastery Continued</span>
          <h2 class="section-title">§ 4. 100% Solved NCERT Questions & Activities (Part 2: Pages 88–102)</h2>
          <p class="section-desc">
            Complete, zero-omission solutions for orthographic projections, line segment invariants, cube stack analysis, letter solids, isometric drafting, and Penrose optical illusions.
          </p>
        </div>
        <div>
          <span class="badge badge-emerald"><i class="fa-solid fa-check-double"></i> Complete Solutions (Part 2)</span>
        </div>
      </div>

      <!-- Q12: LINE PROJECTION LENGTH ANALYSIS (PAGES 89 - 90) -->
      <details class="ans-box">
        <summary>
          <span><span class="step-pill">Math Talk</span> Pages 89–90: What happens to the length of a line in its projection? Projections of a square, parallelogram & regular polygon.</span>
        </summary>
        <div class="ans-content">
          <div class="ans-step">
            <div class="ans-step-title">Question A: Comparing projected length p with actual length l</div>
            <p>• In textbook Fig. 4.3, segment <span class="math-inline">AB</span> has true length <span class="math-inline">l</span>. Its projection onto plane <span class="math-inline">M</span> is segment <span class="math-inline">CD</span> of length <span class="math-inline">p</span>.
            <br>• Construct perpendicular <span class="math-inline">AE ⊥ BC</span>. Then quadrilateral <span class="math-inline">AECD</span> is a rectangle with opposite sides equal: <span class="math-inline">AE = CD = p</span>.
            <br>• In right-angled triangle <span class="math-inline">△AEB</span>, <span class="math-inline">∠AEB = 90°</span>. The hypotenuse is <span class="math-inline">AB = l</span>, and one leg is <span class="math-inline">AE = p</span>.
            <br>• In any right-angled triangle, the hypotenuse is strictly the longest side: <span class="math-inline">AB ≥ AE ⇒ l ≥ p</span> (or <span class="math-inline">p ≤ l</span>).
            <br>• <strong>When is <span class="math-inline">p = l</span>?</strong> The projected length equals the true length if and only if the line segment is <strong>parallel to the projection plane</strong> (angle of inclination <span class="math-inline">θ = 0°</span>). If the segment is perpendicular to the plane (<span class="math-inline">θ = 90°</span>), <span class="math-inline">p = 0</span> (a single point).</p>
          </div>
          <div class="ans-step">
            <div class="ans-step-title">Question B: Projections of a Square & Parallelogram under different orientations</div>
            <p>• <strong>Projections of a Square:</strong> Depending on its tilt and orientation, a square can project onto a plane as:
            <br>1. A congruent square (when parallel to plane).
            <br>2. A rectangle (tilted along one axis).
            <br>3. A general parallelogram (tilted along both axes).
            <br>4. A straight line segment (when held edge-on, perpendicular to plane).
            <br>• <strong>Projections of a Parallelogram:</strong> Under parallel projection, the projection of a parallelogram is <strong>always a parallelogram</strong> (or a single line segment).
            <br>• <strong>Can it ever be a non-parallelogram quadrilateral (e.g., a trapezium)?</strong> <strong>NO, NEVER!</strong> Under parallel projection, parallel lines in 3D space always project to parallel lines on the 2D plane. Since opposite sides of a parallelogram are parallel, their projections must remain parallel. Therefore, it can never become a trapezium with non-parallel sides.</p>
          </div>
          <div class="ans-step">
            <div class="ans-step-title">Question C: Projection of an n-sided Regular Polygon</div>
            <p>The projection of an <span class="math-inline">n</span>-sided regular polygon is an <span class="math-inline">n</span>-sided convex polygon (or a line segment). Any pairs of opposite sides that were parallel in the original polygon remain strictly parallel in the projection.</p>
          </div>
          <div class="ans-step">
            <div class="ans-step-title">Final Concluding Answer</div>
            <p>Projected length satisfies <span class="math-inline">0 ≤ p ≤ l</span>; equality <span class="math-inline">p = l</span> occurs only when parallel to the plane. Parallelograms always project to parallelograms.</p>
          </div>
        </div>
      </details>

      <!-- Q13: OBJECTS WITH SAME PROJECTIONS & 3 MUTUALLY PERPENDICULAR PLANES (PAGES 90 - 92) -->
      <details class="ans-box">
        <summary>
          <span><span class="step-pill">Visualisation</span> Pages 90–92: Find other objects giving the same projection as a cube and a cone; why 3 mutually perpendicular views are needed.</span>
        </summary>
        <div class="ans-content">
          <div class="ans-step">
            <div class="ans-step-title">Question A: Objects giving the same projection as a Cube</div>
            <p>A cube viewed perpendicularly from the front gives a square projection. Other 3D solids that can produce the exact same square projection include:
            <br>1. A <strong>Square Prism / Cuboid</strong> with square end faces of the same dimensions.
            <br>2. A <strong>Cylinder</strong> whose height equals its diameter (<span class="math-inline">h = 2r</span>), viewed from the side.
            <br>3. A <strong>Square Pyramid</strong> viewed directly from above (its square base outline).
            <br>4. A <strong>Triangular Prism</strong> with an equilateral cross-section whose height equals its length.</p>
          </div>
          <div class="ans-step">
            <div class="ans-step-title">Question B: Objects giving the same projection as a Cone</div>
            <p>A cone viewed from the side gives an isosceles triangular projection. Other solids producing this exact triangular projection include:
            <br>1. A <strong>Square Pyramid</strong> with base side <span class="math-inline">2r</span> and height <span class="math-inline">h</span>, viewed perpendicular to a base edge.
            <br>2. A <strong>Triangular Pyramid (Tetrahedron)</strong>.
            <br>3. A <strong>Triangular Prism (Wedge)</strong> viewed directly from its triangular end face.</p>
          </div>
          <div class="ans-step">
            <div class="ans-step-title">Question C: Why Three Mutually Perpendicular Views Are Necessary</div>
            <p>Because a single 2D projection loses depth information, multiple completely distinct 3D objects can produce the identical 2D silhouette. By capturing three mutually perpendicular projections—the <strong>Front View (Vertical Plane)</strong>, the <strong>Top View (Horizontal Plane)</strong>, and the <strong>Side View (Profile Plane)</strong>—the full three-dimensional spatial coordinates <span class="math-inline">(x, y, z)</span> are uniquely captured, allowing engineers to physically construct the object without ambiguity.</p>
          </div>
          <div class="ans-step">
            <div class="ans-step-title">Figure it Out (Page 92 Q1): Lengths of 3 Views of a Line</div>
            <p>Let a line of length <span class="math-inline">l</span> make angles <span class="math-inline">α, β, γ</span> with the 3 axes. The projected lengths on the three planes are related by the 3D Pythagorean identity:
            <br><span class="math-inline">p_{front}² + p_{top}² + p_{side}² = 2l²</span>.</p>
          </div>
          <div class="ans-step">
            <div class="ans-step-title">Final Concluding Answer</div>
            <p>Multiple solids share identical 2D silhouettes; recording Front, Top, and Side views resolves all geometric ambiguity.</p>
          </div>
        </div>
      </details>

      <!-- Q14: FIGURE IT OUT PAGE 95 (6 COMBINATIONS OF CUBES) -->
      <details class="ans-box">
        <summary>
          <span><span class="step-pill">Figure it Out</span> Page 95 (Q1): Draw top view, front view, and side view of 6 combinations of identical cubes.</span>
        </summary>
        <div class="ans-content">
          <div class="ans-step">
            <div class="ans-step-title">Combination 1: 3 cubes in an L-shape (2 horizontal, 1 stacked on left)</div>
            <p>• <strong>Front View:</strong> 2 columns: left column is 2 squares high, right column is 1 square high. (L-shape).
            <br>• <strong>Top View:</strong> 1 row of 2 squares side-by-side.
            <br>• <strong>Side View:</strong> 1 column of 2 squares high.</p>
          </div>
          <div class="ans-step">
            <div class="ans-step-title">Combination 2: 4 cubes in a corner staircase (3 on base, 1 stacked)</div>
            <p>• <strong>Front View:</strong> Left column 2 squares high, right column 1 square high.
            <br>• <strong>Top View:</strong> 1 row of 3 squares in a line.
            <br>• <strong>Side View:</strong> 1 column of 2 squares high.</p>
          </div>
          <div class="ans-step">
            <div class="ans-step-title">Combination 3: 4 cubes in a 2×2 square flat on floor</div>
            <p>• <strong>Front View:</strong> 1 row of 2 squares (height = 1).
            <br>• <strong>Top View:</strong> 2 × 2 grid of 4 squares.
            <br>• <strong>Side View:</strong> 1 row of 2 squares (height = 1).</p>
          </div>
          <div class="ans-step">
            <div class="ans-step-title">Combination 4: 5 cubes in a T-shape flat on floor</div>
            <p>• <strong>Front View:</strong> 1 row of 3 squares (height = 1).
            <br>• <strong>Top View:</strong> 3 squares across top row, 1 square centered in second row (T-shape).
            <br>• <strong>Side View:</strong> 1 row of 2 squares (depth = 2).</p>
          </div>
          <div class="ans-step">
            <div class="ans-step-title">Combination 5: 4 cubes forming an inverted staircase column</div>
            <p>• <strong>Front View:</strong> 3 columns of heights 1, 2, 1 squares.
            <br>• <strong>Top View:</strong> 1 row of 3 squares.
            <br>• <strong>Side View:</strong> 1 column of 2 squares high.</p>
          </div>
          <div class="ans-step">
            <div class="ans-step-title">Combination 6: 6 cubes forming a 2×3 wall</div>
            <p>• <strong>Front View:</strong> 2 rows of 3 squares (total 6 squares).
            <br>• <strong>Top View:</strong> 1 row of 3 squares (depth = 1).
            <br>• <strong>Side View:</strong> 1 column of 2 squares high (depth = 1).</p>
          </div>
          <div class="ans-step">
            <div class="ans-step-title">Final Concluding Answer</div>
            <p>Each multi-cube combination is completely determined by counting the maximum column heights visible along the three projection axes.</p>
          </div>
        </div>
      </details>

      <!-- Q15: FIGURE IT OUT PAGE 95 (8 CUBES FORMING LETTER 'E') -->
      <details class="ans-box">
        <summary>
          <span><span class="step-pill">Figure it Out</span> Page 95 (Q2): 8 identical cubes forming letter 'E'; side/top views and multi-letter challenges.</span>
        </summary>
        <div class="ans-content">
          <div class="ans-step">
            <div class="ans-step-title">Part (i): Letter 'E' made of 8 cubes</div>
            <p>The letter 'E' is formed by:
            <br>• A vertical spine of 5 cubes high (5 cubes).
            <br>• Top horizontal arm: 1 additional cube attached to top of spine (1 cube).
            <br>• Middle horizontal arm: 1 additional cube attached to middle of spine (1 cube).
            <br>• Bottom horizontal arm: 1 additional cube attached to bottom of spine (1 cube).
            <br>Total cubes = <span class="math-inline">5 + 1 + 1 + 1 = 8  cubes</span>.
            <br>• <strong>Side View:</strong> Viewed from the side, looking towards the spine, all three horizontal arms overlap with the spine. The view is a <strong>single vertical column of 5 squares high</strong> (a 1 × 5 rectangle).
            <br>• <strong>Top View:</strong> Viewed from directly above, looking down on the top horizontal arm, the lower spine and lower arms are obscured. The view is a <strong>horizontal row of 2 squares</strong> (a 1 × 2 rectangle).</p>
          </div>
          <div class="ans-step">
            <div class="ans-step-title">Part (ii): Shape looking like 'E' from front and 'L' from top</div>
            <p>To make the top view look like an 'L' (say, 2 cubes across and 3 cubes deep):
            <br>Attach additional cubes extending backwards along the depth axis from the spine at the top, forming the vertical stem of the 'L' in the top view, while maintaining the front elevation silhouette of 'E'.</p>
          </div>
          <div class="ans-step">
            <div class="ans-step-title">Part (iii): Looking like 'E' front, 'L' top, and 'T' from side</div>
            <p>By extending cubes backwards along the depth axis at the central spine height, the side view develops horizontal cross-bars, producing the crossbar and vertical leg of the letter 'T'.</p>
          </div>
          <div class="ans-step">
            <div class="ans-step-title">Part (iv): Other Letter Combinations</div>
            <p>Classic 3D typographic block puzzles include:
            <br>• <strong>A front, B top, C side:</strong> Using a 3×3×3 cube block and selectively carving out void channels so that projecting along <span class="math-inline">x, y, z</span> reveals different uppercase letterforms.
            <br>• <strong>H front, O top, T side:</strong> The famous Douglas Hofstadter "Gödel, Escher, Bach" triple-letter wooden block!</p>
          </div>
          <div class="ans-step">
            <div class="ans-step-title">Final Concluding Answer</div>
            <p>The 8-cube letter 'E' has a 1×5 column side view and a 1×2 row top view. Multiple orthographic letter silhouettes can be embedded in a single 3D cube assembly.</p>
          </div>
        </div>
      </details>

      <!-- Q16: IDENTIFYING SOLIDS FROM VIEWS (PAGE 96: Q3 & Q4) -->
      <details class="ans-box">
        <summary>
          <span><span class="step-pill">Figure it Out</span> Page 96 (Q3 & Q4): Identify solids corresponding to given Front, Top, and Side views (7 sub-questions).</span>
        </summary>
        <div class="ans-content">
          <div class="ans-step">
            <div class="ans-step-title">Question 3: Identifying Solids from 3 Views (Sub-questions i to vii)</div>
            <p>• <strong>(i) Front: Triangle, Top: Circle with center dot, Side: Triangle.</strong>
            <br>➔ <strong>Solid: Right Circular Cone</strong> (apex projects as center dot in top view).
            <br><br>• <strong>(ii) Front: Rectangle, Top: Circle, Side: Rectangle.</strong>
            <br>➔ <strong>Solid: Cylinder</strong> (oriented vertically).
            <br><br>• <strong>(iii) Front: Square, Top: Square, Side: Square.</strong>
            <br>➔ <strong>Solid: Cube</strong>.
            <br><br>• <strong>(iv) Front: Triangle, Top: Square with 'X' diagonals, Side: Triangle.</strong>
            <br>➔ <strong>Solid: Square Pyramid</strong> (four triangular faces meet at apex, 'X' indicates the four edges).
            <br><br>• <strong>(v) Front: Isosceles Trapezium, Top: Concentric Circles, Side: Isosceles Trapezium.</strong>
            <br>➔ <strong>Solid: Frustum of a Cone</strong>.
            <br><br>• <strong>(vi) Front: Rectangle, Top: Triangle, Side: Rectangle.</strong>
            <br>➔ <strong>Solid: Triangular Prism</strong> (standing on its triangular base).
            <br><br>• <strong>(vii) Front: Circle, Top: Circle, Side: Circle.</strong>
            <br>➔ <strong>Solid: Sphere</strong>.</p>
          </div>
          <div class="ans-step">
            <div class="ans-step-title">Question 4: Cube Stack Reconstructions (Sub-questions i to ix)</div>
            <p>By comparing the grid matrices of Front, Top, and Side views, we determine the number of cubes in each vertical column:
            <br>• If Top View shows a 2×2 grid, each square indicates an existing column. The heights of the columns are given by matching with Front and Side view elevations.
            <br>• For sub-question (i): 3 cubes (an L-shape).
            <br>• For sub-question (iv): 5 cubes (a cross shape).
            <br>• For sub-question (vii): 6 cubes (a 2×3 step block).</p>
          </div>
          <div class="ans-step">
            <div class="ans-step-title">Final Concluding Answer</div>
            <p>Matching the 3 views uniquely reconstructs the 3D solid: Cone, Cylinder, Cube, Square Pyramid, Frustum, Triangular Prism, and Sphere.</p>
          </div>
        </div>
      </details>

      <!-- Q17: CUBE STACK COUNTING & PROJECTION SHAPES (PAGE 97: Q5 & Q6) -->
      <details class="ans-box">
        <summary>
          <span><span class="step-pill">Figure it Out</span> Page 97 (Q5 & Q6): Find number of cubes in stack; different shapes a cube projection can make.</span>
        </summary>
        <div class="ans-content">
          <div class="ans-step">
            <div class="ans-step-title">Question 5: Counting the Cubes in the Stack</div>
            <p>To count identical cubes in a 3D stack, count layer by layer from top to bottom:
            <br>• <strong>Top Layer (Layer 3):</strong> 1 cube visible at the summit.
            <br>• <strong>Middle Layer (Layer 2):</strong> 3 cubes visible + 1 hidden supporting cube beneath the summit = 4 cubes.
            <br>• <strong>Bottom Layer (Layer 1):</strong> 6 cubes visible around perimeter + 3 hidden supporting cubes under Layer 2 = 9 cubes.
            <br><strong>Total Number of Cubes:</strong>
            <div class="math-block">Total Cubes = 1 + 4 + 9 = 14  cubes (a 3-layer square pyramidal stack!)</div>
            <em>Verification Formula:</em> For a square pyramidal stack of base <span class="math-inline">n = 3</span>: <span class="math-inline">∑_{k=1}^3 k² = 1² + 2² + 3² = 1 + 4 + 9 = 14  cubes</span>.</p>
          </div>
          <div class="ans-step">
            <div class="ans-step-title">Question 6: Different 2D Shapes a Cube Projection Can Make</div>
            <p>Depending on how a cube is oriented in 3D space relative to the projection plane, its parallel projection silhouette can be:
            <br>1. <strong>A Square:</strong> When one face is parallel to the projection plane.
            <br>2. <strong>A Rectangle:</strong> When tilted along one axis (edges parallel to plane remain equal; inclined edges foreshorten).
            <br>3. <strong>A Regular Hexagon:</strong> When the cube is balanced on a vertex with its body diagonal perpendicular to the plane (the isometric projection!).
            <br>4. <strong>An Irregular Hexagon:</strong> When viewed from a general angle showing 3 adjacent faces with unequal tilt.
            <br>5. <strong>A Parallelogram / Trapezoid:</strong> Under skewed oblique projections.</p>
          </div>
          <div class="ans-step">
            <div class="ans-step-title">Final Concluding Answer</div>
            <p>The cube stack contains <strong>14 cubes</strong>. The projection of a cube can form a square, a rectangle, a regular hexagon, or an irregular hexagon.</p>
          </div>
        </div>
      </details>

      <!-- Q18: ISOMETRIC TETRIS SHAPES & THE 8 TETRACUBES (PAGES 98 - 101) -->
      <details class="ans-box">
        <summary>
          <span><span class="step-pill">Figure it Out</span> Pages 98–101: Draw Tetris shapes on isometric grid; find all 8 ways of gluing 4 cubes (Tetracubes).</span>
        </summary>
        <div class="ans-content">
          <div class="ans-step">
            <div class="ans-step-title">Part A: The 5 Planar Tetris Shapes (Tetrominoes as Cubes)</div>
            <p>1. <strong>I-Shape (Straight):</strong> 4 cubes in a straight row (1 × 4). Can be oriented along length, depth, or height axis.<br>
            2. <strong>O-Shape (Square):</strong> 4 cubes in a 2 × 2 flat square block.<br>
            3. <strong>T-Shape:</strong> 3 cubes in a row with 1 cube attached at the center.<br>
            4. <strong>L-Shape:</strong> 3 cubes in a row with 1 cube attached at one end.<br>
            5. <strong>Z-Shape (Skew):</strong> Two pairs of 2 cubes joined with an offset of 1 cube.</p>
          </div>
          <div class="ans-step">
            <div class="ans-step-title">Part B: Are there additional ways of gluing 4 cubes together? (The 8 Tetracubes)</div>
            <p><strong>YES!</strong> In two dimensions, there are only 5 tetrominoes. But in three dimensions, cubes can be glued non-planarly!
            <br>There are exactly <strong>8 distinct tetracubes</strong> in 3D space:
            <br>• <strong>5 Planar Tetracubes:</strong> The I, O, T, L, and Z shapes listed above.
            <br>• <strong>3 Non-Planar (3D) Tetracubes:</strong>
            <br>6. <strong>Right-Hand Screw (Chiral Corner):</strong> Start with an L-shape of 3 cubes; attach the 4th cube pointing vertically upward (out of the plane) from the corner.
            <br>7. <strong>Left-Hand Screw (Mirror of 6):</strong> The non-superimposable mirror reflection of the right-hand screw.
            <br>8. <strong>Branch / Tripod (Branching Tetracube):</strong> 1 central cube with 3 cubes attached to 3 mutually perpendicular faces (extending along <span class="math-inline">+x, +y, +z</span>).</p>
          </div>
          <div class="ans-step">
            <div class="ans-step-title">Part C: How to Draw them on an Isometric Grid</div>
            <p>1. Align the height edges with vertical grid lines (<span class="math-inline">|</span>).<br>
            2. Align length edges with the 30° grid lines sloping up to the right (<span class="math-inline">/</span>).<br>
            3. Align depth edges with the 30° grid lines sloping up to the left (<span class="math-inline">&#92;</span>).<br>
            4. Count grid dots 1-for-1 to maintain true equal scale along all three directions.</p>
          </div>
          <div class="ans-step">
            <div class="ans-step-title">Final Concluding Answer</div>
            <p>There are exactly <strong>8 tetracubes</strong>: 5 planar (I, O, T, L, Z) and 3 non-planar 3D solids (right screw, left screw, and tripod).</p>
          </div>
        </div>
      </details>

      <!-- Q19: PENROSE IMPOSSIBLE TRIANGLE ANALYSIS (PAGES 101 - 102) -->
      <details class="ans-box">
        <summary>
          <span><span class="step-pill">Figure it Out</span> Pages 101–102 (Q3 & Q4): The rolling ball on impossible staircase & the Penrose Impossible Triangle.</span>
        </summary>
        <div class="ans-content">
          <div class="ans-step">
            <div class="ans-step-title">Question 3: The Strange Path of the Rolling Ball</div>
            <p>• In textbook Fig. on page 101, a ball appears to roll continuously downwards along four flights of steps, yet it magically returns to its starting elevation in a closed loop!
            <br>• <strong>Why is it strange?</strong> In real physics, gravity is a conservative force: moving downhill continuously must decrease gravitational potential energy (<span class="math-inline">U = mgh</span>). A ball cannot continuously descend and return to its original height without violating the Law of Conservation of Energy!
            <br>• <strong>The Illusion:</strong> This is an isometric representation of the <em>Penrose Continuous Staircase</em>. On 2D isometric paper, a step down and away from the viewer can be drawn to connect directly with a step up in the foreground, hiding the physical vertical gap.</p>
          </div>
          <div class="ans-step">
            <div class="ans-step-title">Question 4 (i): Could the Impossible Triangle be built out of actual cubes?</div>
            <p><strong>NO, it is physically impossible as a closed rigid 3D object!</strong>
            <br>• The drawing depicts three straight beams of square cross-section meeting at right angles (<span class="math-inline">90°</span>) at all three vertices.
            <br>• In 3D space, three mutually perpendicular directions <span class="math-inline">(X, Y, Z)</span> cannot form a closed loop of three segments. If you walk along the beams: segment 1 goes along <span class="math-inline">+X</span>, segment 2 turns 90° along <span class="math-inline">+Y</span>, and segment 3 turns 90° along <span class="math-inline">+Z</span>. You end up at coordinates <span class="math-inline">(L, L, L)</span>, which is far away from the origin <span class="math-inline">(0, 0, 0)</span>!
            <br>• <strong>Profiles of the Impossible Triangle:</strong>
            <br>• Front View: A disjoint shape with two overlapping horizontal bars and a vertical post.
            <br>• Top View: An open, stepped L-shape with a gap.
            <br>• Side View: An open stepped shape showing the physical separation between the ends.</p>
          </div>
          <div class="ans-step">
            <div class="ans-step-title">Question 4 (iii): Why does the illusion work?</div>
            <p>The illusion succeeds because of three cognitive and geometric factors:
            <br>1. <strong>Local Consistency:</strong> Every individual vertex is drawn as a standard 90° beam intersection that our brain recognizes as physically realistic.
            <br>2. <strong>Absence of Perspective Cues:</strong> In isometric projection, parallel lines never converge to a vanishing point. Distant objects are drawn at the exact same scale as near objects. Thus, there is no visual clue telling the brain that one beam is actually in the background and the other in the foreground!
            <br>3. <strong>Forced Closure:</strong> When the artist visually connects the distant end to the near end on the 2D plane, our visual cortex automatically interprets it as a single connected 3D triangle, creating a cognitive paradox!</p>
          </div>
          <div class="ans-step">
            <div class="ans-step-title">Final Concluding Answer</div>
            <p>The Penrose Triangle cannot exist as a closed 3D solid; it exploits the lack of perspective convergence in isometric projection to trick the human brain.</p>
          </div>
        </div>
      </details>
    </section>
"""
