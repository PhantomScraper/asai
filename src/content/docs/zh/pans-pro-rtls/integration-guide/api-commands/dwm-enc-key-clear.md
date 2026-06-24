---
title: "dwm_enc_key_clear"
lang: zh
slug: "pans-pro-rtls/integration-guide/api-commands/dwm-enc-key-clear"
section: "pans-pro-rtls"
sourceUrl: "https://docs.leapslabs.com/zh-cn/pans-pro-rtls/integration-guide/api-commands/dwm-enc-key-clear/"
order: 178
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="dwm-enc-key-clear">
<span id="id1"></span><h1>dwm_enc_key_clear</h1>
<p>清除加密密钥，并禁用加密选项（如果已启用）。 如果密钥未设置，则不会执行任何操作。</p>
<div class="admonition caution">
<p class="admonition-title">小心</p>
<p>通常，在设置新值时，此调用会写入内部闪存。 因此，它不应该被频繁使用，在最坏的情况下可能需要数百毫秒！它需要重置才能使新配置生效。</p>
</div>
<dl class="c function">
<dt class="sig sig-object c" id="c.dwm_enc_key_clear">
<span class="kt"><span class="pre">int</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">dwm_enc_key_clear</span></span></span><span class="sig-paren">(</span><span class="kt"><span class="pre">void</span></span><span class="sig-paren">)</span><br></dt>
<dd><dl class="field-list simple">
<dt class="field-odd">参数</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>input</strong> – (无)</p></li>
<li><p><strong>output</strong> – <a class="reference internal" href="/docs/zh/pans-pro-rtls/integration-guide/generic-api-information#pans-statuscode"><span class="std std-ref">状态代码</span></a></p></li>
</ul>
</dd>
</dl>
</dd></dl>

<p><strong>C代码示例</strong></p>
<div class="highlight-c notranslate"><div class="highlight"><pre><span></span><span class="kt">int</span><span class="w"> </span><span class="n">rv</span><span class="p">;</span>
<span class="n">rv</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">dwm_enc_key_clear</span><span class="p">();</span>
<span class="k">if</span><span class="w"> </span><span class="p">(</span><span class="n">rv</span><span class="w"> </span><span class="o">==</span><span class="w"> </span><span class="n">DWM_ERR_INTERNAL</span><span class="p">)</span><span class="w"> </span><span class="p">{</span>
<span class="w">  </span><span class="n">printf</span><span class="p">(</span><span class="s">"internal error</span><span class="se">\n</span><span class="s">”);</span>
<span class="p">}</span>
</pre></div>
</div>
<p><strong>SPI/UART 示例</strong></p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 50%">
<col style="width: 50%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="2"><p>TLV 请求</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>类型</p></td>
<td><p>长度</p></td>
</tr>
<tr class="row-odd"><td><p>0X3D</p></td>
<td><p>0x00</p></td>
</tr>
</tbody>
</table>
<p>类型0x3D表示命令 <a class="reference internal" href="#dwm-enc-key-clear"><span class="std std-ref">dwm_enc_key_clear</span></a>。</p>
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
