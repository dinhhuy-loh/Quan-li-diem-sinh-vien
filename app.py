
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Cau hinh trang web
st.set_page_config(
    page_title="Quan ly diem sinh vien",
    page_icon="📚",
    layout="wide"
)

# Tao du lieu 10 sinh vien
data = {
    "Ho ten": [
        "Nguyen Van An", "Tran Thi Binh",
        "Le Van Cuong", "Pham Thi Dung",
        "Hoang Van Em", "Vo Thi Giang",
        "Dang Van Hung", "Bui Thi Lan",
        "Do Van Minh", "Nguyen Thi Hoa"
    ],
    "Chuyen can": [9, 8, 7, 10, 6, 8, 9, 7, 5, 10],
    "Giua ky": [8, 7, 6, 9, 5, 8, 8, 6, 4, 9],
    "Cuoi ky": [9, 8, 7, 9, 4, 9, 8, 5, 3, 10]
}

df = pd.DataFrame(data)

# Tinh diem tong ket
df["Tong ket"] = (
    0.2 * df["Chuyen can"]
    + 0.3 * df["Giua ky"]
    + 0.5 * df["Cuoi ky"]
).round(2)

# Xep loai
def xep_loai(diem):
    if diem >= 8.5:
        return "Gioi"
    elif diem >= 7:
        return "Kha"
    elif diem >= 5:
        return "Trung binh"
    return "Yeu"

df["Xep loai"] = df["Tong ket"].apply(xep_loai)

# Tieu de
st.title("QUẢN LÝ ĐIỂM SINH VIÊN")
st.markdown("---")

# 1. Bang diem
st.header("1. Bảng điểm sinh viên")
st.dataframe(df, use_container_width=True, hide_index=True)

# 2. Thong ke
st.header("2. Thống kê kết quả")

diem_tb = df["Tong ket"].mean()
idx_max = df["Tong ket"].idxmax()
idx_min = df["Tong ket"].idxmin()
so_sinh_vien_dat = (df["Tong ket"] >= 5).sum()

cot1, cot2, cot3, cot4 = st.columns(4)

cot1.metric("Điểm trung bình", f"{diem_tb:.2f}")
cot2.metric(
    "Điểm cao nhất",
    f"{df.loc[idx_max, 'Tong ket']:.2f}"
)
cot3.metric(
    "Điểm thấp nhất",
    f"{df.loc[idx_min, 'Tong ket']:.2f}"
)
cot4.metric("Số sinh viên đạt", f"{so_sinh_vien_dat}/10")

st.write(
    "Sinh viên cao điểm nhất:",
    df.loc[idx_max, "Ho ten"]
)
st.write(
    "Sinh viên thấp điểm nhất:",
    df.loc[idx_min, "Ho ten"]
)

# 3. Chon sinh vien
st.header("3. Tra cứu điểm sinh viên")

ten_sv = st.selectbox(
    "Chọn một sinh viên:",
    df["Ho ten"].tolist()
)

sv = df[df["Ho ten"] == ten_sv].iloc[0]

st.subheader(f"Thông tin sinh viên: {ten_sv}")

c1, c2, c3 = st.columns(3)
c1.metric("Chuyên cần", f"{sv['Chuyen can']:.2f}")
c2.metric("Giữa kỳ", f"{sv['Giua ky']:.2f}")
c3.metric("Cuối kỳ", f"{sv['Cuoi ky']:.2f}")

c4, c5 = st.columns(2)
c4.metric("Điểm tổng kết", f"{sv['Tong ket']:.2f}")
c5.metric("Xếp loại", sv["Xep loai"])

# 4. Bieu do cot
st.header("4. Biểu đồ điểm tổng kết")

fig, ax = plt.subplots(figsize=(12, 5))
bars = ax.bar(df["Ho ten"], df["Tong ket"])

ax.set_title("ĐIỂM TỔNG KẾT CỦA 10 SINH VIÊN")
ax.set_xlabel("Họ tên sinh viên")
ax.set_ylabel("Điểm tổng kết")
ax.set_ylim(0, 10)
ax.tick_params(axis="x", labelrotation=45)

# Hien diem tren dau cot
ax.bar_label(bars, fmt="%.2f", padding=3)

fig.tight_layout()
st.pyplot(fig)
plt.close(fig)

# 5. Thong tin nguoi tao
st.markdown("---")
st.caption("Người tạo ứng dụng: [Nguyễn Đình Huy] | MSSV: [066208018496]")
