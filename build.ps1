$env:LC_ALL='C.UTF-8'
[System.Console]::OutputEncoding = [System.Text.Encoding]::UTF8

try {
Remove-Item .\build -Recurse
Remove-Item .\TrackerGG.egg-info -Recurse
Remove-Item .\dist -Recurse
}
catch {

}

Write-Host -NoNewLine "Press Any Key To Continue";
$null = $Host.UI.RawUI.ReadKey('NoEcho,IncludeKeyDown');

python setup.py sdist bdist_wheel