$arquivoOrigem = "C:\Users\luizc\OneDrive\Documentos\PDW\PDW.xlsx"
$diretorioDestino = "C:\Users\luizc\Dropbox\PDW_DRPBX"

$ultimoTempoModificacao = Get-Item $arquivoOrigem | Select-Object -ExpandProperty LastWriteTime

while ($true) {
    $tempoModificacaoAtual = Get-Item $arquivoOrigem | Select-Object -ExpandProperty LastWriteTime
    if ($tempoModificacaoAtual -gt $ultimoTempoModificacao) {
        Copy-Item $arquivoOrigem -Destination $diretorioDestino -Force
        $ultimoTempoModificacao = $tempoModificacaoAtual
        Write-Host "Arquivo PDW.xlsx foi copiado para o diretório de destino."
    }
    Start-Sleep -Seconds 5 # Verifica a cada 5 segundos
}