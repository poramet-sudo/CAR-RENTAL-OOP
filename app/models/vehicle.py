from abc import ABC, abstractmethod

# ==========================================
# 4 เสาหลัก OOP และ SOLID ที่แสดงในโค้ดนี้:
# 1. Abstraction: คลาส Vehicle เป็นแบบร่าง ซ่อนความซับซ้อนไว้
# 2. Inheritance: คลาสลูกรับคุณสมบัติ 'seats' และเมธอด 'seat_category' ไปใช้ได้ฟรีๆ
# 3. Encapsulation: ซ่อนตรรกะการคำนวณหมวดหมู่ที่นั่งไว้ภายใน ไม่ให้ระบบอื่นแก้ได้โดยตรง
# 4. Single Responsibility Principle (SRP): คลาสรับผิดชอบการคำนวณหมวดหมู่ของตัวเอง
# ==========================================

class Vehicle(ABC):
    # เลื่อน seats เข้ามาในคลาสแม่ เพื่อลดการเขียนโค้ดซ้ำ (Clean Code)
    def __init__(self, vehicle_id: str, brand: str, model: str, year: int, base_price: float, transmission: str, seats: int):
        self.vehicle_id = vehicle_id
        self.brand = brand
        self.model = model
        self.year = year
        self.transmission = transmission
        self.seats = seats
        self._base_price = base_price 

    @property
    def full_name(self) -> str:
        return f"{self.brand} {self.model} {self.year}"

    # Encapsulation: ทำตรรกะจัดกลุ่มที่นั่งไว้ในนี้ หน้าเว็บมีหน้าที่แค่นำไปแสดงผล (SRP)
    @property
    def seat_category(self) -> str:
        if self.seats <= 3:
            return "1-3"
        elif self.seats <= 6:
            return "4-6"
        else:
            return "7-11"

    # Polymorphism: บังคับให้คลาสลูกต้องมีเมธอดเหล่านี้
    @abstractmethod
    def get_details(self) -> dict:
        pass

    @abstractmethod
    def calculate_price(self) -> float:
        pass

# Inheritance: รถตู้สืบทอดจาก Vehicle
class VanWithDriver(Vehicle):
    def __init__(self, vehicle_id: str, brand: str, model: str, year: int, base_price: float, seats: int, driver_fee: float, transmission: str):
        # ส่ง seats ขึ้นไปให้คลาสแม่จัดการ
        super().__init__(vehicle_id, brand, model, year, base_price, transmission, seats)
        self.driver_fee = driver_fee
        self.vehicle_type = "รถตู้ (พร้อมคนขับ)"

    def calculate_price(self) -> float:
        return self._base_price + self.driver_fee

    def get_details(self) -> dict:
        return {
            "id": self.vehicle_id,
            "name": self.full_name,
            "type": self.vehicle_type,
            "seats": self.seats,
            "seat_category": self.seat_category, # ส่งข้อมูลหมวดหมู่ที่นั่งออกไปให้ UI
            "transmission": self.transmission,
            "price": self.calculate_price(),
            "features": ["เบาะ VIP", "แอร์ไมโครบัส", "รวมน้ำมัน"]
        }

# Inheritance: รถเก๋งสืบทอดจาก Vehicle
class CarWithDriver(Vehicle):
    def __init__(self, vehicle_id: str, brand: str, model: str, year: int, base_price: float, seats: int, driver_fee: float, transmission: str):
        super().__init__(vehicle_id, brand, model, year, base_price, transmission, seats)
        self.driver_fee = driver_fee
        self.vehicle_type = "รถเก๋ง (พร้อมคนขับ)"

    def calculate_price(self) -> float:
        return self._base_price + self.driver_fee

    def get_details(self) -> dict:
        return {
            "id": self.vehicle_id,
            "name": self.full_name,
            "type": self.vehicle_type,
            "seats": self.seats,
            "seat_category": self.seat_category, # ส่งข้อมูลหมวดหมู่ที่นั่งออกไปให้ UI
            "transmission": self.transmission,
            "price": self.calculate_price(),
            "features": ["ประหยัดน้ำมัน", "นั่งสบาย", "คนขับสุภาพ"]
        }