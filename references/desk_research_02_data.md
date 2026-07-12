# Data Quality and Normalization

## Data Quality dimensions

1. Completeness
2. Accuracy
3. Consistency
4. Timeliness
5. Comparability
6. Granularity
7. Revision risk
8. Provenance

## Các cặp dễ nhầm

- GDP nominal vs real
- GDP per capita current USD vs constant USD vs PPP
- GDP vs GNI/GNP
- Household saving rate vs gross national saving
- Household debt/GDP vs debt/disposable income
- Mean wealth vs median wealth
- Bank accounts vs account owners
- Securities accounts vs unique investors
- Listed price vs transaction price
- New home vs existing home
- Average price vs year-end close vs annual peak
- Buy price vs sell price

## Normalization record

Mỗi phép biến đổi phải ghi:

- source value/unit/time;
- target unit/time;
- formula;
- FX/CPI/PPP series;
- base year;
- rounding;
- limitations.

## Interpolation policy

Chỉ nội suy khi:

- mục tiêu là visualization/trend, không phải event inference;
- missing gap ngắn và series đủ mượt;
- phương pháp được ghi rõ;
- chart đánh dấu điểm nội suy;
- kết luận được kiểm tra lại khi loại các điểm nội suy.

Không nội suy qua structural break, crisis, policy change hoặc gap dài.

## Phase comparison

Khi so sánh trước/sau:

- dùng cùng chỉ tiêu và phương pháp đo;
- kiểm tra số năm mỗi phase;
- tách level, growth và volatility;
- tránh kết luận từ trung bình bị chi phối bởi một outlier;
- chạy sensitivity với breakpoint +/- 1-3 năm khi phù hợp.

## Sign convention

Mỗi spread/premium phải định nghĩa trước:

```text
premium_pct = (domestic_equivalent - global_equivalent) / global_equivalent * 100
```

- `premium_pct > 0`: premium
- `premium_pct < 0`: discount

QA phải bắt lỗi label trái dấu.
