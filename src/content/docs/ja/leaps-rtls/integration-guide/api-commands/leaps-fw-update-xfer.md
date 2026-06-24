---
title: "leaps_fw_update_xfer"
lang: ja
slug: "leaps-rtls/integration-guide/api-commands/leaps-fw-update-xfer"
section: "leaps-rtls"
sourceUrl: "https://docs.leapslabs.com/ja/leaps-rtls/integration-guide/api-commands/leaps-fw-update-xfer/"
order: 238
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="leaps-fw-update-xfer">
<span id="id1"></span><h1>leaps_fw_update_xfer</h1>
<hr class="docutils">
<p><a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/api-commands/leaps-fw-update-start#leaps-fw-update-start"><span class="std std-ref">leaps_fw_update_start</span></a> の後にファームウェア データ チャンクを転送するために繰り返し呼び出す必要があります。これは、すべてのファームウェアが転送されるまで行われます。データ チャンクが正常に処理された場合はステータス <code class="docutils literal notranslate"><span class="pre">ok</span></code> が返され、エラーの場合は返されます。エラーは <code class="docutils literal notranslate"><span class="pre">ok</span></code> 以外のステータスで示されます。ファームウェアのアップデートが失敗する理由は次のとおりです。</p>
<ul class="simple">
<li><p>内部エラー</p></li>
<li><p>無効なパラメータ - 例:長さがゼロのデータチャンク、または破損したデータ</p></li>
<li><p>許可されていません - まだ開始されていないか、更新プロセス全体が失敗しました</p></li>
<li><p>チェックサム エラー - 受信したデータが壊れているか、更新の開始時に <a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/api-commands/leaps-fw-update-start#leaps-fw-update-start"><span class="std std-ref">leaps_fw_update_start</span></a> によって提供されたチェックサム値と、最後にモジュールによって計算されたチェックサムが一致しません</p></li>
</ul>
<p>これまでのファームウェア更新手順によってすでに処理されたデータのサイズとオフセットは、更新が完了するまで、leaps_fw_update_xfer への呼び出しごとに応答として返されます。</p>
<hr class="docutils">
<div class="sd-container-fluid sd-sphinx-override sd-mb-4 docutils">
<div class="sd-row sd-row-cols-2 sd-row-cols-xs-2 sd-row-cols-sm-2 sd-row-cols-md-2 sd-row-cols-lg-2 docutils">
<div class="sd-col sd-d-flex-row sd-col-11 sd-col-xs-11 sd-col-sm-11 sd-col-md-11 sd-col-lg-11 sd-m-2 docutils">
<div class="sd-card sd-sphinx-override sd-w-100 sd-shadow-sm docutils">
<div class="sd-card-body docutils">
<div class="sd-card-title sd-font-weight-bold docutils">
入力</div>
<ul class="simple">
<li><p class="sd-card-text">オフセット： 32ビット整数 (<em>ファームウェア・データ全体のオフセット</em>)</p></li>
<li><p class="sd-card-text">データ: 4 ～ 240 バイト (<em>ファームウェア データ チャンク</em>)</p></li>
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
<hr class="docutils">
<p><strong>例</strong></p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 13%">
<col style="width: 11%">
<col style="width: 24%">
<col style="width: 51%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="4"><p>TLV 要求</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td rowspan="2"><p>タイプ</p></td>
<td rowspan="2"><p>長さ</p></td>
<td colspan="2"><p>値</p></td>
</tr>
<tr class="row-odd"><td><p>オフセット</p></td>
<td><p>データチャンク</p></td>
</tr>
<tr class="row-even"><td><p>0x3F</p></td>
<td><p>0x24</p></td>
<td><p>0x00 0x00 0x00
0x00</p></td>
<td><p>0xA5 0xA5 0xA5 0xA5 0xA5 0xA5 0xA5
0xA5 …. 0xA5 0xA5 0xA5 0xA5</p></td>
</tr>
</tbody>
</table>
<p>タイプ 0x3F (63 dec) は、コマンド Leaps_fw_update_xfer を意味します</p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 14%">
<col style="width: 11%">
<col style="width: 11%">
<col style="width: 8%">
<col style="width: 11%">
<col style="width: 23%">
<col style="width: 23%">
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
<td><p>0x04</p></td>
<td><p>0x7E</p></td>
<td><p>0x08</p></td>
<td><p>0x00 0x00 0x00
0x00</p></td>
<td><p>0x00 0x10 0x00
0x00</p></td>
</tr>
</tbody>
</table>
<p>タイプ 0x40 はステータスコード</p>
<p>タイプ 0x7E (126 dec) はファームウェア データ要求を意味します</p>
</div>


           </div>
