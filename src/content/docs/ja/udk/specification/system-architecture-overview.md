---
title: "LEAPS RTLS"
lang: ja
slug: "udk/specification/system-architecture-overview"
section: "udk"
sourceUrl: "https://docs.leapslabs.com/ja/udk/specification/system-architecture-overview/"
order: 53
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="leaps-rtls">
<h1>LEAPS RTLS</h1>
<p>このセクションでは LEAPS RTLS システムをより詳細に理解し、特定のコンポーネントの概要を説明します。</p>
<hr class="docutils">
<div class="section" id="leaps-rtls-architecture">
<h2>LEAPS RTLS アーキテクチャ</h2>
<p>次の図は、LEAPS RTLS システムの主なコンセプトの概要です。各コンポーネントの詳細情報は、以降のセクションで説明します。</p>
<div class="admonition note">
<p class="admonition-title">注釈</p>
<p>The firmware for the UDK contains the LEAPS UWB Sub-System as well as Qorvo FiRa UWB Sub-System.</p>
</div>
<div class="figure align-default" id="id1">
<img alt="LEAPS RTLS サブシステム" class="with-shadow float-center" src="/docs-assets/ja/_images/leaps-architect-solution-for-udk.png">
<p class="caption"><span class="caption-text">LEAPS RTLS アーキテクチャ。</span></p>
</div>
<hr class="docutils">
<a class="reference internal image-reference" href="../../../_images/leaps-uwbs.png"><img alt="../../../_images/leaps-uwbs.png" class="align-right" src="/docs-assets/ja/_images/leaps-uwbs.png" style="width: 91.80000000000001px; height: 75.8px;"></a>
</div>
<div class="section" id="leaps-uwbs">
<h2>LEAPS UWBS</h2>
<p>LEAPS UWBS は幅広いユースケースをカバーする完全組み込みのUWBサブシステムです。1つのUWBサブシステムで様々なモードやプロファイルを設定できます。UWBSはアンカーまたはタグとして動作します。ゲートウェイは、UWBネットワークと上位レイヤーの間のゲートウェイとなります。ネットワーク・プロファイルは、大容量かつ低消費電力で完全にスケーラブルです。</p>
<ul class="simple">
<li><p>汎用性があるため、システム要件、コスト、展開時間、メンテナンスの複雑さのバランスが取りやすくなっています。単純な距離の近接から、無制限のレシーバーの高速トラッキングやナビゲーションまで、幅広いアプリケーションに対応します。</p></li>
<li><p>インフラデバイスの適応的クラスタリング、エアタイムの再利用、スロット割り当てなどを可能にする洗練されたUWBMACを統合している。スケーラブルで実績のある衝突検出、衝突回避、衝突解決により、システムは複雑な環境でも堅牢に機能します。</p></li>
<li><p>サポートされる測定技術には、TWR、DL-TDoA、UL-TDoAが含まれます。統合ロケーションエンジンにより、デバイスはDL-TDoAまたはTWRを使用したナビゲーションモードで独立して動作します。</p></li>
<li><p>優れた電源管理により、TWR および TDoA モードで長いバッテリー寿命を実現します。</p></li>
</ul>
<hr class="docutils">
<a class="reference internal image-reference" href="../../../_images/leapsapi.png"><img alt="../../../_images/leapsapi.png" class="align-right" src="/docs-assets/ja/_images/leapsapi.png" style="width: 87.3px; height: 144.6px;"></a>
</div>
<div class="section" id="leaps-api">
<h2>LEAPS API</h2>
<ul class="simple">
<li><p>LEAPS RTLS ソフトウェアスタックは、カスタムアプリケーションに合わせてデバイスを簡単に設定できる API を提供します。 LEAPS RTLS ソフトウェアスタックは、カスタムアプリケーションに合わせてデバイスを簡単に設定できる API を提供します。</p></li>
<li><p>この API は、UART、USB、SPI、BLE インターフェースを介した外部デバイスのために、バイナリ TLV (Type-Length-Value) フレーム・フォーマットを使用します。データの一元化が使用されている場合、JSONを使用したMQTT経由の通信が高レベルのアプリケーションで利用可能です。</p></li>
<li><p>APIコマンドラインインターフェースは、UART、USB、BLEインターフェースを介して、より使いやすく読みやすいフォーマットでサポートされます。</p></li>
</ul>
<hr class="docutils">
<a class="reference internal image-reference" href="../../../_images/leapsmanager.png"><img alt="../../../_images/leapsmanager.png" class="align-right" src="/docs-assets/ja/_images/leapsmanager.png" style="width: 101.7px; height: 119.1px;"></a>
</div>
<div class="section" id="leaps-manager">
<h2>LEAPS Manager</h2>
<p>LEAPS Manager is a mobile application that provides device discovery, device configuration, network configuration, network management and location visualization.</p>
<ul class="simple">
<li><p>デモウィザードを使用すると、定義済みのデモセットアップでキットを簡単かつ迅速に設定できます。</p></li>
<li><p>2Dと3Dのグリッドはリアルタイムで位置を更新し、ネットワーク内のデバイスを視覚化します。</p></li>
<li><p>デバイスとの通信はBLE経由で行われ、接続の信頼性を維持するために最大6つの同時接続をサポートしています。</p></li>
<li><p>データの一元化が使用されている場合、MQTTを介したLEAPS Serverとの通信が可能で、ネットワーク全体のデバイスの管理と可視化が可能になります。</p></li>
<li><p>その他の便利な機能には、デバイス管理、BLE によるファームウェアアップデート、アンカーの自動位置決め、ロギング、デバッグコンソールなどがあります。</p></li>
</ul>
<hr class="docutils">
<a class="reference internal image-reference" href="../../../_images/leapsgateway.png"><img alt="../../../_images/leapsgateway.png" class="align-right" src="/docs-assets/ja/_images/leapsgateway.png" style="width: 90.3px; height: 63.599999999999994px;"></a>
</div>
<div class="section" id="leaps-gateway">
<h2>LEAPS Gateway</h2>
<p>LEAPS Gatewayは UWB サブシステムと TCP/IP ネットワーク間のゲートウェイとして機能します。</p>
<ul class="simple">
<li><p>LEAPS Gatewayは一方ではSPIまたはUSB経由の汎用LEAPS API経由でLEAPS UWBSと通信し、もう一方ではTCP/IP経由でLEAPS Serverと通信します。</p></li>
<li><p>LEAPS UWBネットワークプロファイルに応じて、アンカーとタグの位置情報およびテレメトリデータをLEAPS Serverとの間でアップリンクおよびダウンリンク転送するための媒体を提供します。</p></li>
<li><p>UWBSとの相互接続は、専用のLEAPS Gateway組み込みデバイス上のSPIを介して行われます。LEAPS UWBSとの相互接続がUDKデバイスのようにUSB経由で行われる場合、LEAPS GatewayはデーモンサービスとしてLinuxプラットフォーム上で動作します。</p></li>
</ul>
<hr class="docutils">
<a class="reference internal image-reference" href="../../../_images/leapsserver.png"><img alt="../../../_images/leapsserver.png" class="align-right" src="/docs-assets/ja/_images/leapsserver.png" style="width: 77.1px; height: 63.599999999999994px;"></a>
</div>
<div class="section" id="leaps-server">
<h2>LEAPS Server</h2>
<p>LEAPS ServerはUWBネットワークの中央データハブです。MQTTブローカーを介して、すべてのLEAPS Gatewayデバイスと世界を相互接続します。</p>
<ul class="simple">
<li><p>アップリンクデータコンセントレータ、ダウンリンクデータルータ、データプロセッサ、ロケーションエンジン、デバイス管理、デバイスアクセス制御として機能し、サービス品質を保証します。</p></li>
<li><p>コネクタを介して世界と通信します。現在サポートされているコネクタは MQTT で、AWS もサポートしています。</p></li>
<li><p>LEAPS Serverは Linux プラットフォーム上でデーモンサービスとして動作します。</p></li>
</ul>
<hr class="docutils">
<a class="reference internal image-reference" href="../../../_images/leapscenter.png"><img alt="../../../_images/leapscenter.png" class="align-right" src="/docs-assets/ja/_images/leapscenter.png" style="width: 85.5px; height: 121.0px;"></a>
</div>
<div class="section" id="leaps-center">
<h2>LEAPS Center</h2>
<p><a class="reference internal" href="/docs/ja/leaps-rtls/infrastructure/leaps-center#leapscenter"><span class="std std-ref">LEAPS Center</span></a> は、デバイス管理、ネットワーク管理、ネットワーク全体の位置情報と遠隔測定データの可視化を提供するウェブアプリケーションです。</p>
<ul class="simple">
<li><p>2Dと3Dのグリッドはリアルタイムで位置を更新し、ネットワーク内のデバイスを視覚化します。</p></li>
<li><p>その他の便利な機能には、ユーザー管理、ゾーン管理、ゾーン履歴、フロアプラン管理、ポジション履歴、ポジションヒートマップがあります。</p></li>
<li><p>The <a class="reference internal" href="/docs/ja/leaps-rtls/infrastructure/leaps-center#leapscenter"><span class="std std-ref">LEAPS Center</span></a> は MQTT を介して LEAPS Serverと通信します。これは Linux または Windows プラットフォーム上でサービスとして動作します。</p></li>
</ul>
<hr class="docutils">
<a class="reference internal image-reference" href="../../../_images/leapsbroker.png"><img alt="../../../_images/leapsbroker.png" class="align-right" src="/docs-assets/ja/_images/leapsbroker.png" style="width: 93.3px; height: 51.9px;"></a>
</div>
<div class="section" id="mqtt-broker">
<h2>MQTT Broker</h2>
<p>MQTT Brokerは、クライアントからのすべてのメッセージを受信し、そのメッセージを適切な宛先クライアントにルーティングするサーバーです。MQTT クライアントとは、MQTT ライブラリを実行し、ネットワーク経由で MQTT ブローカーに接続するあらゆるデバイス（マイクロコントローラから本格的なサーバーまで）のことです。</p>
<hr class="docutils">
</div>
</div>


           </div>
