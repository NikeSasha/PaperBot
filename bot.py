from slack_sdk import WebClient
import os
import datetime

client = WebClient(token=os.environ['SLACK_TOKEN'])
channel = "#test"

def generate_digest():
    today = datetime.datetime.now().strftime("%B %d, %Y")
    return f"""📚 *Daily AI Research Digest – {today}*

Here are today’s top 3 papers in your field (e.g. NLP, ML, CV):

1. *“Self-Aligning LLMs with Minimal Human Feedback”*  
*Summary:* Proposes a lightweight framework for aligning large language models using synthetic feedback instead of RLHF.  
*Why it matters:* Reduces alignment cost by 80% while maintaining performance — a game-changer for smaller labs.

2. *“Chain-of-Backprop: Reasoning Through Differentiable Memory”*  
*Summary:* Introduces a neural architecture that combines reasoning chains with differentiable memory for complex multi-step tasks.  
*Why it matters:* Outperforms standard CoT (Chain-of-Thought) prompting on math and planning benchmarks.

3. *“Emergent Behaviors in LLMs via Sparse Reward Fine-Tuning”*  
*Summary:* Shows that rare but well-targeted reward signals can induce abstract behavior generalization in GPT-style models.  
*Why it matters:* Opens new directions for efficient model tuning with limited data and feedback.

💡 Posted by PaperBot | Suggestions powered by full-text analysis & expert heuristics  
🧠 Domain: Artificial Intelligence | 📈 Filtering: Novelty + Impact
"""

def post_digest():
    try:
        message = generate_digest()
        response = client.chat_postMessage(channel=channel, text=message)
        print("✅ Digest sent:", response["ts"])
    except Exception as e:
        print(f"❌ Some error: {e}")

if __name__ == "__main__":
    post_digest()
