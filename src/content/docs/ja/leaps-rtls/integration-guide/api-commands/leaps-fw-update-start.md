---
title: "leaps_fw_update_start"
lang: ja
slug: "leaps-rtls/integration-guide/api-commands/leaps-fw-update-start"
section: "leaps-rtls"
sourceUrl: "https://docs.leapslabs.com/ja/leaps-rtls/integration-guide/api-commands/leaps-fw-update-start/"
order: 237
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="leaps-fw-update-start">
<span id="id1"></span><h1>leaps_fw_update_start</h1>
<p>ファームウェアの更新プロセスを開始します。 <a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/api-commands/leaps-fw-update-xfer#leaps-fw-update-xfer"><span class="std std-ref">leaps_fw_update_xfer</span></a> の前に最初に呼び出す必要があり、数秒かかることがあります。受け入れられた場合、要求はコマンド ステータス <code class="docutils literal notranslate"><span class="pre">ok</span></code> を返し、その後に最初のデータ要求が続きます。データ要求は <a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/api-commands/leaps-fw-update-xfer#leaps-fw-update-xfer"><span class="std std-ref">leaps_fw_update_xfer</span></a> によって処理される必要があります。FW 更新のターゲットは、FW ID が 1 の ELDR (拡張ローダー) または FW ID が 2 のメイン FW のいずれかです。ELDR はすべての HW プラットフォームでサポートされているわけではありません。デバイス情報を読み取る方法については、<a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/api-commands/leaps-dev-info-get#leaps-dev-info-get"><span class="std std-ref">leaps_dev_info_get</span></a> コマンドを参照してください。ファームウェアは自身を更新できないため、FW 更新プロセス中はブートローダーまたは ELDR に再起動する必要があります。</p>
<p>拒否された場合、アップデートは開始されません。ファームウェアのアップデートが拒否される理由は次のとおりです:</p>
<ul class="simple">
<li><p>許可されていません - FW アップデート ターゲットとして指定された FW ID は、ブートローダー モードに入る必要があります (ブートローダー モードはリセット後の短時間だけ常に開始されます。モジュールがブートローダー モードに留まる時間は <a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/api-commands/leaps-boot-cfg-set#leaps-boot-cfg-set"><span class="std std-ref">leaps_boot_cfg_set</span></a> で設定できます)。</p></li>
<li><p>繰り返しになるが - ELDR/FWに切り替えるにはリセットが必要であり、デバイスのリセット後に更新開始要求を再度送信する必要がある。デバイスは <a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/api-commands/leaps-reset#leaps-reset"><span class="std std-ref">leaps_reset</span></a> でリセットできる。</p></li>
<li><p>内部エラー</p></li>
<li><p>引数が無効です - ハードウェア バージョンまたは FW ID が無効です。</p></li>
</ul>
<p>進行中のファームウェアのアップデートは、このコマンドによって再開されます。</p>
<hr class="docutils">
<div class="sd-container-fluid sd-sphinx-override sd-mb-4 docutils">
<div class="sd-row sd-row-cols-2 sd-row-cols-xs-2 sd-row-cols-sm-2 sd-row-cols-md-2 sd-row-cols-lg-2 docutils">
<div class="sd-col sd-d-flex-row sd-col-11 sd-col-xs-11 sd-col-sm-11 sd-col-md-11 sd-col-lg-11 sd-m-2 docutils">
<div class="sd-card sd-sphinx-override sd-w-100 sd-shadow-sm docutils">
<div class="sd-card-body docutils">
<div class="sd-card-title sd-font-weight-bold docutils">
入力</div>
<ul class="simple">
<li><p class="sd-card-text">hw_version: 32ビット整数 (<em>ハードウェアバージョン</em>)</p></li>
<li><p class="sd-card-text">fw_id: '1' | ‘2’ (<em>1 ELDR - 拡張ローダーの場合、または 2 メインファームウェアの場合</em>)</p></li>
<li><p class="sd-card-text">fw_checksum: 32ビット整数 (<em>アップロードするファームウェアのcrc32</em>)</p></li>
<li><p class="sd-card-text">fw_size: 32ビット整数 (<em>ファームウェアのサイズ</em>)</p></li>
</ul>
</div>
</div>
</div>
<div class="sd-col sd-d-flex-row sd-col-11 sd-col-xs-11 sd-col-sm-11 sd-col-md-11 sd-col-lg-11 sd-m-2 docutils">
<div class="sd-card sd-sphinx-override sd-w-100 sd-shadow-sm docutils">
<div class="sd-card-body docutils">
<div class="sd-card-title sd-font-weight-bold docutils">
出力</div>
<ul class="simple">
<li><p class="sd-card-text"><a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/leaps-api/api-generic-data-types#statuscode"><span class="std std-ref">ステータスコード</span></a></p></li>
<li><p class="sd-card-text">offset: 32ビット整数 (<em>leaps_fw_update_xfer</em> が次に書き込む必要があるデータのオフセット)</p></li>
<li><p class="sd-card-text">サイズ: 32 ビット整数 (<em>leaps_fw_update_xfer によって書き込まれる必要があるデータのサイズ</em>)</p></li>
</ul>
</div>
</div>
</div>
</div>
</div>
<hr class="docutils">
<p><strong>例</strong></p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 13%">
<col style="width: 12%">
<col style="width: 18%">
<col style="width: 15%">
<col style="width: 15%">
<col style="width: 15%">
<col style="width: 13%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="7"><p>TLV リクエスト</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td rowspan="2"><p>タイプ</p></td>
<td rowspan="2"><p>長さ</p></td>
<td colspan="5"><p>値</p></td>
</tr>
<tr class="row-odd"><td><p>ハードウェアのバージョン</p></td>
<td><p>ファームウェアID</p></td>
<td><p>予約済み</p></td>
<td><p>ファームウェアチェックサム</p></td>
<td><p>サイズ</p></td>
</tr>
<tr class="row-even"><td><p>0x3E</p></td>
<td><p>0x10</p></td>
<td><p>0x2A 0x00
0xCA 0xDE</p></td>
<td><p>0x02</p></td>
<td><p>0x00
0x00
0x00</p></td>
<td><p>0xea
0xF5
0x67
0x6D</p></td>
<td><p>0xC4
0x26
0x00
0x00</p></td>
</tr>
</tbody>
</table>
<p>タイプ 0x3E (62 dec) はコマンド leaps_fw_update_start を意味します</p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 12%">
<col style="width: 10%">
<col style="width: 9%">
<col style="width: 7%">
<col style="width: 10%">
<col style="width: 26%">
<col style="width: 26%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="7"><p>TLV 応答</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td rowspan="2"><p>タイプ</p></td>
<td rowspan="2"><p>長さ</p></td>
<td rowspan="2"><p>値</p></td>
<td rowspan="2"><p>タイプ</p></td>
<td rowspan="2"><p>長さ</p></td>
<td colspan="2"><p>値</p></td>
</tr>
<tr class="row-odd"><td><p>オフセット</p></td>
<td><p>サイズ</p></td>
</tr>
<tr class="row-even"><td><p>0x40</p></td>
<td><p>0x01</p></td>
<td><p>0x00</p></td>
<td><p>0x7e</p></td>
<td><p>0x08</p></td>
<td><p>0x00 0x00 0x00 0x00</p></td>
<td><p>0x00 0x10 0x00 0x00</p></td>
</tr>
</tbody>
</table>
<p>タイプ 0x40 はステータスコード</p>
<p>タイプ 0x7E (126) はファームウェア データ要求を意味します</p>
</div>


           </div>
