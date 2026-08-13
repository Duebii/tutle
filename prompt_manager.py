"""프롬프트 추가와 이후 프롬프트 관리 기능을 담당한다."""

from data import prompts
from input_helpers import get_required_input, select_category


def add_prompt():
    """입력받은 프롬프트를 목록에 추가하고 기본값은 즐겨찾기 해제로 설정한다."""
    print("\n=== 프롬프트 추가 ===")
    title = get_required_input("제목")
    content = get_required_input("내용")
    category = select_category()

    new_prompt = {
        "title": title,
        "content": content,
        "category": category,
        "favorite": False,
    }
    prompts.append(new_prompt)

    print(f"'{title}' 프롬프트가 추가되었습니다.")
    return new_prompt
