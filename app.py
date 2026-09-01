"""
AI Content Repurposing Tool
----------------------------
Paste in a blog post, article, or transcript and generate a Twitter/X thread,
LinkedIn post, Instagram caption, and email newsletter blurb using an LLM.

SETUP:
1. pip install streamlit anthropic python-dotenv
2. Create a file named ".env" in the same folder with:
       ANTHROPIC_API_KEY=your-key-here
3. Run:  streamlit run app.py
"""

import os
import streamlit as st
import anthropic
from dotenv import load_dotenv

load_dotenv()

# ---------- Config ----------
MODEL = "claude-sonnet-4-6"  # swap for any Claude model you have access to

FORMAT_PROMPTS = {
    "Twitter/X Thread": (
        "Turn the following content into an engaging Twitter/X thread of 5-8 tweets. "
        "Number each tweet (1/, 2/, etc.), keep each tweet under 280 characters, "
        "start with a strong hook, and end with a clear takeaway or call to action."
    ),
    "LinkedIn Post": (
        "Turn the following content into a LinkedIn post. Use short paragraphs, "
        "a compelling first line (hook), a few line breaks for readability, "
        "and end with a question or call to action to drive engagement. "
        "Keep it under 200 words."
    ),
    "Instagram Caption": (
        "Turn the following content into an Instagram caption. Keep it punchy and "
        "conversational, under 150 words, and end with 5-8 relevant hashtags."
    ),
    "Email Newsletter Blurb": (
        "Turn the following content into a short email newsletter blurb (under 120 words) "
        "with a catchy subject line on the first line, followed by the blurb body. "
        "Make it inviting and easy to skim."
    ),
}

TONE_OPTIONS = ["Professional", "Casual", "Witty", "Inspirational"]

CHAR_LIMITS = {
    "Twitter/X Thread": 280,
    "Instagram Caption": 2200,
}


# ---------- Helpers ----------
def get_client():
    api_key = os.getenv("ANTHROPIC_API_KEY")
    if not api_key:
        st.error("No API key found. Add ANTHROPIC_API_KEY to a .env file in this folder.")
        st.stop()
    return anthropic.Anthropic(api_key=api_key)


def generate_content(client, source_text, format_name, tone):
    system_prompt = (
        f"You are an expert social media and content marketing copywriter. "
        f"Write in a {tone.lower()} tone. Do not add explanations, notes, or preambles — "
        f"output ONLY the final content requested."
    )
    user_prompt = f"{FORMAT_PROMPTS[format_name]}\n\nCONTENT:\n{source_text}"

    response = client.messages.create(
        model=MODEL,
        max_tokens=600,
        system=system_prompt,
        messages=[{"role": "user", "content": user_prompt}],
    )
    return response.content[0].text.strip()


# ---------- UI ----------
st.set_page_config(page_title="AI Content Repurposer", page_icon="🪄", layout="centered")

st.title("🪄 AI Content Repurposing Tool")
st.write(
    "Paste in a blog post, article, or transcript below, choose the formats you want, "
    "and generate ready-to-post content in seconds."
)

source_text = st.text_area(
    "Paste your source content here",
    height=250,
    placeholder="Paste your blog post, article, or transcript...",
)

col1, col2 = st.columns(2)
with col1:
    selected_formats = st.multiselect(
        "Formats to generate",
        options=list(FORMAT_PROMPTS.keys()),
        default=["Twitter/X Thread", "LinkedIn Post"],
    )
with col2:
    tone = st.selectbox("Tone", TONE_OPTIONS)

generate_clicked = st.button("Generate", type="primary", use_container_width=True)

if generate_clicked:
    if not source_text.strip():
        st.warning("Please paste some source content first.")
    elif not selected_formats:
        st.warning("Please select at least one format to generate.")
    else:
        client = get_client()
        with st.spinner("Generating your content..."):
            for fmt in selected_formats:
                try:
                    output = generate_content(client, source_text, fmt, tone)
                except Exception as e:
                    st.error(f"Error generating {fmt}: {e}")
                    continue

                with st.expander(f"📄 {fmt}", expanded=True):
                    st.text_area(
                        label=f"{fmt} output",
                        value=output,
                        height=200,
                        key=f"output_{fmt}",
                        label_visibility="collapsed",
                    )

                    limit = CHAR_LIMITS.get(fmt)
                    if limit:
                        longest_part = max(output.split("\n"), key=len, default="")
                        if len(longest_part) > limit:
                            st.caption(
                                f"⚠️ Longest line is {len(longest_part)} characters "
                                f"(limit ~{limit})."
                            )
                        else:
                            st.caption(f"✅ Within the ~{limit} character guideline.")

        st.success("Done! Copy any section above using the copy icon in the top-right of each box.")

st.divider()
st.caption(
    "Built with Streamlit + Claude (Anthropic API). Swap MODEL at the top of app.py to use a different model."
)
