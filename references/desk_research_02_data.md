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
- Market size vs company revenue
- Enterprise spend vs private investment vs corporate investment
- Capex vs opex vs transaction value
- Funding round size vs cumulative capital raised
- Private-company valuation vs public-company market capitalization
- M&A transaction value vs minority/strategic investment
- Technology segment vs buyer vertical vs deployment model

## Normalization record

Mỗi phép biến đổi phải ghi:

- source value/unit/time;
- target unit/time;
- formula;
- FX/CPI/PPP series;
- base year;
- rounding;
- limitations.

## Data-vintage consistency

Mỗi số liệu phải có tối thiểu bốn mốc:

1. `reference_period`: kỳ mà số liệu đo lường;
2. `publication_date`: ngày nguồn công bố;
3. `access_date`: ngày truy cập;
4. `as_of_date`: ngày báo cáo khóa dữ liệu.

Bắt buộc kiểm tra:

- năm gắn nhãn trong bảng có đúng với kỳ của giao dịch/sự kiện hay không;
- fiscal year và calendar year có bị trộn hay không;
- số liệu năm đã kết thúc còn bị trình bày là estimate dựa trên nửa đầu năm hay không;
- báo cáo cập nhật sau kỳ dữ liệu có dùng nguồn/revision mới nhất hay không;
- cover, footer, version, copyright và câu hẹn cập nhật có nhất quán về thời gian hay không.

Không được đặt một sự kiện xảy ra năm `t+1` vào cột năm `t` chỉ vì báo cáo có tiêu đề năm `t`. Nếu dùng dữ liệu mới hơn để cập nhật một báo cáo lịch sử, phải gắn nhãn `LATEST AS-OF` và tách khỏi chuỗi thời gian gốc.

## Market-size reconciliation

Báo cáo `industry-market` không được dùng một con số TAM duy nhất nếu các nguồn có taxonomy khác nhau. Tối thiểu phải lập `market_size_reconciliation.csv` với các trường:

```csv
estimate_id,metric_name,value,unit,reference_year,forecast_year,publisher,publication_date,scope_definition,included_layers,excluded_layers,geography,methodology,actual_or_forecast,overlap_risk,comparability_group,confidence,notes
```

Quy trình:

1. Xác định rõ chỉ tiêu là **revenue**, **spend**, **investment**, **capex**, **transaction value**, **valuation** hay **economic impact**.
2. Nhóm các estimate chỉ khi cùng định nghĩa, địa lý, kỳ và phạm vi.
3. Công bố range hoặc median của nhóm so sánh được; không lấy trung bình cơ học của các taxonomy khác nhau.
4. Nếu phân bổ tổng thị trường xuống các lớp, phải có bridge từ tổng đến từng lớp và quy tắc loại trùng.
5. Tổng các lớp con phải reconcile với lớp cha trong sai số làm tròn đã công bố.
6. Nếu một vertical hoặc technology segment lớn hơn lớp cha, phải giải thích rằng hai taxonomy giao cắt; không trình bày như cấu trúc cộng dồn.
7. Không dùng con số từ nhiều hãng nghiên cứu để ép tổng các lớp bằng đúng một TAM đã chọn.

### Ma trận taxonomy tối thiểu cho industry-market

| Trục | Ví dụ | Có cộng dồn không? |
|---|---|---|
| Chuỗi giá trị | chip, cloud, model, middleware, application, services | Có thể, chỉ khi loại trùng và cùng định nghĩa revenue |
| Công nghệ | ML, GenAI, vision, NLP, robotics | Thường giao cắt; không cộng máy móc |
| Triển khai | cloud, private/on-prem, edge | Có thể nếu nguồn dùng các nhóm loại trừ nhau |
| Ngành sử dụng | finance, health, retail, manufacturing | Có thể nếu đo cùng loại chi tiêu và loại trừ nhau |
| Địa lý | US, China, Europe, APAC | Có thể nếu cùng base và không trùng khu vực |
| Loại dòng tiền | revenue, spend, investment, capex, valuation | Không được cộng với nhau |

## Company-event normalization

Mọi bảng về công ty phải tách:

- public market cap;
- private post-money valuation;
- funding round size;
- cumulative capital raised;
- strategic investment commitment;
- completed cash paid;
- announced M&A value;
- revenue/run-rate revenue;
- fiscal-year revenue.

Với valuation/funding/M&A, ghi rõ `event_date`, `deal_status`, `pre_or_post_money`, `primary_or_secondary`, `source_type` và `as_of_date`. Không xếp strategic investment vào M&A nếu không có chuyển quyền kiểm soát hoặc mua lại doanh nghiệp/tài sản.

## Precision and uncertainty policy

- Số gốc giữ độ chính xác của nguồn.
- Số tổng hợp từ taxonomy không đồng nhất không được trình bày với độ chính xác giả tạo đến một chữ số thập phân.
- Uncertainty band phải đến từ range nguồn, sensitivity, historical forecast error hoặc mô hình xác suất; không tự đặt `±10-15%` chỉ để tạo cảm giác định lượng.
- Prescriptive ratio như “chi 5-10% ngân sách IT” chỉ được dùng khi có benchmark phù hợp theo ngành/quy mô và phải ghi rõ phân vị, mẫu khảo sát và điều kiện áp dụng.

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
