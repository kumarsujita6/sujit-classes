# -*- coding: utf-8 -*-
"""
Part 8: Section 5 - Complete Exam Question Bank for Class 8 SST Chapter 9.
Chapter: India's Long Road to Independence (NCERT NEP Code: hess109 / hees202)
Contains:
- Part A: 5 Conceptual MCQs with Interactive Quiz Engine & Trap Explanations
- Part B: 5 Assertion & Reasoning Questions (CBSE Board Pattern)
- Part C: 6 Short Answer Questions (2M / 3M)
- Part D: 4 Long Answer Questions (5M) with Step-by-Step Marking Schemes
- Part E: 2 Competency-Based Case Studies with Source Extracts
- Part F: 5 Previous Years Questions (PYQs) & High-Probability Exam Questions
Total: 27 Comprehensive Exam Questions with 100% Model Answers.
"""

PART8_CONTENT = '''
    <!-- ========================================== -->
    <!-- SECTION 5: COMPLETE EXAM QUESTION BANK    -->
    <!-- ========================================== -->
    <section class="section-wrapper" id="section-5">
      <div class="section-header">
        <span class="section-badge" style="background:#dbeafe; color:#1e40af;"><i class="fa-solid fa-graduation-cap"></i> Section 5</span>
        <h2 class="section-title">Complete Exam Question Bank</h2>
        <p class="section-desc">
          An exhaustive bank of 27 high-yield exam questions covering all cognitive levels: interactive MCQs with trap analyses, Assertion &amp; Reasoning, 2M/3M short answers, 5M long answers with marking schemes, competency case studies, and PYQs.
        </p>
      </div>

      <!-- Live Score Counter Bar -->
      <div style="background:#ffffff; border:1px solid var(--border); border-radius:var(--radius-md); padding:0.85rem 1.25rem; margin-bottom:1.75rem; display:flex; align-items:center; justify-content:space-between; box-shadow:var(--shadow-sm);">
        <div style="font-weight:700; color:var(--dark); font-size:0.95rem;">
          <i class="fa-solid fa-trophy" style="color:#eab308; margin-right:8px;"></i> Interactive Quiz Progress:
        </div>
        <div style="font-size:0.95rem; font-weight:800; color:var(--primary);">
          Score: <span id="quiz-score">0</span> / 5
        </div>
      </div>

      <!-- ========================================== -->
      <!-- PART A: 5 CONCEPTUAL MCQS WITH TRAP ALERTS -->
      <!-- ========================================== -->
      <h3 style="font-family:'Space Grotesk',sans-serif; font-size:1.35rem; color:var(--dark); margin: 1.5rem 0 1rem; border-left: 4px solid var(--primary); padding-left: 0.75rem;">
        Part A: 5 Conceptual MCQs with Interactive Quiz Engine &amp; Trap Alerts
      </h3>

      <!-- MCQ 1 -->
      <div class="quiz-card" id="mcq-card-1">
        <div class="quiz-q-title">
          1. In 1905, Viceroy Lord Curzon announced the Partition of Bengal on the official pretext of administrative convenience. What was the real political motive of the British Empire?
        </div>
        <div class="quiz-options-list">
          <button class="quiz-opt-btn" onclick="checkAnswer(1, 0, false)">
            <span>A) To establish Dhaka as the new winter imperial capital of British India.</span>
          </button>
          <button class="quiz-opt-btn" onclick="checkAnswer(1, 1, true)">
            <span>B) To shatter the intellectual nerve center of Indian nationalism by dividing Hindus and Muslims along communal lines.</span>
          </button>
          <button class="quiz-opt-btn" onclick="checkAnswer(1, 2, false)">
            <span>C) To develop the handloom silk and jute mills of East Bengal independently.</span>
          </button>
          <button class="quiz-opt-btn" onclick="checkAnswer(1, 3, false)">
            <span>D) To build an exclusive deep-water naval base on the Bay of Bengal for the Royal Navy.</span>
          </button>
        </div>
        <div class="quiz-feedback" id="feedback-1">
          <strong>Correct Answer: (B)</strong>
          <br><strong>Historical Justification:</strong> Bengal was the epicentre of anti-colonial intellectual resistance. Curzon deliberately carved out a Muslim-majority Eastern Bengal &amp; Assam and a Hindu-majority West Bengal to pit communities against each other under the classic imperial strategy of <em>"Divide and Rule"</em>.
          <br><strong style="color:#b91c1c;">Exam Hall Trap Alert:</strong> Do not fall for Option (A) or (C)! Administrative convenience was only the deceptive official excuse put forward in colonial government communiqués.
        </div>
      </div>

      <!-- MCQ 2 -->
      <div class="quiz-card" id="mcq-card-2">
        <div class="quiz-q-title">
          2. Why did Mahatma Gandhi choose the British Salt Monopoly as the central issue to launch the nationwide Civil Disobedience Movement in 1930?
        </div>
        <div class="quiz-options-list">
          <button class="quiz-opt-btn" onclick="checkAnswer(2, 0, false)">
            <span>A) Because salt was an elite luxury commodity used only by wealthy urban merchants.</span>
          </button>
          <button class="quiz-opt-btn" onclick="checkAnswer(2, 1, false)">
            <span>B) Because British salt was heavily subsidized, causing losses to Indian industrialists.</span>
          </button>
          <button class="quiz-opt-btn" onclick="checkAnswer(2, 2, true)">
            <span>C) Because salt was a universal daily necessity consumed by every Indian, making the salt tax a direct, cruel symbol of foreign oppression against the poorest peasant.</span>
          </button>
          <button class="quiz-opt-btn" onclick="checkAnswer(2, 3, false)">
            <span>D) Because the British government had offered to exempt handspun cotton cloth from all duties.</span>
          </button>
        </div>
        <div class="quiz-feedback" id="feedback-2">
          <strong>Correct Answer: (C)</strong>
          <br><strong>Historical Justification:</strong> Nature provides salt free along India's 7,500 km coastline. By taxing this basic survival food, the British Raj touched the daily life of every single man, woman, and child, allowing Gandhi to unite all social classes, castes, and religions into one emotional moral struggle.
          <br><strong style="color:#b91c1c;">Exam Hall Trap Alert:</strong> Students often mistakenly choose Option (B) thinking of industrial tariffs. Salt satyagraha was chosen precisely because it was non-industrial and universally felt by the rural poor.
        </div>
      </div>

      <!-- MCQ 3 -->
      <div class="quiz-card" id="mcq-card-3">
        <div class="quiz-q-title">
          3. What was the core ideological reason that Bhagat Singh and Chandrashekhar Azad renamed the HRA to the 'Hindustan Socialist Republican Association' (HSRA) in September 1928?
        </div>
        <div class="quiz-options-list">
          <button class="quiz-opt-btn" onclick="checkAnswer(3, 0, false)">
            <span>A) To merge their secret society with the Indian National Congress.</span>
          </button>
          <button class="quiz-opt-btn" onclick="checkAnswer(3, 1, true)">
            <span>B) To declare that their struggle sought not just political independence, but an egalitarian socialist society free from the exploitation of man by man.</span>
          </button>
          <button class="quiz-opt-btn" onclick="checkAnswer(3, 2, false)">
            <span>C) To renounce armed resistance and contest provincial legislative elections.</span>
          </button>
          <button class="quiz-opt-btn" onclick="checkAnswer(3, 3, false)">
            <span>D) To seek financial subsidies from the British House of Commons.</span>
          </button>
        </div>
        <div class="quiz-feedback" id="feedback-3">
          <strong>Correct Answer: (B)</strong>
          <br><strong>Historical Justification:</strong> At the Feroz Shah Kotla ruins in Delhi, Bhagat Singh emphasized that merely replacing British rulers with Indian capitalists would change nothing for the starving workers and peasants. The goal of the revolution was Socialism—abolishing human exploitation and securing power for labor.
          <br><strong style="color:#b91c1c;">Exam Hall Trap Alert:</strong> A common student blunder is viewing Bhagat Singh as an impulsive terrorist. In reality, he was a voracious reader of Marxist and socialist literature who championed a classless, secular society.
        </div>
      </div>

      <!-- MCQ 4 -->
      <div class="quiz-card" id="mcq-card-4">
        <div class="quiz-q-title">
          4. How did the Poona Pact of September 1932 resolve the acute political impasse between Mahatma Gandhi and Dr. B.R. Ambedkar?
        </div>
        <div class="quiz-options-list">
          <button class="quiz-opt-btn" onclick="checkAnswer(4, 0, false)">
            <span>A) By implementing separate electorates for Dalits in all 11 British provinces.</span>
          </button>
          <button class="quiz-opt-btn" onclick="checkAnswer(4, 1, true)">
            <span>B) By abandoning separate electorates in favor of joint electorates, while more than doubling reserved seats for Depressed Classes from 71 to 148.</span>
          </button>
          <button class="quiz-opt-btn" onclick="checkAnswer(4, 2, false)">
            <span>C) By completely abolishing all reservations for Depressed Classes in legislatures.</span>
          </button>
          <button class="quiz-opt-btn" onclick="checkAnswer(4, 3, false)">
            <span>D) By referring the untouchability question to the League of Nations for arbitration.</span>
          </button>
        </div>
        <div class="quiz-feedback" id="feedback-4">
          <strong>Correct Answer: (B)</strong>
          <br><strong>Historical Justification:</strong> Signed in Yerwada jail, the Poona Pact achieved a brilliant national compromise: it preserved the social solidarity of the general electorate (preventing communal fragmentation) while drastically increasing political representation for Dalits from 71 to 148 seats.
          <br><strong style="color:#b91c1c;">Exam Hall Trap Alert:</strong> Do not choose Option (A)! Gandhi fasted unto death specifically to <em>abolish</em> separate electorates.
        </div>
      </div>

      <!-- MCQ 5 -->
      <div class="quiz-card" id="mcq-card-5">
        <div class="quiz-q-title">
          5. Which military event in February 1946 conclusively demonstrated to the British Government that it could no longer rely on the armed forces to suppress Indian independence?
        </div>
        <div class="quiz-options-list">
          <button class="quiz-opt-btn" onclick="checkAnswer(5, 0, false)">
            <span>A) The Chapekar Brothers' assassination of Commissioner Rand in Pune.</span>
          </button>
          <button class="quiz-opt-btn" onclick="checkAnswer(5, 1, false)">
            <span>B) The Battle of Buribalam fought by Bagha Jatin in Balasore.</span>
          </button>
          <button class="quiz-opt-btn" onclick="checkAnswer(5, 2, true)">
            <span>C) The Royal Indian Navy (RIN) Mutiny, where 20,000 ratings across 78 warships revolted against British officers.</span>
          </button>
          <button class="quiz-opt-btn" onclick="checkAnswer(5, 3, false)">
            <span>D) The signing of the Gandhi-Irwin Pact in New Delhi.</span>
          </button>
        </div>
        <div class="quiz-feedback" id="feedback-5">
          <strong>Correct Answer: (C)</strong>
          <br><strong>Historical Justification:</strong> The British held India with the sword of the Indian soldier and sailor. When 20,000 naval ratings mutinied on 78 ships, accompanied by sympathy strikes in the Air Force and Army Signal Corps, British Prime Minister Clement Attlee realized that continuing imperial rule was militarily impossible.
          <br><strong style="color:#b91c1c;">Exam Hall Trap Alert:</strong> Options (A) and (B) took place in 1897 and 1915 respectively, decades before the 1946 transfer of power!
        </div>
      </div>

      <!-- ========================================== -->
      <!-- PART B: 5 ASSERTION & REASONING QUESTIONS -->
      <!-- ========================================== -->
      <h3 style="font-family:'Space Grotesk',sans-serif; font-size:1.35rem; color:var(--dark); margin: 2.5rem 0 1rem; border-left: 4px solid var(--primary); padding-left: 0.75rem;">
        Part B: 5 Assertion &amp; Reasoning Questions (CBSE Board Pattern)
      </h3>
      <p style="font-size:0.9rem; color:var(--text-muted); margin-bottom:1.25rem;">
        <strong>Directions:</strong> In each question, two statements are given—one labeled <strong>Assertion (A)</strong> and the other labeled <strong>Reason (R)</strong>. Select the correct option:
        <br>(A) Both (A) and (R) are true, and (R) is the correct explanation of (A).
        <br>(B) Both (A) and (R) are true, but (R) is NOT the correct explanation of (A).
        <br>(C) (A) is true, but (R) is false.
        <br>(D) (A) is false, but (R) is true.
      </p>

      <!-- A&R 1 -->
      <details class="ans-box">
        <summary class="ans-summary">
          <span><i class="fa-solid fa-circle-question" style="color:#c2410c; margin-right:8px;"></i> A&amp;R Question 1: Tagore's Renunciation of British Knighthood (1919)</span>
        </summary>
        <div class="ans-content">
          <p><strong>Assertion (A):</strong> Rabindranath Tagore renounced his prestigious British Knighthood in May 1919.</p>
          <p><strong>Reason (R):</strong> The brutal, unprovoked massacre of over a thousand unarmed civilians at Jallianwala Bagh under General Dyer's orders made British imperial titles a source of glaring humiliation and shame.</p>
          <div class="step-card">
            <div class="step-label">Correct Option: (A)</div>
            <div class="step-text">
              <strong>Both (A) and (R) are true, and (R) is the correct explanation of (A).</strong>
              <br>Tagore was deeply agonized when news of the Amritsar massacre reached him. In his historic letter to Viceroy Lord Chelmsford on 31 May 1919, he explicitly stated that imperial honours had become intolerable in the context of such inhuman degradation, and he wished to stand shorn of all distinctions alongside his suffering countrymen.
            </div>
          </div>
        </div>
      </details>

      <!-- A&R 2 -->
      <details class="ans-box">
        <summary class="ans-summary">
          <span><i class="fa-solid fa-circle-question" style="color:#c2410c; margin-right:8px;"></i> A&amp;R Question 2: Nationwide Boycott of the Simon Commission (1927–28)</span>
        </summary>
        <div class="ans-content">
          <p><strong>Assertion (A):</strong> The Simon Commission was greeted across India with universal black-flag demonstrations and thunderous chants of "Simon Go Back!".</p>
          <p><strong>Reason (R):</strong> The seven-member statutory commission appointed by the British Parliament was an all-white body that did not include a single Indian member to deliberate on India's constitutional future.</p>
          <div class="step-card">
            <div class="step-label">Correct Option: (A)</div>
            <div class="step-text">
              <strong>Both (A) and (R) are true, and (R) is the correct explanation of (A).</strong>
              <br>Indians of all political parties (Congress, Muslim League, Liberal Federation) viewed the total exclusion of Indians as a direct insult to national self-respect and self-determination, sparking unanimous black-flag boycotts across the country.
            </div>
          </div>
        </div>
      </details>

      <!-- A&R 3 -->
      <details class="ans-box">
        <summary class="ans-summary">
          <span><i class="fa-solid fa-circle-question" style="color:#c2410c; margin-right:8px;"></i> A&amp;R Question 3: Sudden Withdrawal of Non-Cooperation Movement (1922)</span>
        </summary>
        <div class="ans-content">
          <p><strong>Assertion (A):</strong> Mahatma Gandhi abruptly suspended the nationwide Non-Cooperation Movement on 12 February 1922.</p>
          <p><strong>Reason (R):</strong> An infuriated mob burned down the Chauri Chaura police station in Gorakhpur, killing 22 policemen, which violated the fundamental condition of nonviolence (Ahimsa).</p>
          <div class="step-card">
            <div class="step-label">Correct Option: (A)</div>
            <div class="step-text">
              <strong>Both (A) and (R) are true, and (R) is the correct explanation of (A).</strong>
              <br>Gandhi believed that true Satyagraha could never rely on mob violence. He felt that continuing the movement after the Chauri Chaura arson would descend into chaos and give the British military moral justification to ruthlessly crush unarmed citizens.
            </div>
          </div>
        </div>
      </details>

      <!-- A&R 4 -->
      <details class="ans-box">
        <summary class="ans-summary">
          <span><i class="fa-solid fa-circle-question" style="color:#c2410c; margin-right:8px;"></i> A&amp;R Question 4: Ideological Approach of Early Moderates</span>
        </summary>
        <div class="ans-content">
          <p><strong>Assertion (A):</strong> Early Moderate leaders of the Congress were criticized as "political mendicants" by Assertive Nationalists like Bal Gangadhar Tilak.</p>
          <p><strong>Reason (R):</strong> Early Moderates believed that violent armed conspiracies were the only effective means to drive the British out of India.</p>
          <div class="step-card">
            <div class="step-label">Correct Option: (C)</div>
            <div class="step-text">
              <strong>(A) is true, but (R) is false.</strong>
              <br><strong>Explanation:</strong> Assertion (A) is completely true: Assertive Nationalists condemned the Moderates' polite appeals as political begging (*mendicancy*). However, Reason (R) is completely false: the Moderates vehemently opposed violence; they believed in the "3Ps" (Prayer, Petition, and Protest) and had faith in British constitutional fair play.
            </div>
          </div>
        </div>
      </details>

      <!-- A&R 5 -->
      <details class="ans-box">
        <summary class="ans-summary">
          <span><i class="fa-solid fa-circle-question" style="color:#c2410c; margin-right:8px;"></i> A&amp;R Question 5: Separate Electorates in 1909 Morley-Minto Reforms</span>
        </summary>
        <div class="ans-content">
          <p><strong>Assertion (A):</strong> The Morley-Minto Reforms of 1909 introduced Separate Electorates for Muslims in provincial legislative councils.</p>
          <p><strong>Reason (R):</strong> The British colonial administration sought to foster genuine inter-communal unity and build a secular composite Indian nation.</p>
          <div class="step-card">
            <div class="step-label">Correct Option: (C)</div>
            <div class="step-text">
              <strong>(A) is true, but (R) is false.</strong>
              <br><strong>Explanation:</strong> Assertion (A) is historically accurate. Reason (R) is entirely false: the colonial rulers introduced Separate Electorates specifically to divide Hindus and Muslims into separate political camps, weakening national solidarity under their deliberate policy of "Divide and Rule".
            </div>
          </div>
        </div>
      </details>

      <!-- ========================================== -->
      <!-- PART C: 6 SHORT ANSWER QUESTIONS (2M / 3M) -->
      <!-- ========================================== -->
      <h3 style="font-family:'Space Grotesk',sans-serif; font-size:1.35rem; color:var(--dark); margin: 2.5rem 0 1rem; border-left: 4px solid var(--primary); padding-left: 0.75rem;">
        Part C: 6 Short Answer Questions (2 Marks &amp; 3 Marks)
      </h3>

      <!-- SAQ 1 -->
      <details class="ans-box">
        <summary class="ans-summary">
          <span><i class="fa-solid fa-pen-nib" style="color:#c2410c; margin-right:8px;"></i> SAQ 1 (3 Marks): What was the "Drain of Wealth" theory? Name two nationalists who formulated it.</span>
        </summary>
        <div class="ans-content">
          <p><strong>Model Answer (Point-Wise):</strong></p>
          <div class="step-card">
            <div class="step-label">Core Definition (1.5 Marks)</div>
            <div class="step-text">
              The <strong>"Drain of Wealth"</strong> was the systematic, unilateral transfer of Indian economic revenues, raw materials, and peasant taxes to Britain without any commercial, financial, or material return to India.
              <br>• It occurred through <strong>Home Charges</strong> (pensions, salaries, and interest on public debt paid in London), <strong>guaranteed 5% railway profits</strong> to British investors, and <strong>unrequited exports</strong> of Indian agricultural produce.
            </div>
          </div>
          <div class="step-card">
            <div class="step-label">Key Nationalists (1.5 Marks)</div>
            <div class="step-text">
              1. <strong>Dadabhai Naoroji:</strong> Formulated the theory mathematically in his landmark book <em>Poverty and Un-British Rule in India</em> (1901).
              <br>2. <strong>Romesh Chunder Dutt (R.C. Dutt):</strong> Detailed the destruction of Indian agriculture and crafts in his classic work <em>The Economic History of India</em>.
            </div>
          </div>
        </div>
      </details>

      <!-- SAQ 2 -->
      <details class="ans-box">
        <summary class="ans-summary">
          <span><i class="fa-solid fa-pen-nib" style="color:#c2410c; margin-right:8px;"></i> SAQ 2 (2 Marks): State two major differences between the Moderates and Assertive Nationalists.</span>
        </summary>
        <div class="ans-content">
          <p><strong>Model Answer (Comparative Matrix):</strong></p>
          <div class="step-card">
            <div class="step-label">Comparison Points (2 Marks)</div>
            <div class="step-text">
              1. <strong>Ultimate Goal:</strong> Moderates aimed for gradual administrative reforms and <em>Dominion Status</em> within the British Empire; Assertive Nationalists demanded <strong>Swaraj (Self-Rule)</strong> as an inalienable birthright.
              <br>2. <strong>Methods of Struggle:</strong> Moderates relied on constitutional <em>"Prayer, Petition, and Protest"</em> (3Ps) appealing to British fair play; Assertive Nationalists relied on <strong>Swadeshi, nationwide Boycott, National Education, and mass agitation</strong>.
            </div>
          </div>
        </div>
      </details>

      <!-- SAQ 3 -->
      <details class="ans-box">
        <summary class="ans-summary">
          <span><i class="fa-solid fa-pen-nib" style="color:#c2410c; margin-right:8px;"></i> SAQ 3 (3 Marks): Why did the Rowlatt Act of 1919 provoke intense fury across India?</span>
        </summary>
        <div class="ans-content">
          <p><strong>Model Answer (Point-Wise):</strong></p>
          <div class="step-card">
            <div class="step-label">Three Key Reasons (3 Marks)</div>
            <div class="step-text">
              1. <strong>Arrest Without Warrant &amp; Trial:</strong> It empowered the police to arrest any Indian on mere suspicion and detain them in prison for up to <strong>two years without a formal trial or jury</strong>.
              <br>2. <strong>Suppression of Fundamental Rights:</strong> It suspended the writ of <em>Habeas Corpus</em>, gagged the vernacular press, and denied legal counsel, famously condemned as <strong>"No Dalil, No Vakil, No Appeal"</strong>.
              <br>3. <strong>Betrayal of Wartime Loyalty:</strong> Indians had contributed over a million soldiers to fight for Britain in World War I, expecting constitutional self-rule; receiving a tyrannical police law instead was seen as a cruel insult.
            </div>
          </div>
        </div>
      </details>

      <!-- SAQ 4 -->
      <details class="ans-box">
        <summary class="ans-summary">
          <span><i class="fa-solid fa-pen-nib" style="color:#c2410c; margin-right:8px;"></i> SAQ 4 (3 Marks): Describe the role played by revolutionary secret societies like Anushilan Samiti and Jugantar.</span>
        </summary>
        <div class="ans-content">
          <p><strong>Model Answer (Point-Wise):</strong></p>
          <div class="step-card">
            <div class="step-label">Three Historic Contributions (3 Marks)</div>
            <div class="step-text">
              1. <strong>Physical &amp; Ideological Training:</strong> They opened physical culture clubs (*akharas*) across Bengal and Maharashtra, training youths in sword-fighting, wrestling, guerrilla tactics, and patriotic reading.
              <br>2. <strong>Targeted Executions of Tyrants:</strong> They established clandestine bomb factories (e.g. Muraripukur in Calcutta) to execute cruel colonial officials, such as Douglas Kingsford (Muzaffarpur bomb, 1908).
              <br>3. <strong>Igniting Fearless Courage:</strong> The serene martyrdom of members like 18-year-old Khudiram Bose shattered the myth of British invincibility and inspired millions of ordinary Indians to shed fear of colonial prisons.
            </div>
          </div>
        </div>
      </details>

      <!-- SAQ 5 -->
      <details class="ans-box">
        <summary class="ans-summary">
          <span><i class="fa-solid fa-pen-nib" style="color:#c2410c; margin-right:8px;"></i> SAQ 5 (2 Marks): What was the historical significance of the 1916 Lucknow Pact?</span>
        </summary>
        <div class="ans-content">
          <p><strong>Model Answer (Point-Wise):</strong></p>
          <div class="step-card">
            <div class="step-label">Two Core Milestones (2 Marks)</div>
            <div class="step-text">
              1. <strong>Congress Reunification:</strong> It healed the 9-year rift of the 1907 Surat Split, reuniting the Assertive Nationalists (under Tilak) with the Moderates under one banner.
              <br>2. <strong>Congress-League Hindu-Muslim Front:</strong> The Indian National Congress and the All-India Muslim League signed a joint agreement to present common constitutional demands for self-government to the British Crown, creating a formidable united national platform.
            </div>
          </div>
        </div>
      </details>

      <!-- SAQ 6 -->
      <details class="ans-box">
        <summary class="ans-summary">
          <span><i class="fa-solid fa-pen-nib" style="color:#c2410c; margin-right:8px;"></i> SAQ 6 (3 Marks): Mention three heroic underground activities carried out during the 1942 Quit India Movement.</span>
        </summary>
        <div class="ans-content">
          <p><strong>Model Answer (Point-Wise):</strong></p>
          <div class="step-card">
            <div class="step-label">Three Underground Deeds (3 Marks)</div>
            <div class="step-text">
              1. <strong>Clandestine Congress Radio:</strong> 22-year-old <strong>Usha Mehta</strong> and her team set up secret mobile radio transmitters broadcasting uncensored news of protests and Gandhi's messages across India.
              <br>2. <strong>Guerrilla Networks:</strong> Leaders like <strong>Jayaprakash Narayan</strong> and Ram Manohar Lohia escaped from Hazaribagh prison and organized the <em>Azad Dasta</em> underground armed squads in the Nepal border forests.
              <br>3. <strong>Parallel Free Governments (Prati Sarkar):</strong> Rebels displaced British authorities and set up self-governing local administrations, notably the <strong>Tamluk Jatiya Sarkar</strong> in Bengal and <strong>Nana Patil's Prati Sarkar</strong> in Satara.
            </div>
          </div>
        </div>
      </details>

      <!-- ========================================== -->
      <!-- PART D: 4 LONG ANSWER QUESTIONS (5 MARKS)  -->
      <!-- ========================================== -->
      <h3 style="font-family:'Space Grotesk',sans-serif; font-size:1.35rem; color:var(--dark); margin: 2.5rem 0 1rem; border-left: 4px solid var(--primary); padding-left: 0.75rem;">
        Part D: 4 Long Answer Questions (5 Marks Each with Marking Schemes)
      </h3>

      <!-- LAQ 1 -->
      <details class="ans-box">
        <summary class="ans-summary">
          <span><i class="fa-solid fa-file-pen" style="color:#c2410c; margin-right:8px;"></i> LAQ 1 (5 Marks): Causes, Programs, and Significance of the 1905 Swadeshi &amp; Boycott Movement</span>
        </summary>
        <div class="ans-content">
          <div class="step-card">
            <div class="step-label">Step-by-Step Marking Scheme</div>
            <div class="step-text">
              • <strong>Causes / Triggers:</strong> 1.5 Marks
              <br>• <strong>Programs of Resistance (Swadeshi &amp; Boycott):</strong> 2.0 Marks
              <br>• <strong>Historical Significance &amp; Outcome:</strong> 1.5 Marks
            </div>
          </div>
          <div class="step-card">
            <div class="step-label">1. Causes &amp; Triggers of the Movement</div>
            <div class="step-text">
              • <strong>Imperial Partition of Bengal (1905):</strong> Lord Curzon partitioned Bengal on 16 October 1905 to divide the nationalist hub along communal lines into Muslim-majority East Bengal and Hindu-majority West Bengal under the pretext of administrative efficiency.
              <br>• <strong>Deepening Economic Despair:</strong> Continuous famines, destruction of Indian handloom weavers, and drain of wealth created immense anger against British trade monopolies.
            </div>
          </div>
          <div class="step-card">
            <div class="step-label">2. Core Programs of the Movement</div>
            <div class="step-text">
              • <strong>Total Boycott:</strong> Bonfires of imported Manchester factory cloth, foreign salt, and sugar at crossroads; picketing shops; lawyers boycotting British law courts.
              <br>• <strong>Economic Swadeshi:</strong> Revival of native handlooms; establishment of indigenous mills like Tata Swadeshi Mills and Acharya P.C. Ray's <em>Bengal Chemicals</em>; V.O. Chidambaram Pillai's Swadeshi shipping company in Tuticorin.
              <br>• <strong>National Education:</strong> Creation of the National Council of Education (1906) and Bengal National College under Sri Aurobindo, teaching modern sciences in vernacular languages.
              <br>• <strong>Cultural Mobilisation:</strong> Mass singing of Bankim Chandra's <em>"Vande Mataram"</em>; Tagore leading the <em>Raksha Bandhan</em> fraternity ceremony on the streets of Calcutta.
            </div>
          </div>
          <div class="step-card">
            <div class="step-label">3. Historical Significance &amp; Outcome</div>
            <div class="step-text">
              • <strong>Forced Annulment:</strong> The British were forced to reunite Bengal in December 1911 at the Delhi Durbar, proving that determined mass resistance could defeat imperial decrees.
              <br>• <strong>Transformation of Nationalism:</strong> Ended the era of elite Moderate petitions and established self-reliance (*Atma-shakti*) and mass mobilization as the main engines of the freedom movement.
            </div>
          </div>
        </div>
      </details>

      <!-- LAQ 2 -->
      <details class="ans-box">
        <summary class="ans-summary">
          <span><i class="fa-solid fa-file-pen" style="color:#c2410c; margin-right:8px;"></i> LAQ 2 (5 Marks): "The Dandi Salt March was a Masterpiece of Mass Mobilisation." Justify.</span>
        </summary>
        <div class="ans-content">
          <div class="step-card">
            <div class="step-label">Step-by-Step Marking Scheme</div>
            <div class="step-text">
              • <strong>Choice of Salt as a Symbol:</strong> 1.0 Mark
              <br>• <strong>The 24-Day March Strategy:</strong> 1.0 Mark
              <br>• <strong>Breaking the Law at Dandi:</strong> 1.0 Mark
              <br>• <strong>Pan-Indian Echo &amp; Social Breadth:</strong> 1.0 Mark
              <br>• <strong>International Impact &amp; Political Parity:</strong> 1.0 Mark
            </div>
          </div>
          <div class="step-card">
            <div class="step-label">Model Answer (Five Structured Arguments)</div>
            <div class="step-text">
              1. <strong>Genius Choice of a Universal Symbol:</strong> Salt is an essential daily necessity consumed by the poorest beggar and richest landlord alike. By targeting the British salt monopoly, Gandhi transformed a simple dietary ingredient into an explosive moral issue that united all castes, creeds, and classes.
              <br>2. <strong>The 24-Day Theatrical Pilgrimage:</strong> Walking 240 miles on foot through dozens of villages over 24 days allowed Gandhi to hold daily prayer meetings, educate thousands of villagers, recruit satyagrahis, and build nationwide emotional suspense before the law was actually broken.
              <br>3. <strong>The Moment of Defiance (6 April 1930):</strong> Picking up a lump of natural sea salt at Dandi was a nonviolent, sublime gesture that anyone anywhere could replicate. It turned passive citizens into active lawbreakers.
              <br>4. <strong>Unprecedented Pan-Indian Echo:</strong> The march sparked illegal salt manufacturing across India: Sarojini Naidu at Dharasana, Rajagopalachari at Vedaranyam, Kelappan in Kerala, and Gopabandhu Choudhury and Rama Devi at <strong>Inchudi in Balasore, Odisha</strong>. It drew thousands of sheltered women onto the streets for the first time.
              <br>5. <strong>Global Moral Victory &amp; Parity:</strong> International reporters (like Webb Miller) documented British police brutality, destroying Britain's claim to moral superiority. It forced Viceroy Lord Irwin to negotiate with Gandhi on equal terms, leading to the historic Gandhi-Irwin Pact of 1931.
            </div>
          </div>
        </div>
      </details>

      <!-- LAQ 3 -->
      <details class="ans-box">
        <summary class="ans-summary">
          <span><i class="fa-solid fa-file-pen" style="color:#c2410c; margin-right:8px;"></i> LAQ 3 (5 Marks): Netaji Subhas Chandra Bose &amp; The Azad Hind Fauj (INA) in India's Liberation</span>
        </summary>
        <div class="ans-content">
          <div class="step-card">
            <div class="step-label">Step-by-Step Marking Scheme</div>
            <div class="step-text">
              • <strong>Ideology &amp; Forward Bloc:</strong> 1.0 Mark
              <br>• <strong>The Great Escape &amp; Submarine Odyssey:</strong> 1.0 Mark
              <br>• <strong>Formation of INA &amp; Provisional Govt:</strong> 1.0 Mark
              <br>• <strong>Rani of Jhansi Regiment &amp; Military Offensive:</strong> 1.0 Mark
              <br>• <strong>Red Fort Trials &amp; Strategic Impact:</strong> 1.0 Mark
            </div>
          </div>
          <div class="step-card">
            <div class="step-label">Model Answer</div>
            <div class="step-text">
              • <strong>1. Ideological Clarity:</strong> Netaji believed that World War II provided India with an unprecedented opportunity to strike colonial Britain. Resigning from Congress, he founded the Forward Bloc (1939) to prepare for direct action.
              <br>• <strong>2. The Epic Escape &amp; Global Diplomacy:</strong> Escaping British house arrest in Calcutta in January 1941 disguised as "Ziauddin", he journeyed across Afghanistan and Russia to Berlin, later completing a perilous 90-day submarine voyage to Tokyo in 1943.
              <br>• <strong>3. The Provisional Government &amp; INA Command:</strong> In Singapore (October 1943), Netaji assumed command of the Indian National Army (INA) and founded the <em>Provisional Government of Free India</em>, giving the immortal battle cries <strong>"Jai Hind!"</strong> and <strong>"Chalo Dilli!"</strong>.
              <br>• <strong>4. Pioneering Gender Equality &amp; Military Assault:</strong> Created the <strong>Rani of Jhansi Regiment</strong> under Captain Lakshmi Sahgal—the first female combat unit in modern Asia. The INA advanced into Burma and hoisted the Indian Tricolour on Indian soil at Moirang (Manipur) in April 1944.
              <br>• <strong>5. Breaking Colonial Military Loyalty:</strong> The post-war Red Fort trials of Prem Sahgal, Gurbaksh Dhillon, and Shah Nawaz Khan united all Indian communities and directly triggered the 1946 Royal Indian Navy Mutiny, destroying the British Empire's military foundation.
            </div>
          </div>
        </div>
      </details>

      <!-- LAQ 4 -->
      <details class="ans-box">
        <summary class="ans-summary">
          <span><i class="fa-solid fa-file-pen" style="color:#c2410c; margin-right:8px;"></i> LAQ 4 (5 Marks): Why Was Quit India Called "The Most Serious Rebellion Since 1857"?</span>
        </summary>
        <div class="ans-content">
          <div class="step-card">
            <div class="step-label">Step-by-Step Marking Scheme</div>
            <div class="step-text">
              • <strong>Context &amp; "Do or Die" Call:</strong> 1.0 Mark
              <br>• <strong>Leaderless Character Post-Zero Hour:</strong> 1.0 Mark
              <br>• <strong>Scale of Defiance &amp; Parallel Governments:</strong> 1.5 Marks
              <br>• <strong>Brutality of Colonial Repression:</strong> 1.0 Mark
              <br>• <strong>Decisive Strategic Impact on Independence:</strong> 0.5 Mark
            </div>
          </div>
          <div class="step-card">
            <div class="step-label">Model Answer</div>
            <div class="step-text">
              Viceroy Lord Linlithgow confessed in a secret cable to Prime Minister Winston Churchill that the Quit India uprising was <em>"by far the most serious rebellion since that of 1857"</em> for five major reasons:
              <br>1. <strong>Uncompromising Mantra:</strong> On 8 August 1942 at Gowalia Tank, Gandhi gave the ultimate call: <strong>"Do or Die" (Karo ya Maro)</strong>. There was no demand for piecemeal reforms; the only demand was total and immediate British evacuation.
              <br>2. <strong>Leaderless Mass Spontaneity:</strong> When the British arrested the entire top Congress leadership on the morning of 9 August in <em>Operation Zero Hour</em>, the movement did not die. Deprived of leaders, ordinary citizens took over, paralyzing cities, factories, and railways on an unprecedented scale.
              <br>3. <strong>Establishment of Parallel Governments (Prati Sarkar):</strong> In places like Balia (Chittu Pandey), Tamluk (Jatiya Sarkar), and Satara (Nana Patil), British colonial administration was completely overthrown and independent Indian administrations functioned for weeks or months.
              <br>4. <strong>Underground Heroism &amp; Mass Sacrifice:</strong> Women and youth led the fight: Aruna Asaf Ali hoisted the flag, Usha Mehta operated the Secret Congress Radio, 73-year-old Matangini Hazra faced bullets chanting "Vande Mataram", and tribal leader Lakshman Nayak mobilized Odisha.
              <br>5. <strong>Unprecedented Military Repression:</strong> The British had to deploy 57 army battalions, use machine-gun fire from aircraft, arrest over 100,000 people, and slaughter an estimated 10,000 citizens. Though brutally suppressed, Quit India destroyed British administrative legitimacy forever.
            </div>
          </div>
        </div>
      </details>

      <!-- ========================================== -->
      <!-- PART E: 2 COMPETENCY-BASED CASE STUDIES   -->
      <!-- ========================================== -->
      <h3 style="font-family:'Space Grotesk',sans-serif; font-size:1.35rem; color:var(--dark); margin: 2.5rem 0 1rem; border-left: 4px solid var(--primary); padding-left: 0.75rem;">
        Part E: 2 Competency-Based Case Studies with Source Extracts
      </h3>

      <!-- Case Study 1 -->
      <details class="ans-box">
        <summary class="ans-summary">
          <span><i class="fa-solid fa-file-lines" style="color:#c2410c; margin-right:8px;"></i> Case Study 1: Sri Aurobindo on Passive Resistance and Swaraj (1907 Source)</span>
        </summary>
        <div class="ans-content">
          <p><strong>Read the following primary source extract and answer the questions that follow:</strong></p>
          <div style="background:#fff7ed; border-left:4px solid #ea580c; padding:1rem; border-radius:6px; font-style:italic; margin-bottom:1rem; font-size:0.92rem;">
            "Political freedom is the life-breath of a nation; to attempt social reform, educational reform, industrial expansion, the moral betterment of the race without political freedom is the very height of human folly... The primary method of our resistance must be passive: the refusal to help the colonial administration in the exploitation of our country, the refusal to attend British schools, the refusal to accept foreign goods, and the refusal to submit disputes to British courts."
            <br><span style="font-weight:700; font-style:normal; display:block; margin-top:6px; text-align:right;">— Sri Aurobindo Ghose, <em>Bande Mataram</em> (April 1907)</span>
          </div>

          <div class="step-card">
            <div class="step-label">Question (a): Why did Sri Aurobindo call political freedom the "life-breath of a nation"? (1.5 Marks)</div>
            <div class="step-text">Just as a living organism cannot survive or develop without breathing air, a nation cannot achieve true social justice, industrial prosperity, or moral dignity while remaining in foreign political chains. Self-rule is the essential precondition for all other progress.</div>
          </div>

          <div class="step-card">
            <div class="step-label">Question (b): Identify two concrete methods of "passive resistance" mentioned in the text. (1.5 Marks)</div>
            <div class="step-text">1. Boycotting British educational institutions and establishing independent national schools.
              <br>2. Boycotting British law courts and resolving legal disputes through native community arbitration panchayats.</div>
          </div>

          <div class="step-card">
            <div class="step-label">Question (c): How did this doctrine foreshadow Mahatma Gandhi's Non-Cooperation Movement? (1 Mark)</div>
            <div class="step-text">Aurobindo's 1907 doctrine of refusing to assist colonial administration through systematic boycotts of schools, courts, and foreign goods became the exact foundational operational blueprint adopted by Mahatma Gandhi in the 1920 Non-Cooperation Movement.</div>
          </div>
        </div>
      </details>

      <!-- Case Study 2 -->
      <details class="ans-box">
        <summary class="ans-summary">
          <span><i class="fa-solid fa-file-lines" style="color:#c2410c; margin-right:8px;"></i> Case Study 2: The Dual Realities of August 1947: Joy and Partition Agony</span>
        </summary>
        <div class="ans-content">
          <p><strong>Read the following historical analysis extract and answer the questions that follow:</strong></p>
          <div style="background:#eff6ff; border-left:4px solid #2563eb; padding:1rem; border-radius:6px; font-style:italic; margin-bottom:1rem; font-size:0.92rem;">
            "August 1947 was a moment of extraordinary paradox in world history. While church bells chimed, fireworks illuminated the night skies of Delhi, and the Tricolour replaced the Union Jack over the Red Fort, across the newly drawn Radcliffe Line in Punjab and Bengal, millions of terrified human beings were fleeing on foot, leaving behind ancestral lands, homes, and memories. Trains arrived at railway stations carrying dead bodies. Independence brought the joy of triumph, but Partition left an enduring scar across the subcontinent."
          </div>

          <div class="step-card">
            <div class="step-label">Question (a): What was the "extraordinary paradox" of August 1947? (1.5 Marks)</div>
            <div class="step-text">The paradox was that the supreme historic joy of achieving national independence after 90 years of colonial slavery was accompanied simultaneously by the horrific human catastrophe of Partition, involving communal slaughter and mass displacement.</div>
          </div>

          <div class="step-card">
            <div class="step-label">Question (b): What was the Radcliffe Line and why was its execution tragic? (1.5 Marks)</div>
            <div class="step-text">The Radcliffe Line was the boundary line drawn by British lawyer Sir Cyril Radcliffe partitioning Punjab and Bengal. It was tragic because Radcliffe, who had never visited India, drew the line in just five weeks using outdated census maps. Slicing through villages, canals, and households, its secret announcement two days after independence triggered mass panic.</div>
          </div>

          <div class="step-card">
            <div class="step-label">Question (c): How many people were displaced during Partition? (1 Mark)</div>
            <div class="step-text">Over 15 million people were forcibly uprooted from their homes, constituting the largest forced human migration in world history, with an estimated 1 to 2 million lives lost in communal violence.</div>
          </div>
        </div>
      </details>

      <!-- ========================================== -->
      <!-- PART F: 5 PREVIOUS YEARS QUESTIONS (PYQS) -->
      <!-- ========================================== -->
      <h3 style="font-family:'Space Grotesk',sans-serif; font-size:1.35rem; color:var(--dark); margin: 2.5rem 0 1rem; border-left: 4px solid var(--primary); padding-left: 0.75rem;">
        Part F: 5 Previous Years Questions (PYQs) &amp; High-Probability Exam Questions
      </h3>

      <!-- PYQ 1 -->
      <details class="ans-box">
        <summary class="ans-summary">
          <span><i class="fa-solid fa-award" style="color:#c2410c; margin-right:8px;"></i> PYQ 1 (CBSE): Why was the Simon Commission boycotted? Describe the tragic consequence of the Lahore protest.</span>
        </summary>
        <div class="ans-content">
          <p><strong>Model Answer (Point-Wise):</strong></p>
          <div class="step-card">
            <div class="step-label">Reasons for Boycott (1.5 Marks)</div>
            <div class="step-text">
              1. <strong>All-White Composition:</strong> The statutory commission appointed in November 1927 contained seven British MPs but not a single Indian member.
              <br>2. <strong>Denial of Self-Determination:</strong> Indians rightly asserted that foreigners had no moral or democratic authority to judge India's readiness for constitutional self-government.
            </div>
          </div>
          <div class="step-card">
            <div class="step-label">The Tragic Consequence in Lahore (1.5 Marks)</div>
            <div class="step-text">
              • On 30 October 1928, veteran leader <strong>Lala Lajpat Rai</strong> led a peaceful black-flag demonstration outside Lahore railway station chanting <em>"Simon Go Back!"</em>.
              <br>• Senior British police officers ordered a merciless lathi charge. Lalaji was brutally struck on the head and chest. He succumbed to his injuries on 17 November 1928, after roaring his historic warning that every blow on him would be a nail in the coffin of the British Empire.
            </div>
          </div>
        </div>
      </details>

      <!-- PYQ 2 -->
      <details class="ans-box">
        <summary class="ans-summary">
          <span><i class="fa-solid fa-award" style="color:#c2410c; margin-right:8px;"></i> PYQ 2 (CBSE): Explain the significance of the 1929 Lahore Congress Session. Why was 26 January celebrated as Independence Day?</span>
        </summary>
        <div class="ans-content">
          <p><strong>Model Answer (Point-Wise):</strong></p>
          <div class="step-card">
            <div class="step-label">Significance of Lahore Session 1929 (1.5 Marks)</div>
            <div class="step-text">
              1. <strong>Presided over by Jawaharlal Nehru:</strong> Represented the ascendancy of the dynamic young generation in Congress.
              <br>2. <strong>Historic Purna Swaraj Resolution:</strong> Formally discarded all demands for Dominion Status and proclaimed <strong>Complete Independence (Purna Swaraj)</strong> as the non-negotiable goal.
              <br>3. <strong>Unfurling the Tricolour:</strong> At midnight on 31 December 1929, Nehru hoisted the National Tricolour on the banks of the river Ravi.
            </div>
          </div>
          <div class="step-card">
            <div class="step-label">Why 26 January Was Celebrated (1.5 Marks)</div>
            <div class="step-text">
              • The Congress resolved that Sunday, <strong>26 January 1930</strong>, would be observed across India as the first <strong>Independence Day</strong>, with citizens gathering to take the solemn pledge of complete independence.
              <br>• To honor and preserve this sacred historic date in national memory, the Constitution of India was formally brought into force on <strong>26 January 1950</strong>, celebrated ever since as <strong>Republic Day</strong>.
            </div>
          </div>
        </div>
      </details>

      <!-- PYQ 3 -->
      <details class="ans-box">
        <summary class="ans-summary">
          <span><i class="fa-solid fa-award" style="color:#c2410c; margin-right:8px;"></i> PYQ 3 (CBSE): How did Sardar Vallabhbhai Patel integrate over 560 Princely States into the Indian Union?</span>
        </summary>
        <div class="ans-content">
          <p><strong>Model Answer (Point-Wise):</strong></p>
          <div class="step-card">
            <div class="step-label">Sardar Patel's Historic Feat (3 Marks)</div>
            <div class="step-text">
              1. <strong>The Crisis:</strong> British paramountcy lapsed on 15 August 1947, giving 565 princely rulers the legal option to join India, Pakistan, or declare independence, threatening the "Balkanisation" of India.
              <br>2. <strong>Patel's Diplomatic Masterstroke:</strong> Appointed Minister of States with V.P. Menon as Secretary, Patel appealed to the patriotism and royal wisdom of rulers, offering the <em>Instrument of Accession</em> whereby states surrendered only three subjects: <strong>Defense, Foreign Affairs, and Communications</strong>, retaining internal autonomy and receiving privy purses.
              <br>3. <strong>Firm Action Against Defiant States:</strong> When the Nawab of Junagadh fled to Pakistan against his people's will, a plebiscite integrated it. When the Nizam of Hyderabad unleashed the terror of the Razakars, Patel launched <em>Operation Polo</em> (police action) in September 1948, completing the territorial unification of India.
            </div>
          </div>
        </div>
      </details>

      <!-- PYQ 4 -->
      <details class="ans-box">
        <summary class="ans-summary">
          <span><i class="fa-solid fa-award" style="color:#c2410c; margin-right:8px;"></i> PYQ 4 (CBSE): What were the catastrophic consequences of the Partition of India in August 1947?</span>
        </summary>
        <div class="ans-content">
          <p><strong>Model Answer (Point-Wise):</strong></p>
          <div class="step-card">
            <div class="step-label">Four Major Consequences (3 Marks)</div>
            <div class="step-text">
              1. <strong>Mass Forced Migration:</strong> Over 15 million Hindus, Sikhs, and Muslims were uprooted from ancestral soils, trekking in vast refugee columns across newly drawn borders.
              <br>2. <strong>Unprecedented Communal Slaughter:</strong> Between 1 to 2 million innocent lives were lost in horrific fratricidal massacres, especially across Punjab and Bengal.
              <br>3. <strong>Atrocities on Women:</strong> Tens of thousands of women were abducted, assaulted, and disfigured by communal mobs on both sides of the border.
              <br>4. <strong>Long-Term Geopolitical Rift:</strong> Created permanent diplomatic hostility, wars, and nuclear rivalry between India and Pakistan, diverting precious resources from poverty eradication.
            </div>
          </div>
        </div>
      </details>

      <!-- PYQ 5 -->
      <details class="ans-box">
        <summary class="ans-summary">
          <span><i class="fa-solid fa-award" style="color:#c2410c; margin-right:8px;"></i> PYQ 5 (BSE Odisha Exam Favorite): Discuss the Role of Odisha's Patriots in Salt Satyagraha and Quit India.</span>
        </summary>
        <div class="ans-content">
          <p><strong>Model Answer (Point-Wise):</strong></p>
          <div class="step-card">
            <div class="step-label">Odisha's Valiant Contributions (3 Marks)</div>
            <div class="step-text">
              1. <strong>Inchudi Salt Satyagraha (1930):</strong> Under Gopabandhu Choudhury, Acharya Harihar, and Maa Rama Devi, Inchudi in Balasore became the second most prominent salt defiance center in India, where hundreds of women manufactured contraband salt.
              <br>2. <strong>Martyr Baji Rout (1938):</strong> A 12-year-old boat boy from Dhenkanal who fearlessly refused to ferry British armed police across the flooded Brahmani river and was shot dead on the spot, becoming India's youngest national martyr.
              <br>3. <strong>Heroic Martyrdom of Lakshman Nayak (1942–43):</strong> Tribal leader of Koraput who mobilized thousands of adivasis in nonviolent forest defiance; falsely charged and hanged by the British in Berhampur jail on 29 March 1943.
              <br>4. <strong>Eram Massacre (Bhadrak, 1942):</strong> Celebrated as <em>"Rakta Tirtha"</em> (The Pilgrimage of Blood) where British police opened indiscriminate fire on a peaceful Quit India assembly, killing 29 satyagrahis on the spot—Odisha's Jallianwala Bagh.
            </div>
          </div>
        </div>
      </details>
    </section>
'''
