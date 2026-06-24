---
title: "dwm_mac_addr_set"
lang: ja
slug: "pans-pro-rtls/integration-guide/api-commands/dwm-mac-addr-set"
section: "pans-pro-rtls"
sourceUrl: "https://docs.leapslabs.com/ja/pans-pro-rtls/integration-guide/api-commands/dwm-mac-addr-set/"
order: 200
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="dwm-mac-addr-set">
<span id="id1"></span><h1>dwm_mac_addr_set</h1>
<p>BLE、UWB、イーサネット、Wi-FiインターフェースのMACアドレスを設定し、有効にするにはリセットが必要です。内部の不揮発性メモリを書き込むため、頻繁に使用するべきではありません。デフォルトのMACアドレスを使用するには、工場出荷時のリセット（<em>dwm_factory_reset</em>）が必要です。UWB MAC アドレスの最下位 2 バイトが 0x0000 または 0xFFFF であってはならない。BLEアドレスには、ランダムBLEアドレスまたはパブリックBLEアドレスを使用できます。イーサネットおよびWi-FiアドレスはEUI-48形式を尊重し、U/Iビットはそれに応じて設定する必要があります。</p>
<dl class="c function">
<dt class="sig sig-object c" id="c.dwm_mac_addr_set">
<span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">dwm_mac_addr_set</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">dwm_mac_addr_type_t</span></span><span class="w"> </span><span class="n"><span class="pre">type</span></span>, <span class="n"><span class="pre">dwm_mac_addr_t</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n"><span class="pre">addr</span></span><span class="sig-paren">)</span><br></dt>
<dd><dl class="field-list simple">
<dt class="field-odd">パラメータ</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>input</strong> -- addr_type, addr_value</p></li>
<li><p><strong>addr_type</strong> -- 8ビット整数（<em>0=UWBアドレス、1=BLEランダムアドレス、2=BLEパブリックアドレス、3=ETHアドレス、4=WIFIアドレス。</em>）</p></li>
<li><p><strong>addr_value</strong> -- 6バイト(<em>6バイト長のMACアドレス</em>)</p></li>
<li><p><strong>output:</strong> -- <a class="reference internal" href="/docs/ja/pans-pro-rtls/integration-guide/generic-api-information#pans-statuscode"><span class="std std-ref">ステータスコード</span></a></p></li>
</ul>
</dd>
</dl>
</dd></dl>

<p><strong>Cコード例</strong></p>
<div class="highlight-c notranslate"><div class="highlight"><pre><span></span><span class="n">dwm_mac_addr_t</span><span class="w"> </span><span class="n">addr</span><span class="p">;</span>
<span class="n">addr</span><span class="p">.</span><span class="n">bytes</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span><span class="o">:</span><span class="w"> </span><span class="mh">0xAA</span><span class="p">;</span>
<span class="n">addr</span><span class="p">.</span><span class="n">bytes</span><span class="p">[</span><span class="mi">1</span><span class="p">]</span><span class="o">:</span><span class="w"> </span><span class="mh">0xBB</span><span class="p">;</span>
<span class="n">addr</span><span class="p">.</span><span class="n">bytes</span><span class="p">[</span><span class="mi">2</span><span class="p">]</span><span class="o">:</span><span class="w"> </span><span class="mh">0xCC</span><span class="p">;</span>
<span class="n">addr</span><span class="p">.</span><span class="n">bytes</span><span class="p">[</span><span class="mi">3</span><span class="p">]</span><span class="o">:</span><span class="w"> </span><span class="mh">0xDD</span><span class="p">;</span>
<span class="n">addr</span><span class="p">.</span><span class="n">bytes</span><span class="p">[</span><span class="mi">4</span><span class="p">]</span><span class="o">:</span><span class="w"> </span><span class="mh">0xEE</span><span class="p">;</span>
<span class="n">addr</span><span class="p">.</span><span class="n">bytes</span><span class="p">[</span><span class="mi">5</span><span class="p">]</span><span class="o">:</span><span class="w"> </span><span class="mh">0xFF</span><span class="p">;</span>
<span class="kt">int</span><span class="w"> </span><span class="n">rv</span><span class="o">:</span><span class="w"> </span><span class="n">dwm_mac_addr_set</span><span class="p">(</span><span class="n">NODE_ADDR_TYPE_UWB</span><span class="p">,</span><span class="w"> </span><span class="o">&amp;</span><span class="n">addr</span><span class="p">);</span>
<span class="k">if</span><span class="w"> </span><span class="p">(</span><span class="n">rv</span><span class="w"> </span><span class="o">!=</span><span class="w"> </span><span class="n">DWM_OK</span><span class="p">)</span><span class="w"> </span><span class="p">{</span>
<span class="w">  </span><span class="n">printf</span><span class="p">(</span><span class="s">"can't set node address, error %d</span><span class="se">\n</span><span class="s">"</span><span class="p">,</span><span class="w"> </span><span class="n">rv</span><span class="p">);</span>
<span class="p">}</span>
</pre></div>
</div>
<p><strong>SPI/UART 例</strong></p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 26%">
<col style="width: 26%">
<col style="width: 48%">
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
<tr class="row-odd"><td rowspan="2"><p>0x2D</p></td>
<td rowspan="2"><p>0x07</p></td>
<td><div class="line-block">
<div class="line">バイト0:MACアドレスタイプ</div>
<div class="line">バイト1-6: リトルエンディアンのMACアドレス</div>
</div>
</td>
</tr>
<tr class="row-even"><td><p>0x00 0xEF 0xCD 0xAB
0x56 0x34 0x12</p></td>
</tr>
</tbody>
</table>
<p>タイプ 0x2D (45 dec) はコマンド dwm_mac_addr_set を意味する</p>
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
