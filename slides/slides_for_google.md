---
theme:
  notesRecipient: me
---

# Good Vibes
## Responsible use of AI for large-scale, rapid Earth Observation workflows

AB  ·  HFT  ·  HH  ·  JW

Institute of Zoology, Zoological Society of London

**ECCB 2026**

<!--
Welcome everyone to 'Good Vibes'. This workshop is about using AI responsibly — specifically for Earth Observation coding workflows. We'll cover what AI is, why it matters for conservation science, and six principles for working with it safely. Then we'll get hands-on.
-->

---

# 🤖 What is AI?
## …and why should you care?

<!--
Let's start with the basics. We're going to take about 5 minutes to frame what AI is, how we should think about it, and what it can do for us as researchers. This sets the stage for the principles and the practical work later.
-->

---

# The ChatGPT Moment
### An explosion of capability since Nov 2022

| Year | Milestone |
|------|-----------|
| Nov 2022 | ChatGPT launches → 100M users in 2 months |
| 2023 | GPT-4, Bard, Claude — multi-modal capabilities |
| 2024 | Reasoning models, agentic AI emerges |
| 2025 | AI coding agents, science-specific models |
| 2026 | 📍 You are here — AI in conservation workflows |

<!--
ChatGPT launched in November 2022 and reached 100 million users in just two months — the fastest adoption of any technology in history. Since then, the pace has been extraordinary. We've gone from novelty chatbots to multi-modal reasoning systems that can write code, analyse data, and even operate autonomously. The point isn't to hype AI — it's to recognise that this is a genuine paradigm shift, and as scientists we need to engage with it thoughtfully.
-->

---

# How We Think About AI
### The metaphor spectrum

| 🧑‍🤝‍🧑 Colleague | 🤝 Peer | 🔧 Tool | 🔍 Search Engine |
|:-:|:-:|:-:|:-:|

⚠️ **Important:** AI is *none of these perfectly*.
It reasons — but not like a human. It retrieves — but not like a database.
How you think about it shapes how you use it.

<!--
People tend to reach for familiar metaphors when thinking about AI. Some treat it like a colleague — expecting judgement and accountability. Others treat it like a search engine — expecting it to just look things up. The truth is it's none of these perfectly. It can reason, but it also hallucinates. It can retrieve information, but it can also fabricate it. The metaphor you carry into your interaction fundamentally shapes how you use it — and how likely you are to be caught out by its failures.
-->

---

# 📚 Use 1: Reviewing & Conceptualisation

🔬 **Literature Review**
Synthesise papers, identify gaps, find connections across disciplines

💡 **Brainstorming**
Generate hypotheses, explore alternative framings, challenge assumptions

🧪 **Hypothesis Generation**
Identify testable predictions from complex datasets and theory

<!--
The first big use case: conceptual work. AI is genuinely useful for literature review — not as a replacement for reading papers, but for synthesising across large bodies of work, spotting gaps, and helping you think across disciplines. It's also a powerful brainstorming partner. You can bounce ideas off it, ask it to challenge your assumptions, or explore alternative framings of a problem. Just remember: it can generate plausible-sounding but wrong hypotheses, so always verify.
-->

---

# 🧮 Use 2: Maths & Reasoning

📊 **Statistical Analysis**
Model selection, power calculations, interpreting complex outputs

📈 **Data Interpretation**
Explaining results, identifying patterns, suggesting visualisations

🔢 **Complex Calculations**
Unit conversions, spatial statistics, remote sensing indices

<!--
The second use case: quantitative reasoning. Modern LLMs are surprisingly capable at mathematics — model selection advice, interpreting statistical outputs, even working through complex derivations. For Earth Observation, think spectral index calculations, spatial statistics, or power analyses for your study design. The caveat: always double-check the maths. AI can make subtle errors that look entirely plausible.
-->

---

# 💻 Use 3: Coding
### This is what we'll focus on today

✍️ **Writing Code**
Generate scripts from natural language descriptions of your analysis

🐛 **Debugging**
Identify bugs, explain errors, suggest fixes — often faster than Stack Overflow

♻️ **Refactoring**
Improve code structure, add documentation, optimise performance

<!--
And here we get to today's focus: coding. AI can write code from scratch based on your descriptions, debug existing code by explaining errors and suggesting fixes, and refactor messy scripts into clean, documented, well-structured code. For many researchers, this is transformative — you don't need to be a software engineer to write production-quality analysis pipelines. But with that power comes responsibility, which is exactly what the rest of this talk is about.
-->

---

# 🎵 What is "Vibe Coding"?

> "There's a new kind of coding I call **vibe coding**, where you fully give in to the vibes, embrace exponentials, and forget that the code even exists."
> — Andrej Karpathy, Feb 2025

The spectrum of AI-assisted coding:

