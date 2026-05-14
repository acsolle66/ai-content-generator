import streamlit as st

from ai import generate_article
from seo import generate_seo_report
from validator import validate_article

# PAGE CONFIG
st.set_page_config(page_title="AI Content Generator", page_icon="🧠", layout="wide")

if "auth" not in st.session_state:
    st.session_state.auth = False

# LOGIN SCREEN
if not st.session_state.auth:
    st.title("Login")

    password = st.text_input("Zadaj heslo pre prístup k aplikácii", type="password")

    if password:
        if password == st.secrets["APP_PASSWORD"]:
            st.session_state.auth = True
            st.rerun()
        else:
            st.error("Nesprávne heslo")

    st.stop()

# HEADER
st.title("🧠 AI Content Generator")
st.write(
    "Generovanie článkov pomocou AI s SEO optimalizáciou a automatickou validáciou štruktúry a kvality generovaného výstupu."
)

# INPUT
topic = st.text_input("Zadaj tému článku:")

# BUTTON
if st.button("Generovať článok"):

    if topic is None or topic.strip() == "":
        st.warning("Prosím zadaj tému článku.")
    else:

        with st.spinner("Generujem článok..."):
            article = generate_article(topic)

        # LAYOUT
        col1, col2 = st.columns([2, 1])

        # ARTICLE OUTPUT
        with col1:
            st.subheader("📄 Vygenerovaný článok")

            container = st.container(border=True)
            container.markdown(article)

        # RIGHT PANEL (METRICS)
        with col2:

            st.subheader("📊 SEO / VALIDÁCIA")

            validation = validate_article(article, topic)
            st.code(validation)

            seo_report = generate_seo_report(article, topic)

            with st.expander("📈 SEO report", expanded=True):
                st.code(seo_report)

        # EXTRA SECTION
        with st.expander("🔎 Raw výstup (debug)", expanded=False):
            st.code(article, language="markdown")
