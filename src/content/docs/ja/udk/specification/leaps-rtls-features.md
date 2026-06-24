---
title: "LEAPS RTLS の機能"
lang: ja
slug: "udk/specification/leaps-rtls-features"
section: "udk"
sourceUrl: "https://docs.leapslabs.com/ja/udk/specification/leaps-rtls-features/"
order: 52
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="leaps-rtls-features">
<h1>LEAPS RTLS の機能</h1>
<p>このセクションでは、UDK キットの具体的な機能に加えて、LEAPS RTLS システムの概要を幅広い視点から説明します。</p>
<hr class="docutils">
<div class="section" id="key-features">
<h2>主な機能</h2>
<p>LEAPS RTLS システムは、ウルトラワイドバンドワイヤレス技術を使用したリアルタイムの正確な測位とデータ遠隔測定のための高度で包括的なソリューションを提供します。このソリューションの中核となるのは、LEAPS UWBS (Ultra-Wideband Sub-system) と呼ばれる高度に洗練された組み込みソフトウェアスタックで、以下を含む多くの高度な機能を提供します：</p>
<ul class="simple">
<li><p>LEAPSは、小さなフットプリントで優れた多用途性を備えており、正確な測位とデータ遠隔測定をリアルタイムで行うためのユニークなスイスアーミーナイフです。UWBサブシステムは1つのファームウェアをベースにしており、様々なモードやネットワーキング・プロファイルに設定可能です。</p></li>
<li><p>汎用性、高性能、低メモリ、低消費電力に重点を置いた、高度に組み込み、効果的、最適化されたスタックです。</p></li>
<li><p>50,000㎡を超える様々な大規模プラントやビルで実証されたシステムの拡張性。</p></li>
<li><p>モジュラー構造により、新機能の追加や新しいハードウェアのサポートが容易になりました。</p></li>
<li><p>現在、Murata 2AB、DWM3001C、DWM1001C、Ambiq Micro MCU など、さまざまなハードウェアプラットフォームで使用できます。</p></li>
<li><p>広範なAPIにより、ユーザーは特定のニーズに応じて簡単にシステムを構成、カスタマイズすることができ、リアルタイム位置追跡のための適応性が高く汎用性の高いソリューションを提供します。アプリケーションは、UART、USB、SPI、BLE、またはUART、USB、BLEインターフェースを介した人間が読めるシェルコマンドラインなどの様々なインターフェースを介して、バイナリTLV（Type-Length-Value）フレームフォーマットを使用することができます。</p></li>
<li><p>LEAPS RTLSシステムは、システムの設定や管理を簡単に行うことができる、広範なフリーソフトウェアツールも提供しています。</p></li>
<li><p>LEAPS RTLS の継続的な開発により、今後より幅広いアプリケーションをカバーする機能が提供されます。これにより、ユーザや製品開発者は1つのコンセプトを学び、多くのアプリケーションに導入することができます。</p></li>
</ul>
</div>
<hr class="docutils">
<div class="section" id="performance">
<h2>パフォーマンス</h2>
<ul class="simple">
<li><p>ネットワーキング・スタックは、アンカーとタグの両方に効果的なメカニズムを用いて、常に通信時間の再利用を目指すように設計されている。これにより、事実上、無制限のノードが広範なエリアに配置されます。アンカー自動クラスタリングとタグ・ローミングの効果的なメカニズムにより、これらすべてが自動的に行われます。</p></li>
<li><p>タグの測定モードにより、最大密度はTWRで320Hz、UL-TDoAで600Hz、DL-TDoAでは無制限になります。最大密度は特定の条件下で達成されます。すべてのタグが互いに範囲内にある場合、例えば更新レート0.1Hzで3200個のタグ、1Hzで320個のタグ、10Hzで32個のタグが存在します。タグ同士の干渉はゼロか最小になります。</p></li>
<li><p>タグの最大ロケーションレート： ネットワークプロファイルと測定モードによる. 通常、TWR、DL-TDoA、UL-TDoAでは10Hz。 DL-TDoAはタグあたり最大50Hzの更新レートを提供できます。</p></li>
<li><p>X-Y 位置精度: 50 cm 以上、通常は 10 cm です。</p></li>
<li><p>ポイントツーポイントの範囲： 見通し条件（CH5/CH9）では最大50m、PA使用時は最大150m。</p></li>
<li><p>インフラ配備のグリッドサイズ: 通常20 x 20m、最大40 x 40mまで対応可能。</p></li>
<li><p>優れた電源管理により、TWR および TDoA モードで長いバッテリー寿命を実現します。</p></li>
<li><p>モーションセンサーのアクティビティを利用した適応型ロケーションレートにより、バッテリーの寿命が長くなり、タグの総量が増えます。</p></li>
</ul>
</div>
</div>


           </div>
