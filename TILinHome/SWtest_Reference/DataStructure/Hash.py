'''
Hash table은 키를 값에 매핑할 수 있는 구조인, 연관 배열 추가에 사용되는 자료 구조이다.
Hash table은 Hash 함수를 사용하여 색인(index, Key)을 버킷(bucket)이나 슬롯(slot)의 배열로 계산한다.
주어진 N개의 key, data쌍을 Hash table에 입력한 후, Q개의 key를 입력 받아 key에 해당하는 data를 각 줄에 출력하시오.
(1<=N, Q<=4096) * Key : 최대 64개의 문자열 * Data : 최대 128개의 문자열
'''

hash = {}


def find(key):
    return hash.get(key)


def add(key, value):
    hash.update({key: value})


def main():
    T = int(input())

    for test_case in range(1, T + 1):
        N = int(input())

        for i in range(N):
            key, value = map(str, input().split())
            add(key, value)

        print("#%d" % test_case)

        Q = int(input())

        for i in range(Q):
            key = input()
            key = key.strip(" ")
            value = find(key)
            if value:
                print(value)
            else:
                print("not find")


if __name__ == "__main__":
    main()

'''
2 // 테스트 케이스 수 T 
8 // 입력 데이터 수 N  
Attract Charm //key data 
Gather Collect 
Fundamental Essential 
Abundant Plentiful 
Achieve Accomplish 
Assign Allocate 
Surprise Amaze 
Assess Estimate 
3 // 검색할 데이터 수 Q 
Attract 
Surprise 
education 
10 
Bear Stand 
Famous Noted 
Characteristic Attribute 
Decrease Diminish 
Defect Flaw 
Depict Describe 
Eager Avid 
Flourish Thrive 
Huge Tremendous 
Important Crucial 
5 
treasure 
Bear 
Defect 
Huge 
hydrogen
'''

'''
#1 
Charm 
Amaze 
not find 
#2 
not find 
Stand 
Flaw 
Tremendous 
not find
'''