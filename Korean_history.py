def score():
    print("이것은 2022년 9월 고1 모의고사-한국사 채점 프로그램입니다. 답을 입력하면 맞을 경우 '정답입니다'가 틀렸을 경우에는 정답과 해설이 같이 출력됩니다. 마지막에는 총점이 출력됩니다.")
    print("혹시나 문제 해설에 오타가 있을 경우에는 'jdh04133@naver.com'으로 연락 부탁드립니다.")
    one = input("Please enter the correct answer to question 1: ")
    one = int(one)
    if one == 4:
        one_score = 2
        print("정답입니다!")
    else:
        one_score = 0
        print("1번: 4")
        print("밑줄 친 '이 시대'는 신석기 시대이다. 신석기 시대에는 농경과 목축이 시작되었다. 신석기인은 주로 강가나 바닷가에 움집을 짓고 생활하였으며 간석기를 사용하였다. ①은 조선, ③은 고조선에 해당한다. ② 선종은 신라 말기부터 고려 시대에 걸쳐 유행하였다. ⑤ 팔관회는 삼국 시대에 시작되어 고려 시대에 국가 의례로 정착되었다.")
    two = input("Please enter the correct answer to question 2: ")
    two = int(two)
    if two == 3:
        two_score = 2
        print("정답입니다!")
    else:
        two_score = 0
        print("2번: 3")
        print("㈎는 신라이다. 석굴암 본존불상, 불국사 삼층석탑, 이차돈 순교비는 신라의 대표적인 불교 문화유산이다. 골품제는 신라의 신분 제도이다. ①은 후백제, ②는 고구려, ④는 백제, ⑤는 부여에 해당한다.")
    three = input("Please enter the correct answer to question 3: ")
    three = int(three)
    if three == 1:
        three_score = 3
        print("정답입니다!")
    else:
        three_score = 0
        print("3번: 1")
        print("밑줄 친 '이 나라'는 발해이다. 대조영이 건국한 발해는 9세기 선왕 때 전성기를 맞이하였으며, 이 무렵 주변국으로부터 해동성국이라고 불렸다. ②, ④는 조선, ③, ⑤는 신라에 해당한다.")
    four = input("Please enter the correct answer to question 4: ")
    four = int(four)
    if four == 4:
        four_score = 3
        print("정답입니다!")
    else:
        four_score = 0
        print("4번: 4")
        print("밑줄 친 '전쟁'은 임진왜란이다. 임진왜란 초기 선조는 의주로 피란하였다. 그러나 이순신이 이끄는 수군과 전국 각자에서 일어난 의병의 활약, 명의 참전 등에 힙입어 전세가 역전되었다. ① 한일의정서는 러일 전쟁 중에 체결되었다. ② 척화비는 신미양요 직후에 세워졌다. ③ 양헌수는 병인양요 당시 정족산성에서 항전하였다. ⑤는 1868년에 발생하였다.")
    five = input("Please enter the correct answer to question 5: ")
    five = int(five)
    if five == 2:
        five_score = 2
        print("정답입니다!")
    else:
        five_score = 0
        print("5번: 2")
        print("㈎는 거란의 1차 침입(993), ㈏는 금의 사대 요구 수용(1126)과 관련된 그림이다. 별무반은 여진 정벌을 위해 윤관의 건의로 편성되었다.(1104), ①은 660년, ③은 1866년, ④는 14세기 후반, ⑤는 1636년에 해당한다.")
    six = input("Please enter the correct answer to question 6: ")
    six = int(six)
    if six == 5:
        six_score = 3
        print("정답입니다!")
    else:
        six_score = 0
        print("6번: 5")
        print("㈎는 고려 공민왕이다. 공민왕은 신돈을 등용하고 전민변정도감을 설치하여 권문세족이 불법으로 빼앗은 토지와 억울하게 노비로 삼은 양민을 원래대로 돌려놓고자 하였다. ①은 고려 태조, ②는 조선 영조, ③은 조선 고종, ④는 조선 세종에 해당한다.")
    seven = input("Please enter the correct answer to question 7: ")
    seven = int(seven)
    if seven == 4:
        seven_score = 2
        print("정답입니다!")
    else:
        seven_score = 0
        print("7번: 4")
        print("자료는 신미양요 당시 상황이다. 미국이 제너럴셔먼호 사건을 구실로 강화도에 침입하자, 어재연이 이끄는 조선 수비대는 광성보에 결사 항전하였다.(1871)")
    eight = input("Please enter the correct answer to question 8: ")
    eight = int(eight)
    if eight == 1:
        eight_score = 3
        print("정답입니다!")
    else:
        eight_score = 0
        print("8번: 1")
        print("㈎는 고려이다. 원 간섭기에는 민족적 자유 의식을 표현한 역사서가 편찬되었는데, 『제왕운기』와 『삼국유사』 등이 대표적이다. 국자감은 고려의 최고 교육 기관이다. ②, ④는 조선, ③은 대한 제국, ⑤는 신라에 해당한다.")
    nine = input("Please enter the correcta answer to question 9: ")
    nine = int(nine)
    if nine == 4:
        nine_score = 2
        print("정답입니다!")
    else:
        nine_score = 0
        print("9번: 4")
        print("밑줄 친 '이 시기'는 조선 후기이다. 조선 후기에는 상품 화폐 경제가 발달하면서 상평통보가 활발하게 유통되었다. ②는 통일 신라에 해당한다. ① 녹읍은 신라 신문왕 때 폐지되었으나 경덕왕 때 부활하였다. ③ 과전법은 고려 말부터 조선 초까지 시행되었다. ⑤ 산미 증식 계획은 일제에 의해 1920년부터 1934년까지 실시되었으며, 군량 마련을 위해 1938년에 다시 실시되었다.")
    ten = input("Please enter the correct answer to question 10: ")
    ten = int(ten)
    if ten == 3:
        ten_score = 2
        print("정답입니다!")
    else:
        ten_score = 0
        print("10번: 3")
        print("㈎는 조선 성종이다. 성종은 『경국대전』을 반포하여 조선의 통치 체제를 확립하였다. ①은 백제 성왕, ②는 신라 진흥왕, ⑤는 조선 고종에 해당한다. ④ 헌의 6조는 대한 제국이 선포된 이후인 1898에 고종이 승인하였다.")
    eleven = input("Please enter the correct answer to question 11: ")
    eleven = int(eleven)
    if eleven == 5:
        eleven_score = 2
        print("정답입니다!")
    else:
        eleven_score =0
        print("11번: 5")
        print("밑줄 친 '이 책'은 『조선책략』이다. 『조선책략』이 유포되자 이만손 등은 영남 만인소를 올렸다.(1881) ① 병인박해는 1866년에 일어났다. ② 강화도 조약은 1876년에 채결되었다. ③ 숙종 때 조선과 청은 경계를 확정하여 1712년 백두산정계비를 세웠다. ④ 삼별초는 개경 환도에 반대하며 대몽 항쟁을 전개하였다.")
    twelve = input("Please enter the correct answer to question 12: ")
    twelve = int(twelve)
    if twelve == 1:
        twelve_score = 3
        print("정답입니다!")
    else:
        twelve_score =0
        print("12번: 1")
        print("㈎는 흥선 대원군이다. 흥선 대원군은 민생 안정을 위해 호포제를 시행하였다. ③, ⑤는 고려에 해당한다. ② 몽골의 침입으로 강화도로 천도했던 고려는 몽골과 강화를 맺고 개경으로 환도하였다.(1270) ④ 대한 제국 시기 고종은 이범윤을 간도 관리사로 임명하였다.(1903)")
    thirteen = input("Please enter the correct answer to question 13: ")
    thirteen = int(thirteen)
    if thirteen == 2:
        thirteen_score = 3
        print("정답입니다!")
    else:
        thirteen_score = 0
        print("13번: 2")
        print("밑줄 친 '정변'은 갑신정변이다. 갑신정변은 김옥균, 박영효, 서재필 등 급진 개화파의 주도로 일어났다. ① 예송은 조선 현종 때 자의 대비의 상복 문제를 둘러싸고 발생하였다. ③ 묘청 등은 풍수지리설을 내세워 서경 천도를 주장하였다. ④ 대한 제국은 구본신참의 원칙 아래에 광무 개혁을 추진하였다. ⑤ 을미의병은 을미사변과 단발령에 대한 반발로 발생하였다.")
    fourteen = input("Please enter the correct answer to question 14: ")
    fourteen = int(fourteen)
    if fourteen == 1:
        fourteen_score = 3
        print("정답입니다!")
    else:
        fourteen_score =0
        print("14번: 1")
        print("밑줄 친 '이 조약'은 을사늑약이다. 을사늑약의 체결(1905)로 대한 제국의 외교권이 박탈되고 통감부가 설치되었다. ② 고종은 을미사변 이후 러시아 공사관으로 처소를 옮겼다.(아관 파천) ③ 홍범 14조는 제2차 갑오개혁 때 반포되었다. ④ 6조 직계제는 태종과 세조 등이 실시하였다. ⑤ 보빙사는 조미 수호 통상 조약 체결 이후 미국에서 파견되었다.")
    fifteen = input("Please enter the correct answer to question 15: ")
    fifteen = int(fifteen)
    if fifteen == 3:
        fifteen_score = 2
        print("정답입니다!")
    else:
        fifteen_score = 0
        print("15번: 3")
        print("밑줄 친 '농민군'은 동학 농민군이다. 전봉준이 이끄는 동학 농민군이다. 전봉준이 이끄는 동학 농민군은 관군을 황토현 전투에서 격파하였으며, 조선 정부와 전주 화약을 채결하였다. ②는 신민회, ④는 병인양요 당시 프랑스군, ⑤는 지눌에 해당한다. ① 화백 회의는 신라의 귀족 회의 기구이다.")
    sixteen = input("Please enter the correct answer to question 16: ")
    sixteen = int(sixteen)
    if sixteen == 5:
        sixteen_score = 2
        print("정답입니다!")
    else:
        sixteen_score = 0
        print("16번: 5")
        print("밑줄 친 '장정'은 조청 상민 수륙 무역 장정이다. 이 장정은 임오군란 이후 채결되었다.(1882) 조선 건국은 1392년, 인조반정은 1623년, 정묘호란은 1627년, 임술 농민 봉기는 1862년, 임오군란은 1882년, 시모노세키 조약은 1895년의 사실이다.")
    seventeen = input("Please enter the correct answer to question 17: ")
    seventeen = int(seventeen)
    if seventeen == 4:
        seventeen_score = 3
        print("정답입니다!")
    else:
        seventeen_score = 0
        print("17번: 4")
        print("㈎는 국채 보상 운동이다. 이 운동은 『대한매일신보』 등 언론사의 지원으로 전국적으로 확산되었다. ① 묘청은 서경 천도가 좌절되자 난을 일으켰으나 김부식이 이끄는 관군에 의해 진압되었다. ② 조선 정조는 통공 정책을 실시하여 육의전을 제외한 시전 상인의 금난전권을 폐지하였다. ③ 장용영은 조선 정조가 설치한 친위 부대이다. ⑤ 고려 말 이성계는 요동 정벌에 반대하며 위화도 회군을 단행하였다.")
    eighteen = input("Please enter the correct answer to question 18: ")
    eighteen = int(eighteen)
    if eighteen == 5:
        eighteen_score = 2
        print("정답입니다!")
    else:
        eighteen_score = 0
        print("18번: 5")
        print("자료의 보안회는 일제의 황무지 개간권 요구에 반발하여 조직되었다.(1904) 경인선은 1899년 개통된 우리나라 최초의 철도이다. ①은 신라, ②, ④는 고려에 해당한다. ③ 홍경래의 난은 서북 지방에 대한 차별과 세도 정권의 수탈에 반발하여 1811년에 일어났다.")
    nineteen = input("Please enter the correct answer to question 19: ")
    nineteen = int(nineteen)
    if nineteen == 3:
        nineteen_score = 3
        print("정답입니다!")
    else:
        nineteen_score = 0
        print("19번: 3")
        print("㈎는 대한 제국이다. 대한 제국은 대한국 국제를 제정하여 황제가 입법권, 행정권, 사법권 등 모든 권한을 가지는 전제 군주 국가임을 명시하였다. ①은 신라, ②, ⑤는 고려, ④는 고구려에 해당한다.")
    twenty = input("Please enter the correct answer to question 20: ")
    twenty = int(twenty)
    if twenty == 2:
        twenty_score = 3
        print("정답입니다!")
    else:
        twenty_score = 0
        print("20번: 2")
        print("자료는 1910년대의 상황이다. 이 시기 일제는 헌병 경찰 제도와 조선 태형령을 시행하는 등 강압적으로 조선을 통치하였다. 또한 회사령을 제정하여 기업을 설립할 때 조선 총독의 허가를 받게 하였다. ①, ③, ④는 조선, ⑤는 고려에 해당한다.")
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