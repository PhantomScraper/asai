---
title: "leaps_hw_ver_set_once"
lang: ja
slug: "leaps-rtls/integration-guide/api-commands/leaps-hw-ver-set-once"
section: "leaps-rtls"
sourceUrl: "https://docs.leapslabs.com/ja/leaps-rtls/integration-guide/api-commands/leaps-hw-ver-set-once/"
order: 260
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="leaps-hw-ver-set-once">
<span id="id1"></span><h1>leaps_hw_ver_set_once</h1>
<p>ライトワンス メモリのハードウェア バージョンを設定します。この呼び出しでハードウェア バージョンが正常に設定された後は、変更できません。HW バージョン バッファのサイズは 2 です。つまり、バッファがいっぱいになった後、バージョン番号を最大 2 回書き込むことができます。2 番目の HW バージョンは、1 番目の HW バージョンよりも優先度が高くなります。1 番目の HW バージョンと同じ 2 番目の HW バージョンを書き込もうとすると、無効なパラメータとして拒否されます。</p>
<hr class="docutils">
<div class="sd-container-fluid sd-sphinx-override sd-mb-4 docutils">
<div class="sd-row sd-row-cols-2 sd-row-cols-xs-2 sd-row-cols-sm-2 sd-row-cols-md-2 sd-row-cols-lg-2 docutils">
<div class="sd-col sd-d-flex-row sd-col-11 sd-col-xs-11 sd-col-sm-11 sd-col-md-11 sd-col-lg-11 sd-m-2 docutils">
<div class="sd-card sd-sphinx-override sd-w-100 sd-shadow-sm docutils">
<div class="sd-card-body docutils">
<div class="sd-card-title sd-font-weight-bold docutils">
入力</div>
<ul class="simple">
<li><p class="sd-card-text"><a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/leaps-api/api-generic-data-types#statuscode"><span class="std std-ref">ステータスコード</span></a></p></li>
<li><p class="sd-card-text">hw_version: 32 ビット整数</p></li>
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
<li><p class="sd-card-text">(<em>なし</em>)</p></li>
</ul>
</div>
</div>
</div>
</div>
</div>
<hr class="docutils">
<p>SPI/UART の例</p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 31%">
<col style="width: 37%">
<col style="width: 31%">
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
<tr class="row-odd"><td rowspan="2"><p>0x84</p></td>
<td rowspan="2"><p>0x04</p></td>
<td><p>リトルエンディアンでのハードウェア バージョン (例: 0x 02100111)</p></td>
</tr>
<tr class="row-even"><td><p>0x11 0x01
0x10 0x02</p></td>
</tr>
</tbody>
</table>
<p>タイプ 0x84 (132 dec) はコマンド <a class="reference internal" href="#leaps-hw-ver-set-once"><span class="std std-ref">leaps_hw_ver_set_once</span></a> を意味します</p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 30%">
<col style="width: 30%">
<col style="width: 40%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="3"><p>TLV 応答</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>タイプ</p></td>
<td><p>長さ</p></td>
<td><p>値（エラーコードを参照）</p></td>
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
