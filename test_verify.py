import sys

def verify_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        text = f.read()
    print("File:", filepath)
    print("Size:", len(text))
    print("Has raw dollar:", chr(36) in text)
    print("Has raw cite:", '<cite' in text)
    print("Has details.ans-box:", 'details class="ans-box"' in text)
    print("SVG count:", text.count('<svg'))
    assert not chr(36) in text, "Contains raw dollar sign!"
    assert not '<cite' in text, "Contains raw cite tag!"
    assert 'details class="ans-box"' in text, "Missing ans-box!"
    assert text.count('<svg') >= 2, "Must have at least 2 SVG diagrams!"
    print("VERIFICATION PASSED!")

if __name__ == '__main__':
    verify_file(sys.argv[1])
