# -*- coding: utf-8 -*-
"""
Section 5 Module Part 1: Interactive Exam Question Bank
MCQs, Assertion-Reasoning & Short Answer Questions
Class 8 Mathematics Chapter 11: Exploring Some Geometric Themes
"""

def get_section_5_part1():
    return """
    <!-- SECTION 5: COMPLETE EXAM QUESTION BANK (PART 1) -->
    <section id="section5" class="section-box">
      <div class="section-header">
        <div class="section-header-left">
          <span class="section-tag">Exam Battleground</span>
          <h2 class="section-title">§ 5. Complete Exam Question Bank (Part 1: MCQs, A&R, Short Answers)</h2>
          <p class="section-desc">
            Rigorous CBSE and BSE pattern exam questions featuring interactive MCQs with trap analysis, Assertion & Reasoning evaluations, and step-marked Short Answer questions.
          </p>
        </div>
        <div>
          <span class="score-badge" id="quizScoreDisplay"><i class="fa-solid fa-trophy"></i> Score: 0 / 5</span>
        </div>
      </div>

      <!-- PART 5.1: CONCEPTUAL MCQS (5 QUESTIONS WITH TRAP ANALYSIS) -->
      <div class="concept-card">
        <h3 class="concept-card-title"><i class="fa-solid fa-list-check"></i> 5.1 Conceptual Multiple Choice Questions (Interactive Quiz)</h3>
        <p>Test your conceptual understanding. Click your chosen option to receive immediate feedback and uncover common exam traps.</p>

        <!-- MCQ 1 -->
        <div class="mcq-card" id="mcqCard1">
          <div class="mcq-question">
            <strong>Q1.</strong> In the construction of the Sierpinski Carpet, if the starting solid square has an area of 729 cm², what is the total area of the remaining square pieces at Step 3?
          </div>
          <div class="options-grid">
            <button class="option-btn" onclick="evaluateMCQ(1, 'A', false, 'You forgot to apply the power of 3! (8/9) × 729 = 648 cm² is only for Step 1.')">
              <span class="pos-badge">A</span> 648 cm²
            </button>
            <button class="option-btn" onclick="evaluateMCQ(1, 'B', false, '576 cm² corresponds to (8/9)² × 729, which is the area at Step 2, not Step 3.')">
              <span class="pos-badge">B</span> 576 cm²
            </button>
            <button class="option-btn" onclick="evaluateMCQ(1, 'C', true, 'Brilliant! At Step 3, Area = (8/9)³ × A₀ = (512 / 729) × 729 = 512 cm².')">
              <span class="pos-badge">C</span> 512 cm²
            </button>
            <button class="option-btn" onclick="evaluateMCQ(1, 'D', false, '343 cm² is 7³, which has no relation to the Sierpinski factor 8/9.')">
              <span class="pos-badge">D</span> 343 cm²
            </button>
          </div>
          <div class="trap-feedback" id="feedback1"></div>
        </div>

        <!-- MCQ 2 -->
        <div class="mcq-card" id="mcqCard2">
          <div class="mcq-question">
            <strong>Q2.</strong> A polyhedron has 14 faces and 24 edges. How many vertices does this polyhedron possess?
          </div>
          <div class="options-grid">
            <button class="option-btn" onclick="evaluateMCQ(2, 'A', false, 'Trap alert: If V = 10, then F + V - E = 14 + 10 - 24 = 0, violating Euler\'s law!')">
              <span class="pos-badge">A</span> 10
            </button>
            <button class="option-btn" onclick="evaluateMCQ(2, 'B', true, 'Correct! By Euler\'s Formula: F + V - E = 2 ⟹ 14 + V - 24 = 2 ⟹ V - 10 = 2 ⟹ V = 12.')">
              <span class="pos-badge">B</span> 12
            </button>
            <button class="option-btn" onclick="evaluateMCQ(2, 'C', false, '14 vertices would give F + V - E = 14 + 14 - 24 = 4 ≠ 2.')">
              <span class="pos-badge">C</span> 14
            </button>
            <button class="option-btn" onclick="evaluateMCQ(2, 'D', false, '16 vertices violates Euler\'s topological invariant.')">
              <span class="pos-badge">D</span> 16
            </button>
          </div>
          <div class="trap-feedback" id="feedback2"></div>
        </div>

        <!-- MCQ 3 -->
        <div class="mcq-card" id="mcqCard3">
          <div class="mcq-question">
            <strong>Q3.</strong> Which of the following hexamino arrangements can NEVER be folded into a closed 3D cube?
          </div>
          <div class="options-grid">
            <button class="option-btn" onclick="evaluateMCQ(3, 'A', false, 'The Latin cross (1-4-1 pattern) is one of the most classic valid nets of a cube.')">
              <span class="pos-badge">A</span> A 1-4-1 Latin cross arrangement
            </button>
            <button class="option-btn" onclick="evaluateMCQ(3, 'B', false, 'A 1-3-2 step arrangement is a valid cube net (#7, #8, #9).')">
              <span class="pos-badge">B</span> A 1-3-2 step arrangement
            </button>
            <button class="option-btn" onclick="evaluateMCQ(3, 'C', true, 'Spot on! Any arrangement containing a 2 × 2 block of 4 squares can NEVER fold into a cube because the faces overlap!')">
              <span class="pos-badge">C</span> An arrangement containing a 2 × 2 cluster of 4 squares
            </button>
            <button class="option-btn" onclick="evaluateMCQ(3, 'D', false, 'A 2-2-2 zigzag staircase is a completely valid cube net (#10).')">
              <span class="pos-badge">D</span> A 2-2-2 zigzag staircase arrangement
            </button>
          </div>
          <div class="trap-feedback" id="feedback3"></div>
        </div>

        <!-- MCQ 4 -->
        <div class="mcq-card" id="mcqCard4">
          <div class="mcq-question">
            <strong>Q4.</strong> A line segment of actual length 15 cm in 3D space is projected onto a vertical plane. Which of the following could CANNOT be the length of its orthographic projection?
          </div>
          <div class="options-grid">
            <button class="option-btn" onclick="evaluateMCQ(4, 'A', false, 'p = 0 cm occurs when the line is perpendicular (at 90°) to the vertical plane.')">
              <span class="pos-badge">A</span> 0 cm
            </button>
            <button class="option-btn" onclick="evaluateMCQ(4, 'B', false, 'p = 10.5 cm is completely valid since 0 ≤ 10.5 ≤ 15 (cos θ = 10.5/15 = 0.7).')">
              <span class="pos-badge">B</span> 10.5 cm
            </button>
            <button class="option-btn" onclick="evaluateMCQ(4, 'C', false, 'p = 15 cm occurs when the line is parallel to the vertical plane.')">
              <span class="pos-badge">C</span> 15 cm
            </button>
            <button class="option-btn" onclick="evaluateMCQ(4, 'D', true, 'Correct! Under orthographic projection, p = l · cos θ ≤ l. Since l = 15 cm, the projected length can never exceed 15 cm!')">
              <span class="pos-badge">D</span> 16.2 cm
            </button>
          </div>
          <div class="trap-feedback" id="feedback4"></div>
        </div>

        <!-- MCQ 5 -->
        <div class="mcq-card" id="mcqCard5">
          <div class="mcq-question">
            <strong>Q5.</strong> On an isometric grid, what is the angle between any two of the three principal coordinate axes (Height, Length, and Depth)?
          </div>
          <div class="options-grid">
            <button class="option-btn" onclick="evaluateMCQ(5, 'A', false, '90° is the angle in true 3D space, but on the 2D isometric paper, the axes are projected at 120°!')">
              <span class="pos-badge">A</span> 90°
            </button>
            <button class="option-btn" onclick="evaluateMCQ(5, 'B', true, 'Exactly! The 360° circle is divided equally into 3 angles of 120° (360° ÷ 3 = 120°), ensuring equal true scaling along all three dimensions.')">
              <span class="pos-badge">B</span> 120°
            </button>
            <button class="option-btn" onclick="evaluateMCQ(5, 'C', false, '60° is the angle of the isometric grid triangles, but the principal axes are spaced at 120°.')">
              <span class="pos-badge">C</span> 60°
            </button>
            <button class="option-btn" onclick="evaluateMCQ(5, 'D', false, '45° is used in cabinet oblique projections, not isometric drawings.')">
              <span class="pos-badge">D</span> 45°
            </button>
          </div>
          <div class="trap-feedback" id="feedback5"></div>
        </div>
      </div>

      <!-- PART 5.2: ASSERTION & REASONING (5 QUESTIONS) -->
      <div class="concept-card">
        <h3 class="concept-card-title"><i class="fa-solid fa-scale-balanced"></i> 5.2 Assertion & Reasoning Question Bank</h3>
        <p>
          Directions: In each question below, two statements are given—one labeled <strong>Assertion (A)</strong> and the other labeled <strong>Reason (R)</strong>. Choose the correct option:
          <br><strong>(a)</strong> Both A and R are true, and R is the correct explanation of A.
          <br><strong>(b)</strong> Both A and R are true, but R is NOT the correct explanation of A.
          <br><strong>(c)</strong> A is true, but R is false.
          <br><strong>(d)</strong> A is false, but R is true.
        </p>

        <!-- AR 1 -->
        <details class="ans-box">
          <summary>
            <span><span class="step-pill">A&R 1</span> Assertion: The Koch Snowflake has an infinite perimeter but encloses a strictly finite area.</span>
          </summary>
          <div class="ans-content">
            <p><strong>Assertion (A):</strong> The Koch Snowflake has an infinite perimeter but encloses a strictly finite area.<br>
            <strong>Reason (R):</strong> At each step of the Koch Snowflake, the perimeter multiplies by <span class="math-inline">4/3 &gt; 1</span> causing divergence, while the area additions form a converging geometric series bounded by <span class="math-inline">1.6 · A₀</span>.</p>
            <div class="ans-step">
              <div class="ans-step-title">Evaluation</div>
              <p>• Assertion (A) is completely true: <span class="math-inline">Pₙ → ∞</span> while <span class="math-inline">Aₙ → 1.6 A₀</span>.<br>
              • Reason (R) is completely true and correctly explains the mathematical mechanism (<span class="math-inline">4/3 &gt; 1</span> causes divergence, while <span class="math-inline">4/9 &lt; 1</span> creates a converging series sum of 8/5).</p>
            </div>
            <p><strong>Correct Option:</strong> <strong>(a)</strong> Both A and R are true, and R is the correct explanation of A.</p>
          </div>
        </details>

        <!-- AR 2 -->
        <details class="ans-box">
          <summary>
            <span><span class="step-pill">A&R 2</span> Assertion: A standard spherical globe of the Earth can be constructed by folding a flat sheet of paper.</span>
          </summary>
          <div class="ans-content">
            <p><strong>Assertion (A):</strong> A standard spherical globe of the Earth can be constructed by folding a flat sheet of paper without wrinkles, cuts, or stretching.<br>
            <strong>Reason (R):</strong> Carl Friedrich Gauss proved in <em>Theorema Egregium</em> that a flat plane has zero Gaussian curvature (<span class="math-inline">K = 0</span>), whereas a sphere has positive Gaussian curvature (<span class="math-inline">K = 1/R²</span>).</p>
            <div class="ans-step">
              <div class="ans-step-title">Evaluation</div>
              <p>• Assertion (A) is <strong>FALSE</strong>: It is physically and mathematically impossible to wrap a sphere with flat paper without wrinkling, tearing, or stretching.<br>
              • Reason (R) is <strong>TRUE</strong>: Gauss's theorem proves that Gaussian curvature is an intrinsic invariant, so a surface with <span class="math-inline">K = 0</span> can never map isometrically onto a surface with <span class="math-inline">K &gt; 0</span>.</p>
            </div>
            <p><strong>Correct Option:</strong> <strong>(d)</strong> A is false, but R is true.</p>
          </div>
        </details>

        <!-- AR 3 -->
        <details class="ans-box">
          <summary>
            <span><span class="step-pill">A&R 3</span> Assertion: A prism whose bases are 12-sided polygons has 14 faces, 24 vertices, and 36 edges.</span>
          </summary>
          <div class="ans-content">
            <p><strong>Assertion (A):</strong> A prism whose bases are 12-sided polygons has 14 faces, 24 vertices, and 36 edges.<br>
            <strong>Reason (R):</strong> For any prism with an <span class="math-inline">n</span>-sided base, <span class="math-inline">F = n + 2</span>, <span class="math-inline">V = 2n</span>, and <span class="math-inline">E = 3n</span>.</p>
            <div class="ans-step">
              <div class="ans-step-title">Evaluation</div>
              <p>• For <span class="math-inline">n = 12</span>: <span class="math-inline">F = 12 + 2 = 14</span>, <span class="math-inline">V = 2(12) = 24</span>, <span class="math-inline">E = 3(12) = 36</span>. Assertion (A) is true.<br>
              • Reason (R) provides the exact general formulas from which these numbers are derived.<br>
              • Euler Check: <span class="math-inline">14 + 24 - 36 = 2</span> (Valid!).</p>
            </div>
            <p><strong>Correct Option:</strong> <strong>(a)</strong> Both A and R are true, and R is the correct explanation of A.</p>
          </div>
        </details>

        <!-- AR 4 -->
        <details class="ans-box">
          <summary>
            <span><span class="step-pill">A&R 4</span> Assertion: Under parallel orthographic projection, a parallelogram can project as a trapezium with non-parallel sides.</span>
          </summary>
          <div class="ans-content">
            <p><strong>Assertion (A):</strong> Under parallel orthographic projection, a parallelogram can project as a trapezium with non-parallel sides.<br>
            <strong>Reason (R):</strong> Parallel projection preserves parallelism; parallel lines in space always project to parallel lines on the projection plane.</p>
            <div class="ans-step">
              <div class="ans-step-title">Evaluation</div>
              <p>• Assertion (A) is <strong>FALSE</strong>: Because parallel lines must project to parallel lines, the opposite sides can never become non-parallel! A parallelogram can only project to a parallelogram or a straight line.<br>
              • Reason (R) is <strong>TRUE</strong>: Invariance of parallelism is a foundational axiom of parallel projections.</p>
            </div>
            <p><strong>Correct Option:</strong> <strong>(d)</strong> A is false, but R is true.</p>
          </div>
        </details>

        <!-- AR 5 -->
        <details class="ans-box">
          <summary>
            <span><span class="step-pill">A&R 5</span> Assertion: The Penrose Triangle is an impossible 3D object that can only exist as a 2D drawing.</span>
          </summary>
          <div class="ans-content">
            <p><strong>Assertion (A):</strong> The Penrose Triangle is an impossible 3D object that can only exist as a 2D drawing.<br>
            <strong>Reason (R):</strong> Isometric projection lacks vanishing points and perspective convergence, allowing disjoint 3D beam ends to appear to touch on 2D paper.</p>
            <div class="ans-step">
              <div class="ans-step-title">Evaluation</div>
              <p>• Assertion (A) is true: A closed rigid triangle cannot have three 90° angles in 3D Euclidean space.<br>
              • Reason (R) is true and accurately explains why the 2D isometric drawing tricks the brain into perceiving closure.</p>
            </div>
            <p><strong>Correct Option:</strong> <strong>(a)</strong> Both A and R are true, and R is the correct explanation of A.</p>
          </div>
        </details>
      </div>

      <!-- PART 5.3: SHORT ANSWER QUESTIONS (6 QUESTIONS - 2M / 3M) -->
      <div class="concept-card">
        <h3 class="concept-card-title"><i class="fa-solid fa-pen-ruler"></i> 5.3 Short Answer Question Bank (2-Mark & 3-Mark Questions)</h3>
        <p>Bulleted model answers with explicit step-by-step CBSE marking schemes.</p>

        <!-- SA 1 -->
        <details class="ans-box">
          <summary>
            <span><span class="step-pill">2 Marks</span> SA 1: Define a fractal and state two prominent examples of fractals found in nature.</span>
          </summary>
          <div class="ans-content">
            <div class="ans-step">
              <div class="ans-step-title">Model Answer</div>
              <p>• <strong>Definition:</strong> A fractal is a geometric shape that exhibits <strong>self-similarity</strong>, meaning that smaller parts of the shape resemble the whole shape at smaller and smaller scales. <em>[1 Mark]</em><br>
              • <strong>Natural Examples:</strong>
              <br>1. <strong>Fern Frond:</strong> Each leaflet replicates the shape of the entire frond, and smaller pinnules replicate the leaflet.
              <br>2. <strong>Romanesco Broccoli:</strong> Each conical bud is composed of smaller self-similar conical buds arranged in logarithmic spirals. <em>[1 Mark]</em></p>
            </div>
            <p><strong>Marking Scheme:</strong> 1 Mark for definition highlighting self-similarity; 1 Mark for two valid natural examples.</p>
          </div>
        </details>

        <!-- SA 2 -->
        <details class="ans-box">
          <summary>
            <span><span class="step-pill">2 Marks</span> SA 2: In the Sierpinski Gasket, calculate the number of remaining triangles (R₄) and cumulative holes (H₄) at Step 4.</span>
          </summary>
          <div class="ans-content">
            <div class="ans-step">
              <div class="ans-step-title">Model Answer</div>
              <p>• <strong>Step 1 (Formula Identification):</strong>
              <br>Number of remaining triangles: <span class="math-inline">Rₙ = 3ⁿ</span>.
              <br>Cumulative holes: <span class="math-inline">Hₙ = (3ⁿ - 1) / 2</span>. <em>[0.5 Mark]</em><br>
              • <strong>Step 2 (Calculation for n = 4):</strong>
              <br><span class="math-inline">R₄ = 3⁴ = 81  triangles</span>. <em>[0.75 Mark]</em>
              <br><span class="math-inline">H₄ = (3⁴ - 1) / 2 = (81 - 1) / 2 = 80 / 2 = 40  holes</span>. <em>[0.75 Mark]</em></p>
            </div>
            <p><strong>Final Answer:</strong> <span class="math-inline">R₄ = 81</span> remaining triangles and <span class="math-inline">H₄ = 40</span> removed holes.</p>
          </div>
        </details>

        <!-- SA 3 -->
        <details class="ans-box">
          <summary>
            <span><span class="step-pill">3 Marks</span> SA 3: State Euler's Formula for polyhedra and verify it for a Hexagonal Prism.</span>
          </summary>
          <div class="ans-content">
            <div class="ans-step">
              <div class="ans-step-title">Model Answer</div>
              <p>• <strong>Statement:</strong> For any convex polyhedron, the number of Faces (<span class="math-inline">F</span>), Vertices (<span class="math-inline">V</span>), and Edges (<span class="math-inline">E</span>) satisfies the invariant relation:
              <br><span class="math-inline">F + V - E = 2</span> (or <span class="math-inline">F + V = E + 2</span>). <em>[1 Mark]</em><br>
              • <strong>Hexagonal Prism Parameters (n = 6):</strong>
              <br>• Faces: 2 hexagonal bases + 6 rectangular sides: <span class="math-inline">F = 6 + 2 = 8</span>. <em>[0.5 Mark]</em>
              <br>• Vertices: 6 on top + 6 on bottom: <span class="math-inline">V = 2 × 6 = 12</span>. <em>[0.5 Mark]</em>
              <br>• Edges: 6 on top + 6 on bottom + 6 vertical: <span class="math-inline">E = 3 × 6 = 18</span>. <em>[0.5 Mark]</em><br>
              • <strong>Verification:</strong>
              <br><span class="math-inline">F + V - E = 8 + 12 - 18 = 20 - 18 = 2</span>.
              <br>Since the result is exactly 2, Euler's formula is verified! <em>[0.5 Mark]</em></p>
            </div>
          </div>
        </details>

        <!-- SA 4 -->
        <details class="ans-box">
          <summary>
            <span><span class="step-pill">3 Marks</span> SA 4: Explain why a 2 × 2 cluster of 4 squares can never form part of a valid net of a cube.</span>
          </summary>
          <div class="ans-content">
            <div class="ans-step">
              <div class="ans-step-title">Model Answer</div>
              <p>• <strong>Geometric Reason:</strong> In a 2 × 2 cluster of 4 squares, four squares meet at a single central interior vertex. <em>[1 Mark]</em><br>
              • <strong>Folding Conflict:</strong> In a 3D cube, exactly <strong>three</strong> faces meet at every vertex at 90° angles (<span class="math-inline">90° + 90° + 90° = 270° &lt; 360°</span>). When the 4 squares sharing a vertex are folded along their edges to form 90° dihedral angles, the fourth square is forced to fold directly onto one of the other three squares. <em>[1 Mark]</em><br>
              • <strong>Consequence:</strong> Two squares overlap each other, leaving one of the 6 sides of the cube completely uncovered and open. Therefore, any hexamino with a 2 × 2 square block is an invalid net. <em>[1 Mark]</em></p>
            </div>
          </div>
        </details>

        <!-- SA 5 -->
        <details class="ans-box">
          <summary>
            <span><span class="step-pill">2 Marks</span> SA 5: Distinguish between the shadows cast by a handheld torch and the shadows cast by the Sun.</span>
          </summary>
          <div class="ans-content">
            <div class="ans-step">
              <div class="ans-step-title">Model Answer</div>
              <p>• <strong>Torch Shadow:</strong> A torch acts as a nearby point source. Its light rays <strong>diverge</strong> radially outwards, casting a shadow that is magnified, stretched, and perspective-distorted depending on distance. <em>[1 Mark]</em><br>
              • <strong>Sun Shadow:</strong> The Sun is located ~150 million km away. Because of this astronomical distance, sunlight rays reaching Earth are effectively <strong>perfectly parallel</strong>. When striking a surface perpendicularly, sun shadows represent true <strong>orthographic projections</strong> with no perspective magnification. <em>[1 Mark]</em></p>
            </div>
          </div>
        </details>

        <!-- SA 6 -->
        <details class="ans-box">
          <summary>
            <span><span class="step-pill">3 Marks</span> SA 6: Name the 3 principal views in orthographic projection and specify which dimensions (Length, Height, Depth) each view captures.</span>
          </summary>
          <div class="ans-content">
            <div class="ans-step">
              <div class="ans-step-title">Model Answer</div>
              <p>• <strong>1. Front View (Elevation):</strong> Projected onto the Vertical Plane from the front. It captures <strong>Length</strong> and <strong>Height</strong>. <em>[1 Mark]</em><br>
              • <strong>2. Top View (Plan):</strong> Projected onto the Horizontal Plane from directly above. It captures <strong>Length</strong> and <strong>Depth</strong>. <em>[1 Mark]</em><br>
              • <strong>3. Side View (Profile):</strong> Projected onto the Side Profile Plane from the side. It captures <strong>Depth</strong> and <strong>Height</strong>. <em>[1 Mark]</em></p>
            </div>
          </div>
        </details>
      </div>
    </section>
"""
