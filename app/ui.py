# app/ui.py

import streamlit as st
import requests

# -----------------------------
# CONFIG
# -----------------------------
API_URL = "http://localhost:8000/ask"

st.set_page_config(
    page_title="Medical Multi-RAG Assistant",
    page_icon="🏥",
    layout="wide"
)

# -----------------------------
# SIDEBAR
# -----------------------------
st.sidebar.title("🏥 Hospital Assistant")
st.sidebar.markdown("### Departments")
st.sidebar.markdown("""
- 🫀 Cardiology  
- 🧠 Neurology  
- 🦴 Orthopedics  
- 🚑 Emergency  
""")

st.sidebar.markdown("---")
st.sidebar.info("AI-powered Multi-RAG system")

# -----------------------------
# HEADER
# -----------------------------
st.markdown(
    """
    <h1 style='text-align: center; color: #2E86C1;'>
    🏥 Medical Multi-RAG Assistant
    </h1>
    <p style='text-align: center;'>
    Find hospitals, policies, and real-time medical insights
    </p>
    """,
    unsafe_allow_html=True
)

# -----------------------------
# INPUT
# -----------------------------
st.markdown("### 🔍 Ask Your Question")

query = st.text_input(
    "Search Query",
    placeholder="Example: Best hospital near Bangalore or ICU policy",
    label_visibility="collapsed"
)

search_btn = st.button("🔎 Search")

# -----------------------------
# RESULTS
# -----------------------------
if search_btn:
    if not query.strip():
        st.warning("⚠️ Please enter a query")
    else:
        try:
            with st.spinner("Fetching results... 🤖"):
                response = requests.post(API_URL, json={"query": query})

            if response.status_code == 200:
                result = response.json()

                # 🚨 Handle backend error
                if "error" in result:
                    st.error(f"❌ {result['error']}")
                else:
                    route = result.get("route", "N/A")
                    answer = result.get("answer", "No answer returned")

                    st.markdown("---")

                    # Layout
                    col1, col2 = st.columns(2)

                    with col1:
                        st.markdown("### 🧭 Route Used")
                        st.success(route)

                    with col2:
                        st.markdown("### 📌 Your Query")
                        st.info(query)

                    # ✅ ONLY ANSWER (Context removed)
                    st.markdown("### 🤖 AI Response")
                    st.markdown(
                        f"""
                        <div style="
                            background-color:#F4F6F7;
                            padding:20px;
                            border-radius:10px;
                            border-left:6px solid #2E86C1;
                        ">
                        {answer}
                        </div>
                        """,
                        unsafe_allow_html=True
                    )

            else:
                st.error(f"❌ API Error: {response.status_code}")

        except requests.exceptions.ConnectionError:
            st.error("🚫 Cannot connect to backend. Make sure FastAPI is running.")

        except Exception as e:
            st.error(f"⚠️ Unexpected error: {e}")

# -----------------------------
# SAMPLE QUERIES
# -----------------------------
st.markdown("---")
st.markdown("### 💡 Try Sample Queries")

samples = [
    "Best hospital near Bangalore",
    "ICU rules in hospital",
    "Cardiology hospital in Chennai",
    "Emergency admission policy"
]

cols = st.columns(2)

for i, sample in enumerate(samples):
    if cols[i % 2].button(sample):
        st.session_state["query"] = sample
        st.rerun()

# -----------------------------
# FOOTER
# -----------------------------
st.markdown("---")
st.markdown(
    "<center>🚀 Built with Multi-RAG | FastAPI | FAISS | OpenAI</center>",
    unsafe_allow_html=True
)