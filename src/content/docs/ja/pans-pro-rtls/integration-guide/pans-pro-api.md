---
title: "PANS PRO API"
lang: ja
slug: "pans-pro-rtls/integration-guide/pans-pro-api"
section: "pans-pro-rtls"
sourceUrl: "https://docs.leapslabs.com/ja/pans-pro-rtls/integration-guide/pans-pro-api/"
order: 93
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="pans-pro-api">
<span id="id1"></span><h1>PANS PRO API</h1>
<p>このガイドでは、Decawave の DW1000 IC に基づく DWM モジュールのパブリック アプリケーション インターフェイスを指定します。 API は基本的に、DW1000 IC 部品やその他の周辺機器に SPI/I2C インターフェイス レジスタ セットを介して直接アクセスする詳細を処理することなく、アプリケーション レベルでライブラリを介してモジュールを駆動するために MCU と通信する手段を提供する一連の関数です。IEEE 802.15.4-2011 標準で定義された UWB 物理層を持つ DW1000 IC 部品は、モジュールの MCU によって制御される UWB 無線モジュールとして機能します。モジュールは、ユーザーがシステムと対話するための複数のインターフェイスを提供します。これには、スマートフォン アプリケーションを介して使用できる UART および SPI ハードウェア インターフェイスと BLE インターフェイスが含まれます。</p>
<p><strong>API とそのガイド</strong></p>
<p>API 関数のセットには、さまざまな通信インターフェイスを介してアクセスできるため、開発者はモジュールを使用し、システムに統合する際に柔軟性が得られます。 API アクセスには主に次の 2 種類があります:</p>
<blockquote>
<div><ol class="arabic simple">
<li><p>外部アクセス API: UART、SPI、BLE 経由。</p></li>
<li><p>統合アクセス API: オンボード ユーザー アプリ経由 (C コード)。</p></li>
</ol>
</div></blockquote>
<p>上記の API インターフェイスには次のようなものがあります:</p>
<blockquote>
<div><ol class="arabic simple">
<li><p>UART (汎用)、SPI、およびオンボード API は、<em>API</em> <em>コマンド</em> セクションで紹介されています。</p></li>
<li><p>UART (シェル) API は、 <em>シェル コマンド</em> セクションで紹介されています。</p></li>
<li><p>BLE API は、<em>TLV タイプ リスト</em> セクションで紹介されています。</p></li>
</ol>
</div></blockquote>
<p>次のページでは PANS API 関数自体を指定し、各 API 関数のパラメーター、機能、およびユーティリティの詳細を説明します。</p>
<p>ユーザーは API を使用して、個々のモジュールを構成できます。</p>
<hr class="docutils">
<p>次のサブセクションでは、サポートされている各種の API を示します。</p>
<div class="toctree-wrapper compound">
<ul>
<li class="toctree-l1"><a class="reference internal" href="/docs/ja/pans-pro-rtls/integration-guide/tlv-api">TLV API</a></li>
<li class="toctree-l1"><a class="reference internal" href="/docs/ja/pans-pro-rtls/integration-guide/shell-api">シェルAPI</a></li>
<li class="toctree-l1"><a class="reference internal" href="/docs/ja/pans-pro-rtls/integration-guide/mqtt-api">MQTT API</a></li>
<li class="toctree-l1"><a class="reference internal" href="/docs/ja/pans-pro-rtls/integration-guide/supported-intefaces">サポートされているインターフェイス</a></li>
<li class="toctree-l1"><a class="reference internal" href="/docs/ja/pans-pro-rtls/integration-guide/api-limitation">API の制限</a></li>
<li class="toctree-l1"><a class="reference internal" href="/docs/ja/pans-pro-rtls/integration-guide/api-operation">API オペレーション</a></li>
</ul>
</div>
</div>


           </div>
