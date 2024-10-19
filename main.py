import openai
from config import OPENAI_API_KEY
from reddit_data import fetch_reddit_posts

openai.api_key = OPENAI_API_KEY

def generate_prompt_from_post(post_title):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"Generate a creative NFT art idea based on the following topic: {post_title}.",
        max_tokens=100
    )
    return response.choices[0].text.strip()

if __name__ == "__main__":
    # Fetch Reddit posts
    posts = fetch_reddit_posts("cryptocurrency", limit=3)

    # Generate NFT prompts from the posts
    for post in posts:
        prompt = generate_prompt_from_post(post)
        print(f"Reddit Post: {post}")
        print(f"Generated NFT Art Prompt: {prompt}")
        print("-" * 50)