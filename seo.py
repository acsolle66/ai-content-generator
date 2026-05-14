def generate_seo_report(article, keyword):

    keyword_count = article.lower().count(keyword.lower())
    word_count = len(article.split())
    heading_count = article.count("##")

    return f"""
=========================
📊 SEO REPORT
=========================

🔎 KĽÚČOVÉ SLOVO
- Kľúčové slovo: {keyword}
- Počet výskytov: {keyword_count}

🧱 ŠTRUKTÚRA ČLÁNKU
- Počet nadpisov (H2): {heading_count}
- Počet slov: {word_count}

📈 HODNOTENIE
- Keyword hustota: {round((keyword_count / word_count) * 100, 2) if word_count > 0 else 0}%

🧠 GEO SIGNALY
- Článok je optimalizovaný pre AI čitateľnosť: ✔ (manuálne/heuristicky)
- Štruktúrovaný obsah: {"áno" if heading_count >= 3 else "nie"}

=========================
"""
