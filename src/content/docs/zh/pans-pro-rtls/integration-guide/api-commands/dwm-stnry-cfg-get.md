---
title: "dwm_stnry_cfg_get"
lang: zh
slug: "pans-pro-rtls/integration-guide/api-commands/dwm-stnry-cfg-get"
section: "pans-pro-rtls"
sourceUrl: "https://docs.leapslabs.com/zh-cn/pans-pro-rtls/integration-guide/api-commands/dwm-stnry-cfg-get/"
order: 211
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="dwm-stnry-cfg-get">
<span id="id1"></span><h1>dwm_stnry_cfg_get</h1>
<p>读取标签节点使用的固定模式配置. 即使静态检测被禁用，也可以读取配置（参见 <a class="reference internal" href="/docs/zh/pans-pro-rtls/integration-guide/api-commands/dwm-cfg-tag-set#dwm-cfg-tag-set"><span class="std std-ref">dwm_cfg_tag_set</span></a>）。</p>
<dl class="c function">
<dt class="sig sig-object c" id="c.dwm_stnry_cfg_get">
<span class="n"><span class="pre">uint16_t</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">dwm_stnry_cfg_get</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">dwm_stnry_sensitivity_t</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n"><span class="pre">sensitivity</span></span><span class="sig-paren">)</span><br></dt>
<dd><dl class="field-list simple">
<dt class="field-odd">参数</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>output</strong> – <a class="reference internal" href="/docs/zh/pans-pro-rtls/integration-guide/generic-api-information#pans-statuscode"><span class="std std-ref">状态代码</span></a>, 灵敏度</p></li>
<li><p><strong>sensitivity</strong> – ‘0’ | ‘1’ | ‘2’ (<em>0 - LOW [512 mg] , 1 - NORMAL [2048 mg], 2 - HIGH [4064 mg]</em>)</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<p><strong>C代码示例</strong></p>
<div class="highlight-c notranslate"><div class="highlight"><pre><span></span><span class="n">dwm_stnry_sensitivity_t</span><span class="w"> </span><span class="n">sensitivity</span><span class="p">;</span>
<span class="n">dwm_stnry_cfg_get</span><span class="p">(</span><span class="o">&amp;</span><span class="n">sensitivity</span><span class="p">);</span>
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
<tr class="row-odd"><td><p>0x12</p></td>
<td><p>0x00</p></td>
</tr>
</tbody>
</table>
<p>类型0x12 表示指令 dwm_stnry_cfg_get</p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 17%">
<col style="width: 17%">
<col style="width: 17%">
<col style="width: 17%">
<col style="width: 17%">
<col style="width: 17%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="6"><p>TLV 响应</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>类型</p></td>
<td><p>长度</p></td>
<td><p>价值（参见错误代码）</p></td>
<td><p>类型</p></td>
<td><p>长度</p></td>
<td><p>价值</p></td>
</tr>
<tr class="row-odd"><td><p>0x40</p></td>
<td><p>0x01</p></td>
<td><p>0x00</p></td>
<td><p>0x4A</p></td>
<td><p>0x01</p></td>
<td><p>0x01</p></td>
</tr>
</tbody>
</table>
<div class="line-block">
<div class="line">类型0x40表示 <a class="reference internal" href="/docs/zh/pans-pro-rtls/integration-guide/generic-api-information#pans-statuscode"><span class="std std-ref">状态代码</span></a> 上一条命令的状态码</div>
<div class="line">类型0x4A表示静态灵敏度</div>
</div>
</div>


           </div>
