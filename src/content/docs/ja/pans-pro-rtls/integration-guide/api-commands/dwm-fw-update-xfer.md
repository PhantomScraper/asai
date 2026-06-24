---
title: "dwm_fw_update_xfer"
lang: ja
slug: "pans-pro-rtls/integration-guide/api-commands/dwm-fw-update-xfer"
section: "pans-pro-rtls"
sourceUrl: "https://docs.leapslabs.com/ja/pans-pro-rtls/integration-guide/api-commands/dwm-fw-update-xfer/"
order: 184
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="dwm-fw-update-xfer">
<span id="id1"></span><h1>dwm_fw_update_xfer</h1>
<p>この呼び出しはイーサネットゲートウェイでのみ利用可能である。ファームウェアデータチャンクを転送するために、 <a class="reference internal" href="/docs/ja/pans-pro-rtls/integration-guide/api-commands/dwm-fw-update-start#dwm-fw-update-start"><span class="std std-ref">dwm_fw_update_start</span></a> の後に、すべてのファームウェアデータチャンクが転送されるまで、繰り返しコールされるべきである。ファームウェアのアップデートに必要なすべてのデータが転送されるまで、データリクエストフレームに続いてステータス <code class="docutils literal notranslate"><span class="pre">ok</span></code> を返す。エラーは <code class="docutils literal notranslate"><span class="pre">ok</span></code> 以外のステータスで示される。ファームウェア・アップデートに失敗した理由は以下の通りである：</p>
<ul class="simple">
<li><p>内部エラー</p></li>
<li><p>無効なパラメータ - 長さがゼロのデータチャンクなど</p></li>
<li><p>未許可 - まだ開始されていないか、更新プロセス全体が失敗した</p></li>
<li><p>チェックサムエラー - 受信した画像が壊れています。</p></li>
</ul>
<p>更新が完了するまで、 <a class="reference internal" href="#dwm-fw-update-xfer"><span class="std std-ref">dwm_fw_update_xfer</span></a> を呼び出すたびに、これまでにファームウェア更新プロシージャによってフラッシュメモリに書き込まれたデータのサイズとオフセットが応答として返される。</p>
<div class="sd-container-fluid sd-sphinx-override sd-mb-4 docutils">
<div class="sd-row sd-row-cols-2 sd-row-cols-xs-2 sd-row-cols-sm-2 sd-row-cols-md-2 sd-row-cols-lg-2 docutils">
<div class="sd-col sd-d-flex-row sd-col-11 sd-col-xs-11 sd-col-sm-11 sd-col-md-11 sd-col-lg-11 sd-m-2 docutils">
<div class="sd-card sd-sphinx-override sd-w-100 sd-shadow-sm docutils">
<div class="sd-card-body docutils">
<div class="sd-card-title sd-font-weight-bold docutils">
入力</div>
<ul class="simple">
<li><p class="sd-card-text">オフセット： 32ビット整数 (<em>ファームウェア・データ全体のオフセット</em>)</p></li>
<li><p class="sd-card-text">data: 4バイトから最大32バイト（<em>ファームウェアデータチャンク</em>）</p></li>
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
<li><p class="sd-card-text">size: 32ビット整数 (<em>leaps_fw_update_xfer</em> が書き込む必要のあるファームウェアデータチャンクのサイズ)</p></li>
</ul>
</div>
</div>
</div>
</div>
</div>
<p><strong>SPI/UART 例</strong></p>
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
<tr class="row-odd"><td></td>
<td></td>
<td><p>オフセット</p></td>
<td><p>データチャンク</p></td>
</tr>
<tr class="row-even"><td><p>0x3F</p></td>
<td><p>0x24</p></td>
<td><p>0x00 0x00
0x00 0x00</p></td>
<td><p>0xA5 0xA5 0xA5
0xA5 0xA5 0xA5
0xA5 0xA5 ….
0xA5 0xA5 0xA5
0xA5</p></td>
</tr>
</tbody>
</table>
<p>タイプ 0x3F (63 dec) は、コマンド dwm_fw_update_xfer を意味する</p>
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
<tr class="row-odd"><th class="head" colspan="6"><p>TLV 応答</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>タイプ 長さ</p></td>
<td><p>値</p></td>
<td><p>タイプ</p></td>
<td><p>長さ</p></td>
<td colspan="2"><p>値</p></td>
</tr>
<tr class="row-odd"><td rowspan="2"><p>0x40
0x01</p></td>
<td rowspan="2"><p>0x00</p></td>
<td rowspan="2"><p>0x7E</p></td>
<td rowspan="2"><p>0x08</p></td>
<td><p>オフセット</p></td>
<td><p>サイズ</p></td>
</tr>
<tr class="row-even"><td><p>0x00 0x00
0x00 0x00</p></td>
<td><p>0x00 0x10
0x00 0x00</p></td>
</tr>
</tbody>
</table>
<div class="line-block">
<div class="line">タイプ 0x40 はステータスコード</div>
<div class="line">タイプ 0x7E (126 dec) はデータ要求を意味する</div>
</div>
</div>


           </div>
