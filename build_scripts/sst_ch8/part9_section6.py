# -*- coding: utf-8 -*-
"""
Part 9: Section 6 - Exam Hall Traps & 15 High-Yield Revision Points
Plus complete interactive JavaScript Engine (Reading Progress Bar, Interactive Quiz,
SpeechSynthesis Audio Reader, Details Accordion Controllers, Back-to-Top Button)
and Semantic Footer.
"""

PART9_CONTENT = '''
    <!-- ========================================== -->
    <!-- SECTION 6: EXAM HALL TRAPS & 15 REVISION POINTS -->
    <!-- ========================================== -->
    <section id="sec6">
      <div class="section-header">
        <div class="section-icon" style="background:#fee2e2; color:#be123c;"><i class="fa-solid fa-shield-halved"></i></div>
        <div class="section-header-text">
          <span class="section-tag" style="color:#be123c;">Section 6 &bull; Final Exam Polish</span>
          <h2>6. Exam Hall Traps &amp; 15 High-Yield Fast Recall Points</h2>
        </div>
      </div>

      <!-- 5 Common Exam Hall Traps -->
      <div class="callout callout-warn">
        <div class="callout-title"><i class="fa-solid fa-triangle-exclamation"></i> 5 Common Exam Hall Traps &amp; Student Blunders</div>
        <p style="margin-bottom:1rem;">Examiners frequently design trick questions around these five widespread misconceptions:</p>
        
        <div style="margin-bottom:1rem; padding-bottom:0.75rem; border-bottom:1px solid #fecaca;">
          <strong>Trap 1: The Mercator Greenland Illusion</strong>
          <br><span style="color:#991b1b; font-size:0.9rem;">&cross; Common Mistake:</span> Writing that Greenland and Africa are approximately the same physical size.
          <br><span style="color:#15803d; font-size:0.9rem;">&check; The Geographical Fact:</span> Africa (30.37M km&#178;) is <strong>14 times larger</strong> than Greenland (2.16M km&#178;)! Also, India (3.287M km&#178;) is 1.5 times larger than Greenland, despite Mercator maps visually shrinking India.
        </div>

        <div style="margin-bottom:1rem; padding-bottom:0.75rem; border-bottom:1px solid #fecaca;">
          <strong>Trap 2: Misinterpreting the 'Third Pole'</strong>
          <br><span style="color:#991b1b; font-size:0.9rem;">&cross; Common Mistake:</span> Stating that the 'Third Pole' is a magnetic pole located in northern Siberia or the Arctic.
          <br><span style="color:#15803d; font-size:0.9rem;">&check; The Geographical Fact:</span> The <em>Third Pole</em> is the scientific nickname for the <strong>Tibetan Plateau and adjoining mountain ranges</strong>, earned because it holds the greatest concentration of glacial freshwater ice outside the Arctic and Antarctic!
        </div>

        <div style="margin-bottom:1rem; padding-bottom:0.75rem; border-bottom:1px solid #fecaca;">
          <strong>Trap 3: Thinking All Deserts are Scorching Sand Seas</strong>
          <br><span style="color:#991b1b; font-size:0.9rem;">&cross; Common Mistake:</span> Answering that the Sahara is the largest desert on Earth, or defining a desert by "hot temperatures and sand dunes".
          <br><span style="color:#15803d; font-size:0.9rem;">&check; The Geographical Fact:</span> Deserts are defined strictly by <strong>low precipitation (&lt;25 cm/year)</strong>. By this definition, <strong>Antarctica is Earth's largest desert</strong> (14.2M km&#178;), and it is a frigid polar desert. The Sahara is only the largest <em>hot</em> desert!
        </div>

        <div style="margin-bottom:1rem; padding-bottom:0.75rem; border-bottom:1px solid #fecaca;">
          <strong>Trap 4: Assuming Bleached Corals are Instantly Dead</strong>
          <br><span style="color:#991b1b; font-size:0.9rem;">&cross; Common Mistake:</span> Believing that when coral polyps expel zooxanthellae, they are dead skeletons that can never recover.
          <br><span style="color:#15803d; font-size:0.9rem;">&check; The Geographical Fact:</span> Bleaching is an acute starvation stress state. If ocean water temperatures cool within <strong>2 to 4 weeks</strong>, corals re-acquire algae and recover. Only prolonged persistent heat leads to permanent mortality.
        </div>

        <div>
          <strong>Trap 5: Confusing Green Color on Physical Maps with Dense Forests</strong>
          <br><span style="color:#991b1b; font-size:0.9rem;">&cross; Common Mistake:</span> Assuming any green region on a physical world map indicates a dense jungle or rainforest.
          <br><span style="color:#15803d; font-size:0.9rem;">&check; The Geographical Fact:</span> On physical hypsometric maps, <strong>green represents low altitude / elevation</strong> (flat plains &lt;200 m above sea level). A barren salt marsh, tundra lowland, or city plain is also shaded green!
        </div>
      </div>

      <!-- 15 Fast Recall Points -->
      <h3 style="margin-top:2.5rem;">15 High-Yield Fast Recall Points</h3>
      <p style="font-size:0.92rem; color:var(--text-muted); margin-bottom:1.25rem;">
        Review these fifteen high-frequency points on the morning of your examination:
      </p>

      <ul class="revision-list">
        <li class="revision-item">
          <span class="revision-num">1</span>
          <div><strong>Oblate Spheroid Geometry:</strong> Earth bulges at the Equator and flattens at the poles due to centrifugal rotational forces, making it mathematically impossible to flatten onto 2D paper without distortion (the orange peel paradox).</div>
        </li>
        <li class="revision-item">
          <span class="revision-num">2</span>
          <div><strong>Mercator Trade-Off:</strong> Preserves compass bearing angles (rhumb lines) for sailing ships, but severely exaggerates landmass areas as one approaches the poles (e.g., Greenland vs Africa).</div>
        </li>
        <li class="revision-item">
          <span class="revision-num">3</span>
          <div><strong>Equal-Area Projections (Gall-Peters):</strong> Preserve proportional surface area across all regions, showing true land size for the Global South (Africa, India, South America).</div>
        </li>
        <li class="revision-item">
          <span class="revision-num">4</span>
          <div><strong>Hydrosphere Dominance:</strong> Oceans cover 71% of Earth's surface, hold 97% of its water, and absorb over 90% of excess planetary heat.</div>
        </li>
        <li class="revision-item">
          <span class="revision-num">5</span>
          <div><strong>The Plankton Powerhouse:</strong> Microscopic marine phytoplankton generate over 50% of the oxygen in Earth's atmosphere through photosynthesis and sequester 30% of carbon emissions.</div>
        </li>
        <li class="revision-item">
          <span class="revision-num">6</span>
          <div><strong>Ocean Currents Conveyor:</strong> The warm Gulf Stream keeps Western European ports ice-free, while the reversing Indian Ocean monsoon currents regulate South Asian agriculture.</div>
        </li>
        <li class="revision-item">
          <span class="revision-num">7</span>
          <div><strong>Rainforests of the Sea:</strong> Coral reefs cover &lt;1% of the seabed but shelter &gt;25% of all ocean species; built of calcium carbonate by polyps in symbiosis with zooxanthellae.</div>
        </li>
        <li class="revision-item">
          <span class="revision-num">8</span>
          <div><strong>The Great Barrier Reef (2,300 km):</strong> World's largest living structure off Queensland, Australia, threatened by marine heatwaves that induce mass coral bleaching.</div>
        </li>
        <li class="revision-item">
          <span class="revision-num">9</span>
          <div><strong>The Suez Canal (1869):</strong> A 193 km human-made waterway linking the Mediterranean to the Red Sea, saving 7,000 km on the voyage between India and Europe.</div>
        </li>
        <li class="revision-item">
          <span class="revision-num">10</span>
          <div><strong>Tibetan Plateau ('Third Pole'):</strong> World's highest and largest plateau (&gt;4,500 m avg elevation, 2.5M km&#178;), functioning as the Water Tower of Asia feeding 10 major rivers for 1.4B people.</div>
        </li>
        <li class="revision-item">
          <span class="revision-num">11</span>
          <div><strong>Eurasian Steppes &amp; Permafrost:</strong> An 8,000 km grassland carbon sink whose deep soils sequester CO&#8322;, while northern permafrost acts as a cryogenic freezer trapping explosive methane.</div>
        </li>
        <li class="revision-item">
          <span class="revision-num">12</span>
          <div><strong>The Nile (6,650 km):</strong> World's longest river, flowing north from Lake Victoria and Ethiopia across the Sahara into the Mediterranean Sea ("The Gift of the Nile").</div>
        </li>
        <li class="revision-item">
          <span class="revision-num">13</span>
          <div><strong>The Amazon ('Lungs of the Earth'):</strong> Contains 390 billion trees, absorbs 2B tonnes CO&#8322;/yr, pumps 'flying rivers' of water vapor, and receives 22,000 tonnes of fertilizing phosphorus dust from the Sahara!</div>
        </li>
        <li class="revision-item">
          <span class="revision-num">14</span>
          <div><strong>Atacama &amp; Antarctica Extremes:</strong> Atacama (Chile) is the driest non-polar desert (NASA rover testing ground); Antarctica is the largest and coldest desert on Earth (14.2M km&#178;, 70% of world freshwater).</div>
        </li>
        <li class="revision-item">
          <span class="revision-num">15</span>
          <div><strong>The Paika Sangram of Odisha (1817):</strong> Heroic armed uprising led by Buxi Jagabandhu against British land confiscation and salt monopolies 40 years before 1857 &mdash; affirming the sacred right of native peoples to their soil.</div>
        </li>
      </ul>
    </section>

  </div> <!-- End Main Container -->

  <!-- Floating Back-to-Top Button -->
  <button id="back-to-top" onclick="scrollToTop()" title="Back to top">
    <i class="fa-solid fa-arrow-up"></i>
  </button>

  <!-- Semantic Footer -->
  <footer>
    <p style="font-weight:700; color:var(--dark); font-size:1.05rem; margin-bottom:0.5rem;">
      Sujit Classes &bull; Conceptual Excellence Portal
    </p>
    <p style="margin-bottom:0.75rem;">
      Comprehensive Master Study Note for Class 8 Social Science &bull; Chapter 8: World Geography: Some Glimpses (hess108)
    </p>
    <p style="font-size:0.82rem; color:var(--text-muted); margin-bottom:0;">
      Prepared strictly in accordance with NCERT NEP 2020 Middle Stage Curricular Framework and BSE Odisha Educational Standards.
      <br><a href="../../index.html"><i class="fa-solid fa-house"></i> Return to Study Portal</a> &bull;
      <a href="#sec1"><i class="fa-solid fa-arrow-up"></i> Jump to Top</a>
    </p>
  </footer>

  <!-- ========================================== -->
  <!-- JAVASCRIPT ENGINE -->
  <!-- ========================================== -->
  <script>
    // 1. Reading Progress Bar & Back-to-Top Button Visibility
    window.addEventListener('scroll', function() {
      var winScroll = document.documentElement.scrollTop || document.body.scrollTop;
      var height = document.documentElement.scrollHeight - document.documentElement.clientHeight;
      var scrolled = height > 0 ? (winScroll / height) * 100 : 0;
      
      var bar = document.getElementById('reading-progress-bar');
      if (bar) bar.style.width = scrolled + '%';

      var btt = document.getElementById('back-to-top');
      if (btt) {
        if (winScroll > 350) {
          btt.style.display = 'flex';
        } else {
          btt.style.display = 'none';
        }
      }
    });

    // 2. Smooth Scroll to Top
    function scrollToTop() {
      window.scrollTo({ top: 0, behavior: 'smooth' });
    }

    // 3. Interactive Quiz Engine
    var answeredCards = {};
    var currentScore = 0;

    function checkAnswer(btn, selectedIndex) {
      var card = btn.closest('.quiz-card');
      var cardId = card.id;

      if (answeredCards[cardId]) return;
      answeredCards[cardId] = true;

      var correctIndex = parseInt(card.getAttribute('data-correct'), 10);
      var options = card.querySelectorAll('.opt-btn');
      var trapExp = card.querySelector('.trap-explanation');

      if (selectedIndex === correctIndex) {
        btn.classList.add('correct');
        btn.querySelector('.opt-letter').innerHTML = '<i class="fa-solid fa-check"></i>';
        currentScore++;
      } else {
        btn.classList.add('wrong');
        btn.querySelector('.opt-letter').innerHTML = '<i class="fa-solid fa-xmark"></i>';
        options[correctIndex].classList.add('correct');
        options[correctIndex].querySelector('.opt-letter').innerHTML = '<i class="fa-solid fa-check"></i>';
      }

      // Reveal trap explanation
      if (trapExp) {
        trapExp.style.display = 'block';
      }

      // Disable remaining options
      options.forEach(function(b) {
        b.disabled = true;
      });

      // Update real-time score
      document.getElementById('quiz-score').innerText = currentScore;
      var feedback = document.getElementById('quiz-feedback');
      if (feedback) {
        if (currentScore === 5) {
          feedback.innerHTML = '<span style="color:#dcfce7; font-weight:700;"><i class="fa-solid fa-trophy"></i> Master Geographer! 5/5 Perfect Score!</span>';
        } else if (currentScore >= 3) {
          feedback.innerHTML = '<span style="color:#fef08a; font-weight:700;"><i class="fa-solid fa-thumbs-up"></i> Great Effort! Review the trap explanations to master every concept.</span>';
        } else {
          feedback.innerHTML = 'Keep studying! Review Sections 2 and 3 and test yourself again.';
        }
      }
    }

    // 4. Accordion Toggle Functions
    function expandAllDetails(sectionId) {
      var sec = document.getElementById(sectionId);
      if (!sec) return;
      var details = sec.querySelectorAll('details.ans-box');
      details.forEach(function(d) {
        d.open = true;
      });
    }

    function collapseAllDetails(sectionId) {
      var sec = document.getElementById(sectionId);
      if (!sec) return;
      var details = sec.querySelectorAll('details.ans-box');
      details.forEach(function(d) {
        d.open = false;
      });
    }

    // 5. SpeechSynthesis Audio Reader Engine
    var synth = window.speechSynthesis;
    var isSpeaking = false;

    function toggleAudioReader() {
      if (!synth) {
        alert("Text-to-Speech is not supported in your browser.");
        return;
      }

      if (isSpeaking) {
        if (synth.paused) {
          synth.resume();
          updateAudioUI(true);
        } else {
          synth.pause();
          updateAudioUI(false, "Resume");
        }
        return;
      }

      var textToSpeak = "Chapter 8: World Geography: Some Glimpses. Exploring Society: India and Beyond. " +
        "The Earth is an oblate spheroid that bulges at the Equator and is flattened at the poles. " +
        "Because of the orange peel paradox, flattening a 3-dimensional sphere onto a 2-dimensional flat sheet " +
        "always creates geometric distortion. The famous Mercator projection preserves compass angles for navigation, " +
        "but severely exaggerates polar landmasses, making Greenland look equal to Africa, though Africa is 14 times larger! " +
        "Oceans cover 71 percent of Earth and regulate our global climate as massive heat sinks. " +
        "Microscopic phytoplankton in the sunlit ocean produce over 50 percent of the oxygen we breathe. " +
        "Coral reefs, known as the rainforests of the sea, cover less than 1 percent of the ocean floor, " +
        "yet shelter over 25 percent of all marine species. Heatwaves trigger coral bleaching, where stressed polyps expel their colorful algae. " +
        "From the high roof of the Tibetan Plateau, known as the Third Pole and Water Tower of Asia, " +
        "to the scorching dunes of the Sahara, the great migration across the African Savannah, " +
        "the vast carbon sink of the Eurasian Steppes, and the Amazon Rainforest with its flying rivers, " +
        "understanding world geography teaches us to revere our living planet Earth.";

      var utterance = new SpeechSynthesisUtterance(textToSpeak);
      utterance.rate = 0.92;
      utterance.pitch = 1.0;
      utterance.lang = 'en-IN';

      utterance.onstart = function() {
        isSpeaking = true;
        updateAudioUI(true);
      };

      utterance.onend = function() {
        isSpeaking = false;
        updateAudioUI(false);
      };

      utterance.onerror = function() {
        isSpeaking = false;
        updateAudioUI(false);
      };

      synth.cancel(); // Clear any previous queue
      synth.speak(utterance);
    }

    function stopAudioReader() {
      if (synth) {
        synth.cancel();
        isSpeaking = false;
        updateAudioUI(false);
      }
    }

    function updateAudioUI(speaking, customText) {
      var speechBtn = document.getElementById('speech-btn');
      var speechBtnText = document.getElementById('speech-btn-text');
      var playBtn = document.getElementById('audio-bar-play');

      if (speaking) {
        if (speechBtn) speechBtn.classList.add('active-audio');
        if (speechBtnText) speechBtnText.innerText = "Pause";
        if (playBtn) playBtn.innerHTML = '<i class="fa-solid fa-pause"></i> Pause';
      } else {
        if (speechBtn) speechBtn.classList.remove('active-audio');
        var text = customText || "Listen";
        if (speechBtnText) speechBtnText.innerText = text;
        if (playBtn) playBtn.innerHTML = '<i class="fa-solid fa-play"></i> ' + (customText ? customText : "Listen Now");
      }
    }
  </script>
</body>
</html>
'''
