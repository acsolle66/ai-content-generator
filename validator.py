def validate_article(article, keyword):

    results = []

    # POČET SLOV
    word_count = len(article.split())

    if word_count >= 500:
        results.append(f"✅ Dobrý rozsah textu ({word_count} slov >= 500 slov)")
    else:
        results.append(f"❌ Článok je príliš krátky ({word_count} slov < 500 slov)")

    # NADPISY
    h2_count = article.count("##")

    if h2_count >= 3:
        results.append(f"✅ Dobrá štruktúra nadpisov ({h2_count} H2 nadpisy >= 3)")
    else:
        results.append(f"❌ Nedostatok H2 nadpisov ({h2_count} < 3)")

    # KĽÚČOVÉ SLOVO
    keyword_count = article.lower().count(keyword.lower())

    if keyword_count >= 3:
        results.append(
            f"✅ Použitie kľúčového slova je OK ({keyword_count} výskytov >= 3)"
        )
    else:
        results.append(f"⚠ Nízky výskyt kľúčového slova ({keyword_count} výskytov < 3)")

    # FAQ SEKCIA
    if "FAQ" in article.upper():
        results.append("✅ FAQ sekcia prítomná")
    else:
        results.append("⚠ Chýba FAQ sekcia")

    # ZHRNUTIE
    if "zhrnutie" in article.lower() or "summary" in article.lower():
        results.append("✅ Sekcia zhrnutia prítomná")
    else:
        results.append("⚠ Chýba sekcia zhrnutia")

    # ODRAZKY
    if "-" in article or "*" in article:
        results.append("✅ Odrážky detekované")
    else:
        results.append("⚠ Neboli nájdené žiadne odrážky")

    # DĹŽKA ODSEKOV
    paragraphs = article.split("\n\n")

    long_paragraphs = [p for p in paragraphs if len(p.split()) > 120]

    if len(long_paragraphs) == 0:
        results.append("✅ Čitateľnosť odsekov je OK")
    else:
        results.append(f"⚠ Detekované dlhé odseky: {len(long_paragraphs)}")

    return "\n".join(results)
