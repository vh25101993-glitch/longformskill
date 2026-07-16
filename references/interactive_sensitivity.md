# Interactive Scenario & Sensitivity Charts

Chuẩn này dùng cho báo cáo Financial HTML khi người đọc cần **điều chỉnh giả định tăng/giảm và nhìn thấy kết quả thay đổi theo thời gian thực**.

Mục tiêu không phải tạo một “máy dự báo”. Mục tiêu là minh bạch hóa quan hệ:

> Input giả định → công thức/mô hình → output → độ nhạy → điều kiện hòa vốn/đảo chiều.

## 1. Khi nào bắt buộc

Dùng Scenario & Sensitivity Lab khi thỏa cả hai điều kiện:

1. Kết quả phụ thuộc vào một hoặc nhiều biến có thể thay đổi.
2. Quan hệ giữa input và output có công thức, accounting identity, mô hình định lượng hoặc logic truyền dẫn đủ cơ sở.

Ví dụ phù hợp:

| Nhóm báo cáo | Input có thể điều chỉnh | Output nên hiển thị |
|---|---|---|
| Doanh nghiệp phi tài chính | tăng trưởng doanh thu, biên gộp, SG&A/doanh thu, thuế suất, P/E, EV/EBITDA, WACC | doanh thu, EBIT, LNST, EPS, giá trị hợp lý |
| Ngân hàng | tăng trưởng tín dụng, NIM, CIR, cost of credit, thuế suất, P/B | NII, PBT, ROE, BVPS, giá trị hợp lý |
| Bất động sản | giá bán, absorption, cap rate, lãi vay, tiến độ bàn giao | doanh thu, dòng tiền, NAV, DSCR |
| Tài sản/portfolio | lợi suất kỳ vọng, volatility, FX, phí, lạm phát, tỷ trọng | nominal return, real return, drawdown proxy, terminal value |
| Macro/policy | lãi suất, pass-through, độ trễ, tỷ giá, tăng trưởng | output mô hình có công thức rõ |

Không dùng khi chỉ có tương quan quan sát hoặc nhận định định tính. Trong trường hợp đó, dùng các kịch bản rời rạc và ghi rõ “không phải mô hình liên tục”.

## 2. Phân loại dữ liệu

Mỗi giá trị phải có nhãn:

- `FACT`: số liệu nguồn, không thay đổi bởi control.
- `DERIVED`: số tính từ `FACT`.
- `SCENARIO`: giả định do người dùng hoặc preset chọn.
- `DERIVED-SCENARIO`: output sinh từ mô hình kịch bản.
- `FORECAST`: chỉ dùng khi có dự báo độc lập, không đồng nhất với giá trị kéo từ slider.

Không vẽ `FACT` và `SCENARIO` cùng một series mà không phân biệt legend, màu hoặc nét.

## 3. Thành phần bắt buộc

### 3.1 Control panel

Mỗi biến có:

- tên rõ nghĩa;
- đơn vị;
- `min`, `max`, `step`, `default`;
- nguồn hoặc căn cứ của baseline;
- căn cứ chọn miền giá trị;
- `<input type="range">` và `<output>` hoặc ô số đồng bộ;
- `aria-label`/`aria-describedby`.

Khuyến nghị tối đa 5 control trong một lab. Nếu nhiều hơn, chia thành nhóm “Hoạt động”, “Tài chính”, “Định giá”.

### 3.2 Output panel

Hiển thị 2-5 KPI quan trọng nhất:

- giá trị hiện tại;
- chênh lệch tuyệt đối so với baseline;
- chênh lệch % nếu mẫu số phù hợp;
- nhãn đơn vị;
- trạng thái `DERIVED-SCENARIO`.

Không làm tròn quá sớm trong hàm tính. Chỉ format tại lớp hiển thị.

### 3.3 Dynamic chart

Ưu tiên:

1. **One-way sensitivity line:** chọn một biến làm trục x; giữ các biến khác tại giá trị hiện tại.
2. **Tornado chart:** thay từng biến từ low → high, đo thay đổi output so với baseline.
3. **Breakeven curve:** thể hiện điểm output bằng 0 hoặc đạt threshold.
4. **Two-way heatmap:** hai input và một output; chỉ dùng khi ECharts hoặc plugin heatmap đã khóa phiên bản.
5. **Waterfall bridge:** giải thích chênh lệch baseline → scenario.

