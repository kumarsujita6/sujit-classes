# -*- coding: utf-8 -*-
"""
Section 6 Module: Exam Hall Trap Alerts, 15 Master Revision Points,
Interactive Scripts & HTML Footer
Class 8 Mathematics Chapter 11: Exploring Some Geometric Themes
"""

def get_section_6():
    return """
    <!-- SECTION 6: EXAM HALL TRAP ALERTS & REVISION POINTS -->
    <section id="section6" class="section-box">
      <div class="section-header">
        <div class="section-header-left">
          <span class="section-tag">Score Maximization</span>
          <h2 class="section-title">§ 6. Exam Hall Trap Alerts & 15 Master Revision Points</h2>
          <p class="section-desc">
            Five critical misconceptions that cost students marks in board exams, paired with 15 rapid-recap bullet points for last-minute revision.
          </p>
        </div>
        <div>
          <span class="badge badge-gold"><i class="fa-solid fa-triangle-exclamation"></i> 5 Blunders & 15 Facts</span>
        </div>
      </div>

      <!-- 5 EXAM HALL TRAP ALERTS -->
      <div class="concept-card">
        <h3 class="concept-card-title"><i class="fa-solid fa-shield-halved"></i> 6.1 Top 5 Student Blunders (Pitfall vs Pro-Tip)</h3>

        <!-- BLUNDER 1 -->
        <div class="callout callout-warn">
          <div class="callout-title"><i class="fa-solid fa-circle-xmark"></i> Trap 1: Confusing Remaining Squares (Rₙ) with Cumulative Holes (Hₙ)</div>
          <p>
            <strong>The Common Blunder:</strong> When asked to find the number of holes at Step 2 in the Sierpinski Carpet, students often write <span class="math-inline">8² = 64</span>!
            <br><strong>The Mathematical Reality:</strong> 64 is the number of <em>remaining solid squares</em> (<span class="math-inline">R₂ = 8² = 64</span>). The number of holes is the cumulative sum of holes removed: Step 1 removed 1 hole; Step 2 removed 8 new holes; so total holes = <span class="math-inline">1 + 8 = 9  holes</span>!
            <br><span style="color: var(--emerald); font-weight: 700;">★ Pro-Tip:</span> Memorize the distinct formulas: <span class="math-inline">Rₙ = 8ⁿ</span>, whereas <span class="math-inline">Hₙ = (8ⁿ - 1) / 7</span>!
          </p>
        </div>

        <!-- BLUNDER 2 -->
        <div class="callout callout-warn">
          <div class="callout-title"><i class="fa-solid fa-circle-xmark"></i> Trap 2: Believing the Koch Snowflake Encloses an Infinite Area</div>
          <p>
            <strong>The Common Blunder:</strong> Students reason: <em>"Because the perimeter grows by 4/3 at every step and approaches infinity, the enclosed area must also grow to infinity!"</em>
            <br><strong>The Mathematical Reality:</strong> The perimeter does approach infinity (<span class="math-inline">Pₙ = 3s · (4/3)ⁿ → ∞</span>), but the area additions shrink so rapidly that the total area forms a converging geometric series: <span class="math-inline">A_{∞} = 1.6 · A₀</span>! The entire infinite snowflake can fit completely inside a circle drawn around the original triangle!
            <br><span style="color: var(--emerald); font-weight: 700;">★ Pro-Tip:</span> Infinite boundary does NOT imply infinite area! You can hold the Koch Snowflake in your palm.
          </p>
        </div>

        <!-- BLUNDER 3 -->
        <div class="callout callout-warn">
          <div class="callout-title"><i class="fa-solid fa-circle-xmark"></i> Trap 3: Drawing Surface Geodesic Paths Across Empty Space Off the Net</div>
          <p>
            <strong>The Common Blunder:</strong> When solving the Ant & Laddu problem, students draw a straight line between the two points on the very first net unfolding they sketch, without checking if the line stays within the paper boundary!
            <br><strong>The Mathematical Reality:</strong> If a straight line on an unfolded net passes through empty white space (as on textbook page 86), that line corresponds to an ant jumping through thin air, which violates the problem constraint of crawling strictly on the surface!
            <br><span style="color: var(--emerald); font-weight: 700;">★ Pro-Tip:</span> Always test multiple unfolding configurations. A valid geodesic line must lie 100% inside the contiguous unfolded face polygons.
          </p>
        </div>

        <!-- BLUNDER 4 -->
        <div class="callout callout-warn">
          <div class="callout-title"><i class="fa-solid fa-circle-xmark"></i> Trap 4: Assuming Parallel Projections Can Destroy Parallelism</div>
          <p>
            <strong>The Common Blunder:</strong> Thinking that because perspective drawing causes railroad tracks to converge to a point on the horizon, parallel sunlight shadows also converge into a trapezium.
            <br><strong>The Mathematical Reality:</strong> In orthographic and parallel projections, parallel projection rays ensure that <strong>parallel lines always remain strictly parallel</strong>! A square or parallelogram can NEVER project into a trapezium.
            <br><span style="color: var(--emerald); font-weight: 700;">★ Pro-Tip:</span> If an exam question asks whether a parallelogram's shadow under sunlight can be a trapezium, answer an emphatic <strong>NO</strong>!
          </p>
        </div>

        <!-- BLUNDER 5 -->
        <div class="callout callout-warn">
          <div class="callout-title"><i class="fa-solid fa-circle-xmark"></i> Trap 5: Counting the 2 × 2 Square Cluster as a Cube Net</div>
          <p>
            <strong>The Common Blunder:</strong> Students see 6 connected squares and assume any arrangement of 6 squares can fold into a cube.
            <br><strong>The Mathematical Reality:</strong> Out of 35 distinct hexaminoes, only <strong>11 nets</strong> are valid! Any net containing a 2 × 2 block of squares forces two faces to overlap, leaving an opposite face open.
            <br><span style="color: var(--emerald); font-weight: 700;">★ Pro-Tip:</span> The 11 valid nets fall strictly into 1-4-1 (6 nets), 1-3-2 (3 nets), 2-2-2 (1 net), and 3-3 (1 net). Spot the 2×2 cluster to immediately eliminate invalid options!
          </p>
        </div>
      </div>

      <!-- 15 MASTER REVISION POINTS -->
      <div class="concept-card">
        <h3 class="concept-card-title"><i class="fa-solid fa-list-ol"></i> 6.2 15 High-Yield Master Revision Points</h3>
        <ol style="margin-left: 1.5rem; line-height: 1.9; font-size: 0.95rem; color: var(--text-main);">
          <li><strong>Fractal Definition:</strong> A geometric shape that exhibits self-similarity at smaller and smaller scales, coined by Benoit Mandelbrot in 1975 from Latin <em>fractus</em>.</li>
          <li><strong>Natural Fractals:</strong> Fern leaves, Romanesco broccoli logarithmic spirals, river deltas, lightning discharges, clouds, and coastlines.</li>
          <li><strong>Sierpinski Carpet Formulas:</strong> <span class="math-inline">Rₙ = 8ⁿ</span> remaining squares; cumulative holes <span class="math-inline">Hₙ = (8ⁿ - 1)/7</span>; area <span class="math-inline">Aₙ = (8/9)ⁿ · A₀</span> (approaches 0 as <span class="math-inline">n → ∞</span>).</li>
          <li><strong>Sierpinski Gasket Formulas:</strong> <span class="math-inline">Rₙ = 3ⁿ</span> triangles; holes <span class="math-inline">Hₙ = (3ⁿ - 1)/2</span>; area <span class="math-inline">Aₙ = (3/4)ⁿ · A₀ → 0</span>; perimeter <span class="math-inline">Pₙ = 3s · (1.5)ⁿ → ∞</span>.</li>
          <li><strong>Koch Snowflake Formulas:</strong> <span class="math-inline">Nₙ = 3 · 4ⁿ</span> sides; side length <span class="math-inline">Lₙ = s / 3ⁿ</span>; perimeter <span class="math-inline">Pₙ = 3s · (4/3)ⁿ → ∞</span>; area converges to exactly <span class="math-inline">1.6 · A₀</span>.</li>
          <li><strong>Temple Architecture:</strong> Kandariya Mahadev Temple at Khajuraho (c. 1025 CE) embodies fractal geometry with 84 urushringas replicating the central shikhara, symbolizing cosmic infinity (Brahman).</li>
          <li><strong>Escher's Fractal Art:</strong> M.C. Escher's woodcut <em>‘Smaller and Smaller’</em> tiles self-similar lizards that halve in size towards the center.</li>
          <li><strong>Dissection Law:</strong> Slicing corners between edge midpoints turns a square of area <span class="math-inline">A</span> into a 45° rotated square of area <span class="math-inline">A/2</span>; slicing thirds of an equilateral triangle produces a regular hexagon.</li>
          <li><strong>Polyhedra Definitions:</strong> Solids bounded entirely by flat plane polygonal surfaces. Cylinders, cones, and spheres are curved solids, NOT polyhedra.</li>
          <li><strong>Prisms vs Pyramids:</strong> For <span class="math-inline">n</span>-gon base: Prism has <span class="math-inline">F = n+2, V = 2n, E = 3n</span>; Pyramid has <span class="math-inline">F = n+1, V = n+1, E = 2n</span>.</li>
          <li><strong>Euler's Invariant:</strong> For all convex polyhedra, <span class="math-inline">F + V - E = 2</span> (Faces + Vertices - Edges = 2).</li>
          <li><strong>Cube & Platonic Nets:</strong> A cube has exactly <strong>11 nets</strong>; a regular tetrahedron has <strong>2 nets</strong>; a regular octahedron has <strong>11 nets</strong>; a dodecahedron has <strong>43,380 nets</strong>; a sphere has <strong>0 flat nets</strong>.</li>
          <li><strong>Surface Geodesics:</strong> The shortest path between two points on a cuboid surface corresponds to a straight line on an unfolded 2D net, computed via Baudhāyana-Pythagoras theorem (<span class="math-inline">d = √(Δx² + Δy²)</span>).</li>
          <li><strong>Orthographic Invariant:</strong> The projection of a line segment satisfies <span class="math-inline">0 ≤ p ≤ l</span> (equality holds only when parallel). Parallel lines in 3D space ALWAYS project to parallel lines on 2D planes.</li>
          <li><strong>Isometric Grid Principles:</strong> 'Isometric' means equal measure. The 3 coordinate axes are oriented at 120° angles to each other, preserving true 1:1 scale along length, depth, and height without perspective vanishing points.</li>
        </ol>
      </div>
    </section>

    <!-- Page Footer -->
    <footer class="page-footer">
      <div class="footer-content">
        <div class="footer-col">
          <h4>Sujit Classes</h4>
          <p>
            Pioneering conceptual clarity, mathematical rigor, and joyful deep learning for school students across Odisha in English and Odia Medium.
          </p>
        </div>
        <div class="footer-col">
          <h4>Class 8 Mathematics</h4>
          <ul class="footer-links">
            <li><a href="math-ch1-a-square-and-a-cube.html">Ch 1: A Square and a Cube</a></li>
            <li><a href="math-ch2-power-play.html">Ch 2: Power Play</a></li>
            <li><a href="math-ch3-a-story-of-numbers.html">Ch 3: A Story of Numbers</a></li>
            <li><a href="math-ch4-quadrilaterals.html">Ch 4: Quadrilaterals</a></li>
            <li><a href="math-ch7-proportional-reasoning-1.html">Ch 7: Proportional Reasoning - 1</a></li>
            <li><a href="math-ch9-the-baudhayana-pythagoras-theorem.html">Ch 9: The Baudhāyana-Pythagoras Theorem</a></li>
            <li><a href="math-ch10-proportional-reasoning-2.html">Ch 10: Proportional Reasoning - 2</a></li>
            <li><a href="math-ch11-exploring-some-geometric-themes.html" style="color: #818cf8; font-weight: 700;">Ch 11: Exploring Some Geometric Themes</a></li>
          </ul>
        </div>
        <div class="footer-col">
          <h4>Quick Navigation</h4>
          <ul class="footer-links">
            <li><a href="../../index.html"><i class="fa-solid fa-house"></i> Home Portal</a></li>
            <li><a href="#section1">§ 1. Visual Blueprint</a></li>
            <li><a href="#section2">§ 2. Concepts & Vocab</a></li>
            <li><a href="#section3">§ 3. Formula Bank</a></li>
            <li><a href="#section4">§ 4. Solved NCERT</a></li>
            <li><a href="#section5">§ 5. Exam Bank</a></li>
            <li><a href="#section6">§ 6. Trap Alerts</a></li>
          </ul>
        </div>
      </div>
      <div class="footer-bottom">
        <p>© 2026 Sujit Classes. All Rights Reserved. NEP 2020 Aligned Master Study System.</p>
      </div>
    </footer>
  </div> <!-- end container -->

  <!-- INTERACTIVE SCRIPTS -->
  <script>
    /* ----------------------------------------------------------
       1. READING PROGRESS BAR
       ---------------------------------------------------------- */
    window.addEventListener('scroll', () => {
      const winScroll = document.body.scrollTop || document.documentElement.scrollTop;
      const height = document.documentElement.scrollHeight - document.documentElement.clientHeight;
      const scrolled = (winScroll / height) * 100;
      const bar = document.getElementById('progressBar');
      if (bar) {
        bar.style.width = scrolled + '%';
      }
    });

    /* ----------------------------------------------------------
       2. INTERACTIVE MCQ QUIZ ENGINE
       ---------------------------------------------------------- */
    let quizScore = 0;
    const answeredQuestions = new Set();

    function evaluateMCQ(qNum, selectedOption, isCorrect, feedbackText) {
      const card = document.getElementById('mcqCard' + qNum);
      const feedback = document.getElementById('feedback' + qNum);
      if (!card || !feedback) return;

      if (answeredQuestions.has(qNum)) return;
      answeredQuestions.add(qNum);

      const buttons = card.querySelectorAll('.option-btn');
      buttons.forEach(btn => {
        btn.disabled = true;
        btn.style.cursor = 'default';
        const optBadge = btn.querySelector('.pos-badge');
        if (optBadge) {
          const optLetter = optBadge.innerText.trim();
          if (optLetter === selectedOption) {
            if (isCorrect) {
              btn.classList.add('selected-correct');
              btn.innerHTML += ' <i class="fa-solid fa-circle-check" style="margin-left: auto; color: #059669;"></i>';
            } else {
              btn.classList.add('selected-wrong');
              btn.innerHTML += ' <i class="fa-solid fa-circle-xmark" style="margin-left: auto; color: #dc2626;"></i>';
            }
          }
        }
      });

      feedback.className = 'trap-feedback show ' + (isCorrect ? 'correct-feedback' : 'wrong-feedback');
      feedback.innerHTML = '<strong>' + (isCorrect ? '✓ Correct! ' : '✗ Conceptual Trap! ') + '</strong>' + feedbackText;

      if (isCorrect) {
        quizScore++;
      }
      const scoreDisplay = document.getElementById('quizScoreDisplay');
      if (scoreDisplay) {
        scoreDisplay.innerHTML = '<i class="fa-solid fa-trophy"></i> Score: ' + quizScore + ' / 5';
      }
    }

    /* ----------------------------------------------------------
       3. TEXT-TO-SPEECH (AUDIO TEACHER READER)
       ---------------------------------------------------------- */
    const synth = window.speechSynthesis;
    let currentUtterance = null;
    let isPlayingAudio = false;
    let speechRate = 1.0;

    const chapterSummarySpeechText = 
      "Welcome to Class 8 Mathematics Chapter 11: Exploring Some Geometric Themes, based on the NCERT Ganita Prakash curriculum. " +
      "In this chapter, we explore two grand geometric themes: the infinite world of self-similar fractals and the spatial visualization of three-dimensional solids. " +
      "We begin with fractals, shapes where every smaller fragment resembles the entire object, seen in fern leaves, Romanesco broccoli, clouds, and coastlines. " +
      "In mathematics, the Sierpinski Carpet repeatedly removes central ninths from a square: remaining squares equal 8 to the power n, and area decays to zero. " +
      "The Sierpinski Gasket repeatedly removes inverted triangles: remaining triangles equal 3 to the power n, area approaches zero, but perimeter approaches infinity! " +
      "The Koch Snowflake adds triangular bumps onto equilateral sides: number of sides equals 3 times 4 to the power n, creating an infinite perimeter enclosing a strictly finite area of 1.6 times the original triangle. " +
      "We discover fractal beauty in ancient Indian temple architecture, such as the Kandariya Mahadev temple in Khajuraho with 84 mini spires, in African Fulani wedding blankets, and in M.C. Escher's woodcuts. " +
      "In the second theme, we visualize 3D solids. A cylinder shows circular and rectangular profiles; a cone shows circular and triangular profiles. " +
      "For polyhedra, prisms have faces equal to n plus 2, vertices equal to 2n, and edges equal to 3n. Pyramids have faces and vertices equal to n plus 1, and edges equal to 2n. Both obey Euler's formula: Faces plus Vertices minus Edges equals 2. " +
      "We examine flat nets: a cube has exactly 11 distinct nets, but an arrangement with a 2 by 2 cluster of squares can never form a cube. By Gauss's theorem, a sphere can never have a flat net. " +
      "To find the shortest surface path for an ant to reach a laddu on a cuboid, we unfold the faces into a 2D net and draw a straight line using the Baudhāyana-Pythagoras theorem. In the 30 by 12 by 12 centimeter box, the shortest path is 40 centimeters. " +
      "Finally, in orthographic projection, parallel lines always remain parallel, and length satisfies p less than or equal to l. On an isometric grid, three axes are spaced at 120 degrees, allowing true-scale drafting and explaining why the Penrose Triangle illusion deceives the human brain. " +
      "Review the solved exercises, practice the exam question bank, avoid common traps, and achieve excellence with Sujit Classes!";

    function toggleAudioReader() {
      const btn = document.getElementById('ttsPlayBtn');
      const icon = document.getElementById('ttsIcon');
      const status = document.getElementById('ttsStatus');

      if (!synth) {
        if (status) status.innerText = "Speech synthesis is not supported on this browser.";
        return;
      }

      if (isPlayingAudio) {
        synth.cancel();
        isPlayingAudio = false;
        if (icon) icon.className = "fa-solid fa-play";
        if (status) status.innerText = "Audio paused. Click Play to resume teacher narration.";
      } else {
        synth.cancel();
        currentUtterance = new SpeechSynthesisUtterance(chapterSummarySpeechText);
        currentUtterance.rate = speechRate;
        currentUtterance.pitch = 1.0;
        currentUtterance.lang = 'en-US';

        currentUtterance.onend = function() {
          isPlayingAudio = false;
          if (icon) icon.className = "fa-solid fa-play";
          if (status) status.innerText = "Narration completed. Click Play to listen again.";
        };

        currentUtterance.onerror = function() {
          isPlayingAudio = false;
          if (icon) icon.className = "fa-solid fa-play";
          if (status) status.innerText = "Audio playback interrupted.";
        };

        synth.speak(currentUtterance);
        isPlayingAudio = true;
        if (icon) icon.className = "fa-solid fa-pause";
        if (status) status.innerText = "Playing audio narration... Listen attentively to key concepts.";
      }
    }

    function updateSpeechRate() {
      const select = document.getElementById('ttsRate');
      if (select) {
        speechRate = parseFloat(select.value);
        if (isPlayingAudio) {
          toggleAudioReader();
          toggleAudioReader();
        }
      }
    }
  </script>
</body>
</html>
"""
