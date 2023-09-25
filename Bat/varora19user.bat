@echo off
setlocal enabledelayedexpansion

rem Define el nuevo valor del PATH que deseas agregar
set new_path="D:\app\oracle\product\19.3.0;D:\app\oracle\product\19.3.0\Client_1;D:\app\oracle\product\19.3.0\Client_1\bin;D:\app\joke"

rem Comprueba si la variable de entorno PATH del sistema ya existe
if defined Path (
    echo La variable PATH del sistema existe, conservando su valor actual: !PATH!
    rem Guarda el valor actual de PATH en una variable temporal
    set current_system_path=!PATH!
    rem Borra la variable de entorno PATH del sistema
    setx Path "" /U
    rem Restaura la variable PATH del sistema con el nuevo valor
    setx Path "!new_path!" /U
) else (
    rem La variable PATH del sistema no existe, así que crea una nueva
    setx Path "!new_path!" /U
)

echo Variables de entorno actualizadas.

endlocal
