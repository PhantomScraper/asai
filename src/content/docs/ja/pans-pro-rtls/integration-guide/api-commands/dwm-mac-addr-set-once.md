---
title: "dwm_mac_addr_set_once"
lang: ja
slug: "pans-pro-rtls/integration-guide/api-commands/dwm-mac-addr-set-once"
section: "pans-pro-rtls"
sourceUrl: "https://docs.leapslabs.com/ja/pans-pro-rtls/integration-guide/api-commands/dwm-mac-addr-set-once/"
order: 199
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="dwm-mac-addr-set-once">
<span id="id1"></span><h1>dwm_mac_addr_set_once</h1>
<p>MACアドレスリストをOTPメモリに書き込みます。慎重に使用してください。書き込み後は値を変更できません。これは、UWB、BLE、Ethernet、またはWi-Fiインターフェースで使用するデバイスのMACアドレスプールを提供するために、製造段階で使用することを目的としています。現在、MAC アドレスのリストは次のようにさまざまなインターフェイスに割り当てられています:</p>
<ul class="simple">
<li><p>MAC アドレス 0 が UWB インターフェイスに割り当てられます。最下位 2 バイトは 0x0000 または 0xFFFF と等しくであってはなりません。</p></li>
<li><p>MAC アドレス 1 が BLE インターフェイスに割り当てられます。このアドレスはパブリック BLE アドレスとして使用されます。</p></li>
<li><p>MAC アドレス 2 はイーサネット、MAC アドレス 3 は Wi-Fi インターフェースにそれぞれ割り当てられます。アドレスは、LAA/UAA および U/I ビットに関して EUI-48 形式である必要があります。</p></li>
</ul>
<dl class="c function">
<dt class="sig sig-object c" id="c.dwm_mac_addr_set_once">
<span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">dwm_mac_addr_set_once</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">dwm_mac_addr_t</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n"><span class="pre">addr</span></span>, <span class="n"><span class="pre">uint8_t</span></span><span class="w"> </span><span class="n"><span class="pre">count</span></span><span class="sig-paren">)</span><br></dt>
<dd><dl class="field-list simple">
<dt class="field-odd">パラメータ</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>input</strong> -- mac_addr_0, [mac_addr_1], [mac_addr_2], [mac_addr_3]</p></li>
<li><p><strong>mac_addr_0</strong> -- 48 ビット値 (<em>リトルエンディアンの UWB MAC アドレス</em>)</p></li>
<li><p><strong>mac_addr_1</strong> -- 48 ビット値 (<em>少しの BLE MAC アドレス)エンディアン</em>)</p></li>
<li><p><strong>mac_addr_2</strong> -- 48 ビット値 (<em>リトルエンディアンのイーサネット MAC アドレス</em>)</p></li>
<li><p><strong>mac_addr_3</strong> -- 48 ビット値 (<em>リトルエンディアンの WIFI MAC アドレス</em>)</p></li>
<li><p><strong>output:</strong> -- <a class="reference internal" href="/docs/ja/pans-pro-rtls/integration-guide/generic-api-information#pans-statuscode"><span class="std std-ref">ステータスコード</span></a></p></li>
</ul>
</dd>
</dl>
</dd></dl>

<p><strong>Cコード例</strong></p>
<div class="highlight-c notranslate"><div class="highlight"><pre><span></span><span class="n">dwm_mac_addr_list_t</span><span class="w"> </span><span class="n">mac_addr_list</span><span class="p">;</span>
<span class="n">dwm_mac_addr_get</span><span class="p">(</span><span class="o">&amp;</span><span class="n">mac_addr_list</span><span class="p">);</span>
<span class="n">memcpy</span><span class="p">(</span><span class="n">mac_addr_list</span><span class="p">.</span><span class="n">mac</span><span class="p">[</span><span class="mi">0</span><span class="p">],</span><span class="w"> </span><span class="p">(</span><span class="kt">uint8_t</span><span class="p">[</span><span class="n">DWM_MAC_ADDR_LEN</span><span class="p">]){</span><span class="mh">0xaa</span><span class="p">,</span><span class="w"> </span><span class="mh">0xbb</span><span class="p">,</span><span class="w"> </span><span class="mh">0xcc</span><span class="p">,</span><span class="w"> </span><span class="mh">0xdd</span><span class="p">,</span><span class="w"> </span><span class="mh">0xee</span><span class="p">,</span><span class="w"> </span><span class="mh">0xff</span><span class="p">},</span><span class="w"> </span><span class="n">DWM_MAC_ADDR_LEN</span><span class="p">);</span>
<span class="nl">rv</span><span class="p">:</span><span class="w"> </span><span class="n">dwm_mac_addr_set</span><span class="p">(</span><span class="o">&amp;</span><span class="n">mac_addr_list</span><span class="p">);</span>
<span class="k">if</span><span class="w"> </span><span class="p">(</span><span class="n">rv</span><span class="w"> </span><span class="o">!=</span><span class="w"> </span><span class="n">DWM_OK</span><span class="p">)</span><span class="w"> </span><span class="p">{</span>
<span class="w">  </span><span class="n">printf</span><span class="p">(</span><span class="s">"can't set MAC address list, error %d</span><span class="se">\n</span><span class="s">"</span><span class="p">,</span><span class="w"> </span><span class="n">rv</span><span class="p">);</span>
<span class="p">}</span>
</pre></div>
</div>
<p><strong>SPI/UART 例</strong></p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 22%">
<col style="width: 22%">
<col style="width: 56%">
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
<tr class="row-odd"><td rowspan="2"><p>0x82</p></td>
<td rowspan="2"><p>0x18</p></td>
<td><div class="line-block">
<div class="line">(バイト 0-5) リトルエンディアンの MAC アドレス 0</div>
<div class="line">(バイト 6-11) リトルエンディアンの MAC アドレス 1</div>
<div class="line">(バイト 12-17) リトルエンディアンの MAC アドレス 2</div>
<div class="line">(バイト 18-23) リトルエンディアンの MAC アドレス 3</div>
</div>
</td>
</tr>
<tr class="row-even"><td><p>...</p></td>
</tr>
</tbody>
</table>
<p>タイプ 0x82 (130 dec) はコマンド dwm_mac_addr_set_once を意味します</p>
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
<p>タイプ0x40は、直前のコマンドの <a class="reference internal" href="/docs/ja/pans-pro-rtls/integration-guide/generic-api-information#pans-statuscode"><span class="std std-ref">ステータスコード</span></a> を意味する</p>
</div>


           </div>
