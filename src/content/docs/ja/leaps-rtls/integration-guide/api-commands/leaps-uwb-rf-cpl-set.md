---
title: "leaps_uwb_rf_cpl_set"
lang: ja
slug: "leaps-rtls/integration-guide/api-commands/leaps-uwb-rf-cpl-set"
section: "leaps-rtls"
sourceUrl: "https://docs.leapslabs.com/ja/leaps-rtls/integration-guide/api-commands/leaps-uwb-rf-cpl-set/"
order: 272
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="leaps-uwb-rf-cpl-set">
<span id="id1"></span><h1>leaps_uwb_rf_cpl_set</h1>
<p>UWB チャネルとともに UWB RF 準拠を設定します。たとえば、UWB 設定パラメータが次のような場合Tx 電力などは <a class="reference external" href="#leaps_uwb_cfg_set">leaps_uwb_cfg_set</a> を使用して設定され、UWB RF コンプライアンスは自動的に <code class="docutils literal notranslate"><span class="pre">カスタム</span></code> に設定されます。設定を有効にするにはリセットが必要です。設定は不揮発性メモリに保存されます。すべてのボードですべてのチャネルがサポートされているわけではありません。 ARIB RF 準拠は、UWB チャネル 9 でのみサポートされます。</p>
<div class="sd-container-fluid sd-sphinx-override sd-mb-4 docutils">
<div class="sd-row sd-row-cols-2 sd-row-cols-xs-2 sd-row-cols-sm-2 sd-row-cols-md-2 sd-row-cols-lg-2 docutils">
<div class="sd-col sd-d-flex-row sd-col-11 sd-col-xs-11 sd-col-sm-11 sd-col-md-11 sd-col-lg-11 sd-m-2 docutils">
<div class="sd-card sd-sphinx-override sd-w-100 sd-shadow-sm docutils">
<div class="sd-card-body docutils">
<div class="sd-card-title sd-font-weight-bold docutils">
入力</div>
<ul class="simple">
<li><p class="sd-card-text">uwb_channel: '2' | ‘3’ | ‘5’ | ‘9’ (<em>UWB チャネル 2、3、5 は DW1000 ボードでのみサポートされ、UWB チャネル 5、9 は DW3000 ボードでのみサポートされます</em>)</p></li>
<li><p class="sd-card-text">rf_compliance: '0' | ‘1’ | ‘2’ (<em>RF 準拠オプション、0 = FCC/ETSI、1 = ETSI + 10dB、2 = ARIB</em>)</p></li>
<li><p class="sd-card-text">pcode: '9' | '10' | '11' | '12' (<em>Tx/Rx プリアンブル コード、これはオプションです。ユーザーが入力しない場合は、以下に指定されているデフォルト値が使用されます。</em>)</p>
<ul>
<li><p class="sd-card-text">Channel 2: Tx/Rx Preamble Code = 11</p></li>
<li><p class="sd-card-text">Channel 3: Tx/Rx Preamble Code = 12</p></li>
<li><p class="sd-card-text">Channel 5: Tx/Rx Preamble Code = 9</p></li>
<li><p class="sd-card-text">Channel 9: Tx/Rx Preamble Code = 11</p></li>
</ul>
</li>
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
<div class="admonition note">
<p class="admonition-title">注釈</p>
<ul class="simple">
<li><p>チャネル 2 とチャネル 3 は``0 = FCC/ETSI``のみをサポートします</p></li>
<li><p>ARIB はチャネル 9 でのみサポートされます。</p></li>
</ul>
</div>
<hr class="docutils">
<p><strong>例</strong></p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 15%">
<col style="width: 15%">
<col style="width: 70%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="3"><p>TLV 要求</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td rowspan="2"><p>タイプ</p></td>
<td rowspan="2"><p>長さ</p></td>
<td><p>値</p></td>
</tr>
<tr class="row-odd"><td><p>バイト0:</p>
<blockquote>
<div><ul class="simple">
<li><p>Bits [7:4]: rf_compliance</p></li>
<li><p>Bits [3:0]: uwb_channel</p></li>
</ul>
</div></blockquote>
<p>byte 1: pcode</p>
</td>
</tr>
<tr class="row-even"><td><p>0x8A</p></td>
<td><p>0x02</p></td>
<td><p>0x29 0x0B</p></td>
</tr>
</tbody>
</table>
<p>タイプ 0x8A (138 dec) はコマンド <a class="reference internal" href="#leaps-uwb-rf-cpl-set"><span class="std std-ref">leaps_uwb_rf_cpl_set</span></a> を意味します</p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 33%">
<col style="width: 33%">
<col style="width: 34%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="3"><p>TLV回复</p></th>
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
</div>


           </div>
