def score():
    print("이것은 2022년 9월 고1 모의고사-과학 채점 프로그램입니다. 답을 입력하면 맞을 경우 '정답입니다'가 틀렸을 경우에는 정답과 해설이 같이 출력됩니다. 마지막에는 총점이 출력됩니다.")
    print("혹시나 문제 해설에 오타가 있을 경우에는 'jdh04133@naver.com'으로 연락 부탁드립니다.")
    one = input("Please enter the correct answer to question 1: ")
    one = int(one)
    if one == 5:
        one_score = 2
        print("정답입니다!")
    else:
        one_score = 0
        print("1번: 5")
        print("사람이 에어 매트에 충돌할 떄 에어 매트는 충격을 받는 시간을 길게 하여 사람이 받는 평균 힘의 크기를 줄여 준다. 태권도 보호대와 헬멧, 모서리 쿠션은 충돌 시 충격을 받는 시간을 길게 함으로써 사람에게 가해지는 평균 힘의 크기를 감소시켜 피해를 줄인다.")
    two = input("Please enter the correct answer to question 2: ")
    two = int(two)
    if two == 2:
        two_score = 2
        print("정답입니다!")
    else:
        two_score = 0
        print("2번: 2")
        print("나트륨과 물이 반응하면 수소 기체가 발생하고 그 수용액은 염기성이다. 수소 기체는 가연성 기체로, 성냥불을 대었을 때 '펑' 소리가 나는 실험을 통해 확인할 수 있고, 염기성 용액은 페놀프탈레인 용액을 떨어뜨렸을 떄 붉게 변하는 실험으로 확인할 수 있다.")
    three = input("Please enter the correct answer to question 3: ")
    three = int(three)
    if three == 3:
        three_score = 2
        print("정답입니다!")
    else:
        three_score = 0
        print("3번: 3")
        print("A는 소포체, B는 핵, C는 리보솜이다. 핵(B)에는 유전 물질인 DNA가 있다. 리보솜(C)은 단백질을 합성하고, 식물 세포의 엽록체에서 광합성이 일어난다.")
    four = input("Please enter the correct answer to question 4: ")
    four = int(four)
    if four == 1:
        four_score = 2
        print("정답입니다!")
    else:
        four_score = 0
        print("4번: 1")
        print("혼합층의 형성은 기권과 수권(A), 화산 가스의 분출은 기권과 지권(B), 식물의 증산 작용은 기권과 생물권(C)의 상호 작용이다.")
    five = input("Please enter the correct answer to question 5: ")
    five = int(five)
    if five == 1:
        five_score = 3
        print("정답입니다!")
    else:
        five_score = 0
        print("5번: 1")
        print("㈎는 전사, ㈏는 번역이다. ㉠은 타이민(T), ㉡은 아데닌(A), ㉢은 유라실(U)이다. 번역은 세포질의 리보솜에서 일어난다.")
    six = input("Please enter the correct answer to question 6: ")
    six = int(six)
    if six == 4:
        six_score = 2
        print("정답입니다!")
    else:
        six_score = 0
        print("6번: 4")
        print("초전도체는 임계 온도(Tc)보다 낮은 온도에서 전기 저항이 0이 되고, A가 떠 있기 위해서는 A에 작용하는 중력을 상쇄시키는 방향으로 자기력이 작용하여야 한다.")
    seven = input("Please enter the correct answer to question 7: ")
    seven = int(seven)
    if seven == 5:
        seven_score = 2
        print("정답입니다!")
    else:
        seven_score = 0
        print("7번: 5")
        print("㉠은 핵산, ㉡은 단백질이다. 단백질(㉡)은 효소의 주성분이며, 핵산(㉠)과 단백질(㉡)은 탄소 화합물에 해당한다.")
    eight = input("Please enter the correct answer to question 8: ")
    eight = int(eight)
    if eight == 3:
        eight_score = 3
        print("정답입니다!")
    else:
        eight_score = 0
        print("8번: 3")
        print("사과와 인공위성에 작용하는 힘은 모두 중력이다. 인공위성에 작용하는 중력의 방향과 운동 방향은 수직이다. 자유 낙하하는 물체는 질량과 관계없이 모두 중력 가속도로 낙하하므로 시간에 따라 일정하게 속력이 증가한다.")
    nine = input("Please enter the correcta answer to question 9: ")
    nine = int(nine)
    if nine == 2:
        nine_score = 3
        print("정답입니다!")
    else:
        nine_score = 0
        print("9번: 2")
        print("㉠은 막단백질을 통해, ㉡은 인지질 이중층을 통해 확산한다. 확산은 고농도에서 저농도로 물질이 이동하는 것이므로 ㉠의 농도는 세포 외부에서가 세포 내부에서보다 높다. 포도당은 ㉠과 같은 방식으로 이동한다. 세포막을 통한 물질의 이동은 물질의 종류에 따라 선택적으로 일어나는데, 이를 선택적 투과성이라고 한다.")
    ten = input("Please enter the correct answer to question 10: ")
    ten = int(ten)
    if ten == 5:
        ten_score = 3
        print("정답입니다!")
    else:
        ten_score = 0
        print("10번: 5")
        print("㉠은 성분 원소가 3가지이며 수용액이 전기 전도성이 있는 이온 결합 물질이므로 질산 나트륨(NaNO3)이고, 고체 상태에서는 이온이 이동할 수 없으므로 전기 전도성이 없다. ㉡은 성분 원소가 3가지이며 수용액이 전기 전도성이 없으므로 공유 결합 물질인 설탕(C12H22O11)이고, 성분 원소인 C, H, O는 모두 비금속 원소이다. ㉢은 성분 원소가 2가지인 염화 나트륨(NaCl)으로, Na+과 Cl- 사이의 이온 결합 물질이다.")
    eleven = input("Please enter the correct answer to question 11: ")
    eleven = int(eleven)
    if eleven == 3:
        eleven_score = 2
        print("정답입니다!")
    else:
        eleven_score =0
        print("11번: 3")
        print("카탈레이스는 과산화 수소 분해 반응의 활성화 에너지를 낮춰 화학 반응 속도를 증가시키는 생체 촉매이다. 과산화 수소의 분해 결과로 물(㉠)과 산소가 생성된다.")
    twelve = input("Please enter the correct answer to question 12: ")
    twelve = int(twelve)
    if twelve == 4:
        twelve_score = 3
        print("정답입니다!")
    else:
        twelve_score =0
        print("12번: 4")
        print("고온의 원소는 특정 파장의 빛을 방출한다. 별 S의 흡수 스펙트럼에는 B의 흡수선이 나타나지 않으므로 별 S의 대기에는 B가 존재하지 않는다. 원소의 종류에 따라 고유한 스펙트럼을 나타내므로 별빛의 스펙트럼을 분석하면 별을 구성하는 원소를 확인할 수 있다.")
    thirteen = input("Please enter the correct answer to question 13: ")
    thirteen = int(thirteen)
    if thirteen == 5:
        thirteen_score = 2
        print("정답입니다!")
    else:
        thirteen_score = 0
        print("13번: 5")
        print("맨틀 대류를 일으키는 지구 내부 에너지의 급격한 방출에 의해 지진과 화산 활동이 발생한다. 화산재가 대량으로 성층권에 유입될 경우 지표에 도달하는 태양 복사 에너지양이 일시적으로 감소하여 기온이 떨어질 수 있다. 화산 가스에 포함된 이산화 황은 대기 중의 황산염 농도를 증가시키고 산성비의 원인이 된다.")
    fourteen = input("Please enter the correct answer to question 14: ")
    fourteen = int(fourteen)
    if fourteen == 4:
        fourteen_score = 3
        print("정답입니다!")
    else:
        fourteen_score =0
        print("14번: 4")
        print("A지역은 동아프리카 열곡대로 V자 모양의 골짜기가 형성되어 있다. B지역은 히말라야 산맥으로 인도판과 유라시아판이 충돌하여 형성된 습곡 산맥이다. C지역은 산안드레아스 단층으로 북아메리카판과 태평양판이 서로 어긋나게 이동하며 형성된 보존형 경계이다.")
    fifteen = input("Please enter the correct answer to question 15: ")
    fifteen = int(fifteen)
    if fifteen == 3:
        fifteen_score = 2
        print("정답입니다!")
    else:
        fifteen_score = 0
        print("15번: 3")
        print("태양 에너지는 대기와 물을 순환시켜 기상 현상을 일으키고 지구 시스템의 에너지원 중 가장 많은 양을 차지한다. 달과 태양의 인력이 지구에 작용하여 생기는 조력 에너지는 밀물과 썰물을 일으켜 해수면의 높이를 변화시킨다.")
    sixteen = input("Please enter the correct answer to question 16: ")
    sixteen = int(sixteen)
    if sixteen == 2:
        sixteen_score = 3
        print("정답입니다!")
    else:
        sixteen_score = 0
        print("16번: 2")
        print("제시된 규칙에 따라 만들 수 있는 스타이로폼 공(O) 3개로 이루어진 사슬 모양의 탄소 골격 4가지의 구조(필요한 이쑤시개 수)는 다음과 같다.")
        print("https://pbs.twimg.com/media/Fb9RkBraIAAecpZ?format=jpg&name=large")
        print("4가지 구조를 만들 때 필요한 이쑤시개의 총 개수는 10+9+8+8=35이다.")
    seventeen = input("Please enter the correct answer to question 17: ")
    seventeen = int(seventeen)
    if seventeen == 5:
        seventeen_score = 3
        print("정답입니다!")
    else:
        seventeen_score = 0
        print("17번: 5")
        print("힘-시간 그래프에서 곡선 아래의 면적(S)은 A가 쿠션으로부터 받은 충격량(I)의 크기이다. 그러므로 │I│=S이다. A가 쿠션으로부터 받은 충격량(I)은 A의 운동량 변화량(p0→0)과 같으므로 충돌 직전의 운동량│p0│=│I│=S이다. 용수철에 의한 A의 운동량의 변화량(0→p0)은 충격량과 같으므로, A가 용수철로부터 받은 충격량의 크기는 S이다.")
    eighteen = input("Please enter the correct answer to question 18: ")
    eighteen = int(eighteen)
    if eighteen == 2:
        eighteen_score = 3
        print("정답입니다!")
    else:
        eighteen_score = 0
        print("18번: 2")
        print("A와 B는 금속 원소이므로 주기율표에서 왼쪽에 위치하며, B와 C는 전자 껍질 수가 같으므로 같은 주기(가로줄)에 위치하고, C와 D는 원자가 전자 수가 같으므로 같은 족(세로줄)에 위치한다. 화합물 BD2에서 각 이온의 전자 배치가 네온(Ne)의 전자 배치와 같고, 양이온과 음이온의 전하 비가 +2:-1이므로 B는 3주기 2족, D는 2주기 17족이 가능하다.")
    nineteen = input("Please enter the correct answer to question 19: ")
    nineteen = int(nineteen)
    if nineteen == 4:
        nineteen_score = 2
        print("정답입니다!")
    else:
        nineteen_score = 0
        print("19번: 4")
        print("분자 Xy3을 구성하는 우너자 Y는 전자 수=양성자 수=원자가 전자 수=1인 수소이다. 원자 X는 원자가 전자 수가 5이므로 3개의 전자를 얻어 안정한 전자 배치를 가지려는 성질이 있으며, X2 분자에서 X 원자 사이에는 공유 결합을 형성한다. XY3 분자 1개에는 공유 전자쌍 3개와 비공유 전자쌍 1개가 존재한다.")
    twenty = input("Please enter the correct answer to question 20: ")
    twenty = int(twenty)
    if twenty == 3:
        twenty_score = 3
        print("정답입니다!")
    else:
        twenty_score = 0
        print("20번: 3")
        print("A와 B에 작용하는 중력의 방향은 연직 아래로 같다. 동일한 속력으로 발사된 B가 수평 방향으로 등속도 운동을 하므로 수평 도달 거리는 낙하 시간에 비례한다. ㈐에서보다 ㈑에서가 낙하 시간이 크므로 수평 도덜 거리 ㉠은 1.2m보다 크다. 자유 낙하하는 A의 속력은 시간에 비례하므로 ㈑에서가 ㈐에서보다 크다")
    total = one_score + two_score + three_score + four_score + five_score + six_score + seven_score + eight_score + nine_score + ten_score + eleven_score + twelve_score + thirteen_score + fourteen_score + fifteen_score + sixteen_score + seventeen_score + eighteen_score + nineteen_score + twenty_score
    print("총점은 " + str(total) + "점 입니다.")
    total = int(total)
    if total <= 50 and total >= 40:
        print("등급은 1등급입니다.")
    elif total <= 39 and total >=35:
        print("등급은 2등급입니다.")
    elif total <= 34 and total >= 30:
        print("등급은 3등급입니다.")
    elif total <= 29 and total >= 25:
        print("등급은 4등급입니다.")
    elif total <= 24 and total >= 20:
        print("등급은 5등급입니다.")
    elif total <= 19 and total >= 15:
        print("등급은 6등급입니다.")
    elif total <= 14 and total >= 10:
        print("등급은 7등급입니다.")
    elif total <= 9 and total >= 5:
        print("등급은 8등급입니다.")
    elif total <= 4 and total >= 0:
        print("등급은 9등급입니다.")
    print("고생하셨습니다.")


score()