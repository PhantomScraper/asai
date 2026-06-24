---
title: "一般的な API 情報"
lang: ja
slug: "pans-pro-rtls/integration-guide/generic-api-information"
section: "pans-pro-rtls"
sourceUrl: "https://docs.leapslabs.com/ja/pans-pro-rtls/integration-guide/generic-api-information/"
order: 154
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="generic-api-information">
<h1>一般的な API 情報</h1>
<p>次のセクションでは、頻繁に使用される TLV 値について説明します。</p>
<blockquote>
<div><div class="admonition note">
<p class="admonition-title">注釈</p>
<p>特に指定のない限り、API で使用される整数はリトルエンディアンです。</p>
</div>
</div></blockquote>
<div class="section" id="status-code">
<span id="pans-statuscode"></span><h2>ステータスコード</h2>
<p>すべての TLV リクエストはステータス コードに応答し、リクエストが正常に処理されたかどうかに関する情報が得られます。</p>
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
<p>ノード (アンカーまたはタグ) の 13 バイトの位置。</p>
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
<p>ユーザーが使用できる GPIO ピンのインデックス。以下のリスト内の特定のデバイスのインデックスを参照してください。</p>
<ul class="simple">
<li><p>DWM1001: 8, 12, 13, 15, 23, 27</p></li>
</ul>
</div>
</div>


           </div>
