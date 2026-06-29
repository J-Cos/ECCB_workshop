# 🎤 Antigravity Live Demo — Presenter's Script

**Workshop:** Good Vibes: Responsible use of AI for large-scale, rapid Earth Observation workflows  
**Conference:** ECCB 2026  
**Duration:** ~5 minutes  
**File under refactoring:** `messy_gee_script.py`

---

## 🟢 Introduction (30 seconds)

> **Say to audience:**
>
> "Let me show you what this looks like in practice. I have here a real Google Earth Engine script that analyses deforestation in Borneo using the Hansen Global Forest Change dataset. It works — it loads data, computes tree cover loss by year, calculates areas, and even draws a little ASCII chart.
>
> But look at it. Could you maintain this? Could you test it? Could you hand this to a colleague and expect them to understand what `temp`, `d`, `r`, or `result2` mean? Could you come back to this in six months?
>
> This is typical hastily-written research code. Let's see what agentic AI can do with it."

**Action:** Have `messy_gee_script.py` open in the editor. Scroll through it briefly to show the audience the mess.

---

## 🔵 Prompt 1: Refactor (1.5 minutes)

### Prompt to type into Antigravity:

```
Refactor this messy_gee_script.py into clean, well-structured Python with descriptive
function names, proper separation of concerns (data loading, processing, analysis,
visualisation), and remove all magic numbers in favour of named constants.
```

### While it's working — point out to the audience:

- **Function extraction:** Watch how it pulls inline code into named functions like `load_hansen_dataset()`, `calculate_loss_by_year()`, `compute_forest_area()`
- **Constants:** Magic numbers like `30` (tree cover threshold), the bounding box coordinates, and `range(1, 24)` become named constants at the top: `TREE_COVER_THRESHOLD = 30`, `BORNEO_BBOX = [...]`, `ANALYSIS_YEARS = range(2001, 2024)`
- **Separation of concerns:** Data loading, processing, analysis, and display move into distinct sections or functions
- **Main guard:** It adds `if __name__ == '__main__':` — a small thing that enables importing without side effects

### Talking point:

> "Notice it didn't just reformat — it *restructured* the logic. It identified that this monolith has four distinct responsibilities and separated them. That's software engineering judgement, not just search-and-replace."

---

## 🟣 Prompt 2: Documentation (1 minute)

### Prompt to type into Antigravity:

```
Add comprehensive Google-style docstrings to all functions, add type hints,
and add a module-level docstring explaining what this script does, its inputs,
outputs, and dependencies.
```

### While it's working — point out to the audience:

- **Module-level docstring:** Describes purpose, data sources, dependencies, and expected outputs
- **Google-style docstrings:** Each function gets `Args:`, `Returns:`, and sometimes `Raises:` sections
- **Type hints:** `def calculate_loss_by_year(loss_image: ee.Image, region: ee.Geometry, ...) -> dict[int, float]:`
- **Accuracy:** The docstrings actually describe what the code does, not generic boilerplate

### Talking point:

> "Documentation that would take 30 minutes of careful writing, done in seconds. And it's *accurate* — it read the code and described what it actually does. This is Principle 2 from our framework — Contextualise. The AI understands the domain context."

---

## 🟠 Prompt 3: Unit Tests (1.5 minutes)

### Prompt to type into Antigravity:

```
Write pytest unit tests for all pure functions in this module. Mock the ee module
for functions that call GEE. Include edge cases like empty regions and zero forest cover.
```

### While it's working — point out to the audience:

- **Test structure:** Separate test file with clear test names like `test_calculate_loss_percentage_normal`, `test_calculate_loss_percentage_zero_forest`
- **Mocking strategy:** Uses `unittest.mock.patch` to mock `ee` module calls — the tests run without GEE authentication
- **Edge cases:** Tests for zero forest cover (division by zero), empty result dictionaries, negative net change
- **Assertions:** Checks both values and types

### Talking point:

> "This is Principle 3 — Verify — automated. These tests are the safety net that lets us refactor with confidence. Notice it identified the pure functions that *can* be tested without GEE, and mocked the ones that can't. That's a real testing strategy, not just boilerplate."

---

## 🔴 Prompt 4: Integration Test (30 seconds)

### Prompt to type into Antigravity:

```
Write an integration test that runs the full analysis pipeline on a small test region
and validates the output structure and value ranges.
```

### While it's working — point out to the audience:

- **Small test region:** Uses a tiny bounding box to keep the test fast
- **Structure validation:** Checks that results contain expected keys and that values are non-negative
- **End-to-end:** Validates the full pipeline from data loading to output

### Talking point:

> "Now we have confidence the refactored code still produces correct results. The integration test is the bridge between 'it looks right' and 'it *is* right'."

---

## 🟢 Wrap-up (30 seconds)

> **Say to audience:**
>
> "In five minutes, we went from unmaintainable research code to a tested, documented, professional codebase. The script still does exactly the same analysis — same data, same results — but now it's:
>
> - **Readable** — a new team member can understand it
> - **Testable** — we have automated verification
> - **Maintainable** — we can change one thing without breaking everything
> - **Reproducible** — constants are explicit, not buried in code
>
> This is what agentic AI can do for your research code. But remember our six principles. We still need to **review** everything it generated, **verify** the tests actually pass, and **understand** the changes before we commit them. The AI is a powerful assistant, but you are still the scientist."

---

## ⚠️ Fallback Plan

### If Antigravity is slow or unresponsive:

> "Live demos and conference Wi-Fi are natural enemies. I ran this exact sequence yesterday and captured the output. Let me walk you through what happened."

**Action:** Open the pre-captured screenshots from `fallback_screenshots/` and walk through each step narrating the same talking points above.

### If Antigravity produces unexpected output:

> "This is actually a great teaching moment — this is why Principle 3, Verify, matters. The AI doesn't always produce what you expect, and you need to critically evaluate every output."

### Pre-demo checklist:

- [ ] `messy_gee_script.py` is open in the editor
- [ ] Antigravity is running and authenticated
- [ ] GEE authentication is active (`ee.Initialize()` works)
- [ ] Fallback screenshots are captured from a dry run
- [ ] Font size is large enough for the back of the room (≥18pt)
- [ ] Terminal and editor side-by-side layout ready
- [ ] Backup copy of messy script (in case you need to reset mid-demo)

### Timing guide:

| Section          | Duration | Cumulative |
|------------------|----------|------------|
| Introduction     | 0:30     | 0:30       |
| Prompt 1: Refactor | 1:30  | 2:00       |
| Prompt 2: Docs   | 1:00     | 3:00       |
| Prompt 3: Unit Tests | 1:30 | 4:30       |
| Prompt 4: Integration | 0:30 | 5:00      |
| Wrap-up          | 0:30     | 5:30       |

**Buffer:** ~30 seconds for Antigravity response time. Total should fit comfortably in 6 minutes.
