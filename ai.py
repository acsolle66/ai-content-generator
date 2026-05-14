import streamlit as st
from openai import OpenAI

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])


def generate_article(topic):

    prompt = f"""
    Vytvor SEO a GEO optimalizovaný článok na tému: {topic}

    Požiadavky:
    - Použi markdown formátovanie
    - Použi jasnú hierarchiu nadpisov
    - Použi 1 hlavný H1 nadpis
    - Použi minimálne 3 H2 sekcie
    - Článok musí byť praktický, informatívny a dobre čitateľný
    - Zahrň FAQ sekciu
    - Ak je to vhodné, použi odrážky
    - Na konci pridaj krátke zhrnutie
    - Optimalizuj text pre AI čitateľnosť a GEO
    - Použi relevantné pojmy a súvisiace entity
    - Vyhni sa zbytočnej vate
    - Použi kratšie a prehľadné odseky
    - Dĺžka článku približne 500 až 700 slov
    """

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {
                "role": "system",
                "content": (
                    "Si AI content špecialista zameraný na tvorbu SEO a GEO "
                    "optimalizovaného obsahu. "
                    "Tvojou úlohou je vytvárať kvalitné články s jasnou "
                    "štruktúrou, vysokou informačnou hodnotou a dobrou "
                    "čitateľnosťou pre používateľov aj AI systémy. "
                    "Používaj stručné odseky, relevantné nadpisy, FAQ sekcie "
                    "a praktické informácie bez zbytočnej vaty."
                ),
            },
            {"role": "user", "content": prompt},
        ],
        temperature=0.7,
    )

    return response.choices[0].message.content
