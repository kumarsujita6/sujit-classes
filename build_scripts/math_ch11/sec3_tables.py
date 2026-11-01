# -*- coding: utf-8 -*-
"""
Section 3 Module: Rapid Revision Fact & Formula/Law Bank
Class 8 Mathematics Chapter 11: Exploring Some Geometric Themes
"""

def get_section_3():
    return """
    <!-- SECTION 3: FORMULA & LAW BANK -->
    <section id="section3" class="section-box">
      <div class="section-header">
        <div class="section-header-left">
          <span class="section-tag">Quick Revision Engine</span>
          <h2 class="section-title">§ 3. Rapid Revision Fact & Formula/Law Bank</h2>
          <p class="section-desc">
            A high-density reference repository of recursive growth laws, polyhedra structural metrics, Euler's invariant proofs, orthographic silhouette lookups, and surface geodesic formulas.
          </p>
        </div>
        <div>
          <span class="badge badge-gold"><i class="fa-solid fa-bolt"></i> 5 Master Tables</span>
        </div>
      </div>

      <!-- TABLE 3.1: FRACTAL RECURRENCE & ASYMPTOTIC LIMITS -->
      <div class="concept-card">
        <h3 class="concept-card-title"><i class="fa-solid fa-calculator"></i> Table 3.1: Master Fractal Recurrence & Asymptotic Limit Matrix</h3>
        <p>
          Compare the mathematical machinery governing the three classic fractals in Ganita Prakash. Observe how the ratio of sub-parts to scaling factor creates contrasting asymptotic behaviors.
        </p>

        <div class="data-table-wrapper">
          <table class="data-table">
            <thead>
              <tr>
                <th>Fractal Name</th>
                <th>Initiator (Step 0)</th>
                <th>Remaining Pieces (Rₙ)</th>
                <th>Cumulative Holes (Hₙ)</th>
                <th>Area Formula (Aₙ)</th>
                <th>Perimeter Formula (Pₙ)</th>
                <th>Limit as n → ∞</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>Sierpinski Carpet</strong></td>
                <td>Solid Square (side <span class="math-inline">s</span>, area <span class="math-inline">A₀</span>)</td>
                <td><span class="math-inline">Rₙ = 8ⁿ</span></td>
                <td><span class="math-inline">Hₙ = (8ⁿ - 1) / 7</span></td>
                <td><span class="math-inline">Aₙ = (8/9)ⁿ · A₀</span></td>
                <td>Boundary increases infinitely</td>
                <td><strong>Area → 0</strong><br><span style="color: var(--emerald); font-weight: 700;">Zero Area Object!</span></td>
              </tr>
              <tr>
                <td><strong>Sierpinski Gasket</strong></td>
                <td>Equilateral Triangle (side <span class="math-inline">s</span>, area <span class="math-inline">A₀</span>)</td>
                <td><span class="math-inline">Rₙ = 3ⁿ</span></td>
                <td><span class="math-inline">Hₙ = (3ⁿ - 1) / 2</span></td>
                <td><span class="math-inline">Aₙ = (3/4)ⁿ · A₀</span></td>
                <td><span class="math-inline">Pₙ = 3s · (3/2)ⁿ</span></td>
                <td><strong>Area → 0</strong><br><strong>Perimeter → ∞</strong></td>
              </tr>
              <tr>
                <td><strong>Koch Snowflake</strong></td>
                <td>Equilateral Triangle (side <span class="math-inline">s</span>, area <span class="math-inline">A₀</span>)</td>
                <td><span class="math-inline">Nₙ = 3 · 4ⁿ</span> sides<br>(segment <span class="math-inline">s / 3ⁿ</span>)</td>
                <td><span class="math-inline">Bumps = 3 · 4ⁿ⁻¹</span></td>
                <td><span class="math-inline">Aₙ = A₀ [1 + ⅓∑(4/9)ᵏ]</span></td>
                <td><span class="math-inline">Pₙ = 3s · (4/3)ⁿ</span></td>
                <td><strong>Area → 1.6 · A₀ (FINITE)</strong><br><strong>Perimeter → ∞ (INFINITE)</strong></td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>

      <!-- TABLE 3.2: POLYHEDRA & PLATONIC SOLIDS METRIC BANK -->
      <div class="concept-card">
        <h3 class="concept-card-title"><i class="fa-solid fa-shapes"></i> Table 3.2: Polyhedra Structural Metric & Euler's Law Verification</h3>
        <p>
          Euler's Formula states that for every convex polyhedron, <span class="math-inline">F + V - E = 2</span> (Faces + Vertices - Edges = 2). This topological law holds universally across all prisms, pyramids, and Platonic solids.
        </p>

        <div class="data-table-wrapper">
          <table class="data-table">
            <thead>
              <tr>
                <th>Solid Name</th>
                <th>Base / Face Polygons</th>
                <th>Faces (F)</th>
                <th>Vertices (V)</th>
                <th>Edges (E)</th>
                <th>Euler Verification: F + V - E</th>
                <th>Distinct Net Count</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>Triangular Prism</strong></td>
                <td>2 Triangles + 3 Rectangles</td>
                <td>5</td>
                <td>6</td>
                <td>9</td>
                <td>5 + 6 - 9 = <strong>2</strong></td>
                <td>9 nets</td>
              </tr>
              <tr>
                <td><strong>Rectangular Cuboid</strong></td>
                <td>6 Rectangles (pairs congruent)</td>
                <td>6</td>
                <td>8</td>
                <td>12</td>
                <td>6 + 8 - 12 = <strong>2</strong></td>
                <td>54 nets</td>
              </tr>
              <tr>
                <td><strong>Cube (Regular Hexahedron)</strong></td>
                <td>6 Congruent Squares</td>
                <td>6</td>
                <td>8</td>
                <td>12</td>
                <td>6 + 8 - 12 = <strong>2</strong></td>
                <td><strong>11 nets</strong></td>
              </tr>
              <tr>
                <td><strong>Regular Tetrahedron</strong></td>
                <td>4 Congruent Equilateral Triangles</td>
                <td>4</td>
                <td>4</td>
                <td>6</td>
                <td>4 + 4 - 6 = <strong>2</strong></td>
                <td><strong>2 nets</strong></td>
              </tr>
              <tr>
                <td><strong>Square Pyramid</strong></td>
                <td>1 Square + 4 Triangles</td>
                <td>5</td>
                <td>5</td>
                <td>8</td>
                <td>5 + 5 - 8 = <strong>2</strong></td>
                <td>8 nets</td>
              </tr>
              <tr>
                <td><strong>Regular Octahedron</strong></td>
                <td>8 Congruent Equilateral Triangles</td>
                <td>8</td>
                <td>6</td>
                <td>12</td>
                <td>8 + 6 - 12 = <strong>2</strong></td>
                <td><strong>11 nets</strong></td>
              </tr>
              <tr>
                <td><strong>Regular Dodecahedron</strong></td>
                <td>12 Congruent Regular Pentagons</td>
                <td>12</td>
                <td>20</td>
                <td>30</td>
                <td>12 + 20 - 30 = <strong>2</strong></td>
                <td><strong>43,380 nets</strong></td>
              </tr>
              <tr>
                <td><strong>Regular Icosahedron</strong></td>
                <td>20 Congruent Equilateral Triangles</td>
                <td>20</td>
                <td>12</td>
                <td>30</td>
                <td>20 + 12 - 30 = <strong>2</strong></td>
                <td><strong>43,380 nets</strong></td>
              </tr>
              <tr>
                <td><strong>General Prism (n-gon)</strong></td>
                <td>2 n-gons + n Parallelograms</td>
                <td><span class="math-inline">n + 2</span></td>
                <td><span class="math-inline">2n</span></td>
                <td><span class="math-inline">3n</span></td>
                <td><span class="math-inline">(n+2) + 2n - 3n = 2</span></td>
                <td>Varies by n</td>
              </tr>
              <tr>
                <td><strong>General Pyramid (n-gon)</strong></td>
                <td>1 n-gon + n Triangles</td>
                <td><span class="math-inline">n + 1</span></td>
                <td><span class="math-inline">n + 1</span></td>
                <td><span class="math-inline">2n</span></td>
                <td><span class="math-inline">(n+1) + (n+1) - 2n = 2</span></td>
                <td>Varies by n</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>

      <!-- TABLE 3.3: ORTHOGRAPHIC SILHOUETTE IDENTIFICATION MATRIX -->
      <div class="concept-card">
        <h3 class="concept-card-title"><i class="fa-solid fa-eye"></i> Table 3.3: Orthographic 2D Silhouette Lookup Matrix</h3>
        <p>
          Quick lookup table matching three-dimensional geometry with its orthographic projections on the Vertical (Front), Horizontal (Top), and Profile (Side) planes.
        </p>

        <div class="data-table-wrapper">
          <table class="data-table">
            <thead>
              <tr>
                <th>3D Solid (Orientation)</th>
                <th>Front View (Vertical Plane)</th>
                <th>Top View (Horizontal Plane)</th>
                <th>Side View (Profile Plane)</th>
                <th>Key Engineering Identification Feature</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>Vertical Cylinder</strong></td>
                <td>Rectangle (<span class="math-inline">2r × h</span>)</td>
                <td>Circle (radius <span class="math-inline">r</span>)</td>
                <td>Rectangle (<span class="math-inline">2r × h</span>)</td>
                <td>Front and Side views identical rectangles; Top view pure circle.</td>
              </tr>
              <tr>
                <td><strong>Vertical Cone</strong></td>
                <td>Isosceles Triangle (base <span class="math-inline">2r</span>, height <span class="math-inline">h</span>)</td>
                <td>Circle with center point (apex)</td>
                <td>Isosceles Triangle</td>
                <td>Apex projects as point in Top view center; triangular elevations.</td>
              </tr>
              <tr>
                <td><strong>Sphere</strong></td>
                <td>Circle (radius <span class="math-inline">R</span>)</td>
                <td>Circle (radius <span class="math-inline">R</span>)</td>
                <td>Circle (radius <span class="math-inline">R</span>)</td>
                <td>Completely invariant circle from all possible viewpoints in space.</td>
              </tr>
              <tr>
                <td><strong>Triangular Prism (Horizontal)</strong></td>
                <td>Rectangle</td>
                <td>Rectangle with center ridge line</td>
                <td>Triangle (base shape)</td>
                <td>Side view reveals the true triangular cross-section.</td>
              </tr>
              <tr>
                <td><strong>Square Pyramid (Apex Up)</strong></td>
                <td>Triangle</td>
                <td>Square with diagonal crosslines (X)</td>
                <td>Triangle</td>
                <td>Top view diagonals indicate edges meeting at the central apex.</td>
              </tr>
              <tr>
                <td><strong>Frustum of a Cone</strong></td>
                <td>Isosceles Trapezium</td>
                <td>Two Concentric Circles</td>
                <td>Isosceles Trapezium</td>
                <td>Unequal circular ends project as concentric circles from above.</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>

      <!-- TABLE 3.4: SURFACE GEODESIC COMPARISON -->
      <div class="concept-card">
        <h3 class="concept-card-title"><i class="fa-solid fa-route"></i> Table 3.4: Geodesic Surface Distance Comparison for the 30 × 12 × 12 cm Cuboid</h3>
        <p>
          Ant starts on End Wall 1 (1 cm below ceiling, centered); Laddu on End Wall 2 (1 cm above floor, centered). Comparing the 3 potential unfolding paths:
        </p>

        <div class="data-table-wrapper">
          <table class="data-table">
            <thead>
              <tr>
                <th>Unfolding Route</th>
                <th>Traversed Faces</th>
                <th>Horizontal Leg (Δx)</th>
                <th>Vertical Leg (Δy)</th>
                <th>Distance Formula: √(Δx² + Δy²)</th>
                <th>Evaluation</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>Route 1: Ceiling Direct</strong></td>
                <td>End Wall 1 ➔ Ceiling ➔ End Wall 2</td>
                <td><span class="math-inline">1 + 30 + 11 = 42 cm</span></td>
                <td><span class="math-inline">0 cm</span> (centered)</td>
                <td><span class="math-inline">d = 42.0 cm</span></td>
                <td>Straight line along ceiling. Longer by 2 cm!</td>
              </tr>
              <tr>
                <td><strong>Route 2: Side Wall Single</strong></td>
                <td>End Wall 1 ➔ Side Wall ➔ End Wall 2</td>
                <td><span class="math-inline">6 + 30 + 6 = 42 cm</span></td>
                <td><span class="math-inline">11 - 1 = 10 cm</span></td>
                <td><span class="math-inline">√(42² + 10²) = √1864 ≈ 43.17 cm</span></td>
                <td>Longest route due to 10 cm vertical drop.</td>
              </tr>
              <tr>
                <td><strong>Route 3: Helical Spiral (5 Faces)</strong></td>
                <td>End 1 ➔ Ceiling ➔ Side ➔ Floor ➔ End 2</td>
                <td><span class="math-inline">32 cm</span></td>
                <td><span class="math-inline">24 cm</span></td>
                <td><span class="math-inline">√(32² + 24²) = √1600 = <strong>40.0 cm</strong></span></td>
                <td><strong style="color: var(--emerald);">ABSOLUTE SHORTEST PATH (GEODESIC)!</strong></td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>

      <!-- TABLE 3.5: PROJECTION INVARIANTS -->
      <div class="concept-card">
        <h3 class="concept-card-title"><i class="fa-solid fa-ruler-combined"></i> Table 3.5: Geometric Properties Preserved vs Altered Under Orthographic Projection</h3>
        <p>
          Understanding which geometric quantities remain invariant under parallel projection is essential for solving spatial reasoning problems.
        </p>

        <div class="data-table-wrapper">
          <table class="data-table">
            <thead>
              <tr>
                <th>Geometric Property</th>
                <th>Is it Preserved?</th>
                <th>Mathematical Rule & Proof</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><strong>Parallelism of Lines</strong></td>
                <td><strong style="color: var(--emerald);">YES (Always)</strong></td>
                <td>If lines <span class="math-inline">L₁ ∥ L₂</span> in space, their parallel projections <span class="math-inline">p(L₁) ∥ p(L₂)</span> are always parallel (or coincide into a single line/point). A parallelogram can NEVER project into a trapezium!</td>
              </tr>
              <tr>
                <td><strong>Midpoints / Ratio of Segments</strong></td>
                <td><strong style="color: var(--emerald);">YES (Always)</strong></td>
                <td>If point <span class="math-inline">M</span> divides segment <span class="math-inline">AB</span> in ratio <span class="math-inline">1:1</span>, then <span class="math-inline">p(M)</span> divides <span class="math-inline">p(AB)</span> in ratio <span class="math-inline">1:1</span>. Parallel projection preserves linear ratios along a line.</td>
              </tr>
              <tr>
                <td><strong>Length of a Segment</strong></td>
                <td><strong style="color: var(--danger);">NO (Only when ∥)</strong></td>
                <td><span class="math-inline">p = l · cos θ ≤ l</span>. Length is preserved only when the segment is parallel to the plane (<span class="math-inline">θ = 0°</span>). If tilted, it shrinks!</td>
              </tr>
              <tr>
                <td><strong>Angles Between Lines</strong></td>
                <td><strong style="color: var(--danger);">NO (Distorted)</strong></td>
                <td>A 90° right angle in space can project as acute, obtuse, or 90° depending on the angle of tilt. (Exception: if one arm of a right angle is parallel to the plane, it projects as 90°).</td>
              </tr>
              <tr>
                <td><strong>Convexity of Polygons</strong></td>
                <td><strong style="color: var(--emerald);">YES</strong></td>
                <td>A convex polygon always projects to a convex polygon (or a line segment). It cannot become concave.</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </section>
"""
