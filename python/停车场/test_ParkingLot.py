import unittest
from unittest import TestCase

from Car import Car
from ParkingLot import ParkingLot

class TestParkingLot(TestCase):

    def test_park_two_cars_should_get_different_tickets(self):
        parking_lot = ParkingLot(2)
        car1 = Car(car_number=1, car_owner='li', contact_way=172, car_color='b', car_model=3)
        car2 = Car(car_number=2, car_owner='zhang', contact_way=176, car_color='w', car_model=3)
        t1 = parking_lot.park_car(car1)
        t2 = parking_lot.park_car(car2)
        self.assertNotEquals(t1, t2)

    def test_when_park_car_and_parking_lot_is_full_should_get_exception(self):
        parking_lot = ParkingLot(1)
        car1 = Car(car_number=1, car_owner='li', contact_way=172, car_color='b', car_model=3)
        car2 = Car(car_number=2, car_owner='zhang', contact_way=176, car_color='w', car_model=3)
        parking_lot.park_car(car1)
        self.assertRaises(Exception, parking_lot.park_car(car2), "车库已满")

    def test_get_car(self):
        parking_lot = ParkingLot(1)
        car1 = Car(car_number=1, car_owner='li',contact_way=172, car_color='b',car_model=3)
        t1 = parking_lot.park_car(car1)
        taken_car1 = parking_lot.take_car(t1)
        self.assertEquals(car1, taken_car1)

    def test_get_car_with_wrong_ticket_should_get_exception(self):
        parking_lot = ParkingLot(1)
        car1 = Car(car_number=1, car_owner='li', contact_way=172, car_color='b', car_model=3)
        t1=parking_lot.park_car(car1)
        t2="wrongticket"
        self.assertRaises(Exception, parking_lot.take_car(t2),'停车票错误')

    def test_get_cars_when_a_car_is_taken_should_get_exception(self):
        parking_lot = ParkingLot(1)
        car = Car(car_number=1, car_owner='li',contact_way=172, car_color='b',car_model=3)
        t = parking_lot.park_car(car)
        parking_lot.take_car(t)
        self.assertRaises(Exception, parking_lot.take_car(t),"停车票错误")


if __name__ == '__main__':
    unittest.main()