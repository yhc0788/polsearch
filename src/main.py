import os
import requests
import openai

LAW_API_KEY = os.getenv('LAW_API_KEY')
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')


def search_judgment(query: str):
    """Search judgments using the Law.go.kr API."""
    if not LAW_API_KEY:
        raise RuntimeError('LAW_API_KEY environment variable not set')

    url = 'https://www.law.go.kr/DRF/lawSearch.do'
    params = {
        'OC': LAW_API_KEY,
        'target': 'prec',  # precedent search
        'query': query,
        'type': 'JSON',
    }
    response = requests.get(url, params=params, timeout=10)
    response.raise_for_status()
    return response.json()


def call_llm(judgments, query: str) -> str:
    """Call the OpenAI API to analyze judgments."""
    if not OPENAI_API_KEY:
        raise RuntimeError('OPENAI_API_KEY environment variable not set')

    openai.api_key = OPENAI_API_KEY
    prompt = f"""다음 신고 내용에 대해 판결문을 참고하여 적용 가능한 법조항을 알려주세요.\n신고 내용: {query}\n판결문 정보: {judgments}\n"""
    completion = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=[
            {'role': 'system', 'content': '당신은 한국 법 전문가입니다.'},
            {'role': 'user', 'content': prompt},
        ],
    )
    return completion.choices[0].message['content'].strip()


def main() -> None:
    query = input('신고 내용을 입력하세요: ')
    judgments = search_judgment(query)
    result = call_llm(judgments, query)
    print('\n=== 적용 가능한 법조항 ===')
    print(result)


if __name__ == '__main__':
    main()
