---
title: "dwm_enc_key_set"
lang: zh
slug: "pans-pro-rtls/integration-guide/api-commands/dwm-enc-key-set"
section: "pans-pro-rtls"
sourceUrl: "https://docs.leapslabs.com/zh-cn/pans-pro-rtls/integration-guide/api-commands/dwm-enc-key-set/"
order: 179
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="dwm-enc-key-set">
<span id="id1"></span><h1>dwm_enc_key_set</h1>
<p>设置加密密钥。 密钥存储在非易失性存储器中。 仅由 0 组成的密钥将被视为无效。 如果设置了密钥，节点将自动启用加密。 当节点检测到加密信息并能用密钥解密信息时，将通过 UWB 网络触发自动启用加密。 自动启用加密后，BLE 选项将被禁用。 可以通过清除密钥来禁用加密（参见 <a class="reference internal" href="/docs/zh/pans-pro-rtls/integration-guide/api-commands/dwm-enc-key-clear#dwm-enc-key-clear"><span class="std std-ref">dwm_enc_key_clear</span></a>）。</p>
<div class="admonition caution">
<p class="admonition-title">小心</p>
<p>通常，在设置新值时，这个调用会写入内部闪存。 因此，此调用不应频繁使用，最坏情况下可能需要数百毫秒！新的配置需要重置才能生效。</p>
</div>
<dl class="c function">
<dt class="sig sig-object c" id="c.dwm_enc_key_set">
<span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">dwm_enc_key_set</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">dwm_enc_key_t</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n"><span class="pre">key</span></span><span class="sig-paren">)</span><br></dt>
<dd><dl class="field-list simple">
<dt class="field-odd">参数</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>input</strong> – 密钥</p></li>
<li><p><strong>key</strong> – 16字节 (<em>加密密钥</em>)</p></li>
<li><p><strong>output</strong> – <a class="reference internal" href="/docs/zh/pans-pro-rtls/integration-guide/generic-api-information#pans-statuscode"><span class="std std-ref">状态代码</span></a></p></li>
</ul>
</dd>
</dl>
</dd></dl>

<p><strong>C代码示例</strong></p>
<div class="highlight-c notranslate"><div class="highlight"><pre><span></span><span class="n">dwm_enc_key_t</span><span class="w"> </span><span class="n">key</span><span class="p">;</span>
<span class="n">key</span><span class="p">.</span><span class="n">byte</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mh">0x00</span><span class="p">;</span>
<span class="n">key</span><span class="p">.</span><span class="n">byte</span><span class="p">[</span><span class="mi">1</span><span class="p">]</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mh">0x11</span><span class="p">;</span>
<span class="n">key</span><span class="p">.</span><span class="n">byte</span><span class="p">[</span><span class="mi">2</span><span class="p">]</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mh">0x22</span><span class="p">;</span>
<span class="cm">/* ... */</span>
<span class="n">key</span><span class="p">.</span><span class="n">byte</span><span class="p">[</span><span class="mi">15</span><span class="p">]</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mh">0xFF</span><span class="p">;</span>
<span class="n">dwm_enc_key_set</span><span class="p">(</span><span class="o">&amp;</span><span class="n">key</span><span class="p">)</span>
</pre></div>
</div>
<p><strong>SPI/UART 示例</strong></p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 33%">
<col style="width: 33%">
<col style="width: 33%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="3"><p>TLV 请求</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>类型</p></td>
<td><p>长度</p></td>
<td><p>价值</p></td>
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
<p>类型 0x3C 表示命令 <a class="reference internal" href="#dwm-enc-key-set"><span class="std std-ref">dwm_enc_key_set</span></a></p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 33%">
<col style="width: 33%">
<col style="width: 33%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="3"><p>TLV 响应</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>类型</p></td>
<td><p>长度</p></td>
<td><p>价值（参见错误代码）</p></td>
</tr>
<tr class="row-odd"><td><p>0x40</p></td>
<td><p>0x01</p></td>
<td><p>0x00</p></td>
</tr>
</tbody>
</table>
<p>类型0x40表示 <a class="reference internal" href="/docs/zh/pans-pro-rtls/integration-guide/generic-api-information#pans-statuscode"><span class="std std-ref">状态代码</span></a> 上一条命令的状态码</p>
</div>


           </div>