Một lab có thể chứa tối đa 2 chart. Tránh biến thành dashboard dày đặc.

### 3.4 Actions

- `Reset`: khôi phục baseline.
- `Bear / Base / Bull`: chỉ dùng khi preset có định nghĩa và căn cứ.
- `Download JSON/CSV`: tùy chọn.
- `Copy scenario link`: chỉ dùng nếu HTML có cơ chế serialize state ổn định.

## 4. Data contract đề xuất

```js
const MODEL = {
  version: '1.0.0',
  baselinePeriod: 'FY2026',
  currency: 'VND bn',
  parameters: {
    revenueGrowth: {
      label: 'Tăng trưởng doanh thu',
      unit: '%',
      min: -10,
      max: 30,
      step: 0.5,
      baseline: 8,
      source: 'Kế hoạch doanh nghiệp / giả định phân tích',
      status: 'SCENARIO'
    },
    grossMargin: {
      label: 'Biên lợi nhuận gộp',
      unit: '%',
      min: 20,
      max: 50,
      step: 0.5,
      baseline: 35,
      source: 'BCTC và lịch sử biên',
      status: 'SCENARIO'
    }
  },
  outputs: {
    pat: { label: 'LNST', unit: 'VND bn', status: 'DERIVED-SCENARIO' }
  }
};
```

`chart_manifest.csv` của chart tương tác phải ghi thêm:

- `interactive=true`;
- parameter keys;
- baseline/min/max/step;
- model version;
- formula;
- output metrics;
- presets;
- assumptions held constant;
- expected direction;
- fallback table.

## 5. Component mẫu: multi-input one-way sensitivity

Ví dụ dưới đây dùng Chart.js 4.4.1. Người dùng thay đổi ba giả định; chart biểu diễn quan hệ giữa **biến được chọn trên trục x** và LNST, trong khi các biến còn lại giữ tại giá trị hiện hành.

### 5.1 HTML

```html
<div class="scenario-lab" id="profitLab">
  <div class="scenario-head">
    <div>
      <span class="scenario-badge">SCENARIO · model v1.0</span>
      <h4>Scenario & Sensitivity Lab</h4>
      <p>Điều chỉnh giả định và quan sát LNST thay đổi theo điều kiện ceteris paribus.</p>
    </div>
    <button type="button" class="scenario-reset" id="profitReset">Reset baseline</button>
  </div>

  <div class="scenario-layout">
    <div class="scenario-controls">
      <label class="scenario-control">
        <span>Tăng trưởng doanh thu <output id="revenueGrowthOut">8,0%</output></span>
        <input id="revenueGrowth" data-sensitivity-control type="range"
               min="-10" max="30" step="0.5" value="8"
               aria-label="Tăng trưởng doanh thu">
      </label>

      <label class="scenario-control">
        <span>Biên lợi nhuận gộp <output id="grossMarginOut">35,0%</output></span>
        <input id="grossMargin" data-sensitivity-control type="range"
               min="20" max="50" step="0.5" value="35"
               aria-label="Biên lợi nhuận gộp">
      </label>

      <label class="scenario-control">
        <span>Chi phí hoạt động / doanh thu <output id="opexRatioOut">18,0%</output></span>
        <input id="opexRatio" data-sensitivity-control type="range"
               min="10" max="30" step="0.5" value="18"
               aria-label="Chi phí hoạt động trên doanh thu">
      </label>

      <label class="scenario-select">
        <span>Biến trên trục x</span>
        <select id="profitDriver">
          <option value="revenueGrowth">Tăng trưởng doanh thu</option>
          <option value="grossMargin">Biên lợi nhuận gộp</option>
          <option value="opexRatio">Chi phí hoạt động / doanh thu</option>
        </select>
      </label>
    </div>

    <div class="scenario-results" aria-live="polite">
      <div class="scenario-kpi"><small>Doanh thu</small><strong id="scenarioRevenue" data-sensitivity-output>—</strong></div>
      <div class="scenario-kpi"><small>EBIT</small><strong id="scenarioEbit" data-sensitivity-output>—</strong></div>
      <div class="scenario-kpi"><small>LNST</small><strong id="scenarioPat" data-sensitivity-output>—</strong></div>
      <div class="scenario-kpi"><small>Δ LNST vs baseline</small><strong id="scenarioDelta" data-sensitivity-output>—</strong></div>
    </div>
  </div>

  <div class="chart-wrap tall"><canvas id="profitSensitivityChart"></canvas></div>

  <details class="scenario-disclosure">
    <summary>Công thức và giới hạn</summary>
    <p>Doanh thu = doanh thu gốc × (1 + tăng trưởng); EBIT = doanh thu × (biên gộp − tỷ lệ chi phí hoạt động); LNST = EBIT × (1 − thuế suất). Mô hình giữ thuế suất 20% và không phản ánh vốn lưu động, chi phí tài chính, lợi ích cổ đông thiểu số hoặc yếu tố bất thường.</p>
  </details>
</div>
```

