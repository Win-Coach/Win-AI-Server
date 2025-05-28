def analyze_text(text: str) -> str:
    # 테스트용 분석: 단순 단어 수 세기
    word_count = len(text.split())
    return f"입력된 문장은 {word_count}개의 단어로 구성되어 있습니다."