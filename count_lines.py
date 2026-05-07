# my_timer 모듈에서 my_timer decorator import
from my_timer import my_timer

# read_lines 모듈에서 read_lines generator import
from read_lines import read_lines


# 아래 함수에 @my_timer decorator 적용
@my_timer
# count_lines 함수 정의: 인자 path는 str 타입, 반환은 int 타입
def count_lines(path: str) -> int:
    # 카운터 변수 0으로 초기화
    count = 0

    # read_lines(path)가 yield하는 각 줄을 line으로 받아 for loop
    for line in read_lines(path):

        # 카운터 1 증가
        count = count + 1

    # 카운터 값 반환
    return count



# 직접 실행 진입점 (if __name__ == "__main__":)
if __name__ == "__main__":
    # count_lines를 "read_lines.py"를 인자로 호출, 결과를 변수에 저장
    linecount = count_lines("read_lines.py")
    # f-string으로 "Total lines: <값>" 형태로 출력
    print(f"Total lines: {linecount}")
