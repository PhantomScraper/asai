---
title: "leaps_uwb_profile_get"
lang: ja
slug: "leaps-rtls/integration-guide/api-commands/leaps-uwb-profile-get"
section: "leaps-rtls"
sourceUrl: "https://docs.leapslabs.com/ja/leaps-rtls/integration-guide/api-commands/leaps-uwb-profile-get/"
order: 275
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="leaps-uwb-profile-get">
<span id="id1"></span><h1>leaps_uwb_profile_get</h1>
<p>現在アクティブな UWB プロファイルに関する情報を読み取ります。UWB 接続がないため情報を読み取れない場合は、<code class="docutils literal notranslate"><span class="pre">許可されていません</span></code> を返します。</p>
<hr class="docutils">
<div class="sd-container-fluid sd-sphinx-override sd-mb-4 docutils">
<div class="sd-row sd-row-cols-2 sd-row-cols-xs-2 sd-row-cols-sm-2 sd-row-cols-md-2 sd-row-cols-lg-2 docutils">
<div class="sd-col sd-d-flex-row sd-col-11 sd-col-xs-11 sd-col-sm-11 sd-col-md-11 sd-col-lg-11 sd-m-2 docutils">
<div class="sd-card sd-sphinx-override sd-w-100 sd-shadow-sm docutils">
<div class="sd-card-body docutils">
<div class="sd-card-title sd-font-weight-bold docutils">
入力</div>
<ul class="simple">
<li><p class="sd-card-text">(<em>なし</em>)</p></li>
</ul>
</div>
</div>
</div>
<div class="sd-col sd-d-flex-row sd-col-11 sd-col-xs-11 sd-col-sm-11 sd-col-md-11 sd-col-lg-11 sd-m-2 docutils">
<div class="sd-card sd-sphinx-override sd-w-100 sd-shadow-sm docutils">
<div class="sd-card-body docutils">
<div class="sd-card-title sd-font-weight-bold docutils">
出力</div>
<ul class="simple">
<li><p class="sd-card-text"><a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/leaps-api/api-generic-data-types#statuscode"><span class="std std-ref">ステータスコード</span></a></p></li>
<li><p class="sd-card-text">sf_period_us: 32 ビット符号なし整数 (<em>マイクロ秒単位のスーパーフレーム期間</em>)</p></li>
<li><p class="sd-card-text">スロット期間_us: 16 ビット符号なし整数 (<em>マイクロ秒単位のスロット期間</em>)</p></li>
<li><p class="sd-card-text">sf_num_max: 16 ビット符号なし整数 (<em>スーパーフレーム番号の最大値</em>)</p></li>
<li><p class="sd-card-text">anchor_upd_rate: 16 ビット符号なし整数 (<em>スーパーフレーム期間の乗算でのアンカーの更新レート</em>)</p></li>
<li><p class="sd-card-text">active_profile_id: '1'|'2'|'3'|'4'|'5'|'6' (<em>現在のプロファイル ID/番号、値0は自動プロファイルを意味します</em>)</p></li>
</ul>
</div>
</div>
</div>
</div>
</div>
<hr class="docutils">
<p><strong>例</strong></p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 52%">
<col style="width: 48%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="2"><p>TLV 要求</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>タイプ</p></td>
<td><p>長さ</p></td>
</tr>
<tr class="row-odd"><td><p>0x1F</p></td>
<td><p>0x00</p></td>
</tr>
</tbody>
</table>
<p>タイプ 0x1F(31 dec) は、コマンド Leaps_uwb_profile_get を意味します</p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 4%">
<col style="width: 6%">
<col style="width: 5%">
<col style="width: 4%">
<col style="width: 6%">
<col style="width: 15%">
<col style="width: 14%">
<col style="width: 14%">
<col style="width: 13%">
<col style="width: 11%">
<col style="width: 8%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="11"><p>TLV 応答</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td rowspan="2"><p>タイプ</p></td>
<td rowspan="2"><p>長さ</p></td>
<td rowspan="2"><p>値</p></td>
<td rowspan="2"><p>タイプ</p></td>
<td rowspan="2"><p>長さ</p></td>
<td colspan="6"><p>値</p></td>
</tr>
<tr class="row-odd"><td><div class="line-block">
<div class="line">(バイト 0 ～ 3)</div>
<div class="line">スーパーフレーム期間</div>
<div class="line">マイクロ秒単位</div>
</div>
</td>
<td><div class="line-block">
<div class="line">(バイト 4 ～ 5)</div>
<div class="line">スロット期間</div>
<div class="line">マイクロ秒</div>
</div>
</td>
<td><div class="line-block">
<div class="line">(バイト 6 ～ 7)</div>
<div class="line">スーパーフレーム</div>
<div class="line">最大数</div>
</div>
</td>
<td><div class="line-block">
<div class="line">(バイト 8 ～ 9)</div>
<div class="line">アンカーの更新</div>
<div class="line">レート</div>
</div>
</td>
<td><div class="line-block">
<div class="line">(バイト 10)</div>
<div class="line">アクティブ</div>
<div class="line">プロファイルID</div>
</div>
</td>
<td><p>(バイト 11) 予約済み</p></td>
</tr>
<tr class="row-even"><td><p>0x40</p></td>
<td><p>0x01</p></td>
<td><p>0x00</p></td>
<td><p>0x5B</p></td>
<td><p>0x0C</p></td>
<td><p>0xA0 0x86
0x01 0x00</p></td>
<td><p>0xF4
0x01</p></td>
<td><p>0xa0
0x05</p></td>
<td><p>0x1E
0x00</p></td>
<td><p>0x02</p></td>
<td><p>0x00</p></td>
</tr>
</tbody>
</table>
<p>タイプ 0x5B(91 dec) は UWB プロファイル情報を意味します</p>
</div>


           </div>
