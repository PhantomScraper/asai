---
title: "ISSUE003"
lang: zh
slug: "udk/known-issue/issue-003"
section: "udk"
sourceUrl: "https://docs.leapslabs.com/zh-cn/udk/known-issue/issue-003/"
order: 113
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="issue003">
<span id="issue-fwu-lm-3"></span><h1>ISSUE003</h1>
<hr class="docutils">
<p><strong>摘要</strong></p>
<p>主固件更新失败，LEAPS Manager应用程序无法再检测到设备。</p>
<hr class="docutils">
<p><strong>受影响的版本</strong>：</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">v0.16.2</span></code></p></li>
</ul>
<hr class="docutils">
<p><strong>如何影响用户</strong>：</p>
<ul>
<li><p>受影响: <a class="reference internal" href="/docs/zh/udk/udk-start/firmware-update#udkfirmwareupdate"><span class="std std-ref">固件更新</span></a></p></li>
<li><p>意外行为 <span class="red-text">Main firmware</span> 更新失败，并且 <a class="reference internal" href="/docs/zh/leaps-rtls/infrastructure/leaps-manager#leapsmanager"><span class="std std-ref">LEAPS Manager</span></a> 应用程序无法再检测到设备. 设备进入未知状态. 如下面的GIF图片：</p>
<a class="reference internal image-reference" href="../../../_images/firmware-update-failed.gif"><img alt="../../../_images/firmware-update-failed.gif" class="align-center" src="/docs-assets/zh-cn/_images/firmware-update-failed.gif" style="width: 50%;"></a>
</li>
</ul>
<hr class="docutils">
<p><strong>重现步骤</strong>：</p>
<ul class="simple">
<li><p>未知</p></li>
</ul>
<hr class="docutils">
<p><strong>工作方法</strong>：</p>
<ul class="simple">
<li><p>取出电池并关闭电源，然后使用USB-C Data Cable将设备的 <a class="reference internal" href="/docs/zh/udk/udk-start/device-hw-interfaces#hardware-interface"><span class="std std-ref">USB-C Data Port 2</span></a> 连接到 PC，然后通过 <a class="reference internal" href="/docs/zh/udk/udk-start/firmware-update#udkfirmwareupdate"><span class="std std-ref">OpenOCD</span></a> 执行更新。</p></li>
</ul>
</div>


           </div>
