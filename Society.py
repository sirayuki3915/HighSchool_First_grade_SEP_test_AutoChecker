def score():
    print("이것은 2022년 9월 고1 모의고사-사회 채점 프로그램입니다. 답을 입력하면 맞을 경우 '정답입니다'가 틀렸을 경우에는 정답과 해설이 같이 출력됩니다. 마지막에는 총점이 출력됩니다.")
    print("혹시나 문제 해설에 오타가 있을 경우에는 'jdh04133@naver.com'으로 연락 부탁드립니다.")
    one = input("Please enter the correct answer to question 1: ")
    one = int(one)
    if one == 2:
        one_score = 2
        print("정답입니다!")
    else:
        one_score = 0
        print("1번: 2")
        print("ㄱ. 시간적 관점, ㄴ.윤리적 관점, ㄷ. 사회적 관점, ㄹ. 공간적 관점이다.")
    two = input("Please enter the correct answer to question 2: ")
    two = int(two)
    if two == 3:
        two_score = 2
        print("정답입니다!")
    else:
        two_score = 0
        print("2번: 3")
        print("제시문을 통해 국가가 백성들의 경제적 안정을 보장해 주어야 한다는 것을 추론할 수 있다.")
    three = input("Please enter the correct answer to question 3: ")
    three = int(three)
    if three == 4:
        three_score = 2
        print("정답입니다!")
    else:
        three_score = 0
        print("3번: 4")
        print("㈎는 누리소통망(SNS)에서 의견을 주고 받는 상황을, ㈏는 학생이 온라인으로 실시간 원격 수업을 받는 상황을 나타낸 것이다. ② ㈎는 누리소통망(SNS)에서 개인의 정치적 의견을 자유롭게 제시하는 모습을 보여주고 있다. ③ ㈏는 정보 교류의 공간적 제약이 축소된 상황을 나타낸다. ⑤ ㈎, ㈏에서는 모두 쌍방향적인 의사소통 과정이 나타난다.")
    four = input("Please enter the correct answer to question 4: ")
    four = int(four)
    if four == 4:
        four_score = 2
        print("정답입니다!")
    else:
        four_score = 0
        print("4번: 4")
        print("프랑스 혁명은 사회 게약설, 계몽사상 등을 배경으로 18세기 후반에 일어났다. 이에 따라 모든 인간이 태어날 때부터 자유롭고 평등하다는 내용이 프랑스 인권 선언에 명시되었다. ㄱ. 원칙적으로 사유 재산 제도를 인정한다. ㄷ. 프랑스 인권 선언은 자유권 중심의 인권을 강조하고 있다.")
    five = input("Please enter the correct answer to question 5: ")
    five = int(five)
    if five == 3:
        five_score = 3
        print("정답입니다!")
    else:
        five_score = 0
        print("5번: 3")
        print("지역 조사 활동 순서는 조사 목적 및 주제 선정→지역 정보 수집(실내 조사, 야외 조사)→지리 정보 분석→보고서 작성 단계로 이루어진다. ㉢의 인공위성의 영상 자료 분석은 삶의 만족도 조사 방법으로 적절하지 않다.")
    six = input("Please enter the correct answer to question 6: ")
    six = int(six)
    if six == 4:
        six_score = 2
        print("정답입니다!")
    else:
        six_score = 0
        print("6번: 4")
        print("자료는 자연재해인 태풍에 대한 긴급 재난 문자이다. ① 태풍은 강한 바람을 동반하기 때문에 대기 중 미세 먼지 농도를 낮춘다. ② 태풍은 기후적 요인에 의해 발생하는 자연재해이다. ③ 판의 경계에 위치한 국가에서 발생 빈도가 높은 것은 지진이다. ⑤ 겨울철에 주로 발생하는 자연재해는 폭설, 한파이다.")
    seven = input("Please enter the correct answer to question 7: ")
    seven = int(seven)
    if seven == 1:
        seven_score = 3
        print("정답입니다!")
    else:
        seven_score = 0
        print("7번: 1")
        print("갑이 주장하는 자연관은 생태 중심주의, 을이 주장하는 자연관은 인간 중심주의이다. ② 인간 중심주의이다. ③, ④ 생태 중심주의의 입장이다. ⑤ 인간 중심주의만의 입장이다.")
    eight = input("Please enter the correct answer to question 8: ")
    eight = int(eight)
    if eight == 1:
        eight_score = 2
        print("정답입니다!")
    else:
        eight_score = 0
        print("8번: 1")
        print("신문 칼럼은 코로나-19가 확산되는 상황에서 특정 인종에 대한 혐오 표현이 나타나는 모습을 보여주며, 이러한 인종 차별에 대응하는 사회적 차원의 노력이 필요하다는 메시지를 전달하고 있다.")
    nine = input("Please enter the correcta answer to question 9: ")
    nine = int(nine)
    if nine == 4:
        nine_score = 2
        print("정답입니다!")
    else:
        nine_score = 0
        print("9번: 4")
        print("자료는 온실가스로 인하여 지구 온난화가 가속화되는 현상을 나타낸 것이다. ④ 지구 온난화가 지속되면 겨울철보다 여름철의 지속 기간이 길어질 것이다.")
    ten = input("Please enter the correct answer to question 10: ")
    ten = int(ten)
    if ten == 4:
        ten_score = 3
        print("정답입니다!")
    else:
        ten_score = 0
        print("10번: 4")
        print("㈎는 과점 시장에서의 담합 행위를 ㈏는 경제 주체의 행위가 다른 경제 주체에게 의도하지 않은 손해를 주는 부정적 외부 효과를 나타낸 것이다. ㄱ. ㈎는 전체 공급자 간의 공정한 경쟁이 이루어지지 않은 모습을 보여준다.")
    eleven = input("Please enter the correct answer to question 11: ")
    eleven = int(eleven)
    if eleven == 5:
        eleven_score = 3
        print("정답입니다!")
    else:
        eleven_score =0
        print("11번: 5")
        print("부산, 울산, 경북 지역에 광역전철 동해남부선이 개통되면서 ⑤ 대도시가 주변 지역의 경제력을 흡수하는 현상이 강화될 것이다.")
    twelve = input("Please enter the correct answer to question 12: ")
    twelve = int(twelve)
    if twelve == 2:
        twelve_score = 2
        print("정답입니다!")
    else:
        twelve_score =0
        print("12번: 2")
        print("㈎는 참정권에 해당한다. 참정권은 국가의 의사 결정 과정에 참여할 수 있는 권리이다. ① 청구권이다. ③, ⑤ 평등권이다. ④ 사회권이다.")
    thirteen = input("Please enter the correct answer to question 13: ")
    thirteen = int(thirteen)
    if thirteen == 5:
        thirteen_score = 2
        print("정답입니다!")
    else:
        thirteen_score = 0
        print("13번: 5")
        print("제시문에서는 양심적으로 부당하다고 판된되는 법률을 위반하되 지역 사회의 양심에 그 법률의 부당성을 호소하기 위해서 징역형도 불사해야 한다고 주장하므로, 부당한 법률에 대한 시민 불복종은 처벌을 감수해야 한다는 것을 알 수 있다.")
    fourteen = input("Please enter the correct answer to question 14: ")
    fourteen = int(fourteen)
    if fourteen == 1:
        fourteen_score = 3
        print("정답입니다!")
    else:
        fourteen_score =0
        print("14번: 1")
        print("교사의 질문에 따라 학생들은 다양한 시민 참여 방법을 제시하고 있다. ㄷ. ㉠은 ㉡과 달리 대의 민주주의의 한계를 보완할 수 있다.")
    fifteen = input("Please enter the correct answer to question 15: ")
    fifteen = int(fifteen)
    if fifteen == 1:
        fifteen_score = 3
        print("정답입니다!")
    else:
        fifteen_score = 0
        print("15번: 1")
        print("우리나라는 산업화로 인하여 2차, 3차 산업의 비중이 증가하고, 1차 산업 종사자 비중은 감소하며, 개인주의 가치관이 증가하였다.")
    sixteen = input("Please enter the correct answer to question 16: ")
    sixteen = int(sixteen)
    if sixteen == 3:
        sixteen_score =3
        print("정답입니다!")
    else:
        sixteen_score = 0
        print("16번: 3")
        print("㈎는 수정 자본주의, ㈏는 신자유주의이다. ① 산업 혁명은 ㉡의 등장 배경으로 작용하였다. ② ㉡ 시기의 사상가 애덤 스미스는 '보이지 않는 손'의 역할을 중시하였다.")
    seventeen = input("Please enter the correct answer to question 17: ")
    seventeen = int(seventeen)
    if seventeen == 3:
        seventeen_score = 3
        print("정답입니다!")
    else:
        seventeen_score = 0
        print("17번: 3")
        print("열대 기후 지역은 고온 다습하여 주민은 얇고 간편한 옷을 주로 착용하며, 음식이 쉽게 상하는 것을 방지하기 위해 기름에 볶거나 튀기며 향신료를 많이 사용한다. 또한 지면의 열기와 습기를 차단하는 고상 가옥이 나타나며, 이동식 화전 농업이 이루어진다. 건조 기후 지역의 가옥 형태는 벽이 두껍고 창문이 작으며, 건물의 지붕이 평평하고, 건물 간의 간격이 좁다. 또한 주민들은 얇은 천으로 온몸을 감싼 옷을 주로 입는다. 침엽수가 풍부한 냉대 기후 지역에서는 통나무집이 나타난다.")
    eighteen = input("Please enter the correct answer to question 18: ")
    eighteen = int(eighteen)
    if eighteen == 2:
        eighteen_score = 2
        print("정답입니다!")
    else:
        eighteen_score = 0
        print("18번: 2")
        print("제시문은 아리스토텔레스의 입장이다. 아리스토텔레스는 인간이 이성적인 기능을 탁월하게 수행할 때 참된 행복이 이루어진다고 주장한다. A는 게임으로 얻은 감각적 쾌락이 최고의 행복이라고 생각하기 때문에 다음 글의 입장에서는 감각적인 쾌락보다는 이성에 따른 삶을 추구해야한다고 조언할 것이다.")
    nineteen = input("Please enter the correct answer to question 19: ")
    nineteen = int(nineteen)
    if nineteen == 5:
        nineteen_score = 3
        print("정답입니다!")
    else:
        nineteen_score = 0
        print("19번: 5")
        print("ㄱ. 최저 임금은 반드시 지켜야 하는 사항이다. 연소 근로자도 성인과 동일한 최저임금을 적용 받아야 한다. ㄴ. 을이 계약대로 근무할 경우, 을의 1일 근무 시간은 휴게 시간 1시간을 제외한 6시간이므로, 을의 1일 임금은 60,000원(10,000X6시간)이다. ㄹ. 갑, 을, 병은 모두 연소 근로자이므로 야간 근로가 금지된다.")
    twenty = input("Please enter the correct answer to question 20: ")
    twenty = int(twenty)
    if twenty == 2:
        twenty_score = 3
        print("정답입니다!")
    else:
        twenty_score = 0
        print("20번: 2")
        print("합리적인 선택을 하기 위해서는 선택에 따른 편익이 기회비용보다 큰 것을 선택해야 하며, 여러 대안 중에서 기회비용이 가장 작은 것을 선택해야 한다. ㄱ. ㉠의 명시적 비용은 3만 원이고, ㉡의 명시적 비용은 2만 원이다. ㄴ. ㉠의 암묵적 비용은 2만 원이고, ㉡의 암묵적 비용은 5만 원이다. ㄹ. ㉠, ㉡의 편익이 50%씩 감소하더라도 갑의 선택은 달라지지 않는다.")
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