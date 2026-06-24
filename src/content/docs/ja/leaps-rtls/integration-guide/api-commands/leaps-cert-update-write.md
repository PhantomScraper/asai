---
title: "leaps_cert_update_write"
lang: ja
slug: "leaps-rtls/integration-guide/api-commands/leaps-cert-update-write"
section: "leaps-rtls"
sourceUrl: "https://docs.leapslabs.com/ja/leaps-rtls/integration-guide/api-commands/leaps-cert-update-write/"
order: 281
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="leaps-cert-update-write">
<span id="id1"></span><h1>leaps_cert_update_write</h1>
<p>この呼び出しはイーサネット ゲートウェイでのみ使用できます。 <a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/api-commands/leaps-cert-update-start#leaps-cert-update-start"><span class="std std-ref">leaps_cert_update_start</span></a> の後に、すべてのデータ チャンクが転送されるまで、証明書を転送するために繰り返し呼び出す必要があります。すべてのデータが転送されるまで、データ要求に続いてステータス <code class="docutils literal notranslate"><span class="pre">ok</span></code> を返します。すべてのデータが転送されると、データ要求が続かず、または更新が何らかのエラーで終了するまで、ステータス <code class="docutils literal notranslate"><span class="pre">ok</span></code> が返されます。エラーは、<code class="docutils literal notranslate"><span class="pre">ok</span></code> 以外のステータス コードで示されます。アップデートが失敗する理由は次のとおりです:</p>
<ul class="simple">
<li><p>内部エラー</p></li>
<li><p>無効なパラメータ - 長さがゼロのデータチャンク、データチャンクがスキップされたなど</p></li>
<li><p>未許可 - まだ開始されていないか、更新プロセス全体が失敗した</p></li>
</ul>
<p>これまでの更新プロシージャによってフラッシュに既に書き込まれているデータのサイズとオフセットは、更新が完了するまで、leaps_cert_update_write を呼び出すたびに応答として返されます。</p>
<hr class="docutils">
<div class="sd-container-fluid sd-sphinx-override sd-mb-4 docutils">
<div class="sd-row sd-row-cols-2 sd-row-cols-xs-2 sd-row-cols-sm-2 sd-row-cols-md-2 sd-row-cols-lg-2 docutils">
<div class="sd-col sd-d-flex-row sd-col-11 sd-col-xs-11 sd-col-sm-11 sd-col-md-11 sd-col-lg-11 sd-m-2 docutils">
<div class="sd-card sd-sphinx-override sd-w-100 sd-shadow-sm docutils">
<div class="sd-card-body docutils">
<div class="sd-card-title sd-font-weight-bold docutils">
入力</div>
<ul class="simple">
<li><p class="sd-card-text">offset: 32 ビット符号なし整数 (<em>証明書データオフセット。</em>)</p></li>
<li><p class="sd-card-text">データ: 4 ～ 240 バイト (<em>現在アップロード中の証明書データ チャンク、最大 240 バイト</em>)</p></li>
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
<col style="width: 25%">
<col style="width: 25%">
<col style="width: 25%">
<col style="width: 25%">
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
<tr class="row-odd"><td rowspan="2"><p>0x3B</p></td>
<td rowspan="2"><p>0x24</p></td>
<td><p>オフセット</p></td>
<td><p>データ</p></td>
</tr>
<tr class="row-even"><td><p>0x00 0x00
0x00 0x00</p></td>
<td><p>0xA5 0xA5 0xA5
0xA5 0xA5 0xA5
0xA5 0xA5 ….
0xA5 0xA5 0xA5
0xA5</p></td>
</tr>
</tbody>
</table>
<p>タイプ0x3B (59 dec) はコマンド leaps_cert_update_write を意味します</p>
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
<div class="line">タイプ 0x40 はステータスコード</div>
<div class="line">タイプ 0x7E (126 dec) はデータ要求を意味する</div>
</div>
</div>


           </div>
