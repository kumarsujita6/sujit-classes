# -*- coding: utf-8 -*-
"""
Section 2: Complete Line-by-Line Conceptual Explanations & Bilingual Glossary
"""
from gen_svgs import get_svg_terms, get_svg_tokens, get_svg_distributive, get_svg_brackets, get_svg_tree

def get_section_2():
    svg_terms = get_svg_terms()
    svg_tokens = get_svg_tokens()
    svg_brackets = get_svg_brackets()
    svg_distributive = get_svg_distributive()
    svg_tree = get_svg_tree()

    return f'''
    <!-- SECTION 2: CONCEPTUAL EXPLANATIONS & BILINGUAL GLOSSARY -->
    <section id="section-2" class="study-section">
      <div class="section-header">
        <div class="section-icon icon-teal">
          <i class="fa-solid fa-book-open-reader"></i>
        </div>
        <div>
          <h2>Section 2: Complete Conceptual Explanations &amp; Bilingual Glossary</h2>
          <p>Exhaustive line-by-line breakdown with intuitive physical models, mental math reasoning, and 30 bilingual terms in English and Odia script.</p>
        </div>
      </div>

      <!-- TOPIC 2.1 -->
      <h3><i class="fa-solid fa-arrow-right-arrow-left"></i> 2.1 Simple Expressions, Values, and Equality</h3>
      <p>
        In mathematics, numbers alone are like single words, but when we connect numbers using operation signs such as 
        addition (+), subtraction (−), multiplication (×), and division (÷), we form <strong>mathematical phrases</strong>. 
        These phrases are known as <strong>arithmetic expressions</strong> (ପାଟୀଗାଣିତିକ ରାଶି).
      </p>

      <div class="callout callout-def">
        <div class="callout-title"><i class="fa-solid fa-calculator"></i> What is an Arithmetic Expression?</div>
        <p>
          An <strong>arithmetic expression</strong> is a meaningful combination of numbers and one or more arithmetic operations (+, −, ×, ÷) that does not contain an equals sign or inequality sign. 
          Examples include:
        </p>
        <ul>
          <li><span class="math-inline">13 + 2</span> (read as "13 plus 2" or "the sum of 13 and 2")</li>
          <li><span class="math-inline">20 − 4</span> (read as "20 minus 4" or "the difference between 20 and 4")</li>
          <li><span class="math-inline">12 × 5</span> (read as "12 multiplied by 5" or "the product of 12 and 5")</li>
          <li><span class="math-inline">18 ÷ 3</span> (read as "18 divided by 3" or "the quotient of 18 and 3")</li>
        </ul>
      </div>

      <p>
        <strong>Every arithmetic expression has a unique Value:</strong> The <em>value</em> of an arithmetic expression is the single number 
        that results when all indicated calculations are correctly carried out. 
        For instance, the value of the expression <span class="math-inline">13 + 2</span> is the number <span class="math-inline">15</span>. 
        We use the equality symbol (<span class="math-inline">=</span>) to express this relationship:
      </p>
      <div class="math-display">13 + 2 = 15</div>

      <div class="callout callout-act">
        <div class="callout-title"><i class="fa-solid fa-lightbulb"></i> One Value, Countless Expressions!</div>
        <p>
          Just like a person can be called by different nicknames or wear different clothes while remaining the exact same person, 
          a single numerical value can be expressed in infinitely many ways! 
          Consider the number <strong>12</strong>:
        </p>
        <ul>
          <li>Using addition: <span class="math-inline">10 + 2 = 12</span> or <span class="math-inline">7 + 5 = 12</span></li>
          <li>Using subtraction: <span class="math-inline">15 − 3 = 12</span> or <span class="math-inline">20 − 8 = 12</span></li>
          <li>Using multiplication: <span class="math-inline">3 × 4 = 12</span> or <span class="math-inline">2 × 6 = 12</span> or <span class="math-inline">1 × 12 = 12</span></li>
          <li>Using division: <span class="math-inline">24 ÷ 2 = 12</span> or <span class="math-inline">36 ÷ 3 = 12</span> or <span class="math-inline">48 ÷ 4 = 12</span></li>
        </ul>
        <p>
          Because they all yield 12, we can link them together as equal expressions: 
          <span class="math-inline">10 + 2 = 15 − 3 = 3 × 4 = 24 ÷ 2</span>.
        </p>
      </div>

      <h4>Comparing Expressions: The Power of Mathematical Reasoning</h4>
      <p>
        When asked to compare two expressions such as <span class="math-inline">1023 + 125</span> and <span class="math-inline">1022 + 128</span>, 
        a beginner immediately reaches for pencil and paper to perform long addition. 
        However, a skilled mathematician uses <strong>structural comparison</strong> without computing the values at all!
      </p>

      <p>
        Let us visualize this using the textbook's delightful marble scenario:
      </p>
      <ul>
        <li><strong>Raja's Marbles:</strong> Raja started with 1,023 marbles and received 125 more today. Total = <span class="math-inline">1023 + 125</span>.</li>
        <li><strong>Joy's Marbles:</strong> Joy started with 1,022 marbles and received 128 more today. Total = <span class="math-inline">1022 + 128</span>.</li>
      </ul>
      <p>
        Let us compare their starting amounts and daily gifts:
      </p>
      <ol>
        <li>At the beginning, Raja had <strong>1 more marble</strong> than Joy (<span class="math-inline">1023 − 1022 = 1</span>).</li>
        <li>However, during the day, Joy received <strong>3 more marbles</strong> than Raja (<span class="math-inline">128 − 125 = 3</span>).</li>
        <li>Since Joy gained 3 extra marbles while Raja had an advantage of only 1 marble, Joy ends up with <span class="math-inline">3 − 1 = 2</span> marbles more than Raja!</li>
      </ol>
      <div class="math-display">1023 + 125 &lt; 1022 + 128 &nbsp; (Joy has 2 marbles more)</div>

      <p>
        Similarly, consider the subtraction comparison: <span class="math-inline">113 − 25</span> versus <span class="math-inline">112 − 24</span>.
      </p>
      <ul>
        <li>Raja had 113 marbles and lost 25. Joy had 112 marbles and lost 24.</li>
        <li>Raja started with 1 marble more than Joy (<span class="math-inline">113 − 112 = 1</span>).</li>
        <li>But Raja also lost exactly 1 marble more than Joy (<span class="math-inline">25 − 24 = 1</span>).</li>
        <li>The initial advantage of +1 was perfectly balanced by the extra loss of −1. Therefore, both boys are left with the exact same number of marbles!</li>
      </ul>
      <div class="math-display">113 − 25 = 112 − 24 = 88</div>

      <!-- TOPIC 2.2 -->
      <h3><i class="fa-solid fa-triangle-exclamation"></i> 2.2 Reading and Evaluating Complex Expressions: The Ambiguity Dilemma</h3>
      <p>
        When an expression contains more than one operation, confusion easily arises if the expression is written without context. 
        In language, punctuation marks like commas determine meaning:
      </p>
      <ul>
        <li><em>"Shalini sat next to a friend with toys."</em> &rarr; The friend has toys, and Shalini sat next to her.</li>
        <li><em>"Shalini sat next to a friend, with toys."</em> &rarr; Shalini has the toys, and she sat with them next to her friend.</li>
      </ul>
      <p>
        Without punctuation, a reader cannot tell who owns the toys! 
        Mathematics faces the exact same dilemma. Consider the story of Mallesh and Purna from the textbook:
      </p>

      <div class="callout callout-warn">
        <div class="callout-title"><i class="fa-solid fa-user-xmark"></i> The Classic Ambiguity: Mallesh vs Purna</div>
        <p>
          Mallesh brought 30 marbles to the playground. Arun brought 5 bags of marbles with 4 marbles in each bag. 
          To find the total number of marbles brought to the playground, Mallesh wrote:
        </p>
        <div class="math-display">30 + 5 × 4</div>
        <p>
          Two students evaluated this raw expression:
        </p>
        <ul>
          <li><strong>Purna's Evaluation:</strong> Purna added first: <span class="math-inline">30 + 5 = 35</span>, then multiplied: <span class="math-inline">35 × 4 = 140</span> marbles.</li>
          <li><strong>Mallesh's Evaluation:</strong> Mallesh multiplied first: <span class="math-inline">5 × 4 = 20</span>, then added: <span class="math-inline">30 + 20 = 50</span> marbles.</li>
        </ul>
        <p>
          Who was right? Mallesh was completely right because Arun's 5 bags had 4 marbles each, giving 20 marbles, plus Mallesh's 30 marbles = 50 marbles. 
          Purna got it wrong because he blindly performed addition from left to right! 
          To eliminate all ambiguity, mathematics uses two powerful tools: <strong>Brackets</strong> and the <strong>Notion of Terms</strong>.
        </p>
      </div>

      <!-- TOPIC 2.3 -->
      <h3><i class="fa-solid fa-boxes-stacked"></i> 2.3 Terms in Expressions: The Atomic Building Blocks (ପଦ)</h3>
      <p>
        When an expression does not have brackets specifying the order, how do we know what to calculate first? 
        The NCERT Ganita Prakash curriculum introduces the foundational concept of <strong>Terms</strong>.
      </p>

      <div class="callout callout-def">
        <div class="callout-title"><i class="fa-solid fa-cube"></i> Formal Definition of a Term (ପଦ)</div>
        <p>
          <strong>Terms</strong> are the parts of an arithmetic expression separated strictly by a <strong>'+' sign</strong>. 
          When an expression has no brackets, we evaluate each term independently first, and then add the resulting values of all terms together.
        </p>
      </div>

      <p>
        For example, in the simple expression <span class="math-inline">12 + 7</span>, there are two terms: <strong>12</strong> and <strong>7</strong>. 
        Each term is an independent quantity joined by addition.
      </p>

      <h4>How Do We Handle Subtraction? The Additive Inverse Revolution</h4>
      <p>
        What if an expression contains a minus sign, such as <span class="math-inline">83 − 14</span>? Are there two terms, or does subtraction break our rule?
      </p>
      <p>
        Here lies one of the most beautiful insights of mathematics: <strong>Subtracting a number is identical to adding its opposite (additive inverse)!</strong>
      </p>
      <ul>
        <li>The additive inverse of <span class="math-inline">+14</span> is <span class="math-inline">−14</span>.</li>
        <li>The additive inverse of <span class="math-inline">−14</span> is <span class="math-inline">+14</span>.</li>
        <li>Therefore, subtracting 14 from 83 is rewritten as: <span class="math-inline">83 − 14 = 83 + (−14)</span>.</li>
      </ul>
      <p>
        Now, the expression is strictly a sum of two terms: the first term is <strong>83</strong>, and the second term is <strong>−14</strong>!
      </p>

      {svg_terms}

      <h4>Single Terms Containing Multiplications and Divisions</h4>
      <p>
        Notice that phrases like <span class="math-inline">6 × 5</span>, <span class="math-inline">4 × 6</span>, or <span class="math-inline">16 ÷ 2</span> do not contain any '+' sign. 
        Therefore, each of them forms a <strong>single indivisible term</strong>!
      </p>
      <ul>
        <li>In <span class="math-inline">5 + 6 × 3</span>, the terms are <strong>5</strong> and <strong>6 × 3</strong>. (Term 2 evaluates to 18, so total = 5 + 18 = 23).</li>
        <li>In <span class="math-inline">23 − 2 × 4 + 16</span>, we rewrite as <span class="math-inline">23 + (−(2 × 4)) + 16</span>. The terms are <strong>23</strong>, <strong>−8</strong>, and <strong>16</strong>.</li>
        <li>In <span class="math-inline">48 − 10 × 2 + 16 ÷ 2</span>, the terms are <strong>48</strong>, <strong>−20</strong>, and <strong>8</strong>.</li>
      </ul>

      <!-- TOPIC 2.4 -->
      <h3><i class="fa-solid fa-arrows-rotate"></i> 2.4 Fundamental Laws of Addition of Terms</h3>
      <p>
        Once an expression is understood as a sum of terms, two monumental mathematical properties guarantee complete computational freedom:
      </p>

      <h4>1. The Commutative Property of Addition (ଯୋଗର କ୍ରମବିନିମୟ ନିୟମ)</h4>
      <p>
        <strong>Swapping terms does not change the sum.</strong> For any two terms <span class="math-inline">Term 1</span> and <span class="math-inline">Term 2</span>:
      </p>
      <div class="math-display">Term 1 + Term 2 = Term 2 + Term 1</div>
      <p>
        Consider Madhu flying a drone from a terrace (Example 6 in NCERT):
      </p>
      <ul>
        <li>The drone first climbs 6 m up, then descends 4 m down: <span class="math-inline">6 + (−4) = 2</span> m above the terrace.</li>
        <li>What if we swap the sequence? The drone first descends 4 m, then ascends 6 m: <span class="math-inline">(−4) + 6 = 2</span> m above the terrace!</li>
      </ul>
      <p>
        The final position is identical regardless of which movement occurred first.
      </p>

      <h4>2. The Associative Property of Addition (ଯୋଗର ସହଯୋଗୀ ନିୟମ)</h4>
      <p>
        <strong>Grouping terms does not change the sum.</strong> For any three terms:
      </p>
      <div class="math-display">[ Term 1 + Term 2 ] + Term 3 = Term 1 + [ Term 2 + Term 3 ]</div>
      <p>
        Consider adding three terms: <span class="math-inline">(−7) + 10 + (−11)</span>:
      </p>
      <ul>
        <li><strong>Grouping A:</strong> <span class="math-inline">[ (−7) + 10 ] + (−11) = 3 + (−11) = −8</span></li>
        <li><strong>Grouping B:</strong> <span class="math-inline">(−7) + [ 10 + (−11) ] = (−7) + (−1) = −8</span></li>
      </ul>

      {svg_tokens}

      <div class="callout callout-act">
        <div class="callout-title"><i class="fa-solid fa-shirt"></i> Everyday Life Analogy: Hat &amp; Shoes vs Socks &amp; Shoes</div>
        <p>
          Mathematics connects directly to our physical world:
        </p>
        <ul>
          <li><strong>Commutative Operation (Order doesn't matter):</strong> Putting on your hat and putting on your shoes. You can wear the hat first, then shoes; or shoes first, then hat. You look and feel identical!</li>
          <li><strong>Non-Commutative Operation (Order strictly matters!):</strong> Putting on your socks and putting on your shoes. If you wear socks first, then shoes, you are ready for school. But if you put on shoes first and then pull socks over them, you look ridiculous and feel awful! In math, subtraction and division are non-commutative, whereas addition of terms is always commutative.</li>
        </ul>
      </div>

      <!-- TOPIC 2.5 -->
      <h3><i class="fa-solid fa-folder-open"></i> 2.5 Removing Brackets - Part I: The Sign Inversion Gate</h3>
      <p>
        Brackets <span class="math-inline">( )</span> are used to group numbers that belong together. 
        When simplifying expressions, we often wish to remove brackets. What happens to the terms inside?
      </p>

      <h4>Rule 1: Brackets Preceded by a Plus Sign (+)</h4>
      <p>
        When brackets are preceded by a positive sign, the brackets simply dissolve without changing any sign inside:
      </p>
      <div class="math-display">a + (b + c) = a + b + c &nbsp;&nbsp;&nbsp;&nbsp; a + (b − c) = a + b − c</div>
      <p>
        <strong>Example (Hira's Coins):</strong> Hira has 28 coins in one pouch and 35 in another. She gifts 10 coins from the second pouch: 
        <span class="math-inline">28 + (35 − 10) = 28 + 35 − 10 = 63 − 10 = 53</span> coins.
      </p>

      <h4>Rule 2: Brackets Preceded by a Minus Sign (−)</h4>
      <p>
        When brackets preceded by a negative sign are removed, <strong>EVERY term inside the bracket inverts its sign</strong>:
      </p>
      <ul>
        <li>A positive term inside turns negative: <span class="math-inline">a − (b + c) = a − b − c</span></li>
        <li>A negative term inside turns positive: <span class="math-inline">a − (b − c) = a − b + c</span></li>
      </ul>

      {svg_brackets}

      <div class="callout callout-def">
        <div class="callout-title"><i class="fa-solid fa-receipt"></i> Why does a − (b − c) become a − b + c? (The Shopkeeper Logic)</div>
        <p>
          Let us understand this with two crystal-clear everyday examples:
        </p>
        <ol>
          <li>
            <strong>Irfan's Grocery Bill:</strong> Irfan buys biscuits for ₹15 and dal for ₹56, paying with a ₹100 note. 
            Change = <span class="math-inline">100 − (15 + 56)</span>. 
            The shopkeeper can subtract both items one after the other: first take away ₹15 (<span class="math-inline">100 − 15 = 85</span>), then take away ₹56 (<span class="math-inline">85 − 56 = 29</span>). 
            Hence, <span class="math-inline">100 − (15 + 56) = 100 − 15 − 56 = 29</span>. Both signs become negative!
          </li>
          <li>
            <strong>Correcting an Over-Deduction:</strong> Consider <span class="math-inline">500 − (250 − 100)</span>. 
            The amount to subtract is <span class="math-inline">250 − 100 = 150</span>, so <span class="math-inline">500 − 150 = 350</span>. 
            If you blindly subtract 250 from 500 (<span class="math-inline">500 − 250 = 250</span>), you subtracted <strong>100 too much</strong>! 
            To correct this over-subtraction, you must <em>add back</em> the 100: <span class="math-inline">500 − 250 + 100 = 350</span>! 
            That is why the minus sign in front of (−100) inverted into +100!
          </li>
        </ol>
      </div>

      <!-- TOPIC 2.6 -->
      <h3><i class="fa-solid fa-shapes"></i> 2.6 Removing Brackets - Part II: The Distributive Property (ବଣ୍ଟନ ନିୟମ)</h3>
      <p>
        When a multiplier sits outside parentheses containing a sum or difference, how do we evaluate it? 
        This is governed by the famous <strong>Distributive Property of Multiplication over Addition and Subtraction</strong>.
      </p>

      <div class="callout callout-def">
        <div class="callout-title"><i class="fa-solid fa-network-wired"></i> The Distributive Law (ବଣ୍ଟନ ନିୟମ)</div>
        <p>
          The multiple of a sum (or difference) is equal to the sum (or difference) of the individual multiples:
        </p>
        <div class="math-display">a × (b + c) = a × b + a × c</div>
        <div class="math-display">a × (b − c) = a × b − a × c</div>
      </div>

      <p>
        Look at Example 15 from the textbook: Lhamo and Norbu go to a hotel. Each orders 1 vegetable cutlet (₹43) and 1 rasgulla (₹24). 
        How much must they pay altogether?
      </p>
      <ul>
        <li><strong>Method 1 (Total per person first):</strong> Each person owes <span class="math-inline">(43 + 24) = 67</span>. For 2 friends, total = <span class="math-inline">2 × (43 + 24) = 2 × 67 = 134</span>.</li>
        <li><strong>Method 2 (By food item):</strong> They ordered 2 cutlets (<span class="math-inline">2 × 43 = 86</span>) and 2 rasgullas (<span class="math-inline">2 × 24 = 48</span>). Total = <span class="math-inline">86 + 48 = 134</span>.</li>
      </ul>
      <p>
        Both methods yield ₹134! Hence, <span class="math-inline">2 × (43 + 24) = 2 × 43 + 2 × 24</span>.
      </p>

      {svg_distributive}

      <h4>Mental Math Superpower: Lightning Multiplication</h4>
      <p>
        The distributive property is the secret weapon used by human calculators:
      </p>
      <ul>
        <li>
          <strong>Calculate 97 × 25:</strong> We notice that 97 is <span class="math-inline">100 − 3</span>. 
          Therefore:
          <div class="math-display">97 × 25 = (100 − 3) × 25 = 100 × 25 − 3 × 25 = 2500 − 75 = 2425</div>
        </li>
        <li>
          <strong>Calculate 104 × 15:</strong> We express 104 as <span class="math-inline">100 + 4</span>.
          <div class="math-display">104 × 15 = (100 + 4) × 15 = 100 × 15 + 4 × 15 = 1500 + 60 = 1560</div>
        </li>
        <li>
          <strong>Calculate 49 × 50:</strong> We express 49 as <span class="math-inline">50 − 1</span>.
          <div class="math-display">49 × 50 = (50 − 1) × 50 = 50 × 50 − 1 × 50 = 2500 − 50 = 2450</div>
        </li>
      </ul>

      <!-- TOPIC 2.7 -->
      <h3><i class="fa-solid fa-tree"></i> 2.7 Expression Trees &amp; Hierarchical Order of Operations</h3>
      <p>
        Computer scientists and mathematicians evaluate complex expressions by constructing an <strong>Expression Tree</strong> (ରାଶି ଶାଖା ଚିତ୍ର). 
        In an expression tree, operations at the bottom leaves must be completed before their parent nodes can execute. 
        Addition of terms sits at the very root of the tree!
      </p>

      {svg_tree}

      <!-- BILINGUAL VOCABULARY TABLE -->
      <h3><i class="fa-solid fa-language"></i> Exhaustive Bilingual Mathematical Glossary (30 Terms)</h3>
      <p>
        Mastering technical vocabulary in both English and standard textbook Odia (ଓଡ଼ିଆ) empowers students 
        to transition effortlessly between CBSE and BSE Odisha state curricula.
      </p>

      <div class="table-container">
        <table>
          <thead>
            <tr>
              <th>#</th>
              <th>Term / Concept</th>
              <th>Part of Speech</th>
              <th>English Meaning</th>
              <th>ଓଡ଼ିଆ ଅର୍ଥ (Odia Meaning in Odia Script)</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>1</td>
              <td><strong>Arithmetic Expression</strong></td>
              <td>Noun phrase</td>
              <td>A mathematical phrase combining numbers and operations (+, −, ×, ÷) without an equality sign.</td>
              <td class="odia-text">ପାଟୀଗାଣିତିକ ରାଶି / ଗାଣିତିକ ରାଶି</td>
            </tr>
            <tr>
              <td>2</td>
              <td><strong>Value of an Expression</strong></td>
              <td>Noun phrase</td>
              <td>The single numerical result obtained after evaluating an expression.</td>
              <td class="odia-text">ରାଶିର ମାନ</td>
            </tr>
            <tr>
              <td>3</td>
              <td><strong>Term</strong></td>
              <td>Noun</td>
              <td>The distinct components of an expression separated strictly by addition (+) signs.</td>
              <td class="odia-text">ପଦ</td>
            </tr>
            <tr>
              <td>4</td>
              <td><strong>Order of Operations</strong></td>
              <td>Noun phrase</td>
              <td>The established mathematical sequence determining which operations are executed first.</td>
              <td class="odia-text">ଗାଣିତିକ ପ୍ରକ୍ରିୟାର କ୍ରମ</td>
            </tr>
            <tr>
              <td>5</td>
              <td><strong>Bracket / Parentheses</strong></td>
              <td>Noun</td>
              <td>Grouping symbols ( ) used to enclose terms that must be calculated together first.</td>
              <td class="odia-text">ବନ୍ଧନୀ</td>
            </tr>
            <tr>
              <td>6</td>
              <td><strong>Additive Inverse</strong></td>
              <td>Noun phrase</td>
              <td>A number having the opposite sign such that their sum equals zero (e.g., +14 and −14).</td>
              <td class="odia-text">ଯୋଗାତ୍ମକ ବିପରୀତ</td>
            </tr>
            <tr>
              <td>7</td>
              <td><strong>Commutative Property</strong></td>
              <td>Noun phrase</td>
              <td>The rule stating that swapping the order of terms does not change the sum (a + b = b + a).</td>
              <td class="odia-text">ଯୋଗର କ୍ରମବିନିମୟ ନିୟମ</td>
            </tr>
            <tr>
              <td>8</td>
              <td><strong>Associative Property</strong></td>
              <td>Noun phrase</td>
              <td>The rule stating that grouping terms in any order gives the same sum ((a + b) + c = a + (b + c)).</td>
              <td class="odia-text">ଯୋଗର ସହଯୋଗୀ ନିୟମ</td>
            </tr>
            <tr>
              <td>9</td>
              <td><strong>Distributive Property</strong></td>
              <td>Noun phrase</td>
              <td>Multiplying a number by a sum equals the sum of the individual products (a(b+c) = ab + ac).</td>
              <td class="odia-text">ବଣ୍ଟନ ନିୟମ</td>
            </tr>
            <tr>
              <td>10</td>
              <td><strong>Equality Sign (=)</strong></td>
              <td>Noun phrase</td>
              <td>The mathematical symbol denoting that two expressions have identical numerical value.</td>
              <td class="odia-text">ସମାନ ଚିହ୍ନ</td>
            </tr>
            <tr>
              <td>11</td>
              <td><strong>Inequality</strong></td>
              <td>Noun</td>
              <td>A relationship comparing two unequal values using greater than (&gt;) or less than (&lt;).</td>
              <td class="odia-text">ଅସମତା</td>
            </tr>
            <tr>
              <td>12</td>
              <td><strong>Greater Than (&gt;)</strong></td>
              <td>Prepositional phrase</td>
              <td>Symbol indicating that the left-hand quantity has a larger value than the right-hand quantity.</td>
              <td class="odia-text">ବୃହତ୍ତର / ଠାରୁ ବଡ଼</td>
            </tr>
            <tr>
              <td>13</td>
              <td><strong>Less Than (&lt;)</strong></td>
              <td>Prepositional phrase</td>
              <td>Symbol indicating that the left-hand quantity has a smaller value than the right-hand quantity.</td>
              <td class="odia-text">କ୍ଷୁଦ୍ରତର / ଠାରୁ ସାନ</td>
            </tr>
            <tr>
              <td>14</td>
              <td><strong>Ascending Order</strong></td>
              <td>Noun phrase</td>
              <td>Arranging numbers or expressions from smallest to largest value.</td>
              <td class="odia-text">ଊର୍ଦ୍ଧ୍ୱକ୍ରମ (ଛୋଟରୁ ବଡ଼)</td>
            </tr>
            <tr>
              <td>15</td>
              <td><strong>Descending Order</strong></td>
              <td>Noun phrase</td>
              <td>Arranging numbers or expressions from largest to smallest value.</td>
              <td class="odia-text">ଅଧଃକ୍ରମ (ବଡ଼ରୁ ଛୋଟ)</td>
            </tr>
            <tr>
              <td>16</td>
              <td><strong>Sum</strong></td>
              <td>Noun</td>
              <td>The total result obtained by adding two or more numbers or terms together.</td>
              <td class="odia-text">ଯୋଗଫଳ</td>
            </tr>
            <tr>
              <td>17</td>
              <td><strong>Difference</strong></td>
              <td>Noun</td>
              <td>The result obtained by subtracting one quantity from another.</td>
              <td class="odia-text">ବିୟୋଗଫଳ</td>
            </tr>
            <tr>
              <td>18</td>
              <td><strong>Product</strong></td>
              <td>Noun</td>
              <td>The result obtained by multiplying two or more quantities together.</td>
              <td class="odia-text">ଗୁଣନଫଳ</td>
            </tr>
            <tr>
              <td>19</td>
              <td><strong>Quotient</strong></td>
              <td>Noun</td>
              <td>The result obtained by dividing one number (dividend) by another (divisor).</td>
              <td class="odia-text">ଭାଗଫଳ</td>
            </tr>
            <tr>
              <td>20</td>
              <td><strong>Evaluation</strong></td>
              <td>Noun</td>
              <td>The process of calculating and simplifying an expression to find its numerical value.</td>
              <td class="odia-text">ମାନ ନିର୍ଣ୍ଣୟ</td>
            </tr>
            <tr>
              <td>21</td>
              <td><strong>Preceding Sign</strong></td>
              <td>Noun phrase</td>
              <td>The operational symbol (+ or −) placed immediately before a bracket or term.</td>
              <td class="odia-text">ପୂର୍ବବର୍ତ୍ତୀ ଚିହ୍ନ</td>
            </tr>
            <tr>
              <td>22</td>
              <td><strong>Sign Inversion</strong></td>
              <td>Noun phrase</td>
              <td>The reversing of signs (+ to −, and − to +) when removing brackets preceded by a minus.</td>
              <td class="odia-text">ଚିହ୍ନ ପରିବର୍ତ୍ତନ</td>
            </tr>
            <tr>
              <td>23</td>
              <td><strong>Grouping</strong></td>
              <td>Noun</td>
              <td>Collecting terms together inside brackets or mental clusters to simplify computation.</td>
              <td class="odia-text">ଦଳଭୁକ୍ତ କରିବା</td>
            </tr>
            <tr>
              <td>24</td>
              <td><strong>Swapping</strong></td>
              <td>Noun</td>
              <td>Exchanging the physical positions of two terms without modifying their signs.</td>
              <td class="odia-text">ସ୍ଥାନ ଅଦଳବଦଳ</td>
            </tr>
            <tr>
              <td>25</td>
              <td><strong>Multiple</strong></td>
              <td>Noun</td>
              <td>A number that can be divided by another number without leaving a remainder.</td>
              <td class="odia-text">ଗୁଣିତକ</td>
            </tr>
            <tr>
              <td>26</td>
              <td><strong>Mathematical Reasoning</strong></td>
              <td>Noun phrase</td>
              <td>Deducing truth and comparing values logically without performing lengthy calculations.</td>
              <td class="odia-text">ଯୌକ୍ତିକ ଚିନ୍ତନ / ଯୁକ୍ତିସଙ୍ଗତ ନିଷ୍ପତ୍ତି</td>
            </tr>
            <tr>
              <td>27</td>
              <td><strong>Token Model</strong></td>
              <td>Noun phrase</td>
              <td>A physical visualization using positive and negative counters to demonstrate integer operations.</td>
              <td class="odia-text">ଟୋକନ୍ ମଡେଲ୍ (ଚିହ୍ନ ଗୋଲକ)</td>
            </tr>
            <tr>
              <td>28</td>
              <td><strong>Expression Tree</strong></td>
              <td>Noun phrase</td>
              <td>A branching hierarchical graph showing how sub-expressions combine into a root value.</td>
              <td class="odia-text">ରାଶି ଶାଖା ଚିତ୍ର</td>
            </tr>
            <tr>
              <td>29</td>
              <td><strong>Zero Pair</strong></td>
              <td>Noun phrase</td>
              <td>A pair consisting of one positive unit (+1) and one negative unit (−1) that cancel to 0.</td>
              <td class="odia-text">ଶୂନ ଯୁଗଳ</td>
            </tr>
            <tr>
              <td>30</td>
              <td><strong>Area Model</strong></td>
              <td>Noun phrase</td>
              <td>A visual geometric proof representing multiplication as the area of a divided rectangle.</td>
              <td class="odia-text">କ୍ଷେତ୍ରଫଳ ମଡେଲ୍</td>
            </tr>
          </tbody>
        </table>
      </div>
    </section>
'''
