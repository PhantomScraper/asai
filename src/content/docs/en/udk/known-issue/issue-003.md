---
title: "ISSUE003"
lang: en
slug: "udk/known-issue/issue-003"
section: "udk"
sourceUrl: "https://docs.leapslabs.com/udk/known-issue/issue-003/"
order: 113
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="issue003">
<span id="issue-fwu-lm-3"></span><h1>ISSUE003</h1>
<hr class="docutils">
<p><strong>Summary</strong></p>
<p>The Main firmware update failed and LEAPS Manager application can no longer detect the device.</p>
<hr class="docutils">
<p><strong>Affected version</strong>:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">v0.16.2</span></code></p></li>
</ul>
<hr class="docutils">
<p><strong>How to impact users</strong>:</p>
<ul>
<li><p>Affected: <a class="reference internal" href="/docs/en/udk/udk-start/firmware-update#udkfirmwareupdate"><span class="std std-ref">Firmware Update</span></a></p></li>
<li><p>Unexpected Behavior: The <span class="red-text">Main firmware</span> update failed and <a class="reference internal" href="/docs/en/leaps-rtls/infrastructure/leaps-manager#leapsmanager"><span class="std std-ref">LEAPS Manager</span></a> application can no longer detect the device. Device falls into an unknown state. Like the GIF Image below:</p>
<a class="reference internal image-reference" href="../../../_images/firmware-update-failed.gif"><img alt="../../../_images/firmware-update-failed.gif" class="align-center" src="/docs-assets/_images/firmware-update-failed.gif" style="width: 50%;"></a>
</li>
</ul>
<hr class="docutils">
<p><strong>Steps to Reproduce</strong>:</p>
<ul class="simple">
<li><p>Unknown</p></li>
</ul>
<hr class="docutils">
<p><strong>Workaround</strong>:</p>
<ul class="simple">
<li><p>Remove the battery and turn off the power then use a USB-C Data Cable to connect the <a class="reference internal" href="/docs/en/udk/udk-start/device-hw-interfaces#hardware-interface"><span class="std std-ref">USB-C Data Port 2</span></a> of devices to your PC then perform update via <a class="reference internal" href="/docs/en/udk/udk-start/firmware-update#udkfirmwareupdate"><span class="std std-ref">OpenOCD</span></a>.</p></li>
</ul>
</div>


           </div>
