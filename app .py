"""
SchemeSetu — AI Welfare Scheme Navigator
------------------------------------------
Helps underserved citizens discover Indian government welfare schemes
they're eligible for, and explains how to apply — in plain language.

AI: Uses Groq's free LLM API (Llama 3) to reason over the user's
profile and generate personalized, accurate scheme recommendations
and application guidance.
"""

import os
import json
import streamlit as st
from groq import Groq

st.set_page_config(page_title="SchemeSetu — AI Welfare Scheme Navigator", page_icon="🤝", layout="centered")

# ---------- AI CLIENT ----------
API_KEY = os.environ.get("GROQ_API_KEY", "")

def get_client():
    if not API_KEY:
        return None
    return Groq(api_key=API_KEY)

def ask_ai(system_prompt, user_prompt):
    client = get_client()
    if client is None:
        return ("⚠️ No GROQ_API_KEY found. Add your free Groq API key as an environment "
                "variable / secret named GROQ_API_KEY to enable AI responses.")
    try:
        completion = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
            temperature=0.4,
            max_tokens=900,
        )
        return completion.choices[0].message.content
    except Exception as e:
        return f"⚠️ AI request failed: {e}"

# ---------- UI ----------
st.title("🤝 SchemeSetu")
st.caption("AI-powered welfare scheme navigator — find what you qualify for, in plain language.")

tab1, tab2 = st.tabs(["🔍 Find My Schemes", "💬 Ask a Question"])

with tab1:
    st.subheader("Tell us a little about yourself")
    col1, col2 = st.columns(2)
    with col1:
        state = st.text_input("State", placeholder="e.g. Tamil Nadu")
        age = st.number_input("Age", min_value=0, max_value=100, value=25)
        gender = st.selectbox("Gender", ["Female", "Male", "Other / Prefer not to say"])
        category = st.selectbox("Social Category", ["General", "OBC", "SC", "ST", "EWS", "Minority", "Not sure"])
    with col2:
        occupation = st.text_input("Occupation", placeholder="e.g. farmer, student, daily wage worker")
        income = st.selectbox("Annual Family Income", [
            "Below ₹1 lakh", "₹1–2.5 lakh", "₹2.5–5 lakh", "₹5–8 lakh", "Above ₹8 lakh"
        ])
        education = st.selectbox("Education Level", [
            "No formal education", "Below 10th", "10th/12th passed", "Diploma/ITI", "Graduate", "Postgraduate"
        ])
        disability = st.selectbox("Person with Disability?", ["No", "Yes"])

    goal = st.text_area("What are you hoping to get help with?",
                         placeholder="e.g. scholarship for my daughter's college, health insurance, small business loan")

    if st.button("🔎 Find schemes I may qualify for", type="primary"):
        if not state or not goal:
            st.warning("Please fill in at least State and what you're hoping to get help with.")
        else:
            profile = {
                "state": state, "age": age, "gender": gender, "category": category,
                "occupation": occupation, "income": income, "education": education,
                "disability": disability, "goal": goal,
            }
            system_prompt = (
                "You are SchemeSetu, an assistant that helps underserved Indian citizens find "
                "government welfare schemes (central and state-level) they may be eligible for. "
                "Given a citizen's profile, respond in simple, warm, plain language (avoid jargon). "
                "Structure your answer as:\n"
                "1. Top 3-5 schemes they likely qualify for (name + one-line what it gives them)\n"
                "2. For EACH scheme: eligibility check against their profile, and simple step-by-step "
                "application instructions (documents needed, where to apply — online portal or office)\n"
                "3. One encouraging closing line.\n"
                "Be specific and realistic. If unsure of an exact scheme name, describe the closest "
                "real category of scheme and suggest they confirm at their nearest Common Service Centre (CSC)."
            )
            user_prompt = f"Citizen profile:\n{json.dumps(profile, indent=2)}\n\nRecommend schemes and application steps."
            with st.spinner("Matching you to schemes..."):
                answer = ask_ai(system_prompt, user_prompt)
            st.markdown("### 📋 Your Personalized Scheme Guide")
            st.markdown(answer)

with tab2:
    st.subheader("Ask anything about welfare schemes")
    question = st.text_area("Your question", placeholder="e.g. Can an SC-category diploma student get a scholarship in Tamil Nadu?")
    if st.button("Ask SchemeSetu"):
        if not question.strip():
            st.warning("Please type a question.")
        else:
            system_prompt = (
                "You are SchemeSetu, a helpful assistant explaining Indian government welfare "
                "schemes in simple plain language for people who may not be familiar with official "
                "terminology. Be concise, accurate, and practical about how to apply."
            )
            with st.spinner("Thinking..."):
                answer = ask_ai(system_prompt, question)
            st.markdown(answer)

st.divider()
st.caption("Built for the NxtWave Academy Idea2Impact Hackathon · Theme: Sustainability & Social Impact")
