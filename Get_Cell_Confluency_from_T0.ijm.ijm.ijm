//Get the cell confluency = AREA, of the cells from the pre-picture (TIME POINT = 0)

dir1 = getDirectory("/Volumes/Documents/Lab_work/KI_Carl_Sellgren/Incucyte/Plate8");
dir2 = getDirectory("/Volumes/Documents/Lab_work/KI_Carl_Sellgren/Incucyte_Analys/Cell_Area_T0_Plate8");
list = getFileList(dir1)


setBatchMode(true);
for (f=0; f<list.length; f++) {
showProgress(f+1, list.length);
	//get files with the ending "00d00h00m.tif" which are all pre-images (Time point = 0)
	if(endsWith(list[f], "00d00h00m.tif")) {

		open(dir1+list[f]);
		run("Duplicate...", " ");
		//convert image into 16-bit type
		run("16-bit");
		run("Subtract Background...", "rolling=15 light");
		setAutoThreshold("Default");
		//run("Threshold...");
		setThreshold(0, 65528);
		setOption("BlackBackground", false);
		run("Convert to Mask");
		run("Set Measurements...", "area area_fraction display redirect=None decimal=3");
		//Analyze Particles: exclude round objects (=debris) -> 0.00-1.00 = perfect circle
		run("Analyze Particles...", "  circularity=0.00-0.17 summarize");
		saveAs("Results", dir2+list[f]+".txt");
		run("Close");
		close(dir1+list[f]);
		close("*");
	}
}






