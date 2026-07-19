# 🤝 SchemeSetu — AI Welfare Scheme Navigator

**Theme:** Sustainability & Social Impact
**Hackathon:** NxtWave Academy Idea2Impact Online Hackathon

## Problem Statement

Millions of eligible people in India — especially rural citizens, daily-wage
workers, students, and women — miss out on government welfare schemes
(scholarships, health insurance, women & child welfare programs, disability
benefits, etc.) simply because:

- Eligibility rules are scattered across dozens of government websites in
  dense bureaucratic language.
- People don't know a scheme exists that applies to their exact situation.
- Even when they know a scheme exists, the application process (documents,
  portals, offices) is confusing.

**Who it affects:** Low-income families, rural communities, first-generation
students, and anyone without easy access to a government helpline or agent.

**Why existing solutions fail:** Government scheme portals (like myscheme.gov.in)
require the user to already know what to search for and can be overwhelming
to navigate. There's no simple, conversational way to just describe your
situation and get a personalized answer.

## Our Solution

SchemeSetu is a lightweight web app where a user fills in a short profile
(state, income, occupation, category, education, disability status, and what
they need help with). An LLM (Llama 3 via Groq) reasons over this profile and:

1. Suggests the top schemes they likely qualify for
2. Explains eligibility against their specific profile
3. Gives plain-language, step-by-step application instructions

A second tab lets users ask free-form questions ("Can an SC-category diploma
student get a scholarship in Tamil Nadu?") and get a direct, simple answer.

**AI is central, not decorative** — the matching, eligibility reasoning, and
plain-language explanation are all generated live by the LLM based on the
user's actual input, not hardcoded rules.

## Tech Stack

- **Frontend/Backend:** [Streamlit](https://streamlit.io) (Python)
- **AI:** Groq API (`llama-3.1-8b-instant`) — chosen for its free tier and speed
- **Deployment:** Streamlit Community Cloud / Hugging Face Spaces / Render

## Setup Instructions (Local)

```bash
git clone <this-repo-url>
cd schemesetu
pip install -r requirements.txt
export GROQ_API_KEY="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"   
streamlit run app.py
```

## Deployment

This app is deployed and live at: **[ADD YOUR DEPLOYED LINK HERE]**

## Demo Video

**[ADD YOUR 2–3 MIN DEMO VIDEO LINK HERE]**

## Future Scope

- Regional language support (Tamil, Hindi, Telugu, etc.)
- Direct links to official application portals per scheme
- SMS/WhatsApp interface for users without smartphones
