---
title: "leaps_enc_key_set"
lang: ja
slug: "leaps-rtls/integration-guide/api-commands/leaps-enc-key-set"
section: "leaps-rtls"
sourceUrl: "https://docs.leapslabs.com/ja/leaps-rtls/integration-guide/api-commands/leaps-enc-key-set/"
order: 261
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="leaps-enc-key-set">
<span id="id1"></span><h1>leaps_enc_key_set</h1>
<p>。暗号化キーを設定します。キーは不揮発性メモリに保存されます。ゼロのみで構成されるキーは無効とみなされます。キーが設定されると、ノードは自動的に暗号化を有効にできます。ノードが暗号化されたメッセージを検出し、キーを使用してメッセージを復号化できる場合、UWB ネットワークを介して暗号化の自動有効化がトリガーされます。暗号化が自動的に有効になると、BLE オプションは無効になります。キーをクリアすると暗号化を無効にすることができます (<a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/api-commands/leaps-enc-key-clear#leaps-enc-key-clear"><span class="std std-ref">leaps_enc_key_clear</span></a>)。</p>
<p>この呼び出しは、新しい値が設定された場合に内部フラッシュに書き込むため、頻繁に使用するべきではなく、最悪の場合は数百ミリ秒かかる可能性があります。新しい設定を有効にするにはリセットが必要です。</p>
<hr class="docutils">
<div class="sd-container-fluid sd-sphinx-override sd-mb-4 docutils">
<div class="sd-row sd-row-cols-2 sd-row-cols-xs-2 sd-row-cols-sm-2 sd-row-cols-md-2 sd-row-cols-lg-2 docutils">
<div class="sd-col sd-d-flex-row sd-col-11 sd-col-xs-11 sd-col-sm-11 sd-col-md-11 sd-col-lg-11 sd-m-2 docutils">
<div class="sd-card sd-sphinx-override sd-w-100 sd-shadow-sm docutils">
<div class="sd-card-body docutils">
<div class="sd-card-title sd-font-weight-bold docutils">
入力</div>
<ul class="simple">
<li><p class="sd-card-text">16 バイトの値 (<em>暗号化キー</em>)</p></li>
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
<col style="width: 33%">
<col style="width: 33%">
<col style="width: 33%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="3"><p>TLV リクエスト</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>タイプ</p></td>
<td><p>長さ</p></td>
<td><p>値</p></td>
</tr>
<tr class="row-odd"><td><p>0x3C</p></td>
<td><p>0x10</p></td>
<td><p>0x00 0x11
0x22 0x33
0x44 0x55
0x66 0x77
0x88 0x99
0xAA 0xBB
0xCC 0xDD
0xEE 0xFF</p></td>
</tr>
</tbody>
</table>
<p>0x3C と入力すると、コマンド Leaps_enc_key_set を意味します</p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 33%">
<col style="width: 33%">
<col style="width: 34%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="3"><p>TLV 応答</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>タイプ</p></td>
<td><p>長さ</p></td>
<td><p>値</p></td>
</tr>
<tr class="row-odd"><td><p>0x40</p></td>
<td><p>0x01</p></td>
<td><p>0x00</p></td>
</tr>
</tbody>
</table>
<p>タイプ 0x40 はステータスコード</p>
</div>


           </div>
