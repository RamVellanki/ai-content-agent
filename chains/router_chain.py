from chains.summarizer_chain import short_summary_chain, detailed_summary_chain

def choose_summarizer_chain(article_text):
    """
    Decide which summarizer chain to use based on article length.
    """
    word_count = len(article_text.split())

    if word_count < 500:
        return short_summary_chain()
    else:
        return detailed_summary_chain()