| Fully manual | AI-assisted | AI-led | Fully AI-generated |
|:-:|:-:|:-:|:-:|
| 🟢 | 🟡 | 🟠 | 🔴 |

For *scientific code*, we need to stay in the responsible middle of this spectrum.

<!--
Andrej Karpathy — one of the founders of OpenAI and former head of AI at Tesla — coined the term 'vibe coding' in early 2025. It describes the experience of describing what you want in natural language and letting AI write all the code. At one extreme, you write everything yourself. At the other, you let AI do everything and don't even read the output. For apps and prototypes, maybe that's fine. But for scientific code — where policy decisions depend on correct analysis — we need to be somewhere in the responsible middle. That's what today is about.
-->

---

But how do we do this
# responsibly?

↓

Six Principles for Working with AI

<!--
So we've seen what AI can do — literature review, maths, and especially coding. But the critical question is: how do we use these capabilities responsibly? How do we avoid publishing results based on buggy AI-generated code? That brings us to our six principles.
-->

---

# 📋 Six Principles
## for Responsible AI-Assisted Coding

<!--
This is the core of today's framing talk. Six principles that we think every researcher should follow when using AI to write code. These aren't theoretical — they come from our own experience of making mistakes and learning from them.
-->

---

# Principle 1
## 🧠 Treat It as an Intelligence

It reasons. Give it context, domain knowledge, and specifics.

- **Provide domain context** — "I'm analysing Sentinel-2 imagery for land cover classification in tropical forests"
- **Be specific** — "Use the SCL band to mask clouds, not QA60" rather than "remove clouds"
- **Share your constraints** — memory limits, time series length, study area extent
- **Don't treat it like a search bar** — it can reason through multi-step problems if you frame them well

<!--
Principle 1: treat AI as an intelligence, not a search engine. It can reason — but only if you give it the right context. Tell it what satellite you're using, what region, what time period, what your scientific question is. The more specific you are, the better the output. Don't just say 'remove clouds' — tell it which cloud masking band to use and why. Think of it as briefing a capable but uninformed colleague.
-->

---

# Principle 2
## 🔍 Distrust by Default

Assume output is plausible but wrong until verified.

🎭 AI is **confidently incorrect**.
Think of it as a *very keen but unreliable junior colleague* —
enthusiastic, articulate, and sometimes completely wrong.

- It will **invent** function names, band names, and API calls that don't exist
- It will produce code that **looks correct** but has subtle logical errors
- It will present wrong answers with **complete confidence**

<!--
Principle 2: distrust by default. This is perhaps the most important principle. AI is confidently incorrect. It will generate code that looks perfectly reasonable, uses plausible-sounding function names, and produces output — but the output might be completely wrong. Think of it as a very keen but unreliable junior colleague: they'll hand you beautifully formatted work, explain it eloquently, and be 100% confident — even when it's wrong. Your job is to verify everything.
-->

---

# Principle 3
## ✅ Verify with Tests

If you can't test it, you can't trust it.

- **Write unit tests** — test individual functions with known inputs and expected outputs
- **Check edge cases** — empty collections, null geometries, single-pixel regions
- **Validate against known answers** — use published datasets, manual calculations, or sanity checks
- **Ask AI to write tests too** — then verify the tests themselves!

💡 Pro tip: Ask AI to generate the code *and* the tests separately, then check they agree. Inconsistencies reveal bugs.

<!--
Principle 3: verify with tests. Unit testing isn't just good software practice — when working with AI, it's essential. Write tests with known inputs and expected outputs. Check edge cases: what happens with an empty image collection? A null geometry? A single pixel? Validate against published datasets or manual calculations. You can even ask AI to write the tests — but then you need to verify the tests themselves. The gold standard: generate code and tests separately, and check they agree.
-->

---

# Principle 4
## 📖 Prioritise Reporting & Interpretation

Don't just run code — understand what it does.

- **Can you explain every line?** If not, you don't understand your analysis
- **Document assumptions** — why this reducer? Why this scale? Why this time period?
- **Interpret results critically** — does the output make ecological sense?
- **Write for your future self** — add comments that explain *why*, not just *what*

<!--
Principle 4: prioritise reporting and interpretation. It's tempting to just run AI-generated code and use the output. But if you can't explain every line of that code, you don't actually understand your analysis. And if you don't understand your analysis, you can't defend it in peer review. Document your assumptions: why did you choose that reducer? That scale? That time period? Interpret results critically — does this NDVI trend make ecological sense for this biome? And write comments that explain WHY you made choices, not just what the code does.
-->

---

# Principle 5
## 💥 Engineer Adversity

Deliberately try to break your AI-generated code.

- **Feed it bad inputs** — wrong date formats, corrupted imagery, mismatched CRS
- **Test edge cases** — polar regions, date-line crossings, very large/small areas
- **Try empty datasets** — what happens when your filter returns zero images?
- **If it breaks, it wasn't robust** — and that's information you need *before* publication

