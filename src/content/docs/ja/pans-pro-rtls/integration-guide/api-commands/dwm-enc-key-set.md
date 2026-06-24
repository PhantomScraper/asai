---
title: "dwm_enc_key_set"
lang: ja
slug: "pans-pro-rtls/integration-guide/api-commands/dwm-enc-key-set"
section: "pans-pro-rtls"
sourceUrl: "https://docs.leapslabs.com/ja/pans-pro-rtls/integration-guide/api-commands/dwm-enc-key-set/"
order: 179
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="dwm-enc-key-set">
<span id="id1"></span><h1>dwm_enc_key_set</h1>
<p>暗号化キーを設定します。キーは不揮発性メモリに保存されます。ゼロだけで構成されるキーは無効とみなされます。キーが設定されている場合、ノードは自動的に暗号化を有効にします。ノードが暗号化されたメッセージを検出し、キーを使用してメッセージを復号できる場合、UWBネットワークを介して暗号化が自動的に有効化されます。暗号化が自動的に有効化されると、BLEオプションは無効になります。暗号化はキーをクリアすることで無効化できます（<a class="reference internal" href="/docs/ja/pans-pro-rtls/integration-guide/api-commands/dwm-enc-key-clear#dwm-enc-key-clear"><span class="std std-ref">dwm_enc_key_clear</span></a> を参照）。</p>
<div class="admonition caution">
<p class="admonition-title">注意</p>
<p>通常、この呼び出しは新しい値を設定するときに内部フラッシュに書き込みます。したがって、頻繁に使用すべきではなく、最悪の場合は数百ミリ秒かかる可能性があります。新しい設定を有効にするにはリセットが必要です。</p>
</div>
<dl class="c function">
<dt class="sig sig-object c" id="c.dwm_enc_key_set">
<span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">dwm_enc_key_set</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">dwm_enc_key_t</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n"><span class="pre">key</span></span><span class="sig-paren">)</span><br></dt>
<dd><dl class="field-list simple">
<dt class="field-odd">パラメータ</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>input</strong> -- キー</p></li>
<li><p><strong>key</strong> -- 16 バイト (<em>暗号化キー</em>)</p></li>
<li><p><strong>output</strong> -- <a class="reference internal" href="/docs/ja/pans-pro-rtls/integration-guide/generic-api-information#pans-statuscode"><span class="std std-ref">ステータスコード</span></a></p></li>
</ul>
</dd>
</dl>
</dd></dl>

<p><strong>Cコード例</strong></p>
<div class="highlight-c notranslate"><div class="highlight"><pre><span></span><span class="n">dwm_enc_key_t</span><span class="w"> </span><span class="n">key</span><span class="p">;</span>
<span class="n">key</span><span class="p">.</span><span class="n">byte</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mh">0x00</span><span class="p">;</span>
<span class="n">key</span><span class="p">.</span><span class="n">byte</span><span class="p">[</span><span class="mi">1</span><span class="p">]</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mh">0x11</span><span class="p">;</span>
<span class="n">key</span><span class="p">.</span><span class="n">byte</span><span class="p">[</span><span class="mi">2</span><span class="p">]</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mh">0x22</span><span class="p">;</span>
<span class="cm">/* ... */</span>
<span class="n">key</span><span class="p">.</span><span class="n">byte</span><span class="p">[</span><span class="mi">15</span><span class="p">]</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mh">0xFF</span><span class="p">;</span>
<span class="n">dwm_enc_key_set</span><span class="p">(</span><span class="o">&amp;</span><span class="n">key</span><span class="p">)</span>
</pre></div>
</div>
<p><strong>SPI/UART 例</strong></p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 33%">
<col style="width: 33%">
<col style="width: 33%">
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
<tr class="row-odd"><td><p>0x3C</p></td>
<td><p>0x10</p></td>
<td><p>0x00 0x11 0x22
0x33 0x44 0x55
0x66 0x77 0x88
0x99 0xAA 0xBB
0xCC 0xDD 0xEE
0xFF</p></td>
</tr>
</tbody>
</table>
<p>タイプ 0x3C はコマンド <a class="reference internal" href="#dwm-enc-key-set"><span class="std std-ref">dwm_enc_key_set</span></a> を意味します</p>
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
