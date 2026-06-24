---
title: "ISSUE004"
lang: zh
slug: "udk/known-issue/issue-004"
section: "udk"
sourceUrl: "https://docs.leapslabs.com/zh-cn/udk/known-issue/issue-004/"
order: 85
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="issue004">
<span id="issue-1"></span><h1>ISSUE004</h1>
<hr class="docutils">
<p><strong>摘要</strong></p>
<blockquote>
<div><p>某些FiRa参数的配置工作不稳定。</p>
</div></blockquote>
<hr class="docutils">
<p><strong>受影响的版本</strong>：</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">v0.16.2</span></code></p></li>
</ul>
<hr class="docutils">
<p><strong>如何影响用户</strong>：</p>
<ul class="simple">
<li><p>受影响的: <a class="reference internal" href="/docs/zh/udk/udk-start/locate-device-using-angle-of-arrival-demo#anchor-lc"><span class="std std-ref">使用到达角(AoA)定位设备演示</span></a>。</p></li>
<li><p>意外行为： 某些 FiRa 参数的配置工作不稳定。</p>
<ul>
<li><p>当测量方案为SS-TWR非延迟或DS-TWR非延迟时，无法关闭报告角度参数。</p></li>
<li><p>当参数测距持续时间配置为1000毫秒时，测距无法可靠工作。</p></li>
</ul>
</li>
</ul>
<hr class="docutils">
<p><strong>复制步骤</strong>：</p>
<ul class="simple">
<li><p>无</p></li>
</ul>
<hr class="docutils">
<p><strong>解决方法</strong>：</p>
<ul class="simple">
<li><p>无</p></li>
</ul>
</div>


           </div>
