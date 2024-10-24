# change the ticker value, export as csv, and import to sheets

import yfinance as yf
import pandas as pd


stock_symbol = 'ticker'
interval = '1mo'  

stock_data = yf.download(stock_symbol, start='2023-01-01', end='2023-10-01', interval=interval)

ticker = yf.Ticker(stock_symbol)

info = ticker.info

additional_metrics = {
    'Metric': [
        'Price', 'Price (USD)', 'Year on Year Chart', 'Change', 'Change %',
        'Perf Week', 'Perf Month', 'Perf Quarter', 'Perf Half Year', 'Perf Year',
        'Perf (ytd)', 'Market Cap', 'Cap Size', 'Income (ttm)', 'Revenue (ttm)',
        'Shares Outstanding', 'Shares Float', 'Book/Sh Book Value Per Share (mrq)',
        'Cash/Sh Cash Per Share (mrq)', 'Insider Ownership Percentage',
        '6-Month Change In Ownership', 'Institutional Ownership Percentage',
        '3-Month Change In Institutional Ownership', '52 Wk Range',
        'Dist. From 52 Wk High', 'Dist. From 52 Wk Low', 'P/E (ttm)',
        'Forward P/E (next fiscal year)', 'PEG (price to earnings growth)',
        'P/S Price To Sales (ttm)', 'P/B Price To Book (mrq)',
        'P/C Price To Cash Per Share (mrq)', 'P/FCF Price To Free Cashflow (ttm)',
        'Quick Ratio (mrq)', 'Current Ratio (mrq)', 'Total Debt/Eq (mrq)',
        'Lt Debt/Eq (mrq)', 'Beta', 'Volatility (week, month)',
        'ROA Return On Assets (ttm)', 'ROE Return On Equity (ttm)',
        'ROI Return On Investment (ttm)', 'Gross Margin (ttm)',
        'Operating Margin (ttm)', 'Profit Margin (ttm)', 'Do They Issue Dividends?',
        'Dividend Payout Ratio (ttm)', 'Analysts\' Dividend Est. (fiscal year)',
        'Dividend Trailing 12 Months', 'Diluted EPS (ttm)', 
        'Last Quarter EPS Surprise', 'EPS Estimate Next Year',
        'EPS Estimate Next Quarter', 'EPS Growth This Year',
        'EPS Growth Estimate Next Year', 'EPS Growth (ttm)',
        'EPS Growth (q/q)', 'Sales Growth (ttm)', 'Sales Growth (q/q)',
        'Sales Growth Past 5 Years', 'Volume', 'Avg. Volume',
        'No. of Shares Issued', '52wk Returns', 'Standard Deviation of Returns',
        'Yahoo Finance ESG score'
    ],
    'Value': [
        info.get('currentPrice', None), 
        info.get('currentPrice', None),  
        None,  
        info.get('regularMarketChange', None), 
        info.get('regularMarketChangePercent', None),
        info.get('regularMarketPerformanceWeek', None),
        info.get('regularMarketPerformanceMonth', None),
        info.get('regularMarketPerformanceQuarter', None),
        info.get('regularMarketPerformanceHalfYear', None),
        info.get('regularMarketPerformanceYear', None),
        info.get('ytdReturn', None),
        info.get('marketCap', None),
        info.get('marketCap', None),  
        info.get('netIncomeToCommon', None), 
        info.get('totalRevenue', None),
        info.get('sharesOutstanding', None),
        info.get('floatShares', None),
        info.get('bookValue', None),
        info.get('cash', None),
        info.get('insiderPercent', None),
        info.get('sixMonthChangeInOwnership', None),
        info.get('institutionalPercent', None),
        info.get('threeMonthChangeInInstitutionalOwnership', None),
        info.get('fiftyTwoWeekRange', None),
        info.get('distanceFrom52WeekHigh', None),
        info.get('distanceFrom52WeekLow', None),
        info.get('trailingPE', None),
        info.get('forwardPE', None),
        info.get('pegRatio', None),
        info.get('priceToSalesTrailing12Months', None),
        info.get('priceToBook', None),
        info.get('priceToCash', None),
        info.get('priceToFreeCashflow', None),
        info.get('quickRatio', None),
        info.get('currentRatio', None),
        info.get('debtToEquity', None),
        info.get('debtToEquityRatio', None),
        info.get('beta', None),
        None,  
        info.get('returnOnAssets', None),
        info.get('returnOnEquity', None),
        info.get('roi', None),  
        info.get('grossMargins', None),
        info.get('operatingMargins', None),
        info.get('profitMargins', None),
        info.get('dividendRate', None) is not None,
        info.get('payoutRatio', None),
        info.get('dividendEstimate', None),
        info.get('dividendYield', None),
        info.get('dilutedEps', None),
        info.get('lastQuarterEpsSurprise', None),
        info.get('epsForward', None),
        info.get('epsNextQuarter', None),
        info.get('epsThisYear', None),
        info.get('epsGrowthNextYear', None),
        info.get('epsGrowth', None),
        info.get('epsGrowthQuarterOverQuarter', None),
        info.get('salesGrowth', None),
        info.get('salesGrowthQuarterOverQuarter', None),
        info.get('salesGrowth5Years', None),
        info.get('volume', None),
        info.get('averageVolume', None),
        None,  
        None,  
        None,  
        info.get('esgScore', None)
    ]
}


metrics_df = pd.DataFrame(additional_metrics)

combined_data = pd.concat([stock_data, metrics_df.set_index('Metric')], axis=1)

combined_data.to_csv(f'{stock_symbol}_financial_data.csv')

print(f'Data for {stock_symbol} saved to {stock_symbol}_financial_data.csv with {interval} interval.')

combined_data.to_csv(f'{stock_symbol}_financial_data.csv')

print(f'Data for {stock_symbol} saved to {stock_symbol}_financial_data.csv with {interval} interval.')
