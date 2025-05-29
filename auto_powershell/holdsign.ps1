# 定义目标目录
$rootDir = "D:\meme\meme_emoji\emoji"

# 获取所有名称包含 "hold_sigh" 的文件夹（递归搜索）
$foldersToRename = Get-ChildItem -Path $rootDir -Directory -Recurse | 
                  Where-Object { $_.Name -like "*hold_sigh*" }

# 遍历并重命名
foreach ($folder in $foldersToRename) {
    $newName = $folder.Name -replace "hold_sigh", "holdsign"
    $newPath = Join-Path -Path $folder.Parent.FullName -ChildPath $newName
    
    try {
        Rename-Item -Path $folder.FullName -NewName $newName -ErrorAction Stop
        Write-Host "[成功] 已重命名: $($folder.FullName) -> $newName" -ForegroundColor Green
    }
    catch {
        Write-Host "[失败] 无法重命名: $($folder.FullName) (原因: $_)" -ForegroundColor Red
    }
}

Write-Host "`n操作完成！共处理 $($foldersToRename.Count) 个文件夹。" -ForegroundColor Cyan