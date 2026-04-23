$folder = "new_folder"
$if_folder = "if_folder"
$hyperionDev = "hyperionDev"
$new_projects = "new-projects"

if(Test-Path -Path $folder){	
	New-Item -Path $if_folder -ItemType Directory
    Write-Output "Folder with the name $if_folder is created"
}
if(Test-Path -Path $if_folder){	
	New-Item -Path $hyperionDev -ItemType Directory
	Write-Output "Folder with the name $hyperionDev is created"            
}

else{
	New-Item -Path $new_projects -ItemType Directory
	Write-Output "Folder with the name $new_projects is created"            	
}