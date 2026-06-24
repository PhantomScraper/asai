---
title: "dwm_mac_addr_get"
lang: ja
slug: "pans-pro-rtls/integration-guide/api-commands/dwm-mac-addr-get"
section: "pans-pro-rtls"
sourceUrl: "https://docs.leapslabs.com/ja/pans-pro-rtls/integration-guide/api-commands/dwm-mac-addr-get/"
order: 198
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="dwm-mac-addr-get">
<span id="id1"></span><h1>dwm_mac_addr_get</h1>
<p>デバイスが使用するMACアドレスリストを取得します。デバイスは、ユーザーが指定したアドレスまたはデフォルトのアドレスを使用します。各インターフェースのデフォルトMACアドレスは、<em>dwm_mac_addr_set_once</em> を呼び出すことで1回のみ変更できます。このMACアドレスはOTPメモリに書き込まれ、新しいデフォルトMACアドレスとなります。ユーザーは <em>dwm_mac_addr_set</em> を呼び出すことでカスタムMACアドレスを設定できます。ユーザーが変更したデフォルトMACアドレスは、工場出荷時設定へのリセット（<em>dwm_factory_reset</em> を参照）によって復元できます。デバイスは、リスト内の MAC アドレスから特定のインターフェイスへの固定マッピングを次のように使用します:</p>
<ol class="arabic simple">
<li><p>UWB</p></li>
<li><p>BLE</p></li>
<li><p>イーサネット</p></li>
<li><p>无线网络</p></li>
</ol>
<p>BLE アドレスには、ランダム BLE アドレスまたはパブリック BLE アドレスを指定できます。特定のインターフェイスがサポートされていない場合、リスト内の対応する MAC アドレスは空になります。</p>
<dl class="c function">
<dt class="sig sig-object c" id="c.dwm_mac_addr_get">
<span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">dwm_mac_addr_get</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">dwm_mac_addr_list_t</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n"><span class="pre">mac_addr_list</span></span><span class="sig-paren">)</span><br></dt>
<dd><dl class="field-list simple">
<dt class="field-odd">パラメータ</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>output</strong> -- <a class="reference internal" href="/docs/ja/pans-pro-rtls/integration-guide/generic-api-information#pans-statuscode"><span class="std std-ref">ステータスコード</span></a>, type_0, type_1, type_2, type_3, mac_addr_0, mac_addr_1, mac_addr_2, mac_addr_3</p></li>
<li><p><strong>type_N</strong> -- ステータス、フラグ (<em>リストのインデックス 0 にある MAC アドレスを説明するタイプ</em>)</p></li>
<li><p><strong>status</strong> -- 2 ビット (* MAC アドレスのステータス: MAC_ADDR_EMPTY = 0、MAC_ADDR_DEFAULT = 1、MAC_ADDR_USER_SPECIFIED = 2、MAC_ADDR_MUTABLE_DEFAULT = 3*)</p></li>
<li><p><strong>flags</strong> -- 6 ビット (<em>アドレスが PUBLIC_BLE_ADDR の場合、ビット 0 が設定され、残りのビットは将来の使用のために予約されています</em>)</p></li>
<li><p><strong>mac_addr_N</strong> -- 48 ビット値 (<em>リトルエンディアン</em>)</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<p><strong>Cコード例</strong></p>
<div class="highlight-c notranslate"><div class="highlight"><pre><span></span><span class="n">dwm_mac_addr_list_t</span><span class="w"> </span><span class="n">mac_addr_list</span><span class="p">;</span>
<span class="nl">rv</span><span class="p">:</span><span class="w"> </span><span class="n">dwm_mac_addr_get</span><span class="p">(</span><span class="o">&amp;</span><span class="n">mac_addr_list</span><span class="p">);</span>
<span class="k">if</span><span class="w"> </span><span class="p">(</span><span class="n">rv</span><span class="w"> </span><span class="o">==</span><span class="w"> </span><span class="n">DWM_OK</span><span class="p">)</span><span class="w"> </span><span class="p">{</span>
<span class="w">  </span><span class="n">printf</span><span class="p">(</span><span class="s">"UWB MAC 0x%02x%02x%02x%02x%02x%02x status=x%02x</span><span class="se">\n</span><span class="s">"</span><span class="p">,</span>
<span class="w">  </span><span class="n">mac_addr_list</span><span class="p">.</span><span class="n">mac</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="mi">0</span><span class="p">],</span>
<span class="w">  </span><span class="n">mac_addr_list</span><span class="p">.</span><span class="n">mac</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="mi">1</span><span class="p">],</span>
<span class="w">  </span><span class="n">mac_addr_list</span><span class="p">.</span><span class="n">mac</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="mi">2</span><span class="p">],</span>
<span class="w">  </span><span class="n">mac_addr_list</span><span class="p">.</span><span class="n">mac</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="mi">3</span><span class="p">],</span>
<span class="w">  </span><span class="n">mac_addr_list</span><span class="p">.</span><span class="n">mac</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="mi">4</span><span class="p">],</span>
<span class="w">  </span><span class="n">mac_addr_list</span><span class="p">.</span><span class="n">mac</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="mi">5</span><span class="p">],</span>
<span class="w">  </span><span class="n">mac_addr_list</span><span class="p">.</span><span class="n">type</span><span class="p">[</span><span class="mi">0</span><span class="p">].</span><span class="n">status</span><span class="p">);</span>
<span class="p">}</span><span class="w"> </span><span class="k">else</span><span class="w"> </span><span class="p">{</span>
<span class="w">  </span><span class="n">printf</span><span class="p">(</span><span class="s">"can't get MAC address list, error %d</span><span class="se">\n</span><span class="s">"</span><span class="p">,</span><span class="w"> </span><span class="n">rv</span><span class="p">);</span>
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
<tr class="row-odd"><td><p>0x83</p></td>
<td><p>0x00</p></td>
</tr>
</tbody>
</table>
<p>タイプ 0x83 (131 dec) はコマンドを意味しますdwm_mac_addr_get</p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 10%">
<col style="width: 10%">
<col style="width: 10%">
<col style="width: 10%">
<col style="width: 10%">
<col style="width: 51%">
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
<td rowspan="2"><p>0xC1</p></td>
<td rowspan="2"><p>0x18</p></td>
<td><div class="line-block">
<div class="line">(バイト 0 ～ 4) リスト内の MAC アドレスの種類</div>
</div>
<div class="line-block">
<div class="line">(バイト 5-10) リトルエンディアンの MAC アドレス 0</div>
<div class="line">(バイト 11-16) リトルエンディアンの MAC アドレス 1</div>
<div class="line">(バイト 17-22) リトルエンディアンの MAC アドレス 2</div>
<div class="line">(バイト 23-28) リトルエンディアンの MAC アドレス 3</div>
</div>
</td>
</tr>
<tr class="row-even"><td><p>...</p></td>
</tr>
</tbody>
</table>
<div class="line-block">
<div class="line">タイプ0x40は、直前のコマンドの <a class="reference internal" href="/docs/ja/pans-pro-rtls/integration-guide/generic-api-information#pans-statuscode"><span class="std std-ref">ステータスコード</span></a> を意味する</div>
<div class="line">タイプ 0xC1(193 dec) は MAC アドレスリストを意味します</div>
</div>
<p><strong>MAC アドレス フラグのエンコーディング</strong></p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 11%">
<col style="width: 11%">
<col style="width: 11%">
<col style="width: 11%">
<col style="width: 11%">
<col style="width: 11%">
<col style="width: 11%">
<col style="width: 11%">
<col style="width: 11%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="9"><p>MAC アドレスリストのフラグ</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td colspan="2"><p>バイト 0</p></td>
<td colspan="3"><p>バイト1</p></td>
<td colspan="2"><p>バイト2</p></td>
<td colspan="2"><p>バイト3</p></td>
</tr>
<tr class="row-odd"><td><p>ビット 2 ～ 7</p></td>
<td><p>ビット0～1</p></td>
<td><p>ビット 11 ～ 15</p></td>
<td><p>ビット10</p></td>
<td><p>ビット 8 ～ 9</p></td>
<td><p>ビット 18 ～ 23</p></td>
<td><p>ビット 16 ～ 17</p></td>
<td><p>ビット 26-31</p></td>
<td><p>ビット 24-25</p></td>
</tr>
<tr class="row-even"><td><p>R</p></td>
<td><p>S_0</p></td>
<td><p>R</p></td>
<td><p>P_1</p></td>
<td><p>S_1</p></td>
<td><p>R</p></td>
<td><p>S_2</p></td>
<td><p>R</p></td>
<td><p>S_3</p></td>
</tr>
</tbody>
</table>
<p>R は将来の使用のために予約済みです。S_0、S_1、S_2、S_3 は MAC アドレスのステータスを示します。ステータスには次の値を指定できます。</p>
<blockquote>
<div><ul class="simple">
<li><p>0 - 空の MAC アドレス</p></li>
<li><p>1 - OTP メモリからのデフォルトの MAC アドレス。</p></li>
<li><p>2 - ユーザーが指定した MAC アドレス</p></li>
<li><p>3 - 変更可能なデフォルト MAC アドレスは、<em>dwm_mac_addr_set_once</em> を使用して 1 回だけ書き換えることができます。</p></li>
</ul>
</div></blockquote>
<p>BLE アドレスがパブリック BLE アドレスの場合、P_1 が設定されます。 BLE MAC アドレスがランダムな場合、フラグはクリアされます。 BLE アドレス タイプの詳細については、BLE 仕様を参照してください。</p>
</div>


           </div>
