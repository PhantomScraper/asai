---
title: "leaps_alarm_start"
lang: ja
slug: "leaps-rtls/integration-guide/api-commands/leaps-alarm-start"
section: "leaps-rtls"
sourceUrl: "https://docs.leapslabs.com/ja/leaps-rtls/integration-guide/api-commands/leaps-alarm-start/"
order: 146
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="leaps-alarm-start">
<span id="id1"></span><h1>leaps_alarm_start</h1>
<p>指定された期間、オンボードアラームをアクティブにします。</p>
<hr class="docutils">
<div class="sd-container-fluid sd-sphinx-override sd-mb-4 docutils">
<div class="sd-row sd-row-cols-2 sd-row-cols-xs-2 sd-row-cols-sm-2 sd-row-cols-md-2 sd-row-cols-lg-2 docutils">
<div class="sd-col sd-d-flex-row sd-col-11 sd-col-xs-11 sd-col-sm-11 sd-col-md-11 sd-col-lg-11 sd-m-2 docutils">
<div class="sd-card sd-sphinx-override sd-w-100 sd-shadow-sm docutils">
<div class="sd-card-body docutils">
<div class="sd-card-title sd-font-weight-bold docutils">
入力</div>
<ul class="simple">
<li><p class="sd-card-text">LED、モーター、ブザー:​​ ‘0’ | ‘1’ (<em>1 は特定のアラームを有効にします</em>)</p></li>
<li><p class="sd-card-text">期間: 8 ビット符号なし整数 (200 ミリ秒の倍数のアラーム期間)</p></li>
<li><p class="sd-card-text">強度: 8 ビット符号なし整数 (<em>アラーム強度</em>)</p></li>
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
<col style="width: 17%">
<col style="width: 17%">
<col style="width: 66%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="3"><p>TLV 要求</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>タイプ</p></td>
<td><p>長さ</p></td>
<td><p>値</p></td>
</tr>
<tr class="row-odd"><td rowspan="2"><p>0x85</p></td>
<td rowspan="2"><p>0x04</p></td>
<td><p>バイト 0: アラーム設定</p>
<ul class="simple">
<li><p>ビット 0 - LED を有効にする</p></li>
<li><p>ビット 1 - ブザーを有効にする</p></li>
<li><p>ビット 2 - モーターを有効にする</p></li>
<li><p>ビット 3 ～ 7 は予約済み</p></li>
</ul>
<div class="line-block">
<div class="line">バイト 1: 予約済み</div>
<div class="line">バイト 2: 200 ミリ秒の倍数の継続時間</div>
<div class="line">バイト 3: 強​​度</div>
</div>
</td>
</tr>
<tr class="row-even"><td><p>0x07 0x00 0x05 0xff</p></td>
</tr>
</tbody>
</table>
<p>0x85 と入力すると、コマンド Leaps_alarm_start を意味します</p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 25%">
<col style="width: 25%">
<col style="width: 49%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="3"><p>TLV 応答</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>タイプ</p></td>
<td><p>長さ</p></td>
<td><p>値 <strong>（エラーコードを参照）</strong></p></td>
</tr>
<tr class="row-odd"><td><p>0x40</p></td>
<td><p>0x01</p></td>
<td><p>0x00</p></td>
</tr>
</tbody>
</table>
<p>タイプ 0x40 は、直前のコマンドの err_code を意味する</p>
</div>


           </div>
