import os
import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

chapters = [
    (1, "sst-ch1-natural-resources-and-their-use.html", "Natural Resources and Their Use"),
    (2, "sst-ch2-reshaping-indias-political-map.html", "Reshaping India's Political Map"),
    (3, "sst-ch3-the-rise-of-the-marathas.html", "The Rise of the Marathas"),
    (4, "sst-ch4-the-colonial-era-in-india.html", "The Colonial Era in India"),
    (5, "sst-ch5-universal-franchise-and-indias-electoral-system.html", "Universal Franchise and India's Electoral System"),
    (6, "sst-ch6-the-parliamentary-system-legislature-and-executive.html", "The Parliamentary System: Legislature and Executive"),
    (7, "sst-ch7-factors-of-production.html", "Factors of Production"),
    (8, "sst-ch8-world-geography-some-glimpses.html", "World Geography: Some Glimpses"),
    (9, "sst-ch9-indias-long-road-to-independence.html", "India's Long Road to Independence"),
    (10, "sst-ch10-a-journey-through-indian-architecture.html", "A Journey Through Indian Architecture")
]

print("=" * 70)
print("CLASS 8 SOCIAL SCIENCE (ENGLISH) - COMPREHENSIVE VERIFICATION AUDIT")
print("=" * 70)

all_ok = True
target_dir = os.path.join("english", "class8")

for ch_num, filename, title in chapters:
    file_path = os.path.join(target_dir, filename)
    if not os.path.exists(file_path):
        print(f"[FAIL] Ch {ch_num}: File missing at {file_path}")
        all_ok = False
        continue

    size = os.path.getsize(file_path)
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    checks = {
        "File Size > 40KB": size > 40000,
        "Reading Progress Bar": 'id="reading-progress-bar"' in content,
        "Quiz Cards": 'class="quiz-card"' in content,
        "Collapsible Solutions": '<details class="ans-box"' in content,
        "Callout Boxes": 'class="callout' in content,
        "Inline SVGs": '<svg' in content,
        "Audio Reader (TTS)": 'speechSynthesis' in content or 'toggleAudio' in content,
        "Back to Top": 'id="back-to-top"' in content
    }

    failed_checks = [k for k, v in checks.items() if not v]
    if failed_checks:
        print(f"[FAIL] Ch {ch_num} ({filename}): Failed checks: {failed_checks}")
        all_ok = False
    else:
        svg_count = content.count("<svg")
        quiz_count = content.count('class="quiz-card"')
        ans_count = content.count('<details class="ans-box"')
        print(f"[PASS] Ch {ch_num:2d}: {title:<45} | {size:6d} B | SVGs: {svg_count} | Quizzes: {quiz_count} | Solutions: {ans_count}")

print("\n" + "=" * 70)
print("VERIFYING INDEX.HTML REGISTRATION")
print("=" * 70)

with open("index.html", "r", encoding="utf-8") as f:
    index_content = f.read()

for ch_num, filename, title in chapters:
    id_str = f"id: 'c8_sst_{ch_num}'"
    if id_str not in index_content:
        print(f"[FAIL] index.html missing {id_str}")
        all_ok = False
    else:
        # Check isLive: true
        pattern = re.compile(rf"id:\s*['\"]c8_sst_{ch_num}['\"].*?isLive:\s*(true|false)", re.DOTALL)
        match = pattern.search(index_content)
        if match and match.group(1) == "true":
            # Check link
            expected_link = f"english/class8/{filename}"
            if expected_link in index_content:
                print(f"[PASS] c8_sst_{ch_num:2d} properly registered: isLive=true, link={expected_link}")
            else:
                print(f"[FAIL] c8_sst_{ch_num} link mismatch, expected {expected_link}")
                all_ok = False
        else:
            print(f"[FAIL] c8_sst_{ch_num} is not marked isLive: true")
            all_ok = False

if all_ok:
    print("\n>>> ALL VERIFICATION CHECKS PASSED PERFECTLY! <<<")
else:
    print("\n>>> SOME VERIFICATION CHECKS FAILED! <<<")
