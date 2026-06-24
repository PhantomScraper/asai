---
title: "ISSUE004"
lang: ja
slug: "udk/known-issue/issue-004"
section: "udk"
sourceUrl: "https://docs.leapslabs.com/ja/udk/known-issue/issue-004/"
order: 85
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="issue004">
<span id="issue-1"></span><h1>ISSUE004</h1>
<hr class="docutils">
<p><strong>概要</strong></p>
<blockquote>
<div><p>一部の FiRa パラメータの設定が確実に動作しません。</p>
</div></blockquote>
<hr class="docutils">
<p><strong>影響を受けるバージョン</strong>：</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">v0.16.2</span></code></p></li>
</ul>
<hr class="docutils">
<p><strong>ユーザーへの影響</strong>：</p>
<ul class="simple">
<li><p>影響を受ける項目: <a class="reference internal" href="/docs/ja/udk/udk-start/locate-device-using-angle-of-arrival-demo#anchor-lc"><span class="std std-ref">到着角度(AoA)を使ったデバイスの位置特定デモ</span></a></p></li>
<li><p>意外行为： 某些 FiRa 参数的配置工作不稳定。</p>
<ul>
<li><p>測定スキームがSS-TWR非遅延またはDS-TWR非遅延の場合、レポート角度パラメータをオフにできません。</p></li>
<li><p>パラメータRanging durationが1000ミリ秒に設定されている場合、Rangingが確実に動作しない。</p></li>
</ul>
</li>
</ul>
<hr class="docutils">
<p><strong>再現するためのステップ</strong>：</p>
<ul class="simple">
<li><p>なし</p></li>
</ul>
<hr class="docutils">
<p><strong>回避方法</strong>：</p>
<ul class="simple">
<li><p>なし</p></li>
</ul>
</div>


           </div>
