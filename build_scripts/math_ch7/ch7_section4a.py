# -*- coding: utf-8 -*-
"""
Module: ch7_section4a.py
Contains Section 4 (Part A): 100% Solved NCERT In-Text Examples (Examples 1 to 12)
and In-Text Activities & Math Talks, presented in rigorous 5-step pedagogical format.
"""

def get_section4a():
    return """
    <!-- ========================================== -->
    <!-- SECTION 4: 100% SOLVED NCERT QUESTIONS     -->
    <!-- ========================================== -->
    <section id="section4">
      <div class="section-header">
        <div class="section-tag"><i class="fa-solid fa-pen-ruler"></i> Exhaustive NCERT Solutions</div>
        <h2 class="section-title">Section 4: 100% Solved NCERT Questions &amp; Inquiries</h2>
        <p class="section-desc">
          Every single in-text example, classroom activity, Math Talk prompt, and "Figure it Out" problem solved step-by-step in our signature 5-step presentation inside collapsible self-testing boxes.
        </p>
      </div>

      <!-- PART A: IN-TEXT EXAMPLES (EXAMPLES 1 TO 12) -->
      <h3 class="subheading"><i class="fa-solid fa-graduation-cap"></i> Part 4.1: Solved In-Text Examples (Examples 1 to 12)</h3>

      <!-- EXAMPLE 1 -->
      <details class="ans-box" id="ex1">
        <summary>Example 1: Are the ratios 3 : 4 and 72 : 96 proportional? (NCERT Page 162)</summary>
        <div class="ans-content">
          <div class="step-container">
            <div class="step-box step-1">
              <span class="step-badge">Step 1: Given Information &amp; Goal</span>
              <p>Two ratios are given: <em>Ratio 1 = 3 : 4</em> and <em>Ratio 2 = 72 : 96</em>. We must determine whether these two ratios are in proportion.</p>
            </div>
            <div class="step-box step-2">
              <span class="step-badge">Step 2: Proportionality Criterion</span>
              <p>Two ratios are proportional if and only if their simplest forms are identical, or equivalently, if the product of extremes equals the product of means (<em>a × d = b × c</em>).</p>
            </div>
            <div class="step-box step-3">
              <span class="step-badge">Step 3: Step-by-Step Simplification &amp; Calculation</span>
              <p>
                • <strong>Ratio 1:</strong> 3 : 4 is already in simplest form since HCF(3, 4) = 1.
                <br>• <strong>Ratio 2:</strong> To simplify 72 : 96, find the HCF of 72 and 96:
                <br>&nbsp;&nbsp;Prime factors of 72 = 2³ × 3² = 8 × 9
                <br>&nbsp;&nbsp;Prime factors of 96 = 2⁵ × 3¹ = 32 × 3
                <br>&nbsp;&nbsp;HCF(72, 96) = 2³ × 3¹ = 24.
                <br>Dividing both terms by 24:
                <br>&nbsp;&nbsp;72 ÷ 24 = 3
                <br>&nbsp;&nbsp;96 ÷ 24 = 4
                <br>&nbsp;&nbsp;Simplest Form of 72 : 96 = <strong>3 : 4</strong>.
              </p>
            </div>
            <div class="step-box step-4">
              <span class="step-badge">Step 4: Alternative Cross-Product Verification</span>
              <p>
                Let <em>a = 3, b = 4, c = 72, d = 96</em>.
                <br>Extremes product = <em>a × d = 3 × 96 = 288</em>.
                <br>Means product = <em>b × c = 4 × 72 = 288</em>.
                <br>Since <em>a × d = b × c = 288</em>, the ratios are strictly proportional!
              </p>
            </div>
            <div class="step-box step-5">
              <span class="step-badge">Step 5: Final Concluding Answer</span>
              <p><strong>Yes, the ratios 3 : 4 and 72 : 96 are proportional.</strong> We write: <strong>3 : 4 :: 72 : 96</strong>.</p>
            </div>
          </div>
        </div>
      </details>

      <!-- EXAMPLE 2 -->
      <details class="ans-box" id="ex2">
        <summary>Example 2: Kesang's Lemonade Sugar Scaling (NCERT Page 162-163)</summary>
        <div class="ans-content">
          <div class="step-container">
            <div class="step-box step-1">
              <span class="step-badge">Step 1: Given Information &amp; Goal</span>
              <p>
                • Initial batch: 6 glasses of lemonade require 10 spoons of sugar.
                <br>• Father asks her to make 18 more glasses of lemonade.
                <br>• Goal: Find how many spoons of sugar she should add to maintain identical sweetness.
              </p>
            </div>
            <div class="step-box step-2">
              <span class="step-badge">Step 2: Mathematical Modelling</span>
              <p>
                To preserve sweetness, the ratio of glasses of lemonade to spoons of sugar must be proportional:
                <br><em>Glasses : Sugar :: Glasses : Sugar</em> ⇒ <strong>6 : 10 :: 18 : x</strong>
              </p>
            </div>
            <div class="step-box step-3">
              <span class="step-badge">Step 3: Calculating Factor of Change</span>
              <p>
                Factor of change in the first term = <em>18 ÷ 6 = 3</em>.
                <br>Since the number of glasses increased by a factor of 3, the sugar must also increase by the same factor:
                <br><em>x = 10 × 3 = 30 spoons</em>.
                <br>Alternatively, by cross-multiplication: <em>6 × x = 10 × 18 ⇒ 6x = 180 ⇒ x = 180 / 6 = 30</em>.
              </p>
            </div>
            <div class="step-box step-4">
              <span class="step-badge">Step 4: Verification &amp; Total Lemonade Context</span>
              <p>
                • Ratio for 18 glasses: 18 : 30 = 3 : 5 (divided by 6).
                <br>• Initial ratio: 6 : 10 = 3 : 5 (divided by 2). Both ratios are identical (0.6 glasses per spoon).
                <br><em>Note:</em> If considering the entire celebration batch (6 + 18 = 24 glasses), the total sugar needed would be <em>10 + 30 = 40 spoons</em> (24 : 40 = 3 : 5).
              </p>
            </div>
            <div class="step-box step-5">
              <span class="step-badge">Step 5: Final Concluding Answer</span>
              <p><strong>Kesang should add 30 spoons of sugar</strong> to make 18 glasses of lemonade with the exact same sweetness.</p>
            </div>
          </div>
        </div>
      </details>

      <!-- EXAMPLE 3 -->
      <details class="ans-box" id="ex3">
        <summary>Example 3: Nitin and Hari's Compound Wall Strength (NCERT Page 163)</summary>
        <div class="ans-content">
          <div class="step-container">
            <div class="step-box step-1">
              <span class="step-badge">Step 1: Given Information &amp; Goal</span>
              <p>
                • Nitin builds a wall of length 60 ft using 3 bags of cement.
                <br>• Hari builds a wall of length 40 ft using 2 bags of cement.
                <br>• Nitin worries Hari's wall is weaker because she used less cement. Is Nitin correct?
              </p>
            </div>
            <div class="step-box step-2">
              <span class="step-badge">Step 2: Mathematical Criterion of Strength</span>
              <p>
                The strength of the wall depends on the ratio of wall length to cement bags used (or cement per foot of wall). The walls will be equally strong if the ratios are proportional:
                <br>Ratio for Nitin: <em>Length : Cement = 60 : 3</em>
                <br>Ratio for Hari: <em>Length : Cement = 40 : 2</em>
              </p>
            </div>
            <div class="step-box step-3">
              <span class="step-badge">Step 3: Calculating Simplest Ratios</span>
              <p>
                • Nitin's ratio = 60 : 3 = (60 ÷ 3) : (3 ÷ 3) = <strong>20 : 1</strong> (20 ft of wall per 1 bag of cement).
                <br>• Hari's ratio = 40 : 2 = (40 ÷ 2) : (2 ÷ 2) = <strong>20 : 1</strong> (20 ft of wall per 1 bag of cement).
              </p>
            </div>
            <div class="step-box step-4">
              <span class="step-badge">Step 4: Consistency Check</span>
              <p>
                In both cases, exactly 1 bag of cement is used for every 20 feet of wall. The concentration of cement per foot of wall is identical (<em>1/20 bag/ft</em>).
              </p>
            </div>
            <div class="step-box step-5">
              <span class="step-badge">Step 5: Final Concluding Answer</span>
              <p><strong>Nitin is NOT correct in his thinking.</strong> Both walls use exactly the same proportion of cement (20 ft per bag). Hari used fewer bags simply because her wall was shorter. Both walls are equally strong, so Nitin should not worry!</p>
            </div>
          </div>
        </div>
      </details>

      <!-- EXAMPLE 4 -->
      <details class="ans-box" id="ex4">
        <summary>Example 4: School Teacher-to-Student Ratio Comparison (NCERT Page 163)</summary>
        <div class="ans-content">
          <div class="step-container">
            <div class="step-box step-1">
              <span class="step-badge">Step 1: Given Information &amp; Goal</span>
              <p>
                • Reference school: 5 teachers and 170 students.
                <br>• Goal: Find the teacher-to-student ratio and compare with a standard school (e.g., a school with 10 teachers and 340 students).
              </p>
            </div>
            <div class="step-box step-2">
              <span class="step-badge">Step 2: Ratio Setup &amp; Simplification</span>
              <p>
                Teacher-to-student ratio = <em>Number of Teachers : Number of Students = 5 : 170</em>.
                <br>Divide both terms by HCF(5, 170) = 5:
                <br><em>(5 ÷ 5) : (170 ÷ 5) = 1 : 34</em>.
              </p>
            </div>
            <div class="step-box step-3">
              <span class="step-badge">Step 3: Pedagogical Interpretation</span>
              <p>
                A ratio of <strong>1 : 34</strong> means there is 1 teacher for every 34 students. Under the Right to Education (RTE) Act guidelines in India, the recommended pupil-teacher ratio (PTR) for upper primary classes is 35 : 1. Thus, 1 : 34 is very healthy.
              </p>
            </div>
            <div class="step-box step-4">
              <span class="step-badge">Step 4: Proportional Comparison with Sample School</span>
              <p>
                Suppose your school has 12 teachers and 408 students:
                <br>Ratio = 12 : 408 = (12 ÷ 12) : (408 ÷ 12) = <strong>1 : 34</strong>.
                <br>Since <em>5 : 170 :: 12 : 408</em> (both equal 1 : 34), the ratios are proportional!
              </p>
            </div>
            <div class="step-box step-5">
              <span class="step-badge">Step 5: Final Concluding Answer</span>
              <p>The simplest teacher-to-student ratio in the reference school is <strong>1 : 34</strong>. Any school where the number of students is exactly 34 times the number of teachers has a proportional ratio.</p>
            </div>
          </div>
        </div>
      </details>

      <!-- EXAMPLE 5 -->
      <details class="ans-box" id="ex5">
        <summary>Example 5: Classroom Blackboard Dimensions &amp; Drawing Scale (NCERT Page 163)</summary>
        <div class="ans-content">
          <div class="step-container">
            <div class="step-box step-1">
              <span class="step-badge">Step 1: Given Information &amp; Measurement</span>
              <p>
                • Standard classroom blackboard measurement: Width = 240 cm, Height = 120 cm.
                <br>• Goal: Find the aspect ratio (width : height) and draw a proportional rectangle in a student notebook.
              </p>
            </div>
            <div class="step-box step-2">
              <span class="step-badge">Step 2: Aspect Ratio Reduction</span>
              <p>
                Width : Height = 240 : 120.
                <br>HCF(240, 120) = 120.
                <br>Dividing by 120: <em>(240 ÷ 120) : (120 ÷ 120) = <strong>2 : 1</strong></em>.
              </p>
            </div>
            <div class="step-box step-3">
              <span class="step-badge">Step 3: Scaling Down for Notebook Drawing</span>
              <p>
                To draw a proportional rectangle in a student notebook, choose a scale factor:
                <br>• Student A chooses scale 1 cm = 20 cm: Width = 12 cm, Height = 6 cm (Ratio 12 : 6 = 2 : 1).
                <br>• Student B chooses scale 1 cm = 30 cm: Width = 8 cm, Height = 4 cm (Ratio 8 : 4 = 2 : 1).
                <br>• Student C chooses scale 1 cm = 40 cm: Width = 6 cm, Height = 3 cm (Ratio 6 : 3 = 2 : 1).
              </p>
            </div>
            <div class="step-box step-4">
              <span class="step-badge">Step 4: Verification &amp; Class Discussion</span>
              <p>
                Do all drawings look the same?
                <br>They have <strong>different sizes</strong>, but they all have the <strong>exact same shape</strong> (aspect ratio 2 : 1). All these rectangles are geometrically similar.
              </p>
            </div>
            <div class="step-box step-5">
              <span class="step-badge">Step 5: Final Concluding Answer</span>
              <p>The blackboard aspect ratio is <strong>2 : 1</strong>. Any rectangle drawn with width twice its height (e.g., 10 cm × 5 cm, 8 cm × 4 cm) is proportional to the blackboard.</p>
            </div>
          </div>
        </div>
      </details>

      <!-- EXAMPLE 6 -->
      <details class="ans-box" id="ex6">
        <summary>Example 6: Neelima and Mother's Age Ratio Analysis (NCERT Page 164)</summary>
        <div class="ans-content">
          <div class="step-container">
            <div class="step-box step-1">
              <span class="step-badge">Step 1: Given Information &amp; Goal</span>
              <p>
                • At age 3, Neelima's mother's age was 10 times her age: Mother's age = 3 × 10 = 30 years.
                <br>• Goal: Find the age ratio when Neelima is 3 years old, and when Neelima is 12 years old. Determine if the ratio remains the same.
              </p>
            </div>
            <div class="step-box step-2">
              <span class="step-badge">Step 2: Computing Initial Age Ratio</span>
              <p>
                Initial Age of Neelima = 3 years; Mother = 30 years.
                <br>Ratio = 3 : 30 = (3 ÷ 3) : (30 ÷ 3) = <strong>1 : 10</strong>.
              </p>
            </div>
            <div class="step-box step-3">
              <span class="step-badge">Step 3: Computing Ratio 9 Years Later</span>
              <p>
                When Neelima is 12 years old, <em>12 - 3 = 9 years</em> have elapsed.
                <br>Mother's age = 30 + 9 = 39 years.
                <br>New Ratio = 12 : 39.
                <br>Divide by HCF(12, 39) = 3:
                <br><em>(12 ÷ 3) : (39 ÷ 3) = <strong>4 : 13</strong></em>.
              </p>
            </div>
            <div class="step-box step-4">
              <span class="step-badge">Step 4: Proportionality Test</span>
              <p>
                Compare 1 : 10 and 4 : 13:
                <br>1 / 10 = 0.10 &nbsp;vs&nbsp; 4 / 13 ≈ 0.3077.
                <br>Cross-multiplication: 1 × 13 = 13, but 10 × 4 = 40. Since 13 ≠ 40, the ratios are <strong>NOT proportional</strong>.
              </p>
            </div>
            <div class="step-box step-5">
              <span class="step-badge">Step 5: Final Concluding Answer</span>
              <p>The initial ratio is <strong>1 : 10</strong>, and the ratio at age 12 is <strong>4 : 13</strong>. <strong>No, the ratio does NOT remain the same.</strong> Adding the same number to both terms of a ratio changes the ratio.</p>
            </div>
          </div>
        </div>
      </details>

      <!-- EXAMPLE 7 -->
      <details class="ans-box" id="ex7">
        <summary>Example 7: Missing Numbers Proportional to 14 : 21 (NCERT Page 164)</summary>
        <div class="ans-content">
          <div class="step-container">
            <div class="step-box step-1">
              <span class="step-badge">Step 1: Given Information &amp; Goal</span>
              <p>
                Base ratio: <strong>14 : 21</strong> (Simplest form: 14 ÷ 7 : 21 ÷ 7 = <strong>2 : 3</strong>).
                <br>Find the missing values in:
                <br>(i) [__] : 42 &nbsp;&nbsp;&nbsp; (ii) 6 : [__] &nbsp;&nbsp;&nbsp; (iii) 2 : [__]
              </p>
            </div>
            <div class="step-box step-2">
              <span class="step-badge">Step 2: Proportional Equations</span>
              <p>
                Set up cross-multiplications or scaling factors based on <em>2 : 3</em>:
                <br>(i) <em>x : 42 :: 2 : 3</em>
                <br>(ii) <em>6 : y :: 2 : 3</em>
                <br>(iii) <em>2 : z :: 2 : 3</em>
              </p>
            </div>
            <div class="step-box step-3">
              <span class="step-badge">Step 3: Step-by-Step Algebraic Calculation</span>
              <p>
                • <strong>Part (i):</strong> <em>x / 42 = 2 / 3 ⇒ 3x = 84 ⇒ x = 84 / 3 = 28</em>. (Or: 42 is 2 × 21, so 2 × 14 = 28).
                <br>• <strong>Part (ii):</strong> <em>6 / y = 2 / 3 ⇒ 2y = 18 ⇒ y = 18 / 2 = 9</em>. (Or: multiplier = 6/14 = 3/7, so 21 × 3/7 = 9).
                <br>• <strong>Part (iii):</strong> <em>2 / z = 2 / 3 ⇒ 2z = 6 ⇒ z = 3</em>.
              </p>
            </div>
            <div class="step-box step-4">
              <span class="step-badge">Step 4: Verification</span>
              <p>
                • 28 : 42 = 28/14 : 42/14 = 2 : 3 ✓
                <br>• 6 : 9 = 6/3 : 9/3 = 2 : 3 ✓
                <br>• 2 : 3 = 2 : 3 ✓
              </p>
            </div>
            <div class="step-box step-5">
              <span class="step-badge">Step 5: Final Concluding Answer</span>
              <p>The missing numbers are: (i) <strong>28 : 42</strong> &nbsp;|&nbsp; (ii) <strong>6 : 9</strong> &nbsp;|&nbsp; (iii) <strong>2 : 3</strong>.</p>
            </div>
          </div>
        </div>
      </details>

      <!-- EXAMPLE 8 -->
      <details class="ans-box" id="ex8">
        <summary>Example 8: Mid-Day Meal Rainy Day Rice Calculation (NCERT Page 167)</summary>
        <div class="ans-content">
          <div class="step-container">
            <div class="step-box step-1">
              <span class="step-badge">Step 1: Given Information &amp; Goal</span>
              <p>
                • Normal attendance: 120 students require 15 kg of rice.
                <br>• Rainy day attendance: 80 students present.
                <br>• Goal: Find how many kilograms of rice the cook should make to avoid food wastage.
              </p>
            </div>
            <div class="step-box step-2">
              <span class="step-badge">Step 2: Trairāśika Proportion Setup</span>
              <p>
                Students and rice consumption are in direct proportion:
                <br><em>Students : Rice :: Students : Rice</em> ⇒ <strong>120 : 15 :: 80 : x</strong>
                <br>Pramāṇa = 120 students, Phala = 15 kg rice, Ichchhā = 80 students, Ichchhāphala = <em>x</em>.
              </p>
            </div>
            <div class="step-box step-3">
              <span class="step-badge">Step 3: Calculating by Āryabhaṭa's Rule &amp; Scaling Factor</span>
              <p>
                • <strong>Method 1 (Factor of Change):</strong>
                <br>Factor = <em>80 ÷ 120 = 2/3</em>.
                <br>Rice needed = <em>15 × (2/3) = 10 kg</em>.
                <br>• <strong>Method 2 (Āryabhaṭa's Trairāśika Formula):</strong>
                <br><em>x = (Phala × Ichchhā) ÷ Pramāṇa = (15 × 80) ÷ 120 = 1200 ÷ 120 = 10 kg</em>.
              </p>
            </div>
            <div class="step-box step-4">
              <span class="step-badge">Step 4: Unitary Verification</span>
              <p>
                Rice consumption per student = <em>15 kg ÷ 120 = 1/8 kg = 0.125 kg (125 grams)</em>.
                <br>For 80 students: <em>80 × 0.125 kg = 10 kg</em>. Checks out perfectly!
              </p>
            </div>
            <div class="step-box step-5">
              <span class="step-badge">Step 5: Final Concluding Answer</span>
              <p>The cook should make <strong>10 kg of rice</strong> on the rainy day.</p>
            </div>
          </div>
        </div>
      </details>

      <!-- EXAMPLE 9 -->
      <details class="ans-box" id="ex9">
        <summary>Example 9: Car Traveling Distance with Unit Conversion (NCERT Page 169)</summary>
        <div class="ans-content">
          <div class="step-container">
            <div class="step-box step-1">
              <span class="step-badge">Step 1: Given Information &amp; Goal</span>
              <p>
                • Car covers 90 km in 150 minutes at constant speed.
                <br>• Target time: 4 hours.
                <br>• Goal: Find the distance covered in 4 hours.
              </p>
            </div>
            <div class="step-box step-2">
              <span class="step-badge">Step 2: Unit Harmonization &amp; Proportion Formulation</span>
              <p>
                The two time quantities must have the same unit.
                <br>Target time = 4 hours = <em>4 × 60 = 240 minutes</em>.
                <br>Proportion: <em>Time (min) : Distance (km) :: Time (min) : Distance (km)</em>
                <br><strong>150 : 90 :: 240 : x</strong>
              </p>
            </div>
            <div class="step-box step-3">
              <span class="step-badge">Step 3: Cross-Multiplication Calculation</span>
              <p>
                <em>150 × x = 240 × 90</em>
                <br><em>x = (240 × 90) ÷ 150</em>
                <br>Divide 90 and 150 by 30: <em>90/30 = 3</em>, <em>150/30 = 5</em>:
                <br><em>x = (240 × 3) ÷ 5 = 720 ÷ 5 = 144 km</em>.
              </p>
            </div>
            <div class="step-box step-4">
              <span class="step-badge">Step 4: Speed Consistency Check</span>
              <p>
                Speed of car = <em>Distance / Time = 90 km / (150/60 h) = 90 / 2.5 = 36 km/h</em>.
                <br>Distance in 4 hours = <em>Speed × Time = 36 km/h × 4 h = 144 km</em>. Exactly consistent!
              </p>
            </div>
            <div class="step-box step-5">
              <span class="step-badge">Step 5: Final Concluding Answer</span>
              <p>The car will cover a distance of <strong>144 km</strong> in 4 hours.</p>
            </div>
          </div>
        </div>
      </details>

      <!-- EXAMPLE 10 -->
      <details class="ans-box" id="ex10">
        <summary>Example 10: Himachal vs Meghalaya Tea Pricing Comparison (NCERT Page 169-170)</summary>
        <div class="ans-content">
          <div class="step-container">
            <div class="step-box step-1">
              <span class="step-badge">Step 1: Given Information &amp; Goal</span>
              <p>
                • Himachal Pradesh: 200 g packet costs ₹200.
                <br>• Meghalaya: 1 kg packet costs ₹800.
                <br>• Goal: Determine if the weight-to-price ratios are proportional, and determine which tea is more expensive.
              </p>
            </div>
            <div class="step-box step-2">
              <span class="step-badge">Step 2: Unit Harmonization</span>
              <p>
                Convert 1 kg to grams: <em>1 kg = 1,000 g</em>.
                <br>• Himachal Ratio (Weight in g : Price in ₹) = <strong>200 : 200</strong>.
                <br>• Meghalaya Ratio (Weight in g : Price in ₹) = <strong>1000 : 800</strong>.
              </p>
            </div>
            <div class="step-box step-3">
              <span class="step-badge">Step 3: Simplest Ratios &amp; Proportionality Check</span>
              <p>
                • Himachal simplest form = 200 ÷ 200 : 200 ÷ 200 = <strong>1 : 1</strong> (1 gram costs ₹1).
                <br>• Meghalaya simplest form = 1000 ÷ 200 : 800 ÷ 200 = <strong>5 : 4</strong> (5 grams cost ₹4, or 1 g costs ₹0.80).
                <br>Since <em>1 : 1 ≠ 5 : 4</em>, the ratios are <strong>NOT proportional</strong>.
              </p>
            </div>
            <div class="step-box step-4">
              <span class="step-badge">Step 4: Standard 1 kg Cost Comparison</span>
              <p>
                • Cost of 1 kg tea in Meghalaya = <strong>₹800</strong>.
                <br>• In Himachal, 200 g = 1/5 kg costs ₹200.
                <br>&nbsp;&nbsp;Therefore, cost of 1 kg = 5 × ₹200 = <strong>₹1,000</strong>.
                <br>Difference = ₹1,000 - ₹800 = ₹200 per kg.
              </p>
            </div>
            <div class="step-box step-5">
              <span class="step-badge">Step 5: Final Concluding Answer</span>
              <p>The weight-to-price ratios are <strong>NOT proportional</strong>. The <strong>tea from Himachal Pradesh is more expensive</strong> (₹1,000 per kg compared to ₹800 per kg for Meghalaya tea).</p>
            </div>
          </div>
        </div>
      </details>

      <!-- EXAMPLE 11 -->
      <details class="ans-box" id="ex11">
        <summary>Example 11: Prashanti &amp; Bhuvan Food Cart Partnership Profit (NCERT Page 174)</summary>
        <div class="ans-content">
          <div class="step-container">
            <div class="step-box step-1">
              <span class="step-badge">Step 1: Given Information &amp; Goal</span>
              <p>
                • Prashanti's investment = ₹75,000.
                <br>• Bhuvan's investment = ₹25,000.
                <br>• Total first month profit = ₹4,000.
                <br>• Profit is shared in proportion to their investment ratio. Goal: Calculate each person's profit share.
              </p>
            </div>
            <div class="step-box step-2">
              <span class="step-badge">Step 2: Investment Ratio Simplification</span>
              <p>
                Investment Ratio (Prashanti : Bhuvan) = 75,000 : 25,000.
                <br>Divide both by 25,000:
                <br><em>(75,000 ÷ 25,000) : (25,000 ÷ 25,000) = <strong>3 : 1</strong></em>.
              </p>
            </div>
            <div class="step-box step-3">
              <span class="step-badge">Step 3: Partitioning the Whole Profit</span>
              <p>
                Total parts = <em>3 + 1 = 4 parts</em>.
                <br>Value of 1 part = <em>Total Profit ÷ 4 = ₹4,000 ÷ 4 = ₹1,000</em>.
                <br>• <strong>Prashanti's Share:</strong> 3 parts × ₹1,000 = <strong>₹3,000</strong>.
                <br>• <strong>Bhuvan's Share:</strong> 1 part × ₹1,000 = <strong>₹1,000</strong>.
              </p>
            </div>
            <div class="step-box step-4">
              <span class="step-badge">Step 4: Verification</span>
              <p>
                Sum of shares = ₹3,000 + ₹1,000 = ₹4,000 (matches total profit).
                <br>Ratio of shares = 3,000 : 1,000 = 3 : 1 (matches investment ratio).
              </p>
            </div>
            <div class="step-box step-5">
              <span class="step-badge">Step 5: Final Concluding Answer</span>
              <p><strong>Prashanti receives ₹3,000</strong> and <strong>Bhuvan receives ₹1,000</strong> of the profit.</p>
            </div>
          </div>
        </div>
      </details>

      <!-- EXAMPLE 12 -->
      <details class="ans-box" id="ex12">
        <summary>Example 12: Sand &amp; Cement Mixture Adjustment (NCERT Page 174-175)</summary>
        <div class="ans-content">
          <div class="step-container">
            <div class="step-box step-1">
              <span class="step-badge">Step 1: Given Information &amp; Goal</span>
              <p>
                • Total weight of mixture = 40 kg.
                <br>• Initial ratio (sand : cement) = 3 : 1.
                <br>• Desired new ratio (sand : cement) = 5 : 2 (by adding cement only; sand remains unchanged).
                <br>• Goal: Find how many kilograms of cement must be added.
              </p>
            </div>
            <div class="step-box step-2">
              <span class="step-badge">Step 2: Quantities in Original Mixture</span>
              <p>
                Total parts in original mixture = 3 + 1 = 4.
                <br>• Weight of sand = <em>(3/4) × 40 = 30 kg</em>.
                <br>• Weight of cement = <em>(1/4) × 40 = 10 kg</em>.
              </p>
            </div>
            <div class="step-box step-3">
              <span class="step-badge">Step 3: Calculating Cement Required for New Ratio</span>
              <p>
                In the new mixture, the sand remains 30 kg. The new ratio of sand to cement must be 5 : 2.
                <br>Setup proportion: <strong>5 : 2 :: 30 : C_new</strong>
                <br>By cross-multiplication:
                <br><em>5 × C_new = 2 × 30</em>
                <br><em>5 × C_new = 60 ⇒ C_new = 60 ÷ 5 = 12 kg</em>.
              </p>
            </div>
            <div class="step-box step-4">
              <span class="step-badge">Step 4: Additional Cement Needed &amp; Verification</span>
              <p>
                Additional cement = <em>C_new - C_initial = 12 kg - 10 kg = 2 kg</em>.
                <br>Verification: With 30 kg sand and 12 kg cement, ratio = 30 : 12 = (30÷6) : (12÷6) = 5 : 2 ✓.
              </p>
            </div>
            <div class="step-box step-5">
              <span class="step-badge">Step 5: Final Concluding Answer</span>
              <p><strong>2 kg of cement</strong> must be added to the original mixture.</p>
            </div>
          </div>
        </div>
      </details>

      <!-- PART B: IN-TEXT ACTIVITIES & MATH TALKS -->
      <h3 class="subheading"><i class="fa-solid fa-comments"></i> Part 4.2: In-Text Activities &amp; Math Talks</h3>

      <!-- IN-TEXT TABLE: MANJUNATH FILTER COFFEE -->
      <details class="ans-box" id="act-coffee">
        <summary>In-Text Table: Manjunath's Filter Coffee Decoction-to-Milk Table (NCERT Page 164-165)</summary>
        <div class="ans-content">
          <p>
            Manjunath mixes coffee decoction with milk. The benchmark recipes are:
            <br>• <strong>Regular Coffee:</strong> 20 mL decoction to 40 mL milk ⇒ Ratio = 20 : 40 = <strong>1 : 2 (0.50)</strong>.
            <br>• <strong>Strong Coffee:</strong> 30 mL decoction to 40 mL milk ⇒ Ratio = 30 : 40 = <strong>3 : 4 (0.75 > 0.50)</strong>.
            <br>• <strong>Light Coffee:</strong> 10 mL decoction to 40 mL milk ⇒ Ratio = 10 : 40 = <strong>1 : 4 (0.25 &lt; 0.50)</strong>.
          </p>
          <div class="table-container">
            <table class="data-table">
              <thead>
                <tr>
                  <th>Row</th>
                  <th>Decoction (mL)</th>
                  <th>Milk (mL)</th>
                  <th>Simplest Ratio</th>
                  <th>Decoction/Milk Value</th>
                  <th>Classification (Regular / Strong / Light)</th>
                  <th>Mathematical Reason</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td>1</td>
                  <td>300</td>
                  <td>600</td>
                  <td>1 : 2</td>
                  <td>0.50</td>
                  <td><strong style="color: #4f46e5;">Regular</strong></td>
                  <td>Exactly equals the standard regular ratio (1 : 2).</td>
                </tr>
                <tr>
                  <td>2</td>
                  <td>150</td>
                  <td>500</td>
                  <td>3 : 10</td>
                  <td>0.30</td>
                  <td><strong style="color: #d97706;">Light</strong></td>
                  <td>0.30 is less than 0.50 (more diluted).</td>
                </tr>
                <tr>
                  <td>3</td>
                  <td>200</td>
                  <td>400</td>
                  <td>1 : 2</td>
                  <td>0.50</td>
                  <td><strong style="color: #4f46e5;">Regular</strong></td>
                  <td>200 : 400 simplifies to 1 : 2 (perfect regular strength).</td>
                </tr>
                <tr>
                  <td>4</td>
                  <td>24</td>
                  <td>56</td>
                  <td>3 : 7</td>
                  <td>≈ 0.428</td>
                  <td><strong style="color: #d97706;">Light</strong></td>
                  <td>3/7 ≈ 0.428 is less than 1/2 = 0.50 (lighter than regular).</td>
                </tr>
                <tr>
                  <td>5</td>
                  <td>100</td>
                  <td>300</td>
                  <td>1 : 3</td>
                  <td>≈ 0.333</td>
                  <td><strong style="color: #d97706;">Light</strong></td>
                  <td>1/3 ≈ 0.333 is less than 0.50 (noticeably light coffee).</td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
      </details>

      <!-- ACTIVITY 1: FESTIVAL RECIPE SCALING -->
      <details class="ans-box" id="act1">
        <summary>Activity 1: Scaling a Family Dish for 15 Guests (NCERT Page 170)</summary>
        <div class="ans-content">
          <div class="step-container">
            <div class="step-box step-1">
              <span class="step-badge">Step 1: Baseline Recipe (Family of 5)</span>
              <p>
                Consider preparing vegetable pulao for a family of 5:
                <br>• Rice = 300 g
                <br>• Mixed Vegetables = 250 g
                <br>• Ghee/Oil = 50 mL
                <br>• Water = 600 mL
                <br>• Spices &amp; Salt = 20 g
              </p>
            </div>
            <div class="step-box step-2">
              <span class="step-badge">Step 2: Scaling Ratio &amp; Target Population</span>
              <p>
                Target: Family of 5 + 15 guests = <strong>20 people total</strong>.
                <br>Scale Factor <em>k = Target ÷ Baseline = 20 ÷ 5 = 4</em>.
              </p>
            </div>
            <div class="step-box step-3">
              <span class="step-badge">Step 3: Calculating Scaled Quantities</span>
              <p>
                Multiply every ingredient quantity by the scale factor 4:
                <br>• Rice: 300 g × 4 = <strong>1,200 g (1.2 kg)</strong>
                <br>• Mixed Vegetables: 250 g × 4 = <strong>1,000 g (1.0 kg)</strong>
                <br>• Ghee/Oil: 50 mL × 4 = <strong>200 mL</strong>
                <br>• Water: 600 mL × 4 = <strong>2,400 mL (2.4 L)</strong>
                <br>• Spices &amp; Salt: 20 g × 4 = <strong>80 g</strong>
              </p>
            </div>
            <div class="step-box step-4">
              <span class="step-badge">Step 4: Proportional Invariance Check</span>
              <p>
                Ratio of rice to water initially = 300 : 600 = 1 : 2.
                <br>Ratio of rice to water in scaled batch = 1200 : 2400 = 1 : 2 ✓. The taste and texture will be perfectly preserved.
              </p>
            </div>
            <div class="step-box step-5">
              <span class="step-badge">Step 5: Final Concluding Answer</span>
              <p>By applying a scaling factor of 4, all ingredients are increased proportionally to serve 20 people perfectly.</p>
            </div>
          </div>
        </div>
      </details>

      <!-- MATH TALK: MOTORCYCLE SPEED VS TIME -->
      <details class="ans-box" id="mt-speed">
        <summary>Math Talk: Motorcycle Journey - Lucknow to Kanpur (NCERT Page 171)</summary>
        <div class="ans-content">
          <div class="step-container">
            <div class="step-box step-1">
              <span class="step-badge">Step 1: Problem Scenario</span>
              <p>
                Puneeth's father rode from Lucknow to Kanpur in 2 hours at 50 km/h. If he drives at 75 km/h, can this problem be modelled as <em>50 : 2 :: 75 : x</em>?
              </p>
            </div>
            <div class="step-box step-2">
              <span class="step-badge">Step 2: Physics of Motion Analysis</span>
              <p>
                Total distance = <em>Speed × Time = 50 km/h × 2 h = 100 km</em>.
                <br>When speed increases, the time to cover the same distance MUST decrease.
              </p>
            </div>
            <div class="step-box step-3">
              <span class="step-badge">Step 3: Calculating True Time</span>
              <p>
                New time = <em>Distance ÷ New Speed = 100 km ÷ 75 km/h = 4/3 hours</em>.
                <br>4/3 hours = 1 hour + (1/3 × 60) minutes = <strong>1 hour 20 minutes (80 minutes)</strong>.
              </p>
            </div>
            <div class="step-box step-4">
              <span class="step-badge">Step 4: Why Direct Proportion Fails</span>
              <p>
                If we used <em>50 : 2 :: 75 : x</em>, cross-multiplication would give <em>x = (2 × 75) / 50 = 3 hours</em>.
                <br>This would mean driving faster takes MORE time, which is completely absurd in physics!
              </p>
            </div>
            <div class="step-box step-5">
              <span class="step-badge">Step 5: Final Concluding Answer</span>
              <p><strong>No, this problem cannot be modelled as 50 : 2 :: 75 : x.</strong> Speed and time are in <strong>inverse proportion</strong>. At 75 km/h, it takes him <strong>1 hour 20 minutes</strong>.</p>
            </div>
          </div>
        </div>
      </details>
"""
