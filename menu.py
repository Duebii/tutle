"""메뉴 출력과 메뉴 선택 처리를 담당한다."""

from prompt_manager import add_prompt

MENU_NAMES = {
    "1": "프롬프트 추가",
    "2": "프롬프트 목록",
    "3": "카테고리별 조회",
    "4": "프롬프트 검색",
    "5": "프롬프트 상세 보기",
    "6": "즐겨찾기 관리",
    "7": "즐겨찾기 목록",
}


def show_menu():
    """프로그램에서 선택할 수 있는 메뉴를 출력한다."""
    print("\n=== 나만의 프롬프트 관리 ===")
    for number, name in MENU_NAMES.items():
        print(f"{number}. {name}")
    print("0. 종료")


def handle_menu_choice(choice):
    """선택한 메뉴의 기능을 실행하거나 안내를 출력한다."""
    if choice == "1":
        add_prompt()
        return

    if choice not in MENU_NAMES:
        print("잘못된 메뉴 번호입니다. 다시 선택해 주세요.")
        return

    print(f"'{MENU_NAMES[choice]}' 기능은 준비 중입니다.")
