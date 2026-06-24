---
title: "LEAPS UWBS"
lang: ja
slug: "leaps-rtls/integration-guide/leaps-uwbs"
section: "leaps-rtls"
sourceUrl: "https://docs.leapslabs.com/ja/leaps-rtls/integration-guide/leaps-uwbs/"
order: 66
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="leaps-uwbs">
<span id="leapsuwbs"></span><h1>LEAPS UWBS</h1>
<p><a class="reference external" href="https://www.leapslabs.com/">LEAPS</a> UWBSは、幅広いユースケースをカバーする完全組み込み型の高度なUWBサブシステムです。1つのUWBサブシステムで様々なモードやプロファイルに設定可能です。UWBSはアンカー、タグ、ゲートウェイとして動作します。ネットワーキング・プロファイルは大容量かつ低消費電力で完全にスケーラブルです。</p>
<hr class="docutils">
<div class="section" id="software-architecture">
<h2>ソフトウェア アーキテクチャ</h2>
<div class="figure align-center" id="id1">
<a class="reference internal image-reference" href="../../../_images/leaps_uwbs.png"><img alt="../../../_images/leaps_uwbs.png" src="/docs-assets/ja/_images/leaps_uwbs.png" style="width: 730.8000000000001px; height: 657.9px;"></a>
<p class="caption"><span class="caption-text"><a class="reference external" href="https://www.leapslabs.com/">LEAPS</a> UWBSアーキテクチャ</span></p>
</div>
</div>
<hr class="docutils">
<div class="section" id="key-features">
<h2>主な機能</h2>
<ul class="simple">
<li><p>多用途性により、システム要件、コスト、展開時間、メンテナンスの複雑さのバランスを取ることが容易になります。アプリケーションは単純な距離の近接から、無制限のレシーバーの高速トラッキングやナビゲーションまで多岐にわたります。</p></li>
<li><p>インフラデバイスの適応的クラスタリング、エアタイムの再利用、スロット割り当てなどを可能にする洗練されたUWBMACを統合している。スケーラブルで実績のある衝突検出、衝突回避、衝突解決により、システムは複雑な環境でも堅牢に機能します。</p></li>
<li><p>サポートされる測定技術には、TWR、DL-TDoA、UL-TDoAが含まれます。統合ロケーションエンジンにより、デバイスはDL-TDoAまたはTWRを使用したナビゲーションモードで独立して動作します。</p></li>
<li><p>優れた電源管理により、TWRモードとTDoAモードの両方で長いバッテリー寿命を実現します。</p></li>
</ul>
</div>
<hr class="docutils">
<div class="section" id="used-terminology">
<h2>使用されている用語</h2>
<ul class="simple">
<li><p><strong>アンカー</strong>：位置が固定されています。</p></li>
<li><p><strong>タグ</strong>：位置を変更し、アンカーの助けを借りて動的に位置を決定する。</p></li>
<li><p><strong>ゲートウェイ</strong>：ネットワーク・ノードに関するステートフルな情報（読み取り/イントロスペクト）、ノード情報のキャッシュ、データ収集と履歴の追跡、アプリケーション・レイヤがUWBネットワーク・エレメントと対話するための手段（別名：<em>インタラクション・プロキシ</em>）を提供します。</p></li>
<li><p><strong>ノード</strong>：ネットワーク・ノード（アンカー、タグ、ゲートウェイなど）。</p></li>
<li><p><strong>LE</strong>：ロケーションエンジン。</p></li>
<li><p><strong>CORE_INT:</strong> 新しいUART/SPIインタフェース・イベントをユーザーに通知するために、ファームウェアが予約したGPIOピン。</p></li>
<li><p><strong>TLV:</strong> Type-Length-Valueエンコーディング。</p></li>
<li><p><strong>UWBS</strong>：UWBサブシステム。</p></li>
</ul>
</div>
<hr class="docutils">
<div class="section" id="uwb-rf">
<h2>UWB RF</h2>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 12%">
<col style="width: 17%">
<col style="width: 20%">
<col style="width: 20%">
<col style="width: 31%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"></th>
<th class="head"><p><a class="reference internal" href="/docs/ja/leaps-rtls#leaps-rtls"><span class="std std-ref">LEAPS RTLS</span></a> ,
<a class="reference internal" href="/docs/ja/pans-pro-rtls#pans-pro-rtls"><span class="std std-ref">PANS PRO RTLS</span></a> ,
PANS v2.0</p></th>
<th class="head"><p><a class="reference internal" href="/docs/ja/leaps-rtls#leaps-rtls"><span class="std std-ref">LEAPS RTLS</span></a>,
<a class="reference internal" href="/docs/ja/pans-pro-rtls#pans-pro-rtls"><span class="std std-ref">PANS PRO RTLS</span></a></p></th>
<th class="head"><p>Qorvo FiRa</p></th>
<th class="head"><p>カスタムスタック（DW3000 RF）</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>チャンネル</p></td>
<td><p>5</p></td>
<td><p>5,9</p></td>
<td><p>9</p></td>
<td><p>5,9</p></td>
</tr>
<tr class="row-odd"><td><p>PRF</p></td>
<td><p>64M</p></td>
<td><p>64M</p></td>
<td><p>64M</p></td>
<td><p>16M, 64M</p></td>
</tr>
<tr class="row-even"><td><p>プリアンブル長</p></td>
<td><p>128</p></td>
<td><p>128</p></td>
<td><p>64</p></td>
<td><p>32, 64, 72, 128, 256, 512, 1024, 1536, 2048, 4096</p></td>
</tr>
<tr class="row-odd"><td><p>PAC Size</p></td>
<td><p>8</p></td>
<td><p>8</p></td>
<td><p>8</p></td>
<td><p>4, 8, 16, 32</p></td>
</tr>
<tr class="row-even"><td><p>Rxコード</p></td>
<td><p>9</p></td>
<td><p>9</p></td>
<td><p>9</p></td>
<td><p>1-29 (PRF16: 1-8; PRF64: 9-24)</p></td>
</tr>
<tr class="row-odd"><td><p>Txコード</p></td>
<td><p>9</p></td>
<td><p>9</p></td>
<td><p>9</p></td>
<td><p>1-29 (PRF16: 1-8; PRF64: 9-24)</p></td>
</tr>
<tr class="row-even"><td><p>SFDタイプ</p></td>
<td><p>IEEE 802.15.4ショート8シンボル</p></td>
<td><p>IEEE 802.15.4ショート8シンボル</p></td>
<td><p>IEEE 802.15.4z定義8シンボル</p></td>
<td><p>IEEE 802.15.4ショート8シンボル、デカウェーブ定義8シンボル、デカウェーブ定義16シンボル、IEEE 802.15.4z定義8シンボル</p></td>
</tr>
<tr class="row-odd"><td><p>データ・レート</p></td>
<td><p>6.8 Mbit/s</p></td>
<td><p>6.8 Mbit/s</p></td>
<td><p>6.8 Mbit/s</p></td>
<td><p>6.8Mbit/s, 850kbits/s</p></td>
</tr>
<tr class="row-even"><td><p>PHRモード</p></td>
<td><p>DW独自の拡張フレームPHRモード</p></td>
<td><p>DW独自の拡張フレームPHRモード</p></td>
<td><p>標準</p></td>
<td><p>標準、拡張（DW独自拡張フレームPHRモード）</p></td>
</tr>
<tr class="row-odd"><td><p>PHRレート</p></td>
<td><p>標準</p></td>
<td><p>標準</p></td>
<td><p>標準</p></td>
<td><p>標準、データレート(6M81)でのPHR</p></td>
</tr>
<tr class="row-even"><td><p>SFDタイムアウト</p></td>
<td><p>129</p></td>
<td><p>129</p></td>
<td><p>65</p></td>
<td><p>設定可能</p></td>
</tr>
<tr class="row-odd"><td><p>STSモード</p></td>
<td><p><cite>-</cite></p></td>
<td><p>オフ</p></td>
<td><p>オフ</p></td>
<td><p>オフ、1、2、データなし、超決定性符号</p></td>
</tr>
<tr class="row-even"><td><p>STS長</p></td>
<td><p><cite>-</cite></p></td>
<td><p>0</p></td>
<td><p>0</p></td>
<td><p>32, 64, 128, 256, 512, 1024, 2048</p></td>
</tr>
<tr class="row-odd"><td><p>PDOAモード</p></td>
<td><p><cite>-</cite></p></td>
<td><p>M0</p></td>
<td><p>M1</p></td>
<td><p>M0、M1、M3</p></td>
</tr>
<tr class="row-even"><td rowspan="2"><p>対応ハードウェア</p></td>
<td><p><cite>UWB IC:</cite> DW1000</p></td>
<td><p><cite>UWB IC:</cite> DW3000ファミリー、QM33ファミリー</p></td>
<td><p><cite>UWB IC:</cite> DW3000ファミリー、QM33ファミリー</p></td>
<td><p><cite>UWB IC:</cite> DW3000ファミリー、QM33ファミリー</p></td>
</tr>
<tr class="row-odd"><td><p><cite>モジュール:</cite> DWM1001C</p></td>
<td><p><cite>モジュール:</cite> DWM3001C、Murata Type2AB</p></td>
<td><p><cite>モジュール:</cite> DWM3001C、Murata Type2AB</p></td>
<td><p><cite>モジュール:</cite> DWM3001C、Murata Type2AB</p></td>
</tr>
</tbody>
</table>
</div>
<hr class="docutils">
<div class="section" id="ble-rf">
<h2>BLE RF</h2>
<p>周波数帯域は2.4GHz、40チャンネル、2MHz間隔（詳細はBLE仕様5.3を参照）。</p>
</div>
</div>


           </div>
