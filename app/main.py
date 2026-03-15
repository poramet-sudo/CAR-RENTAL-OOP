from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from starlette.middleware.sessions import SessionMiddleware
from starlette.exceptions import HTTPException as StarletteHTTPException
from fastapi.responses import RedirectResponse
# 1. นำเข้าตัวจัดการ Exception พื้นฐานของ FastAPI
from fastapi.exception_handlers import http_exception_handler 

from app.core.database import engine, Base
from app.utils.flash import get_flashed_messages

# นำเข้า Router ทั้งหมด
from app.routers import auth_web
from app.routers import vehicle_web  # ไฟล์ของเพื่อนที่เราสร้างเตรียมไว้

# สร้างตารางในฐานข้อมูล
Base.metadata.create_all(bind=engine)

app = FastAPI(title="UBU RentCar OOP")

# เปิดใช้งาน Session (สำคัญมากสำหรับ Login และ Flash)
app.add_middleware(SessionMiddleware, secret_key="super-secret-ubu-key")

templates = Jinja2Templates(directory="app/templates")

# ประกอบร่าง Router
app.include_router(auth_web.router)
app.include_router(vehicle_web.router) # เพิ่มของเพื่อนเข้ามา

# ระบบจัดการ Exception (เมื่อยามเฝ้าประตูสั่งเด้งหน้าเว็บ)
@app.exception_handler(StarletteHTTPException)
# 2. เปลี่ยนชื่อฟังก์ชันนิดหน่อยเพื่อไม่ให้ชื่อไปซ้ำกับตัวที่ import เข้ามา
async def custom_http_exception_handler(request: Request, exc: StarletteHTTPException):
    if exc.status_code == 303:
        return RedirectResponse(url=exc.headers.get("Location"))
    
    # 3. แก้ไขบรรทัดนี้: ให้เรียกใช้ http_exception_handler ที่ import มาแทน
    return await http_exception_handler(request, exc)

# หน้าแรกสุดของเว็บไซต์
@app.get("/")
async def read_root(request: Request):
    messages = get_flashed_messages(request)
    return templates.TemplateResponse(
        "index.html", 
        {
            "request": request, 
            "messages": messages, 
            "current_user": request.session.get("username"),
            "user_role": request.session.get("role")
        }
    )