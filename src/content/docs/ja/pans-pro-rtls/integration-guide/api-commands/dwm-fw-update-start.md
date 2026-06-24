---
title: "dwm_fw_update_start"
lang: ja
slug: "pans-pro-rtls/integration-guide/api-commands/dwm-fw-update-start"
section: "pans-pro-rtls"
sourceUrl: "https://docs.leapslabs.com/ja/pans-pro-rtls/integration-guide/api-commands/dwm-fw-update-start/"
order: 183
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="dwm-fw-update-start">
<span id="id1"></span><h1>dwm_fw_update_start</h1>
<p>この呼び出しはイーサネット・ゲートウェイでのみ利用可能です。ファームウェアのアップデートを開始する。<a class="reference internal" href="/docs/ja/pans-pro-rtls/integration-guide/api-commands/dwm-fw-update-xfer#dwm-fw-update-xfer"><span class="std std-ref">dwm_fw_update_xfer</span></a> をコールする前にコールする必要があります。リクエストが受け入れられた場合、コマンドステータスが返される： <code class="docutils literal notranslate"><span class="pre">ok</span></code> の後に最初のデータリクエストが続く。データリクエストは常に <a class="reference internal" href="/docs/ja/pans-pro-rtls/integration-guide/api-commands/dwm-fw-update-xfer#dwm-fw-update-xfer"><span class="std std-ref">dwm_fw_update_xfer</span></a> によって処理されなければならない。拒否された場合、更新は開始されない。</p>
<p>ファームウェアのアップデートが拒否された理由は以下の通り：</p>
<ul class="simple">
<li><p>無効なハードウェアバージョンが与えられているか、モジュールがブートローダモードにない(モジュールがブートローダモードにある時間は <a class="reference internal" href="/docs/ja/pans-pro-rtls/integration-guide/api-commands/dwm-boot-cfg-set#dwm-boot-cfg-set"><span class="std std-ref">dwm_boot_cfg_set</span></a> で設定できます。）</p></li>
<li><p>内部エラー</p></li>
<li><p>忙しい - ファームウェアのアップデートがすでに進行中です。</p></li>
</ul>
<div class="sd-container-fluid sd-sphinx-override sd-mb-4 docutils">
<div class="sd-row sd-row-cols-2 sd-row-cols-xs-2 sd-row-cols-sm-2 sd-row-cols-md-2 sd-row-cols-lg-2 docutils">
<div class="sd-col sd-d-flex-row sd-col-11 sd-col-xs-11 sd-col-sm-11 sd-col-md-11 sd-col-lg-11 sd-m-2 docutils">
<div class="sd-card sd-sphinx-override sd-w-100 sd-shadow-sm docutils">
<div class="sd-card-body docutils">
<div class="sd-card-title sd-font-weight-bold docutils">
入力</div>
<ul class="simple">
<li><p class="sd-card-text">hw_version: 32ビット整数 (<em>ハードウェアバージョン</em>)</p></li>
<li><p class="sd-card-text">fw_version: 32ビット整数 (<em>ファームウェアのバージョン</em>)</p></li>
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
<li><p class="sd-card-text"><a class="reference internal" href="/docs/ja/pans-pro-rtls/integration-guide/generic-api-information#pans-statuscode"><span class="std std-ref">ステータスコード</span></a></p></li>
<li><p class="sd-card-text">offset: 32 ビット整数 (<a class="reference internal" href="/docs/ja/pans-pro-rtls/integration-guide/api-commands/dwm-fw-update-xfer#dwm-fw-update-xfer"><span class="std std-ref">dwm_fw_update_xfer</span></a> が次に書き込むデータのオフセット)</p></li>
<li><p class="sd-card-text">size: 32 ビット整数 (<a class="reference internal" href="/docs/ja/pans-pro-rtls/integration-guide/api-commands/dwm-fw-update-xfer#dwm-fw-update-xfer"><span class="std std-ref">dwm_fw_update_xfer</span></a> が書き込むデータのサイズ)</p></li>
</ul>
</div>
</div>
</div>
</div>
</div>
<p><strong>SPI/UART 例</strong></p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 17%">
<col style="width: 17%">
<col style="width: 17%">
<col style="width: 17%">
<col style="width: 17%">
<col style="width: 17%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="6"><p>TLV 要求</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>タイプ</p></td>
<td><p>長さ</p></td>
<td><p>ハードウェア・バージョン</p></td>
<td><p>ファームウェアのバージョン</p></td>
<td><p>ァームウェアチェックサム</p></td>
<td><p>サイズ</p></td>
</tr>
<tr class="row-odd"><td><p>0x3E</p></td>
<td><p>0x10</p></td>
<td><p>0x2A
0x00
0xCA
0xDE</p></td>
<td><p>0x01 0x00
0x01 0x01</p></td>
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
<p>タイプ 0x3E (62 dec) は、コマンド <a class="reference internal" href="#dwm-fw-update-start"><span class="std std-ref">dwm_fw_update_start</span></a> を意味する。</p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 14%">
<col style="width: 14%">
<col style="width: 14%">
<col style="width: 14%">
<col style="width: 14%">
<col style="width: 14%">
<col style="width: 14%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="7"><p>TLV 応答</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>タイプ</p></td>
<td><p>長さ</p></td>
<td><p>値</p></td>
<td><p>タイプ</p></td>
<td><p>長さ</p></td>
<td colspan="2"><p>値</p></td>
</tr>
<tr class="row-odd"><td rowspan="2"><p>0x40</p></td>
<td rowspan="2"><p>0x01</p></td>
<td rowspan="2"><p>0x00</p></td>
<td rowspan="2"><p>0x7E</p></td>
<td rowspan="2"><p>0x08</p></td>
<td><p>オフセット</p></td>
<td><p>サイズ</p></td>
</tr>
<tr class="row-even"><td><p>0x00
0x00
0x00
0x00</p></td>
<td><p>0x00
0x10
0x00
0x00</p></td>
</tr>
</tbody>
</table>
<div class="line-block">
<div class="line">タイプ 0x40 は <a class="reference internal" href="/docs/ja/pans-pro-rtls/integration-guide/generic-api-information#pans-statuscode"><span class="std std-ref">ステータスコード</span></a> を意味します。</div>
<div class="line">タイプ 0x7E (126) はデータ要求を意味する</div>
</div>
</div>


           </div>
