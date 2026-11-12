# -*- coding: utf-8 -*-
"""
Section 6: Exam Hall Trap Alerts, 15 High-Yield Revision Points & Interactive JavaScript Engine
for Class 8 Science Chapter 6: Pressure, Winds, Storms, and Cyclones
"""

def get_section6():
    return '''
    <!-- SECTION 6: EXAM HALL TRAP ALERTS & RAPID REVISION POINTS -->
    <section class="study-section" id="sec6">
      <div id="section-6"></div>
      <div class="section-header">
        <span class="section-tag">Exam Mastery &bull; Error Proofing</span>
        <h2 class="section-title">
          <i class="fa-solid fa-triangle-exclamation"></i>
          Section 6: Exam Hall Trap Alerts &amp; 15 High-Yield Revision Points
        </h2>
        <p class="section-desc">
          Identify common cognitive traps before they cost marks in the exam hall, and review the top 15 core concepts for quick revision.
        </p>
      </div>

      <!-- 5 COMMON EXAM HALL TRAP ALERTS -->
      <h3 class="subheading"><i class="fa-solid fa-radiation"></i> Top 5 Exam Hall Blunders (Don't Lose Marks Here!)</h3>

      <div class="callout callout-warn">
        <div class="callout-title"><i class="fa-solid fa-triangle-exclamation"></i> Trap 1: Confusing "Liquid Weight" with "Hydrostatic Pressure"</div>
        <p><strong>The Blunder:</strong> Believing that a wide vessel containing 50 litres of water exerts higher bottom pressure than a narrow tube containing 1 litre of water when both are filled to the same vertical depth of 1 metre.</p>
        <p><strong>The Correction:</strong> Total downward force is greater in the wide vessel (<span class="math-entity">F = P &times; A</span>), but hydrostatic pressure depends <strong>only on vertical depth</strong> (<span class="math-entity">P = h &times; &rho; &times; g</span>). If depth <span class="math-entity">h</span> and liquid density <span class="math-entity">&rho;</span> are identical, bottom pressure is identical!</p>
      </div>

      <div class="callout callout-warn">
        <div class="callout-title"><i class="fa-solid fa-triangle-exclamation"></i> Trap 2: Believing a Vacuum Has "Suction Power"</div>
        <p><strong>The Blunder:</strong> Writing in an exam that a rubber sucker sticks because "the vacuum inside pulls it to the wall," or that drinking through a straw works because "the lungs pull the liquid up."</p>
        <p><strong>The Correction:</strong> A vacuum is empty space; it cannot pull anything. Adhesion and straw operation are driven entirely by <strong>external atmospheric pressure pushing inward</strong> against the lower pressure inside the cavity.</p>
      </div>

      <div class="callout callout-warn">
        <div class="callout-title"><i class="fa-solid fa-triangle-exclamation"></i> Trap 3: Thinking High-Speed Winds "Push" Roofs Off</div>
        <p><strong>The Blunder:</strong> Stating that a storm blows a roof away because wind blows upward from underneath the eaves.</p>
        <p><strong>The Correction:</strong> High-speed wind sweeps <em>across the top</em> of the roof, lowering air pressure above it via Bernoulli's principle. Higher indoor atmospheric pressure pushes upward, lifting the roof off.</p>
      </div>

      <div class="callout callout-warn">
        <div class="callout-title"><i class="fa-solid fa-triangle-exclamation"></i> Trap 4: Assuming Rubber Tyres Insulate a Car from Lightning</div>
        <p><strong>The Blunder:</strong> Explaining vehicle lightning safety by stating that "rubber tyres insulate the car from the ground."</p>
        <p><strong>The Correction:</strong> Lightning that has traveled through thousands of metres of air is not stopped by a few centimetres of rubber. Safety is provided by the <strong>metallic outer chassis (Faraday Cage)</strong>, which routes current around passengers.</p>
      </div>

      <div class="callout callout-warn">
        <div class="callout-title"><i class="fa-solid fa-triangle-exclamation"></i> Trap 5: Thinking the Eye of a Cyclone Is the Most Dangerous Part</div>
        <p><strong>The Blunder:</strong> Writing that the eye of a cyclone has the highest winds and most dangerous storm conditions.</p>
        <p><strong>The Correction:</strong> The eye is a calm, cloudless, low-wind zone where dry air gently descends. The most dangerous sector is the <strong>Eye Wall</strong> encircling the eye.</p>
      </div>

      <!-- 15 RAPID REVISION POINTS -->
      <h3 class="subheading"><i class="fa-solid fa-bolt-lightning"></i> 15 High-Yield Rapid Revision Points</h3>
      <div class="concept-grid">
        <div class="concept-card">
          <div class="card-icon blue"><i class="fa-solid fa-1"></i></div>
          <h4 class="card-title">1. Pressure Definition</h4>
          <p>Pressure is thrust per unit area: <span class="math-entity">P = F / A</span>. The SI unit is Pascal (<span class="math-entity">Pa</span>) or <span class="math-entity">N/m&sup2;</span>.</p>
        </div>

        <div class="concept-card">
          <div class="card-icon blue"><i class="fa-solid fa-2"></i></div>
          <h4 class="card-title">2. Area Law</h4>
          <p>For a fixed force, smaller contact area increases pressure; larger area decreases pressure.</p>
        </div>

        <div class="concept-card">
          <div class="card-icon blue"><i class="fa-solid fa-3"></i></div>
          <h4 class="card-title">3. Liquid Depth Law</h4>
          <p>Hydrostatic pressure increases with depth: <span class="math-entity">P = h &times; &rho; &times; g</span>. It is independent of container shape or volume.</p>
        </div>

        <div class="concept-card">
          <div class="card-icon blue"><i class="fa-solid fa-4"></i></div>
          <h4 class="card-title">4. Omnidirectional Fluid Force</h4>
          <p>Liquids exert equal pressure in all directions at the same depth, including laterally on sidewalls.</p>
        </div>

        <div class="concept-card">
          <div class="card-icon blue"><i class="fa-solid fa-5"></i></div>
          <h4 class="card-title">5. Dam Base Engineering</h4>
          <p>Dam bases are built broad and thick to withstand high lateral hydrostatic pressure at deep reservoir levels.</p>
        </div>

        <div class="concept-card">
          <div class="card-icon blue"><i class="fa-solid fa-6"></i></div>
          <h4 class="card-title">6. Atmospheric Ocean</h4>
          <p>Standard sea-level air pressure is ~101.3 kPa, exerting ~2,250 N of downward force on a 15 cm &times; 15 cm area.</p>
        </div>

        <div class="concept-card">
          <div class="card-icon blue"><i class="fa-solid fa-7"></i></div>
          <h4 class="card-title">7. Biological Pressure Balance</h4>
          <p>Internal blood and fluid pressure balances external atmospheric pressure, preventing our bodies from collapsing.</p>
        </div>

        <div class="concept-card">
          <div class="card-icon blue"><i class="fa-solid fa-8"></i></div>
          <h4 class="card-title">8. Thermal Wind Engine</h4>
          <p>Solar heating expands air into rising low-pressure updrafts. Cooler air rushes in from high-pressure zones to create wind.</p>
        </div>

        <div class="concept-card">
          <div class="card-icon blue"><i class="fa-solid fa-9"></i></div>
          <h4 class="card-title">9. Sea Breeze (Daytime)</h4>
          <p>Land warms faster than water. Air rises over land, and cool air flows from sea to land.</p>
        </div>

        <div class="concept-card">
          <div class="card-icon blue"><i class="fa-solid fa-10"></i></div>
          <h4 class="card-title">10. Land Breeze (Nighttime)</h4>
          <p>Land cools faster than water. Air rises over warmer sea water, and cool air flows from land to sea.</p>
        </div>

        <div class="concept-card">
          <div class="card-icon blue"><i class="fa-solid fa-11"></i></div>
          <h4 class="card-title">11. Bernoulli Effect</h4>
          <p>High wind speed reduces lateral static pressure, creating aerodynamic lift on house roofs and airfoils.</p>
        </div>

        <div class="concept-card">
          <div class="card-icon blue"><i class="fa-solid fa-12"></i></div>
          <h4 class="card-title">12. Cloud Electrification</h4>
          <p>Collisions between rising ice crystals and falling water droplets charge cloud summits positively and cloud bases negatively.</p>
        </div>

        <div class="concept-card">
          <div class="card-icon blue"><i class="fa-solid fa-13"></i></div>
          <h4 class="card-title">13. Lightning Discharge</h4>
          <p>Dielectric breakdown of air triggers an electrical discharge reaching 30,000 &deg;C; explosive thermal air expansion causes thunder.</p>
        </div>

        <div class="concept-card">
          <div class="card-icon blue"><i class="fa-solid fa-14"></i></div>
          <h4 class="card-title">14. Tropical Cyclogenesis</h4>
          <p>Formed over warm tropical ocean waters (&ge; 27 &deg;C), fueled by latent heat of condensation, and spun by Coriolis deflection.</p>
        </div>

        <div class="concept-card">
          <div class="card-icon blue"><i class="fa-solid fa-15"></i></div>
          <h4 class="card-title">15. Cyclone Anatomy &amp; Surge</h4>
          <p>Features a calm central Eye, a violent Eye Wall, and destructive 3 to 12 metre coastal storm surges.</p>
        </div>
      </div>
    </section>
  </main>

  <!-- Interactive Client-Side JavaScript Engine -->
  <script>
    // 1. Reading Progress Bar Controller
    window.addEventListener('scroll', function() {
      var winScroll = document.body.scrollTop || document.documentElement.scrollTop;
      var height = document.documentElement.scrollHeight - document.documentElement.clientHeight;
      var scrolled = (winScroll / height) * 100;
      var bar = document.getElementById('readingProgressBar');
      if (bar) {
        bar.style.width = scrolled + '%';
      }
    });

    // 2. Interactive Text-to-Speech Audio Reader Engine
    var isSpeaking = false;
    function toggleAudioReader() {
      if (!('speechSynthesis' in window)) {
        alert("Text-to-speech is not supported by your current browser.");
        return;
      }

      if (isSpeaking) {
        window.speechSynthesis.cancel();
        isSpeaking = false;
        updateAudioButtons(false);
      } else {
        var summaryText = "Class 8 Science Chapter 6: Pressure, Winds, Storms, and Cyclones. " +
          "Pressure is defined as thrust per unit surface area, measured in Pascals. " +
          "Liquid pressure increases with depth and acts in all directions. " +
          "Atmospheric pressure at sea level is approximately 101.3 kilopascals, exerting 2,250 Newtons of force on an average palm. " +
          "Uneven solar heating creates convection winds: daytime Sea Breeze from sea to land, and nighttime Land Breeze from land to sea. " +
          "High-speed winds lower static air pressure via Bernoulli's principle, producing aerodynamic lift that can blow roofs off houses. " +
          "Thunderstorms form when warm, humid updrafts collide, separating electric charges: positive at cloud summits and negative at cloud bases. " +
          "Lightning heats air to 30,000 degrees Celsius, producing thunder. " +
          "Tropical cyclones develop over warm oceans above 27 degrees Celsius, fueled by the latent heat of condensation and organized by Coriolis rotation.";

        var utterance = new SpeechSynthesisUtterance(summaryText);
        utterance.rate = 0.95;
        utterance.pitch = 1.0;
        utterance.onend = function() {
          isSpeaking = false;
          updateAudioButtons(false);
        };
        utterance.onerror = function() {
          isSpeaking = false;
          updateAudioButtons(false);
        };

        window.speechSynthesis.speak(utterance);
        isSpeaking = true;
        updateAudioButtons(true);
      }
    }

    function updateAudioButtons(active) {
      var heroBtn = document.getElementById('heroAudioBtn');
      var navBtn = document.getElementById('navAudioBtn');
      if (heroBtn) {
        heroBtn.innerHTML = active ? 
          '<i class="fa-solid fa-circle-stop"></i> <span>⏹ Stop Audio Narration</span>' : 
          '<i class="fa-solid fa-headphones"></i> <span>🔊 Listen to Chapter Summary</span>';
      }
      if (navBtn) {
        navBtn.innerHTML = active ? 
          '<i class="fa-solid fa-circle-stop"></i> <span>Stop</span>' : 
          '<i class="fa-solid fa-volume-high"></i> <span>Listen</span>';
      }
    }

    // 3. Interactive Quiz Engine State & Evaluation
    var quizState = {};
    var totalQuizQuestions = 5;

    function checkQuizAnswer(qNum, optIdx, isCorrect, feedbackMsg) {
      var card = document.getElementById('qcard' + qNum);
      if (!card) return;

      var buttons = card.querySelectorAll('.quiz-opt');
      buttons.forEach(function(btn, idx) {
        btn.disabled = true;
        if (idx === optIdx) {
          if (isCorrect) {
            btn.classList.add('correct');
          } else {
            btn.classList.add('wrong');
          }
        }
      });

      var fb = document.getElementById('qfb' + qNum);
      if (fb) {
        fb.className = 'quiz-feedback show ' + (isCorrect ? 'success' : 'danger');
        fb.innerHTML = (isCorrect ? '<i class="fa-solid fa-circle-check"></i> ' : '<i class="fa-solid fa-circle-xmark"></i> ') + feedbackMsg;
      }

      quizState[qNum] = isCorrect;
      updateQuizScoreboard();
    }

    function updateQuizScoreboard() {
      var score = 0;
      var answered = 0;
      for (var k in quizState) {
        answered++;
        if (quizState[k] === true) score++;
      }

      var countEl = document.getElementById('quizScoreCount');
      if (countEl) countEl.textContent = score;

      var msgEl = document.getElementById('quizTeacherMsg');
      if (msgEl) {
        if (score === totalQuizQuestions) {
          msgEl.textContent = "🌟 Perfect 5/5! You have mastered Pressure, Winds, Storms, and Cyclones!";
        } else if (score >= 3) {
          msgEl.textContent = "👏 Excellent performance! Strong conceptual foundation in atmospheric physics!";
        } else if (answered > 0) {
          msgEl.textContent = "👍 Good effort! Review the detailed teacher explanation boxes to eliminate exam traps.";
        }
      }
    }
  </script>
</body>
</html>
'''
