import pandas as pd
from colorama import Fore, Back, Style

cho = {
    'choice': [1, 2, 3, 4, 5],
    'NAME OF THE APPLICATION': [
        "TO CALCULATE THE SIMPLE INTEREST",
        "TO CALCULATE THE COMPOUND INTEREST",
        "TO CALCULATE THE EMI",
        "TO CALCULATE THE GST",
        "TO CALCULATE THE FIXED DEPOSIT"
    ]
}

df1 = pd.DataFrame(cho)

def colorize_text(text, color):
    return f"{color}{text}{Style.RESET_ALL}"

colored_headers = [colorize_text(header, Fore.RED) for header in df1.columns]

# Make sure to convert the DataFrame values to strings to avoid 'nan' issues
colored_data = df1.applymap(lambda x: colorize_text(str(x), Fore.GREEN))

colored_df1 = pd.DataFrame(colored_data, columns=colored_headers)

print(colored_df1)