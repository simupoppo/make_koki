cd /d %~dp0
@ECHO OFF
ECHO +-----------------------------------------------------+
ECHO  SET LANGUAGE. IF ENGLISH : input "1"
ECHO  �����ݒ肵�܂��B���{��̏ꍇ��"0"����͂��Ă��������B
ECHO +-----------------------------------------------------+
SET /P INPUT_STR=

if %INPUT_STR%==0 (
    make_koki_ja.exe
) else (
    make_koki.exe
)
for /f "tokens=1* delims==" %%a in (output.txt) do (
    set %%a=%%b
)
if exist makeobj.exe (
    if %ispng%==1 (
        makeobj pak128 %pak% %dat%
    )
)