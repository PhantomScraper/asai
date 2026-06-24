---
title: "ISSUE003"
lang: ja
slug: "udk/known-issue/issue-003"
section: "udk"
sourceUrl: "https://docs.leapslabs.com/ja/udk/known-issue/issue-003/"
order: 113
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="issue003">
<span id="issue-fwu-lm-3"></span><h1>ISSUE003</h1>
<hr class="docutils">
<p><strong>概要</strong></p>
<p>メインファームウェアのアップデートに失敗し、LEAPS Managerアプリケーションがデバイスを検出できなくなりました。</p>
<hr class="docutils">
<p><strong>影響を受けるバージョン</strong>：</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">v0.16.2</span></code></p></li>
</ul>
<hr class="docutils">
<p><strong>ユーザーへの影響</strong>：</p>
<ul>
<li><p>影響を受ける: <a class="reference internal" href="/docs/ja/udk/udk-start/firmware-update#udkfirmwareupdate"><span class="std std-ref">ファームウェアのアップデート</span></a></p></li>
<li><p>予期しない動作です： <span class="red-text">Main firmware</span> のアップデートに失敗し、 <a class="reference internal" href="/docs/ja/leaps-rtls/infrastructure/leaps-manager#leapsmanager"><span class="std std-ref">LEAPS Manager</span></a> アプリケーションがデバイスを検出できなくなりました。デバイスは不明な状態になりました。下のGIF画像のような状態です：</p>
<a class="reference internal image-reference" href="../../../_images/firmware-update-failed.gif"><img alt="../../../_images/firmware-update-failed.gif" class="align-center" src="/docs-assets/ja/_images/firmware-update-failed.gif" style="width: 50%;"></a>
</li>
</ul>
<hr class="docutils">
<p><strong>再現するためのステップ</strong>：</p>
<ul class="simple">
<li><p>不明</p></li>
</ul>
<hr class="docutils">
<p><strong>回避方法</strong>：</p>
<ul class="simple">
<li><p>その後、USB-C データケーブルを使ってデバイスの <a class="reference internal" href="/docs/ja/udk/udk-start/device-hw-interfaces#hardware-interface"><span class="std std-ref">USB-C データポート 2</span></a> を PC に接続し、 <a class="reference internal" href="/docs/ja/udk/udk-start/firmware-update#udkfirmwareupdate"><span class="std std-ref">OpenOCD</span></a> を使ってアップデートを実行してください。</p></li>
</ul>
</div>


           </div>
