from flask import Flask, request, jsonify, render_template
import re

app = Flask(__name__)

timetable = [
    "국어A, 미술, 사회D(윤리), 음악, 수학A, 과학D(지구과학)",
    "한국사, 영어B, 음악, 미술, 영어A, 체육, 국어A",
    "수학B, 과학A(물리), 한국사, 사회A(지리), 과학실험, 수학A",
    "영어A, 국어B, 사회C(도시), 한국사, 과학C(생명과학), 과학B(화학), 사회B(문화)",
    "국어A, 체육, 영어B, 수학A, 적응, 자치"
]

test_schedule = [
    "12월 8일 과학",
    "12월 9일 수학",
    "12월 10일 국어/한국사",
    "12월 11일 영어",
    "12월 12일 사회"
]

school_event = [
    "12월 29일 돌곶이제",
    "12월 31일 방학식"
]

assignments = [
    "수행평가 일정이 없습니다."
]

lunch_menu = {
    1: "차조밥<br>된장찌개<br>제육볶음<br>감자채전<br>김구이<br>배추김치",
    2: "흑미밥<br>사골우거지국<br>순대야채볶음<br>궁중떡볶이<br>우엉조림<br>배추김치",
    3: "찹쌀밥<br>미니마라탕<br>물만두<br>단무지/배추김치<br>에그타르트<br>요구르트",
    4: "찹쌀밥<br>얼큰콩나물국<br>떡갈비<br>온두부*볶음김치<br>양배추숙쌈*쌈장<br>깍두기",
    5: "깍두기볶음밥<br>달걀파국<br>통옥수수텐더*시즈닝<br>미트볼떡조림<br>배추김치<br>귤",
    15: "혼합잡곡밥<br>들깨미역국<br>매운갈비찜<br>버섯잡채<br>배추김치<br>케이크",
    16: "기장밥<br>설렁탕*소면<br>삼치카레구이<br>단호박샐러드<br>깻잎나물무침<br>깍두기",
    17: "국물떡볶이<br>후리카케밥<br>꼬치튀김<br>단무지<br>배추김치<br>복숭아음료",
    18: "찹쌀밥<br>얼갈이된장국<br>돈육양송이볶음<br>건새우부추전<br>유채나물<br>배추김치",
    19: "마파두부덮밥<br>유부미소국<br>짬뽕왕교자<br>토리알감자꼬치<br>배추김치<br>파인애플",
    22: "현미밥<br>북어두부국<br>돼지고기김치찜<br>연두부*양념장<br>도토리묵무침<br>배추김치",
    23: "흑미밥<br>삼색수제비국<br>언양식불고기*겨자소스<br>골뱅이소면무침<br>호박볶음<br>배추김치",
    24: "비빔밥<br>다시마무채국<br>계란후라이<br>고구마맛탕<br>백김치<br>요거바",
    26: "기장밥<br>순댓국<br>김치전<br>김말이강정<br>부추양파무침<br>섞박지/딸기",
    29: "불닭마요덮밥<br>감자국<br>소떡소떡<br>비타민유자무침<br>배추김치<br>샤인머스켓요구르트",
    30: "콩나물밥<br>호박고추장찌개<br>간장불고기<br>갈비만두<br>총각김치<br>호떡",
    31: "로제스파게티<br>옥수수스프<br>해쉬둥지돈까스<br>양상추샐러드*오리엔탈D<br>오이피클*할라피뇨<br>깔라만시레몬에이드"
}

def get_date_info(user_message):
    pattern = r"(\d+)\s*월\s*(\d+)\s*일"
    match = re.search(pattern, user_message)
    
    if not match:
        return None

    month_num_str = match.group(1)
    day_num_str = match.group(2)

    if month_num_str != "12":
        return "12월의 정보만 있습니다."

    try:
        day = int(day_num_str)
        if day in lunch_menu:
            return f"🍽️ 12월 {day}일 급식:<br>{lunch_menu[day]}"
        else:
            return f"12월 {day}일에는 중식 정보가 없습니다."
    except ValueError:
        return None

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message", "")
    response = None

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
    
    if response is None:
        date_response = get_date_info(user_message)
        if date_response:
            response = date_response
            
    if response is None:
        response = "📢 요일이나 '시험 일정', '학교 행사', '수행평가', '급식이 궁금한 날짜'를 포함해서 질문해 주세요!"

    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)






