import matplotlib.pyplot as plt 
from utils import get_dataframe, is_ticker_aviable

if __name__ == "__main__":
    while True:
        ticker_1 = input("Enter first stock ticker: ")
        if not is_ticker_aviable(ticker=ticker_1):
            print("Wrong ticker name. We have a limited acces to the tickers so it might be our problem")
            continue
        ticker_2 = input("Enter second stock ticker: ")
        if (not is_ticker_aviable(ticker=ticker_2)) or ticker_1 == ticker_2:
            print("Wrong ticker name. We have a limited acces to the tickers so it might be our problem")
            continue
        
        df_1 = get_dataframe(ticker=ticker_1)
        df_2 = get_dataframe(ticker=ticker_2)
        stocks_df = df_1.merge(df_2, right_index=True, left_index=True)

        stocks_df.plot(xlabel="Year", ylabel="Price, $", title=f"Comparison of {ticker_1} and {ticker_2} stock prices", rot=0)
        plt.show()
        
        break