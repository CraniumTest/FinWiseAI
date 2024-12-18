from flask import Flask, request, jsonify
import pandas as pd
from financial_planning import generate_financial_plan

app = Flask(__name__)

@app.route('/financial_plan', methods=['POST'])
def financial_plan():
    user_data = request.json
    plan = generate_financial_plan(pd.DataFrame(user_data))
    return jsonify(plan)

if __name__ == '__main__':
    app.run(debug=True)
