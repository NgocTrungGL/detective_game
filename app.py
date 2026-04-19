from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# GAME_DATA = [
#     {
#         "id": 1,
#         "title": "手がかり1：怪しい物",
#         "story": "学校の門の前に落ちていた...<span class='blank'>______</span>... の１面には、大学近くで起きた交通事故について書かれていた。その事件は、田中先輩に関係しているのではないかと疑われている。",
#         "answers": ["新聞"],
#         "full_sentence": "学校の門の前に落ちていた<span class='highlight-word'>新聞</span>の１面には、大学近くで起きた交通事故について書かれていた。その事件は、田中先輩に関係しているのではないかと疑われている。",
#         "translation_vi": "Trước cổng trường có tờ bao bị rơi, trang đầu nói về một vụ tai nạn xe xảy ra gần khu đại học. Vụ việc được nghi ngờ rằng có liên quan đến Tanaka-senpai.",
#         "hints": [
#             "朝に読む人が多いです。",
#             "世界の出来事が分かります。",
#             "駅やコンビニにも置いてあります。"
#         ]
#     },
#     {
#         "id": 2,
#         "title": "手がかり2：目撃者",
#         "story": "ある学生は、その日、先輩が学校を出る...<span class='blank'>______</span>...をとても急いで歩いているのを見たと証言している。",
#         "answers": ["道"],
#         "full_sentence": "ある学生は、その日、先輩が学校を出る<span class='highlight-word'>道</span>をとても急いで歩いているのを見たと証言している。",
#         "translation_vi": "Một sinh viên cho biết hôm đó thấy tiền bối đi rất vội trên đường dẫn ra khỏi trường",
#         "hints": [
#             " 人や車が通るところです。",
#             " 迷うとき、この場所が分からなくなります。",
#             "学校の前にもあります。"
#         ]
#     },
#     {
#         "id": 3,
#         "title": "手がかり3：カメラ",
#         "story": "防犯カメラには、事故が起きたまさにその時刻に先輩が道路を...<span class='blank'>______</span>...様子が映っていた。その頃、被害者の携帯電話には「思いを込めて書きました…」というメッセージが届いていた。",
#         "answers": ["渡す"],
#         "full_sentence": "防犯カメラには、事故が起きたまさにその時刻に先輩が道路を<span class='highlight-word'>渡す</span>様子が映っていた。その頃、被害者の携帯電話には「思いを込めて書きました…」というメッセージが届いていた。",
#         "translation_vi": "Một camera an ninh ghi lại cảnh tiền bối băng qua đường đúng thời điểm tai nạn. Điện thoại của nạn nhân lúc đó có tin nhắn '思いを込めて書きました…'",
#         "hints": [
#             "横断歩道ですることです。",
#             "信号を見て行います。",
#             "向こう側へ行くときに必要です。"
#         ]
#     },
#     {
#         "id": 4,
#         "title": "手がかり4：うわさ",
#         "story": "友人たちは、被害者を「後輩思いの優しい...<span class='blank'>______</span>...」だと語っている。その特徴は、田中さんによく似ているという。",
#         "answers": ["先輩"],
#         "full_sentence": "友人たちは、被害者を「後輩思いの優しい<span class='highlight-word'>先輩</span>だと語っている。その特徴は、田中さんによく似ているという。",
#         "translation_vi": "Bạn bè mô tả nạn nhân là một đàn anh rất quan tâm hậu bối. Theo như mô tả thì đây rất giống với Tanaka sempai",
#         "hints": [
#             "自分より早く学校に入った人です。",
#             "困ったときに相談できるひと。",
#             "後輩に優しい人も多いです。"
#         ]
#     },
#     {
#         "id": 5,
#         "title": "手がかり5：部室",
#         "story": "部活動のスケジュールによると、被害者はその夜に...<span class='blank'>______</span>...が入っていた。その時間帯は、田中先輩の普段の練習時間とも重なっている。",
#         "answers": ["練習"],
#         "full_sentence": "部活動のスケジュールによると、被害者はその夜に<span class='highlight-word'>練習</span>が入っていた。その時間帯は、田中先輩の普段の練習時間とも重なっている。",
#         "translation_vi": "Lịch của câu lạc bộ cho thấy tối hôm đó nạn nhân có buổi luyện tập. Thời điểm này cũng trùng với lịch luyện tập thường ngày của Tanaka sempai",
#         "hints": [
#             "上手になるために必要です。",
#             "スポーツでも音楽でも行います。",
#             "本番の前にします。"
#         ]
#     },
#     {
#         "id": 6,
#         "title": "手掛かり６：トラブル",
#         "story": "クラスメイトによると、田中は最近、多くの科目を再履修するため...<span class='blank'>______</span>...でとてもストレスを抱えており、恋人への気配りもできなくなっていたという。そのことが原因で、別れることになったと噂されている。",
#         "answers": ["授業登録"],
#         "full_sentence": "クラスメイトによると、田中は最近、多くの科目を再履修するため<span class='highlight-word'>授業登録</span>でとてもストレスを抱えており、恋人への気配りもできなくなっていたという。そのことが原因で、別れることになったと噂されている。",
#         "translation_vi": "Bạn cùng lớp nói dạo này Tanaka rất căng thẳng vì phải đăng kí tín chỉ lại nhiều môn nên không quan tâm đến người yêu và nghe nói đã phải chia tay vì điều này.",
#         "hints": [
#             "新しい学期の準備で行います。",
#             "時間割を決めるために必要です。",
#             "システムエラーが起こると困ります。"
#         ]
#     },
#     {
#         "id": 7,
#         "title": "手がかり7：原稿",
#         "story": "先輩の田中先輩の部屋に立ち寄ったとき、未完成の...<span class='blank'>______</span>...と「第3章を直さなきゃ！」というメモを見つけた。",
#         "answers": ["論文"],
#         "full_sentence": "先輩の田中先輩の部屋に立ち寄ったとき、未完成の<span class='highlight-word'>論文</span>と「第3章を直さなきゃ！」というメモを見つけた。",
#         "translation_vi": "Khi tôi ghé vào phòng tiền bối Takana thì Trong phòng anh ấy, tôi tìm thấy bản luận văn chưa hoàn thành cùng ghi chú “Phải sửa lại chương 3!”.",
#         "hints": [
#             "研究について書きます。",
#             "大学生にとってとても大事です。",
#             "長い文章になることが多いです。"
#         ]
#     },
#     {
#         "id": 8,
#         "title": "手がかり8：不思議な手紙",
#         "story": "パソコンの中には、教授宛ての下書き...<span class='blank'>______</span>...があり、「すみません、期限までに提出できません。」と書いてあった。",
#         "answers": ["メール"],
#         "full_sentence": "パソコンの中には、教授宛ての下書き<span class='highlight-word'>メール</span>があり、「すみません、期限までに提出できません。」と書いてあった。",
#         "translation_vi": "Trong máy tính, có mail nháp gửi cho giáo sư: “Xin lỗi, em chưa thể nộp bài đúng hạn.”",
#         "hints": [
#             "連絡文",
#             "書きかけの文面です。",
#             "通信手段の一つです。"
#         ]
#     },
#     {
#         "id": 9,
#         "title": "手がかり9：締め切り",
#         "story": "私は、タナカ先輩の論文は事故のあった日に...<span class='blank'>______</span>...されるはずだったのだと気づいた。",
#         "answers": ["提出"],
#         "full_sentence": "私は、タナカ先輩の論文は事故のあった日に<span class='highlight-word'>提出</span>されるはずだったのだと気づいた。",
#         "translation_vi": "Tôi hiểu ra rằng Bài luận văn của Tanaka sempai đáng lẽ phải nộp vào hôm tai nạn",
#         "hints": [
#             "宿題やレポートですることです。",
#             "期限があります。",
#             "遅れると問題になります。"
#         ]
#     }
# ]
GAME_DATA = [
    {
        "id": 1,
        "title": "手がかり1：部屋の中",
        "story": "被害者の部屋で、ベッドの近くに...<span class='blank'>______</span>...がきれいに置いてあった。",
        "answers": ["蚊帳"],
        "full_sentence": "被害者の部屋で、ベッドの近くに<span class='highlight-word'>蚊帳</span>がきれいに置いてあった。",
        "translation_vi": "Trong phòng nạn nhân, gần giường có một chiếc màn chống muỗi được đặt gọn gàng.",
        "hints": [
            "虫を防ぐために使います。",
            "ベッドのまわりに置きます。",
            "夏によく使います。"
        ]
    },
    {
        "id": 2,
        "title": "手がかり2：不思議な場所",
        "story": "部屋の奥には、小さな...<span class='blank'>______</span>...があり、毎日お祈りしていたようだ。",
        "answers": ["仏壇"],
        "full_sentence": "部屋の奥には、小さな<span class='highlight-word'>仏壇</span>があり、毎日お祈りしていたようだ。",
        "translation_vi": "Ở sâu trong phòng có một bàn thờ Phật nhỏ, có vẻ nạn nhân cầu nguyện mỗi ngày.",
        "hints": [
            "家の中にあります。",
            "お祈りするときに使います。",
            "日本の文化と関係があります。"
        ]
    },
    {
        "id": 3,
        "title": "手がかり3：ノート",
        "story": "机の上には、「宇宙研究」と書かれたノートがあり、中には...<span class='blank'>______</span>...についてのメモがあった。",
        "answers": ["人工衛星"],
        "full_sentence": "机の上には、「宇宙研究」と書かれたノートがあり、中には<span class='highlight-word'>人工衛星</span>についてのメモがあった。",
        "translation_vi": "Trên bàn có một cuốn sổ ghi “nghiên cứu vũ trụ”, bên trong có ghi chú về vệ tinh nhân tạo.",
        "hints": [
            "宇宙にあります。",
            "地球のまわりを回ります。",
            "テレビや通信に使われます。"
        ]
    },
    {
        "id": 4,
        "title": "手がかり4：お金の問題",
        "story": "引き出しの中から、「...<span class='blank'>______</span>...を返してください」と書かれた紙が見つかった。",
        "answers": ["敷金"],
        "full_sentence": "引き出しの中から、「<span class='highlight-word'>敷金</span>を返してください」と書かれた紙が見つかった。",
        "translation_vi": "Trong ngăn kéo có một tờ giấy ghi: “Hãy trả lại tiền đặt cọc.”",
        "hints": [
            "家を借りるときに払います。",
            "お金に関係があります。",
            "あとで返してもらうこともあります。"
        ]
    },
    {
        "id": 5,
        "title": "手がかり5：壁の痕跡",
        "story": "部屋の壁には、何かを...<span class='blank'>______</span>...ような跡が残っていた。そこに何があったのかは分からないが、不自然な点だった。",
        "answers": ["はがす"],
        "full_sentence": "部屋の壁には、何かを<span class='highlight-word'>はがす</span>ような跡が残っていた。そこに何があったのかは分からないが、不自然な点だった。",
        "translation_vi": "Trên tường có dấu vết như đã bóc thứ gì đó. Không rõ trước đó là gì, nhưng rất đáng nghi.",
        "hints": [
            "シールを取るときに使います。",
            "表面から取ります。",
            "何かがなくなります。"
        ]
    },
    {
        "id": 6,
        "title": "手がかり6：ITの資料",
        "story": "パソコンの中には、新しいシステムの...<span class='blank'>______</span>...が書かれたファイルがあった。",
        "answers": ["要件"],
        "full_sentence": "パソコンの中には、新しいシステムの<span class='highlight-word'>要件</span>が書かれたファイルがあった。",
        "translation_vi": "Trong máy tính có file ghi các yêu cầu của một hệ thống mới.",
        "hints": [
            "仕事でよく使う言葉です。",
            "必要な条件です。",
            "システム開発で大切です。"
        ]
    },
    {
        "id": 7,
        "title": "手がかり7：ログイン記録",
        "story": "事件の前、誰かが被害者のアカウントに...<span class='blank'>______</span>...していたことが分かった。",
        "answers": ["認証"],
        "full_sentence": "事件の前、誰かが被害者のアカウントに<span class='highlight-word'>認証</span>していたことが分かった。",
        "translation_vi": "Trước vụ việc, có ai đó đã xác thực vào tài khoản của nạn nhân.",
        "hints": [
            "ログインのときに必要です。",
            "パスワードと関係があります。",
            "安全のために行います。"
        ]
    },
    {
        "id": 8,
        "title": "手がかり8：計画",
        "story": "さらに調べると、事件にはある大きな...<span class='blank'>______</span>...が関係していることが分かった。",
        "answers": ["スキーム"],
        "full_sentence": "さらに調べると、事件にはある大きな<span class='highlight-word'>スキーム</span>が関係していることが分かった。",
        "translation_vi": "Điều tra thêm cho thấy vụ việc liên quan đến một kế hoạch lớn.",
        "hints": [
            "計画のことです。",
            "ビジネスで使います。",
            "カタカナ語です。"
        ]
    },
    {
        "id": 9,
        "title": "手がかり9：真相",
        "story": "この事件の裏には、お金を優先する...<span class='blank'>______</span>...の考え方があったのかもしれない。",
        "answers": ["資本主義"],
        "full_sentence": "この事件の裏には、お金を優先する<span class='highlight-word'>資本主義</span>の考え方があったのかもしれない。",
        "translation_vi": "Đằng sau vụ việc có thể là tư tưởng đặt tiền bạc lên trên hết của chủ nghĩa tư bản.",
        "hints": [
            "経済の考え方です。",
            "お金と関係があります。",
            "社会でよく使われる言葉です。"
        ]
    }
]
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_level/<int:level_id>', methods=['GET'])
def get_level(level_id):
    if level_id <= len(GAME_DATA):
        return jsonify(GAME_DATA[level_id - 1])
    else:
        return jsonify({"finished": True})

@app.route('/check_answer', methods=['POST'])
def check_answer():
    data = request.json
    user_answer = data.get('answer', '').strip()
    level_id = data.get('level_id', 1)

    current_level = GAME_DATA[level_id - 1]

    if user_answer in current_level['answers']:
        # Trả về thêm full_sentence và translation
        return jsonify({
            "correct": True,
            "message": "データが一致！復号中…",
            "full_sentence": current_level["full_sentence"],
            "translation": current_level["translation_vi"]
        })
    else:
        return jsonify({"correct": False, "message": "残念！ヒントを使ってみましょう。"})

if __name__ == '__main__':
    app.run(debug=True)
