---
title: "dwm_stnry_cfg_set"
lang: zh
slug: "pans-pro-rtls/integration-guide/api-commands/dwm-stnry-cfg-set"
section: "pans-pro-rtls"
sourceUrl: "https://docs.leapslabs.com/zh-cn/pans-pro-rtls/integration-guide/api-commands/dwm-stnry-cfg-set/"
order: 212
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="dwm-stnry-cfg-set">
<span id="id1"></span><h1>dwm_stnry_cfg_set</h1>
<p>写入标签节点使用的静态模式配置。 即使静态检测被禁用，也会保存此配置（参见 <a class="reference internal" href="/docs/zh/pans-pro-rtls/integration-guide/api-commands/dwm-cfg-tag-set#dwm-cfg-tag-set"><span class="std std-ref">dwm_cfg_tag_set</span></a>）。 该配置会写入内部非易失性存储器，因此应谨慎使用。 启用静态模式后，新的灵敏度设置立即生效。 默认灵敏度为 “高”。</p>
<dl class="c function">
<dt class="sig sig-object c" id="c.dwm_stnry_cfg_set">
<span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">dwm_stnry_cfg_set</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">uint16_t</span></span><span class="sig-paren">)</span><br></dt>
<dd><dl class="field-list simple">
<dt class="field-odd">参数</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>input</strong> – 灵敏度</p></li>
<li><p><strong>sensitivity</strong> – ‘0’ | ‘1’ | ‘2’ (<em>0 - LOW [4064 mg] , 1 - NORMAL [2048 mg], 2 - HIGH [512 mg]</em>)</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<p><strong>C代码示例</strong></p>
<div class="highlight-c notranslate"><div class="highlight"><pre><span></span><span class="n">dwm_stnry_cfg_set</span><span class="p">(</span><span class="n">DWM_STNRY_SENSITIVITY_HIGH</span><span class="p">);</span>
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
<tr class="row-odd"><td><p>0x11</p></td>
<td><p>0x01</p></td>
<td><p>0x01</p></td>
</tr>
</tbody>
</table>
<p>类型 0x11 表示命令 dwm_stnry_cfg_set</p>
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
<div class="line-block">
<div class="line">类型0x40表示 <a class="reference internal" href="/docs/zh/pans-pro-rtls/integration-guide/generic-api-information#pans-statuscode"><span class="std std-ref">状态代码</span></a> 上一条命令的状态码</div>
</div>
</div>


           </div>
