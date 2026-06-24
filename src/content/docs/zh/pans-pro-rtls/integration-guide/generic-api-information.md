---
title: "通用 API 信息"
lang: zh
slug: "pans-pro-rtls/integration-guide/generic-api-information"
section: "pans-pro-rtls"
sourceUrl: "https://docs.leapslabs.com/zh-cn/pans-pro-rtls/integration-guide/generic-api-information/"
order: 154
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="generic-api-information">
<h1>通用 API 信息</h1>
<p>以下部分描述了常用的 TLV 值</p>
<blockquote>
<div><div class="admonition note">
<p class="admonition-title">注解</p>
<p>除非另有说明，否则 API 中使用的整数都是小端序的。</p>
</div>
</div></blockquote>
<div class="section" id="status-code">
<span id="pans-statuscode"></span><h2>状态代码</h2>
<p>每个 TLV 请求都会得到状态代码的回复，状态代码提供了请求是否被成功处理的信息。</p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">err_code =  8-bit unsigned integer = ‘0’ | ‘1’ | ‘2’ | ‘3’ | ’4’ | ’5’</span>
<span class="go">0: ok</span>
<span class="go">1: unknown command or broken TLV frame</span>
<span class="go">2: internal error</span>
<span class="go">3: invalid parameter</span>
<span class="go">4: busy</span>
<span class="go">5: operation not permitted</span>
</pre></div>
</div>
</div>
<div class="section" id="position">
<h2>位置</h2>
<p>节点（锚点或标记）的 13 个字节位置。</p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">position = x, y, z, pqf (* position coordinates *)</span>
<span class="go">x = 32-bit integer (* bytes 0-3, in millimeters *)</span>
<span class="go">y = 32-bit integer (* bytes 4-7, in millimeters *)</span>
<span class="go">z = 32-bit integer (* bytes 8-11, in millimeters *)</span>
<span class="go">pqf = 8-bit integer (* byte 12, position quality factor in percents *)</span>
</pre></div>
</div>
</div>
<div class="section" id="gpio-idx">
<h2>gpio_idx</h2>
<p>用户可用的 GPIO 引脚索引。 请参阅下面列表中特定设备的索引。</p>
<ul class="simple">
<li><p>DWM1001: 8, 12, 13, 15, 23, 27</p></li>
</ul>
</div>
</div>


           </div>
