"""나만의 프롬프트 관리 프로그램 실행 파일."""

CATEGORIES = [
    "텍스트 생성",
    "이미지 생성",
    "영상 생성",
    "페르소나",
    "자동화",
    "기타",
]

REQUIRED_PROMPT_FIELDS = {"title", "content", "category", "favorite"}

prompts = [
    {
        "title": "블로그 글 작성 도우미",
        "content": "주어진 주제에 대해 SEO를 고려한 블로그 글을 작성해 주세요.",
        "category": "텍스트 생성",
        "favorite": True,
    },
    {
        "title": "제품 소개 이미지 생성",
        "content": "제품의 특징이 잘 드러나는 광고용 이미지를 생성해 주세요.",
        "category": "이미지 생성",
        "favorite": False,
    },
    {
        "title": "IT 콘텐츠 페르소나",
        "content": "초보자도 이해하기 쉽게 설명하는 IT 콘텐츠 전문가 역할을 해 주세요.",
        "category": "페르소나",
        "favorite": False,
    },
]


def is_valid_prompt(prompt):
    """프롬프트가 필수 정보와 올바른 자료형을 갖췄는지 확인한다."""
    return (
        isinstance(prompt, dict)
        and set(prompt) == REQUIRED_PROMPT_FIELDS
        and isinstance(prompt["title"], str)
        and isinstance(prompt["content"], str)
        and isinstance(prompt["category"], str)
        and isinstance(prompt["favorite"], bool)
    )


def is_valid_prompt_list(prompt_list):
    """프롬프트 전체 데이터가 딕셔너리 목록으로 구성됐는지 확인한다."""
    return isinstance(prompt_list, list) and all(
        is_valid_prompt(prompt) for prompt in prompt_list
    )


def main():
    """프로그램 시작 메시지를 출력한다."""
    print("나만의 프롬프트 관리 프로그램을 시작합니다.")


if __name__ == "__main__":
    main()
