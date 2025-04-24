import os
import sys
from streamlit.web import cli as stcli

if __name__ == "__main__":
    os.chdir(os.path.dirname(__file__))

    sys.argv = ["streamlit", "run", "app.py", "--server.port=8501", "--global.developmentMode=false", \
                "--theme.base=light", "--theme.primaryColor=#10475a", "--theme.secondaryBackgroundColor=#f2f9f2"]

    stcli.main()