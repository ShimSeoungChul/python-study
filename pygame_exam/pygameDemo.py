import pygame
import sys

pygame.init()   # pygame 관련 값을 초기화
windowSurface = pygame.display.set_mode((400, 300)) # 너비와 높이가 지정된 윈도우 객체(게임 스크린) 생성
pygame.display.set_caption('파이게임')  # 게임 스크린의 제목을 적어둠
windowSurface.fill(color=(255, 255, 255))   # 게임 스크린의 기본 설정인 검정색 바탕을 흰색으로 변경한다.

# 원 그리그: 좌표 (100, 150)을 중심으로 하는 반지름 30인 원을 그린다.
pygame.draw.circle(surface=windowSurface, color=(255,0,0), center=(100, 150), radius=30)

pygame.display.update() # 설정한 도형을 출력하기 위해 윈도우 화면을 갱신

while True: # while 조건이 참인 동안 게임 루프 처리
    for event in pygame.event.get():    # 게임 도중 발생하는 이벤트를 받는다.
        if event.type == pygame.QUIT:   # 이벤트 중 윈도우의 닫기 버튼을 누른다.
            pygame.quit()   # 게임을 종료
            sys.exit()      # 응용 프로그램을 종료

