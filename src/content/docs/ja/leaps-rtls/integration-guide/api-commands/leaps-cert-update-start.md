---
title: "leaps_cert_update_start"
lang: ja
slug: "leaps-rtls/integration-guide/api-commands/leaps-cert-update-start"
section: "leaps-rtls"
sourceUrl: "https://docs.leapslabs.com/ja/leaps-rtls/integration-guide/api-commands/leaps-cert-update-start/"
order: 153
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="leaps-cert-update-start">
<span id="id1"></span><h1>leaps_cert_update_start</h1>
<p>この呼び出しはイーサネット ゲートウェイでのみ使用できます。証明書更新プロセスを開始し、<a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/api-commands/leaps-cert-update-write#leaps-cert-update-write"><span class="std std-ref">leaps_cert_update_write</span></a> を呼び出す前に最初に呼び出す必要があります。要求が受け入れられると、コマンド ステータス = “ok” が返され、その後に最初のデータ要求が続きます。ユーザーは、<a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/api-commands/leaps-cert-update-write#leaps-cert-update-write"><span class="std std-ref">leaps_cert_update_write</span></a> を使用してデータ要求に応答する必要があります。拒否された場合、更新は開始されません。証明書の更新が拒否される理由は次のとおりです:</p>
<ul class="simple">
<li><p>不可 - アップロードする証明書のサイズが無効。</p></li>
<li><p>内部エラー</p></li>
<li><p>アップロードされる証明書のIDが不明です。</p></li>
</ul>
<p>証明書はder形式でなければならない。</p>
<hr class="docutils">
<div class="sd-container-fluid sd-sphinx-override sd-mb-4 docutils">
<div class="sd-row sd-row-cols-2 sd-row-cols-xs-2 sd-row-cols-sm-2 sd-row-cols-md-2 sd-row-cols-lg-2 docutils">
<div class="sd-col sd-d-flex-row sd-col-11 sd-col-xs-11 sd-col-sm-11 sd-col-md-11 sd-col-lg-11 sd-m-2 docutils">
<div class="sd-card sd-sphinx-override sd-w-100 sd-shadow-sm docutils">
<div class="sd-card-body docutils">
<div class="sd-card-title sd-font-weight-bold docutils">
入力</div>
<ul class="simple">
<li><p class="sd-card-text">cert_type : 8ビット符号なし整数 (<em>証明書の識別子/タイプ。0 - CA証明書、1 - 私の証明書、2 - 私の秘密鍵。</em>)</p></li>
<li><p class="sd-card-text">size: 32ビット符号なし整数（<em>アップロードされる証明書の合計サイズ、最大2048バイト</em>）。</p></li>
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
<li><p class="sd-card-text">offset: 32ビット符号なし整数 (<em>次のデータチャンクの予想オフセット</em>)</p></li>
<li><p class="sd-card-text">size: 32ビット符号なし整数 (<em>次のデータチャンクの予想サイズ</em>)</p></li>
<li><p class="sd-card-text"><a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/leaps-api/api-generic-data-types#statuscode"><span class="std std-ref">ステータスコード</span></a></p></li>
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
<col style="width: 22%">
<col style="width: 22%">
<col style="width: 34%">
<col style="width: 22%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="4"><p>TLV 要求</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>タイプ</p></td>
<td><p>長さ</p></td>
<td colspan="2"><p>値</p></td>
</tr>
<tr class="row-odd"><td rowspan="2"><p>0x36</p></td>
<td rowspan="2"><p>0x05</p></td>
<td><p>cert_type (1バイト)</p></td>
<td><p>サイズ (4 バイト)</p></td>
</tr>
<tr class="row-even"><td><p>0x00</p></td>
<td><p>0xC4 0x26 0x00
0x00</p></td>
</tr>
</tbody>
</table>
<p>タイプ0x36 (54 dec) はコマンド Leaps_cert_update_start を意味します</p>
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
<td><p>0xE4
0x03
0x00
0x00</p></td>
</tr>
</tbody>
</table>
<div class="line-block">
<div class="line">タイプ 0x40 はステータスコード</div>
<div class="line">タイプ 0x7E (126) はデータ要求を意味する</div>
</div>
</div>


           </div>
