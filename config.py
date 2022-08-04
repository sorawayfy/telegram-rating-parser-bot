import os
from dotenv import load_dotenv
from functions.Function_URFU import Function_URFU


load_dotenv()

# TG
TOKEN = str(os.getenv('TOKEN'))

# NAMES
UNIVERSITIES = [
    {
        "name": "УРФУ",
        "callback": "Function_URFU"
    }
]

# FUNCTIONS
FUNCTIONS = {
    # [NAME]: [FUNCTION]
    "Function_URFU": Function_URFU
}
