for %%F in (*.pdf) do (
	echo Processing file %%F
	
	REM neatline conversion
	echo Performing neatline extraction on file %%F to file %%~nF.pdf
	python cutline.py %%F
)
