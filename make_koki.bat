cd /d %~dp0
@ECHO OFF
ECHO +-----------------------------------------------------+
ECHO  SET LANGUAGE. IF ENGLISH : input "1"
ECHO  Œ¾Œê‚ğİ’è‚µ‚Ü‚·B“ú–{Œê‚Ìê‡‚Í"0"‚ğ“ü—Í‚µ‚Ä‚­‚¾‚³‚¢B
ECHO +-----------------------------------------------------+
SET /P INPUT_STR=

if %INPUT_STR%==0 (
    python make_koki_ja.py
) else (
    python make_koki.py
)
for /f "tokens=1* delims==" %%a in (output.txt) do (
    set %%a=%%b
)
if exist makeobj.exe (
    if %ispng%==1 (
        makeobj pak128 %pak% %dat%
    )
)