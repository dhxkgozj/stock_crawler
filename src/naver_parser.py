import pandas as pd

code_df = pd.read_html('http://kind.krx.co.kr/corpgeneral/corpList.do?method=download&searchType=13', header=0)[0]


code_df.종목코드 = code_df.종목코드.map('{:06d}'.format)

code_df = code_df[['회사명', '종목코드']]

code_df = code_df.rename(columns={'회사명': 'name', '종목코드': 'code'})
