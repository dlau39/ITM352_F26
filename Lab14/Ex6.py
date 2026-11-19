from io import StringIO

import pandas as pd
import requests

url = "https://www.hicentral.com/hawaii-mortgage-rates.php"

response = requests.get(url)

int_rate_table = pd.read_html(StringIO(response.text))[0]
print(int_rate_table.to_string(index=False, float_format=lambda value: f"{value:.3f}"))