### 5.2 CSS

```css
.scenario-lab{margin:24px 0;padding:22px;border:1px solid var(--line);border-radius:18px;background:linear-gradient(180deg,rgba(59,130,246,.08),rgba(15,23,42,.7))}
.scenario-head{display:flex;justify-content:space-between;gap:18px;align-items:flex-start;margin-bottom:18px}
.scenario-head h4{margin:5px 0 4px;color:#fff}.scenario-head p{margin:0;color:var(--muted);font-size:.88rem}
.scenario-badge{display:inline-block;font-size:.68rem;letter-spacing:.08em;font-weight:800;color:#93c5fd}
.scenario-reset{border:1px solid rgba(59,130,246,.45);background:rgba(59,130,246,.12);color:#bfdbfe;border-radius:9px;padding:8px 12px;cursor:pointer;white-space:nowrap}
.scenario-layout{display:grid;grid-template-columns:minmax(250px,.9fr) minmax(300px,1.1fr);gap:18px}
.scenario-controls{display:grid;gap:14px}.scenario-control,.scenario-select{display:grid;gap:7px;color:#cbd5e1;font-size:.84rem}
.scenario-control>span,.scenario-select>span{display:flex;justify-content:space-between;gap:12px}.scenario-control output{color:#fbbf24;font-weight:800;font-variant-numeric:tabular-nums}
.scenario-control input[type="range"]{width:100%;accent-color:#3b82f6}.scenario-select select{width:100%;background:var(--bg2);color:var(--txt);border:1px solid var(--line);border-radius:9px;padding:9px 10px}
.scenario-results{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:12px}.scenario-kpi{padding:16px;border-radius:13px;background:rgba(255,255,255,.035);border:1px solid var(--line)}
.scenario-kpi small{display:block;color:var(--muted);margin-bottom:8px}.scenario-kpi strong{font-size:1.35rem;color:#fbbf24;font-variant-numeric:tabular-nums}
.scenario-disclosure{margin-top:14px;color:var(--muted);font-size:.82rem}.scenario-disclosure summary{cursor:pointer;color:#bfdbfe}
@media(max-width:760px){.scenario-head{display:grid}.scenario-layout{grid-template-columns:1fr}.scenario-results{grid-template-columns:1fr 1fr}}
@media(max-width:420px){.scenario-results{grid-template-columns:1fr}}
@media print{.scenario-controls,.scenario-reset{display:none!important}.scenario-lab{background:#fff;color:#111;border-color:#bbb}}
```

### 5.3 JavaScript

