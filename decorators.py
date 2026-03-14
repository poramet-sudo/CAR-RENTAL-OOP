from fastapi import Request, HTTPException, status
from app.utils.flash import set_flash
from fastapi.responses import RedirectResponse

# ฟังก์ชันดักจับ: ต้องเข้าสู่ระบบ (Login Required)
async def login_required(request: Request):
    user_id = request.session.get("user_id")
    if not user_id:
        set_flash(request, "กรุณาเข้าสู่ระบบก่อนเข้าถึงหน้านี้", "warning")
        # สร้าง Exception พิเศษเพื่อให้ระบบ Redirect ไปหน้า Login
        raise HTTPException(
            status_code=status.HTTP_303_SEE_OTHER,
            headers={"Location": "/login"}
        )
    return {
        "id": user_id, 
        "username": request.session.get("username"), 
        "role": request.session.get("role")
    }

# ฟังก์ชันดักจับ: ต้องเป็น Admin เท่านั้น (Admin Required)
async def admin_required(request: Request):
    # เรียกใช้ตัวเช็ค Login ก่อน
    user = await login_required(request)
    if user["role"] != "admin":
        set_flash(request, "คุณไม่มีสิทธิ์เข้าถึงส่วนของผู้ดูแลระบบ", "danger")
        raise HTTPException(
            status_code=status.HTTP_303_SEE_OTHER,
            headers={"Location": "/"}
        )
    return user