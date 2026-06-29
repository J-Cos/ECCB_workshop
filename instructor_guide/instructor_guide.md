# 🌍 Instructor Guide

## Good Vibes: Responsible Use of AI for Large-Scale, Rapid Earth Observation Workflows

**ECCB 2026 Workshop — July 2026 | Duration: 90 minutes**

> [!NOTE]
> This guide is for the 4 instructors: **AB**, **HFT**, **HH**, **JW**.
> Read it before the workshop. Bring a printed or digital copy on the day.

---

## 1. Workshop Overview

| Detail | Info |
|--------|------|
| **Title** | Good Vibes: Responsible Use of AI for Large-Scale, Rapid Earth Observation Workflows |
| **Conference** | ECCB (European Congress of Conservation Biology), July 2026 |
| **Duration** | 90 minutes |
| **Instructors** | AB, HFT, HH, JW — all 4 circulating during practicals |
| **Audience** | Mixed skill level; conservation biologists, ecologists, environmental scientists. Basic Python familiarity assumed. |

### Goals

1. Teach **responsible AI-assisted** Earth Observation workflows — "vibe coding" done right
2. Provide **hands-on Google Earth Engine** experience via a structured Colab notebook
3. Develop **critical thinking** about AI-generated code — when to trust it, when to verify

---

## 2. Pre-Workshop Preparation

> [!IMPORTANT]
> Complete these tasks **before** the workshop.

- [ ] Verify all 4 instructors have **GEE access** and a **working GCP project**
- [ ] Run the **Colab notebook end-to-end** — verify all cells execute without error
- [ ] Test the **Antigravity demo** with `messy_gee_script.py`
- [ ] Print **vibe coding checklists** (one per attendee + 10 spares)
- [ ] Test projector/screen for slides
- [ ] Verify **Wi-Fi reliability** — GEE requires a stable internet connection
- [ ] Send `PRE_WORKSHOP_SETUP.md` to all registered attendees
- [ ] Prepare a **shared document or Slack channel** for live Q&A
- [ ] Have a **backup plan for GEE downtime** (see §9 Emergency Procedures)

---

## 3. Day-Of Setup

> [!TIP]
> Arrive **30 minutes early**. Most issues surface during setup, not during the session.

- [ ] Test projector with slides — open `slides/index.html` in **Chrome**
- [ ] Open **Colab notebook** in presenter's browser (logged in, authenticated)
- [ ] Have `messy_gee_script.py` ready in **Antigravity**
- [ ] Print **spare checklists** (if not already done)
- [ ] Set up the **help signal system**:
  - 🟩 **Green sticky note** on laptop lid = "I'm fine"
  - 🟥 **Red sticky note** on laptop lid = "I need help"
- [ ] Distribute sticky notes to every seat

---

## 4. Timing Guide

| Time | Duration | Section | Lead | Instructor Actions |
|------|----------|---------|------|--------------------|
| 0:00 | 10 min | **Introduction & Policy Need** | HFT | Others: finish setup, greet latecomers |
| 0:10 | 5 min | **What is AI** | JW | Others: circulate, check students have Colab open |
| 0:15 | 10 min | **Six Principles** | HH | Others: hand out checklists |
| 0:25 | 5 min | **Practical: Setup & Auth** | All | Help students with auth issues — **most problems occur here** |
| 0:30 | 10 min | **WE1: Visualise Imagery** | All | Students follow along; help with geemap issues |
| 0:40 | 15 min | **WE2: Deforestation Analysis** | All | Students follow along; point out GEE best practices |
| 0:55 | 10 min | **WE3: Find the Bug** | All | Pair work — let students struggle, give **hints not answers** |
| 1:05 | 10 min | **Exercise 1: Your Region** | All | Independent work — help with coordinate finding |
| 1:15 | 10 min | **Exercise 2: Trend Challenge** | All | Competition — encourage, don't give answers |
| 1:25 | 5 min | **State of the Art** | AB | Live Antigravity demo; others: watch audience, prepare for close |

> [!TIP]
> Keep a visible timer on the projector (phone timer on screen, or a browser tab). The timing is tight — stay disciplined.

