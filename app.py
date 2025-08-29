from flask import Flask, request, jsonify

app = Flask(__name__)


FULL_NAME = "Monish"   
DOB = "28012005"         
EMAIL = "monishkumar0128@gmai.com"
ROLL_NO = "22BCE1247"

def alternating_caps_reverse(s):
    res = ""
    make_upper = True
    for ch in reversed(s):
        if ch.isalpha():
            res += ch.upper() if make_upper else ch.lower()
            make_upper = not make_upper
    return res

@app.route("/bfhl", methods=["POST"])
def bfhl():
    try:
        data = request.get_json().get("data", [])
        odd_numbers, even_numbers, alphabets, special_characters = [], [], [], []
        total_sum = 0

        for item in data:
            if item.isdigit() or (item.startswith('-') and item[1:].isdigit()):
                num = int(item)
                if num % 2 == 0:
                    even_numbers.append(item)
                else:
                    odd_numbers.append(item)
                total_sum += num
            elif item.isalpha():
                alphabets.append(item.upper())
            else:
                special_characters.append(item)

        concat_string = alternating_caps_reverse("".join(alphabets))

        return jsonify({
            "is_success": True,
            "user_id": f"{FULL_NAME}_{DOB}",
            "email": EMAIL,
            "roll_number": ROLL_NO,
            "odd_numbers": odd_numbers,
            "even_numbers": even_numbers,
            "alphabets": alphabets,
            "special_characters": special_characters,
            "sum": str(total_sum),
            "concat_string": concat_string
        }), 200

    except Exception as e:
        return jsonify({"is_success": False, "message": str(e)}), 500

@app.route("/", methods=["GET"])
def home():
    return "BFHL API is running 🚀. Use POST /bfhl"

if __name__ == "__main__":
    app.run(port=5000, debug=True)
