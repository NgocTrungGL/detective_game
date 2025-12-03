from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# 新しいデータ構造：3つのヒント & 空欄入りストーリー
GAME_DATA = [
    {
        "id": 1,
        "title": "手がかり①：落ちていたもの",
        "story": "学校の門の前で一枚の新聞を拾った。１面には事故についての ...<span class='blank'>______</span>... が載っていた。",
        "answers": ["新聞"],
        "hints": [
            "意味：ニュース、報道。",
            "よく使う言葉：新聞（しんぶん）",
            "答え（漢字2文字）：報…（ほう…）"
        ]
    },
    {
        "id": 2,
        "title": "手がかり②：目撃証言―道",
        "story": "学生の証言：「彼は駅の方へ向かって ...<span class='blank'>______</span>... を急いで歩いていました。」",
        "answers": ["道"],
        "hints": [
            "意味：車が通る大きな道。",
            "よく使う言葉：道（みち）",
            "答え（漢字2文字）：道…（どう…）"
        ]
    },
    {
        "id": 3,
        "title": "手がかり③：カメラ映像―行動",
        "story": "防犯カメラ映像：田中さんが道路を ...<span class='blank'>______</span>... ところに車が突っ込んだ。",
        "answers": ["渡る"],
        "hints": [
            "意味：横に切って進む、横断する。",
            "よく使う言葉：渡る（わたる）",
            "答え（動詞）：横…（よこ…）"
        ]
    },
    {
        "id": 4,
        "title": "手がかり④：噂話―性格",
        "story": "みんなの噂：「彼はとても真面目な ...<span class='blank'>______</span>... だよ。」",
        "answers": ["先輩"],
        "hints": [
            "意味：学年が上の学生。",
            "よく使う言葉：先輩（せんぱい）",
            "答え（漢字3文字）：上…（じょう…）"
        ]
    },
    {
        "id": 5,
        "title": "手がかり⑤：部室―スケジュール表",
        "story": "掲示板には「18:00 〜 ...<span class='blank'>______</span>... のリハーサル」と書かれている。",
        "answers": ["練習する"],
        "hints": [
            "意味：本番前の練習・リハーサル。",
            "よく使う言葉：練習（れんしゅう）",
            "答え（カタカナ）：リ…（り…）"
        ]
    },
    {
        "id": 6,
        "title": "手がかり⑥：クラスメイト―トラブル",
        "story": "田中さんは、 ...<span class='blank'>______</span>... の手続きがシステムエラーでできずにストレスを抱えていた。",
        "answers": ["授業登録"],
        "hints": [
            "意味：授業や単位の登録申請。",
            "よく使う言葉：授業登録（じゅぎょうとうろく）",
            "答え（漢字4文字）：履…（り…）"
        ]
    },
    {
        "id": 7,
        "title": "手がかり⑦：アパート―原稿",
        "story": "部屋の机の上には、書きかけの ...<span class='blank'>______</span>... が置いてあった。",
        "answers": ["論文"],
        "hints": [
            "意味：レポート、研究の文章。",
            "よく使う言葉：論文（ろんぶん）",
            "答え（カタカナ）：レ…（れ…）"
        ]
    },
    {
        "id": 8,
        "title": "手がかり⑧：パソコン―下書きメール",
        "story": "下書きフォルダには教授宛の ...<span class='blank'>______</span>... が残っていた。",
        "answers": ["メール"],
        "hints": [
            "意味：メール（フォーマルな表現）。",
            "よく使う言葉：メール（めーる）",
            "答え（漢字＋カナ）：電…（でん…）"
        ]
    },
    {
        "id": 9,
        "title": "手がかり⑨：締め切り",
        "story": "どうやら今日は、そのレポートを ...<span class='blank'>______</span>... 最終期限だったようだ。",
        "answers": ["提出"],
        "hints": [
            "意味：提出すること、出すこと。",
            "よく使う言葉：出す（だす）",
            "答え（漢字2文字）：提…（てい…）"
        ]
    }
]

@app.route('/')
def index():
    return render_template('game.html')

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
    level_id = data.get('level_id')
    current_level = GAME_DATA[level_id - 1]
    
    if user_answer in current_level['answers']:
        return jsonify({"correct": True, "message": "正解！手がかりが解放されました。"})
    else:
        return jsonify({"correct": False, "message": "残念！ヒントを使ってみましょう。"})


if __name__ == '__main__':
    app.run(debug=True)
