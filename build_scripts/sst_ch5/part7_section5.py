# -*- coding: utf-8 -*-
"""
Part 7: Section 5 - Complete Exam Question Bank (27 Total Questions).
Includes:
1. 5 Interactive Conceptual MCQs with Trap Alerts & Score Tracker
2. 5 Assertion & Reasoning Questions with Step-by-Step Proofs
3. 6 Short Answer Questions (2M / 3M) with Point-Wise Schemes
4. 4 Long Answer Questions (5M) with Official Marking Criteria
5. 2 Competency-Based Source Analysis Case Studies
6. 5 Previous Years & Most Probable Exam Questions with Model Answers
"""

PART7_CONTENT = '''
    <!-- ========================================== -->
    <!-- SECTION 5: COMPLETE EXAM QUESTION BANK    -->
    <!-- ========================================== -->
    <section class="section-block" id="section-5">
      <div class="section-header">
        <div class="section-title-wrap">
          <span class="section-tag"><i class="fa-solid fa-trophy"></i> CBSE Exam Bank</span>
          <h2 class="section-title">Section 5: Complete Exam Question Bank (27 Questions)</h2>
          <p class="section-desc">
            An exhaustive treasury of high-probability examination questions covering every cognitive level—from interactive conceptual traps to competency-based real-world case studies.
          </p>
        </div>
      </div>

      <!-- ========================================= -->
      <!-- PART A: 5 INTERACTIVE CONCEPTUAL MCQS     -->
      <!-- ========================================= -->
      <h3 class="subsection-title">
        <i class="fa-solid fa-gamepad" style="color: #1e3a8a;"></i>
        Part A: Interactive Conceptual MCQs (With Instant Evaluation & Trap Alerts)
      </h3>

      <div class="quiz-container">
        <!-- Live Score Tracker Banner -->
        <div class="quiz-score-banner">
          <div class="quiz-score-text">
            <h4><i class="fa-solid fa-brain" style="color: #fbbf24;"></i> Real-Time Quiz Score Tracker</h4>
            <p>Test your conceptual understanding. Click your answer to test yourself!</p>
          </div>
          <div>
            Score: <span class="quiz-score-counter" id="quiz-score">0</span> / 5
          </div>
        </div>

        <!-- MCQ 1 -->
        <div class="quiz-card" id="mcq-card-1">
          <p class="quiz-question">
            <strong>Q1.</strong> Under Article 326 of the Constitution of India and the 61st Amendment Act, 1988, which of the following is a VALID legal ground to bar an Indian citizen from voting?
          </p>
          <div class="quiz-options">
            <button class="quiz-opt-btn" onclick="checkAnswer(1, 0, false)">
              <span>A. Inability to read or write (illiteracy)</span>
            </button>
            <button class="quiz-opt-btn" onclick="checkAnswer(1, 1, true)">
              <span>B. Declared to be of unsound mind by a competent court</span>
            </button>
            <button class="quiz-opt-btn" onclick="checkAnswer(1, 2, false)">
              <span>C. Failure to pay municipal property taxes or agricultural dues</span>
            </button>
            <button class="quiz-opt-btn" onclick="checkAnswer(1, 3, false)">
              <span>D. Not owning any land or permanent residential property</span>
            </button>
          </div>
          <div class="quiz-feedback" id="feedback-1">
            <strong><i class="fa-solid fa-triangle-exclamation"></i> Exam Trap Analysis:</strong><br>
            <strong>Correct Answer: B.</strong> Article 326 strictly forbids discrimination on basis of property, income, tax status, or literacy. The only permissible disqualifications are non-residence, unsound mind declared by a competent court, or conviction for corrupt electoral crimes!<br>
            <em>Common Student Mistake:</em> Students confuse pre-1947 British rules (which required property and tax payments) with the modern Indian Constitution!
          </div>
        </div>

        <!-- MCQ 2 -->
        <div class="quiz-card" id="mcq-card-2">
          <p class="quiz-question">
            <strong>Q2.</strong> In the 10th-century Chola Kudavolai election system described at Uttaramerur, what happened if a sitting committee member failed to submit fully audited village accounts?
          </p>
          <div class="quiz-options">
            <button class="quiz-opt-btn" onclick="checkAnswer(2, 0, false)">
              <span>A. He was given a 30-day grace extension by the village Mahasabha</span>
            </button>
            <button class="quiz-opt-btn" onclick="checkAnswer(2, 1, false)">
              <span>B. He was made to pay a small cash fine to the local temple</span>
            </button>
            <button class="quiz-opt-btn" onclick="checkAnswer(2, 2, true)">
              <span>C. Both he and all his close relatives were permanently disqualified from contesting future elections</span>
            </button>
            <button class="quiz-opt-btn" onclick="checkAnswer(2, 3, false)">
              <span>D. He was demoted to serve as a security guard for the earthen pot</span>
            </button>
          </div>
          <div class="quiz-feedback" id="feedback-2">
            <strong><i class="fa-solid fa-triangle-exclamation"></i> Exam Trap Analysis:</strong><br>
            <strong>Correct Answer: C.</strong> The Chola Uttaramerur inscriptions had one of the strictest anti-corruption rules in ancient world history: failure to submit public financial accounts permanently barred the member AND all his close family relatives from holding public office!<br>
            <em>Trap Alert:</em> Many students guess Option A thinking ancient systems were informal. In reality, Chola accounting audits were ruthlessly strict!
          </div>
        </div>

        <!-- MCQ 3 -->
        <div class="quiz-card" id="mcq-card-3">
          <p class="quiz-question">
            <strong>Q3.</strong> Which of the following constitutional groups is STRICTLY EXCLUDED from voting in the election of the President of India?
          </p>
          <div class="quiz-options">
            <button class="quiz-opt-btn" onclick="checkAnswer(3, 0, false)">
              <span>A. Elected Members of Legislative Assemblies of Delhi and Puducherry</span>
            </button>
            <button class="quiz-opt-btn" onclick="checkAnswer(3, 1, true)">
              <span>B. Nominated members of the Rajya Sabha (12 members)</span>
            </button>
            <button class="quiz-opt-btn" onclick="checkAnswer(3, 2, false)">
              <span>C. Elected Members of the Lok Sabha</span>
            </button>
            <button class="quiz-opt-btn" onclick="checkAnswer(3, 3, false)">
              <span>D. Elected Members of the Legislative Assembly of Odisha</span>
            </button>
          </div>
          <div class="quiz-feedback" id="feedback-3">
            <strong><i class="fa-solid fa-triangle-exclamation"></i> Exam Trap Analysis:</strong><br>
            <strong>Correct Answer: B.</strong> The Presidential Electoral College consists strictly of <em>ELECTED</em> members of Parliament and State Assemblies. Nominated members are chosen by the sitting executive and are excluded to avoid conflicts of interest. Members of Legislative Councils (MLCs) are also excluded!<br>
            <em>Trap Alert:</em> Note that elected MLAs from UTs like Delhi and Puducherry DO vote; only nominated members and MLCs are excluded.
          </div>
        </div>

        <!-- MCQ 4 -->
        <div class="quiz-card" id="mcq-card-4">
          <p class="quiz-question">
            <strong>Q4.</strong> In an Indian Lok Sabha constituency reserved for Scheduled Castes (SC), which of the following statements correctly describes who can vote and who can contest?
          </p>
          <div class="quiz-options">
            <button class="quiz-opt-btn" onclick="checkAnswer(4, 0, false)">
              <span>A. Only SC citizens can vote, and only SC candidates can contest</span>
            </button>
            <button class="quiz-opt-btn" onclick="checkAnswer(4, 1, true)">
              <span>B. All registered citizens vote equally, but only SC candidates can contest</span>
            </button>
            <button class="quiz-opt-btn" onclick="checkAnswer(4, 2, false)">
              <span>C. Only SC citizens can vote, but candidates from any community can contest</span>
            </button>
            <button class="quiz-opt-btn" onclick="checkAnswer(4, 3, false)">
              <span>D. Voting is conducted through separate communal electoral rolls</span>
            </button>
          </div>
          <div class="quiz-feedback" id="feedback-4">
            <strong><i class="fa-solid fa-triangle-exclamation"></i> Exam Trap Analysis:</strong><br>
            <strong>Correct Answer: B.</strong> India rejected separate electorates! In a reserved seat, EVERY registered voter (general, OBC, SC, ST) votes on the exact same roll; only the contesting candidate must belong to the SC community.<br>
            <em>Critical Blunder:</em> Nearly 40% of students mistakenly pick Option A, falsely assuming reserved seats mean reserved voting rights!
          </div>
        </div>

        <!-- MCQ 5 -->
        <div class="quiz-card" id="mcq-card-5">
          <p class="quiz-question">
            <strong>Q5.</strong> What happens immediately after a voter presses a candidate\'s button on the EVM Ballot Unit?
          </p>
          <div class="quiz-options">
            <button class="quiz-opt-btn" onclick="checkAnswer(5, 0, false)">
              <span>A. A paper receipt prints out and the voter carries it home as proof</span>
            </button>
            <button class="quiz-opt-btn" onclick="checkAnswer(5, 1, false)">
              <span>B. The machine connects to the internet to upload the vote to Nirvachan Sadan</span>
            </button>
            <button class="quiz-opt-btn" onclick="checkAnswer(5, 2, true)">
              <span>C. A red lamp glows, a loud beep sounds, and the VVPAT slip is visible for 7 seconds before dropping into a sealed box</span>
            </button>
            <button class="quiz-opt-btn" onclick="checkAnswer(5, 3, false)">
              <span>D. The voter\'s fingerprint is scanned to verify ink chemistry</span>
            </button>
          </div>
          <div class="quiz-feedback" id="feedback-5">
            <strong><i class="fa-solid fa-triangle-exclamation"></i> Exam Trap Analysis:</strong><br>
            <strong>Correct Answer: C.</strong> The sequence is: button press → red LED on Ballot Unit → VVPAT window illuminates printed paper slip for exactly 7 seconds → slip cuts and drops into sealed ballot box → loud beep confirms Control Unit has stored the vote.<br>
            <em>Misconception:</em> EVMs NEVER connect to the internet or cellular networks; they are 100% offline standalone devices!
          </div>
        </div>
      </div>

      <!-- ========================================= -->
      <!-- PART B: 5 ASSERTION & REASONING QUESTIONS -->
      <!-- ========================================= -->
      <h3 class="subsection-title">
        <i class="fa-solid fa-scale-unbalanced-flip" style="color: #047857;"></i>
        Part B: Assertion & Reasoning Questions (CBSE Format)
      </h3>
      <p style="font-size: 0.9rem; color: #475569; margin-bottom: 1.25rem;">
        <strong>Directions:</strong> Select the correct option from the following:<br>
        (A) Both Assertion (A) and Reason (R) are true, and Reason (R) is the correct explanation of Assertion (A).<br>
        (B) Both Assertion (A) and Reason (R) are true, but Reason (R) is NOT the correct explanation of Assertion (A).<br>
        (C) Assertion (A) is true, but Reason (R) is false.<br>
        (D) Assertion (A) is false, but Reason (R) is true.
      </p>

      <!-- A&R 1 -->
      <details class="ans-box">
        <summary class="ans-summary">
          <span><strong>Assertion & Reasoning 1:</strong> On Universal Franchise and Illiteracy in 1947.</span>
        </summary>
        <div class="ans-content">
          <p><strong>Assertion (A):</strong> The makers of the Indian Constitution adopted Universal Adult Franchise despite the overall literacy rate being only about 14% at Independence.</p>
          <p><strong>Reason (R):</strong> Universal Adult Franchise is based on the democratic conviction that wisdom and political equality do not depend on formal educational degrees, and poor citizens have equal stakes in national governance.</p>
          <hr style="margin: 0.8rem 0; border: none; border-top: 1px dashed #cbd5e1;">
          <p><strong>Correct Option: (A)</strong> Both (A) and (R) are true, and (R) is the correct explanation of (A).</p>
          <p><strong>Logical Proof:</strong> The Constituent Assembly debates clearly show that Dr. B.R. Ambedkar and Alladi Krishnaswami Ayyar consciously rejected educational franchises because they believed political democracy must treat every human being as an equal sovereign citizen, regardless of literacy.</p>
        </div>
      </details>

      <!-- A&R 2 -->
      <details class="ans-box">
        <summary class="ans-summary">
          <span><strong>Assertion & Reasoning 2:</strong> On the First-Past-The-Post (FPTP) System.</span>
        </summary>
        <div class="ans-content">
          <p><strong>Assertion (A):</strong> Under India\'s First-Past-The-Post system, a candidate can be declared elected to the Lok Sabha even without securing more than 50 per cent of the total votes polled.</p>
          <p><strong>Reason (R):</strong> In FPTP, the candidate who secures the highest number of votes compared to any individual rival candidate wins the constituency.</p>
          <hr style="margin: 0.8rem 0; border: none; border-top: 1px dashed #cbd5e1;">
          <p><strong>Correct Option: (A)</strong> Both (A) and (R) are true, and (R) is the correct explanation of (A).</p>
          <p><strong>Logical Proof:</strong> In multi-cornered contests, if Candidate A gets 35%, Candidate B gets 33%, and Candidate C gets 32%, Candidate A wins. A plurality (highest individual tally), not an absolute majority (50%+1), is required under FPTP.</p>
        </div>
      </details>

      <!-- A&R 3 -->
      <details class="ans-box">
        <summary class="ans-summary">
          <span><strong>Assertion & Reasoning 3:</strong> On the Independence of the Election Commission.</span>
        </summary>
        <div class="ans-content">
          <p><strong>Assertion (A):</strong> The Election Commission of India functions under the direct administrative control and supervision of the Union Ministry of Home Affairs.</p>
          <p><strong>Reason (R):</strong> Article 324 of the Constitution vests the superintendence, direction, and control of elections in an autonomous constitutional commission.</p>
          <hr style="margin: 0.8rem 0; border: none; border-top: 1px dashed #cbd5e1;">
          <p><strong>Correct Option: (D)</strong> Assertion (A) is false, but Reason (R) is true.</p>
          <p><strong>Logical Proof:</strong> Assertion (A) is completely false. The ECI is an autonomous constitutional body independent of any ministry. Reason (R) is true as Article 324 guarantees this constitutional autonomy.</p>
        </div>
      </details>

      <!-- A&R 4 -->
      <details class="ans-box">
        <summary class="ans-summary">
          <span><strong>Assertion & Reasoning 4:</strong> On the Secret Ballot Mechanism.</span>
        </summary>
        <div class="ans-content">
          <p><strong>Assertion (A):</strong> A secret ballot empowers socially disadvantaged and economically weaker voters to cast their ballots fearlessly.</p>
          <p><strong>Reason (R):</strong> The secret ballot prevents powerful landlords and corrupt candidates from verifying whether a voter obeyed their commands or inducements.</p>
          <hr style="margin: 0.8rem 0; border: none; border-top: 1px dashed #cbd5e1;">
          <p><strong>Correct Option: (A)</strong> Both (A) and (R) are true, and (R) is the correct explanation of (A).</p>
          <p><strong>Logical Proof:</strong> Confidentiality inside the voting compartment breaks the link between intimidation/bribes and voter choice, ensuring true democratic freedom.</p>
        </div>
      </details>

      <!-- A&R 5 -->
      <details class="ans-box">
        <summary class="ans-summary">
          <span><strong>Assertion & Reasoning 5:</strong> On Rajya Sabha Elections and Permanence.</span>
        </summary>
        <div class="ans-content">
          <p><strong>Assertion (A):</strong> The Rajya Sabha is never dissolved by the President and is known as a permanent legislative body.</p>
          <p><strong>Reason (R):</strong> All 245 members of the Rajya Sabha are elected at the same time through direct nationwide adult franchise for a term of five years.</p>
          <hr style="margin: 0.8rem 0; border: none; border-top: 1px dashed #cbd5e1;">
          <p><strong>Correct Option: (C)</strong> Assertion (A) is true, but Reason (R) is false.</p>
          <p><strong>Logical Proof:</strong> Assertion (A) is true. Reason (R) is completely false because Rajya Sabha members are elected indirectly by state MLAs for 6-year terms, with one-third retiring every two years—it is never elected all at once by citizens!</p>
        </div>
      </details>

      <!-- ========================================= -->
      <!-- PART C: 6 SHORT ANSWER QUESTIONS (2M/3M)  -->
      <!-- ========================================= -->
      <h3 class="subsection-title">
        <i class="fa-solid fa-pen-to-square" style="color: #b45309;"></i>
        Part C: Short Answer Questions (2 Marks & 3 Marks)
      </h3>

      <!-- SAQ 1 -->
      <details class="ans-box">
        <summary class="ans-summary">
          <span><strong>SAQ 1 (2 Marks):</strong> State any two major differences between an MP (Member of Parliament) and an MLA (Member of Legislative Assembly).</span>
        </summary>
        <div class="ans-content">
          <p><strong>Answer (CBSE Marking Criteria - 1 Mark per distinct point):</strong></p>
          <ol>
            <li><strong>Legislative Arena & Jurisdiction (1 Mark):</strong> An MP sits in the national Parliament (Lok Sabha/Rajya Sabha in New Delhi) and debates national issues like defense, railways, and foreign policy; whereas an MLA sits in the State Legislative Assembly (Vidhan Sabha in state capital) and debates state issues like agriculture, local policing, and state hospitals.</li>
            <li><strong>Territorial Constituency Scale (1 Mark):</strong> A Lok Sabha MP represents a vastly larger territorial constituency, typically consisting of 5 to 9 Assembly constituencies represented by different MLAs.</li>
          </ol>
        </div>
      </details>

      <!-- SAQ 2 -->
      <details class="ans-box">
        <summary class="ans-summary">
          <span><strong>SAQ 2 (2 Marks):</strong> Why is Mysore Paints and Varnish Ltd famous in Indian elections? What chemical compound is used?</span>
        </summary>
        <div class="ans-content">
          <p><strong>Answer:</strong></p>
          <ul>
            <li><strong>Sole Manufacturer (1 Mark):</strong> Mysore Paints and Varnish Ltd (Karnataka) is the exclusive authorized manufacturer of <strong>indelible ink</strong> used across all Indian elections and exported to over 30 democracies worldwide.</li>
            <li><strong>Active Compound (1 Mark):</strong> The ink contains <strong>Silver Nitrate (AgNO₃)</strong>, which reacts instantly with skin proteins (keratin) and light to form a permanent purple stain that cannot be washed off, effectively preventing fraudulent duplicate voting.</li>
          </ul>
        </div>
      </details>

      <!-- SAQ 3 -->
      <details class="ans-box">
        <summary class="ans-summary">
          <span><strong>SAQ 3 (3 Marks):</strong> Mention three key electoral reforms introduced during the tenure of Chief Election Commissioner T.N. Seshan.</span>
        </summary>
        <div class="ans-content">
          <p><strong>Answer (1 Mark for each valid reform):</strong></p>
          <ul>
            <li><strong>1. Introduction of Voter Photo Identity Cards (EPIC):</strong> Implemented compulsory voter ID cards with photographs to eliminate bogus and proxy voting.</li>
            <li><strong>2. Ruthless Enforcement of the Model Code of Conduct:</strong> Stopped ruling parties from misusing government vehicles, banned liquor and cash distribution, and cancelled polls in violence-marred booths.</li>
            <li><strong>3. Deployment of Central Paramilitary Forces (CAPF):</strong> Ended the menace of booth capturing by replacing biased local police with neutral central forces at sensitive polling stations.</li>
          </ul>
        </div>
      </details>

      <!-- SAQ 4 -->
      <details class="ans-box">
        <summary class="ans-summary">
          <span><strong>SAQ 4 (3 Marks):</strong> Explain the functioning and significance of the VVPAT system.</span>
        </summary>
        <div class="ans-content">
          <p><strong>Answer:</strong></p>
          <ul>
            <li><strong>Meaning (1 Mark):</strong> VVPAT stands for <strong>Voter Verifiable Paper Audit Trail</strong>, an independent printing unit connected directly to the EVM Ballot Unit.</li>
            <li><strong>Functioning (1 Mark):</strong> When a voter presses a candidate button, the VVPAT window illuminates a printed thermal paper slip showing the candidate\'s serial number, name, and election symbol for <strong>exactly 7 seconds</strong>. It then cuts automatically and drops into a sealed box.</li>
            <li><strong>Significance (1 Mark):</strong> It provides physical, tamper-proof proof allowing voters to verify that their electronic vote was registered accurately, and enables recounting in case of legal election disputes.</li>
          </ul>
        </div>
      </details>

      <!-- SAQ 5 -->
      <details class="ans-box">
        <summary class="ans-summary">
          <span><strong>SAQ 5 (3 Marks):</strong> What is the 'Kudavolai' system? Name the dynasty and historical village where its inscription was found.</span>
        </summary>
        <div class="ans-content">
          <p><strong>Answer:</strong></p>
          <ul>
            <li><strong>Historical Anchor (1 Mark):</strong> Found in 10th-century stone inscriptions at <strong>Uttaramerur village</strong> (Tamil Nadu) during the reign of King <strong>Parantaka Chola I of the Chola Dynasty</strong>.</li>
            <li><strong>Working Mechanism (1 Mark):</strong> Village was divided into 30 wards. Candidate names were inscribed on dried palm leaves (<em>olai</em>) and placed inside an earthen pot (<em>kuda</em>). A young innocent child drew tickets publicly in front of the village assembly.</li>
            <li><strong>Significance (1 Mark):</strong> Proves that ancient India had transparent, corruption-free democratic selection systems with strict accounting qualification rules over a thousand years ago.</li>
          </ul>
        </div>
      </details>

      <!-- SAQ 6 -->
      <details class="ans-box">
        <summary class="ans-summary">
          <span><strong>SAQ 6 (3 Marks):</strong> What is the Model Code of Conduct (MCC)? When does it come into operational effect?</span>
        </summary>
        <div class="ans-content">
          <p><strong>Answer:</strong></p>
          <ul>
            <li><strong>Definition (1.5 Marks):</strong> The Model Code of Conduct is a set of ethical and legal guidelines formulated by consensus among political parties and enforced by the ECI to ensure free, fair, and clean election campaigns.</li>
            <li><strong>Operational Timing (1.5 Marks):</strong> It comes into force <strong>the exact minute and hour the ECI announces the election schedule</strong> at a national press conference, and remains legally operational until the final declaration of counting results.</li>
          </ul>
        </div>
      </details>

      <!-- ========================================= -->
      <!-- PART D: 4 LONG ANSWER QUESTIONS (5 MARKS) -->
      <!-- ========================================= -->
      <h3 class="subsection-title">
        <i class="fa-solid fa-file-lines" style="color: #6d28d9;"></i>
        Part D: Long Answer Questions (5 Marks with Marking Schemes)
      </h3>

      <!-- LAQ 1 -->
      <details class="ans-box">
        <summary class="ans-summary">
          <span><strong>LAQ 1 (5 Marks):</strong> Describe the constitutional composition, powers, and administrative responsibilities of the Election Commission of India (ECI).</span>
        </summary>
        <div class="ans-content">
          <p><strong>Step-by-Step Marking Scheme (CBSE 5 Marks):</strong></p>
          <ul>
            <li><em>Constitutional Basis & Autonomy (1 Mark)</em></li>
            <li><em>Structure & Composition (1 Mark)</em></li>
            <li><em>Key Powers & Administrative Responsibilities (3 Marks)</em></li>
          </ul>
          <hr style="margin: 0.8rem 0; border: none; border-top: 1px dashed #cbd5e1;">
          <p><strong>Model Answer:</strong></p>
          <ol>
            <li><strong>Constitutional Anchor (Article 324):</strong> Under Article 324, the ECI is an independent, permanent constitutional authority vested with the superintendence, direction, and conduct of elections to the Lok Sabha, Rajya Sabha, State Assemblies, and the Offices of President and Vice-President. It is completely independent of the executive.</li>
            <li><strong>Composition & Nirvachan Sadan:</strong> Headquartered at Nirvachan Sadan (New Delhi), it consists of a <strong>Chief Election Commissioner (CEC)</strong> and <strong>two Election Commissioners</strong>. They enjoy equal decision-making powers and are protected from arbitrary removal similar to Supreme Court judges.</li>
            <li><strong>Preparation and Revision of Electoral Rolls:</strong> ECI oversees the annual revision of voter lists, registering new 18-year-old citizens and issuing Electors Photo Identity Cards (EPIC).</li>
            <li><strong>Scheduling and Notification of Elections:</strong> Decides election dates, poll phases, counting schedules, and sets up over 1 million polling booths.</li>
            <li><strong>Enforcing the Model Code of Conduct (MCC):</strong> Monitors political rallies, censures candidates for hate speech, prevents misuse of government aircraft/cars, and curbs bribery.</li>
            <li><strong>Allotting Symbols and Countering Corrupt Practices:</strong> Recognizes national and state political parties, allots unique election symbols, deploys central forces, and cancels polls in booths affected by violence.</li>
          </ol>
        </div>
      </details>

      <!-- LAQ 2 -->
      <details class="ans-box">
        <summary class="ans-summary">
          <span><strong>LAQ 2 (5 Marks):</strong> Trace the step-by-step voting journey of a citizen on election day inside a modern Indian polling station.</span>
        </summary>
        <div class="ans-content">
          <p><strong>Marking Scheme:</strong> 1 Mark for entry & 1st Officer verification, 1 Mark for 2nd Officer ink & register, 1 Mark for 3rd Officer control activation, 1.5 Marks for Ballot Unit & VVPAT action, 0.5 Mark for secrecy enclosure.</p>
          <hr style="margin: 0.8rem 0; border: none; border-top: 1px dashed #cbd5e1;">
          <p><strong>Model Answer:</strong></p>
          <ol>
            <li><strong>Step 1: Identity Verification (1st Polling Officer):</strong> The voter enters the polling booth and presents their EPIC or approved government photo ID. The 1st Officer checks the name in the marked copy of the electoral roll, verifies identity, and announces the voter\'s name and serial number aloud.</li>
            <li><strong>Step 2: Inking and Registry (2nd Polling Officer):</strong> The 2nd Officer applies purple <strong>indelible ink</strong> (silver nitrate based) onto the voter\'s left index fingernail. The officer records the voter\'s signature or thumb impression in the <strong>Register of Voters (Form 17A)</strong> and issues a stamped paper voter slip.</li>
            <li><strong>Step 3: Machine Activation (3rd Polling Officer):</strong> The 3rd Officer collects the paper voter slip, verifies that the indelible ink mark is clearly visible, and presses the <strong>'Ballot' button</strong> on the EVM Control Unit. This unlocks the Ballot Unit inside the voting booth.</li>
            <li><strong>Step 4: Casting Vote in Secluded Booth:</strong> The voter enters the private voting compartment where the Ballot Unit and VVPAT are placed. The voter presses the blue button adjacent to their chosen candidate\'s name and symbol (or NOTA).</li>
            <li><strong>Step 5: Visual Verification & Acoustic Confirmation:</strong> A red LED illuminates next to the candidate. Instantly, the transparent window of the VVPAT machine displays a printed slip showing the candidate\'s serial number, name, and symbol for <strong>exactly 7 seconds</strong>. The slip then cuts and drops into a sealed audit container, followed by a loud 'BEEP' confirming the vote has been recorded!</li>
          </ol>
        </div>
      </details>

      <!-- LAQ 3 -->
      <details class="ans-box">
        <summary class="ans-summary">
          <span><strong>LAQ 3 (5 Marks):</strong> Compare and contrast the election of the Lok Sabha with the election of the President of India across five structural dimensions.</span>
        </summary>
        <div class="ans-content">
          <p><strong>Marking Scheme:</strong> 1 Mark for each clearly explained comparative point.</p>
          <hr style="margin: 0.8rem 0; border: none; border-top: 1px dashed #cbd5e1;">
          <p><strong>Model Answer (Comparative Matrix):</strong></p>
          <ol>
            <li><strong>Mode of Election:</strong> Lok Sabha is a <strong>Direct Election</strong> where all 968 million adult citizens vote directly; the President is elected through an <strong>Indirect Election</strong> by an Electoral College.</li>
            <li><strong>Electorate / Voting Body:</strong> Lok Sabha electorate consists of ordinary citizens aged 18+; Presidential Electoral College consists strictly of <strong>elected MPs</strong> (Lok Sabha & Rajya Sabha) and <strong>elected MLAs</strong> of all States, Delhi, and Puducherry.</li>
            <li><strong>Electoral System:</strong> Lok Sabha uses the <strong>First-Past-The-Post (FPTP)</strong> plurality system; the President is chosen via <strong>Proportional Representation with Single Transferable Vote (STV)</strong> and secret ballot.</li>
            <li><strong>Vote Value:</strong> In Lok Sabha, every citizen\'s vote has an exact uniform weight (1 vote = 1 unit); in Presidential elections, the vote value of an MLA or MP is calculated through complex population formulas (e.g., an MLA from populous UP has a higher vote value than an MLA from Sikkim).</li>
            <li><strong>Role and Function:</strong> Lok Sabha MPs represent direct popular local voices and pass laws; the President acts as the ceremonial Constitutional Head of State representing the collective federal unity of India.</li>
          </ol>
        </div>
      </details>

      <!-- LAQ 4 -->
      <details class="ans-box">
        <summary class="ans-summary">
          <span><strong>LAQ 4 (5 Marks):</strong> What are the four major challenges confronting modern Indian elections? Suggest concrete institutional and civic solutions for each.</span>
        </summary>
        <div class="ans-content">
          <p><strong>Marking Scheme:</strong> 2.5 Marks for 4 well-explained challenges + 2.5 Marks for corresponding practical solutions.</p>
          <hr style="margin: 0.8rem 0; border: none; border-top: 1px dashed #cbd5e1;">
          <p><strong>Model Answer:</strong></p>
          <ol>
            <li>
              <strong>Challenge 1: Rampant Money Power & Cash Bribery:</strong> Wealthy politicians spend hundreds of crores distributing cash, liquor, and freebies.<br>
              <em>Solution:</em> Enforce strict state funding of elections, deploy forensic expenditure flying squads, and encourage citizen reporting via the <strong>c-VIGIL smartphone app</strong> with mandated 100-minute police response.
            </li>
            <li>
              <strong>Challenge 2: Criminalization of Politics:</strong> Candidates with serious criminal charges contest and win elections.<br>
              <em>Solution:</em> Fast-track special courts to conclude trials of politicians within one year, and legally bar anyone against whom serious heinous crime charges have been framed by a court.
            </li>
            <li>
              <strong>Challenge 3: Urban Voter Apathy:</strong> Declining turnout among educated urbanites in metro cities (34% non-voters in 2024).<br>
              <em>Solution:</em> Set up polling booths inside high-rise housing societies, deploy Remote EVMs (R-EVMs) for migrant workers, and run aggressive youth engagement campaigns through college campus SVEEP programs.
            </li>
            <li>
              <strong>Challenge 4: Social Media Disinformation & Deepfakes:</strong> Viral fake news, communal reels, and AI voice clones manipulate voters.<br>
              <em>Solution:</em> Mandatory digital watermarking on AI content, strict 48-hour social media silence periods, and comprehensive media-literacy education in schools to verify sources before sharing.
            </li>
          </ol>
        </div>
      </details>

      <!-- ========================================= -->
      <!-- PART E: 2 COMPETENCY-BASED CASE STUDIES   -->
      <!-- ========================================= -->
      <h3 class="subsection-title">
        <i class="fa-solid fa-file-circle-question" style="color: #be123c;"></i>
        Part E: Competency-Based Source Analysis Case Studies
      </h3>

      <!-- CASE STUDY 1 -->
      <details class="ans-box">
        <summary class="ans-summary">
          <span><strong>Case Study 1:</strong> The Lone Polling Booths of Malogam and Gir Forest (Accessibility & Inclusion).</span>
        </summary>
        <div class="ans-content">
          <div style="background: #f8fafc; border-left: 4px solid #1e3a8a; padding: 1rem 1.25rem; margin-bottom: 1rem;">
            <p style="font-style: italic; font-size: 0.93rem; color: #1e293b; margin: 0;">
              <strong>Source Extract:</strong><br>
              "In the 2024 general elections, election officials in the northeastern border state of Arunachal Pradesh trekked across steep mountainous terrain, through dense forests and over suspension footbridges, to set up a polling station in Malogam village, Anjaw district. This fully staffed booth was established for just one registered voter: 44-year-old Sokela Tayang. Similarly, for years, the Election Commission maintained a polling booth inside Gujarat\'s Gir National Park for temple priest Mahant Bharatdas Darshandas. Across India, home voting was also extended to 85+ elderly citizens and persons with benchmark disabilities."
            </p>
          </div>

          <p><strong>Sub-Questions & Answers:</strong></p>
          <ol>
            <li>
              <strong>Why does the ECI spend massive public resources and send entire polling teams for a single voter? (1 Mark)</strong><br>
              <em>Answer:</em> To uphold the constitutional principle that <strong>every single citizen\'s vote has equal value</strong>, fulfilling the sacred ECI pledge: <em>"No voter is left behind"</em> regardless of geographic isolation.
            </li>
            <li>
              <strong>Which two categories of voters were provided doorstep home voting in 2024? (1 Mark)</strong><br>
              <em>Answer:</em> Senior citizens aged <strong>85 years and above</strong> and <strong>Persons with Disabilities (PwDs)</strong> with 40% or more benchmark disability.
            </li>
            <li>
              <strong>Identify the smartphone app introduced to assist voters with disabilities. (1 Mark)</strong><br>
              <em>Answer:</em> The <strong>Saksham App</strong> (developed by the Election Commission of India).
            </li>
            <li>
              <strong>What profound moral message does setting up a single-person polling station send to the world? (1 Mark)</strong><br>
              <em>Answer:</em> It demonstrates that in Indian democracy, individual citizenship rights are sacred, and the state will overcome any physical barrier to protect the sovereign democratic voice of even the loneliest citizen.
            </li>
          </ol>
        </div>
      </details>

      <!-- CASE STUDY 2 -->
      <details class="ans-box">
        <summary class="ans-summary">
          <span><strong>Case Study 2:</strong> Election Misconduct and the c-VIGIL Smartphone App.</span>
        </summary>
        <div class="ans-content">
          <div style="background: #f8fafc; border-left: 4px solid #b45309; padding: 1rem 1.25rem; margin-bottom: 1rem;">
            <p style="font-style: italic; font-size: 0.93rem; color: #1e293b; margin: 0;">
              <strong>Source Extract:</strong><br>
              "During an election campaign in a southern constituency, a candidate distributed silk sarees and high-end household kitchen appliances to female voters. Another candidate\'s convoy was intercepted by a police flying squad, uncovering bundles of ₹500 currency notes hidden inside the door panels of an SUV. Nearby, an alert college student used the ECI\'s c-VIGIL application to live-record a communal hate speech being delivered outside a place of worship. Within 15 minutes, election flying squads arrived on the spot."
            </p>
          </div>

          <p><strong>Sub-Questions & Answers:</strong></p>
          <ol>
            <li>
              <strong>Which specific election code of conduct was violated by the candidate distributing sarees and cash? (1 Mark)</strong><br>
              <em>Answer:</em> The <strong>Model Code of Conduct (MCC)</strong>, specifically the provisions prohibiting voter bribery, financial inducements, and corrupt expenditure.
            </li>
            <li>
              <strong>How does the c-VIGIL app prevent false or fabricated complaints from being uploaded? (1 Mark)</strong><br>
              <em>Answer:</em> The app does not permit uploading pre-recorded gallery files; it requires users to capture live photos or 2-minute live videos directly through the camera, automatically tagging the exact <strong>geographic GPS coordinates and timestamp</strong>.
            </li>
            <li>
              <strong>What is the mandated official response timeline for flying squads responding to a c-VIGIL alert? (1 Mark)</strong><br>
              <em>Answer:</em> Flying squads are mandated to reach the location and investigate within <strong>100 minutes</strong> of the complaint being lodged.
            </li>
            <li>
              <strong>Why is citizen vigilance considered the most powerful safeguard of democratic governance? (1 Mark)</strong><br>
              <em>Answer:</em> Government monitors cannot be present everywhere. When 968 million citizens act as vigilant eyes and ears of democracy, corrupt politicians can no longer bribe voters or break laws in secret.
            </li>
          </ol>
        </div>
      </details>

      <!-- ========================================= -->
      <!-- PART F: 5 PYQS & MOST PROBABLE QUESTIONS  -->
      <!-- ========================================= -->
      <h3 class="subsection-title">
        <i class="fa-solid fa-clock-rotate-left" style="color: #047857;"></i>
        Part F: Previous Years Questions (PYQs) & Most Probable Exam Questions
      </h3>

      <!-- PYQ 1 -->
      <details class="ans-box">
        <summary class="ans-summary">
          <span><strong>PYQ 1:</strong> What is an "Electoral Roll"? Why is it revised annually by the Election Commission?</span>
        </summary>
        <div class="ans-content">
          <p><strong>Answer:</strong></p>
          <ul>
            <li><strong>Definition:</strong> An <strong>Electoral Roll</strong> (commonly known as the Voter List) is the official register maintained by the ECI containing the names, photos, addresses, and voter ID numbers of all eligible citizens registered to vote in a specific constituency.</li>
            <li><strong>Need for Annual Revision:</strong>
              <ol>
                <li><strong>Enrolling Youth:</strong> To add newly eligible 18-year-old citizens who attained legal adulthood during the year.</li>
                <li><strong>Removing Deceased Persons:</strong> To delete names of citizens who have passed away, preventing identity theft and fraudulent votes.</li>
                <li><strong>Updating Address Changes:</strong> To transfer names of citizens who permanently shifted to new residential areas.</li>
              </ol>
            </li>
          </ul>
        </div>
      </details>

      <!-- PYQ 2 -->
      <details class="ans-box">
        <summary class="ans-summary">
          <span><strong>PYQ 2:</strong> Who was Shyam Saran Negi and why does Indian democratic history honor him?</span>
        </summary>
        <div class="ans-content">
          <p><strong>Answer:</strong></p>
          <ul>
            <li><strong>Identity:</strong> Shyam Saran Negi (1917–2022) was a primary school teacher from Kalpa village in Kinnaur, Himachal Pradesh.</li>
            <li><strong>Historical First Voter:</strong> He cast the <strong>very first vote in independent India\'s history on 25 October 1951</strong> during early snow-bound polling for the 1952 general elections.</li>
            <li><strong>Lifelong Democratic Icon:</strong> He voted consistently in 34 consecutive elections over 71 years until his demise at the age of 105, symbolizing the unwavering patriotic duty of an Indian voter.</li>
          </ul>
        </div>
      </details>

      <!-- PYQ 3 -->
      <details class="ans-box">
        <summary class="ans-summary">
          <span><strong>PYQ 3:</strong> What is the First-Past-The-Post (FPTP) system? Illustrate with a numerical example.</span>
        </summary>
        <div class="ans-content">
          <p><strong>Answer:</strong></p>
          <ul>
            <li><strong>Meaning:</strong> The <strong>First-Past-The-Post (FPTP)</strong> system is an electoral method where the candidate who wins more votes than any other individual candidate in a single-member constituency is declared the winner. An absolute majority (more than 50%) is NOT required.</li>
            <li><strong>Numerical Illustration:</strong>
              <ul>
                <li>Total valid votes cast: 100,000</li>
                <li>Candidate A receives: 36,000 votes (36%)</li>
                <li>Candidate B receives: 34,000 votes (34%)</li>
                <li>Candidate C receives: 30,000 votes (30%)</li>
                <li><em>Outcome:</em> Candidate A is declared elected, even though 64% of voters chose someone else! This is exactly how India\'s Lok Sabha and Vidhan Sabha elections operate.</li>
              </ul>
            </li>
          </ul>
        </div>
      </details>

      <!-- PYQ 4 -->
      <details class="ans-box">
        <summary class="ans-summary">
          <span><strong>PYQ 4:</strong> What is a "Coalition Government"? When does a coalition become necessary?</span>
        </summary>
        <div class="ans-content">
          <p><strong>Answer:</strong></p>
          <ul>
            <li><strong>Definition:</strong> A <strong>Coalition Government</strong> is an alliance formed by two or more political parties that join together to form a government and run the executive administration.</li>
            <li><strong>When Necessary:</strong> In the Lok Sabha (543 seats), a single party requires at least <strong>272 seats</strong> (a simple majority) to form the national government. If no single party crosses this magic threshold (a "hung parliament"), multiple parties combine their seats, draft a Common Minimum Programme, and elect a consensus leader as Prime Minister.</li>
          </ul>
        </div>
      </details>

      <!-- PYQ 5 -->
      <details class="ans-box">
        <summary class="ans-summary">
          <span><strong>PYQ 5:</strong> Distinguish between the functions of a Returning Officer (RO) and a Presiding Officer.</span>
        </summary>
        <div class="ans-content">
          <p><strong>Answer:</strong></p>
          <ul>
            <li><strong>Returning Officer (RO):</strong> Appointed for an <strong>entire parliamentary or assembly constituency</strong>. Scrutinizes candidate nomination papers, allots election symbols, supervises counting across all booths, and officially declares the winning MP/MLA.</li>
            <li><strong>Presiding Officer:</strong> Appointed to manage a <strong>single polling station (booth)</strong> on voting day. Conducts mock polls, supervises polling staff, ensures voter secrecy, seals EVMs/VVPATs after polling ends, and deposits them at the strongroom.</li>
          </ul>
        </div>
      </details>
    </section>
'''
