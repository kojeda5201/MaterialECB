Comandos para flash
attrib -h -r -s /s /d *.* 


-- set new format date, decimal and thousand separation
reg add "HKCU\Control Panel\International" /v sShortDate /d "dd/MM/yyyy" /f
reg add "HKCU\Control Panel\International" /v sThousand /d "," /f
reg add "HKCU\Control Panel\International" /v sDecimal /d "." /f

-- para pegar con ctrl + insert
