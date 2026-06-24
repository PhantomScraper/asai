---
title: "バージョンv1.0.0"
lang: ja
slug: "udk/release/udk-v1.0.0"
section: "udk"
sourceUrl: "https://docs.leapslabs.com/ja/udk/release/udk-v1.0.0/"
order: 59
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="version-v1-0-0">
<h1>バージョンv1.0.0</h1>
<div class="admonition note">
<p class="admonition-title">注釈</p>
<ul class="simple">
<li><p><strong>バージョン</strong>:  UDK v1.0.0</p></li>
<li><p><strong>発売日</strong>: 2025年1月8日</p></li>
</ul>
</div>
<ul class="simple">
<li><p>LEAPS UWB サブシステム</p>
<ul>
<li><p>顧客とチームからのフィードバックに基づくバグフィックス＋改善</p></li>
<li><p>UL-TDoA時間同期とマルチレテレーション・アルゴリズムの改善。</p></li>
<li><p>新しいトリレーターアルゴリズムの追加</p></li>
<li><p>消費電力の検証と最適化</p></li>
<li><p>自動テスト（システムテスト、APIテスト、異なるモードのテスト、システムの設定）のための屋外テストセットアップの使用</p></li>
<li><p>ゲートウェイ機能の一部としてのバックホールデータの改善</p></li>
<li><p>DW3000ドライバを最新バージョンに更新</p></li>
<li><p>自動ポジショニング測定が任意のアンカー量で行われることを確認</p></li>
<li><p>ロケーションエンジンのフィルタリングの改善</p></li>
<li><p>FiRa互換の新しいRFプロファイルの追加</p></li>
<li><p>CH9のデフォルトプリアンブルコードの変更</p></li>
<li><p>消費電力を最適化するためにシェルAPIにオートログアウトを追加</p></li>
<li><p>測定と位置のメトリクスを追加</p></li>
<li><p>DWM3001、DWM1001、村田製作所 2AB で検証してください。</p></li>
<li><p>製品リリースの検証</p></li>
</ul>
</li>
<li><p>LEAPS Server</p>
<ul>
<li><p>顧客とチームからのフィードバックに基づくバグ修正 + 改善</p></li>
<li><p>製品リリースの検証</p></li>
</ul>
</li>
<li><p>LEAPS Gateway</p>
<ul>
<li><p>バグ修正</p></li>
<li><p>USB インターフェイスの処理を改善しました。</p></li>
<li><p>製品リリースの検証</p></li>
</ul>
</li>
<li><p>LEAPS Manager Android</p>
<ul>
<li><p>一部の Android デバイスの問題をデバッグおよびバグフィックスし、Bluetooth の安定性を改善します。</p></li>
<li><p>MQTT ネットワーク ID の変更を許可</p></li>
<li><p>ユーザ管理とアクセス許可の改善</p></li>
<li><p>ノードリストとグリッドのリアルタイム更新の改善</p></li>
<li><p>コードのリファクタリングとクリーンアップ</p></li>
<li><p>製品リリースの検証</p></li>
</ul>
</li>
<li><p>LEAPS Manager iOS</p>
<ul>
<li><p>App Store でリリース</p></li>
<li><p>バグ修正</p></li>
<li><p>ノードに便利なプロパティを追加</p></li>
<li><p>ノードリストとグリッドのリアルタイム更新の改善</p></li>
<li><p>FW アップデートの速度を改善します。</p></li>
</ul>
</li>
<li><p>LEAPS Center</p>
<ul>
<li><p>バグ修正</p></li>
<li><p>Docker サポートを更新</p></li>
<li><p>VMWare サポートを更新</p></li>
<li><p>製品リリースの検証</p></li>
</ul>
</li>
<li><p>UDK SDK</p>
<ul>
<li><p>バグ修正</p></li>
<li><p>顧客からのフィードバックに基づくドキュメントの改善</p></li>
</ul>
</li>
</ul>
<hr class="docutils">
<div class="section" id="known-limitations">
<h2>既知の制限</h2>
<table class="colwidths-given docutils align-default">
<colgroup>
<col style="width: 7%">
<col style="width: 53%">
<col style="width: 40%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>いいえ。</p></th>
<th class="head"><p>要約</p></th>
<th class="head"><p>影響を受ける</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>1</p></td>
<td><p><a class="reference internal" href="/docs/ja/udk/known-limitation/limit-001#limitation-1"><span class="std std-ref">UWB デバイスのキャリブレーションはサポートされていません。</span></a></p></td>
<td><p><a class="reference internal" href="/docs/ja/udk/udk-start/locate-device-using-angle-of-arrival-demo#anchor-lc"><span class="std std-ref">到着角度(AoA)を使ったデバイスの位置特定デモ</span></a></p></td>
</tr>
<tr class="row-odd"><td><p>2</p></td>
<td><p><a class="reference internal" href="/docs/ja/udk/known-limitation/limit-002#limitation-2"><span class="std std-ref">一部のデバイスパラメータの設定はサポートされていません</span></a></p></td>
<td><p><a class="reference internal" href="/docs/ja/udk/udk-start/locate-device-using-angle-of-arrival-demo#anchor-lc"><span class="std std-ref">到着角度(AoA)を使ったデバイスの位置特定デモ</span></a></p></td>
</tr>
</tbody>
</table>
<div class="toctree-wrapper compound">
</div>
</div>
<hr class="docutils">
<div class="section" id="known-issues">
<h2>既知の問題</h2>
<table class="colwidths-given docutils align-default">
<colgroup>
<col style="width: 7%">
<col style="width: 53%">
<col style="width: 40%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>いいえ。</p></th>
<th class="head"><p>要約</p></th>
<th class="head"><p>影響を受ける</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>1</p></td>
<td><p>: <a class="reference internal" href="/docs/ja/udk/known-issue/issue-004#issue-1"><span class="std std-ref">FiRaパラメータの設定が正しく動作しません。</span></a></p></td>
<td><p><a class="reference internal" href="/docs/ja/udk/udk-start/locate-device-using-angle-of-arrival-demo#anchor-lc"><span class="std std-ref">到着角度(AoA)を使ったデバイスの位置特定デモ</span></a></p></td>
</tr>
<tr class="row-odd"><td><p>2</p></td>
<td><p><a class="reference internal" href="/docs/ja/udk/known-issue/issue-005#issue-2"><span class="std std-ref">測距開始時または測距停止時にデバイスが予期せずリセットされることがあります。</span></a></p></td>
<td><p><a class="reference internal" href="/docs/ja/udk/udk-start/locate-device-using-angle-of-arrival-demo#anchor-lc"><span class="std std-ref">到着角度(AoA)を使ったデバイスの位置特定デモ</span></a></p></td>
</tr>
</tbody>
</table>
<div class="toctree-wrapper compound">
</div>
<hr class="docutils">
</div>
</div>


           </div>
