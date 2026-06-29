# 🌍 Good Vibes Workshop — Pre-Workshop Setup Guide

**ECCB 2026 | Responsible use of AI for large-scale, rapid Earth Observation workflows**

Welcome! To make the most of our workshop, please complete the setup steps below **before the workshop**.

---

## Step 1: Google Account

You'll need a Google account to access Google Earth Engine, Google Cloud, and Google Colab.

- **If you already have a Google account** (Gmail, Google Workspace, or institutional Google account), you're all set.
- **If your institution restricts Google services**, you may need to create a free personal Google account at [accounts.google.com](https://accounts.google.com/).

## Step 2: Register for Google Earth Engine

1. Go to **[https://code.earthengine.google.com/](https://code.earthengine.google.com/)**
2. Sign in with your Google account
3. Accept the **Terms of Service**
4. If prompted, choose **'Unpaid/Academic'** as your usage type
5. Wait for your registration to be approved

✅ You'll know it worked when you can see the Earth Engine Code Editor interface.

## Step 3: Set Up a Google Cloud Project

Google Earth Engine now requires a Cloud Project for authentication. Here's how to set one up:

1. Go to **[https://console.cloud.google.com/](https://console.cloud.google.com/)**
2. Sign in with the **same Google account** you used for Earth Engine
3. Click **"Select a project"** (top navigation bar) → **"New Project"**
4. Name it anything you like (e.g., `eccb-workshop-2026`)
5. Click **"Create"**
6. **Note your Project ID** — this is different from the project name!
   - Find it under: **Cloud Console → Select your project → Dashboard → Project info → Project ID**
   - It will look something like: `eccb-workshop-2026` or `my-project-12345`
   - 📌 **Write this down — you'll need it during the workshop**
7. **Enable the Earth Engine API:**
   - Go to **APIs & Services → Library**
   - Search for **"Earth Engine"**
   - Click **"Google Earth Engine API"**
   - Click **"Enable"**

> 💡 **No billing account is required** for Earth Engine with academic/unpaid usage. If prompted to set up billing, you can skip it.

## Step 4: Test Everything in Google Colab

Let's make sure everything works together before the workshop.

1. Go to **[https://colab.research.google.com/](https://colab.research.google.com/)**
2. Make sure you're signed in with the **same Google account**
3. Create a **new notebook** (File → New Notebook)
4. Paste the following code into a cell and run it:

```python
# ── Good Vibes Workshop — Setup Test ──

# Install the Earth Engine Python API
!pip install -q earthengine-api

# Import and authenticate
import ee

# This will open a browser window for authentication
# Follow the prompts and allow access
ee.Authenticate()

# ⚡ IMPORTANT: Replace 'YOUR-PROJECT-ID' with your actual Cloud Project ID
ee.Initialize(project='YOUR-PROJECT-ID')

# Test: Load a MODIS image collection and check it works
collection = ee.ImageCollection('MODIS/061/MOD13A1').filterDate('2023-01-01', '2023-02-01')
count = collection.size().getInfo()

print('✅ Setup successful!')
print(f'   Collection: MODIS/061/MOD13A1')
print(f'   Images found: {count}')
print(f'   You are ready for the Good Vibes workshop! 🎉')
```

5. When prompted, follow the authentication flow in your browser
6. If you see **"✅ Setup successful!"** — you're ready!

## Troubleshooting

### "I can't register for Earth Engine"
- Try using a **personal Google account** instead of an institutional one
- Check your **spam/junk folder** for a verification email from Google
- If registration is still pending, try registering again with a different Google account

### "I don't see a Project ID"
- Go to [Cloud Console](https://console.cloud.google.com/)
- Select your project from the top dropdown
- The **Project ID** is on the Dashboard under "Project info"
- ⚠️ The Project ID is different from the Project Name — use the ID!

### "Authentication fails in Colab"
- Make sure you're signed into the **same Google account** in both Colab and Earth Engine
- Try: Runtime → Restart runtime, then re-run the cell
- Make sure you've completed the authentication popup in your browser

### "pip install fails"
- Try restarting the Colab runtime: **Runtime → Restart runtime**
- Then re-run the install cell

### Still stuck?
- We'll have a short troubleshooting session at the start of the workshop — don't worry!

## What to Bring

- 💻 **Laptop** with a modern web browser (Chrome recommended)
- 🔑 **Your Google Cloud Project ID** (from Step 3)
- 🔌 **Charger!**
- 🗺️ **A geographic region you're interested in** — bring lat/lon coordinates for a study area, national park, city, or ecosystem you'd like to explore. You'll use this in the hands-on exercises!

---

*Good Vibes Workshop — ECCB 2026 | AB, HFT, HH, JW | ZSL Institute of Zoology | CC BY 4.0*
