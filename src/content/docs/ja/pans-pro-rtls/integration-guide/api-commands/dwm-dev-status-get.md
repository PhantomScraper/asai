---
title: "dwm_dev_status_get"
lang: ja
slug: "pans-pro-rtls/integration-guide/api-commands/dwm-dev-status-get"
section: "pans-pro-rtls"
sourceUrl: "https://docs.leapslabs.com/ja/pans-pro-rtls/integration-guide/api-commands/dwm-dev-status-get/"
order: 177
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="dwm-dev-status-get">
<span id="id1"></span><h1>dwm_dev_status_get</h1>
<p>このコマンドはデバイスのステータスを読み取ります。ユーザー アプリケーション (オンチップ ライブラリ) で使用する場合、ADC ペリフェラルの使用が可能になるため、バッテリー レベルは使用できません。</p>
<dl class="c function">
<dt class="sig sig-object c" id="c.dwm_dev_status_get">
<span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">dwm_dev_status_get</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">dwm_mac_addr_list_t</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n"><span class="pre">mac_addr_list</span></span><span class="sig-paren">)</span><br></dt>
<dd><dl class="field-list simple">
<dt class="field-odd">パラメータ</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>input</strong> -- (<em>なし</em>)</p></li>
<li><p><strong>output</strong> -- <a class="reference internal" href="/docs/ja/pans-pro-rtls/integration-guide/generic-api-information#pans-statuscode"><span class="std std-ref">ステータスコード</span></a>、稼働時間、バッテリーレベル、温度</p></li>
<li><p><strong>uptime</strong> -- 32 ビット符号なし整数 (<em>秒単位の稼働時間</em>)</p></li>
<li><p><strong>battery_level</strong> -- 8 ビット符号なし整数 (<em>バッテリー残量パーセント、ユーザー アプリケーション ライブラリでは利用できません</em>)</p></li>
<li><p><strong>temperature</strong> -- 16 ビット整数 (<em>温度 (°C)</em>)</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<p><strong>Cコード例</strong></p>
<div class="highlight-c notranslate"><div class="highlight"><pre><span></span><span class="n">dwm_dev_status_t</span><span class="w"> </span><span class="n">status</span><span class="p">;</span>
<span class="kt">int</span><span class="w"> </span><span class="n">rv</span><span class="p">;</span>
<span class="k">if</span><span class="w"> </span><span class="p">(</span><span class="n">rv</span><span class="w"> </span><span class="o">==</span><span class="w"> </span><span class="n">DWM_OK</span><span class="p">)</span><span class="w"> </span><span class="p">{</span>
<span class="w">   </span><span class="n">printf</span><span class="p">(</span><span class="s">"uptime=%lu</span><span class="se">\n</span><span class="s">"</span><span class="p">,</span><span class="w"> </span><span class="n">status</span><span class="p">.</span><span class="n">uptime</span><span class="p">);</span>
<span class="w">   </span><span class="n">printf</span><span class="p">(</span><span class="s">"temperature=%d</span><span class="se">\n</span><span class="s">"</span><span class="p">,</span><span class="w"> </span><span class="n">status</span><span class="p">.</span><span class="n">temperature</span><span class="p">);</span>
<span class="p">}</span><span class="w"> </span><span class="k">else</span><span class="w"> </span><span class="p">{</span>
<span class="w">   </span><span class="n">printf</span><span class="p">(</span><span class="s">"can't read device status, error %d</span><span class="se">\n</span><span class="s">"</span><span class="p">,</span><span class="w"> </span><span class="n">rv</span><span class="p">);</span>
<span class="p">}</span>
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
<tr class="row-odd"><td><p>0x25</p></td>
<td><p>0x00</p></td>
</tr>
</tbody>
</table>
<p>タイプ 0x25 (10 進数 37) はコマンド <a class="reference internal" href="#dwm-dev-status-get"><span class="std std-ref">dwm_dev_status_get</span></a> を意味します。</p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 13%">
<col style="width: 13%">
<col style="width: 13%">
<col style="width: 13%">
<col style="width: 13%">
<col style="width: 33%">
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
<td rowspan="2"><p>0x59</p></td>
<td rowspan="2"><p>0x08</p></td>
<td><div class="line-block">
<div class="line">アップタイム（バイト 0～3）</div>
<div class="line">バッテリーレベル（バイト 4）</div>
<div class="line">予約済み（バイト 5）</div>
<div class="line">温度（バイト 6～7）</div>
</div>
</td>
</tr>
<tr class="row-even"><td><p>0x9d
0x16
0x00
0x00
0x64
0x00
0x21
0x00</p></td>
</tr>
</tbody>
</table>
<div class="line-block">
<div class="line">タイプ 0x59 (10 進数 89) はデバイスのステータスを意味します</div>
<div class="line">タイプ0x40は、直前のコマンドの <a class="reference internal" href="/docs/ja/pans-pro-rtls/integration-guide/generic-api-information#pans-statuscode"><span class="std std-ref">ステータスコード</span></a> を意味する</div>
</div>
</div>


           </div>
