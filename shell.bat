call D:\PythonVenv\flask\Scripts\activate
set FLASK_APP=%cd%\myblog\manage.py
set FLASK_ENV=development
set FLASK_DEBUG=1

call flask shell
call cmd

pause