```js
(function(){
  'use strict';

  const BASE = Object.freeze({ revenue:1000, revenueGrowth:8, grossMargin:35, opexRatio:18, taxRate:20 });
  const PARAMS = {
    revenueGrowth:{label:'Tăng trưởng doanh thu',unit:'%',min:-10,max:30,step:.5},
    grossMargin:{label:'Biên lợi nhuận gộp',unit:'%',min:20,max:50,step:.5},
    opexRatio:{label:'Chi phí hoạt động / doanh thu',unit:'%',min:10,max:30,step:.5}
  };
  const ids = ['revenueGrowth','grossMargin','opexRatio'];
  const controls = Object.fromEntries(ids.map(function(id){ return [id,document.getElementById(id)]; }));
  const outputs = Object.fromEntries(ids.map(function(id){ return [id,document.getElementById(id+'Out')]; }));
  const driver = document.getElementById('profitDriver');
  const reset = document.getElementById('profitReset');

  function model(v){
    const revenue = BASE.revenue * (1 + v.revenueGrowth / 100);
    const ebit = revenue * ((v.grossMargin - v.opexRatio) / 100);
    const pat = ebit * (1 - BASE.taxRate / 100);
    return {revenue:revenue,ebit:ebit,pat:pat};
  }
  function readState(){
    return {revenueGrowth:Number(controls.revenueGrowth.value),grossMargin:Number(controls.grossMargin.value),opexRatio:Number(controls.opexRatio.value)};
  }
  function formatNumber(v){ return new Intl.NumberFormat('vi-VN',{maximumFractionDigits:1}).format(v); }
  function formatPct(v){ return new Intl.NumberFormat('vi-VN',{minimumFractionDigits:1,maximumFractionDigits:1}).format(v)+'%'; }
  function buildCurve(state,key){
    const p = PARAMS[key];
    const points = [];
    const steps = Math.round((p.max-p.min)/p.step);
    for(let i=0;i<=steps;i+=1){
      const x = Number((p.min+i*p.step).toFixed(6));
      const scenario = Object.assign({},state,{[key]:x});
      points.push({x:x,y:model(scenario).pat});
    }
    return points;
  }

  const baselinePat = model(BASE).pat;
  const chart = new Chart(document.getElementById('profitSensitivityChart'),{
    type:'line',
    data:{datasets:[
      {label:'LNST theo biến được chọn',data:[],borderColor:'#3b82f6',backgroundColor:'rgba(59,130,246,.12)',borderWidth:3,pointRadius:0,tension:.2,fill:true},
      {label:'Kịch bản hiện tại',type:'scatter',data:[],pointRadius:6,pointHoverRadius:8,backgroundColor:'#f59e0b',borderColor:'#fff',borderWidth:1}
    ]},
    options:{responsive:true,maintainAspectRatio:false,parsing:false,animation:false,
      plugins:{legend:{position:'top'},tooltip:{callbacks:{label:function(ctx){return ctx.dataset.label+': '+formatNumber(ctx.parsed.y);}}}},
      scales:{x:{type:'linear',grid:{color:'#334155'},title:{display:true,text:'Giả định (%)',color:'#94a3b8'}},y:{grid:{color:'#334155'},title:{display:true,text:'LNST (đơn vị mô hình)',color:'#94a3b8'}}}}
  });

  let frame = 0;
  function render(){
    cancelAnimationFrame(frame);
    frame = requestAnimationFrame(function(){
      const state = readState();
      const result = model(state);
      const key = driver.value;
      const meta = PARAMS[key];
      ids.forEach(function(id){ outputs[id].textContent = formatPct(state[id]); });
      document.getElementById('scenarioRevenue').textContent = formatNumber(result.revenue);
      document.getElementById('scenarioEbit').textContent = formatNumber(result.ebit);
      document.getElementById('scenarioPat').textContent = formatNumber(result.pat);
      const delta = result.pat - baselinePat;
      document.getElementById('scenarioDelta').textContent = (delta>=0?'+':'')+formatNumber(delta);
      chart.data.datasets[0].data = buildCurve(state,key);
      chart.data.datasets[1].data = [{x:state[key],y:result.pat}];
      chart.options.scales.x.min = meta.min;
      chart.options.scales.x.max = meta.max;
      chart.options.scales.x.title.text = meta.label+' ('+meta.unit+')';
      chart.update('none');
    });
  }

  ids.forEach(function(id){ controls[id].addEventListener('input',render); });
  driver.addEventListener('change',render);
  reset.addEventListener('click',function(){
    ids.forEach(function(id){ controls[id].value = BASE[id]; });
    driver.value = 'revenueGrowth';
    render();
  });
  render();
})();
```

## 6. Preset Bear/Base/Bull

Preset chỉ là shortcut cho bộ input, không phải xác suất.

```js
const PRESETS = {
  bear:{revenueGrowth:-3,grossMargin:31,opexRatio:21},
  base:{revenueGrowth:8,grossMargin:35,opexRatio:18},
  bull:{revenueGrowth:18,grossMargin:39,opexRatio:16}
};
function applyPreset(name){
  const preset = PRESETS[name];
  if(!preset) return;
  Object.keys(preset).forEach(function(key){
    const el = document.getElementById(key);
    el.value = Math.min(Number(el.max),Math.max(Number(el.min),preset[key]));
  });
  render();
}
```

