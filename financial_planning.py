from sklearn.linear_model import LinearRegression

def generate_financial_plan(user_data: pd.DataFrame) -> dict:
    regressor = LinearRegression()
    X = user_data[["income", "expenditure"]]
    y = user_data["savings_goal"]
    regressor.fit(X, y)
    prediction = regressor.predict([[user_data.income.mean(), user_data.expenditure.mean()]])
    return {
        "estimated_savings": prediction[0],
        "strategy": "Based on your current spending and income..."
    }
