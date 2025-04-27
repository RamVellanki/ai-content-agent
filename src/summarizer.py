import ollama

def summarize_text(text):
    try:
        response = ollama.chat(
            model='mistral:instruct',
            messages=[
                {"role": "system", "content": "You are a helpful assistant that summarizes articles."},
                {"role": "user", "content": f"Summarize the following article in 5 concise bullet points in Markdown format:\n\n{text}"}
            ]
        )
        return response['message']['content']
    except Exception as e:
        print(f"Summarization failed: {e}")
        return ""