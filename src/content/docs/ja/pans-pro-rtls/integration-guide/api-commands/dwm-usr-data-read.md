---
title: "dwm_usr_data_read"
lang: ja
slug: "pans-pro-rtls/integration-guide/api-commands/dwm-usr-data-read"
section: "pans-pro-rtls"
sourceUrl: "https://docs.leapslabs.com/ja/pans-pro-rtls/integration-guide/api-commands/dwm-usr-data-read/"
order: 216
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="dwm-usr-data-read">
<span id="id1"></span><h1>dwm_usr_data_read</h1>
<p>ノードからユーザデータを読み込みます。UWB で受信した新しいデータはステータスに専用のフラグを設定し (<a class="reference internal" href="/docs/ja/pans-pro-rtls/integration-guide/api-commands/dwm-status-get#dwm-status-get"><span class="std std-ref">dwm_status_get</span></a> を参照)、ユーザアプリケーションにイベントを発生させます (<a class="reference internal" href="/docs/ja/pans-pro-rtls/integration-guide/api-commands/dwm-evt-listener-register#dwm-evt-listener-register"><span class="std std-ref">dwm_evt_listener_register</span></a> を参照)。</p>
<dl class="c function">
<dt class="sig sig-object c" id="c.dwm_usr_data_read">
<span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">dwm_usr_data_read</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">uint8_t</span></span><span class="p"><span class="pre">*</span></span>, <span class="n"><span class="pre">uint8_t</span></span><span class="p"><span class="pre">*</span></span><span class="sig-paren">)</span><br></dt>
<dd><dl class="field-list simple">
<dt class="field-odd">パラメータ</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>input</strong> -- (<em>なし</em>)</p></li>
<li><p><strong>output</strong> -- <a class="reference internal" href="/docs/ja/pans-pro-rtls/integration-guide/generic-api-information#pans-statuscode"><span class="std std-ref">ステータスコード</span></a>, データ, len</p></li>
<li><p><strong>data</strong> -- 1-34バイト（<em>ユーザーデータ</em>）</p></li>
<li><p><strong>len</strong> -- 1バイト (<em>データの長さ</em>)</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<p><strong>Cコード例</strong></p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">uint8_t data[DWM_USR_DATA_LEN_MAX];</span>
<span class="go">uint8_t len;</span>
<span class="go">len = DWM_USR_DATA_LEN_MAX;</span>
<span class="go">dwm_usr_data_read(data, &amp;len);</span>
</pre></div>
</div>
<p><strong>SPI/UART 例</strong></p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 50%">
<col style="width: 50%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="2"><p>TLV 要求</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>タイプ</p></td>
<td><p>長さ</p></td>
</tr>
<tr class="row-odd"><td><p>0x19</p></td>
<td><p>0x00</p></td>
</tr>
</tbody>
</table>
<p>タイプ 0x19 は、コマンド dwm_usr_data_read を意味する</p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 14%">
<col style="width: 14%">
<col style="width: 14%">
<col style="width: 14%">
<col style="width: 14%">
<col style="width: 31%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="6"><p>TLV 応答</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>タイプ</p></td>
<td><p>長さ</p></td>
<td><p>値（エラーコードを参照）</p></td>
<td><p>タイプ</p></td>
<td><p>長さ</p></td>
<td><p>値</p></td>
</tr>
<tr class="row-odd"><td rowspan="2"><p>0x40</p></td>
<td rowspan="2"><p>0x01</p></td>
<td rowspan="2"><p>0x00</p></td>
<td rowspan="2"><p>0x4B</p></td>
<td rowspan="2"><p>0x22</p></td>
<td><p>バイト 0 - N: ユーザーデータ（1 &lt;= N &lt;= 33）</p></td>
</tr>
<tr class="row-even"><td><p>0x01 0x02
0x03 …
0x23 0x22</p></td>
</tr>
</tbody>
</table>
<p>タイプ0x4Bはユーザーデータを意味する</p>
</div>


           </div>
