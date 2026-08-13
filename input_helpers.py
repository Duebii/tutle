"""사용자 입력을 안전하게 받기 위한 보조 함수."""

from data import CATEGORIES


def get_required_input(field_name):
    """비어 있지 않은 입력값을 받을 때까지 반복한다."""
    while True:
        value = input(f"{field_name}: ").strip()
        if value:
            return value
        print(f"{field_name}은(는) 비워 둘 수 없습니다. 다시 입력해 주세요.")


def select_category():
    """카테고리 목록에서 선택하거나 새 카테고리를 직접 입력받는다."""
    print("\n카테고리 선택:")
    for index, category in enumerate(CATEGORIES, start=1):
        print(f"{index}. {category}")

    while True:
        choice = input("번호 또는 새 카테고리 입력: ").strip()
        if choice.isdigit() and 1 <= int(choice) <= len(CATEGORIES):
            return CATEGORIES[int(choice) - 1]
        if choice:
            return choice

        print("카테고리는 비워 둘 수 없습니다. 다시 입력해 주세요.")