Mỗi preset phải công bố input, căn cứ và phần không bao gồm.

## 7. Tornado chart

Tornado đo tác động độc lập của từng biến:

1. Giữ các biến khác tại baseline.
2. Đưa một biến về low và high.
3. Tính `output_low - output_baseline` và `output_high - output_baseline`.
4. Sắp xếp theo biên độ tác động lớn nhất.
5. Dùng horizontal floating bar hoặc hai bar đối xứng.

Không dùng tornado để tuyên bố “đóng góp” nếu mô hình phi tuyến hoặc biến tương tác mạnh. Khi đó ghi “one-at-a-time sensitivity”.

## 8. Two-way heatmap

Heatmap phù hợp với hai input quan trọng như:

- tăng trưởng doanh thu × biên gộp → LNST;
- NIM × cost of credit → ROE;
- WACC × terminal growth → giá trị DCF;
- cap rate × NOI → giá trị tài sản.

Yêu cầu: tối đa 11×11 hoặc 15×15 ô; trục và đơn vị rõ; highlight ô hiện tại; tooltip có cả hai input và output; bảng số liệu fallback; không nội suy màu thành mức chính xác giả.

## 9. QA checklist

### Model integrity

- [ ] Baseline khớp dữ liệu đã audit.
- [ ] Formula khớp text, table và chart.
- [ ] Tất cả input có min/max/step/default/đơn vị.
- [ ] Không có số ngẫu nhiên hoặc network call.
- [ ] Không chia cho 0; không sinh `NaN`/`Infinity`.
- [ ] Quy tắc thuế/lỗ/âm được công bố.
- [ ] Expected direction được kiểm tra bằng test điểm thấp/cao.

### Interaction

- [ ] Kéo từng slider làm output thay đổi.
- [ ] Chọn driver làm trục x cập nhật label và curve.
- [ ] Điểm hiện tại nằm trên đường sensitivity.
- [ ] Reset khôi phục baseline.
- [ ] Preset nằm trong range.
- [ ] Keyboard điều khiển được range/select/button.
- [ ] Mobile 390 px không chồng lấn.

### Disclosure

- [ ] Có badge `SCENARIO`.
- [ ] Có model version.
- [ ] Có công thức và assumptions held constant.
- [ ] Có limitation.
- [ ] `FACT` và `SCENARIO` được phân biệt.
- [ ] Có fallback table.

### Technical

- [ ] Chỉ khởi tạo chart một lần.
- [ ] Dùng `chart.update('none')`.
- [ ] Không có listener trùng.
- [ ] Console không có error.
- [ ] CDN fail vẫn còn bảng/công thức.
- [ ] Print mode ẩn control hoặc in baseline hiện hành có nhãn.

## 10. Hard fail

Không publish nếu có một trong các lỗi:

- slider không làm kết quả thay đổi;
- kết quả thay đổi ngược công thức mà không giải thích;
- baseline không truy xuất được;
- range không có căn cứ hoặc vượt miền kinh tế hợp lý;
- scenario được trình bày như dữ liệu thực;
- chart cập nhật nhưng KPI/table không cập nhật cùng dataset;
- output sinh `NaN`, `Infinity`, giá trị âm bất khả thi mà không có rule;
- preset Bear/Base/Bull không công bố input;
- dùng mô hình liên tục cho quan hệ chỉ có bằng chứng định tính;
- thiếu limitation hoặc fallback.

## 11. Quy tắc lựa chọn mức độ phức tạp

| Mức | Điều kiện | Thành phần |
|---|---|---|
| S1 | 1 input, 1 output | slider + KPI + one-way line |
| S2 | 2-3 input, 2-4 output | multi-control + driver selector + line + reset |
| S3 | 4-5 input, mô hình định giá | groups + presets + tornado/heatmap + export |
| Không mô hình | quan hệ chưa đủ cơ sở | kịch bản rời rạc + bảng giả định + caveat |

Mặc định dùng **S2** cho báo cáo tài chính doanh nghiệp và **S1** cho báo cáo giải thích cơ chế đơn giản.
