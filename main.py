"""나만의 프롬프트 관리 프로그램의 실행 흐름."""

from menu import handle_menu_choice, show_menu


def main():
    """메뉴를 반복 출력하고 사용자 선택을 처리한다."""
    print("나만의 프롬프트 관리 프로그램을 시작합니다.")

    while True:
        show_menu()
        choice = input("선택: ").strip()

        if choice == "0":
            print("프로그램을 종료합니다.")
            break

        handle_menu_choice(choice)


if __name__ == "__main__":
    main()
