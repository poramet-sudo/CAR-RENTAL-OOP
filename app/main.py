from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

# สร้างตัวแอปพลิเคชัน FastAPI
app = FastAPI(title="Car Rental API", description="ระบบเช่ารถยนต์ OOP")

# ตั้งค่าให้ FastAPI รู้จักโฟลเดอร์ templates (หน้าเว็บ HTML)
templates = Jinja2Templates(directory="app/templates")

# (ทางเลือก) ตั้งค่าให้รู้จักโฟลเดอร์ static สำหรับไฟล์ CSS/รูปภาพ
# app.mount("/static", StaticFiles(directory="app/static"), name="static")

# ==========================================
# ส่วนหน้าบ้าน (Frontend - Web UI)
# ==========================================
@app.get("/")
async def read_root(request: Request):
    # ส่งหน้าเว็บ index.html กลับไปให้ผู้ใช้พร้อมข้อมูลเบื้องต้น
    return templates.TemplateResponse(
        "index.html", 
        {"request": request, "title": "ระบบเช่ารถออนไลน์"}
    )

# ==========================================
# ส่วนหลังบ้าน (Backend - API)
# ==========================================
@app.get("/api/health")
async def health_check():
    # API สำหรับเช็คว่าระบบหลังบ้านทำงานปกติไหม
    return {"status": "ok", "message": "API ระบบเช่ารถทำงานปกติ"}