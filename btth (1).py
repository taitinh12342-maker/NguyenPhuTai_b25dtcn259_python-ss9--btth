branch_names = ["Highlands Nha Tho", "Highlands Ba Trieu", "Highlands Nguyen Du", "Highlands Landmark 81", "Highlands Tran Hưng Đạo"]
daily_revenues = [15500000, 28000000, 9200000, 45000000, 11000000] 
target_achieved = [True, True, False, True, False] 

while True:
    choice = input("""
===== HỆ THONG QUẢN LÝ DOANH THU HIGHLANDS =====
1. Hiển thị báo cáo doanh thu tổng hợp
2. Thống kê chi nhánh Cao nhất / Thấp nhất
3. Lọc danh sách cơ sở kém (không đạt chỉ tiêu)
4. Thoát chương trình
================================================
Nhập lựa chọn của bạn (1-4): """)
    if not choice.isdigit():
        print("Sai định dạng nhập vào")
        continue
    choice = int(choice)
    match choice:
        case 1:
            display_title_name = "Tên Cơ Sở"
            display_title_total = "Doanh Thu"
            display_title_status = "Trạng Thái"
            max_display_name = len(max(branch_names, key=len))
            max_display_total = len(str(max(daily_revenues))) + 3
            sum = 0
            print("--- BÁO CÁO DOANH THU TỔNG HỢP ---")
            print(f"{display_title_name:<{max_display_name}} | {display_title_total:<{max_display_total}} | {display_title_status:<15}")
            for j in range(max_display_name + max_display_total + 15 + 1):
                print("-", end = "")
            print()
            for i in range(len(branch_names)):
                if target_achieved[i] == True:
                    status = "Đạt"
                else:
                    status = "Chưa đạt"
                print(f"{branch_names[i]:<{max_display_name}} | {daily_revenues[i]:<{max_display_total}} | {status:<15}")
            for k in range(max_display_name + max_display_total + 15 + 1):
                    print("-", end = "")
            print()
            for h in range(len(daily_revenues)):
                sum += daily_revenues[h]
            print(f"=> DOANH THU TOÀN VÙNG: {sum} VND")
        case 2:
            print("--- THỐNG KÊ CƠ SỞ NỔI BẬT ---")
            idx_total_max = daily_revenues.index(max(daily_revenues))
            idx_total_min = daily_revenues.index(min(daily_revenues))
            print(f"- Cơ sở có doanh thu CAO NHẤT: {branch_names[idx_total_max]} ({daily_revenues[idx_total_max]} VND)")
            print(f"- Cơ sở có doanh thu THẤP NHẤT: {branch_names[idx_total_min]} ({daily_revenues[idx_total_min]} VND)")
        case 3:
            print("--- DANH SÁCH CƠ SỞ CẦN HỖ TRỢ TRA CỨU ĐƯỢC ---")
            failed_branches = []
            for i in range(len(daily_revenues)):
                if target_achieved[i] == False:
                    failed_branches.append(branch_names[i])
            print(failed_branches)
        case 4:
            print("Hệ thống ghi nhận dữ liệu hoàn tất. Tạm biệt!")
            break
        case _:
            print("[Lỗi] Lựa chọn không hợp lệ, vui lòng nhập lại số từ 1 đến 4!")