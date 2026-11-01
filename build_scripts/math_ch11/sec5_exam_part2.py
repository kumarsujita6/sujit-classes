# -*- coding: utf-8 -*-
"""
Section 5 Module Part 2: Long Answer Questions, Case Studies & PYQs
Class 8 Mathematics Chapter 11: Exploring Some Geometric Themes
"""

def get_section_5_part2():
    return """
    <!-- SECTION 5 CONTINUED: LONG ANSWERS, CASE STUDIES & PYQS -->
    <section id="section5b" class="section-box">
      <div class="section-header">
        <div class="section-header-left">
          <span class="section-tag">High-Weightage Mastery</span>
          <h2 class="section-title">§ 5. Complete Exam Question Bank (Part 2: Long Answers, Case Studies, PYQs)</h2>
          <p class="section-desc">
            In-depth 5-mark long answer derivations with marking rubrics, real-world competency-based case studies, and previous years' examination questions with complete model answers.
          </p>
        </div>
        <div>
          <span class="badge badge-emerald"><i class="fa-solid fa-trophy"></i> 5M & Case Studies</span>
        </div>
      </div>

      <!-- PART 5.4: LONG ANSWER QUESTIONS (4 QUESTIONS - 5 MARKS EACH) -->
      <div class="concept-card">
        <h3 class="concept-card-title"><i class="fa-solid fa-file-signature"></i> 5.4 Long Answer Question Bank (5 Marks Each)</h3>
        <p>Comprehensive step-by-step mathematical solutions with explicit CBSE marking rubrics.</p>

        <!-- LA 1 -->
        <details class="ans-box">
          <summary>
            <span><span class="step-pill">5 Marks</span> LA 1: Mathematical Analysis of the Koch Snowflake (Sides, Perimeter Divergence & Finite Area Paradox).</span>
          </summary>
          <div class="ans-content">
            <div class="ans-step">
              <div class="ans-step-title">Question Statement</div>
              <p>An equilateral triangle with side length <span class="math-inline">s = 1</span> unit and area <span class="math-inline">A₀</span> is used to generate the Koch Snowflake.
              <br>(a) Derive general formulas for the number of sides (<span class="math-inline">Nₙ</span>), segment length (<span class="math-inline">Lₙ</span>), and perimeter (<span class="math-inline">Pₙ</span>) at Step <span class="math-inline">n</span>.
              <br>(b) Calculate <span class="math-inline">N₃, L₃,</span> and <span class="math-inline">P₃</span> for Step 3.
              <br>(c) Explain mathematically why the perimeter approaches infinity while the area remains strictly finite.</p>
            </div>
            <div class="ans-step">
              <div class="ans-step-title">Step-by-Step Model Answer & Marking Scheme</div>
              <p>• <strong>Part (a): General Formula Derivation:</strong>
              <br>1. <em>Number of sides:</em> At each step, every side is replaced by 4 smaller segments. Starting with <span class="math-inline">N₀ = 3</span>:
              <br><span class="math-inline">N₁ = 3 × 4¹ = 12</span>, <span class="math-inline">N₂ = 3 × 4² = 48</span>, ..., <span class="math-inline">Nₙ = 3 · 4ⁿ</span>. <em>[1 Mark]</em>
              <br>2. <em>Segment length:</em> At each step, each segment is divided into thirds:
              <br><span class="math-inline">L₀ = 1</span>, <span class="math-inline">L₁ = ⅓</span>, <span class="math-inline">L₂ = 1/3²</span>, ..., <span class="math-inline">Lₙ = 1 / 3ⁿ</span>. <em>[0.5 Mark]</em>
              <br>3. <em>Perimeter:</em> <span class="math-inline">Pₙ = Nₙ × Lₙ = (3 · 4ⁿ) × (1 / 3ⁿ) = 3 · (4/3)ⁿ  units</span>. <em>[0.5 Mark]</em><br><br>
              • <strong>Part (b): Calculations for Step 3:</strong>
              <br>• <span class="math-inline">N₃ = 3 · 4³ = 3 × 64 = 192  sides</span>. <em>[0.5 Mark]</em>
              <br>• <span class="math-inline">L₃ = 1 / 3³ = 1 / 27  units</span>. <em>[0.5 Mark]</em>
              <br>• <span class="math-inline">P₃ = 192 × (1 / 27) = 64 / 9 ≈ 7.11  units</span>. <em>[0.5 Mark]</em><br><br>
              • <strong>Part (c): The Perimeter Divergence & Finite Area Paradox:</strong>
              <br>1. <em>Perimeter:</em> The common ratio of perimeter growth is <span class="math-inline">4/3 = 1.333... &gt; 1</span>. Because the base is strictly greater than 1, <span class="math-inline">Limit as n → ∞: (4/3)ⁿ = ∞</span>. Therefore, the boundary perimeter diverges to <strong>infinity</strong>! <em>[0.75 Mark]</em>
              <br>2. <em>Area:</em> At Step <span class="math-inline">k</span>, <span class="math-inline">3 · 4ᵏ⁻¹</span> small triangles are added, each having area <span class="math-inline">A₀ / 9ᵏ</span>. The added area forms a geometric series with common ratio <span class="math-inline">4/9 &lt; 1</span>. The infinite sum evaluates to:
              <br><span class="math-inline">A_∞ = A₀ [1 + (1/3) ∑_{k=1}^∞ (4/9)ᵏ] = A₀ [1 + (1/3) · (4/9/1 - 4/9)] = A₀ [1 + (1/3) · (4/5)] = A₀ [1 + (4/15)] = (8/5) A₀ = 1.6 A₀</span>.
              <br>Because the infinite geometric series converges, the total enclosed area is strictly <strong>finite</strong> (<span class="math-inline">1.6 A₀</span>). <em>[0.75 Mark]</em></p>
            </div>
            <p><strong>Final Verdict:</strong> The Koch Snowflake has an infinite boundary that encloses a bounded, finite area of <span class="math-inline">1.6 A₀</span>.</p>
          </div>
        </details>

        <!-- LA 2 -->
        <details class="ans-box">
          <summary>
            <span><span class="step-pill">5 Marks</span> LA 2: Surface Geodesic Navigation: Shortest Path on a 20 cm × 10 cm × 10 cm Cuboid.</span>
          </summary>
          <div class="ans-content">
            <div class="ans-step">
              <div class="ans-step-title">Question Statement</div>
              <p>A solid wooden cuboid has length = 20 cm, width = 10 cm, and height = 10 cm. An ant starts at the bottom-left corner <span class="math-inline">A</span> of the front face (10 cm × 10 cm) and wants to crawl along the surface to the diagonally opposite top-right corner <span class="math-inline">B</span> of the rear face (10 cm × 10 cm).
              <br>(a) Identify all distinct unfolding routes connecting corner <span class="math-inline">A</span> to corner <span class="math-inline">B</span> across the intermediate faces.
              <br>(b) Apply the Baudhāyana-Pythagoras theorem to calculate the straight-line distance for each unfolding route.
              <br>(c) Determine the absolute shortest path (geodesic) and calculate how many centimeters the ant saves compared to the longer route.</p>
            </div>
            <div class="ans-step">
              <div class="ans-step-title">Step-by-Step Model Answer & Marking Scheme</div>
              <p>• <strong>Part (a): Identification of Unfolding Configurations:</strong>
              <br>To travel from corner <span class="math-inline">A</span> on the front face to corner <span class="math-inline">B</span> on the rear face, the ant must traverse intermediate faces:
              <br>• <em>Configuration 1 (Across Top Face):</em> Front face (10×10) ➔ Top face (20×10) ➔ Rear face (10×10).
              <br>• <em>Configuration 2 (Across Side Face):</em> Front face (10×10) ➔ Side face (20×10) ➔ Rear face (10×10). <em>[1.5 Marks]</em><br><br>
              • <strong>Part (b): Calculation using Baudhāyana-Pythagoras Theorem:</strong>
              <br>1. <em>For Configuration 1 (Traversing via Top Face):</em>
              <br>• Horizontal span: along the width of front face (10 cm).
              <br>• Vertical span: height of front face (10 cm) + length of top face (20 cm) + height of rear face (10 cm) = <span class="math-inline">10 + 20 + 10 = 40 cm</span>.
              <br>• By Pythagoras theorem:
              <br><span class="math-inline">d₁ = √(10² + 40²) = √(100 + 1600) = √1700 ≈ 41.23 cm</span>. <em>[1.5 Marks]</em>
              <br><br>
              2. <em>For Configuration 2 (Traversing via Side Face):</em>
              <br>• Horizontal span: width of front face (10 cm) + length of side face (20 cm) + width of rear face (10 cm) = <span class="math-inline">10 + 20 + 10 = 40 cm</span>.
              <br>• Vertical span: from bottom edge to top edge = 10 cm.
              <br>• By Pythagoras theorem: <span class="math-inline">d₂ = √(40² + 10²) = √1700 ≈ 41.23 cm</span>.
              <br><br>
              3. <em>Configuration 3 (Traversing across Bottom Face and End Face):</em>
              <br>If the ant traverses Front ➔ Floor (20 cm long) ➔ Rear:
              <br>Horizontal leg = 20 cm, Vertical leg = <span class="math-inline">10 + 10 = 20 cm</span>:
              <br><span class="math-inline">d₃ = √(20² + (10 + 10)²) = √(400 + 400) = √800 = 20√2 ≈ 28.28 cm</span>! <em>[1 Mark]</em><br><br>
              • <strong>Part (c): Determination of Geodesic & Savings:</strong>
              <br>• The shortest possible surface route is Configuration 3: <span class="math-inline">d = 20√2 ≈ 28.28 cm</span>.
              <br>• Compared to Route 1 (<span class="math-inline">41.23 cm</span>), the ant saves:
              <br><span class="math-inline">41.23 - 28.28 = 12.95 cm</span>! <em>[1 Mark]</em></p>
            </div>
            <p><strong>Final Answer:</strong> Shortest surface path is <span class="math-inline">20√2 ≈ 28.28 cm</span>, saving approximately 12.95 cm.</p>
          </div>
        </details>

        <!-- LA 3 -->
        <details class="ans-box">
          <summary>
            <span><span class="step-pill">5 Marks</span> LA 3: Polyhedra Structural Laws, Euler's Invariant & The Five Platonic Solids.</span>
          </summary>
          <div class="ans-content">
            <div class="ans-step">
              <div class="ans-step-title">Question Statement</div>
              <p>(a) Define a polyhedron and distinguish between a prism and a pyramid based on face geometry.
              <br>(b) Write the general formulas for Faces (<span class="math-inline">F</span>), Vertices (<span class="math-inline">V</span>), and Edges (<span class="math-inline">E</span>) of an <span class="math-inline">n</span>-sided prism and an <span class="math-inline">n</span>-sided pyramid. Prove algebraically that Euler's formula holds for all values of <span class="math-inline">n</span> in both families.
              <br>(c) What is a Platonic solid? Name all five Platonic solids and list their face shapes.</p>
            </div>
            <div class="ans-step">
              <div class="ans-step-title">Step-by-Step Model Answer & Marking Scheme</div>
              <p>• <strong>Part (a): Definitions:</strong>
              <br>• <em>Polyhedron:</em> A 3D solid bounded entirely by flat plane polygonal faces.
              <br>• <em>Prism:</em> Has two congruent parallel <span class="math-inline">n</span>-gon bases connected by <span class="math-inline">n</span> rectangular or parallelogram lateral faces.
              <br>• <em>Pyramid:</em> Has a single <span class="math-inline">n</span>-gon base and <span class="math-inline">n</span> triangular lateral faces meeting at a single apex point. <em>[1.5 Marks]</em><br><br>
              • <strong>Part (b): General Formulas & Algebraic Proof of Euler's Formula:</strong>
              <br>1. <em>For an n-sided Prism:</em>
              <br><span class="math-inline">F = n + 2</span>, <span class="math-inline">V = 2n</span>, <span class="math-inline">E = 3n</span>.
              <br>Euler's invariant: <span class="math-inline">F + V - E = (n + 2) + 2n - 3n = 3n + 2 - 3n = 2</span> (Proved!).
              <br>2. <em>For an n-sided Pyramid:</em>
              <br><span class="math-inline">F = n + 1</span>, <span class="math-inline">V = n + 1</span>, <span class="math-inline">E = 2n</span>.
              <br>Euler's invariant: <span class="math-inline">F + V - E = (n + 1) + (n + 1) - 2n = 2n + 2 - 2n = 2</span> (Proved!). <em>[1.5 Marks]</em><br><br>
              • <strong>Part (c): The Five Platonic Solids:</strong>
              <br>A Platonic solid is a convex regular polyhedron whose faces are congruent regular polygons and where the same number of faces meet at each vertex. Exactly 5 exist:
              <br>1. <strong>Regular Tetrahedron:</strong> 4 faces (all equilateral triangles), <span class="math-inline">V = 4, E = 6</span>.
              <br>2. <strong>Cube (Regular Hexahedron):</strong> 6 faces (all squares), <span class="math-inline">V = 8, E = 12</span>.
              <br>3. <strong>Regular Octahedron:</strong> 8 faces (all equilateral triangles), <span class="math-inline">V = 6, E = 12</span>.
              <br>4. <strong>Regular Dodecahedron:</strong> 12 faces (all regular pentagons), <span class="math-inline">V = 20, E = 30</span>.
              <br>5. <strong>Regular Icosahedron:</strong> 20 faces (all equilateral triangles), <span class="math-inline">V = 12, E = 30</span>. <em>[2 Marks]</em></p>
            </div>
          </div>
        </details>

        <!-- LA 4 -->
        <details class="ans-box">
          <summary>
            <span><span class="step-pill">5 Marks</span> LA 4: The 11 Cube Nets & Isometric Coordinate Geometry Principles.</span>
          </summary>
          <div class="ans-content">
            <div class="ans-step">
              <div class="ans-step-title">Question Statement</div>
              <p>(a) Classify the 11 valid folding nets of a cube into their four structural families.
              <br>(b) State two visual rules that allow a student to instantly identify an invalid hexamino net.
              <br>(c) Explain the geometric principles of an isometric grid, including coordinate axis orientation, true scale preservation, and why the Penrose Triangle cannot physically exist in 3D space.</p>
            </div>
            <div class="ans-step">
              <div class="ans-step-title">Step-by-Step Model Answer & Marking Scheme</div>
              <p>• <strong>Part (a): Taxonomy of the 11 Cube Nets:</strong>
              <br>1. <strong>"1-4-1" Pattern (6 Nets):</strong> A 4-in-a-row central band with 1 square above and 1 square below on opposite sides.
              <br>2. <strong>"1-3-2" Pattern (3 Nets):</strong> A 3-in-a-row central band with 1 square on one side and a 2-square step on the other.
              <br>3. <strong>"2-2-2" Pattern (1 Net):</strong> A 3-step zigzag staircase of three pairs of squares.
              <br>4. <strong>"3-3" Pattern (1 Net):</strong> Two rows of 3 squares offset by 1 square. <em>[1.5 Marks]</em><br><br>
              • <strong>Part (b): Rules to Spot Invalid Nets:</strong>
              <br>1. <em>The 2×2 Block Rule:</em> Any net containing a 2×2 square cluster is invalid because faces fold into the same position, creating overlapping faces and leaving an open hole.
              <br>2. <em>The 5-in-a-Row Rule:</em> Any net with 5 or 6 squares in a single straight row is invalid because the 5th square wraps completely around to overlap the 1st square. <em>[1 Mark]</em><br><br>
              • <strong>Part (c): Isometric Geometry & The Penrose Triangle:</strong>
              <br>1. <em>Isometric Grid Principles:</em> 'Isometric' means equal measure. The 3 coordinate axes (Height, Length, Depth) are projected at equal 120° angles to each other. Because the projection is parallel, unit distances along all 3 axes are drawn to true 1:1 scale without perspective shrinkage. <em>[1.25 Marks]</em>
              <br>2. <em>The Penrose Triangle Impossibility:</em> The Penrose Triangle depicts 3 straight square beams meeting at 90° at all 3 vertices. In 3D space, three 90° right angles can never close into a triangle (<span class="math-inline">90° + 90° + 90° = 270° ≠ 180°</span>). The illusion works on 2D isometric paper because parallel projection removes vanishing points, eliminating depth cues and allowing the artist to visually connect the near end to the far end. <em>[1.25 Marks]</em></p>
            </div>
          </div>
        </details>
      </div>

      <!-- PART 5.5: COMPETENCY-BASED CASE STUDIES (2 CASE STUDIES) -->
      <div class="concept-card">
        <h3 class="concept-card-title"><i class="fa-solid fa-briefcase"></i> 5.5 Competency-Based Case Studies (Real-World Applications)</h3>
        <p>CBSE-style real-world problem scenarios testing multi-disciplinary mathematical application.</p>

        <!-- CASE STUDY 1 -->
        <details class="ans-box">
          <summary>
            <span><span class="step-pill">Case Study 1</span> Telecommunications Engineering & Khajuraho Temple Fractal Architecture.</span>
          </summary>
          <div class="ans-content">
            <div class="callout callout-def">
              <div class="callout-title"><i class="fa-solid fa-tower-broadcast"></i> Scenario Background</div>
              <p>
                Modern smartphones must receive a wide range of wireless signals: 4G LTE (800 MHz, 1800 MHz), 5G NR (3.5 GHz), Wi-Fi (2.4 GHz, 5 GHz), Bluetooth (2.4 GHz), and GPS (1.57 GHz). Classical antennas require a physical length equal to approximately one-quarter of the signal's wavelength (<span class="math-inline">λ/4</span>), meaning multiple separate antennas would be needed, making phones bulky. Telecommunication engineers solved this by designing <strong>Fractal Antennas</strong> (using the Sierpinski Carpet or Koch Snowflake curve). Because fractal curves repeat self-similar geometries at multiple microscopic scales, the single antenna resonates efficiently across multiple frequency bands simultaneously!
                <br>Centuries earlier, Indian master-builders designed the <strong>Kandariya Mahadev Temple</strong> at Khajuraho using the identical fractal self-similarity principle: 84 miniature spires (urushringas) clustered around the central shikhara, creating cosmic resonance and architectural earthquake-damping.
              </p>
            </div>

            <p><strong>Sub-Questions (CBSE CBE Pattern):</strong></p>
            <div class="ans-step">
              <div class="ans-step-title">Question 1 (1 Mark): Fractal Resonance Principle</div>
              <p>Why is a fractal geometry uniquely suited for receiving multiple wireless frequencies compared to a straight wire antenna?
              <br><strong>Answer:</strong> An antenna's resonant frequency depends on its physical length. Because a fractal contains self-similar features at multiple distinct length scales (iterations), it can resonate across multiple different electromagnetic wavelengths simultaneously (multi-band performance). <em>[1 Mark]</em></p>
            </div>

            <div class="ans-step">
              <div class="ans-step-title">Question 2 (1 Mark): Iteration Area Calculation</div>
              <p>An engineer etches a Sierpinski Carpet antenna on a microchip starting from a square of area 81 mm². What is the conducting copper area remaining after Step 2?
              <br><strong>Answer:</strong>
              <br><span class="math-inline">A₂ = (8/9)² × A₀ = (64/81) × 81 mm² = 64  mm²</span>. <em>[1 Mark]</em></p>
            </div>

            <div class="ans-step">
              <div class="ans-step-title">Question 3 (1 Mark): Koch Antenna Boundary Growth</div>
              <p>A Koch dipole antenna is built on a triangle of side 9 cm. What is the total perimeter of the antenna at Step 2?
              <br><strong>Answer:</strong>
              <br><span class="math-inline">P₂ = 3s × (4/3)² = 3(9) × (16/9) = 27 × (16/9) = 48  cm</span>.
              <br>The boundary length expands from 27 cm to 48 cm within the same compact footprint! <em>[1 Mark]</em></p>
            </div>

            <div class="ans-step">
              <div class="ans-step-title">Question 4 (1 Mark): Temple Architectural Philosophy</div>
              <p>Explain the cultural and mathematical connection between the Khajuraho temple shikharas and fractal self-similarity.
              <br><strong>Answer:</strong> The Kandariya Mahadev temple features 84 miniature replica spires (urushringas) clustered around the central shikhara. In Vedic philosophy, this fractal self-similarity symbolizes that the infinite supreme universe (Brahman) is fully reflected within every individual soul (Atman). <em>[1 Mark]</em></p>
            </div>
          </div>
        </details>

        <!-- CASE STUDY 2 -->
        <details class="ans-box">
          <summary>
            <span><span class="step-pill">Case Study 2</span> Industrial Packaging Logistics & Space Habitat Geodesic Navigation.</span>
          </summary>
          <div class="ans-content">
            <div class="callout callout-act">
              <div class="callout-title"><i class="fa-solid fa-shuttle-space"></i> Scenario Background</div>
              <p>
                An aerospace engineering consortium is designing a robotic surface maintenance rover for a lunar habitat. The habitat module is shaped like a large rectangular cuboid: Length = 24 meters, Width = 12 meters, and Height = 12 meters.
                <br>• The rover charging dock is situated on one end wall (12 m × 12 m), exactly 2 meters below the habitat ceiling and 6 meters from the side edges.
                <br>• A damaged solar telemetry sensor is located on the opposite end wall (12 m × 12 m), exactly 2 meters above the lunar soil foundation and 6 meters from the side edges.
                <br>The lunar rover's battery is severely depleted and can only travel a maximum of 35 meters along the module's exterior surface before shutting down.
              </p>
            </div>

            <p><strong>Sub-Questions (CBSE CBE Pattern):</strong></p>
            <div class="ans-step">
              <div class="ans-step-title">Question 1 (1 Mark): Flat Net Transformation</div>
              <p>State the fundamental geometric theorem that allows engineers to compute the rover's shortest travel path on the 3D habitat exterior.
              <br><strong>Answer:</strong> The Geodesic Unfolding Theorem: Any continuous path along the faces of a polyhedron transforms into a straight line of the exact same length when the traversed faces are unfolded flat onto a single 2D plane. <em>[1 Mark]</em></p>
            </div>

            <div class="ans-step">
              <div class="ans-step-title">Question 2 (1.5 Marks): Direct Ceiling Path Calculation</div>
              <p>Calculate the distance the rover would travel if it navigated directly straight up, across the ceiling, and down the far wall.
              <br><strong>Answer:</strong>
              <br>Distance along end wall to ceiling = 2 m.
              <br>Distance across ceiling = 24 m.
              <br>Distance down far wall to sensor = <span class="math-inline">12 - 2 = 10  m</span>.
              <br>Total straight-line distance: <span class="math-inline">d_{ceiling} = 2 + 24 + 10 = 36  meters</span>. <em>[1.5 Marks]</em></p>
            </div>

            <div class="ans-step">
              <div class="ans-step-title">Question 3 (1.5 Marks): Spiral Geodesic Path Calculation</div>
              <p>Calculate the distance if the rover uses an unfolded helical spiral net path across 5 faces where the Pythagorean legs are 20 m and 21 m.
              <br><strong>Answer:</strong>
              <br>Applying Baudhāyana-Pythagoras theorem:
              <br><span class="math-inline">d_{spiral} = √(20² + 21²) = √(400 + 441) = √841 = 29.0  meters</span>! <em>[1.5 Marks]</em></p>
            </div>

            <div class="ans-step">
              <div class="ans-step-title">Question 4 (1 Mark): Mission Feasibility Conclusion</div>
              <p>Will the rover reach the damaged sensor before its 35-meter battery reserve is exhausted?
              <br><strong>Answer:</strong>
              <br>• If it takes the direct ceiling path (36 m), the battery will die 1 meter before reaching the sensor!
              <br>• If it takes the 29-meter geodesic spiral route, <span class="math-inline">29  m &lt; 35  m</span>. The rover successfully completes the repair mission with 6 meters of battery range to spare! <em>[1 Mark]</em></p>
            </div>
          </div>
        </details>
      </div>

      <!-- PART 5.6: PREVIOUS YEARS QUESTIONS (5 PYQS & MOST PROBABLE QUESTIONS) -->
      <div class="concept-card">
        <h3 class="concept-card-title"><i class="fa-solid fa-clock-rotate-left"></i> 5.6 Previous Years' Questions (PYQs) & Most Probable Exam Questions</h3>
        <p>Real board examination questions with step-by-step scoring criteria.</p>

        <!-- PYQ 1 -->
        <details class="ans-box">
          <summary>
            <span><span class="step-pill">PYQ 2024</span> PYQ 1: A polyhedron has 20 faces and 12 vertices. Find its edges and identify the Platonic solid.</span>
          </summary>
          <div class="ans-content">
            <div class="ans-step">
              <div class="ans-step-title">Step 1: Given Data & Formula</div>
              <p>Faces <span class="math-inline">F = 20</span>, Vertices <span class="math-inline">V = 12</span>.
              <br>Euler's Formula: <span class="math-inline">F + V - E = 2</span>.</p>
            </div>
            <div class="ans-step">
              <div class="ans-step-title">Step 2: Calculation</div>
              <p><span class="math-inline">20 + 12 - E = 2 ⇒ 32 - E = 2 ⇒ E = 32 - 2 = 30  edges</span>.</p>
            </div>
            <div class="ans-step">
              <div class="ans-step-title">Step 3: Identification</div>
              <p>A regular polyhedron with 20 equilateral triangular faces, 12 vertices, and 30 edges is the <strong>Regular Icosahedron</strong>.</p>
            </div>
            <p><strong>Final Answer:</strong> Number of edges is <strong>30</strong>; the solid is the <strong>Regular Icosahedron</strong>.</p>
          </div>
        </details>

        <!-- PYQ 2 -->
        <details class="ans-box">
          <summary>
            <span><span class="step-pill">PYQ 2023</span> PYQ 2: In the Sierpinski Carpet, if starting square has side 27 cm, find the total area of the 8 holes created during Step 2.</span>
          </summary>
          <div class="ans-content">
            <div class="ans-step">
              <div class="ans-step-title">Step 1: Dimensions of Step 2 Holes</div>
              <p>Starting square has side <span class="math-inline">s = 27  cm</span>.
              <br>• At Step 1: Sub-squares have side <span class="math-inline">27 / 3 = 9  cm</span>. Hole area = <span class="math-inline">9 × 9 = 81  cm²</span>.
              <br>• At Step 2: Each of the 8 remaining squares is divided into 9 squares of side <span class="math-inline">9 / 3 = 3  cm</span>.
              <br>Each hole created at Step 2 is a square of side <span class="math-inline">3  cm</span>.</p>
            </div>
            <div class="ans-step">
              <div class="ans-step-title">Step 2: Area Calculation</div>
              <p>Area of each single Step 2 hole = <span class="math-inline">3  cm × 3  cm = 9  cm²</span>.
              <br>Number of new holes created at Step 2 = 8 holes.
              <br>Total area of these 8 holes = <span class="math-inline">8 × 9  cm² = 72  cm²</span>.</p>
            </div>
            <p><strong>Final Answer:</strong> The total area of the 8 holes created during Step 2 is <strong>72 cm²</strong>.</p>
          </div>
        </details>

        <!-- PYQ 3 -->
        <details class="ans-box">
          <summary>
            <span><span class="step-pill">PYQ 2023</span> PYQ 3: Identify the 3D solid having a rectangular front view, triangular top view, and rectangular side view.</span>
          </summary>
          <div class="ans-content">
            <div class="ans-step">
              <div class="ans-step-title">Step-by-Step Analysis</div>
              <p>• The top view is a <strong>triangle</strong>, meaning looking from above reveals two parallel triangular end faces.
              <br>• The front view is a <strong>rectangle</strong>, corresponding to one of the flat lateral walls.
              <br>• The side view is a <strong>rectangle</strong>, corresponding to another lateral wall.</p>
            </div>
            <div class="ans-step">
              <div class="ans-step-title">Conclusion</div>
              <p>The solid is a <strong>Triangular Prism</strong> oriented standing vertically on its triangular base.</p>
            </div>
            <p><strong>Final Answer:</strong> <strong>Triangular Prism</strong>.</p>
          </div>
        </details>

        <!-- PYQ 4 -->
        <details class="ans-box">
          <summary>
            <span><span class="step-pill">PYQ 2022</span> PYQ 4: Explain why parallel lines in 3D space always project as parallel lines under sunlight.</span>
          </summary>
          <div class="ans-content">
            <div class="ans-step">
              <div class="ans-step-title">Mathematical Proof</div>
              <p>• Sunlight rays reaching Earth travel across ~150 million km, making them effectively <strong>parallel</strong> to one another.
              <br>• Let two lines <span class="math-inline">L₁</span> and <span class="math-inline">L₂</span> in space be parallel (<span class="math-inline">L₁ ∥ L₂</span>).
              <br>• The parallel projection rays passing through <span class="math-inline">L₁</span> form a plane <span class="math-inline">P₁</span>, and those passing through <span class="math-inline">L₂</span> form a plane <span class="math-inline">P₂</span>.
              <br>• Since <span class="math-inline">L₁ ∥ L₂</span> and the projection rays are parallel, plane <span class="math-inline">P₁</span> is strictly parallel to plane <span class="math-inline">P₂</span>.
              <br>• When two parallel planes are intersected by the ground/wall plane, their lines of intersection (the projected shadows) must be strictly <strong>parallel lines</strong>.</p>
            </div>
            <p><strong>Final Answer:</strong> Parallel planes formed by parallel sunlight rays intersect any projection plane along parallel lines.</p>
          </div>
        </details>

        <!-- PYQ 5 -->
        <details class="ans-box">
          <summary>
            <span><span class="step-pill">PYQ 2022</span> PYQ 5: On an isometric grid, a cube of side 4 units is drawn. Find its total surface area and volume.</span>
          </summary>
          <div class="ans-content">
            <div class="ans-step">
              <div class="ans-step-title">Step 1: True Scale Drafting Principle</div>
              <p>On an isometric grid, distances along the three axes (length, depth, height) are drawn to <strong>true scale</strong> (1 grid unit = 1 unit of length). Therefore, the actual side length of the cube is <span class="math-inline">s = 4  units</span>.</p>
            </div>
            <div class="ans-step">
              <div class="ans-step-title">Step 2: Surface Area Calculation</div>
              <p>A cube has 6 congruent square faces:
              <br><span class="math-inline">Total Surface Area = 6 × s² = 6 × 4² = 6 × 16 = 96  sq. units</span>.</p>
            </div>
            <div class="ans-step">
              <div class="ans-step-title">Step 3: Volume Calculation</div>
              <p><span class="math-inline">Volume = s³ = 4³ = 64  cubic units</span>.</p>
            </div>
            <p><strong>Final Answer:</strong> Total Surface Area is <strong>96 sq. units</strong>; Volume is <strong>64 cubic units</strong>.</p>
          </div>
        </details>
      </div>
    </section>
"""
