# -*- coding: utf-8 -*-
"""Part 9: Section 6 - Exam Hall Trap Alerts, 15 Revision Points, Footer & Scripts."""

SECTION6_FOOTER_CONTENT = """
    <!-- SECTION 6: EXAM HALL TRAP ALERTS & 15 RAPID REVISION POINTS -->
    <section id="traps-revision" class="section-card">
      <div class="section-header">
        <div class="section-icon-box">
          <i class="fa-solid fa-triangle-exclamation"></i>
        </div>
        <div>
          <h2 class="section-title">Section 6: Exam Hall Trap Alerts &amp; 15 Revision Points</h2>
          <p class="section-tagline">Critical student blunders to avoid in board exams and high-yield memory anchors for rapid test revision</p>
        </div>
      </div>

      <!-- 5 COMMON EXAM HALL TRAP ALERTS -->
      <h3 class="subheading"><i class="fa-solid fa-bomb"></i> 5 Common Exam Hall Trap Alerts</h3>
      <p>
        Examiners intentionally design questions to catch common student misunderstandings. Study these 5 classic traps and their side-by-side corrections to ensure you never lose marks:
      </p>

      <!-- TRAP 1 -->
      <div class="trap-card">
        <div class="trap-title"><i class="fa-solid fa-circle-exclamation"></i> Trap 1: Forgetting the "Coplanar" Condition in Parallel Lines</div>
        <p>Many students define parallel lines simply as "lines that never meet". On rigorous CBSE and state board exams, this loses 1 full mark!</p>
        <div class="trap-grid">
          <div class="wrong-box">
            <div class="box-label"><i class="fa-solid fa-xmark"></i> Wrong Way (Loses Marks)</div>
            "Parallel lines are two straight lines that never intersect however far they are extended." (Incomplete! Skew lines in 3D never meet but are NOT parallel).
          </div>
          <div class="right-box">
            <div class="box-label"><i class="fa-solid fa-check"></i> Right Way (Full Marks)</div>
            "Parallel lines are straight lines <strong>lying on the same flat plane (coplanar)</strong> that never intersect however far they are extended in either direction."
          </div>
        </div>
      </div>

      <!-- TRAP 2 -->
      <div class="trap-card">
        <div class="trap-title"><i class="fa-solid fa-circle-exclamation"></i> Trap 2: Equating Alternate or Corresponding Angles Without Parallel Lines</div>
        <p>Students see a transversal and immediately write <span class="math-inline">∠1 = ∠5</span> or <span class="math-inline">∠4 = ∠6</span>, forgetting to check if the problem actually states the lines are parallel!</p>
        <div class="trap-grid">
          <div class="wrong-box">
            <div class="box-label"><i class="fa-solid fa-xmark"></i> Wrong Way (Blunder)</div>
            Assuming <span class="math-inline">∠4 = ∠6</span> simply because they form a "Z-shape", even when lines are not parallel.
          </div>
          <div class="right-box">
            <div class="box-label"><i class="fa-solid fa-check"></i> Right Way (Precise Logic)</div>
            Always write: <em>"Since line l ∥ line m and t is a transversal, alternate interior angles are equal: ∠4 = ∠6."</em> If lines are not parallel, alternate angles are NOT equal!
          </div>
        </div>
      </div>

      <!-- TRAP 3 -->
      <div class="trap-card">
        <div class="trap-title"><i class="fa-solid fa-circle-exclamation"></i> Trap 3: Confusing Supplementary (180°) with Complementary (90°)</div>
        <p>In the rush of the exam, students confuse these two terms and write <span class="math-inline">x + y = 90°</span> for consecutive interior angles.</p>
        <div class="trap-grid">
          <div class="wrong-box">
            <div class="box-label"><i class="fa-solid fa-xmark"></i> Wrong Way (Costly Slip)</div>
            Writing: "Consecutive interior angles are complementary, so <span class="math-inline">∠3 + ∠6 = 90°</span>." (Completely incorrect formula!).
          </div>
          <div class="right-box">
            <div class="box-label"><i class="fa-solid fa-check"></i> Right Way (Memory Trick)</div>
            Remember alphabetical order: <strong>C</strong> comes before <strong>S</strong>, and <strong>90°</strong> comes before <strong>180°</strong>!<br>
            • <strong>C</strong>omplementary = <strong>90°</strong><br>
            • <strong>S</strong>upplementary = <strong>180°</strong>
          </div>
        </div>
      </div>

      <!-- TRAP 4 -->
      <div class="trap-card">
        <div class="trap-title"><i class="fa-solid fa-circle-exclamation"></i> Trap 4: Assuming Consecutive Interior Angles are Equal</div>
        <p>Because alternate interior angles are equal, students carelessly assume that interior angles on the same side must also be equal.</p>
        <div class="trap-grid">
          <div class="wrong-box">
            <div class="box-label"><i class="fa-solid fa-xmark"></i> Wrong Way (Calculation Blunder)</div>
            Writing: <span class="math-inline">∠3 = ∠6</span>. (If ∠3 is 50°, student mistakenly concludes ∠6 is 50°!).
          </div>
          <div class="right-box">
            <div class="box-label"><i class="fa-solid fa-check"></i> Right Way (True Formula)</div>
            Consecutive interior angles are <strong>supplementary</strong>, NOT equal:<br>
            <span class="math-inline">∠3 + ∠6 = 180° ⇒ 50° + ∠6 = 180° ⇒ ∠6 = 130°</span>. (They are only equal if both are 90°).
          </div>
        </div>
      </div>

      <!-- TRAP 5 -->
      <div class="trap-card">
        <div class="trap-title"><i class="fa-solid fa-circle-exclamation"></i> Trap 5: Identifying Alternate Angles as Adjacent Angles</div>
        <p>Selecting angles that lie on opposite sides of the transversal but share a common arm along the same line.</p>
        <div class="trap-grid">
          <div class="wrong-box">
            <div class="box-label"><i class="fa-solid fa-xmark"></i> Wrong Way (Confusion)</div>
            Calling <span class="math-inline">∠3</span> and <span class="math-inline">∠4</span> alternate angles. (They are adjacent angles forming a linear pair at the same vertex!).
          </div>
          <div class="right-box">
            <div class="box-label"><i class="fa-solid fa-check"></i> Right Way (Accurate Identification)</div>
            Alternate interior angles must be at <strong>different vertices</strong> along the transversal (<span class="math-inline">∠3</span> at top vertex and <span class="math-inline">∠5</span> at bottom vertex, forming the "Z" shape).
          </div>
        </div>
      </div>

      <!-- 15 RAPID REVISION POINTS -->
      <h3 class="subheading"><i class="fa-solid fa-list-ol"></i> 15 High-Yield Rapid Revision Points</h3>
      <p>
        Read through these 15 bulleted power points 10 minutes before entering your examination hall for instant recall:
      </p>

      <div style="background: #f8fafc; border: 1px solid var(--border); border-radius: var(--radius-lg); padding: 1.75rem; margin-top: 1rem;">
        <ol style="margin-left: 1.5rem; line-height: 2;">
          <li><strong>Plane Surface:</strong> A flat, two-dimensional surface extending endlessly with zero thickness (tabletop, blackboard, paper).</li>
          <li><strong>Intersection Axiom:</strong> Two distinct straight lines in a plane can intersect at <strong>at most one single point</strong>.</li>
          <li><strong>Linear Pair Theorem:</strong> Adjacent angles formed along a straight line always add up to <strong>180°</strong>.</li>
          <li><strong>Vertically Opposite Angles:</strong> Non-adjacent opposite angles across an intersection vertex are <strong>always equal</strong>.</li>
          <li><strong>Perpendicular Lines:</strong> When two intersecting lines form four equal angles, each angle is exactly <strong>90°</strong> (<span class="math-inline">l ⊥ m</span>).</li>
          <li><strong>Parallel Lines:</strong> Coplanar straight lines that remain at constant distance apart and <strong>never meet</strong> however far extended (<span class="math-inline">l ∥ m</span>).</li>
          <li><strong>Skew Lines Warning:</strong> Non-coplanar lines in 3D that never meet are called skew lines and are NOT parallel.</li>
          <li><strong>Paper Folding Law:</strong> Folding a paper sheet horizontally <span class="math-inline">n</span> times produces exactly <span class="math-inline">2ⁿ + 1</span> parallel lines.</li>
          <li><strong>Transversal Definition:</strong> A line intersecting two or more distinct lines at separate points, generating <strong>8 angles</strong>.</li>
          <li><strong>Max-4 Angle Law:</strong> A transversal cutting two lines can form a maximum of <strong>4 distinct angle measures</strong> (or 2 when lines are parallel).</li>
          <li><strong>Corresponding Angles (F-Shape):</strong> Occupy matching relative corner positions; they are equal if and only if lines are parallel.</li>
          <li><strong>Alternate Interior Angles (Z-Shape):</strong> Lie on opposite sides of the transversal between the lines; they are equal if and only if lines are parallel.</li>
          <li><strong>Consecutive Interior Angles (C-Shape):</strong> Lie on the same side of the transversal between the lines; they sum to <strong>180°</strong> if and only if lines are parallel.</li>
          <li><strong>Sliding Set-Square Principle:</strong> Sliding a set square along a stationary ruler preserves equal 90° corresponding angles, generating parallel lines.</li>
          <li><strong>Visual Illusions Cause:</strong> Geometric illusions (Hering, Zöllner) occur because the brain's visual cortex overestimates acute angles formed by intersecting lines.</li>
        </ol>
      </div>
    </section>

  </div> <!-- /container -->

  <!-- FOOTER -->
  <footer>
    <p style="font-weight: 700; color: #f8fafc; font-size: 1.1rem; margin-bottom: 0.5rem;">Sujit Classes Study Portal</p>
    <p style="font-size: 0.9rem; margin-bottom: 1rem;">Empowering CBSE &amp; BSE Odisha Students with Crystal-Clear Mathematical Master Notes</p>
    <p style="font-size: 0.85rem; color: #64748b;">NCERT Ganita Prakash Class 7 Mathematics | Chapter 5: Parallel and Intersecting Lines (NEP gegp105)</p>
    <p style="margin-top: 1.5rem;">
      <a href="../../index.html"><i class="fa-solid fa-house"></i> Return to Main Study Portal</a>
    </p>
  </footer>

  <!-- INTERACTIVE SCRIPTS: PROGRESS BAR, AUDIO READER, & QUIZ ENGINE -->
  <script>
    // 1. READING PROGRESS BAR
    window.addEventListener('scroll', () => {
      const winScroll = document.documentElement.scrollTop || document.body.scrollTop;
      const height = document.documentElement.scrollHeight - document.documentElement.clientHeight;
      const scrolled = (winScroll / height) * 100;
      document.getElementById('progressBar').style.width = scrolled + '%';
    });

    // 2. INTERACTIVE QUIZ ENGINE
    function checkQuiz(qId, selectedOption, isCorrect) {
      const card = document.getElementById('quiz-' + qId);
      const buttons = card.querySelectorAll('.option-btn');
      const feedback = document.getElementById('feedback-' + qId);

      // Disable all buttons once an option is selected
      buttons.forEach((btn, index) => {
        btn.disabled = true;
        if (index === selectedOption) {
          if (isCorrect) {
            btn.classList.add('correct');
            btn.innerHTML = '<i class="fa-solid fa-circle-check"></i> ' + btn.innerText;
          } else {
            btn.classList.add('wrong');
            btn.innerHTML = '<i class="fa-solid fa-circle-xmark"></i> ' + btn.innerText;
          }
        }
      });

      // Show feedback card
      feedback.classList.add('show');
      if (isCorrect) {
        feedback.classList.add('success');
      } else {
        feedback.classList.add('error');
      }
    }

    // 3. AUDIO READER (TEXT-TO-SPEECH)
    let isPlaying = false;
    let synth = window.speechSynthesis;
    let utterance = null;

    function toggleAudioReader() {
      const navBtnText = document.getElementById('navBtnText');

      if (!('speechSynthesis' in window)) {
        alert('Text-to-speech audio reader is not supported in this web browser.');
        return;
      }

      if (isPlaying) {
        synth.cancel();
        isPlaying = false;
        navBtnText.innerText = 'Listen Note';
      } else {
        const narrationText = "Welcome to Class 7 Mathematics Chapter 5 Master Study Notes on Parallel and Intersecting Lines from Sujit Classes. " +
          "When two lines intersect on a plane, they meet at a single point and form four angles. " +
          "Adjacent angles forming a straight line are linear pairs and add up to 180 degrees. " +
          "Opposite angles across the vertex are vertically opposite angles, and they are always equal. " +
          "When intersecting lines form four equal angles of 90 degrees, they are called perpendicular lines. " +
          "Lines that lie in the same flat plane and never meet however far extended are parallel lines. " +
          "A line cutting across two lines is called a transversal. " +
          "When lines are parallel, corresponding angles in the F-shape are equal, " +
          "alternate interior angles in the Z-shape are equal, " +
          "and consecutive interior angles on the same side in the C-shape add up to 180 degrees. " +
          "Explore every section below, inspect the interactive diagrams, and master all solved NCERT exercises and exam questions step by step.";

        utterance = new SpeechSynthesisUtterance(narrationText);
        utterance.rate = 0.95;
        utterance.pitch = 1.0;

        utterance.onend = function() {
          isPlaying = false;
          navBtnText.innerText = 'Listen Note';
        };

        utterance.onerror = function() {
          isPlaying = false;
          navBtnText.innerText = 'Listen Note';
        };

        synth.speak(utterance);
        isPlaying = true;
        navBtnText.innerText = 'Stop Audio';
      }
    }
  </script>
</body>
</html>
"""
