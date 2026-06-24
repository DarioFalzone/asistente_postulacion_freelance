param(
    [Parameter(Mandatory = $true)]
    [string]$InputPath,
    [string]$OutputPath
)

if (-not (Test-Path $InputPath)) {
    Write-Error "Input not found: $InputPath"
    exit 1
}

Add-Type -AssemblyName System.Runtime.WindowsRuntime
$null = [Windows.Foundation.Metadata.ApiInformation,Windows.Foundation,ContentType=WindowsRuntime]

function Await-Operation([object]$async, [Type]$resultType) {
    if ($null -ne $resultType) {
        $method = [System.WindowsRuntimeSystemExtensions].GetMethods() |
            Where-Object { $_.Name -eq 'AsTask' -and $_.IsGenericMethodDefinition -and $_.GetParameters().Count -eq 1 } |
            Select-Object -First 1
        $generic = $method.MakeGenericMethod($resultType)
        $task = $generic.Invoke($null, @($async))
        return $task.GetAwaiter().GetResult()
    } else {
        $method = [System.WindowsRuntimeSystemExtensions].GetMethods() |
            Where-Object { $_.Name -eq 'AsTask' -and -not $_.IsGenericMethodDefinition -and $_.GetParameters().Count -eq 1 } |
            Select-Object -First 1
        $task = $method.Invoke($null, @($async))
        return $task.GetAwaiter().GetResult()
    }
}

$storageFile = [Windows.Storage.StorageFile,Windows.Storage,ContentType=WindowsRuntime]
$pdfDocType = [Windows.Data.Pdf.PdfDocument,Windows.Data.Pdf,ContentType=WindowsRuntime]
$ocrType = [Windows.Media.Ocr.OcrEngine,Windows.Media.Ocr,ContentType=WindowsRuntime]
$decoderType = [Windows.Graphics.Imaging.BitmapDecoder,Windows.Graphics.Imaging,ContentType=WindowsRuntime]
$streamType = [Windows.Storage.Streams.InMemoryRandomAccessStream,Windows.Storage.Streams,ContentType=WindowsRuntime]

$resolvedPath = (Resolve-Path $InputPath).Path
$file = Await-Operation ($storageFile::GetFileFromPathAsync($resolvedPath)) ([Windows.Storage.StorageFile])
$pdf = Await-Operation ($pdfDocType::LoadFromFileAsync($file)) ([Windows.Data.Pdf.PdfDocument])
$ocr = $ocrType::TryCreateFromUserProfileLanguages()
if ($null -eq $ocr) {
    Write-Error "OCR engine not available for current user languages."
    exit 1
}

$sb = New-Object System.Text.StringBuilder
for ($i = 0; $i -lt $pdf.PageCount; $i++) {
    $page = $pdf.GetPage($i)
    $stream = New-Object $streamType
    Await-Operation ($page.RenderToStreamAsync($stream)) $null | Out-Null
    $decoder = Await-Operation ($decoderType::CreateAsync($stream)) ([Windows.Graphics.Imaging.BitmapDecoder])
    $bitmap = Await-Operation ($decoder.GetSoftwareBitmapAsync()) ([Windows.Graphics.Imaging.SoftwareBitmap])
    $result = Await-Operation ($ocr.RecognizeAsync($bitmap)) ([Windows.Media.Ocr.OcrResult])
    $null = $sb.AppendLine("--- PAGE $($i + 1) ---")
    $null = $sb.AppendLine($result.Text)
    $page.Dispose()
}

$text = $sb.ToString()
if ($OutputPath) {
    Set-Content -Path $OutputPath -Value $text -Encoding utf8
} else {
    $text
}
