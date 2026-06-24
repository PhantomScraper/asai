---
title: "バージョン  v0.16.4"
lang: ja
slug: "udk/release/udk-v0.16.4"
section: "udk"
sourceUrl: "https://docs.leapslabs.com/ja/udk/release/udk-v0.16.4/"
order: 58
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="version-v0-16-4">
<h1>バージョン  v0.16.4</h1>
<div class="admonition note">
<p class="admonition-title">注釈</p>
<ul class="simple">
<li><p><strong>バージョン *</strong>： UDK v0.16.4</p></li>
<li><p><strong>リリース日</strong>： 2024 年 11 月 21 日</p></li>
</ul>
</div>
<ul class="simple">
<li><p>LEAPS UWB サブシステム</p>
<ul>
<li><p>バグ修正</p></li>
<li><p>UL-TDoAサポートの追加</p></li>
<li><p>USBおよびSPIインターフェイスのバックホール問題のバグフィックス</p></li>
<li><p>消費電力の改善</p></li>
<li><p>屋外テストセットアップのインストール</p></li>
<li><p>自動ビルドシステムのセットアップ、テストを実行するための関連ツールの作成</p></li>
<li><p>UWB認証およびテストルーチンの顧客への提供</p></li>
</ul>
</li>
<li><p>LEAPS Server</p>
<ul>
<li><p>バグ修正</p></li>
<li><p>UL-TDoAサポートの追加</p></li>
<li><p>マルチレートアルゴリズムおよびロケーションエンジン関連コンポーネントの追加</p></li>
<li><p>測定と位置のメトリクスを追加</p></li>
</ul>
</li>
<li><p>LEAPS Gateway</p>
<ul>
<li><p>UL-TDoAサポートの追加</p></li>
<li><p>最適化されたバックホールデータ</p></li>
</ul>
</li>
<li><p>LEAPS Manager Android</p>
<ul>
<li><p>バグ修正</p></li>
<li><p>UL-TDOA サポートを追加</p></li>
<li><p>測定と位置のメトリクスを追加</p></li>
<li><p>ノードリストとグリッドのリアルタイム更新を追加します</p></li>
<li><p>バッテリー残量表示を追加</p></li>
<li><p>フロアプラン構成フローの改善</p></li>
<li><p>FW 更新ウィンドウにサポートされている HW のリストを追加します</p></li>
<li><p>ログを追加</p></li>
<li><p>MQTTインターフェースを追加</p></li>
<li><p>複数のノードの選択と構成を追加します</p></li>
<li><p>UI/UX を改善する</p></li>
</ul>
</li>
<li><p>LEAPS Manager iOS</p>
<ul>
<li><p>TestFlight 経由でリリース</p></li>
<li><p>バグ修正</p></li>
<li><p>すべてのデモは、デモセレクターとその他の関連するさまざまな改善を使用して設定できます</p></li>
<li><p>UL-TDOA サポートを追加</p></li>
<li><p>測定と位置のメトリクスを追加</p></li>
<li><p>ノードリストとグリッドのリアルタイム更新を追加します</p></li>
<li><p>検出時間設定を追加</p></li>
<li><p>自動配置を改善 (BLE 範囲外のノードを処理できるようにする)</p></li>
<li><p>メートル法/ヤードポンド法の単位設定を追加する</p></li>
<li><p>新しい設計に従って定常/公称更新レート設定を更新します</p></li>
<li><p>フロアプランの改善</p></li>
<li><p>検出のカウントダウンカウンターを追加</p></li>
<li><p>2D グリッドの改善</p></li>
<li><p>UWBS モードを表示します</p></li>
</ul>
</li>
<li><p>LEAPS Center</p>
<ul>
<li><p>多くの改善を加えた新しい UI/UX</p></li>
<li><p>フロアプランの 360 度回転を追加、フロアプランの比率リセットを追加</p></li>
<li><p>サポートページを追加</p></li>
<li><p>ゾーンの表示機能を追加し、ゾーン構成を改善します</p></li>
<li><p>測定と位置のメトリックを追加します。</p></li>
<li><p>ノード構成を改善する</p></li>
<li><p>Springフレームワークを更新</p></li>
<li><p>Docker サポート</p></li>
</ul>
</li>
<li><p>UDK SDK</p>
<ul>
<li><p>DW3000 ドライバが最新バージョンに更新されました</p></li>
<li><p>すべての例が検証されました</p></li>
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
