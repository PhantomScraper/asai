---
title: "ジェネリック"
lang: ja
slug: "faq/generic"
section: "faq"
sourceUrl: "https://docs.leapslabs.com/ja/faq/generic/"
order: 29
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="generic">
<span id="faq-generic"></span><h1>ジェネリック</h1>
<hr class="docutils">
<div class="line-block">
<div class="line">以下の FAQ (よくある質問) は、ウルトラワイドバンド、 <a class="reference internal" href="/docs/ja/leaps-rtls#leaps-rtls"><span class="std std-ref">LEAPS RTLS</span></a> または <a class="reference internal" href="/docs/ja/pans-pro-rtls#pans-pro-rtls"><span class="std std-ref">PANS PRO RTLS</span></a> に関する一般的な質問を扱っています。</div>
</div>
<details class="sd-sphinx-override sd-dropdown sd-card sd-mb-3 sd-fade-in-slide-down">
<summary class="sd-summary-title sd-card-header sd-bg-muted sd-bg-text-muted">
<span class="sd-summary-icon"><svg version="1.1" width="1.0em" height="1.0em" class="sd-octicon sd-octicon-question" viewBox="0 0 16 16" aria-hidden="true"><path fill-rule="evenodd" d="M8 1.5a6.5 6.5 0 100 13 6.5 6.5 0 000-13zM0 8a8 8 0 1116 0A8 8 0 010 8zm9 3a1 1 0 11-2 0 1 1 0 012 0zM6.92 6.085c.081-.16.19-.299.34-.398.145-.097.371-.187.74-.187.28 0 .553.087.738.225A.613.613 0 019 6.25c0 .177-.04.264-.077.318a.956.956 0 01-.277.245c-.076.051-.158.1-.258.161l-.007.004a7.728 7.728 0 00-.313.195 2.416 2.416 0 00-.692.661.75.75 0 001.248.832.956.956 0 01.276-.245 6.3 6.3 0 01.26-.16l.006-.004c.093-.057.204-.123.313-.195.222-.149.487-.355.692-.662.214-.32.329-.702.329-1.15 0-.76-.36-1.348-.863-1.725A2.76 2.76 0 008 4c-.631 0-1.155.16-1.572.438-.413.276-.68.638-.849.977a.75.75 0 101.342.67z"></path></svg></span>リアルタイムロケーションシステムは初めてです。基本的な用語のリストはありますか？<div class="sd-summary-down docutils">
<svg version="1.1" width="1.5em" height="1.5em" class="sd-octicon sd-octicon-chevron-down" viewBox="0 0 24 24" aria-hidden="true"><path fill-rule="evenodd" d="M5.22 8.72a.75.75 0 000 1.06l6.25 6.25a.75.75 0 001.06 0l6.25-6.25a.75.75 0 00-1.06-1.06L12 14.44 6.28 8.72a.75.75 0 00-1.06 0z"></path></svg></div>
<div class="sd-summary-up docutils">
<svg version="1.1" width="1.5em" height="1.5em" class="sd-octicon sd-octicon-chevron-up" viewBox="0 0 24 24" aria-hidden="true"><path fill-rule="evenodd" d="M18.78 15.28a.75.75 0 000-1.06l-6.25-6.25a.75.75 0 00-1.06 0l-6.25 6.25a.75.75 0 101.06 1.06L12 9.56l5.72 5.72a.75.75 0 001.06 0z"></path></svg></div>
</summary><div class="sd-summary-content sd-card-body docutils">
<ul class="simple">
<li><p class="sd-card-text"><strong>アンカー</strong> - <strong>AN (Anchor Node)</strong> - 位置を固定したインフラノード - 位置データの測定、データオフロード、ルーティングが可能な参照ノード。</p>
<ul>
<li><p class="sd-card-text">UWBサブシステムとイーサネットやWiFiなどの他のインターフェースとのゲートウェイとして機能します。UWBサブシステムはSPIまたはUSBインターフェース経由でホストに接続されます。</p></li>
</ul>
</li>
<li><p class="sd-card-text"><strong>Location Engine (LE)</strong> - 測定値を使った位置推定アルゴリズム。大きく分けて2つのグループがあります。</p></li>
</ul>
<blockquote>
<div><ul class="simple">
<li><p class="sd-card-text"><strong>トライレーション</strong> - ノード間の距離を使用して位置を推定するロケーション・エンジン。</p></li>
<li><p class="sd-card-text"><strong>マルチラテレーション</strong> - 特にTDoAを使用する場合に、ノード間の時間差を使用して位置を推定するロケーションエンジン。</p></li>
</ul>
</div></blockquote>
<ul class="simple">
<li><p class="sd-card-text"><strong>ナビゲーション</strong> - 位置データが移動体側で収集され使用される測位モード。LEAPS RTLSとPANS PRO RTLSのナビゲーションモードでは、位置情報はモジュール上で計算され、データはモジュール上のAPI経由で利用できます。このアプローチにより、モバイルデバイス上の位置情報のレイテンシが非常に低くなり、インフラコストが削減され、導入が大幅に簡素化されます。典型的なアプリケーションは、ドローン、ロボット、ツール、車両、携帯機器のナビゲーションなどです。</p></li>
<li><p class="sd-card-text"><strong>ノード</strong> - 他のデバイス(アンカー、タグ、...)と通信可能なネットワークデバイスです。</p></li>
<li><p class="sd-card-text"><strong>タグ</strong> - <strong>TN (タグ・ノード)</strong> - 位置を移動するモバイル・ノード - アンカーを使って位置を測定し、モードによっては指定された更新レートでデータを交換します。</p></li>
<li><p class="sd-card-text"><strong>到着時間差（TDoA）</strong> - 既知の固定位置にあるノード間の時間差を測定する測定技術です。測定結果は時間差です。既知の固定位置にあるノードは通常、同期している必要があります。TDoAは双曲線上の位置測位法であり、次の2つの主要なサブカテゴリーがある。</p></li>
</ul>
<blockquote>
<div><ul class="simple">
<li><p class="sd-card-text"><strong>アップリンクTDoA(UL-TDoA)</strong> - TDoAの <strong>トラッキング</strong> モードで、タグは通常ブリンクと呼ばれる短いメッセージをランダムな時間に送信します。アンカーはBlinkを受信し、同期した時刻を使用して、双曲線測位法によりタグの位置を推定します。この測位方法では、少なくとも4回の測定が必要で、通常アンカーの配置形状に敏感に反応します。タグは短時間のブリンクを送信するだけでよいため、この方式では消費電力が最も少なくて済みます。UL-TDoAタグは、ハードウェア設計とバッテリーの要件も低くなります。より複雑なタイムスケジューリングと衝突回避スキームが必要なTWRシステムに比べ、この方式ではメディアへのランダムアクセスが可能なため、ネットワークのスケーラビリティとタグの低消費電力が実現しやすくなります。</p></li>
<li><p class="sd-card-text"><strong>下りリンクTDoA（DL-TDoA）</strong> - TDoAの <strong>ナビゲーション</strong> モードであり、Tagは時間と通常アンカーの位置を含むアンカーからのネットワークメッセージのみを受信します。これらのデータに基づいて、タグは自分の位置を計算することができます。これはGNSS（全地球衛星測位システム）に類似しており、屋内で使用されます。タグは聞くだけで送信しないので、タグの数に制限はありません。このモードでは、タグは送信しないため、タグの完全なプライバシーが保たれます。</p></li>
</ul>
</div></blockquote>
<ul class="simple">
<li><p class="sd-card-text"><strong>トラッキング</strong> - 位置情報と遠隔測定データが集中サーバーに収集される場合の測位モード。データは LEAPS Server API経由で利用可能です。このモードは、多数のデバイスのデータをサーバー上で一元的に監視・処理するのに適しています。典型的なアプリケーションは、資産追跡、ゾーン違反検出、アスリートのパフォーマンス監視、人員追跡などです。</p></li>
<li><p class="sd-card-text"><strong>双方向測距(TWR)</strong> - 2つのノード間の距離が双方向のメッセージ交換によって推定される測定技術のグループです。測定の結果は距離です。ノードの時間同期はタグの位置計算には必要ありません。</p></li>
<li><p class="sd-card-text"><strong>超広帯域 (UWB)</strong> - 電波スペクトルの大部分において、非常に低いエネルギーレベルで短距離、広帯域の通信が可能な無線技術です。Bluetooth、WIFI、GPSなどの他の技術と比較して、UWBはマルチパスフェージングに非常に強い。そのため、特に屋内での正確な測位に適しています。</p></li>
</ul>
</div>
</details><hr class="docutils">
<details class="sd-sphinx-override sd-dropdown sd-card sd-mb-3 sd-fade-in-slide-down">
<summary class="sd-summary-title sd-card-header sd-bg-muted sd-bg-text-muted">
<span class="sd-summary-icon"><svg version="1.1" width="1.0em" height="1.0em" class="sd-octicon sd-octicon-question" viewBox="0 0 16 16" aria-hidden="true"><path fill-rule="evenodd" d="M8 1.5a6.5 6.5 0 100 13 6.5 6.5 0 000-13zM0 8a8 8 0 1116 0A8 8 0 010 8zm9 3a1 1 0 11-2 0 1 1 0 012 0zM6.92 6.085c.081-.16.19-.299.34-.398.145-.097.371-.187.74-.187.28 0 .553.087.738.225A.613.613 0 019 6.25c0 .177-.04.264-.077.318a.956.956 0 01-.277.245c-.076.051-.158.1-.258.161l-.007.004a7.728 7.728 0 00-.313.195 2.416 2.416 0 00-.692.661.75.75 0 001.248.832.956.956 0 01.276-.245 6.3 6.3 0 01.26-.16l.006-.004c.093-.057.204-.123.313-.195.222-.149.487-.355.692-.662.214-.32.329-.702.329-1.15 0-.76-.36-1.348-.863-1.725A2.76 2.76 0 008 4c-.631 0-1.155.16-1.572.438-.413.276-.68.638-.849.977a.75.75 0 101.342.67z"></path></svg></span>DWM1001、PANS RTLS、PANS PRO RTLS、LEAPS RTLSの違いは何ですか？<div class="sd-summary-down docutils">
<svg version="1.1" width="1.5em" height="1.5em" class="sd-octicon sd-octicon-chevron-down" viewBox="0 0 24 24" aria-hidden="true"><path fill-rule="evenodd" d="M5.22 8.72a.75.75 0 000 1.06l6.25 6.25a.75.75 0 001.06 0l6.25-6.25a.75.75 0 00-1.06-1.06L12 14.44 6.28 8.72a.75.75 0 00-1.06 0z"></path></svg></div>
<div class="sd-summary-up docutils">
<svg version="1.1" width="1.5em" height="1.5em" class="sd-octicon sd-octicon-chevron-up" viewBox="0 0 24 24" aria-hidden="true"><path fill-rule="evenodd" d="M18.78 15.28a.75.75 0 000-1.06l-6.25-6.25a.75.75 0 00-1.06 0l-6.25 6.25a.75.75 0 101.06 1.06L12 9.56l5.72 5.72a.75.75 0 001.06 0z"></path></svg></div>
</summary><div class="sd-summary-content sd-card-body docutils">
<ul class="simple">
<li><p class="sd-card-text"><strong>DWM1001</strong> は、Decawave/Qorvo社の超広帯域（UWB）トランシーバーIC DW1000をベースとしたハードウェアモジュールで、IEEE 802.15.4-2011のUWB実装です。UWBおよびBluetooth®アンテナ、すべてのRF回路、ノルディックセミコンダクターのnRF52832、モーションセンサーが統合されています。このモジュールは当初LEAPSによって設計され、Decawaveブランドで販売されました。</p></li>
<li><p class="sd-card-text"><strong>PANS RTLS</strong> は、TWR測定技術に基づく完全なリアルタイム位置情報システムとネットワークスタックです。UWBサブシステムは、アンカー、タグ、ゲートウェイの各モードに設定可能です。ソフトウェアスタックはLEAPSによって開発され、Decawave/Qorvoブランドで販売されています。</p></li>
<li><p class="sd-card-text"><strong>PANS PRO RTLS</strong> はPANS RTLSスタックに基づいています。これはLEAPSによってメンテナンスされ、市場に提供されています。PANS PRO RTLSは、量産レベルのスタックを提供するため、多くのソフトウェアの改良とバグ修正が行われています。このソフトウェアスタックを搭載した様々な認証製品が市場に導入されています。このスタックは、PANS RTLSスタックと同様にバイナリコードで市場に無償提供されます。</p></li>
<li><p class="sd-card-text"><strong>LEAPS RTLS</strong> は、ナビゲーションとトラッキングの幅広いユースケースをカバーできる先進的なリアルタイム・ロケーション・システムです。そのコアは、様々なモードやプロファイルに設定可能な組み込みUWBサブシステムです。スタックは、アンカー、タグ、ゲートウェイの各モードで動作します。ネットワーキング・プロファイルは、大容量かつ低消費電力で完全にスケーラブルです。その多用途性により、システム要件、コスト、展開時間、メンテナンスの複雑さのバランスを取ることが容易になります。アプリケーションは、単純な距離の近接から、無制限のレシーバーの高速トラッキングやナビゲーションまで多岐にわたります。TWR（Two-Way Ranging）、UL-TDoA（Uplink Time Difference of Arrivalを使用したトラッキング）、DL-TDoA（Downlink Time Difference of Arrivalを使用したナビゲーション）などの測定技術をサポートしています。LEAPSスタックは、LEAPSの製品だけでなく、サードパーティの製品にも統合されています。</p></li>
</ul>
</div>
</details><hr class="docutils">
<details class="sd-sphinx-override sd-dropdown sd-card sd-mb-3 sd-fade-in-slide-down">
<summary class="sd-summary-title sd-card-header sd-bg-muted sd-bg-text-muted">
<span class="sd-summary-icon"><svg version="1.1" width="1.0em" height="1.0em" class="sd-octicon sd-octicon-question" viewBox="0 0 16 16" aria-hidden="true"><path fill-rule="evenodd" d="M8 1.5a6.5 6.5 0 100 13 6.5 6.5 0 000-13zM0 8a8 8 0 1116 0A8 8 0 010 8zm9 3a1 1 0 11-2 0 1 1 0 012 0zM6.92 6.085c.081-.16.19-.299.34-.398.145-.097.371-.187.74-.187.28 0 .553.087.738.225A.613.613 0 019 6.25c0 .177-.04.264-.077.318a.956.956 0 01-.277.245c-.076.051-.158.1-.258.161l-.007.004a7.728 7.728 0 00-.313.195 2.416 2.416 0 00-.692.661.75.75 0 001.248.832.956.956 0 01.276-.245 6.3 6.3 0 01.26-.16l.006-.004c.093-.057.204-.123.313-.195.222-.149.487-.355.692-.662.214-.32.329-.702.329-1.15 0-.76-.36-1.348-.863-1.725A2.76 2.76 0 008 4c-.631 0-1.155.16-1.572.438-.413.276-.68.638-.849.977a.75.75 0 101.342.67z"></path></svg></span>LEAPSはDWM1001モジュールとPANS RTLSネットワークスタックの作成にどのように参加していますか？<div class="sd-summary-down docutils">
<svg version="1.1" width="1.5em" height="1.5em" class="sd-octicon sd-octicon-chevron-down" viewBox="0 0 24 24" aria-hidden="true"><path fill-rule="evenodd" d="M5.22 8.72a.75.75 0 000 1.06l6.25 6.25a.75.75 0 001.06 0l6.25-6.25a.75.75 0 00-1.06-1.06L12 14.44 6.28 8.72a.75.75 0 00-1.06 0z"></path></svg></div>
<div class="sd-summary-up docutils">
<svg version="1.1" width="1.5em" height="1.5em" class="sd-octicon sd-octicon-chevron-up" viewBox="0 0 24 24" aria-hidden="true"><path fill-rule="evenodd" d="M18.78 15.28a.75.75 0 000-1.06l-6.25-6.25a.75.75 0 00-1.06 0l-6.25 6.25a.75.75 0 101.06 1.06L12 9.56l5.72 5.72a.75.75 0 001.06 0z"></path></svg></div>
</summary><div class="sd-summary-content sd-card-body docutils">
<ul class="simple">
<li><p class="sd-card-text"><strong>DWM1001モジュール</strong> は当初LEAPSが設計し、Decawave/Qorvoブランドのもと、設計、モジュールの立ち上げ、検証、製品化に取り組みました。</p></li>
<li><p class="sd-card-text"><strong>LEAPS</strong> はPANS RTLS <strong>の</strong> ソフトウェアスタックを設計・開発しました。</p></li>
</ul>
</div>
</details><hr class="docutils">
<details class="sd-sphinx-override sd-dropdown sd-card sd-mb-3 sd-fade-in-slide-down">
<summary class="sd-summary-title sd-card-header sd-bg-muted sd-bg-text-muted">
<span class="sd-summary-icon"><svg version="1.1" width="1.0em" height="1.0em" class="sd-octicon sd-octicon-question" viewBox="0 0 16 16" aria-hidden="true"><path fill-rule="evenodd" d="M8 1.5a6.5 6.5 0 100 13 6.5 6.5 0 000-13zM0 8a8 8 0 1116 0A8 8 0 010 8zm9 3a1 1 0 11-2 0 1 1 0 012 0zM6.92 6.085c.081-.16.19-.299.34-.398.145-.097.371-.187.74-.187.28 0 .553.087.738.225A.613.613 0 019 6.25c0 .177-.04.264-.077.318a.956.956 0 01-.277.245c-.076.051-.158.1-.258.161l-.007.004a7.728 7.728 0 00-.313.195 2.416 2.416 0 00-.692.661.75.75 0 001.248.832.956.956 0 01.276-.245 6.3 6.3 0 01.26-.16l.006-.004c.093-.057.204-.123.313-.195.222-.149.487-.355.692-.662.214-.32.329-.702.329-1.15 0-.76-.36-1.348-.863-1.725A2.76 2.76 0 008 4c-.631 0-1.155.16-1.572.438-.413.276-.68.638-.849.977a.75.75 0 101.342.67z"></path></svg></span>LEAPS RTLSとPANS PRO RTLSのアーキテクチャの違いは何ですか？<div class="sd-summary-down docutils">
<svg version="1.1" width="1.5em" height="1.5em" class="sd-octicon sd-octicon-chevron-down" viewBox="0 0 24 24" aria-hidden="true"><path fill-rule="evenodd" d="M5.22 8.72a.75.75 0 000 1.06l6.25 6.25a.75.75 0 001.06 0l6.25-6.25a.75.75 0 00-1.06-1.06L12 14.44 6.28 8.72a.75.75 0 00-1.06 0z"></path></svg></div>
<div class="sd-summary-up docutils">
<svg version="1.1" width="1.5em" height="1.5em" class="sd-octicon sd-octicon-chevron-up" viewBox="0 0 24 24" aria-hidden="true"><path fill-rule="evenodd" d="M18.78 15.28a.75.75 0 000-1.06l-6.25-6.25a.75.75 0 00-1.06 0l-6.25 6.25a.75.75 0 101.06 1.06L12 9.56l5.72 5.72a.75.75 0 001.06 0z"></path></svg></div>
</summary><div class="sd-summary-content sd-card-body docutils">
<p class="sd-card-text">LEAPS RTLS（上）とPANS PRO RTLS（下）のシステムアーキテクチャの比較：</p>
<p class="sd-card-text"><strong>LEAPS RTLS システムアーキテクチャ</strong></p>
<img alt="../../_images/leaps-architect-solution.png" class="align-center" src="/docs-assets/ja/_images/leaps-architect-solution.png">
<p class="sd-card-text"><strong>PANS PRO RTLS System Architecture</strong></p>
<img alt="../../_images/pans_pro-sub-system.png" class="align-center" src="/docs-assets/ja/_images/pans_pro-sub-system.png">
</div>
</details><hr class="docutils">
<details class="sd-sphinx-override sd-dropdown sd-card sd-mb-3 sd-fade-in-slide-down">
<summary class="sd-summary-title sd-card-header sd-bg-muted sd-bg-text-muted">
<span class="sd-summary-icon"><svg version="1.1" width="1.0em" height="1.0em" class="sd-octicon sd-octicon-question" viewBox="0 0 16 16" aria-hidden="true"><path fill-rule="evenodd" d="M8 1.5a6.5 6.5 0 100 13 6.5 6.5 0 000-13zM0 8a8 8 0 1116 0A8 8 0 010 8zm9 3a1 1 0 11-2 0 1 1 0 012 0zM6.92 6.085c.081-.16.19-.299.34-.398.145-.097.371-.187.74-.187.28 0 .553.087.738.225A.613.613 0 019 6.25c0 .177-.04.264-.077.318a.956.956 0 01-.277.245c-.076.051-.158.1-.258.161l-.007.004a7.728 7.728 0 00-.313.195 2.416 2.416 0 00-.692.661.75.75 0 001.248.832.956.956 0 01.276-.245 6.3 6.3 0 01.26-.16l.006-.004c.093-.057.204-.123.313-.195.222-.149.487-.355.692-.662.214-.32.329-.702.329-1.15 0-.76-.36-1.348-.863-1.725A2.76 2.76 0 008 4c-.631 0-1.155.16-1.572.438-.413.276-.68.638-.849.977a.75.75 0 101.342.67z"></path></svg></span>2つのデバイス間で可能な限り長い距離を達成するには？<div class="sd-summary-down docutils">
<svg version="1.1" width="1.5em" height="1.5em" class="sd-octicon sd-octicon-chevron-down" viewBox="0 0 24 24" aria-hidden="true"><path fill-rule="evenodd" d="M5.22 8.72a.75.75 0 000 1.06l6.25 6.25a.75.75 0 001.06 0l6.25-6.25a.75.75 0 00-1.06-1.06L12 14.44 6.28 8.72a.75.75 0 00-1.06 0z"></path></svg></div>
<div class="sd-summary-up docutils">
<svg version="1.1" width="1.5em" height="1.5em" class="sd-octicon sd-octicon-chevron-up" viewBox="0 0 24 24" aria-hidden="true"><path fill-rule="evenodd" d="M18.78 15.28a.75.75 0 000-1.06l-6.25-6.25a.75.75 0 00-1.06 0l-6.25 6.25a.75.75 0 101.06 1.06L12 9.56l5.72 5.72a.75.75 0 001.06 0z"></path></svg></div>
</summary><div class="sd-summary-content sd-card-body docutils">
<p class="sd-card-text">これは <a class="reference external" href="https://www.omnicalculator.com/physics/fresnel-zone">フレネルゾーン</a> と関係があります。昔、私たちは高さ1.2mから1.5mで測定をしたことがありますが、信号はある距離で途絶え、5-10mでしばらくすると戻ってきました。その後、私たちはフレネルゾーンに気づき、高さを2mに上げましたが、それ以来この問題は観測されなくなりました。</p>
<p class="sd-card-text">ほとんどの無線信号では、1番目のフレネルゾーンだけに注意すべきですが、UWBでは他のゾーンも重要なようです。</p>
<p class="sd-card-text">実用的な例です：</p>
<p class="sd-card-text">アンテナ間距離＝100m</p>
<ul class="simple">
<li><p class="sd-card-text">周波数＝6.5GHz</p></li>
<li><p class="sd-card-text">第1ゾーン半径＝1.07m</p></li>
<li><p class="sd-card-text">第2ゾーン半径＝1.52m</p></li>
<li><p class="sd-card-text">第3ゾーン半径＝1.86m</p></li>
</ul>
<p class="sd-card-text">アンテナ間距離＝200m</p>
<ul class="simple">
<li><p class="sd-card-text">周波数＝6.5GHz</p></li>
<li><p class="sd-card-text">第1ゾーン半径＝1.52m</p></li>
<li><p class="sd-card-text">第2ゾーン半径＝2.15m</p></li>
<li><p class="sd-card-text">3ゾーン半径＝2.63m</p></li>
</ul>
<p class="sd-card-text">オンライン計算機はこちら <a class="reference external" href="https://www.omnicalculator.com/physics/fresnel-zone">フレネルゾーン計算機</a></p>
</div>
</details></div>


           </div>
