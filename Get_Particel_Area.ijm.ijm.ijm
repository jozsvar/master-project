dir1 = getDirectory("/Volumes/Documents/Lab_work/KI_Carl_Sellgren/Incucyte/Plate1");
dir2 = getDirectory("/Volumes/Documents/Lab_work/KI_Carl_Sellgren/Incucyte_Analys/Particle_Numbers_Plate1");
list = getFileList(dir1);
setBatchMode(true);
for (i=0; i<list.length; i++) {
showProgress(i+1, list.length); 
	open(dir1+list[i]);
	//Insert Macro
	run("Duplicate...", " ");
	run("Find Edges");
	setAutoThreshold("Intermodes dark");
	//run("Threshold...");
	run("Set Measurements...", "area area_fraction display redirect=None decimal=3");
	run("Analyze Particles...", "size=371-Infinity summarize");
	saveAs("Results", dir2+list[i]+".txt");
	run("Close");
	close(dir1+list[i]);
	close("*");
}
