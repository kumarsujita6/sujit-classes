import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

btt_style = '''
    /* Floating Back to Top Button */
    #back-to-top {
      position: fixed;
      bottom: 25px;
      right: 25px;
      background: var(--primary);
      color: white;
      border: none;
      width: 44px;
      height: 44px;
      border-radius: 50%;
      cursor: pointer;
      display: none;
      align-items: center;
      justify-content: center;
      font-size: 20px;
      box-shadow: var(--shadow-lg, 0 10px 15px -3px rgba(0,0,0,0.1));
      transition: all 0.2s;
      z-index: 999;
    }

    #back-to-top:hover {
      background: var(--primary-dark, #0f766e);
      transform: translateY(-2px);
    }
'''

btt_button = '''
  <button id="back-to-top" onclick="scrollToTop()" title="Back to top">↑</button>
'''

btt_script = '''
    function scrollToTop() {
      window.scrollTo({ top: 0, behavior: 'smooth' });
    }
'''

btt_scroll_snippet = '''
      const btt = document.getElementById('back-to-top');
      if (btt) {
        if (winScroll > 300) {
          btt.style.display = 'flex';
        } else {
          btt.style.display = 'none';
        }
      }
'''

for i in range(1, 9):
    # find file
    pattern = f"sst-ch{i}-"
    matched_file = None
    for f in os.listdir("english/class8"):
        if f.startswith(pattern) and f.endswith(".html"):
            matched_file = f
            break
    
    if not matched_file:
        print(f"File for Ch {i} not found!")
        continue

    path = os.path.join("english", "class8", matched_file)
    with open(path, "r", encoding="utf-8") as file:
        content = file.read()

    if 'id="back-to-top"' in content:
        print(f"Ch {i} already has back-to-top.")
        continue

    # Add style
    if "</style>" in content:
        content = content.replace("</style>", btt_style + "\n  </style>")

    # Add button before </body> or before <script>
    if "<script>" in content:
        content = content.replace("<script>", btt_button + "\n  <script>")
    elif "</body>" in content:
        content = content.replace("</body>", btt_button + "\n</body>")

    # Add script logic
    if "document.getElementById('reading-progress-bar').style.width = scrolled + '%';" in content:
        content = content.replace(
            "document.getElementById('reading-progress-bar').style.width = scrolled + '%\';",
            "document.getElementById('reading-progress-bar').style.width = scrolled + '%\';\n" + btt_scroll_snippet
        )

    if "</script>" in content:
        content = content.replace("</script>", btt_script + "\n  </script>")

    with open(path, "w", encoding="utf-8") as file:
        file.write(content)

    print(f"Updated Ch {i} ({matched_file}) with back-to-top button.")
