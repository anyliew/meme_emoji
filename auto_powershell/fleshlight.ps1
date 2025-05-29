# 定义目录路径
$directory = "D:\meme\meme_emoji\emoji"

# 获取所有包含"aircraft_cup"的文件夹
$folders = Get-ChildItem -Path $directory -Directory -Recurse | Where-Object { $_.Name -like "*aircraft_cup*" }

# 遍历并重命名文件夹
foreach ($folder in $folders) {
    $newName = $folder.Name -replace "aircraft_cup", "fleshlight"
    $newPath = Join-Path -Path $folder.Parent.FullName -ChildPath $newName
    
    try {
        Rename-Item -Path $folder.FullName -NewName $newName -ErrorAction Stop
        Write-Host "已重命名: $($folder.FullName) -> $newName"
    }
    catch {
        Write-Host "重命名失败: $($folder.FullName) - $_" -ForegroundColor Red
    }
}

Write-Host "操作完成"