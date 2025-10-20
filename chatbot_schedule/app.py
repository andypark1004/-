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
    "9월 2일: 국어 중간고사",
    "9월 3일: 수학 중간고사",
    "9월 4일: 영어 중간고사"
]

school_event = [
    "9월 5일: 체육 대회",
    "9월 6일: 영어 대회",
    "9월 7일: 학교 축제"
]

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message", "")

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
    
    else:
        response = "📢 요일이나 '시험 일정', '학교 행사'를 포함해서 질문해 주세요!"

    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
    app.run(debug=True)