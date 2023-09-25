@echo off
setlocal

echo Enumerating printers...
wmic printer get name > printer_list.txt

setlocal enabledelayedexpansion
set printer_number=0
for /f "skip=1 tokens=*" %%a in (printer_list.txt) do (
    set /a printer_number+=1
    set "printer_name[!printer_number!]=%%a"
)

echo Available printers:
for /l %%i in (1,1,!printer_number!) do (
    echo %%i: !printer_name[%%i]!
)

set /p printer_choice=Seleccione la impresora por defecto:

if "%printer_choice%"=="" (
    echo No printer number selected.
    goto :eof
)

if !printer_name[%printer_choice%]! neq !printer_name[%printer_choice%]! (
    echo Invalid printer number selected.
    goto :eof
)

set "selected_printer=!printer_name[%printer_choice%]!"

echo Setting !selected_printer! as default printer...
RUNDLL32 PRINTUI.DLL,PrintUIEntry /y /n "!selected_printer!"

endlocal


/////////
@echo off
setlocal EnableDelayedExpansion

echo Enumerating printers...
for /f "tokens=2 delims==;" %%a in ('wmic printer get name /value') do (
    set /a "printer_number+=1"
    set "printer_name[!printer_number!]=%%a"
)

echo Available printers:
for /l %%i in (1,1,!printer_number!) do (
    echo %%i: !printer_name[%%i]!
)

set /p printer_choice=Enter the number of the printer to set as default:

if "%printer_choice%"=="" (
    echo No printer number selected.
    goto :eof
)

if not defined printer_name[%printer_choice%] (
    echo Invalid printer number selected.
    goto :eof
)

set "selected_printer=!printer_choice!"

echo Setting !selected_printer! as default printer...
echo "!selected_printer!"
RUNDLL32 PRINTUI.DLL,PrintUIEntry /y /n "!selected_printer!"

endlocal
