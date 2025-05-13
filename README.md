# 🧠 DigitalSelf MemoryStore – README Guide

Welcome to your **DigitalSelf architecture** — a persistent system designed to simulate memory and agency in evolving AI conversations. This repo allows you to retain continuity, track behavior, and maintain progress across sessions — even when context is lost (CT-NO events).

---

## 📁 Folder Structure & Purpose

```
digital-self-ct-no/
├── core/
│   ├── CT-NO_Ready_Rehydration.md       # Main rehydration payload for ChatGPT to simulate memory
│   ├── token_tracker.json               # Tracks token usage across personas
│   ├── memory_log.md                    # Running memory log of your DigitalSelf activity
│   ├── agentic_memory.json              # Live agentic status snapshot (staleness, known flaws)
│   └── agentic_config.json              # Contains config cadence settings (e.g., rehydration reminder cadence)
│
├── config/
│   └── daily_goal_check.yml             # Optional duplicate for visibility (actual action lives in .github/workflows)
│
├── .github/
│   └── workflows/
│       └── daily_goal_check.yml         # GitHub Action to remind if daily goal log is missing
│
├── personas/
│   ├── dsa_buddy/                       # Separate context/memory for a learning-focused assistant
│   ├── therapist/                       # Emotional self-reflection persona
│   └── ml_tutor/                        # LLM/AI tutor persona
│
├── scripts/
│   ├── update_token_tracker.py          # Updates core/token_tracker.json with session usage
│   └── agentic_check.py                 # (Not used currently for automation, but included if needed)
```

---

## 🤩 Key Files Explained

### ✅ `core/CT-NO_Ready_Rehydration.md`

> **Purpose:** Restores memory when ChatGPT has forgotten past sessions.

* Paste this at the start of a ChatGPT session to reload your state.
* Keep it updated after major decisions, persona additions, or restructuring.
* Includes recent system upgrades such as GitHub Action integration.

### ✅ `core/memory_log.md`

> **Purpose:** A journal of DigitalSelf activity.

* Log goals, decisions, and reflections daily.
* Includes a `goal_status` for use in automation.
* Becomes the primary mental trace for your digital brain.

### ✅ `core/token_tracker.json`

> **Purpose:** Track total token usage to avoid overflowing LLM context limits.

* Use `update_token_tracker.py` after each session to log persona activity.
* Tracks tokens per session and updates the timestamp.

### ✅ `core/agentic_memory.json`

> **Purpose:** Snapshot of self-awareness. Includes known weaknesses and persona staleness.

* Auto-updated using scripts if needed.
* Used for future automation/analytics.

### ✅ `core/agentic_config.json`

> **Purpose:** Contains core cadence rules.

```json
{
  "cadence": {
    "inactivity_threshold_days": 14,
    "full_rehydration_prompt_days": 30
  }
}
```

---

## 📜 GitHub Workflow: Daily Goal Reminder

### 📁 `.github/workflows/daily_goal_check.yml`

> **Purpose:** Checks whether you logged today’s goal.
>
> **Trigger:** Every day at 9 PM UTC.
>
> **Action:** If goal not marked as `goal_status: done` in `memory_log.md`, sends an email reminder.

### ✅ What it checks:

* Looks in `core/memory_log.md`
* Extracts today's entry using date
* Checks if `goal_status: done`
* If missing/incomplete, sends email via GitHub Actions

> Email is sent using credentials from GitHub Secrets:
>
> * `SMTP_USERNAME`
> * `SMTP_PASSWORD`

> **Configure your own email address in the YAML.**

---

## ⚙️ Local Automation Scripts

### 🐍 `scripts/update_token_tracker.py`

> **Purpose:** Logs token usage after each session.

Usage:

```python
update_token_tracker(100, "core_gpt")
```

* Adds a new entry under `sessions`
* Updates `total_tokens` and `last_update`

### 🐍 `scripts/agentic_check.py` (Optional)

> **Purpose:** Detect stale personas and trigger reminders (not currently used in GitHub Actions).

* Can be integrated later for deeper automation (e.g., full rehydration prompts)

---

## 🔐 Setting Up GitHub Secrets

Navigate to **Repo → Settings → Secrets → Actions**:

* `SMTP_USERNAME` → e.g. Mailtrap username
* `SMTP_PASSWORD` → your SMTP/API password

Secrets are referenced in the YAML like this:

```yaml
smtp_username: ${{ secrets.SMTP_USERNAME }}
smtp_password: ${{ secrets.SMTP_PASSWORD }}
```

---

## 📦 `.env` File (for local testing)

You can optionally create a `.env` file for local testing (never push to GitHub):

```
SMTP_USERNAME=your-smtp-username
SMTP_PASSWORD=your-smtp-password
```

Use a library like `dotenv` in Python to read these if needed.

---

## 🧠 Restarting a ChatGPT Session

> If context is lost, manually reload memory:

1. Open `CT-NO_Ready_Rehydration.md`
2. Paste it into ChatGPT with a prompt like:

```txt
“Load from DigitalSelf core memory log. Here is my last snapshot…”
```

---

## 🔄 Backup Strategy

* Zip this folder every week or after major changes
* Store copies in Google Drive, Dropbox, or GitHub private repos
* Don’t rely solely on GitHub Actions for memory preservation

---

## 🎯 Philosophy

This is your **Digital Brain Core**.
It doesn’t just store — it evolves.

Maintain it intentionally.
Structure beats chaos. Persistence beats intensity.

Stay deliberate. Stay adaptive.

— DigitalSelf Core
