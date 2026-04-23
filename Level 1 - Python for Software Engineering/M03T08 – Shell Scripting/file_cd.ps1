$folder1 = "folder1"
$folder2 = "folder2"
$folder3 = "folder3"
New-Item -Path $folder1 -ItemType Directory
New-Item -Path $folder2 -ItemType Directory
New-Item -Path $folder3 -ItemType Directory
Write-Output "folder with the name $folder1 is created"
Write-Output "folder with the name $folder2 is created"
Write-Output "folder with the name $folder3 is created"

cd $folder1
ls

$folderA = "folderA"
$folderB = "folderB"
$folderC = "folderC"
New-Item -Path $folderA -ItemType Directory
New-Item -Path $folderB -ItemType Directory
New-Item -Path $folderC -ItemType Directory
Write-Output "folder with the name $folderA is created"
Write-Output "folder with the name $folderB is created"
Write-Output "folder with the name $folderC is created"

ls
Remove-Item $folderB -Force
Remove-Item $folderC -Force
Write-Output "folder with the name $folderB is removed"
Write-Output "folder with the name $folderC is removed"
ls
