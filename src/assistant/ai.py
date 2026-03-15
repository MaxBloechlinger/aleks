import requests

API_KEY = "YOUR_API_KEY"

history = [
    {
        "role": "system",
        "content": "You are Aleks, a concise personal voice assistant inspired by Tony Starks Jarvis AI assistant. You address the user as Sire."
    }
]


def ask_llm(text):

    history.append({"role": "user", "content": text})

    response = requests.post(
        "https://api.openai.com/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        },
        json={
            "model": "gpt-4o-mini",
            "messages": history[-6:]  # short memory window
        }
    )

    reply = response.json()["choices"][0]["message"]["content"]

    history.append({"role": "assistant", "content": reply})

    return reply