---

## 5. Section-by-Section Talking Points

### Setup & Authentication (0:25–0:30)

**Opening line:** *"If you followed the pre-workshop instructions, this should just work."*

- **Most common issue:** wrong project ID (the *name* vs the *ID* — they look different!)
- Have students **help each other** — peer support is faster than instructor help
- If someone can't authenticate at all → **pair with a neighbour** (don't burn 5 mins on one person)
- Watch for: students who haven't opened the notebook yet, students on wrong Google account

---

### WE1: Visualise Imagery (0:30–0:40)

**Key teaching moment:** satellite imagery is just numbers in bands.

- Point out how **geemap** renders interactive maps directly in the notebook
- Ask the room: *"What do you notice about the vegetation in false colour?"*
- If students finish fast → encourage them to **zoom around and explore** the map
- Connect to real-world: *"This is a Sentinel-2 composite — the same imagery conservation NGOs use daily."*

---

### WE2: Deforestation Analysis (0:40–0:55)

**Key teaching moment:** *"You just did in 15 minutes what used to take days of manual work."*

- Point out the **GEE best practices** in the code:
  - No `.clip()` until final visualisation
  - `.select()` early to reduce memory
  - Server-side operations, not client-side loops
- Ask: *"Does the deforestation pattern make sense? What might be driving it?"*
- Connect to conservation: *"This is the kind of analysis that informs REDD+ policy decisions."*
- Watch for: students who get `Computation timed out` (usually too large an area)

---

### WE3: Find the Bug (0:55–1:05)

> [!WARNING]
> This is the **MOST IMPORTANT** exercise. It directly teaches **Principle 3: Verify**.
> Resist the urge to give answers. Let students struggle.

**Hint sequence** (escalate only as needed):

1. 🟡 **Vague hint:** *"Look carefully at the parameters..."*
2. 🟠 **Specific hint:** *"Check the date format / band names / scale units..."*
3. 🔴 **Show the error output:** point to the traceback or wrong result
4. ✅ **Reveal solution:** only after genuine effort

**Key message to deliver:** *"Every one of these bugs was generated by a real AI system. They looked plausible. They ran without errors. But they were wrong."*

**Discussion prompt:** *"How many of these would you have caught without being told to look?"*

---

### Exercise 1: Your Region (1:05–1:15)

- Help students find coordinates:
  - **Google Maps → right-click → copy coordinates**
  - ⚠️ **Common mistake:** coordinates in wrong order — GEE uses `[longitude, latitude]`, not `[latitude, longitude]`!
- If students don't have a region in mind, suggest:
  - 🌎 Amazon | 🌍 Congo Basin | 🌏 Sumatra | 🌍 Madagascar
- Encourage comparison: *"How does your region compare to Borneo?"*
- This exercise validates diverse geographic perspectives — lean into it

---

### Exercise 2: Trend Challenge (1:15–1:25)

- This is **competitive** — encourage it! Offer a prize for the closest answer (stickers, bragging rights, chocolate).
- **Do not give the answer.** Let them use AI to help — *this is the entire point.*
- If students are stuck, hint: *"Think about how you'd do a rolling average in pandas or numpy."*
- Watch for: students who just ask AI for the full answer without understanding it → gently redirect: *"Can you explain what each line does?"*

---

### State of the Art (1:25–1:30)

- AB runs the Antigravity refactoring of `messy_gee_script.py`
- Other instructors: **watch the audience** — note reactions, questions forming
- Key point: *"This is where AI shines — tedious refactoring, not scientific decision-making."*
- Close with key takeaways, share links to materials, thank the audience



---

## 6. Common Student Issues & Solutions