🎯 Think like a **hostile reviewer** — what would they try?

<!--
Principle 5: engineer adversity. Don't just test the happy path — actively try to break your code. Feed it bad inputs: wrong date formats, corrupted imagery, mismatched coordinate systems. Test geographical edge cases: polar regions, the date line, tiny study areas, continent-scale areas. What happens when your image collection filter returns zero images? If the code breaks, that's information you need now — not after a reviewer finds the bug in your published results. Think like a hostile reviewer: what would they try?
-->

---

# Principle 6
## 🔓 Maximise Transparency

Document which parts are AI-generated and how.

- **Log your prompts** — save the conversations that generated your code
- **Version your code** — use Git; track the evolution from AI draft to final version
- **Capture metadata** — which model, which version, what date
- **Be honest in methods** — "Code was initially generated using [model] and subsequently reviewed, tested, and modified by the authors"

<!--
Principle 6: maximise transparency. This is about scientific integrity. Log your prompts — save the conversations that generated your code. Use version control so reviewers can see how the code evolved from AI draft to final version. Record which model you used, what version, and when. And be honest in your methods section: 'Code was initially generated using [model] and subsequently reviewed, tested, and modified by the authors.' This isn't a weakness — it's good scientific practice. Transparency builds trust.
-->

---

# The Six Principles
### Your checklist for responsible AI coding

| | Principle | Remember |
|---|-----------|----------|
| 🧠 | 1. Treat as Intelligence | Give context, be specific |
| 🔍 | 2. Distrust by Default | Assume wrong until verified |
| ✅ | 3. Verify with Tests | Can't test it? Can't trust it |
| 📖 | 4. Report & Interpret | Understand every line |
| 💥 | 5. Engineer Adversity | Try to break it |
| 🔓 | 6. Maximise Transparency | Log, version, disclose |

<!--
Here are all six principles together as a checklist. You might want to take a photo of this slide — it's a useful reference to keep beside you when you're working with AI. Each principle builds on the others: treat AI as intelligent so you get better output, but distrust that output until you've verified it with tests, understood it well enough to interpret it, tried to break it, and documented the whole process transparently.
-->

---

# ⚠️ Real Failures
### Common AI mistakes in Google Earth Engine

❌ **Wrong Band Names**
AI uses `B4`, `B8` for Sentinel-2 surface reflectance — but the actual band names are `SR_B4`, `SR_B8`. Code runs without error but produces garbage.

❌ **Incorrect Scale**
AI defaults to `scale: 30` (Landsat) for Sentinel-2 analysis. Results are technically valid but scientifically wrong — resampled at the wrong resolution.

❌ **Misapplied Reducers**
AI uses `ee.Reducer.mean()` where `ee.Reducer.median()` was needed for cloud-free compositing. Or applies a spatial reducer when a temporal reducer was intended.

<!--
Let's make this concrete with real examples from Google Earth Engine. First: wrong band names. AI will confidently use B4 and B8 for Sentinel-2 — which are correct for the raw product but wrong for surface reflectance collections where they're prefixed with SR_. The code runs without error, but produces garbage values. Second: incorrect scale. AI often defaults to 30 metres — which is Landsat's resolution — when you're working with 10-metre Sentinel-2 data. Third: misapplied reducers. Using mean instead of median for compositing, or confusing spatial and temporal reducers. These are exactly the kinds of bugs that Principles 2 through 5 are designed to catch.
-->

---

# 🌍 Why This Matters
### For conservation science

Policy decisions depend on **correct analysis**.
A bug in your deforestation script isn't just a software problem —
it's a *conservation* problem.

- 🌳 Habitat loss estimates feed into **protected area designations**
- 🦁 Species distribution models inform **IUCN Red List assessments**
- 🔥 Fire severity maps guide **post-disaster response** and funding allocation
- 💰 Carbon stock estimates drive **climate finance decisions** worth millions

**The stakes are too high for unchecked AI-generated code.**

<!--
And this is why we're spending time on principles before we touch code. In conservation science, the stakes are real. Habitat loss estimates feed directly into protected area designations. Species models inform Red List assessments. Fire maps guide disaster response. Carbon estimates drive climate finance worth millions. A subtle bug in your analysis code — one that AI introduced and you didn't catch — could lead to wrong conclusions, wrong policy decisions, and ultimately harm to the species and ecosystems we're trying to protect. That's why responsible AI coding isn't optional — it's essential.
-->

---

Now let's put this
# into practice

→

Hands-on practical session

<!--
That's the framing complete. You now have a mental model for what AI can do and six principles for using it responsibly. In the next section, we'll put this into practice — you'll use AI to write real Earth Observation code, and apply these principles to verify and improve it.
-->
