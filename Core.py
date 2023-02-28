import openai
import argparse

YOUR_API_KEY = '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'


def chatGPT(prompt, API_KEY=YOUR_API_KEY):
    
    # set api key
    openai.api_key = API_KEY

    # Call the chat GPT API
    completion = openai.Completion.create(
			  engine = 'text-davinci-003'     # 'text-curie-001'  # 'text-babbage-001' #'text-ada-001'
			, prompt = prompt
			, temperature = 0.5 
			, max_tokens = 1024
			, top_p = 1
			, frequency_penalty = 0
			, presence_penalty = 0)

    return completion['choices'][0]['text']


def main():
    # 지문 입력 란
    prompt = input("Insert a prompt: ")
    print(chatGPT(prompt).strip())


if __name__ == '__main__':
    main()