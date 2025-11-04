from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

timetable = [
    "국어A, 미술, 사회D(윤리), 음악, 수학A, 과학D(지구과학)",
    "한국사, 영어B, 음악, 미술, 영어A, 체육, 국어A",
    "수학B, 과학A(물리), 한국사, 사회A(지리), 과학실험, 수학A",
    "영어A, 국어B, 사회C(도시), 한국사, 과학C(생명과학), 과학B(화학), 사회B(문화)",
    "국어A, 체육, 영어B, 수학A, 적응, 자치"
]

test_schedule = [
    "12월 8일부터 12일까지"
]

school_event = [
    "10월 31일 구기 대회",
    "돌곶이제"
]

assignments = [
    "11월 4일 한국사 수행평가",
    "11월 10일 사회D 수행평가",
    "11월 11일 미술 나만의 민화 발표",
    "11월 20일 국어B 수행평가"
]

lunch_menu = {
    3: "찹쌀밥<br>콩나물국<br>해물잡채<br>스팸김치구이<br>단무지<br>미니딸기쿠키",
    4: "흑미밥<br>시금장된장국<br>피자함박스테이크<br>애호박양파볶음<br>배추김치<br>사과",
    5: "쌀밥(자율)<br>얼큰순두부찌개<br>닭봉바베큐소스조림<br>골뱅이야채무침<br>콩나물무침<br>배추김치<br>방울토마토",
    6: "흑미밥<br>순두부찌개<br>에그돈까스<br>단호박샐러드<br>도토리묵무침<br>배추김치<br>귤",
    7: "카레라이스<br>닭강정<br>닭다리구이<br>치즈볼<br>콩나물무침/깍두기<br>귤",
    10: "흑미밥<br>맑은순댓국<br>안동식순살찜닭<br>콩나물잡채<br>김구이<br>잡곡밥",
    11: "흑미밥<br>제육당근쌈+꽃상추<br>다시마무채국<br>연두부양념장<br>완두콩밥<br>과바<br>배추김치",
    12: "매콤소보루덮밥",
    13: "대학수학능력시험 (자율학습실 운영, 급식 없음)",
    14: "제육덮밥<br>계란국",
    17: "찹쌀밥<br>들깨미역국<br>닭볶음탕<br>잡채<br>우엉채조림/배추김치<br>케이크",
    18: "자장밥<br>짬뽕국물<br>유부초밥<br>돈가스+소스<br>쫄면야채무침<br>숙주나물<br>배추김치",
    19: "쌀밥<br>황태채무국<br>오리불고기<br>감자채볶음<br>양상추샐러드+키위D<br>배추김치<br>찹쌀도너츠",
    20: "찹쌀밥<br>감자육개장<br>떡갈비<br>새우튀김<br>양배추숙쌈+쌈장<br>깍두기",
    21: "찹쌀밥<br>멸치국수<br>감자핫도그<br>김말이튀김<br>쇠벽김치<br>요구르트",
    24: "율무밥<br>설렁탕<br>얼갈이겉절이<br>볼어묵볶음<br>두부쑥갓무침/배추김치<br>만두튀김",
    25: "흑미밥<br>북어무국<br>원양식불고기<br>군만두<br>콩나물무침<br>자두주스<br>배추김치",
    26: "흑미밥<br>로제파스타<br>맛동산탕수육<br>고구마샐러드<br>양상추샐러드+케요네즈<br>오이피클<br>구슬아이스크림<br>배추김치",
    27: "흑미밥<br>순두부고추장찌개<br>생선까스+타르타르<br>3색야채계란찜<br>열무무침<br>배추김치<br>망고바",
    28: "흑미밥<br>돈채김치찌개<br>멘치까스<br>미니새송이볶음<br>콩나물무침<br>배추김치<br>양파링"
}

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message", "")

def get_date_info(user_message):    

    if not match:
        return None

    month_num_str = match.group(1)
    day_num_str = match.group(2)

    if month_num_str != "11":
        return "11월의 정보만 있습니다."

    try:
        day = int(day_num_str)
        # 11월 급식 딕셔너리에서 해당 날짜 정보 찾기
        if day in lunch_menu:
            return f"🍽️ 11월 {day}일 급식:<br>{lunch_menu[day]}"
        else:
            # 11월이지만 해당 날짜에 급식이 없는 경우
            return f"11월 {day}일에는 중식 정보가 없습니다. (주말 또는 공휴일)"

    if "시험일정" in user_message or "시험 일정" in user_message:
        response = "📘 시험 일정:<br>" + "<br>".join(f" - {item}" for item in test_schedule)

    elif "학교행사" in user_message or "학교 행사" in user_message:
        response = "🎉 학교 행사:<br>" + "<br>".join(f" - {item}" for item in school_event)

    elif "월요일" in user_message:
        response = "월요일 시간표: " + timetable[0]
    
    elif "화요일" in user_message:
        response = "화요일 시간표: " + timetable[1]
    
    elif "수요일" in user_message:
        response = "수요일 시간표: " + timetable[2]
    
    elif "목요일" in user_message:
        response = "목요일 시간표: " + timetable[3]
    
    elif "금요일" in user_message:
        response = "금요일 시간표: " + timetable[4]
        
    elif "수행평가" in user_message or "수행 평가" in user_message:
        response = "✏️ 수행평가 일정:<br>" + "<br>".join(f" - {item}" for item in assignments)
    
    else:
        response = "📢 요일이나 '시험 일정', '학교 행사', '수행평가', '급식이 궁금 날짜'를 포함해서 질문해 주세요!"

    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

    app.run(debug=True)












