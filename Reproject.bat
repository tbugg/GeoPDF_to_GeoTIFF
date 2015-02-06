for %%F in (*.tif ) do (
	echo Processing file %%F
	
	REM reprojection
	echo Performing reprojection on file %%F to file %%~nF.tiff
	gdalwarp -t_srs EPSG:26912 -dstnodata "0 0 0" %%F NAD83\%%F
)
