---
title: "LIMIT002"
lang: zh
slug: "udk/known-limitation/limit-002"
section: "udk"
sourceUrl: "https://docs.leapslabs.com/zh-cn/udk/known-limitation/limit-002/"
order: 81
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="limit002">
<span id="limitation-2"></span><h1>LIMIT002</h1>
<p><strong>摘要</strong></p>
<p>不支持某些设备参数的配置。</p>
<hr class="docutils">
<p><strong>如何影响用户</strong></p>
<ul class="simple">
<li><p>无</p></li>
</ul>
<hr class="docutils">
<p><strong>重现步骤</strong></p>
<ul class="simple">
<li><p>受影响的: <a class="reference internal" href="/docs/zh/udk/udk-start/locate-device-using-angle-of-arrival-demo#anchor-lc"><span class="std std-ref">使用到达角(AoA)定位设备演示</span></a>。</p></li>
<li><p>配置 <a class="reference internal" href="/docs/zh/leaps-rtls/integration-guide/leaps-uwbs#leapsuwbs"><span class="std std-ref">LEAPS UWBS</span></a> 的 <strong>Qorvo UCI 模式</strong></p></li>
<li><p>意外行为： 不支持某些设备参数的配置。</p>
<ul>
<li><p>发射功率</p></li>
<li><p>天线延迟</p></li>
<li><p>脉冲形状。</p></li>
<li><p>LNA 激活</p></li>
</ul>
</li>
</ul>
<hr class="docutils">
<p><strong>工作方法</strong></p>
<ul class="simple">
<li><p>无</p></li>
</ul>
</div>


           </div>
