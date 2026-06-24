---
title: "dwm_int_cfg_set"
lang: ja
slug: "pans-pro-rtls/integration-guide/api-commands/dwm-int-cfg-set"
section: "pans-pro-rtls"
sourceUrl: "https://docs.leapslabs.com/ja/pans-pro-rtls/integration-guide/api-commands/dwm-int-cfg-set/"
order: 194
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="dwm-int-cfg-set">
<span id="id1"></span><h1>dwm_int_cfg_set</h1>
<p>割り込みが発生すると、専用 GPIO ピンの設定を有効または無効にします。さらに、割り込みやイベントは、GPIO ピン CORE_INT1 を設定することでユーザーに通知されます。ユーザはこのピンを外部割り込みのソースとして使用できます。割り込みは、dwm_status_get を使用してステータスを読み出し、それに応じて新しいステータスに対応することで処理できます。ステータスは読み出すとクリアされます。このコールはUART/SPIインターフェースでのみ使用可能である。通常、このコールは新しい値を設定するときに内部フラッシュに書き込むので、最悪の場合数百ミリ秒かかることがあるため、頻繁に使用するべきではありません！</p>
<dl class="c function">
<dt class="sig sig-object c" id="c.dwm_int_cfg_set">
<span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">dwm_int_cfg_set</span></span></span><span class="sig-paren">(</span><span class="kt"><span class="pre">void</span></span><span class="sig-paren">)</span><br></dt>
<dd><dl class="field-list simple">
<dt class="field-odd">パラメータ</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>input</strong> -- spi_data_ready, loc_ready, bh_status_changed, bh_data_ready, bh_initialized_changed, uwb_scan_ready, usr_data_ready,    :param uwbmac_joined_changed</p></li>
<li><p><strong>spi_data_ready</strong> -- '0' | '1' (<em>新しいSPIデータが専用GPIOピンに割り込みを発生させる、0=無効、1=有効</em>)</p></li>
<li><p><strong>loc_ready</strong> -- ‘0’ | ‘1’ (<em>割り込みは、位置データの準備ができたときに発生する、0=無効、1=有効</em>)</p></li>
<li><p><strong>bh_status_changed</strong> -- ‘0’ | ‘1’ (<em>UWBMACのステータス変更、0=無効、1=有効</em>)</p></li>
<li><p><strong>bh_data_ready</strong> -- '0' | '1' (<em>UWBMACバックホールデータ準備完了、0=無効、1=有効</em>)</p></li>
<li><p><strong>bh_initialized_changed</strong> -- '0' | '1' (<em>UWBMACルート設定、0=無効、1=有効</em>)</p></li>
<li><p><strong>uwb_scan_ready</strong> -- '0' | '1' (<em>UWBスキャン結果あり</em>)</p></li>
<li><p><strong>usr_data_ready</strong> -- '0' | '1' (* UWBMACで受信したユーザーデータ*)</p></li>
<li><p><strong>uwbmac_joined_changed</strong> -- '0' | '1' (<em>UWBMAC加入、 0=無効、1=有効</em>)</p></li>
<li><p><strong>usr_data_sent</strong> -- '0' | '1' (* UWBMAC上で完了したユーザーデータTX*)</p></li>
<li><p><strong>output</strong> -- <a class="reference internal" href="/docs/ja/pans-pro-rtls/integration-guide/generic-api-information#pans-statuscode"><span class="std std-ref">ステータスコード</span></a></p></li>
</ul>
</dd>
</dl>
</dd></dl>

<p><strong>Cコード例</strong></p>
<p>オンモジュール・ユーザー・アプリケーションでは使用できません。外部インターフェース（SPI、UART）のみで使用可能。</p>
<p><strong>SPI/UART 例</strong></p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 21%">
<col style="width: 21%">
<col style="width: 57%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>タイプ</p></th>
<th class="head"><p>長さ</p></th>
<th class="head"><p>値</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>0x34</p></td>
<td><p>0x02</p></td>
<td><div class="line-block">
<div class="line">割り込み設定フラグ：</div>
<div class="line">予約済み（ビット9～15）</div>
<div class="line">usr_data_sent (ビット8)</div>
<div class="line">uwbmac_joined_changed (ビット7)</div>
<div class="line">usr_data_ready (ビット6)</div>
<div class="line">uwb_scan_ready (ビット5)</div>
<div class="line">bh_initialized_changed (ビット4)</div>
<div class="line">bh_data_ready (ビット3)</div>
<div class="line">bh_status_changed (ビット2)</div>
<div class="line">spi_data_ready (ビット1)</div>
<div class="line">loc_ready (ビット0)</div>
</div>
</td>
</tr>
<tr class="row-odd"><td></td>
<td></td>
<td><p>0x0F 0x01</p></td>
</tr>
</tbody>
</table>
<p>タイプ 0x34 は、コマンド dwm_int_cfg_set を意味する。</p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 33%">
<col style="width: 33%">
<col style="width: 33%">
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
<div class="line-block">
<div class="line">タイプ0x40は、直前のコマンドの <a class="reference internal" href="/docs/ja/pans-pro-rtls/integration-guide/generic-api-information#pans-statuscode"><span class="std std-ref">ステータスコード</span></a> を意味する</div>
</div>
</div>


           </div>