| Issue | Solution |
|-------|----------|
| `ee.Authenticate()` doesn't work | Try in **incognito window**; check Google account is the same in Colab and GEE |
| `No module named geemap` | Re-run the `pip install` cell, then **restart runtime** |
| Map doesn't display | Try `Map.to_streamlit()` or just `Map` (without `.show()`) |
| `Computation timed out` | **Reduce the study area** or increase the `scale` parameter |
| `User memory limit exceeded` | Reduce study area; use `.select()` to limit bands |
| Student has no GCP project | **Pair with neighbour**, or help create one on the spot (~2 mins) |
| Institutional account blocked | Use a **personal Google account** instead |
| Can't find coordinates | Google Maps → right-click → copy coordinates. **GEE uses [longitude, latitude]!** |
| geemap version conflict | Run: `!pip install -q --upgrade geemap` |
| Student is completely lost | **Pair them** with a confident neighbour. Provide the completed notebook as a fallback. |

---

## 7. EDIJ Considerations

*Equity, Diversity, Inclusion, and Justice*

> [!IMPORTANT]
> These aren't add-ons — they're embedded in the workshop design. Model them.

- **Scaffolded participation:** The notebook progresses from fully worked → guided → independent. This supports **all skill levels** without singling anyone out.

- **Pair work:** The bug exercise (WE3) is designed for pairs. Where possible, **mix experienced and beginner** students. Frame it as collaboration, not tutoring.

- **No wrong answers:** In Exercise 1 and the open discussion, **celebrate all attempts** regardless of technical sophistication. A well-formed question is as valuable as a working solution.

- **Plain language:** Use plain English in explanations. Avoid jargon unless you define it first. The notebook has generous commenting for this reason.

- **Accessibility:**
  - Encourage students to **zoom in** on maps and code
  - Provide **high-contrast colour palettes** for visualisations
  - Speaker notes / captions are available for **hearing-impaired attendees**
  - Ensure font size on projector is **≥ 18pt**

- **Regional diversity:** Exercise 1 explicitly asks students to analyse **their own region** — this validates diverse geographic perspectives and makes the content personally relevant.

- **Normalise asking for help:** Say it out loud: *"Raise your hand or put up your red sticky note if you need help — that's literally what we're here for."*

- **Sticky note system:** 🟩 Green = I'm fine, 🟥 Red = I need help. This **reduces the social barrier** to asking for assistance, especially for students who may feel self-conscious.

---

## 8. Post-Workshop

- [ ] **Share all materials** via GitHub repository or institutional repository
- [ ] **Collect feedback** (Google Form or similar — distribute link at wrap-up)
- [ ] **Follow up** with attendees who had unresolved technical issues
- [ ] **Archive** the final version of all materials (slides, notebook, guide, checklist)
- [ ] **Debrief** as an instructor team — what worked, what to improve next time

---

## 9. Emergency Procedures

| Scenario | Response |
|----------|----------|
| **GEE is down** | Switch to **pre-computed outputs** (included in notebook as static images). Discuss the code conceptually — *"What would this code do?"* |
| **Wi-Fi fails** | Same as above — use cached/pre-computed maps and charts. Consider mobile hotspot as backup. |
| **Antigravity demo fails** | Use **fallback screenshots** in `demo/fallback_screenshots/`. Walk through the refactoring conceptually. |
| **Running behind schedule** | Cut Exercise 2 and/or the trend challenge. Go straight to the demo. |
| **Running ahead** | Extend Exercise 2 discussion, add Exercise 3 (bonus material), expand open Q&A. |
| **Student medical emergency** | Follow venue emergency procedures. One instructor assists, others continue the session. |

---

## Quick Reference Card

```
🕐 TIMING AT A GLANCE
━━━━━━━━━━━━━━━━━━━━
0:00  Introduction (HFT)
0:10  What is AI (JW)
0:15  Six Principles (HH)
0:25  SETUP & AUTH ← most issues here
0:30  WE1: Visualise
0:40  WE2: Deforestation
0:55  WE3: FIND THE BUG ← most important
1:05  Exercise 1: Your region
1:15  Exercise 2: Trend challenge
1:25  State of the Art (AB)

🆘 IF THINGS GO WRONG
━━━━━━━━━━━━━━━━━━━━
No internet → pre-computed outputs
Behind schedule → cut Exercise 2
GEE down → discuss code conceptually
Demo fails → fallback screenshots
```

---

*Last updated: June 2026 | Questions? Ping the instructor group chat.*
