import numpy as np

def calculate_risk(ticker_data: pd.DataFrame) -> float:
    returns = ticker_data['close'].pct_change().dropna()
    risk = np.std(returns) * np.sqrt(252)  # Annualizing the risk
    return risk
