from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from app.models.vehicle import VanWithDriver, CarWithDriver

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")

@router.get("/search")
async def search_vehicles(request: Request):
    # ข้อมูลรถทั้งหมด 20 คัน (Van = รถตู้, Car = รถเก๋ง/SUV/Eco Car)
    vehicles = [
        # --- กลุ่มรถตู้ (Van) 7-11 ที่นั่ง ---
        VanWithDriver(vehicle_id="V01", brand="Toyota", model="Commuter", year=2020, base_price=1500, seats=10, driver_fee=700, transmission="ธรรมดา"),
        VanWithDriver(vehicle_id="V02", brand="Toyota", model="Majesty", year=2022, base_price=2000, seats=8, driver_fee=800, transmission="อัตโนมัติ"),
        VanWithDriver(vehicle_id="V03", brand="Hyundai", model="Staria", year=2023, base_price=2200, seats=11, driver_fee=800, transmission="อัตโนมัติ"),
        VanWithDriver(vehicle_id="V04", brand="Toyota", model="Commuter", year=2018, base_price=1400, seats=10, driver_fee=700, transmission="ธรรมดา"),
        VanWithDriver(vehicle_id="V05", brand="Hyundai", model="H-1", year=2020, base_price=1800, seats=11, driver_fee=700, transmission="อัตโนมัติ"),
        VanWithDriver(vehicle_id="V06", brand="Toyota", model="Alphard", year=2023, base_price=3500, seats=7, driver_fee=1000, transmission="อัตโนมัติ"),
        VanWithDriver(vehicle_id="V07", brand="Toyota", model="Commuter", year=2021, base_price=1600, seats=10, driver_fee=700, transmission="อัตโนมัติ"),
        VanWithDriver(vehicle_id="V08", brand="Toyota", model="Ventury", year=2019, base_price=1500, seats=11, driver_fee=700, transmission="อัตโนมัติ"),
        
        # --- กลุ่มรถเก๋ง/SUV (Car) 4-6 ที่นั่ง ---
        CarWithDriver(vehicle_id="C01", brand="Toyota", model="Camry", year=2021, base_price=1200, seats=4, driver_fee=500, transmission="อัตโนมัติ"),
        CarWithDriver(vehicle_id="C02", brand="Honda", model="Accord", year=2022, base_price=1300, seats=4, driver_fee=500, transmission="อัตโนมัติ"),
        CarWithDriver(vehicle_id="C03", brand="Mazda", model="3", year=2021, base_price=1000, seats=4, driver_fee=500, transmission="อัตโนมัติ"),
        CarWithDriver(vehicle_id="C04", brand="Toyota", model="Altis", year=2019, base_price=800, seats=4, driver_fee=500, transmission="อัตโนมัติ"),
        CarWithDriver(vehicle_id="C05", brand="Honda", model="Civic", year=2021, base_price=900, seats=4, driver_fee=500, transmission="อัตโนมัติ"),
        CarWithDriver(vehicle_id="C06", brand="Mazda", model="2", year=2022, base_price=700, seats=4, driver_fee=500, transmission="อัตโนมัติ"),
        CarWithDriver(vehicle_id="C07", brand="Toyota", model="Vios", year=2018, base_price=600, seats=4, driver_fee=500, transmission="ธรรมดา"),
        CarWithDriver(vehicle_id="C08", brand="Honda", model="City", year=2022, base_price=750, seats=4, driver_fee=500, transmission="อัตโนมัติ"),
        CarWithDriver(vehicle_id="C09", brand="Hyundai", model="Elantra", year=2019, base_price=850, seats=4, driver_fee=500, transmission="อัตโนมัติ"),
        CarWithDriver(vehicle_id="C10", brand="Mazda", model="CX-5", year=2021, base_price=1200, seats=4, driver_fee=600, transmission="อัตโนมัติ"),

        # --- กลุ่มรถขนาดเล็ก (Eco Car) 1-3 ที่นั่ง (เพิ่มใหม่ 2 คัน) ---
        CarWithDriver(vehicle_id="C11", brand="Honda", model="Brio", year=2022, base_price=500, seats=3, driver_fee=500, transmission="อัตโนมัติ"),
        CarWithDriver(vehicle_id="C12", brand="Mitsubishi", model="Mirage", year=2023, base_price=550, seats=3, driver_fee=500, transmission="อัตโนมัติ")
    ]
    
    # แปลง Object จาก OOP ให้กลายเป็น Dictionary เพื่อส่งไปแสดงผลที่ HTML
    vehicle_data = [v.get_details() for v in vehicles]

    return templates.TemplateResponse(
        "search_results.html", 
        {
            "request": request,
            "vehicles": vehicle_data,
            "current_user": request.session.get("username"),
            "user_role": request.session.get("role")
        }
    )