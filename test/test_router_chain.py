from chains.router_chain import choose_summarizer_chain

short_text = "This is a very short article."
long_text = " ".join(["word"] * 600)  # Simulate long article

short_chain = choose_summarizer_chain(short_text)
long_chain = choose_summarizer_chain(long_text)

print("--------------------------------")
print(short_chain)  # Should be short_summary_chain
print("--------------------------------")
print(long_chain)   # Should be detailed_summary_chain