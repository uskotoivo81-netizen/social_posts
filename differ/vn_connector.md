---
title: MCP Server Là Gì? SpeedyIndex MCP Server cho Claude
seo_title: MCP server là gì? Tìm hiểu SpeedyIndex MCP cho Claude
meta_description: MCP server là gì? Tìm hiểu SpeedyIndex MCP server cho Claude: kiểm tra index Google/Yandex/Bing, tạo tác vụ indexing, theo dõi xếp hạng và backlink trong chat.
keyword: mcp server là gì (н.д. (vn; голова «mcp là gì» 2400/35))
tags: SEO, Artificial Intelligence, Marketing
cover: /home/claude/differ/vn_connector_cover.png
video: -
---

# MCP Server Là Gì? SpeedyIndex MCP Server cho Claude

MCP server là gì? Đó là máy chủ triển khai Model Context Protocol (MCP) — chuẩn mở do Anthropic giới thiệu tháng 11/2024 — cho phép trợ lý AI như Claude gọi công cụ bên ngoài. SpeedyIndex MCP server là connector như vậy: từ Claude bạn có thể kiểm tra index, tạo tác vụ indexing, xem dữ liệu xếp hạng và kiểm tra backlink ngay trong chat.

## MCP server là gì và SpeedyIndex khác gì?

Model Context Protocol cho phép AI gọi công cụ bên ngoài. SpeedyIndex có bản từ xa tại `mcp.speedyindex.com/mcp` (Streamable HTTP) và bản cục bộ qua npm `speedyindex-mcp` (key trong `SPEEDYINDEX_API_KEY`, Node.js 18+). Bản từ xa có 22 công cụ; bản npm có 14.

## SpeedyIndex MCP server làm được gì?

Trong 22 công cụ từ xa, 15 chỉ đọc miễn phí; 7 thay đổi tài khoản, trong đó 5 tốn token: `create_indexing_task`, `submit_single_url`, `create_index_check_task`, `create_backlink_check_task`, `rank_tracker_start_check`. Tạo dự án Rank Tracker và thêm từ khóa miễn phí; chạy kiểm tra tốn token, chi phí xem trước bằng `rank_tracker_get_check_cost`.

- Indexing: Google và Yandex, tối đa 10.000 URL; Google tính phí theo URL được index, URL không được index hoàn token tự động; drip feed 2–30 ngày.
- Kiểm tra index: Google, Yandex, Bing; tối đa 10.000 URL; trả về danh sách đã index / chưa index (kèm tiêu đề trang cho Google).
- Kiểm tra backlink: mở trang donor, kiểm tra liên kết, mã HTTP, anchor, nofollow, Moz DA và spam score; tối đa 50 domain; không tự khám phá.
- Rank Tracker (Google desktop): dự án, 5 khu vực, 10 đối thủ, vị trí, lịch sử 90 lần, AI Overview (xuất hiện, trích dẫn).

Để kiểm tra xem các trang có trong Google Index hay chưa, bạn có thể dùng [Google Index Checker hàng loạt](https://vn.speedyindex.com/kiem-tra-index-google/).

## Cách kết nối SpeedyIndex MCP server với Claude

Trên Claude web/desktop: vào Plugins → Add custom connector → đặt tên "SpeedyIndex", nhập URL `mcp.speedyindex.com/mcp` → Continue → Connect. Dán API key từ mục API trong tài khoản SpeedyIndex hoặc @speedyindexbot, chọn Connect. Không nhập key vào khung chat. Trong chat, bấm "+" → Connectors → bật SpeedyIndex. Kiểm tra: "Số dư SpeedyIndex của tôi là bao nhiêu?" — thấy token và credit là chạy.

Bạn có thể xem hướng dẫn chi tiết tại trang [SpeedyIndex MCP connector](https://vn.speedyindex.com/mcp/); trên hub có video 38 giây. Custom connector dùng mọi gói Claude; gói Free một connector. Team/Enterprise: Owner thêm ở Organization settings → Connectors, từng thành viên kết nối. Claude chỉ truy cập những gì bạn cho phép; custom connector không được Anthropic xác minh.

## Xác nhận, bảo mật và chi phí

Claude hỏi xác nhận trước mỗi lần gọi công cụ; có thể đặt Always allow. 7 công cụ thay đổi tài khoản — gồm 5 tốn token — luôn hỏi trừ khi Always allow. Máy chủ không lưu DB; key lưu trong token mã hóa. Access token 1 giờ, gia hạn tối đa 90 ngày; đổi key thu hồi mọi phiên. Connector miễn phí; tác vụ tốn token, không subscription; tài khoản mới 100 token miễn phí.

## Câu lệnh mẫu cho Claude

- "Số dư SpeedyIndex của tôi là bao nhiêu?" — miễn phí.
- "Liệt kê các tác vụ indexing gần đây và trạng thái?" — miễn phí.
- "Kiểm tra index Google cho 500 URL sau: <danh sách URL>" — tốn token.
- "Tạo tác vụ indexing Google cho 200 URL, drip feed 5 ngày" — tốn token.
- "Kiểm tra các trang donor sau còn liên kết đến domain của tôi không: <danh sách URL donor>" — tốn token, cần URL donor cụ thể.

## Câu hỏi thường gặp

### MCP server là gì và SpeedyIndex MCP server có miễn phí không?

MCP server là máy chủ theo chuẩn Model Context Protocol cho Claude gọi công cụ bên ngoài. Connector SpeedyIndex miễn phí; tác vụ tốn token. Tài khoản mới có 100 token miễn phí.

### SpeedyIndex MCP server hỗ trợ những chức năng gì?

Kiểm tra index Google/Yandex/Bing, tạo tác vụ indexing Google/Yandex, kiểm tra backlink trên trang donor, Rank Tracker Google với vị trí và AI Overview. 15 công cụ chỉ đọc miễn phí.

### Làm thế nào để kết nối SpeedyIndex MCP server với Claude?

Vào Plugins → Add custom connector, nhập URL `mcp.speedyindex.com/mcp`, đăng nhập bằng API key SpeedyIndex, bật connector trong chat. Có thể chạy cục bộ qua npm với biến `SPEEDYINDEX_API_KEY`.