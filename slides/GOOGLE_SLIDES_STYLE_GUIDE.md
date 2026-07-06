# Google Slides Style Guide — ZSL Good Vibes Workshop

Apply these settings after importing from `md2googleslides` to match the ZSL IoZ branding.

---

## Slide Theme Setup (Slide → Edit theme)

### Background
- **Main slides:** Solid colour `#002110` (Burnham — very dark green)
- **Section header slides** (slides 2, 10, 22): Solid `#004D25` (mid-dark green — or as close as Google Slides allows)

### Fonts
- **All text:** Inter (available in Google Slides via Add-ons → search "Inter")
- **Fallback:** Arial or Roboto if Inter is not available
- **Title text:** White `#FFFFFF`, Bold (800 weight), 36–44pt
- **Subtitle text:** `#DEC6A2` (Sapling — warm beige), Medium weight, 20–24pt
- **Body text:** White `#FFFFFF`, Regular weight, 16–18pt
- **Emphasis / keywords:** `#C7F700` (Electric Lime — bright yellow-green), Bold

### Colours at a Glance

| Name | Hex | Use |
|------|-----|-----|
| Fun Green | `#008945` | Principle number circles, section header backgrounds, accent borders |
| Burnham | `#002110` | Main slide background |
| Sapling | `#DEC6A2` | Subtitles, secondary text |
| Electric Lime | `#C7F700` | Bold keywords, highlighted text, "strong" emphasis |
| White | `#FFFFFF` | Primary text, headings |
| Error Red | `#FF6B6B` | Failure example titles (slide 19 only) |

---

## Logo Placement

- Place `zsl-ioz.png` in the **top-right corner** of every slide
- Size: approximately **90px wide** (or ~2.5cm in Google Slides)
- Set to ~85% opacity if Google Slides supports it (otherwise leave at 100%)
- Tip: Add it to the **Slide Master** so it appears on every slide automatically

---

## Slide-by-Slide Layout Notes

| Slide # | Title | Layout suggestion |
|---------|-------|-------------------|
| 1 | Title slide | Centre-aligned, title large, subtitle + authors below, "ECCB 2026" as a green rounded badge |
| 2 | Section header: What is AI | Green background `#004D25`, large title centred |
| 3 | ChatGPT Moment | Table with timeline milestones |
| 4 | Metaphor Spectrum | 4-column table with emojis, callout box below |
| 5 | Use 1: Reviewing | 3 rows: emoji + bold title + description |
| 6 | Use 2: Maths | Same layout as slide 5 |
| 7 | Use 3: Coding | Same layout as slide 5 |
| 8 | Vibe Coding | Blockquote, 4-column spectrum table |
| 9 | Transition: "responsibly?" | Centre-aligned, minimal, large title |
| 10 | Section header: Six Principles | Green background `#004D25` |
| 11–16 | Principle 1–6 | Green-bordered card at top (title + summary), bullet list below |
| 17 | Six Principles summary | 6-row table with emoji, name, reminder |
| 18 | Real Failures | 3 red-tinted cards with ❌ prefix |
| 19 | Why This Matters | Callout box + bullet list |
| 20 | Transition: "into practice" | Centre-aligned, minimal |

### Principle Card Style (Slides 11–16)

Each principle slide has a "card" at the top:
- **Background:** A rounded rectangle shape filled with `#008945` at ~20% opacity (or a subtle green tint)
- **Border:** 1px `#008945`
- **Content:** Principle number in a green circle, title in Electric Lime, description in white
- **Below the card:** Bullet points in white, 16pt

### Failure Card Style (Slide 18)

- **Background:** A rounded rectangle shape filled with a subtle red tint
- **Border:** 1px `rgba(220,60,60,0.3)` — or just a light red
- **Title:** `#FF6B6B` (salmon red), bold
- **Body:** White text, `code` fragments in Electric Lime

---

## Quick Setup Checklist

- [ ] Set slide dimensions to **Widescreen 16:9**
- [ ] Set default background to `#002110`
- [ ] Set default font to Inter (or Arial)
- [ ] Add `zsl-ioz.png` to the Slide Master in top-right
- [ ] Apply green backgrounds to section header slides (2, 10)
- [ ] Check all emphasis text uses `#C7F700` (Electric Lime)
- [ ] Check all subtitle text uses `#DEC6A2` (Sapling)
